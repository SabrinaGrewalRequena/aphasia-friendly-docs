// Shared by the Handout Maker page. Ports of factcheck.py and score.py, verified identical on all 150 pairs.
// ───────────────────────────── Fact check (port of factcheck.py) ─────────────────────────────
const MONTHS_EN = "(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)\\.?";
const MONTHS_ES = "(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)";
const DAYS = "(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|lunes|martes|miércoles|jueves|viernes|sábado|domingo)";
const UNITS = "(?:mg|mcg|µg|g|mL|ml|L|units?|unidades|IU|tablets?|tabletas?|pills?|pastillas?|capsules?|cápsulas?|puffs?|inhalaciones|drops?|gotas|teaspoons?|tsp|cucharaditas?|tablespoons?|tbsp|cucharadas?|patch(?:es)?|parches?)";
const STREET = "(?:Street|St\\.?|Avenue|Ave\\.?|Road|Rd\\.?|Boulevard|Blvd\\.?|Drive|Dr\\.?|Lane|Ln\\.?|Way|Court|Ct\\.?|Parkway|Pkwy\\.?|Place|Pl\\.?|Highway|Hwy\\.?)";
const W = "[\\p{L}\\p{N}_'’-]";
const PATTERNS = [
  ["phone", new RegExp("(?:\\+?1[\\s.-]?)?\\(?\\b\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}\\b|\\b(?:911|988|711|211)\\b", "g")],
  ["email", /\b[\w.+-]+@[\w-]+\.[\w.-]+\b/g],
  ["website", /\b(?:https?:\/\/|www\.)[^\s)<>]+|(?<![@\w.-])[\w-]+\.(?:org|gov|com|net|edu)(?:\/[^\s)<>]*)?/g],
  ["date", new RegExp(`\\b${DAYS},?\\s+${MONTHS_EN}\\s+\\d{1,2}(?:,\\s*\\d{4})?|\\b${MONTHS_EN}\\s+\\d{1,2}(?:st|nd|rd|th)?(?:,\\s*\\d{4})?|\\b\\d{1,2}\\s+de\\s+${MONTHS_ES}(?:\\s+de\\s+\\d{4})?|\\b\\d{1,2}/\\d{1,2}(?:/\\d{2,4})?\\b`, "gi")],
  ["time", /\b\d{1,2}(?::\d{2})?\s*(?:a\.?\s?m\.?|p\.?\s?m\.?|AM|PM)(?=\W|$)|\b\d{1,2}:\d{2}\b/gi],
  ["dose", new RegExp(`\\b\\d+(?:[.,]\\d+)?[ \\t]?${UNITS}\\b`, "gi")],
  ["name", new RegExp(`\\b(?:Dr|Dra|Mr|Mrs|Ms|Sr|Sra|Srta)\\.\\s+[A-ZÁÉÍÓÚÑ]${W}+(?:\\s+[A-ZÁÉÍÓÚÑ]${W}+)?`, "gu")],
  ["address", new RegExp(`\\b\\d{1,6}\\s+(?:[A-Z0-9][\\w.'-]*\\s+){1,4}${STREET}(?:,?\\s+(?:Suite|Ste\\.?|Room|Rm\\.?)\\s*\\w+)?|\\b(?:Calle|Avenida|Av\\.)\\s+[\\wÁÉÍÓÚÑáéíóúñ ]+?\\s+\\d+`, "g")],
];
const CRISIS = ["911", "988"];
const stripMd = (t) => String(t || "").replaceAll("**", "");
const norm = (s) => String(s).toLowerCase().replaceAll("’", "'").replace(/\b([ap])\.?\s?m\.?/g, "$1m").replace(/\s+/g, " ").trim();
const digits = (s) => String(s).replace(/\D/g, "");
const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
function allLines(doc) { const out = []; for (const p of doc.pages || []) for (const l of p.lines || []) out.push([p, l]); return out; }
function outputText(doc) {
  const parts = [doc.title || ""];
  for (const [p, l] of allLines(doc)) { parts.push(p.topic || ""); parts.push(stripMd(l.text)); }
  return parts.join("\n");
}
function extractFacts(text) {
  const facts = [], seen = new Set();
  for (const [type, re] of PATTERNS) {
    re.lastIndex = 0;
    for (const m of text.matchAll(re)) {
      const v = m[0].trim().replace(/[.,;]+$/, "");
      const key = type + "|" + norm(v);
      if (!seen.has(key)) { seen.add(key); facts.push({ type, value: v }); }
    }
  }
  return facts;
}
function numberTokens(text) {
  const t = text.replace(/^\s*(?:step|paso)?\s*\d{1,2}[.)]\s/gim, " ");
  return t.match(/\d[\d,.:/-]*\d|\d/g) || [];
}
function factCheck(original, doc) {
  const out = outputText(doc), outN = norm(out), outD = digits(out);
  const omittedN = norm((doc.omitted || []).join(" "));
  const facts = extractFacts(original).map((f) => {
    const v = f.value, words = v.split(/\s+/);
    let status;
    if (outN.includes(norm(v))) status = "ok";
    else if (["phone", "date", "time", "dose"].includes(f.type) && digits(v) && outD.includes(digits(v))) status = "reformatted";
    else if (f.type === "name" && words.length === 2 && new RegExp(`(?<![\\p{L}])${esc(norm(words[1]))}(?![\\p{L}])`, "u").test(outN)) status = "ok";
    else if (f.type === "name" && new RegExp(`(?<![\\p{L}])${esc(norm(words[0]))}\\s.*(?<![\\p{L}])${esc(norm(words.at(-1)))}(?![\\p{L}])`, "u").test(outN)) status = "ok";
    else if (omittedN.includes(norm(v)) && !CRISIS.includes(v)) status = "omitted";
    else status = "missing";
    return { ...f, status };
  });
  const origRuns = new Set(original.match(/\d+/g) || []);
  const added = [...new Set(numberTokens(out).filter((tok) => !(tok.match(/\d+/g) || []).every((r) => origRuns.has(r))))].sort();
  const crisis = [];
  for (const num of CRISIS) {
    if (new RegExp(`\\b${num}\\b`).test(original) &&
        !allLines(doc).some(([, l]) => l.kind === "crisis" && String(l.text || "").includes(num)))
      crisis.push(`${num} is in the original but not in an emergency box`);
  }
  const passed = facts.every((f) => f.status === "ok" || f.status === "omitted") && !added.length && !crisis.length;
  return { passed, facts, added, crisis };
}

// ───────────────────────────── Reading level + format (port of score.py) ─────────────────────────────
const READ_KINDS = new Set(["text", "step", "checkbox"]);
const CONNECTORS = new Set(["de", "del", "la", "las", "el", "los", "en", "y", "para", "of", "the", "and", "for", "in"]);
const PHONE_RE = /\(?\b\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b|\b(?:911|988)\b/;
const sentences = (t) => t.split(/(?<=[.!?])\s+|\n/).filter((s) => s.trim());
const words = (t) => t.match(/[\p{L}\p{N}_'’-]+/gu) || [];
function syllables(w, lang) {
  w = w.toLowerCase();
  let n = (w.match(lang === "es" ? /[aeiouáéíóúü]+/g : /[aeiouyáéíóúü]+/g) || []).length;
  if (lang !== "es" && w.endsWith("e") && !w.endsWith("le") && !w.endsWith("ee") && n > 1) n -= 1;
  return Math.max(n, 1);
}
function gradeLevel(text, lang) {
  const ss = sentences(text), ws = words(text).filter((w) => !/^\d+$/.test(w));
  if (!ss.length || !ws.length) return 0;
  const syl = ws.reduce((a, w) => a + syllables(w, lang), 0);
  const g = lang === "es"
    ? -0.205 * (100 * ss.length / ws.length) + 0.049 * (100 * syl / ws.length) - 3.407
    : 0.39 * (ws.length / ss.length) + 11.8 * (syl / ws.length) - 15.59;
  return Math.round(Math.max(g, 0) * 10) / 10;
}
function scoreDoc(doc) {
  const lang = doc.language || "en";
  const prose = allLines(doc).filter(([, l]) => READ_KINDS.has(l.kind))
    .map(([, l]) => stripMd(String(l.text || "").replace(/\*\*([^*]*[A-Z0-9ÁÉÍÓÚÑ][^*]*)\*\*/g, "")));
  const issues = [];
  (doc.pages || []).forEach((page, i) => {
    const lines = page.lines || [];
    const limit = lines.length && lines.every((l) => l.kind === "checkbox" || l.kind === "blank") ? 6 : 4;
    if (lines.length > limit) issues.push(`Page ${i + 1}: ${lines.length} lines (max ${limit})`);
    lines.forEach((l, j) => {
      const t = String(l.text || ""), n = words(stripMd(t)).length;
      if (READ_KINDS.has(l.kind) && n > 15) issues.push(`Page ${i + 1}, line ${j + 1}: ${n} words (max 15)`);
      if ((l.kind === "text" || l.kind === "step") && !t.includes("**")) issues.push(`Page ${i + 1}, line ${j + 1}: no bold key word`);
      if (READ_KINDS.has(l.kind) && PHONE_RE.test(t)) issues.push(`Page ${i + 1}, line ${j + 1}: phone number should be on its own line`);
      if (READ_KINDS.has(l.kind) && !l.picture) issues.push(`Page ${i + 1}, line ${j + 1}: no picture`);
      const factLine = /^\*\*[^*]+\*\*\.?$/.test(t.trim());
      const bolds = [...t.matchAll(/\*\*(.+?)\*\*/g)].map((m) => m[1])
        .filter((b) => !/[\d@]/.test(b) && !words(b).filter((w) => !CONNECTORS.has(w.toLowerCase())).every((w) => /^\p{Lu}/u.test(w)));
      if (bolds.length && !factLine && bolds.reduce((a, b) => a + words(b).length, 0) > Math.max(4, Math.floor(n / 2)))
        issues.push(`Page ${i + 1}, line ${j + 1}: too much bold`);
    });
  });
  const pages = doc.pages || [];
  if (pages.length && allLines(doc).some(([, l]) => l.kind === "phone" || l.kind === "crisis")) {
    const last = new Set((pages.at(-1).lines || []).map((l) => l.kind));
    if (!last.has("phone") && !last.has("crisis")) issues.push("Last page has no phone line (end with who can help)");
  }
  return { grade: gradeLevel(prose.join("\n"), lang), issues, pages: pages.length };
}

// ───────────────────────────── Reading the model's JSON (port of common.parse_model_json)
function closeBrackets(s) {
  const stack = []; let inStr = false, escp = false;
  for (const ch of s) {
    if (inStr) { escp = ch === "\\" && !escp; if (ch === '"' && !escp) inStr = false; continue; }
    if (ch === '"') inStr = true;
    else if (ch === "[" || ch === "{") stack.push(ch === "[" ? "]" : "}");
    else if ((ch === "]" || ch === "}") && stack.length) stack.pop();
  }
  if (inStr) throw new Error("cut off inside text");
  return s + stack.reverse().join("");
}
function parseModelJson(raw) {
  raw = raw.trim().replace(/^```(?:json)?\s*|\s*```$/g, "");
  const a = raw.indexOf("{"), b = raw.lastIndexOf("}");
  if (a < 0 || b < 0) throw new Error("no JSON found");
  try { return JSON.parse(raw.slice(a, b + 1)); }
  catch {
    const doc = JSON.parse(closeBrackets(raw.slice(a, b + 1)));
    (doc.notes_for_reviewer ||= []).push("The answer was cut off at the very end and closing brackets were added. Check the last page.");
    return doc;
  }
}
