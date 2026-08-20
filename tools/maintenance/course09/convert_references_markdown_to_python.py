#!/usr/bin/env python3
"""
Convert Markdown '## 📚 References …' blocks to a small Python cell using
IPython.display.Markdown so editors/kernels cannot execute **Books:** as Python.

Idempotent: skips cells that already look like the generated pattern.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

MARKER = "## 📚 References"
SKIP_PREFIX = "# References (shown with Markdown inside a Python cell"


def _soften_reference_markdown(md: str) -> str:
    """Use ### headings instead of **Labels:** so accidental 'run as code' fails less badly."""
    out = md
    out = out.replace("**Books:**", "### Books")
    out = out.replace("**Papers:**", "### Papers")
    out = out.replace("**State-of-the-Art:**", "### State-of-the-art")
    return out


def _cell_text(cell: dict) -> str:
    return "".join(cell.get("source", []))


def _set_source(cell: dict, text: str) -> None:
    lines = text.splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    cell["source"] = lines


def _make_refs_code_cell(refs_md: str) -> dict:
    body = _soften_reference_markdown(refs_md.strip())
    if '"""' in body:
        raise ValueError("References block contains triple-double-quotes; fix manually.")
    # One string per line avoids a giant r"""…""" block (easier to diff; no raw ** in the cell).
    quoted = ",\n".join("        " + json.dumps(line, ensure_ascii=False) for line in body.split("\n"))
    code = (
        "# References (shown with Markdown inside a Python cell — avoids SyntaxError if a Markdown block is run as code.)\n"
        "from IPython.display import Markdown, display\n\n"
        "_md_refs = \"\\n\".join(\n"
        "    [\n"
        f"{quoted},\n"
        "    ]\n"
        ")\n"
        "display(Markdown(_md_refs))\n"
    )
    lines = code.splitlines(keepends=True)
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": lines,
    }


def convert_notebook(path: Path) -> bool:
    nb = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    i = 0
    while i < len(nb["cells"]):
        cell = nb["cells"][i]
        if cell.get("cell_type") != "markdown":
            i += 1
            continue
        text = _cell_text(cell)
        if MARKER not in text:
            i += 1
            continue

        idx = text.find(MARKER)
        before = text[:idx].rstrip()
        refs_md = text[idx:].strip()

        # Next cell already our Python refs cell (already converted)
        if i + 1 < len(nb["cells"]):
            nxt = nb["cells"][i + 1]
            if nxt.get("cell_type") == "code":
                ntxt = _cell_text(nxt)
                if SKIP_PREFIX in ntxt and MARKER in ntxt and (
                    "display(Markdown(r\"\"\"" in ntxt or "_md_refs" in ntxt
                ):
                    i += 1
                    continue

        if before:
            _set_source(cell, before + "\n")
            nb["cells"].insert(i + 1, _make_refs_code_cell(refs_md))
            i += 2
        else:
            nb["cells"][i] = _make_refs_code_cell(refs_md)
            i += 1
        changed = True

    if changed:
        path.write_text(json.dumps(nb, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    changed_files: list[Path] = []
    for path in sorted(root.rglob("*.ipynb")):
        rel = path.relative_to(root)
        if "REFERENCE_NOTEBOOKS" in rel.parts:
            continue
        try:
            if convert_notebook(path):
                changed_files.append(path)
        except Exception as e:
            print(f"FAIL {path}: {e}", file=sys.stderr)
            return 1
    for p in changed_files:
        print(p.relative_to(root))
    print(f"Updated {len(changed_files)} notebook(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
