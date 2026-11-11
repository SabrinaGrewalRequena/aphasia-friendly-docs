"""Readability and format scoring for an aphasia-friendly output.

Usage:
    python score.py output.json
"""
import argparse
import json
import re

from common import all_lines, strip_md

CONNECTORS = {"de", "del", "la", "las", "el", "los", "en", "y", "para", "of", "the", "and", "for", "in"}
READ_KINDS = {"text", "step", "checkbox"}   # phone/crisis/blank lines are not prose
PHONE_RE = re.compile(r"\(?\b\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b|\b(?:911|988)\b")


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", text) if s.strip()]


def words(text):
    return re.findall(r"[\wÁÉÍÓÚÑáéíóúñü'’-]+", text)


def syllables(word, lang):
    """Rough syllable count from vowel groups (no downloads needed)."""
    w = word.lower()
    vowels = "aeiouyáéíóúü" if lang != "es" else "aeiouáéíóúü"
    n = len(re.findall(f"[{vowels}]+", w))
    if lang != "es" and w.endswith("e") and not w.endswith(("le", "ee")) and n > 1:
        n -= 1                      # silent final e
    return max(n, 1)


def grade_level(text, lang):
    """English: Flesch-Kincaid grade. Spanish: Crawford (years of schooling)."""
    sents = sentences(text)
    ws = [w for w in words(text) if not w.isdigit()]
    if not sents or not ws:
        return 0.0
    syl = sum(syllables(w, lang) for w in ws)
    if lang == "es":
        g = -0.205 * (100 * len(sents) / len(ws)) + 0.049 * (100 * syl / len(ws)) - 3.407
    else:
        g = 0.39 * (len(ws) / len(sents)) + 11.8 * (syl / len(ws)) - 15.59
    return round(max(g, 0.0), 1)


def score(doc, max_grade=5, max_lines=4, max_words=15):
    lang = doc.get("language", "en")
    # Names and copied facts (bold text with a capital letter or a digit, e.g. "**Atorvastatin 40 mg**",
    # "**Carolina Valley Medical Center**") cannot be simplified, so the grade leaves them out.
    prose = [strip_md(re.sub(r"\*\*([^*]*[A-Z0-9ÁÉÍÓÚÑ][^*]*)\*\*", "", l["text"]))
             for _, l in all_lines(doc) if l.get("kind") in READ_KINDS]
    prose_text = "\n".join(prose)
    sents = [s for p in prose for s in sentences(p)]
    sent_lens = [len(words(s)) for s in sents] or [0]

    issues = []
    pages = doc.get("pages", [])
    for i, page in enumerate(pages, 1):
        lines = page.get("lines", [])
        limit = 6 if lines and all(l.get("kind") in ("checkbox", "blank") for l in lines) else max_lines
        if len(lines) > limit:
            issues.append(f"page {i}: {len(lines)} lines (max {limit})")
        for j, line in enumerate(lines, 1):
            t, kind = line.get("text", ""), line.get("kind")
            n = len(words(strip_md(t)))
            if kind in READ_KINDS and n > max_words:
                issues.append(f"page {i} line {j}: {n} words (max {max_words})")
            if kind in ("text", "step") and "**" not in t:
                issues.append(f"page {i} line {j}: no bold key word")
            if kind in ("text", "step", "checkbox") and PHONE_RE.search(t):
                issues.append(f"page {i} line {j}: phone number should be on its own phone/crisis line")
            if kind in READ_KINDS and not line.get("picture"):
                issues.append(f"page {i} line {j}: no picture suggested")
            # bolded facts (numbers, names, emails) don't count as "too much bold"
            bolds = [b for b in re.findall(r"\*\*(.+?)\*\*", t)
                     if not re.search(r"[\d@]", b)
                     and not all(w[:1].isupper() for w in words(b) if w.lower() not in CONNECTORS)]
            fact_line = re.fullmatch(r"\*\*[^*]+\*\*\.?", t.strip())   # e.g. a date or address alone
            if bolds and not fact_line and sum(len(words(b)) for b in bolds) > max(4, n // 2):
                issues.append(f"page {i} line {j}: too much bold")
    has_contact = any(l.get("kind") in ("phone", "crisis") for _, l in all_lines(doc))
    if pages and has_contact:
        last_kinds = {l.get("kind") for l in pages[-1].get("lines", [])}
        if not last_kinds & {"phone", "crisis"}:
            issues.append("last page has no phone/contact line (should end with who can help)")

    grade = grade_level(prose_text, lang)
    return {
        "language": lang,
        "pages": len(pages),
        "lines": sum(len(p.get("lines", [])) for p in pages),
        "grade_level": grade,
        "grade_ok": grade <= max_grade,
        "avg_sentence_words": round(sum(sent_lens) / len(sent_lens), 1),
        "max_sentence_words": max(sent_lens),
        "format_issues": issues,
    }


def format_report(s):
    out = [f"READABILITY: grade {s['grade_level']} ({'OK' if s['grade_ok'] else 'TOO HIGH'}), "
           f"avg {s['avg_sentence_words']} words/sentence, longest {s['max_sentence_words']}, "
           f"{s['pages']} pages / {s['lines']} lines",
           f"FORMAT: {'OK' if not s['format_issues'] else str(len(s['format_issues'])) + ' issue(s)'}"]
    out += [f"  - {i}" for i in s["format_issues"]]
    return "\n".join(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("output_json")
    a = ap.parse_args()
    with open(a.output_json, encoding="utf-8") as fh:
        print(format_report(score(json.load(fh))))
