#!/usr/bin/env python3
"""Polish Course 11 student-path notebooks for classroom use.

- English-only student copy
- One clear opening (Lesson Brief) and Closing Takeaway
- Remove duplicate headers and boilerplate I/O cells
- Fix exercise cells (TODO in code cells, not markdown)
- Optional self-check section (idempotent)

Run from repo root:

    python3 "Course 11/scripts/polish_student_materials.py"
"""

from __future__ import annotations

import json
import re
from pathlib import Path

COURSE11 = Path(__file__).resolve().parents[1]
ARABIC_RE = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+")
MARKER_SELF_CHECK = "STUDENT_SELF_CHECK_COURSE11"
MARKER_LESSON_BRIEF = "LESSON_BRIEF_COURSE11"

SELF_CHECK_MD = f"""## Did you understand? (about 2 minutes)

<!-- {MARKER_SELF_CHECK} -->

Answer **without scrolling** first, then compare with the notebook.

1. **One sentence:** What is the main deployment idea this notebook taught?
2. **Trace one step:** Name one artifact (file, API route, container, or metric) and what role it plays in production.
3. **One question:** What would you ask if you had to deploy this for real users tomorrow?

If any answer is blank, re-run the notebook slowly (one cell → read output → next cell).
"""

UNIT_WHY = {
    "unit1": "Students learn to package models and expose them locally before any cloud complexity.",
    "unit2": "Students learn how serving, versioning, and inference modes differ in real systems.",
    "unit3": "Students learn how managed cloud platforms change ops, security, and monitoring.",
    "unit4": "Students learn reproducible environments with Docker, Kubernetes, and CI/CD.",
    "unit5": "Students learn to keep models healthy after launch (monitoring, drift, retraining).",
}


def is_student_nb(path: Path) -> bool:
    if path.suffix != ".ipynb":
        return False
    if "DOCS" in path.parts or "solutions" in path.parts:
        return False
    return any(part.startswith("unit") for part in path.parts)


def is_numbered_example(path: Path) -> bool:
    return "examples" in path.parts and re.match(r"^\d{2}_", path.name)


def is_exercise(path: Path) -> bool:
    return "exercises" in path.parts


def human_title(stem: str) -> str:
    base = stem.replace(".ipynb", "")
    if "_" in base:
        prefix, rest = base.split("_", 1)
        if prefix.isdigit():
            base = rest
    return base.replace("_", " ").strip().title()


def dearabize(text: str) -> str:
    text = re.sub(r"\|\s*[^\n|]*[\u0600-\u06FF][^\n|]*", "", text)
    text = ARABIC_RE.sub("", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def is_boilerplate_io(src: str) -> bool:
    s = src.lower()
    return "inputs & outputs" in s or "المدخلات" in s or (
        "what we use in this notebook" in s and len(src) < 600
    )


def is_official_structure_block(src: str) -> bool:
    return "Official Structure Reference" in src or "DETAILED_UNIT_DESCRIPTIONS" in src


def is_duplicate_title(cell_src: str, title: str) -> bool:
    first_line = cell_src.strip().split("\n", 1)[0].lower()
    t = title.lower()
    return first_line.startswith("#") and (t in first_line or first_line.replace("#", "").strip() in t)


def lesson_brief(title: str, unit_key: str, numbered: bool, exercise: bool = False) -> str:
    why = UNIT_WHY.get(unit_key, "This notebook builds production deployment skills step by step.")
    kind = "exercise" if exercise else "example"
    return f"""# Lesson Brief — {title}
<!-- {MARKER_LESSON_BRIEF} -->

**What you will do:** Work through this {kind} top to bottom. Read each section header before running the next code cell.

**Why it matters:** {why}

**How to run:** Use Python 3.10+. Run cells in order. If you change data or a model above, use **Kernel → Restart & Run All** before trusting later cells.

**Stuck?** See `Course 11/START_HERE.md` and `Course 11/DOCS/REQUIREMENTS_COURSE_11.md`.

---
"""


def closing_takeaway(title: str) -> str:
    return f"""---

## Closing Takeaway — {title}

You finished the core workflow in this notebook. Before moving on, say in your own words:

- What **artifact** did you create or load (pickle, ONNX, API, image, log file)?
- Who or what **calls** it in production (user app, batch job, orchestrator)?
- What would you **check** if predictions suddenly got worse?

Carry that sentence to the next numbered notebook in the unit README.
"""


def markdown_cell(text: str, meta: dict | None = None) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": meta or {},
        "source": [text if text.endswith("\n") else text + "\n"],
    }


def code_cell(text: str) -> dict:
    return {
        "cell_type": "code",
        "metadata": {},
        "source": [text if text.endswith("\n") else text + "\n"],
        "outputs": [],
        "execution_count": None,
    }


def normalize_setup_pip(src: str) -> str:
    return src.replace("pickle5", "pickle").replace("pip install pickle ", "pip install ")


def should_be_code_cell(src: str) -> bool:
    s = src.strip()
    if not s:
        return False
    if s.startswith("#") and "TODO" not in s and "YOUR CODE" not in s:
        return False
    markers = ("TODO", "YOUR CODE HERE", "%pip", "import ", "print(")
    return any(m in s for m in markers)


def polish_cells(cells: list[dict], path: Path) -> tuple[list[dict], list[str]]:
    changes: list[str] = []
    title = human_title(path.stem)
    unit_key = next((p[:5] for p in path.parts if p.startswith("unit")), "unit1")
    numbered = is_numbered_example(path)
    exercise = is_exercise(path)

    cleaned: list[dict] = []
    for cell in cells:
        src = dearabize("".join(cell.get("source", [])))
        if not src.strip():
            changes.append("dropped empty cell")
            continue
        if is_boilerplate_io(src) or is_official_structure_block(src):
            changes.append("removed boilerplate block")
            continue
        cell = dict(cell)
        if cell.get("cell_type") == "code":
            src = normalize_setup_pip(src)
        cell["source"] = [src + ("\n" if not src.endswith("\n") else "")]
        cleaned.append(cell)

    # Merge duplicate opening headers (first 4 cells)
    if cleaned and cleaned[0].get("cell_type") == "markdown":
        i = 1
        while i < min(4, len(cleaned)):
            if cleaned[i].get("cell_type") != "markdown":
                break
            src_i = "".join(cleaned[i].get("source", []))
            if is_duplicate_title(src_i, title) or (
                src_i.strip().startswith("#") and "Learning Objectives" in src_i
            ):
                changes.append("removed duplicate header")
                cleaned.pop(i)
                continue
            i += 1

    full_text = "\n".join("".join(c.get("source", [])) for c in cleaned)

    if MARKER_LESSON_BRIEF not in full_text:
        cleaned.insert(0, markdown_cell(lesson_brief(title, unit_key, numbered, exercise)))
        changes.append("added lesson brief")

    # Convert mistaken markdown TODO blocks to code
    new_cleaned: list[dict] = []
    for cell in cleaned:
        src = "".join(cell.get("source", []))
        if cell.get("cell_type") == "markdown" and should_be_code_cell(src):
            new_cleaned.append(code_cell(src))
            changes.append("markdown TODO → code cell")
        else:
            new_cleaned.append(cell)
    cleaned = new_cleaned

    # Exercise: ensure at least one setup code cell after brief
    if exercise:
        has_code = any(c.get("cell_type") == "code" for c in cleaned)
        if not has_code:
            setup = code_cell(
                "%pip install numpy scikit-learn joblib onnx onnxruntime fastapi uvicorn -q\n"
                "print('Setup complete — fill in the TODO sections below.')"
            )
            cleaned.insert(1, setup)
            changes.append("added exercise setup cell")

    full_text = "\n".join("".join(c.get("source", [])) for c in cleaned)
    if "Closing Takeaway" not in full_text and "Summary" not in full_text:
        cleaned.append(markdown_cell(closing_takeaway(title)))
        changes.append("added closing takeaway")

    if numbered and MARKER_SELF_CHECK not in full_text:
        cleaned.append(markdown_cell(SELF_CHECK_MD))
        changes.append("added self-check")

    return cleaned, changes


def polish_notebook(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    cells, changes = polish_cells(data.get("cells", []), path)
    if not changes:
        return []
    data["cells"] = cells
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return changes


def main() -> int:
    touched = 0
    for nb in sorted(COURSE11.rglob("*.ipynb")):
        if not is_student_nb(nb):
            continue
        changes = polish_notebook(nb)
        if changes:
            touched += 1
            print(f"{nb.relative_to(COURSE11)}: {', '.join(sorted(set(changes)))}")
    print(f"\nPolished {touched} notebooks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
