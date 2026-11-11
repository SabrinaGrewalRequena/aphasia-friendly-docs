"""Step 5: test and compare systems on documents they have not seen.

1) Run the baseline on every test document:
     python evaluate.py run data/test.jsonl results/baseline
   (same --backend/--model/--base-url options as convert.py, e.g. to run your
    fine-tuned model through Ollama)

2) Put the fine-tuned model's outputs (from the Colab notebook) in results/finetuned/
   as <id>.json files.

3) Compare:
     python evaluate.py compare data/test.jsonl results/baseline results/finetuned

This prints a summary table and writes:
   results/summary.csv          one row per document per system
   results/slp_review_sheet.csv blinded sheet for your SLP (systems hidden as A/B)
   results/slp_key.csv          which code is which system (do not give to the SLP)
   results/review/<code>.html   printable handouts for the SLP, named by code
"""
import argparse
import csv
import json
import random
import sys
from pathlib import Path

import factcheck
import render
import score
from common import ROOT, parse_model_json, validate
from convert import build_messages, call_anthropic, call_openai_compatible, load_examples


def load_tests(path):
    return [json.loads(l) for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip()]


def cmd_run(a):
    system = (ROOT / "prompts" / "system.md").read_text(encoding="utf-8")
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for t in load_tests(a.test):
        target = out / f"{t['id']}.json"
        if target.exists():
            print(f"skip {t['id']} (already done)")
            continue
        ex = load_examples(t.get("language", "en"), a.examples, a.pairs, exclude_text=t["original"])
        msgs = build_messages(t["original"], t.get("source", t["id"]), None, ex)
        raw = (call_anthropic(system, msgs, a.model) if a.backend == "anthropic"
               else call_openai_compatible(system, msgs, a.model, a.base_url))
        try:
            target.write_text(json.dumps(parse_model_json(raw), ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"done {t['id']}")
        except Exception as e:
            (out / f"{t['id']}.raw.txt").write_text(raw, encoding="utf-8")
            print(f"FAILED {t['id']}: {e}")


def evaluate_one(test, path):
    if not path.exists():
        return {"valid_json": False, "note": "missing output"}
    try:
        doc = parse_model_json(path.read_text(encoding="utf-8"))
    except Exception as e:
        return {"valid_json": False, "note": f"bad JSON: {e}"}
    fc = factcheck.check(test["original"], doc)
    sc = score.score(doc)
    return {"valid_json": not validate(doc), "doc": doc,
            "facts_pass": fc["passed"],
            "facts_missing": sum(f["status"] == "missing" for f in fc["facts"]),
            "facts_reformatted": sum(f["status"] == "reformatted" for f in fc["facts"]),
            "added_numbers": len(fc["added_numbers"]),
            "crisis_issues": len(fc["crisis_issues"]),
            "grade": sc["grade_level"], "grade_ok": sc["grade_ok"],
            "pages": sc["pages"], "format_issues": len(sc["format_issues"]), "note": ""}


def cmd_compare(a):
    tests = load_tests(a.test)
    systems = [Path(d) for d in a.dirs]
    res_dir = Path(a.results)
    rows = []
    for t in tests:
        for sysdir in systems:
            r = evaluate_one(t, sysdir / f"{t['id']}.json")
            rows.append({"id": t["id"], "language": t.get("language"), "doc_type": t.get("doc_type"),
                         "system": sysdir.name, **{k: v for k, v in r.items() if k != "doc"}, "_doc": r.get("doc")})

    cols = ["id", "language", "doc_type", "system", "valid_json", "facts_pass", "facts_missing",
            "facts_reformatted", "added_numbers", "crisis_issues", "grade", "grade_ok", "pages", "format_issues", "note"]
    res_dir.mkdir(parents=True, exist_ok=True)
    with open(res_dir / "summary.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    print(f"{'system':<16}{'docs':>6}{'valid':>8}{'facts 100%':>12}{'grade<=5':>10}{'avg grade':>11}{'fmt issues':>12}")
    for sysdir in systems:
        rs = [r for r in rows if r["system"] == sysdir.name]
        ok = [r for r in rs if r.get("valid_json")]
        pct = lambda n: f"{100 * n / len(rs):.0f}%" if rs else "-"
        avg = lambda k: f"{sum(r[k] for r in ok) / len(ok):.1f}" if ok else "-"
        print(f"{sysdir.name:<16}{len(rs):>6}{pct(len(ok)):>8}{pct(sum(bool(r.get('facts_pass')) for r in rs)):>12}"
              f"{pct(sum(bool(r.get('grade_ok')) for r in rs)):>10}{avg('grade'):>11}{avg('format_issues'):>12}")
    print("\nTargets from the proposal: facts 100%, grade 5 or below, SLP 'usable' on 80%.")

    # Blinded SLP review pack
    rng = random.Random(7)
    review_dir = res_dir / "review"
    review_dir.mkdir(exist_ok=True)
    sheet, key = [], []
    for t in tests:
        cands = [r for r in rows if r["id"] == t["id"] and r.get("_doc")]
        rng.shuffle(cands)
        for letter, r in zip("ABCDEFGH", cands):
            code = f"{t['id']}-{letter}"
            (review_dir / f"{code}.html").write_text(render.render(r["_doc"]), encoding="utf-8")
            sheet.append({"code": code, "original_id": t["id"],
                          "accuracy_1to5": "", "usability (no edits / minor edits / major edits / not usable)": "",
                          "key_action_clear (yes/no)": "", "comments": ""})
            key.append({"code": code, "system": r["system"]})
    for name, data in (("slp_review_sheet.csv", sheet), ("slp_key.csv", key)):
        if data:
            with open(res_dir / name, "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=list(data[0].keys()))
                w.writeheader()
                w.writerows(data)
    print(f"Wrote {res_dir/'summary.csv'}, the blinded SLP review sheet and {len(sheet)} handouts in {review_dir}/")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("test")
    r.add_argument("out_dir")
    r.add_argument("--backend", choices=["anthropic", "openai"], default="anthropic")
    r.add_argument("--model", default="claude-sonnet-5-5")
    r.add_argument("--base-url", default="http://localhost:11434/v1")
    r.add_argument("--examples", type=int, default=2)
    r.add_argument("--pairs", default=str(ROOT / "data" / "pairs.jsonl"))
    c = sub.add_parser("compare")
    c.add_argument("test")
    c.add_argument("dirs", nargs="+")
    c.add_argument("--results", default="results")
    a = ap.parse_args()
    cmd_run(a) if a.cmd == "run" else cmd_compare(a)


if __name__ == "__main__":
    main()
