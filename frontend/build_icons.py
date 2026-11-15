"""Build frontend/icons.json: the drawings the Handout Maker can put beside each line.

The drawings come from Tabler Icons (MIT license, https://tabler.io/icons), version 3.19.0.
frontend/icon_list.txt names the ones we use, each with plain words Claude uses to choose.

Run:  npm pack @tabler/icons@3.19.0 && tar -xzf tabler-icons-3.19.0.tgz
      python frontend/build_icons.py package/icons/outline
"""
import json
import re
import sys
from pathlib import Path

src = Path(sys.argv[1])
here = Path(__file__).resolve().parent
icons = {}
for line in (here / "icon_list.txt").read_text(encoding="utf-8").strip().splitlines():
    name, label = line.split(" ", 1)
    svg = (src / f"{name}.svg").read_text(encoding="utf-8")
    inner = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
    inner = re.sub(r'<path stroke="none" d="M0 0h24v24H0z" fill="none"\s*/>', "", inner)
    icons[name] = {"label": label, "svg": re.sub(r"\s+", " ", inner).strip()}
(here / "icons.json").write_text(json.dumps(icons, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {len(icons)} drawings to {here / 'icons.json'}")
