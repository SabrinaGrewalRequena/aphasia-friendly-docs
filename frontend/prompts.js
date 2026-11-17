// The instructions sent to Claude by the Claude page (inside claude.ai). The public
// website doesn't use them: its fine-tuned model has the rules built in (see space/).
// Needs RULES, EXAMPLES and ICONS to be defined first.

const ICON_RULE = "\n\n# Pictures\nEvery line has \"picture\" (a short word) AND \"icon\": the NAME of the drawing below that best shows that line's meaning. Use only names from this list, exactly as written. Use \"\" for both when a line needs no picture.\n\nDrawings (name: what it shows):\n" +
  Object.entries(ICONS).map(([n, v]) => `${n}: ${v.label}`).join("\n");

const TRANSCRIBE = "These images are pages of a health document. Copy ALL of its text exactly, word for word, keeping every name, date, time, dose, address and phone number unchanged. Keep the reading order. Reply with only the text.";

function userMessage(text, source, lang) {
  const target = lang ? `Write the output in ${lang === "es" ? "Spanish" : "English"}.\n` : "";
  return `${target}Source name: ${source}\n\nOriginal document:\n<<<\n${String(text).trim()}\n>>>`;
}

// The part that never changes: rules, drawings and two worked examples.
function systemText() {
  let p = RULES + ICON_RULE + "\n\n# Examples\n";
  EXAMPLES.forEach((ex, i) => { p += `\n## Example ${i + 1}: input\n${userMessage(ex.original, ex.source, "")}\n\n## Example ${i + 1}: output\n${JSON.stringify(ex.target)}\n`; });
  return p;
}

// The part for this one document. task: "convert" | "fix" | "transcribe".
function taskText(task, d) {
  if (task === "transcribe") return TRANSCRIBE;
  if (task === "fix") {
    const problems = (d.problems || []).map((p) => "- " + p).join("\n");
    return `# Your task\nA handout was made from the original below and the safety check found problems. Fix ONLY these and keep everything else the same. A missing fact must be copied exactly, or listed in "omitted" with a reason if the reader does not need it.\n\nProblems:\n${problems}\n\nOriginal document:\n<<<\n${String(d.text).trim()}\n>>>\n\nCurrent handout JSON:\n${JSON.stringify(d.doc)}\n\nReply with only the corrected JSON object.`;
  }
  return `# Your task\n${userMessage(d.text, d.source, d.lang)}\n\nReply with only the JSON object.`;
}
