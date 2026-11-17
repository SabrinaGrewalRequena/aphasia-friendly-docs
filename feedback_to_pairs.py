"""Turn SLP reviews from the website (review mode) into training data.

Reviews are saved by the Hugging Face Space to a private dataset (FEEDBACK_REPO), as .jsonl files. Each
review has the original document, every version the model wrote (plus the SLP's edits, if any), which
version the SLP chose, and an optional rating and comment.

This script writes:
  data/pairs/feedback.jsonl   new training pairs: the version the SLP chose (with their edits) as the target.
                              build_dataset.py picks these up like any other pair.
  data/preferences.jsonl      "chosen vs. rejected" pairs (the SLP's choice vs. the other versions, and
                              edited vs. unedited), kept for preference training (DPO) later.

A review only becomes a training pair when the chosen handout still passes the fact check against the
original and the SLP did not mark it "not usable" - otherwise the model would learn a mistake.

Usage:
  python feedback_to_pairs.py feedback/data            # a folder of .jsonl files (or one file)
"""
import argparse
import json
import sys
from pathlib import Path

import factcheck
from common import ROOT, validate
from convert import user_message

SYSTEM = (ROOT / "prompts" / "system_short.md").read_text(encoding="utf-8").strip()


def read_reviews(path):
    p = Path(path)
    files = sorted(p.rglob("*.jsonl")) if p.is_dir() else [p]
    for f in files:
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    print(f"skipped a broken line in {f.name}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("reviews", help="folder (or file) of review .jsonl files downloaded from the feedback dataset")
    ap.add_argument("--pairs-out", default=str(ROOT / "data" / "pairs" / "feedback.jsonl"))
    ap.add_argument("--prefs-out", default=str(ROOT / "data" / "preferences.jsonl"))
    a = ap.parse_args()

    pairs, prefs, seen, notes = [], [], set(), []
    reviews = list(read_reviews(a.reviews))
    for r in reviews:
        rid = str(r.get("id", ""))[:10] or str(len(pairs))
        versions, original = r.get("versions") or [], (r.get("original") or "").strip()
        try:
            chosen_i = int(r.get("chosen") or 0)
            chosen = versions[chosen_i]
        except (ValueError, IndexError, TypeError):
            notes.append(f"{rid}: no valid chosen version"); continue
        target = chosen.get("edited") or chosen.get("model")
        if not original or not isinstance(target, dict):
            notes.append(f"{rid}: missing document or handout"); continue
        lang = r.get("lang") or None
        prompt = user_message(original, r.get("source") or "Uploaded document", lang)

        # Preference pairs: the chosen handout beats every other version, and beats its own unedited form.
        rejected = [v.get("model") for i, v in enumerate(versions) if i != chosen_i]
        if chosen.get("edited"):
            rejected.append(chosen.get("model"))
        for rej in rejected:
            if isinstance(rej, dict) and rej != target:
                prefs.append({"review": rid, "prompt": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
                              "chosen": [{"role": "assistant", "content": json.dumps(target, ensure_ascii=False)}],
                              "rejected": [{"role": "assistant", "content": json.dumps(rej, ensure_ascii=False)}]})

        # Training pair: only good, fact-checked handouts.
        if r.get("rating") == "not_usable":
            notes.append(f"{rid}: rated not usable (kept only as a preference pair)"); continue
        problems = validate(target)
        if problems:
            notes.append(f"{rid}: handout format problem ({problems[0]})"); continue
        if not factcheck.check(original, target)["passed"]:
            notes.append(f"{rid}: chosen handout fails the fact check (kept only as a preference pair)"); continue
        key = (original, json.dumps(target, sort_keys=True))
        if key in seen:
            continue
        seen.add(key)
        pair = {"id": f"feedback-{rid}", "language": target.get("language") or "en", "doc_type": "feedback", "split": "train",
                "provenance": "SLP review on the website (review mode)", "license": "CC BY 4.0 (project-authored)",
                "slp_reviewed": True, "reviewed_by": "SLP (website review mode)", "review_date": (r.get("received") or "")[:10],
                "source": r.get("source") or "Uploaded document", "original": original, "target": target,
                "edited_by_slp": bool(chosen.get("edited")), "rating": r.get("rating"), "comment": r.get("comment")}
        if lang:
            pair["target_language"] = lang
        pairs.append(pair)

    for path, rows in ((a.pairs_out, pairs), (a.prefs_out, prefs)):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"{len(reviews)} reviews -> {len(pairs)} training pairs ({a.pairs_out})")
    print(f"           -> {len(prefs)} preference pairs ({a.prefs_out})")
    for n in notes:
        print("  note:", n)


if __name__ == "__main__":
    main()
