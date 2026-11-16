# The public website (Vercel)

This folder is the website version of the Aphasia Handout Maker. Anyone with the link can use it, with no Claude account.

| File | What it is |
|---|---|
| `index.html` | The page people see. Made by `python frontend/build_artifact.py`. Do not edit it by hand. |
| `api/convert.js` | The server part. It holds the API key, adds the project's instructions, asks Claude, and streams the answer back. |
| `api/_prompts.js` | The project's rules, examples and drawing names for the server. Made by the build script. |

## Setting it up (one time)

1. Sign in at vercel.com with your GitHub account.
2. Click **Add New → Project** and import `aphasia-friendly-docs`.
3. Set **Root Directory** to `web`. Leave the other settings as they are.
4. Under **Environment Variables**, add `ANTHROPIC_API_KEY` and paste your key as its value.
5. Click **Deploy**. Your link looks like `https://<project-name>.vercel.app`.

## Keeping costs safe

- **Set a monthly spend limit** in the Anthropic Console (Settings → Limits). This is the real cap.
- The site has these built-in limits:
  - each visitor can make 10 handouts per hour and 30 per day (best effort; change with `HOURLY_LIMIT` and `DAILY_LIMIT`)
  - documents are limited to 40,000 characters
  - photos are limited to 5 pages
  - only this site's own page can use the server
- A handout costs a few cents. The rules and examples are cached, so repeat requests cost less.

## Updating the site

Run `python frontend/build_artifact.py` and push to GitHub. Vercel redeploys automatically.

## Optional settings

| Variable | Default |
|---|---|
| `ANTHROPIC_MODEL` | `claude-sonnet-5-5` |
| `HOURLY_LIMIT` | `10` |
| `DAILY_LIMIT` | `30` |
