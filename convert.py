"""Convert a health document into an aphasia-friendly handout (Step 3: the baseline).

It sends your rules (prompts/system.md) plus a few example pairs to a language
model, then fact-checks, scores and renders the result as a printable page.

Backends:
  anthropic   Claude via the API (needs ANTHROPIC_API_KEY)            [default]
  openai      any OpenAI-compatible server: Ollama, LM Studio, vLLM,
              or your fine-tuned model (use --base-url and --model)
  manual      prints the full prompt so you can paste it into a chat app,
              then paste the JSON reply into a file and run with --from-json

Usage:
  python convert.py my_letter.txt                          # Claude API
  python convert.py my_letter.docx --lang es               # write the output in Spanish
  python convert.py my_letter.txt --backend openai --base-url http://localhost:11434/v1 --model aphasia-qwen
  python convert.py my_letter.txt --backend manual > prompt.txt
  python convert.py my_letter.txt --from-json reply.json   # check + render a reply you pasted
  python convert.py my_letter.txt --save-pair data/drafts.jsonl   # save as a draft training pair

Outputs go to out/<name>.json, out/<name>.html (print this) and out/<name>.report.txt
"""
import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

import factcheck
import render
import score
from common import ROOT, parse_model_json, read_document, validate

LANG_NAMES = {"en": "English", "es": "Spanish"}


def load_examples(lang, k, pairs_file, exclude_text=""):
    """Pick up to k training pairs, preferring the same language and reviewed pairs."""
    path = Path(pairs_file)
    if not path.exists() or k <= 0:
        return []
    pairs = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    pairs = [p for p in pairs if p.get("split", "train") == "train" and p["original"].strip() != exclude_text.strip()]
    pairs.sort(key=lambda p: (p.get("language") != lang, not p.get("slp_reviewed", False)))
    return pairs[:k]


def user_message(text, source, lang):
    target = f"Write the output in {LANG_NAMES.get(lang, lang)}.\n" if lang else ""
    return f"{target}Source name: {source}\n\nOriginal document:\n<<<\n{text.strip()}\n>>>"


def build_messages(text, source, lang, examples):
    msgs = []
    for ex in examples:
        msgs.append({"role": "user", "content": user_message(ex["original"], ex.get("source", ""), None)})
        msgs.append({"role": "assistant", "content": json.dumps(ex["target"], ensure_ascii=False)})
    msgs.append({"role": "user", "content": user_message(text, source, lang)})
    return msgs


def call_anthropic(system, messages, model, max_tokens=8000):
    import anthropic  # pip install anthropic
    client = anthropic.Anthropic()
    resp = client.messages.create(model=model, system=system, messages=messages,
                                  max_tokens=max_tokens, temperature=0.2)
    return "".join(b.text for b in resp.content if b.type == "text")


def call_openai_compatible(system, messages, model, base_url, max_tokens=4000):
    body = {"model": model, "temperature": 0.2, "max_tokens": max_tokens,
            "messages": [{"role": "system", "content": system}] + messages}
    req = urllib.request.Request(base_url.rstrip("/") + "/chat/completions", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer " + os.environ.get("OPENAI_API_KEY", "none")})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]


def check_and_render(original, doc, out_base, keep=(), pictos=True):
    problems = validate(doc)
    fc = factcheck.check(original, doc, keep)
    sc = score.score(doc)
    report = factcheck.format_report(fc) + "\n" + score.format_report(sc)
    if problems:
        report = "STRUCTURE PROBLEMS:\n" + "\n".join("  - " + p for p in problems) + "\n" + report
    out_base.parent.mkdir(parents=True, exist_ok=True)
    out_base.with_suffix(".json").write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    out_base.with_suffix(".report.txt").write_text(report, encoding="utf-8")
    out_base.with_suffix(".html").write_text(render.render(doc, report, fc["passed"], pictos), encoding="utf-8")
    return fc, sc, report


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help=".txt, .md, .docx or .pdf")
    ap.add_argument("--lang", choices=["en", "es"], help="output language (default: same as original)")
    ap.add_argument("--source", help="name of the original, printed in the footer (default: file name)")
    ap.add_argument("--backend", choices=["anthropic", "openai", "manual"], default="anthropic")
    ap.add_argument("--model", default="claude-sonnet-5-5")
    ap.add_argument("--base-url", default="http://localhost:11434/v1")
    ap.add_argument("--examples", type=int, default=2, help="how many example pairs to show the model")
    ap.add_argument("--pairs", default=str(ROOT / "data" / "pairs.jsonl"))
    ap.add_argument("--from-json", help="skip the model; check + render this JSON reply instead")
    ap.add_argument("--keep", action="append", default=[], help="text that must appear exactly, e.g. a clinic name")
    ap.add_argument("--out-dir", default="out")
    ap.add_argument("--no-pictos", action="store_true")
    ap.add_argument("--save-pair", help="append the result to this JSONL as a DRAFT pair for you/the SLP to correct")
    a = ap.parse_args()

    text = read_document(a.input)
    source = a.source or Path(a.input).stem
    system = (ROOT / "prompts" / "system.md").read_text(encoding="utf-8")
    examples = load_examples(a.lang or "en", a.examples, a.pairs, exclude_text=text)
    messages = build_messages(text, source, a.lang, examples)

    if a.backend == "manual" and not a.from_json:
        print("=== PASTE EVERYTHING BELOW INTO A CHAT ===\n")
        print(system)
        for m in messages[:-1]:
            print(f"\n--- Example {'input' if m['role'] == 'user' else 'output'} ---\n{m['content']}")
        print("\n--- Now convert this ---\n" + messages[-1]["content"])
        return

    if a.from_json:
        raw = Path(a.from_json).read_text(encoding="utf-8")
    elif a.backend == "anthropic":
        raw = call_anthropic(system, messages, a.model)
    else:
        raw = call_openai_compatible(system, messages, a.model, a.base_url)

    try:
        doc = parse_model_json(raw)
    except Exception as e:
        bad = Path(a.out_dir) / (Path(a.input).stem + ".raw.txt")
        bad.parent.mkdir(parents=True, exist_ok=True)
        bad.write_text(raw, encoding="utf-8")
        sys.exit(f"Model did not return valid JSON ({e}). Raw reply saved to {bad}")
    doc.setdefault("source", source)

    out_base = Path(a.out_dir) / Path(a.input).stem
    fc, sc, report = check_and_render(text, doc, out_base, a.keep, not a.no_pictos)
    print(report)
    print(f"\nPrint this: {out_base.with_suffix('.html')}")

    if a.save_pair:
        pair = {"id": Path(a.input).stem, "language": doc.get("language", a.lang or "en"), "doc_type": "",
                "split": "train", "provenance": "", "license": "", "slp_reviewed": False,
                "source": source, "original": text, "target": doc,
                "draft_from": a.model if not a.from_json else "pasted"}
        with open(a.save_pair, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(pair, ensure_ascii=False) + "\n")
        print(f"Saved DRAFT pair to {a.save_pair} — correct it by hand before training on it.")

    sys.exit(0 if fc["passed"] else 1)


if __name__ == "__main__":
    main()
