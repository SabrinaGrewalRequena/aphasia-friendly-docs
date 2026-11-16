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

- **Hardware:** ZeroGPU. A GPU is used only while a handout is being written.
- **Setting:** `ADAPTER` must name the model repo that holds the LoRA adapter.

The project's code is on [GitHub](https://github.com/SabrinaGrewalRequena/aphasia-friendly-docs).

Do not paste real patient information.
