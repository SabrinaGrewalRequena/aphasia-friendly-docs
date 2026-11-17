---
title: Aphasia Friendly Docs
emoji: 📄
colorFrom: pink
colorTo: yellow
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
license: apache-2.0
short_description: Fine-tuned model that writes aphasia-friendly handouts
---

# Aphasia Friendly Docs: model

This Space runs a fine-tuned **Qwen3-4B-Instruct-2507 + LoRA** model. It turns health documents into aphasia-friendly handouts in English and Spanish.

The website [aphasia-friendly-docs.vercel.app](https://aphasia-friendly-docs.vercel.app/) calls this Space's `convert` API.

- **Hardware:** works on free ZeroGPU (a GPU only while a handout is being written, with a daily limit per visitor) or on a paid GPU such as 1x Nvidia L4 (no daily limits). On paid hardware, set a **sleep time** so billing stops when nobody is using it.

**Settings** (Space → Settings → Variables and secrets):

| Name | Type | What it is |
|---|---|---|
| `ADAPTER` | variable | The model repo with the LoRA adapter. Default: `Sabrinaaaa/aphasia-qwen3-4b-lora`. |
| `FEEDBACK_REPO` | variable | Private dataset where SLP reviews are saved, e.g. `Sabrinaaaa/aphasia-feedback`. It's created automatically. |
| `REVIEWER_CODE` | secret | Access code SLPs type on the website to turn on review mode. |
| `HF_TOKEN` | secret | A Hugging Face token with write access, so the Space can save reviews. |

Review saving stays off until `FEEDBACK_REPO`, `REVIEWER_CODE` and `HF_TOKEN` are all set.

The project's code is on [GitHub](https://github.com/SabrinaGrewalRequena/aphasia-friendly-docs).

Do not paste real patient information.
