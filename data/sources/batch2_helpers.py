"""Shared helpers for writing example pairs (used by batch 2 onward)."""
import json
from pathlib import Path


def L(kind, text, picture=""):
    return {"kind": kind, "text": text, "picture": picture}


def P(topic, *lines):
    return {"topic": topic, "lines": list(lines)}


T = lambda t, p="": L("text", t, p)
S = lambda t, p="": L("step", t, p)
C = lambda t, p="": L("checkbox", t, p)
B = lambda t, p="": L("blank", t, p)
PH = lambda t, p="phone": L("phone", t, p)
CR = lambda t, p="ambulance": L("crisis", t, p)


def pair(pid, lang, doc_type, source, original, title, pages, notes=()):
    return {
        "id": pid, "language": lang, "doc_type": doc_type, "split": "train",
        "provenance": "made-up (written for this project)", "license": "CC BY 4.0 (project-authored)",
        "slp_reviewed": False, "source": source, "original": original,
        "target": {"title": title, "language": lang, "source": source, "pages": pages,
                   "notes_for_reviewer": list(notes)},
    }


def mark_reviewed(pairs, reviewer, date):
    """Record SLP approval for every pair in a batch."""
    for p in pairs:
        p.update({"slp_reviewed": True, "reviewed_by": reviewer, "review_date": date})


def write(pairs, filename):
    out = Path(__file__).resolve().parent.parent / "pairs" / filename
    with out.open("w", encoding="utf-8") as fh:
        for p in pairs:
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")
    print(f"Wrote {len(pairs)} pairs to {out}")
