"""Turn an output JSON into a printable, aphasia-friendly HTML handout.

Open the HTML in a browser and print (or "Save as PDF"). Each topic prints on
its own page. Pictures come from ARASAAC (free symbol library) when the browser
is online; click a picture to try the next match. Without internet you get a
labelled box where a picture should go.

Usage:
    python render.py output.json [-o handout.html] [--report report.txt] [--no-pictos]
"""
import argparse
import html
import json
import re
from pathlib import Path

ARASAAC_CREDIT = ("Pictographic symbols: Sergio Palao. Origin: ARASAAC (https://arasaac.org). "
                  "License: CC BY-NC-SA 4.0. Owner: Government of Aragón (Spain).")

CSS = """
@page { size: letter; margin: 0.6in; }
* { box-sizing: border-box; }
body { font-family: Verdana, Tahoma, Arial, sans-serif; color: #111; background: #e9e9e9; margin: 0; }
.sheet { background: #fff; width: 8.5in; min-height: 11in; margin: 24px auto; padding: 0.6in;
         display: flex; flex-direction: column; box-shadow: 0 1px 6px rgba(0,0,0,.2); }
h1 { font-size: 40px; margin: 0 0 8px; }
h2 { font-size: 34px; margin: 0 0 28px; border-bottom: 4px solid #111; padding-bottom: 10px; }
.line { display: flex; align-items: center; gap: 28px; margin: 0 0 30px; font-size: 32px; line-height: 1.4; }
.pic { flex: 0 0 130px; height: 130px; display: flex; align-items: center; justify-content: center;
       border: 2px dashed #aaa; border-radius: 10px; font-size: 16px; color: #666; text-align: center;
       padding: 6px; cursor: pointer; }
.pic img { max-width: 100%; max-height: 100%; }
.pic.has-img { border: none; }
.pic.none { visibility: hidden; }
.num { font-weight: bold; font-size: 36px; min-width: 44px; }
.box { display: inline-block; width: 40px; height: 40px; border: 4px solid #111; border-radius: 4px;
       margin-right: 14px; vertical-align: middle; flex: 0 0 40px; }
.phone .txt { font-size: 40px; font-weight: bold; }
.crisis { border: 6px solid #b00020; border-radius: 12px; padding: 12px; }
.crisis .txt { font-size: 42px; font-weight: bold; }
.footer { margin-top: auto; padding-top: 18px; border-top: 1px solid #999; font-size: 12px; color: #444; }
.footer p { margin: 3px 0; }
.line > div { flex: 1; min-width: 0; }
.nw { white-space: nowrap; }
.banner { max-width: 8.5in; margin: 16px auto; padding: 14px 18px; border-radius: 8px; font: 14px/1.5 monospace;
          white-space: pre-wrap; background: #fff8e1; border: 2px solid #f0b400; }
.banner.pass { background: #e8f5e9; border-color: #43a047; }
@media print {
  body { background: #fff; }
  .sheet { margin: 0; box-shadow: none; width: auto; min-height: 9.6in; padding: 0; page-break-after: always; }
  .sheet:last-of-type { page-break-after: auto; }
  .banner, .no-print { display: none; }
  .pic { border-color: transparent; }
}
"""

JS = """
const LANG = document.documentElement.lang || 'en';
async function loadPic(el) {
  const kw = el.dataset.kw; if (!kw) return;
  try {
    if (!el._ids) {
      const r = await fetch(`https://api.arasaac.org/v1/pictograms/${LANG}/search/${encodeURIComponent(kw)}`);
      if (!r.ok) throw 0;
      el._ids = (await r.json()).map(p => p._id); el._i = 0;
    }
    if (!el._ids.length) return;
    const id = el._ids[el._i % el._ids.length];
    el.innerHTML = `<img alt="${kw}" src="https://static.arasaac.org/pictograms/${id}/${id}_500.png">`;
    el.classList.add('has-img'); el.title = 'Click for a different picture';
  } catch (e) { /* offline: keep the labelled box */ }
}
document.querySelectorAll('.pic[data-kw]').forEach(el => {
  loadPic(el);
  el.addEventListener('click', () => { if (el._ids) { el._i++; loadPic(el); } });
});
"""


def md_bold(text):
    t = html.escape(text)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)


def render_line(line, step_no, pictos, lang="en"):
    label = "imagen" if lang == "es" else "picture"
    kind = line.get("kind", "text")
    kw = (line.get("picture") or "").strip()
    if kw and pictos:
        pic = f'<div class="pic" data-kw="{html.escape(kw)}">[{label}: {html.escape(kw)}]</div>'
    elif kw:
        pic = f'<div class="pic">[{label}: {html.escape(kw)}]</div>'
    else:
        pic = '<div class="pic none"></div>'
    text = md_bold(line.get("text", ""))
    text = re.sub(r"(\d{1,2}(?::\d{2})?\s?[ap]\.\s?m\.)", r'<span class="nw">\1</span>', text, flags=re.I)  # keep times whole
    if kind in ("phone", "crisis"):   # never split a phone number across lines
        text = re.sub(r"(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})", r'<span class="nw">\1</span>', text)
    if kind == "step":
        body = f'<span class="num">{step_no}.</span><span class="txt">{text}</span>'
    elif kind == "checkbox":
        body = f'<span class="box"></span><span class="txt">{text}</span>'
    else:
        body = f'<span class="txt">{text}</span>'
    return f'<div class="line {kind}">{pic}<div style="display:flex;align-items:center">{body}</div></div>'


def render(doc, report_text="", passed=None, pictos=True, reviewed_by=""):
    lang = doc.get("language", "en")
    es = lang == "es"
    title = html.escape(doc.get("title", ""))
    source = html.escape(doc.get("source", ""))
    review = (f"Reviewed by {html.escape(reviewed_by)}" if reviewed_by else
              ("Revisado por: ______________________ CCC-SLP &nbsp; Fecha: __________" if es else
               "Reviewed by: ______________________ CCC-SLP &nbsp; Date: __________"))
    src_label = "Basado en" if es else "Based on"
    footer = (f'<div class="footer"><p>{src_label}: {source}</p><p>{review}</p>'
              + (f"<p>{ARASAAC_CREDIT}</p>" if pictos else "") + "</div>")

    parts = []
    if report_text:
        cls = "banner pass" if passed else "banner"
        parts.append(f'<div class="{cls}">Screen only — not printed.\n\n{html.escape(report_text)}</div>')
    notes = doc.get("notes_for_reviewer") or []
    if notes:
        parts.append('<div class="banner">Notes for reviewer (not printed):\n'
                     + "\n".join("• " + html.escape(n) for n in notes) + "</div>")

    for i, page in enumerate(doc.get("pages", [])):
        step = 0
        lines_html = []
        for line in page.get("lines", []):
            if line.get("kind") == "step":
                step += 1
            lines_html.append(render_line(line, step, pictos, lang))
        head = f"<h1>{title}</h1>" if i == 0 else ""
        parts.append(f'<section class="sheet">{head}<h2>{md_bold(page.get("topic", ""))}</h2>'
                     f'{"".join(lines_html)}{footer}</section>')

    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f"<title>{title}</title><style>{CSS}</style></head><body>{''.join(parts)}"
            f"<script>{JS if pictos else ''}</script></body></html>")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("output_json")
    ap.add_argument("-o", "--out")
    ap.add_argument("--report", help="text file with fact-check/score report to show on screen")
    ap.add_argument("--no-pictos", action="store_true")
    ap.add_argument("--reviewed-by", default="")
    a = ap.parse_args()
    doc = json.loads(Path(a.output_json).read_text(encoding="utf-8"))
    rep = Path(a.report).read_text(encoding="utf-8") if a.report else ""
    out = Path(a.out or Path(a.output_json).with_suffix(".html"))
    out.write_text(render(doc, rep, "FACT CHECK: PASS" in rep, not a.no_pictos, a.reviewed_by), encoding="utf-8")
    print(f"Wrote {out}")
