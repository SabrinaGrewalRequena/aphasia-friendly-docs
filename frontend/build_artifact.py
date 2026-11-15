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
sample = {"source": sample_pair["source"], "original": sample_pair["original"], "output": sample_pair["target"]}

rules = (ROOT / "prompts" / "system.md").read_text(encoding="utf-8")
html = (Path(__file__).with_name("template.html")).read_text(encoding="utf-8")
dump = lambda v: json.dumps(v, ensure_ascii=False).replace("</", "<\\/")
html = (html.replace("__RULES__", dump(rules))
            .replace("__EXAMPLES__", dump(examples))
            .replace("__SAMPLE__", dump(sample)))
out = Path(__file__).with_name("aphasia_handout_maker.html")
out.write_text(html, encoding="utf-8")
print(f"Wrote {out} ({len(html):,} bytes)")
