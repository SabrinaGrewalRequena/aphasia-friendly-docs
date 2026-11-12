"""Builds finetune_colab.ipynb. Run: python notebooks/make_notebook.py"""
from pathlib import Path
import nbformat as nbf

md, code = nbf.v4.new_markdown_cell, nbf.v4.new_code_cell
cells = [
md("""# Step 4 — Fine-tune a small open model (LoRA on Google Colab)

**Before you start**
1. In Colab: **Runtime → Change runtime type → T4 GPU** (free tier works).
2. On your computer run `python build_dataset.py` to make `data/train.jsonl` and `data/test.jsonl`.
3. Run the cells below in order. Training on ~150–500 pairs takes roughly 15–60 minutes on a T4.

The model learns from your example pairs. If a pair has a mistake, the model learns the mistake —
only train on pairs that pass the fact check and that your SLP has approved."""),
code("""%%capture
!pip install unsloth"""),
md("## 1. Upload `train.jsonl` and `test.jsonl`"),
code("""from google.colab import files
uploaded = files.upload()   # choose data/train.jsonl and data/test.jsonl
print(list(uploaded))"""),
md("""## 2. Load the base model

`Qwen3-4B-Instruct-2507` is small, handles English and Spanish well, and has an Apache 2.0 license
(free to share). If you run out of memory, switch to a smaller model in the list."""),
code("""from unsloth import FastLanguageModel
import torch

MODEL = "unsloth/Qwen3-4B-Instruct-2507"
# Smaller / alternative options (all fine for a free T4):
#   "unsloth/Qwen2.5-1.5B-Instruct"   (Apache 2.0, faster, weaker)
#   "unsloth/Llama-3.2-3B-Instruct"   (Llama community license)
MAX_LEN = 4096

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=MODEL, max_seq_length=MAX_LEN, load_in_4bit=True)

model = FastLanguageModel.get_peft_model(
    model, r=16, lora_alpha=16, lora_dropout=0, bias="none",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    use_gradient_checkpointing="unsloth", random_state=3407)"""),
md("## 3. Prepare the training data"),
code("""from datasets import load_dataset

train = load_dataset("json", data_files="train.jsonl", split="train")
train = train.map(lambda ex: {"text": tokenizer.apply_chat_template(ex["messages"], tokenize=False)})
lengths = [len(tokenizer(t).input_ids) for t in train["text"]]
print(len(train), "examples; longest =", max(lengths), "tokens (must be under", MAX_LEN, ")")
print(train[0]["text"][:1500])"""),
md("## 4. Train"),
code("""from trl import SFTTrainer, SFTConfig
from unsloth.chat_templates import train_on_responses_only

trainer = SFTTrainer(
    model=model, processing_class=tokenizer, train_dataset=train,
    args=SFTConfig(
        dataset_text_field="text", max_length=MAX_LEN,
        per_device_train_batch_size=1, gradient_accumulation_steps=8,
        num_train_epochs=3, learning_rate=2e-4, warmup_steps=5,
        lr_scheduler_type="linear", optim="adamw_8bit", weight_decay=0.01,
        logging_steps=5, seed=3407, output_dir="outputs", report_to="none"))

# Only learn from the model's answers, not from the documents themselves
trainer = train_on_responses_only(trainer,
    instruction_part="<|im_start|>user\\n", response_part="<|im_start|>assistant\\n")

stats = trainer.train()
print(stats)"""),
md("""Watch the **loss** in the log: it should go down and level off. If it drops near 0 the model is
memorising — use fewer epochs (e.g. 2) or more data."""),
md("## 5. Run the fine-tuned model on the test documents"),
code("""import json, os, re

FastLanguageModel.for_inference(model)
SYSTEM = json.loads(open("train.jsonl").readline())["messages"][0]["content"]
os.makedirs("finetuned", exist_ok=True)

def convert(original, source):
    msgs = [{"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"Source name: {source}\\n\\nOriginal document:\\n<<<\\n{original.strip()}\\n>>>"}]
    inputs = tokenizer.apply_chat_template(msgs, add_generation_prompt=True, tokenize=True,
                                           return_dict=True, return_tensors="pt").to("cuda")
    out = model.generate(**inputs, max_new_tokens=3000, temperature=0.2, top_p=0.9, do_sample=True)
    return tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

tests = [json.loads(l) for l in open("test.jsonl")]
for t in tests:
    raw = convert(t["original"], t.get("source", t["id"]))
    m = re.search(r"\\{.*\\}", raw, re.S)
    path = f"finetuned/{t['id']}.json"
    open(path if m else path.replace(".json", ".raw.txt"), "w").write(m.group(0) if m else raw)
    print("done", t["id"], "" if m else "(no JSON — saved raw)")

!zip -qr finetuned.zip finetuned
files.download("finetuned.zip")"""),
md("""Unzip `finetuned.zip` into `results/finetuned/` on your computer, then run
`python evaluate.py compare data/test.jsonl results/baseline results/finetuned`."""),
md("## 6. Save the model"),
code("""# Small LoRA adapter (~100 MB) — save to Google Drive so you don't lose it
from google.colab import drive
drive.mount("/content/drive")
model.save_pretrained("/content/drive/MyDrive/aphasia-lora")
tokenizer.save_pretrained("/content/drive/MyDrive/aphasia-lora")"""),
code("""# OPTIONAL: export a GGUF file to run privately on a laptop with Ollama (takes ~10 min)
# model.save_pretrained_gguf("/content/drive/MyDrive/aphasia-gguf", tokenizer, quantization_method="q4_k_m")
# Then on your computer:  ollama create aphasia-qwen -f Modelfile   (see README)"""),
]
nb = nbf.v4.new_notebook(cells=cells, metadata={"accelerator": "GPU", "colab": {"gpuType": "T4"},
                                                  "kernelspec": {"name": "python3", "display_name": "Python 3"}})
out = Path(__file__).with_name("finetune_colab.ipynb")
nbf.write(nb, out)
print("Wrote", out)
