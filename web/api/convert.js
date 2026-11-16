// The website's one server function: /api/convert
//
// The page sends the document text (or photos of the pages). This function adds the
// project's instructions, asks Claude with the site owner's API key, and streams the
// answer back. The key lives only in Vercel's settings (ANTHROPIC_API_KEY), never in
// the page or in GitHub.
//
// Settings (Vercel → Project → Settings → Environment Variables):
//   ANTHROPIC_API_KEY   required
//   ANTHROPIC_MODEL     optional, default claude-sonnet-5-5
//   HOURLY_LIMIT        optional, handouts per visitor per hour (default 10)
//   DAILY_LIMIT         optional, handouts per visitor per day (default 30)

const { systemText, taskText } = require("./_prompts.js");

const MODEL = process.env.ANTHROPIC_MODEL || "claude-sonnet-5-5";
const HOURLY = +process.env.HOURLY_LIMIT || 10;
const DAILY = +process.env.DAILY_LIMIT || 30;
const MAX_TEXT = 40000;          // characters of document text (~12 pages)
const MAX_IMAGES = 5;
const MAX_IMAGE_B64 = 1500000;   // ~1.1 MB per page picture
const TOKENS = { convert: 12000, fix: 12000, transcribe: 6000 };

// Visitor limits. Kept in memory, so they are a speed bump, not a wall: the real cost
// cap is the monthly spend limit set in the Anthropic Console.
const seen = new Map();
function overLimit(ip) {
  const now = Date.now();
  const times = (seen.get(ip) || []).filter((t) => now - t < 86400000);
  if (times.filter((t) => now - t < 3600000).length >= HOURLY || times.length >= DAILY) { seen.set(ip, times); return true; }
  times.push(now); seen.set(ip, times);
  if (seen.size > 5000) seen.delete(seen.keys().next().value);
  return false;
}

function fail(res, status, code) { res.status(status).json({ code }); }

module.exports = async function handler(req, res) {
  if (req.method !== "POST") { res.setHeader("Allow", "POST"); return fail(res, 405, "bad_request"); }
  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return fail(res, 500, "not_configured");

  // Only this site's own page may call it (stops other websites from using the key).
  const origin = req.headers.origin;
  if (origin && new URL(origin).host !== req.headers.host) return fail(res, 403, "bad_request");

  const b = req.body || {};
  const task = b.task;
  if (!["convert", "fix", "transcribe"].includes(task)) return fail(res, 400, "bad_request");
  if (task !== "transcribe") {
    if (typeof b.text !== "string" || b.text.trim().length < 20) return fail(res, 400, "bad_request");
    if (b.text.length > MAX_TEXT) return fail(res, 413, "prompt_too_large");
    if (b.lang && !["en", "es"].includes(b.lang)) return fail(res, 400, "bad_request");
  }
  if (task === "fix" && (typeof b.doc !== "object" || !Array.isArray(b.problems) || JSON.stringify(b.doc).length > 80000))
    return fail(res, 400, "bad_request");
  const images = task === "transcribe" ? b.images : null;
  if (images && (!Array.isArray(images) || !images.length || images.length > MAX_IMAGES ||
      images.some((s) => typeof s !== "string" || s.length > MAX_IMAGE_B64 || !/^[A-Za-z0-9+/=]+$/.test(s))))
    return fail(res, 400, "bad_request");

  // A "fix" is part of the same handout, so only new documents count toward the limit.
  const ip = String(req.headers["x-forwarded-for"] || "").split(",")[0].trim() || "unknown";
  if (task !== "fix" && overLimit(ip)) return fail(res, 429, "too_many");

  const data = {
    text: b.text, lang: b.lang || "", doc: b.doc, problems: (b.problems || []).map(String).slice(0, 60),
    source: String(b.source || "Uploaded document").slice(0, 120),
  };
  const content = [];
  if (images) images.forEach((d) => content.push({ type: "image", source: { type: "base64", media_type: "image/jpeg", data: d } }));
  content.push({ type: "text", text: taskText(task, data) });
  const body = { model: MODEL, max_tokens: TOKENS[task], stream: true, messages: [{ role: "user", content }] };
  // The rules and examples are the same every time, so Claude can cache them (cheaper and faster).
  if (task !== "transcribe") body.system = [{ type: "text", text: systemText(), cache_control: { type: "ephemeral" } }];

  const ctl = new AbortController();
  res.on("close", () => { if (!res.writableEnded) ctl.abort(); });   // the visitor pressed Stop or left
  let up;
  try {
    up = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST", signal: ctl.signal,
      headers: { "content-type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01" },
      body: JSON.stringify(body),
    });
  } catch { return fail(res, 502, "upstream_error"); }
  if (!up.ok) {
    const err = await up.text().catch(() => "");
    console.error("Anthropic error", up.status, err.slice(0, 500));
    const code = up.status === 429 ? "busy" : up.status === 529 ? "busy" : up.status === 413 ? "prompt_too_large"
      : up.status === 400 && /image/i.test(err) ? "image_rejected" : "upstream_error";
    return fail(res, up.status === 429 || up.status === 529 ? 503 : 502, code);
  }

  // Pass Claude's words through as they arrive, so the page can show progress.
  res.status(200);
  res.setHeader("Content-Type", "text/plain; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("X-Accel-Buffering", "no");
  const reader = up.body.getReader(), dec = new TextDecoder();
  let buf = "", stop = "";
  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      buf += dec.decode(value, { stream: true });
      let i;
      while ((i = buf.indexOf("\n")) >= 0) {
        const line = buf.slice(0, i).trim(); buf = buf.slice(i + 1);
        if (!line.startsWith("data:")) continue;
        let ev; try { ev = JSON.parse(line.slice(5)); } catch { continue; }
        if (ev.type === "content_block_delta" && ev.delta?.type === "text_delta") res.write(ev.delta.text);
        else if (ev.type === "message_delta" && ev.delta?.stop_reason) stop = ev.delta.stop_reason;
        else if (ev.type === "error") { console.error("Anthropic stream error", JSON.stringify(ev).slice(0, 500)); res.write("\u0000ERR:" + (/overloaded/.test(ev.error?.type) ? "busy" : "upstream_error")); }
      }
    }
    if (stop === "refusal") res.write("\u0000ERR:refused");
  } catch (e) {
    if (ctl.signal.aborted) return;
    res.write("\u0000ERR:upstream_error");
  }
  res.end();
};
