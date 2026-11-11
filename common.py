"""Shared helpers: reading documents, parsing model output, flattening text."""
import json
import re
from pathlib import Path

KINDS = {"text", "step", "phone", "crisis", "checkbox", "blank"}
ROOT = Path(__file__).resolve().parent


def read_document(path):
    """Read a .txt/.md, .docx or .pdf file and return plain text."""
    p = Path(path)
    suffix = p.suffix.lower()
    if suffix == ".docx":
        import docx  # pip install python-docx
        d = docx.Document(str(p))
        parts = [para.text for para in d.paragraphs]
        for table in d.tables:
            for row in table.rows:
                parts.append(" | ".join(c.text for c in row.cells))
        return "\n".join(parts)
    if suffix == ".pdf":
        from pypdf import PdfReader  # pip install pypdf
        return "\n".join((pg.extract_text() or "") for pg in PdfReader(str(p)).pages)
    return p.read_text(encoding="utf-8")


def parse_model_json(raw):
    """Pull the JSON object out of a model reply (tolerates ```json fences and chatter)."""
    raw = raw.strip()
    raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw)
    start, end = raw.find("{"), raw.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("No JSON object found in model output")
    return json.loads(raw[start:end + 1])


def validate(doc):
    """Return a list of structural problems with an output JSON (empty list = OK)."""
    problems = []
    for key in ("title", "language", "pages"):
        if key not in doc:
            problems.append(f"missing '{key}'")
    for i, page in enumerate(doc.get("pages", []), 1):
        if not page.get("lines"):
            problems.append(f"page {i} has no lines")
        for j, line in enumerate(page.get("lines", []), 1):
            if line.get("kind") not in KINDS:
                problems.append(f"page {i} line {j}: unknown kind {line.get('kind')!r}")
            if not isinstance(line.get("text"), str):
                problems.append(f"page {i} line {j}: missing text")
    return problems


def strip_md(text):
    return text.replace("**", "")


def all_lines(doc):
    for page in doc.get("pages", []):
        for line in page.get("lines", []):
            yield page, line


def output_text(doc, include_title=True):
    """All visible text of an output document, markdown removed."""
    parts = [doc.get("title", "")] if include_title else []
    for page, line in all_lines(doc):
        parts.append(page.get("topic", ""))
        parts.append(strip_md(line.get("text", "")))
    return "\n".join(parts)
