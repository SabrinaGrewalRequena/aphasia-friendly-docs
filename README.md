# Aphasia Friendly Docs

**Turn any document into one people with aphasia can read.**

🌸 **Try it: [aphasia-friendly-docs.vercel.app](https://aphasia-friendly-docs.vercel.app/)** · free · English & Spanish · no account needed

Upload a PDF, a Word file, or a photo of a letter. The site turns it into an aphasia-friendly handout with short sentences, one idea per line, key words in bold, and a picture beside every line. Every name, date, dose and phone number is then checked against the original.

---

## How it works

1. **Read.** The page pulls the text out of the uploaded file. Photos and scanned PDFs are read by Claude.
2. **Rewrite.** Claude rewrites the document using the project's writing rules ([`prompts/system.md`](prompts/system.md)) and two worked examples.
3. **Fact check.** The handout is compared with the original. Any fact that is missing or changed, or any number that was invented, is shown on screen, and **Fix with Claude** repairs it.
4. **Print.** Every line can be edited before downloading a print-ready, letter-size handout.

## Results

The project tested two systems on 25 documents that were never used for training (15 English, 10 Spanish):

| | Claude + rules (the website) | Fine-tuned Qwen3-4B |
|---|---|---|
| Valid handout | 25 / 25 | 24 / 25 |
| Every fact copied exactly | 24 / 25* | 14 / 25 |
| Reading grade ≤ 5 | 25 / 25 (avg 1.6) | 24 / 24 (avg 1.7) |
| Format issues per handout | 0.4 | 2.5 |

\*The one flag was a false alarm: "1 time a day" for "once daily."

A certified speech-language pathologist reviewed all 49 handouts blind and found no errors. The Claude version powers the website. The fine-tuned model remains a free, offline option. Details are in [`docs/results_round1.md`](docs/results_round1.md).

## Training data

- **150 example pairs:** 81 English and 69 Spanish. Each pair is an original document plus its aphasia-friendly version.
- **Review:** all 150 were approved by a certified speech-language pathologist.
- **Split:** 125 for training, 25 held back for testing.
- **Document types:** referrals, appointments, discharge papers, medications, mental health, consent, insurance, home programs, and messy real-world formats such as pharmacy labels, portal messages and faxes.
- **Made-up details:** all names, clinics and phone numbers in the made-up documents are invented. Phone numbers use the fictional 555-01xx range.
- **UNC handouts:** 8 targets are adapted from public aphasia-friendly handouts by the UNC School of Medicine.

## What's in this repo

| Folder / file | What it is |
|---|---|
| [`web/`](web/) | **The website.** `index.html` is the page, and `api/convert.js` is the server that calls Claude. See [`web/README.md`](web/README.md). |
| [`frontend/`](frontend/) | Source for the page: `template.html` (design and logic), `checks.js` (fact check), `prompts.js`, drawings, and `build_artifact.py`, which builds `web/index.html`. |
| [`prompts/`](prompts/) | The writing rules the model follows. |
| [`data/pairs/`](data/pairs/) | The 150 example pairs, one `.jsonl` file per batch. [`data/sources/`](data/sources/) holds the scripts that wrote them. |
| [`review/`](review/) | Review books used for the expert check of each batch. |
| [`notebooks/`](notebooks/) | Google Colab notebook for fine-tuning Qwen3-4B with LoRA. |
| `convert.py`, `factcheck.py`, `score.py`, `render.py` | Command-line version: convert a document, run the fact check, score reading level and format, and make printable HTML. |
| `build_dataset.py`, `check_pairs.py`, `review_pairs.py`, `evaluate.py` | Build train/test files, check every pair, make review books, and compare systems. |
| [`examples/`](examples/) | Sample documents and finished handouts. |
| [`docs/`](docs/) | Results write-ups. |

## Run it yourself

**Update the website:** edit `frontend/template.html`, then run:

```bash
python frontend/build_artifact.py   # rebuilds web/index.html
git push                            # Vercel redeploys the site automatically
```

**Command line:** this needs Python 3.10+ and an Anthropic API key.

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...        # never commit your key
python convert.py examples/sample_documents/aphasia_group_flyer_en.txt
# -> out/aphasia_group_flyer_en.html  (open it, then Print)
```

**Check the data and compare systems:**

```bash
python check_pairs.py                         # fact-check every pair
python build_dataset.py --reviewed-only       # make data/train.jsonl and data/test.jsonl
python evaluate.py run data/test.jsonl results/baseline
python evaluate.py compare data/test.jsonl results/baseline results/finetuned
```

## Privacy and limits

- **Do not upload real patient information** to the website. Remove names, birth dates and record numbers first. For real documents, use the fine-tuned model offline (see the notebook), so nothing leaves your computer.
- The fact check is a safety net, not a guarantee. It is strong on numbers, such as phones, times, doses, dates and addresses, but it can't judge meaning. **Always read a handout before giving it to someone.**
- This tool does not give medical advice.

## Credits

- **Writing engine:** Claude by Anthropic.
- **Drawings on the website:** [Tabler Icons](https://tabler.io/icons) (MIT License; see [`frontend/TABLER_ICONS_LICENSE.txt`](frontend/TABLER_ICONS_LICENSE.txt)).
- **Pictures in the command-line version (`render.py`):** [ARASAAC](https://arasaac.org) pictograms by Sergio Palao, licensed CC BY-NC-SA 4.0.
- **Handout style:** inspired by the UNC School of Medicine's aphasia-friendly handouts.

## About

Made by **Sabrina Grewal Requena**, an incoming medical student who wants to serve her community and make healthcare accessible to all people.
