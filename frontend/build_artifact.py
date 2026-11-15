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

rules = (ROOT / "prompts" / "system.md").read_text(encoding="utf-8")
html = (Path(__file__).with_name("template.html")).read_text(encoding="utf-8")
dump = lambda v: json.dumps(v, ensure_ascii=False).replace("</", "<\\/")
checks = (Path(__file__).with_name("checks.js")).read_text(encoding="utf-8")
html = (html.replace("__CHECKS__", checks)
            .replace("__RULES__", dump(rules))
            .replace("__EXAMPLES__", dump(examples))
            .replace("__SAMPLE__", dump(sample))
            .replace("__ICONS__", (Path(__file__).with_name("icons.json")).read_text(encoding="utf-8")))
out = Path(__file__).with_name("aphasia_handout_maker.html")
out.write_text(html, encoding="utf-8")
print(f"Wrote {out} ({len(html):,} bytes)")
