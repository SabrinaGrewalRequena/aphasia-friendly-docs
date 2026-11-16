"""Aphasia Friendly Docs: runs Sabrina's fine-tuned model (Qwen3-4B + LoRA) on a Hugging Face ZeroGPU Space.

The website (aphasia-friendly-docs.vercel.app) sends a document here and gets the handout back as JSON,
streamed word by word. It asks the model exactly the way it was trained (prompts/system_short.md + the
same user message), and copies facts more reliably by always picking the most likely next word
(greedy decoding, no randomness).

Settings (Space → Settings → Variables): ADAPTER = your model repo, e.g. "your-name/aphasia-qwen3-4b-lora"
"""
import os
from pathlib import Path
from threading import Thread

import gradio as gr
import spaces
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer

BASE = "Qwen/Qwen3-4B-Instruct-2507"
ADAPTER = os.environ.get("ADAPTER", "")          # set this in the Space settings
MAX_CHARS = 30000                                # longest document accepted (~10 pages)
SYSTEM = (Path(__file__).parent / "system_short.md").read_text(encoding="utf-8").strip()
LANG_NAMES = {"en": "English", "es": "Spanish"}

tokenizer = AutoTokenizer.from_pretrained(BASE)
model = AutoModelForCausalLM.from_pretrained(BASE, torch_dtype=torch.bfloat16)
if ADAPTER:
    model = PeftModel.from_pretrained(model, ADAPTER).merge_and_unload()   # your training, built in
else:
    print("WARNING: ADAPTER is not set, so this is the plain base model, not your fine-tuned one.")
model.to("cuda")
model.eval()


def user_message(text, source, lang):
    """Exactly the format used in training (convert.py / build_dataset.py)."""
    target = f"Write the output in {LANG_NAMES.get(lang, lang)}.\n" if lang else ""
    return f"{target}Source name: {source}\n\nOriginal document:\n<<<\n{text.strip()}\n>>>"


def convert(text, source="Uploaded document", lang="", retry=False):
    """What the website calls. Problems come back as a short code ("\x00ERR:quota") because
    Gradio's simple API hides error messages from other websites."""
    text = (text or "").strip()
    if len(text) < 20:
        yield "\x00ERR:no_text"; return
    if len(text) > MAX_CHARS:
        yield "\x00ERR:prompt_too_large"; return
    try:
        yield from generate(text, source, lang if lang in LANG_NAMES else "", bool(retry))
    except Exception as e:                      # e.g. the visitor's free daily GPU time is used up
        print("convert failed:", repr(e))
        yield "\x00ERR:" + ("quota" if "quota" in str(e).lower() else "model_error")


@spaces.GPU(duration=150)
def generate(text, source, lang, retry):
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": user_message(text, (source or "Uploaded document")[:120], lang)}]
    inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt",
                                           return_dict=True).to("cuda")
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    # First try: always the most likely word (copies facts best). "Try again": a little variety.
    sampling = dict(do_sample=True, temperature=0.3, top_p=0.9) if retry else dict(do_sample=False)
    job = Thread(target=model.generate, kwargs=dict(**inputs, streamer=streamer, max_new_tokens=3500,
                                                    pad_token_id=tokenizer.eos_token_id, **sampling))
    job.start()
    out = ""
    for piece in streamer:
        out += piece
        yield out
    job.join()


with gr.Blocks(title="Aphasia Friendly Docs: model") as demo:
    gr.Markdown("## Aphasia Friendly Docs: fine-tuned model\nThe website uses this Space. "
                "Paste a made-up document to try it. **Do not paste real patient information.**")
    doc = gr.Textbox(label="Document text", lines=10)
    with gr.Row():
        src = gr.Textbox(label="Document name", value="Uploaded document")
        lng = gr.Dropdown(label="Language", choices=[("Same as the document", ""), ("English", "en"), ("Spanish", "es")], value="")
        rty = gr.Checkbox(label="Try a different wording", value=False)
    btn = gr.Button("Make handout (JSON)", variant="primary")
    out = gr.Textbox(label="Handout JSON", lines=16)
    btn.click(convert, [doc, src, lng, rty], out, api_name="convert")

demo.queue(max_size=20).launch(show_error=True)   # lets the website show "quota used up" and similar messages
