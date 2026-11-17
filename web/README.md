# The public website (Vercel)

This folder is the website people use: https://aphasia-friendly-docs.vercel.app/

- **`index.html`:** the whole site. It's made by `python frontend/build_artifact.py`, so don't edit it by hand.
- **`sabrina.jpg`:** the About Me photo. It loads only when that tab is opened.
- **Where handouts come from:** the fine-tuned model in the Hugging Face Space `Sabrinaaaa/aphasia-friendly-docs` (see `../space/`).
  - The visitor's browser asks the Space directly, so no API key is needed.
  - The Space address is in `frontend/space_url.txt`.

## Speed

- **Fast first load.** The page loads with no heavy scripts. The PDF and Word readers (about 2 MB) download in the background after the page appears, and are used only when someone uploads those files.
- **Waking the model early.** Opening the page or the Make a Handout tab wakes the model, so it is usually ready by the time someone uploads.
- **Live preview.** Pages appear while the model is still writing.

## Review mode (for SLPs)

Under the upload box there's an optional link: "For speech-language pathologists: review mode." It asks for an access code (the Space's `REVIEWER_CODE`). With review mode on, an SLP can:

- write extra versions and switch between them
- correct any line
- choose the best version and rate it
- leave a comment

The review is saved to the private Hugging Face dataset `FEEDBACK_REPO`. The training notebook turns good reviews into new training examples (see `feedback_to_pairs.py`).

## Updating

- **The site:** run `python frontend/build_artifact.py` and push to GitHub. Vercel redeploys automatically.
- **The model:** retrain in Colab (the notebook can upload the new model for you), then restart the Space.
