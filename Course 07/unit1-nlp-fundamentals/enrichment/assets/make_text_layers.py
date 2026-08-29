#!/usr/bin/env python3
"""Generate the two simulated PDF text layers used by E16.

WHY THIS EXISTS
---------------
E16 must run offline on CPU with no downloads, so it cannot ship a real PDF and
a real extractor (pdftotext / PyMuPDF are not installed in the ai-diploma
environment). Instead we take a REAL document that is already in this
repository -- docs/QUICK_REFERENCE_GUIDE.md -- and render it into the two text
forms a PDF text extractor produces, reproducing the specific information
losses those tools are documented to suffer:

  raw   ("pdftotext" default)  : every glyph run in storage order, joined by
                                 single spaces and wrapped at 78 characters.
                                 All characters survive; ALL geometry is gone.
  layout("pdftotext -layout")  : character columns approximately preserved, and
                                 each cell wrapped WITHIN its own column, so one
                                 logical table row spans several physical lines
                                 with no marker saying so. Plus a running page
                                 header and a page footer between blocks.

Both files are checked in so the notebook reads them the way a real pipeline
reads its extractor's output. Re-run this script after editing the source
document:

    python make_text_layers.py

Nothing here is a model output. See README.md in this folder.
"""
import re
import textwrap
from pathlib import Path

SOURCE_REL = "docs/QUICK_REFERENCE_GUIDE.md"
SOURCE_LINES = 29                 # the "page" we treat as our document: the two semester tables
COLUMN_WIDTHS = [12, 26, 7, 6, 38]
RUNNING_HEADER = "AI Diploma - Quick Reference Guide"


def find_repo_root(start: Path) -> Path:
    for parent in [start, *start.parents]:
        if (parent / "Course 01").is_dir() and (parent / "Course 12").is_dir():
            return parent
    raise RuntimeError(f"Could not locate the repository root from {start}")


def parse_markdown_tables(lines):
    """Return [{heading, header, rows}] for every markdown table in `lines`."""
    tables, current, heading = [], None, None
    for line in lines:
        if line.startswith("### "):
            heading = line[4:].strip()
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue                                    # the |---|---| rule row
            cells = [re.sub(r"\*\*(.*?)\*\*", r"\1", c) for c in cells]   # drop bold markers
            if current is None:
                current = {"heading": heading, "header": cells, "rows": []}
            else:
                current["rows"].append(cells)
        elif current is not None:
            tables.append(current)
            current = None
    if current is not None:
        tables.append(current)
    return tables


def render_layout(table, page):
    """pdftotext -layout style: columns preserved, each cell wrapped inside its column."""
    def row_lines(cells):
        wrapped = [textwrap.wrap(c, w) or [""] for c, w in zip(cells, COLUMN_WIDTHS)]
        height = max(len(w) for w in wrapped)
        return [
            "".join((w[i] if i < len(w) else "").ljust(width + 2)
                    for w, width in zip(wrapped, COLUMN_WIDTHS)).rstrip()
            for i in range(height)
        ]

    out = [RUNNING_HEADER, "", table["heading"], ""]
    out += row_lines(table["header"])
    out.append("")
    for row in table["rows"]:
        out += row_lines(row)
    out += ["", f"AI Diploma  -  page {page}"]
    return "\n".join(out)


def render_raw(table, page):
    """pdftotext default: text in storage order, single-spaced, wrapped at 78 chars."""
    sequence = list(table["header"])
    for row in table["rows"]:
        sequence += row
    out = [RUNNING_HEADER, table["heading"]]
    out += textwrap.wrap(" ".join(sequence), 78)
    out.append(f"AI Diploma - page {page}")
    return "\n".join(out)


def main():
    here = Path(__file__).resolve().parent
    repo = find_repo_root(here)
    source = (repo / SOURCE_REL).read_text(encoding="utf-8").split("\n")[:SOURCE_LINES]
    tables = parse_markdown_tables(source)
    if len(tables) != 2 or any(len(t["rows"]) != 6 for t in tables):
        raise RuntimeError(f"{SOURCE_REL} no longer has the two 6-row semester tables this fixture expects")

    (here / "page_text_layer_layout.txt").write_text(
        "\n\n".join(render_layout(t, i + 3) for i, t in enumerate(tables)) + "\n", encoding="utf-8")
    (here / "page_text_layer_raw.txt").write_text(
        "\n\n".join(render_raw(t, i + 3) for i, t in enumerate(tables)) + "\n", encoding="utf-8")
    print("wrote page_text_layer_layout.txt and page_text_layer_raw.txt")


if __name__ == "__main__":
    main()
