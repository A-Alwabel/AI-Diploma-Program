#!/usr/bin/env python3
"""Append a short end-of-notebook self-check for comprehension (student-facing).

Idempotent via marker ``STUDENT_SELF_CHECK_COURSE09`` in a markdown cell.
"""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbformat.v4 import new_markdown_cell

MARKER = "STUDENT_SELF_CHECK_COURSE09"

MD = f"""## Did you understand? (about 2 minutes)

<!-- {MARKER} -->

Answer **without scrolling** first. Then scroll only to compare with the notebook.

1. **One sentence:** What is the *single main idea* you are supposed to carry to the next lesson?
2. **Trace one step:** Pick one moment from this notebook (a number you printed, a plot, a table, or a GIF/slider frame). Write **state → action → reward → next state** in your own words — even if your “state” is a vector or a tile index.
3. **One honest confusion:** Write one question you still have. That question is what you should bring to class, study group, or office hours.

**If any answer is blank:** run the notebook again from the top **slowly** (run one cell → read the output → only then run the next).

**Remember:** a clean run means the code worked — it does **not** automatically mean every idea clicked. Confusion is normal until you can do steps 1–2 in plain language.
"""


def discover_notebooks(course09: Path) -> list[Path]:
    out: list[Path] = []
    for p in sorted(course09.rglob("*.ipynb")):
        if "DOCS" in p.parts:
            continue
        if "unit" not in str(p):
            continue
        out.append(p)
    return out


def notebook_text(nb: nbformat.NotebookNode) -> str:
    parts: list[str] = []
    for cell in nb.cells:
        src = cell.get("source", "")
        if isinstance(src, list):
            parts.append("".join(src))
        else:
            parts.append(str(src))
    return "\n".join(parts)


def main() -> int:
    course09 = Path(__file__).resolve().parents[1]
    added = 0
    skipped = 0
    for path in discover_notebooks(course09):
        nb = nbformat.read(path, as_version=4)
        if MARKER in notebook_text(nb):
            skipped += 1
            continue
        nb.cells.append(new_markdown_cell(MD))
        nbformat.write(nb, path)
        added += 1
        print("appended", path.relative_to(course09))
    print(f"added={added} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
