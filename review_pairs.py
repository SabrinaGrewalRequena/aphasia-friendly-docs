"""Make a review book for you and your SLP: every example pair side by side
(original on the left, aphasia-friendly pages on the right), plus a checklist.

Usage:
    python review_pairs.py                     # all pairs not yet SLP-reviewed
    python review_pairs.py --all               # every pair
    python review_pairs.py --batch batch3      # only files in data/pairs/ whose name contains "batch3"
Writes:
    review/review_book.html       open in a browser, or print
    review/review_checklist.csv   one row per pair for approve / changes needed
"""
import argparse
import csv
import html
import re
from pathlib import Path

import factcheck
import score
from common import ROOT, load_pairs

KIND_MARK = {"checkbox": "☐ ", "step": "", "phone": "☎ ", "crisis": "⚠ ", "blank": "", "text": ""}

CSS = """
:root { --bg:#f4f4f2; --card:#fff; --ink:#1b1b1b; --muted:#666; --line:#ddd; --ok:#2e7d32; --warn:#b26a00; --bad:#b00020; }
@media (prefers-color-scheme: dark) { :root { --bg:#161616; --card:#222; --ink:#eee; --muted:#aaa; --line:#3a3a3a; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font:15px/1.5 system-ui, -apple-system, Segoe UI, sans-serif; }
header { padding:24px 16px 8px; max-width:1200px; margin:auto; }
h1 { margin:0 0 4px; font-size:24px; }
.sub { color:var(--muted); }
.toc { max-width:1200px; margin:8px auto 16px; padding:0 16px; columns: 2 280px; }
.toc a { color:inherit; display:block; padding:2px 0; }
.pair { max-width:1200px; margin:0 auto 28px; padding:16px; background:var(--card); border:1px solid var(--line); border-radius:10px; }
.pair h2 { margin:0; font-size:19px; }
.meta { color:var(--muted); font-size:13px; margin:4px 0 10px; }
.badge { display:inline-block; padding:1px 8px; border-radius:20px; font-size:12px; font-weight:600; border:1px solid currentColor; margin-right:6px; }
.ok { color:var(--ok); } .warn { color:var(--warn); } .bad { color:var(--bad); }
.cols { display:grid; grid-template-columns: minmax(0,1fr) minmax(0,1.6fr); gap:16px; }
@media (max-width: 800px) { .cols { grid-template-columns: 1fr; } }
.orig { white-space:pre-wrap; background:var(--bg); border-radius:8px; padding:12px; font-size:14px; }
.pages { display:grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap:10px; }
.pg { border:1px solid var(--line); border-radius:8px; padding:10px; background:var(--card); }
.pg h3 { margin:0 0 6px; font-size:14px; border-bottom:2px solid var(--ink); padding-bottom:4px; }
.pg ol, .pg ul { margin:0; padding-left:18px; } .pg li { margin:4px 0; font-size:14px; }
.pg ul { list-style:none; padding-left:0; }
.pic { color:var(--muted); font-size:11px; }
.crisis { color:var(--bad); font-weight:700; }
.notes { margin:10px 0 0; padding:10px 12px; border-left:4px solid var(--warn); background:var(--bg); border-radius:4px; font-size:14px; }
.box { margin-top:10px; font-size:14px; }
.box span { display:inline-block; margin-right:18px; }
@media print { body { background:#fff; } .pair { break-inside: avoid-page; page-break-after: always; border:none; } .toc { display:none; } }
"""


def md(t):
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html.escape(t))


def page_html(page, start):
    items, n = [], start
    for line in page.get("lines", []):
        k = line.get("kind", "text")
        pic = f' <span class="pic">[{html.escape(line.get("picture") or "")}]</span>' if line.get("picture") else ""
        cls = ' class="crisis"' if k == "crisis" else ""
        if k == "step":
            n += 1
            items.append(f"<li{cls}>{n}. {md(line.get('text', ''))}{pic}</li>")
        else:
            items.append(f"<li{cls}>{KIND_MARK.get(k, '')}{md(line.get('text', ''))}{pic}</li>")
    return f'<div class="pg"><h3>{md(page.get("topic", ""))}</h3><ul>{"".join(items)}</ul></div>', n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", default=str(ROOT / "data" / "pairs"))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--batch", help="only pair files whose name contains this text")
    ap.add_argument("--out", default=str(ROOT / "review"))
    a = ap.parse_args()

    src = Path(a.pairs)
    files = [f for f in sorted(src.glob("*.jsonl")) if a.batch in f.name] if a.batch and src.is_dir() else [src]
    pairs = [p for f in files for p in load_pairs(f) if a.all or not p.get("slp_reviewed")]
    out = Path(a.out)
    out.mkdir(exist_ok=True)
    body, toc, rows = [], [], []
    for i, p in enumerate(pairs, 1):
        t = p["target"]
        fc = factcheck.check(p["original"], t)
        sc = score.score(t)
        fc_badge = '<span class="badge ok">facts ✓</span>' if fc["passed"] else '<span class="badge bad">facts ✗</span>'
        gr_badge = (f'<span class="badge {"ok" if sc["grade_ok"] else "warn"}">grade {sc["grade_level"]}</span>')
        pages, step = [], 0
        prev_last = None
        for pg in t.get("pages", []):
            lines = pg.get("lines", [])
            if not (lines and lines[0].get("kind") == "step" and prev_last == "step"):
                step = 0
            h, step = page_html(pg, step)
            prev_last = lines[-1].get("kind") if lines else None
            pages.append(h)
        notes = list(t.get("notes_for_reviewer") or []) + [f"Left out on purpose: {o}" for o in (t.get("omitted") or [])]
        notes_html = ("<div class='notes'><b>Please check:</b><ul>" + "".join(f"<li>{html.escape(n)}</li>" for n in notes)
                      + "</ul></div>") if notes else ""
        anchor = f"p{i}"
        toc.append(f'<a href="#{anchor}">{i}. {html.escape(t.get("title", p["id"]))} '
                   f'<span class="sub">({p.get("language", "")}, {html.escape(p.get("doc_type", ""))})</span></a>')
        body.append(f"""
<section class="pair" id="{anchor}">
  <h2>{i}. {html.escape(t.get('title', ''))}</h2>
  <div class="meta">{fc_badge}{gr_badge}<b>{html.escape(p['id'])}</b> · {html.escape(p.get('language', ''))} ·
    {html.escape(p.get('doc_type', ''))} · {html.escape(p.get('provenance', ''))}</div>
  <div class="cols">
    <div><b>Original</b><div class="orig">{html.escape(p['original'])}</div></div>
    <div><b>Aphasia-friendly version</b> ({len(t.get('pages', []))} pages)<div class="pages">{''.join(pages)}</div></div>
  </div>
  {notes_html}
  <div class="box"><span>☐ Approve</span><span>☐ Approve with small changes</span><span>☐ Needs rework</span>
    <span>Reviewer: __________</span></div>
</section>""")
        rows.append({"number": i, "id": p["id"], "title": t.get("title", ""), "language": p.get("language", ""),
                     "doc_type": p.get("doc_type", ""), "facts_pass": fc["passed"], "grade": sc["grade_level"],
                     "decision (approve / small changes / rework)": "", "changes needed": "", "reviewer": ""})

    page = (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>"
            f"<title>Example Pair Review</title><style>{CSS}</style></head><body>"
            f"<header><h1>Example pair review</h1><div class='sub'>{len(pairs)} pairs waiting for review. "
            f"Original on the left, aphasia-friendly version on the right. ☐ = clinician ticks what applies, "
            f"☎ = phone line, ⚠ = emergency line, [grey words] = picture suggestion.</div></header>"
            f"<nav class='toc'>{''.join(toc)}</nav>{''.join(body)}</body></html>")
    (out / "review_book.html").write_text(page, encoding="utf-8")
    if rows:
        with open(out / "review_checklist.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    print(f"Wrote {out/'review_book.html'} and {out/'review_checklist.csv'} ({len(pairs)} pairs)")


if __name__ == "__main__":
    main()
