# The public website (Vercel)

This folder is the website people use: https://aphasia-friendly-docs.vercel.app/

- `index.html` is the whole site. It's made by `python frontend/build_artifact.py`, so don't edit it by hand.
- The handout is written by the fine-tuned model running in the Hugging Face Space at `Sabrinaaaa/aphasia-friendly-docs` (see `../space/`). The visitor's browser asks the Space directly, so each visitor uses their own free Hugging Face GPU time. No API key is needed.
- The Space address is in `frontend/space_url.txt`.

**To update the site:** run `python frontend/build_artifact.py` and push to GitHub. Vercel redeploys automatically.

**To update the model:** retrain in Colab, upload the new adapter files to the Hugging Face model repo `Sabrinaaaa/aphasia-qwen3-4b-lora`, then restart the Space.
