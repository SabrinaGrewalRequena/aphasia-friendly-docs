"""Check every example pair: structure, fact check (original vs. target) and format score.

Usage:
    python check_pairs.py              # all pairs in data/pairs/
    python check_pairs.py --verbose    # also print every issue
"""
import argparse

import factcheck
import score
from common import ROOT, load_pairs, validate


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", default=str(ROOT / "data" / "pairs"))
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()
    pairs = load_pairs(a.pairs)
    bad = 0
    print(f"{'id':<34}{'lang':<6}{'facts':<8}{'grade':>6}{'pages':>7}{'format':>8}  reviewed")
    for p in pairs:
        problems = validate(p["target"])
        fc = factcheck.check(p["original"], p["target"])
        sc = score.score(p["target"])
        ok = not problems and fc["passed"]
        bad += not ok
        print(f"{p['id']:<34}{p.get('language', ''):<6}{'PASS' if fc['passed'] else 'FAIL':<8}"
              f"{sc['grade_level']:>6}{sc['pages']:>7}{len(sc['format_issues']):>8}  "
              f"{'yes' if p.get('slp_reviewed') else 'no'}")
        if a.verbose or not ok:
            for pr in problems:
                print("    structure:", pr)
            if not fc["passed"]:
                print("    " + factcheck.format_report(fc).replace("\n", "\n    "))
            if a.verbose:
                for i in sc["format_issues"]:
                    print("    format:", i)
    print(f"\n{len(pairs)} pairs, {bad} need fixing")
    return bad


if __name__ == "__main__":
    raise SystemExit(1 if main() else 0)
