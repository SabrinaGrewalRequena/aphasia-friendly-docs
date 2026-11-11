"""Check every example pair: structure, fact check (original vs. target) and format score.

Usage:
    python check_pairs.py              # all pairs in data/pairs/
    python check_pairs.py --verbose    # also print every issue
"""
import argparse
import datetime as dt
import re

import factcheck
import score
from common import ROOT, load_pairs, validate


EN_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ES_DAYS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
EN_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
             "October", "November", "December"]
ES_MONTHS = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
             "octubre", "noviembre", "diciembre"]


def weekday_errors(text):
    """Dates written with a weekday must fall on that weekday."""
    errs = []
    for d, m, day, y in re.findall(rf"({'|'.join(EN_DAYS)}),? ({'|'.join(EN_MONTHS)}) (\d{{1,2}}),? (\d{{4}})", text):
        real = EN_DAYS[dt.date(int(y), EN_MONTHS.index(m) + 1, int(day)).weekday()]
        if real != d:
            errs.append(f"{d}, {m} {day}, {y} is really a {real}")
    for d, day, m, y in re.findall(rf"({'|'.join(ES_DAYS)}),? (\d{{1,2}}) de ({'|'.join(ES_MONTHS)}) de (\d{{4}})", text, re.I):
        real = ES_DAYS[dt.date(int(y), ES_MONTHS.index(m.lower()) + 1, int(day)).weekday()]
        if real != d.lower():
            errs.append(f"{d} {day} de {m} de {y} es {real}")
    return errs


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
        wd = weekday_errors(p["original"])
        ok = not problems and fc["passed"] and not wd
        bad += not ok
        print(f"{p['id']:<34}{p.get('language', ''):<6}{'PASS' if fc['passed'] else 'FAIL':<8}"
              f"{sc['grade_level']:>6}{sc['pages']:>7}{len(sc['format_issues']):>8}  "
              f"{'yes' if p.get('slp_reviewed') else 'no'}")
        if a.verbose or not ok:
            for pr in problems:
                print("    structure:", pr)
            for w in wd:
                print("    date:", w)
            if not fc["passed"]:
                print("    " + factcheck.format_report(fc).replace("\n", "\n    "))
            if a.verbose:
                for i in sc["format_issues"]:
                    print("    format:", i)
    print(f"\n{len(pairs)} pairs, {bad} need fixing")
    return bad


if __name__ == "__main__":
    raise SystemExit(1 if main() else 0)
