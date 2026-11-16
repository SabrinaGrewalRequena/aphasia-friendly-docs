"""Build the Aphasia Handout Maker page (frontend/aphasia_handout_maker.html) from
frontend/template.html, filling in the project's rules, two example pairs and a
made-up example document with its handout, so the page always uses the same rules
as the rest of the project.

Run:  python frontend/build_artifact.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from common import load_pairs  # noqa: E402

EXAMPLE_IDS = ["medication-en-001", "appointment-es-001"]   # short, SLP-approved
SAMPLE_ID = "test-medication-levetiracetam-en"               # made-up test document

pairs = {p["id"]: p for p in load_pairs(ROOT / "data" / "pairs")}
examples = [{"source": pairs[i]["source"], "original": pairs[i]["original"], "target": pairs[i]["target"]}
            for i in EXAMPLE_IDS]
sample_pair = pairs[SAMPLE_ID]
# The example handout gets a drawing name ("icon") per line, the way new handouts do.
ICONS = {"person": "user", "pill": "pill", "doctor": "stethoscope", "seizure": "brain", "shield": "shield-check",
         "clock": "clock", "stop": "hand-stop", "sleepy": "zzz", "sad": "mood-sad", "phone": "phone",
         "no driving": "car-off", "bath": "bath", "ambulance": "ambulance", "calendar": "calendar", "help": "sos"}
output = json.loads(json.dumps(sample_pair["target"]))
for page in output["pages"]:
    for line in page["lines"]:
        line["icon"] = ICONS.get(line.get("picture", ""), "")
sample = {"source": sample_pair["source"], "original": sample_pair["original"], "output": output}

# The example page on the Home tab: a calm coping-skills page from the anxiety handout.
HERO_ID, HERO_PAGE = "mental-health-anxiety-en-001", 2
HERO_ICONS = {"walk": "walk", "calendar": "calendar", "conversation": "messages"}
hero = json.loads(json.dumps(pairs[HERO_ID]["target"]["pages"][HERO_PAGE]))
hero["topic"] = "Things that help"          # this page stands alone here, so drop "Other"
for line in hero["lines"]:
    line["icon"] = HERO_ICONS[line["picture"]]

HERE = Path(__file__).parent
rules = (ROOT / "prompts" / "system.md").read_text(encoding="utf-8")
template = (HERE / "template.html").read_text(encoding="utf-8")
dump = lambda v: json.dumps(v, ensure_ascii=False).replace("</", "<\\/")
checks = (HERE / "checks.js").read_text(encoding="utf-8")
prompts = (HERE / "prompts.js").read_text(encoding="utf-8")
icons_json = (HERE / "icons.json").read_text(encoding="utf-8")
photo = "data:image/jpeg;base64," + __import__("base64").b64encode((HERE / "sabrina.jpg").read_bytes()).decode()


def page(web):
    return (template.replace("__WEB__", "true" if web else "false")
                    .replace("__CHECKS__", checks)
                    .replace("__PROMPTS__", prompts)
                    .replace("__RULES__", dump(rules))
                    .replace("__EXAMPLES__", dump(examples))
                    .replace("__SAMPLE__", dump(sample))
                    .replace("__ICONS__", icons_json)
                    .replace("__PHOTO__", photo)
                    .replace("__HERO__", dump(hero)))


# 1) The Claude page (published as a Claude artifact; uses the viewer's own Claude).
out = HERE / "aphasia_handout_maker.html"
html = page(web=False)
out.write_text(html, encoding="utf-8")
print(f"Wrote {out} ({len(html):,} bytes)")

# 2) The public website (web/ is what Vercel serves; Claude is reached through web/api/convert.js).
WEB = ROOT / "web"
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' "
           "fill='%231d4e89'/%3E%3Cpath d='M9 8h10l4 4v12H9z' fill='none' stroke='white' stroke-width='2.2' stroke-linejoin='round'/%3E"
           "%3Cpath d='M12.5 15h7M12.5 19h5' stroke='white' stroke-width='2.2' stroke-linecap='round'/%3E%3C/svg%3E")
head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="description" content="Turn a health document into an easy-to-read, aphasia-friendly handout with pictures, in English or Spanish.">\n'
        f'<link rel="icon" href="{FAVICON}">\n')
body = page(web=True).replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
title_end = body.index("</style>") + len("</style>")        # title, fonts, libraries and styles go in <head>
site = head + body[:title_end] + "\n</head>\n<body>\n" + body[title_end:] + "\n</body>\n</html>\n"
(WEB / "index.html").write_text(site, encoding="utf-8")
print(f"Wrote {WEB / 'index.html'} ({len(site):,} bytes)")

# The server gets the same rules, examples and drawing names (labels only; it never draws).
labels = {n: {"label": v["label"]} for n, v in json.loads(icons_json).items()}
server = ("// MADE BY frontend/build_artifact.py — do not edit by hand.\n"
          f"const RULES = {json.dumps(rules, ensure_ascii=False)};\n"
          f"const EXAMPLES = {json.dumps(examples, ensure_ascii=False)};\n"
          f"const ICONS = {json.dumps(labels, ensure_ascii=False)};\n"
          + prompts + "\nmodule.exports = { systemText, taskText };\n")
(WEB / "api" / "_prompts.js").write_text(server, encoding="utf-8")
print(f"Wrote {WEB / 'api' / '_prompts.js'} ({len(server):,} bytes)")
