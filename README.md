# Aphasia-Friendly Health Documents — starter kit

Code for the 5 steps in the proposal. It is all working and tested on made-up documents.
What it still needs is **your data, an SLP, and a model run**.

```
prompts/system.md            Step 1  the writing rules, as the model's instructions (confirm with your SLP)
prompts/system_short.md              short version used for fine-tuning
data/pairs.jsonl             Step 2  your example pairs (5 made-up seed pairs to start)
data/make_seed_pairs.py              recreates the 5 seed pairs
convert.py                   Step 3  baseline: document in -> checked, printable handout out
factcheck.py                         every name/date/time/dose/address/phone kept? any number invented?
score.py                             reading grade level + format rules (lines per page, bold, pictures...)
render.py                            JSON -> printable HTML, one topic per page, ARASAAC pictures
build_dataset.py             Step 4  pairs.jsonl -> train.jsonl / test.jsonl
notebooks/finetune_colab.ipynb       LoRA fine-tune of Qwen3-4B on free Colab GPU
evaluate.py                  Step 5  run + compare systems, make a blinded SLP review sheet
examples/                            sample inputs and finished outputs (open the .html files)
```

## Setup (once)

1. Install Python 3.10+.
2. In this folder: `pip install -r requirements.txt`
3. For the Claude API: make an account at console.anthropic.com, add a little credit, create a key, then
   `export ANTHROPIC_API_KEY=sk-...` (Windows: `set ANTHROPIC_API_KEY=sk-...`).
   No budget? Use `--backend manual` (below) and paste the prompt into the Claude app instead.

## Try it

```bash
python convert.py examples/sample_documents/aphasia_group_flyer_en.txt --keep "Jordan Ellis"
# -> out/aphasia_group_flyer_en.html   open in a browser, then Print / Save as PDF
```

The HTML shows the fact-check and score report on screen (not printed). Pictures come from ARASAAC when
you're online; **click a picture to swap it** for the next match. `--keep "text"` adds names the
fact check can't spot by itself (clinic names, people without "Dr.").

Free route without an API key:

```bash
python convert.py my_letter.txt --backend manual > prompt.txt   # paste prompt.txt into a chat
# save the JSON reply as reply.json, then:
python convert.py my_letter.txt --from-json reply.json
```

## The 5 steps

**1. Rules.** `prompts/system.md` holds every rule from the proposal. Go through it with your SLP and edit
it in plain English — the model reads it as written. Keep `prompts/system_short.md` in step with it.

**2. Example pairs.** Each line of `data/pairs.jsonl` is one original + its aphasia-friendly version (see the
5 seed pairs for the format). Fastest way to grow the set:

```bash
python convert.py new_original.txt --save-pair data/drafts.jsonl
```

Then **correct each draft by hand** (and with your SLP), set `"slp_reviewed": true`, fill in `provenance`
and `license`, and move it into `pairs.jsonl`. Never train on uncorrected drafts — the fine-tuned model
would just copy the baseline's mistakes. Aim for a spread of all 5 document types in both languages.

**3. Baseline.** `convert.py` (above). Score a batch with `evaluate.py run`.

**4. Fine-tune.**
```bash
python build_dataset.py --reviewed-only     # makes data/train.jsonl + data/test.jsonl
```
Open `notebooks/finetune_colab.ipynb` in Google Colab (File → Upload notebook), pick a T4 GPU,
upload the two files, run the cells. It downloads `finetuned.zip` with outputs for the test documents.

**5. Compare.**
```bash
python evaluate.py run data/test.jsonl results/baseline
# unzip finetuned.zip into results/finetuned/
python evaluate.py compare data/test.jsonl results/baseline results/finetuned
```
You get a table against the proposal's targets (facts 100%, grade ≤ 5), `results/summary.csv`,
and a **blinded** review pack for the SLP: `results/review/*.html` + `results/slp_review_sheet.csv`
(the SLP doesn't see which system made which; `slp_key.csv` tells you).

## Running the fine-tuned model privately (optional)

Uncomment the GGUF cell in the notebook, download the file, install Ollama, and create a `Modelfile`:
```
FROM ./aphasia-gguf/<the .gguf file in that folder>
```
then `ollama create aphasia-qwen -f Modelfile` and
`python convert.py letter.txt --backend openai --model aphasia-qwen --examples 0`.
Nothing leaves your computer this way — use this route for any real patient document.

## Limits to know

- The fact check is a safety net, not a guarantee. It's strong on numbers (phones, times, doses, dates,
  addresses, emails) and flags any number the model invented. It only finds names with a title
  (Dr., Sra.) — add others with `--keep`. It can't judge meaning; that's the SLP's job.
- The reading grade uses Flesch-Kincaid (English) and Crawford (Spanish) with a simple syllable
  count. It's rough on very short text and long proper names; use it to compare systems, not as the final word.
- ARASAAC pictograms are licensed **CC BY-NC-SA 4.0**. Documents that use them must credit ARASAAC
  (the footer does this) and be shared non-commercially under the same license — so the library should
  be CC BY-NC-SA, and listings (e.g. Teachers Pay Teachers) must be free.
