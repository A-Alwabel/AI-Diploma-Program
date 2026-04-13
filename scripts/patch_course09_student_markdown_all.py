#!/usr/bin/env python3
"""
Student-facing markdown pass for all Course 09 student notebooks (excludes DOCS/).

- Appends ### If Python feels hard right now under ## Lesson Brief or ## Exercise Brief.
- Replaces *generic* ### Step Guide blocks using hints from the following code cell.
- Appends **For weaker coders:** to ## Closing Takeaway when missing.

Idempotent: safe to re-run.

Usage (repo root): python3 scripts/patch_course09_student_markdown_all.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "Course 09"

WEAK_BLOCK = """### If Python feels hard right now

- Run code cells **from top to bottom** the first time; later you can re-run one cell after you change it.
- In code cells, a line that starts with `# ` (hash + space) is a **hint for the very next line**—read the hint, then read the code under it.
- You do **not** need to memorize syntax. Follow the story: *what is stored*, *what gets printed*, and *what the plot is trying to show*.
- If something errors, read the last line of the red traceback first—it usually names the problem in plain language.
"""

CLOSING_WEAK = """**For weaker coders:** After you run the important cells, write one sentence: *what number or plot changed, and does that match what the lesson said should happen?* If not, re-read only the `#` hint lines in that cell—not every line of Python."""

GENERIC_SNIPPETS = (
    "This cell runs a worked example and shows the result through printed values, tables, or plots.",
    "This cell advances the next step of the notebook workflow.",
    "This cell turns the lesson outputs into a final visual recap.",
)


def _cell_text(cell: dict) -> str:
    return "".join(cell.get("source", []))


def _set_text(cell: dict, text: str) -> None:
    if not text.endswith("\n"):
        text += "\n"
    cell["source"] = text.splitlines(keepends=True)


def _ensure_weak_brief(nb: dict) -> bool:
    changed = False
    for cell in nb["cells"]:
        if cell.get("cell_type") != "markdown":
            continue
        src = _cell_text(cell)
        if "### If Python feels hard" in src:
            continue
        if "## Lesson Brief" in src or "## Exercise Brief" in src:
            _set_text(cell, src.rstrip() + "\n\n" + WEAK_BLOCK.strip() + "\n")
            changed = True
    return changed


def _ensure_closing_weak(nb: dict) -> bool:
    changed = False
    for cell in nb["cells"]:
        if cell.get("cell_type") != "markdown":
            continue
        src = _cell_text(cell)
        if "## Closing Takeaway" not in src:
            continue
        if "**For weaker coders:**" in src:
            continue
        _set_text(cell, src.rstrip() + "\n\n" + CLOSING_WEAK + "\n")
        changed = True
    return changed


def _first_print_title(code: str) -> str | None:
    for m in re.finditer(r'print\(\s*["\']([^"\']+)["\']', code):
        t = m.group(1).strip()
        if len(t) > 3 and not t.startswith("\\n"):
            return t[:120]
    return None


def _sniff_code_purpose(code: str) -> str:
    lines = code.splitlines()[:45]
    joined = "\n".join(lines)
    for ln in lines:
        s = ln.strip()
        if s.startswith("# CELL:"):
            return s.replace("# CELL:", "").strip()[:200]
        if s.startswith("# Setup step:"):
            if "%pip" in joined or "pip install" in joined:
                return "Install or import dependencies so later cells can run."
            return "Import libraries and set small global constants for the lesson."
        if s.startswith("# Worked example:"):
            return "Run a worked scenario step by step; compare each print to the markdown theory."
        if s.startswith("# Teaching note:"):
            return "Build the next chunk of the lesson (often a function, table, or training loop)."
        if s.startswith("# Final computation:"):
            return "Summarize or compare results (policies, returns, tables) for the lesson goal."
        if s.startswith("# Visual recap:"):
            return "Try to auto-plot lesson numbers already in memory (optional recap charts)."
        if s.startswith("# Helper function:"):
            return "Define a helper you can read in one place before it is used later."
    pt = _first_print_title(code)
    if pt:
        return f'Follow the printed section: "{pt}"'
    if "gym.make" in joined or "gymnasium" in joined:
        return "Create or step through a Gymnasium environment (reset/step loop)."
    if "torch" in joined.lower() or "nn." in joined:
        return "PyTorch-heavy block (network, loss, or training step)—read shapes and prints first."
    return "Run this cell once, then read the output before worrying about every line of code."


def _sniff_kind(code: str) -> str:
    head = "\n".join(code.splitlines()[:30])
    if "# Visual recap:" in head or "Visual recap:" in head:
        return "recap"
    if "%pip" in head or "pip install" in head:
        return "pip"
    if "# Setup step:" in head and "import" in head:
        return "setup"
    if "# Final computation:" in head:
        return "final"
    return "default"


def _build_step_guide(code: str) -> str:
    purpose = _sniff_code_purpose(code)
    kind = _sniff_kind(code)

    if kind == "recap":
        expect = "Either one or more plots, or a short message that nothing was auto-plotted."
        lost = "Re-run the main lesson cells so numeric variables exist, then try this recap again."
    elif kind == "pip":
        expect = "Pip progress lines and usually a confirmation that imports work."
        lost = "Fix any red install error before continuing—later cells assume this cell succeeded."
    elif kind == "final":
        expect = "Tables, arrays, or comparison prints showing which policy or method wins."
        lost = "If output is empty, run the previous cells that define the data this cell consumes."
    else:
        expect = "Printed numbers, small tables, logs, or figures tied to the current section header."
        lost = "Skim only the `#` lines in the next cell, run it once, then re-read the same hints with the output visible."

    return f"""### Step Guide

**What this cell does:** {purpose}

**How to read it (weak Python OK):** Read the `#` hint lines in the next cell top-to-bottom, run it once, then look at the output before diving into implementation details.

**What to expect in the output:** {expect}

**If you feel lost:** {lost}
"""


def _is_generic_step(src: str) -> bool:
    if "### Step Guide" not in src:
        return False
    return any(s in src for s in GENERIC_SNIPPETS)


def _skip_heuristic_step_upgrade(path: Path) -> bool:
    """Unit 1 example notebooks use hand-written Step Guides; do not overwrite them."""
    try:
        rel = path.relative_to(COURSE)
    except ValueError:
        return False
    parts = rel.parts
    return (
        len(parts) >= 3
        and parts[0] == "unit1-rl-fundamentals"
        and parts[1] == "examples"
        and path.suffix == ".ipynb"
    )


def _upgrade_step_guides(nb: dict, path: Path) -> bool:
    if _skip_heuristic_step_upgrade(path):
        return False
    changed = False
    cells = nb["cells"]
    for i, cell in enumerate(cells):
        if cell.get("cell_type") != "markdown":
            continue
        src = _cell_text(cell)
        if not _is_generic_step(src):
            continue
        code = ""
        j = i + 1
        while j < len(cells) and j <= i + 8:
            if cells[j].get("cell_type") == "code":
                cand = _cell_text(cells[j])
                if cand.strip():
                    code = cand
                    break
            j += 1
        if not code.strip():
            continue
        new_md = _build_step_guide(code)
        if new_md.strip() == src.strip():
            continue
        _set_text(cell, new_md)
        changed = True
    return changed


def iter_student_notebooks() -> list[Path]:
    out: list[Path] = []
    for p in sorted(COURSE.rglob("*.ipynb")):
        if "DOCS" in p.parts:
            continue
        out.append(p)
    return out


def main() -> None:
    paths = list(iter_student_notebooks())
    touched = 0
    for path in paths:
        nb = json.loads(path.read_text(encoding="utf-8"))
        c1 = _ensure_weak_brief(nb)
        c2 = _upgrade_step_guides(nb, path)
        c3 = _ensure_closing_weak(nb)
        if c1 or c2 or c3:
            path.write_text(json.dumps(nb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            touched += 1
    print(f"notebooks scanned: {len(paths)}")
    print(f"notebooks modified: {touched}")


if __name__ == "__main__":
    main()
