"""Aphasia Friendly Docs: runs Sabrina's fine-tuned model (Qwen3-4B + LoRA) on a Hugging Face ZeroGPU Space.

The website (aphasia-friendly-docs.vercel.app) sends a document here and gets the handout back as JSON,
streamed as it is written. It asks the model exactly the way it was trained (prompts/system_short.md + the
same user message), and copies facts more reliably by always picking the most likely next word
(greedy decoding, no randomness).

It also receives optional SLP feedback (which version is best, plus any edits) and saves it to a private
Hugging Face dataset, so the next training round can learn from it.

Settings (Space → Settings → Variables and secrets):
  ADAPTER        variable  the fine-tuned model repo (default "Sabrinaaaa/aphasia-qwen3-4b-lora")
  FEEDBACK_REPO  variable  private dataset for SLP feedback, e.g. "Sabrinaaaa/aphasia-feedback"
  REVIEWER_CODE  secret    the access code SLPs type on the website to turn on review mode
  HF_TOKEN       secret    a Hugging Face token with "write" access (lets the Space save feedback)
"""
import datetime
import hmac
import json
import os
import time
import uuid
from pathlib import Path
from threading import Thread

import gradio as gr
import spaces
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer

BASE = "Qwen/Qwen3-4B-Instruct-2507"
ADAPTER = os.environ.get("ADAPTER", "Sabrinaaaa/aphasia-qwen3-4b-lora")   # the fine-tuned model on Hugging Face
MAX_CHARS = 30000                                # longest document accepted (~10 pages)
SYSTEM = (Path(__file__).parent / "system_short.md").read_text(encoding="utf-8").strip()
LANG_NAMES = {"en": "English", "es": "Spanish"}
# Every handout in training starts like this. Writing it for the model makes it start the handout right away
# (instead of sometimes repeating the document first, which wasted time).
START = '{"title": "'

tokenizer = AutoTokenizer.from_pretrained(BASE)
# Newer GPUs (ZeroGPU, L4, A10G...) use bfloat16. An older T4 can't, so it gets float16.
try:
    DTYPE = torch.float16 if torch.cuda.get_device_capability()[0] < 8 else torch.bfloat16
except Exception:   # ZeroGPU: no GPU at start-up, and its GPUs are new
    DTYPE = torch.bfloat16
model = AutoModelForCausalLM.from_pretrained(BASE, dtype=DTYPE)
if ADAPTER:
    # torch_device="cpu": on ZeroGPU the GPU only exists while a handout is being written,
    # so the trained part is loaded into normal memory first and moved to the GPU below.
    model = PeftModel.from_pretrained(model, ADAPTER, torch_device="cpu").merge_and_unload()   # your training, built in
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


@spaces.GPU(duration=75)   # website visitors are guests on Hugging Face, who get a shorter GPU limit
def generate(text, source, lang, retry):
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": user_message(text, (source or "Uploaded document")[:120], lang)}]
    prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False) + START
    inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to("cuda")
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    # First try: always the most likely word (copies facts best). "Try again": a little variety.
    sampling = dict(do_sample=True, temperature=0.3, top_p=0.9) if retry else dict(do_sample=False)
    job = Thread(target=model.generate, kwargs=dict(**inputs, streamer=streamer, max_new_tokens=3500,
                                                    pad_token_id=tokenizer.eos_token_id, **sampling))
    job.start()
    out, last = START, 0.0
    for piece in streamer:
        out += piece
        # Send an update about 3 times a second instead of after every word: each update carries the
        # whole handout so far, so sending thousands of them made the website slow.
        if time.monotonic() - last > 0.33:
            last = time.monotonic()
            yield out
    job.join()
    yield out


# ───────────────────────────── SLP feedback (optional) ─────────────────────────────
FEEDBACK_REPO = os.environ.get("FEEDBACK_REPO", "").strip()
REVIEWER_CODE = os.environ.get("REVIEWER_CODE", "").strip()
FEEDBACK_DIR = Path(__file__).parent / "feedback"
FEEDBACK_DIR.mkdir(exist_ok=True)
FEEDBACK_FILE = FEEDBACK_DIR / f"feedback-{uuid.uuid4().hex[:8]}.jsonl"   # one file per Space start
scheduler = None
if FEEDBACK_REPO and REVIEWER_CODE and os.environ.get("HF_TOKEN"):
    try:
        from huggingface_hub import CommitScheduler
        # Uploads new feedback to the private dataset every 5 minutes.
        scheduler = CommitScheduler(repo_id=FEEDBACK_REPO, repo_type="dataset", folder_path=FEEDBACK_DIR,
                                    path_in_repo="data", every=5, private=True)
    except Exception as e:
        print("Feedback saving is off:", repr(e))
else:
    print("Feedback saving is off (set FEEDBACK_REPO, REVIEWER_CODE and HF_TOKEN to turn it on).")

KEEP = ("original", "source", "lang", "versions", "chosen", "rating", "comment", "app")


def code_ok(code):
    return bool(REVIEWER_CODE) and hmac.compare_digest(str(code or "").strip().encode(), REVIEWER_CODE.encode())


def check_code(code):
    """The website asks this when an SLP types the access code."""
    if scheduler is None:
        return "\x00ERR:feedback_off"
    return "OK" if code_ok(code) else "\x00ERR:bad_code"


def save_feedback(code, payload):
    """One review: the original document, every version the model wrote (and any SLP edits),
    which version the SLP chose, and optional rating and comment."""
    if scheduler is None:
        return "\x00ERR:feedback_off"
    if not code_ok(code):
        time.sleep(1)                                    # slows down anyone guessing codes
        return "\x00ERR:bad_code"
    if len(payload or "") > 400_000:
        return "\x00ERR:prompt_too_large"
    try:
        data = json.loads(payload)
        assert isinstance(data, dict) and isinstance(data.get("versions"), list) and data["versions"]
        assert isinstance(data.get("original"), str) and len(data["original"].strip()) >= 20
    except Exception:
        return "\x00ERR:bad_request"
    record = {"id": uuid.uuid4().hex, "received": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
              "model": ADAPTER, **{k: data.get(k) for k in KEEP}}
    with scheduler.lock:
        with FEEDBACK_FILE.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return "OK"


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

    # Hidden: only used by the website's review mode
    fb_code = gr.Textbox(visible=False)
    fb_payload = gr.Textbox(visible=False)
    fb_out = gr.Textbox(visible=False)
    fb_check = gr.Button(visible=False)
    fb_save = gr.Button(visible=False)
    fb_check.click(check_code, [fb_code], fb_out, api_name="check_code")
    fb_save.click(save_feedback, [fb_code, fb_payload], fb_out, api_name="feedback")

demo.queue(max_size=20).launch(show_error=True)   # lets the website show "quota used up" and similar messages
