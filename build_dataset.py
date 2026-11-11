"""Turn the pairs in data/pairs/ into training files for fine-tuning (Step 4).

Writes:
  data/train.jsonl  chat-format examples for the Colab notebook
  data/test.jsonl   held-out documents the model never trains on (for Step 5)

A pair is held out when its "split" is "test". If no pair is marked "test",
about 15% are held out at random (fixed seed), split by document type and language.

Usage:
  python build_dataset.py                 # all pairs
  python build_dataset.py --reviewed-only # only pairs your SLP has approved (recommended for the real run)
"""
import argparse
import json
import random
from collections import defaultdict
from pathlib import Path

from common import ROOT, load_pairs, validate
from convert import user_message
import factcheck


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pairs", default=str(ROOT / "data" / "pairs"))
    ap.add_argument("--reviewed-only", action="store_true")
    ap.add_argument("--test-share", type=float, default=0.15)
    a = ap.parse_args()

    system = (ROOT / "prompts" / "system_short.md").read_text(encoding="utf-8").strip()
    pairs = load_pairs(a.pairs)

    kept, skipped = [], []
    for p in pairs:
        why = validate(p["target"])
        if a.reviewed_only and not p.get("slp_reviewed"):
            why.append("not SLP-reviewed")
        if not factcheck.check(p["original"], p["target"])["passed"]:
            why.append("fails fact check (fix the target, or the training data teaches mistakes)")
        (skipped if why else kept).append((p, why))

    if not any(p.get("split") == "test" for p, _ in kept):
        rng = random.Random(42)
        groups = defaultdict(list)
        for p, _ in kept:
            groups[(p.get("doc_type"), p.get("language"))].append(p)
        for g in groups.values():
            rng.shuffle(g)
            for p in g[:round(len(g) * a.test_share)]:
                p["split"] = "test"
        # small groups round down to 0, so top up to the overall share
        rest = [p for p, _ in kept if p.get("split") != "test"]
        rng.shuffle(rest)
        need = round(len(kept) * a.test_share) - sum(p.get("split") == "test" for p, _ in kept)
        for p in rest[:max(need, 0)]:
            p["split"] = "test"

    train, test = [], []
    for p, _ in kept:
        if p.get("split") == "test":
            test.append({"id": p["id"], "language": p.get("language"), "doc_type": p.get("doc_type"),
                         "source": p.get("source", ""), "original": p["original"], "reference": p["target"]})
        else:
            train.append({"messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user_message(p["original"], p.get("source", ""), None)},
                {"role": "assistant", "content": json.dumps(p["target"], ensure_ascii=False)}]})

    for name, rows in (("train", train), ("test", test)):
        with open(ROOT / "data" / f"{name}.jsonl", "w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"{len(train)} training examples -> data/train.jsonl")
    print(f"{len(test)} test documents    -> data/test.jsonl")
    for p, why in skipped:
        print(f"skipped {p['id']}: {'; '.join(why)}")
    if len(train) < 100:
        print(f"\nNote: {len(train)} training examples is a small set. Aim for 150+ before trusting the fine-tune.")


if __name__ == "__main__":
    main()
