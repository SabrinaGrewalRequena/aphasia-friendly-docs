"""Fact check: every name, date, time, dose, address, phone number, email and
website in the original must appear unchanged in the aphasia-friendly version,
and the new version must not contain numbers that were not in the original.

Usage:
    python factcheck.py original.txt output.json [--keep "Duke Clinic" --keep "Dr. Lee"]
"""
import argparse
import json
import re
import sys

from common import all_lines, output_text, read_document, strip_md

MONTHS_EN = r"(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)\.?"
MONTHS_ES = r"(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)"
DAYS = r"(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|lunes|martes|miércoles|jueves|viernes|sábado|domingo)"
UNITS = (r"(?:mg|mcg|µg|g|mL|ml|L|units?|unidades|IU|tablets?|tabletas?|pills?|pastillas?|"
         r"capsules?|cápsulas?|puffs?|inhalaciones|drops?|gotas|teaspoons?|tsp|cucharaditas?|"
         r"tablespoons?|tbsp|cucharadas?|patch(?:es)?|parches?)")
STREET = (r"(?:Street|St\.?|Avenue|Ave\.?|Road|Rd\.?|Boulevard|Blvd\.?|Drive|Dr\.?|Lane|Ln\.?|"
          r"Way|Court|Ct\.?|Parkway|Pkwy\.?|Place|Pl\.?|Highway|Hwy\.?)")

PATTERNS = {
    "phone": r"(?:\+?1[\s.-]?)?\(?\b\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b|\b(?:911|988|711|211)\b",
    "email": r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b",
    "website": r"\b(?:https?://|www\.)[^\s)<>]+|(?<![@\w.-])[\w-]+\.(?:org|gov|com|net|edu)(?:/[^\s)<>]*)?",
    "date": (rf"\b{DAYS},?\s+{MONTHS_EN}\s+\d{{1,2}}(?:,\s*\d{{4}})?|\b{MONTHS_EN}\s+\d{{1,2}}(?:st|nd|rd|th)?(?:,\s*\d{{4}})?"
             rf"|\b\d{{1,2}}\s+de\s+{MONTHS_ES}(?:\s+de\s+\d{{4}})?|\b\d{{1,2}}/\d{{1,2}}(?:/\d{{2,4}})?\b"),
    "time": r"\b\d{1,2}(?::\d{2})?\s*(?:a\.?\s?m\.?|p\.?\s?m\.?|AM|PM)(?=\W|$)|\b\d{1,2}:\d{2}\b",
    "dose": rf"\b\d+(?:[.,]\d+)?\s*{UNITS}\b",
    "name": r"\b(?:Dr|Dra|Mr|Mrs|Ms|Sr|Sra|Srta)\.\s+[A-ZÁÉÍÓÚÑ][\w'’-]+(?:\s+[A-ZÁÉÍÓÚÑ][\w'’-]+)?",
    "address": rf"\b\d{{1,6}}\s+(?:[A-Z0-9][\w.'-]*\s+){{1,4}}{STREET}(?:,?\s+(?:Suite|Ste\.?|Room|Rm\.?)\s*\w+)?|\b(?:Calle|Avenida|Av\.)\s+[\wÁÉÍÓÚÑáéíóúñ ]+?\s+\d+",
}
CRISIS_NUMBERS = ("911", "988")


def norm(s):
    s = s.lower().replace("’", "'")
    s = re.sub(r"\b([ap])\.?\s?m\.?", r"\1m", s)
    return re.sub(r"\s+", " ", s).strip()


def digits(s):
    return re.sub(r"\D", "", s)


def extract_facts(text, keep=()):
    facts, seen = [], set()
    for kind, pat in PATTERNS.items():
        for m in re.finditer(pat, text, flags=re.IGNORECASE if kind in ("date", "dose", "time") else 0):
            val = m.group(0).strip().rstrip(".,;")
            key = (kind, norm(val))
            if key not in seen:
                seen.add(key)
                facts.append({"type": kind, "value": val})
    for k in keep:
        if (("keep", norm(k))) not in seen:
            facts.append({"type": "keep", "value": k})
    return facts


def number_tokens(text):
    """Numbers in text, ignoring step labels like '1.' or 'Step 2' at the start of a line."""
    text = re.sub(r"(?m)^\s*(?:step|paso)?\s*\d{1,2}[.)]\s", " ", text, flags=re.IGNORECASE)
    return re.findall(r"\d[\d,.:/-]*\d|\d", text)


def check(original, out_doc, keep=()):
    out_text = output_text(out_doc)
    out_norm, out_digits = norm(out_text), digits(out_text)
    omitted_norm = norm(" ".join(out_doc.get("omitted") or []))
    results = []
    for f in extract_facts(original, keep):
        v = f["value"]
        if norm(v) in out_norm:
            status = "ok"
        elif f["type"] in ("phone", "date", "time", "dose") and digits(v) and digits(v) in out_digits:
            status = "reformatted"
        elif norm(v) in omitted_norm and v not in CRISIS_NUMBERS:
            status = "omitted"          # left out on purpose and listed with a reason
        else:
            status = "missing"
        results.append({**f, "status": status})

    # Numbers that appear in the output but nowhere in the original = possible invented facts
    orig_digit_runs = set(re.findall(r"\d+", original))
    added = sorted({tok for tok in number_tokens(out_text)
                    if not all(run in orig_digit_runs for run in re.findall(r"\d+", tok))})

    crisis = []
    for num in CRISIS_NUMBERS:
        if re.search(rf"\b{num}\b", original):
            on_crisis_line = any(line.get("kind") == "crisis" and num in line.get("text", "")
                                 for _, line in all_lines(out_doc))
            if not on_crisis_line:
                crisis.append(f"{num} is in the original but not on its own 'crisis' line")

    passed = all(r["status"] in ("ok", "omitted") for r in results) and not added and not crisis
    return {"passed": passed, "facts": results, "added_numbers": added, "crisis_issues": crisis}


def format_report(rep):
    lines = ["FACT CHECK: " + ("PASS" if rep["passed"] else "NEEDS REVIEW")]
    for r in rep["facts"]:
        mark = {"ok": "  ok ", "omitted": "  -- ", "reformatted": "  ~~ ", "missing": "  XX "}[r["status"]]
        lines.append(f"{mark}{r['type']:<8} {r['value']}" + ("" if r["status"] == "ok" else f"   <- {r['status']}"))
    for a in rep["added_numbers"]:
        lines.append(f"  !! number not in original: {a}")
    for c in rep["crisis_issues"]:
        lines.append(f"  !! {c}")
    return "\n".join(lines)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("original")
    ap.add_argument("output_json")
    ap.add_argument("--keep", action="append", default=[], help="extra text that must appear exactly (clinic names etc.)")
    a = ap.parse_args()
    with open(a.output_json, encoding="utf-8") as fh:
        report = check(read_document(a.original), json.load(fh), a.keep)
    print(format_report(report))
    sys.exit(0 if report["passed"] else 1)
