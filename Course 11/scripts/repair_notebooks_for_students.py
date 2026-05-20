#!/usr/bin/env python3
"""Final student-path repairs: valid nbformat + clean exercises."""

from __future__ import annotations

import json
from pathlib import Path

COURSE11 = Path(__file__).resolve().parents[1]

CONTAMINATION_MARKERS = (
    "Part 1: Train and save a model",
    "Real-World Worked Example — Deploy a Trained Model",
    "Real-World Worked Example — MLflow Experiment Tracking",
    "Simulate the FastAPI serving code",
    "RUNS_LOG = pathlib.Path",
)


def is_student(path: Path) -> bool:
    return path.suffix == ".ipynb" and "DOCS" not in path.parts and any(
        p.startswith("unit") for p in path.parts
    )


def ensure_code_schema(cell: dict) -> bool:
    if cell.get("cell_type") != "code":
        return False
    changed = False
    if "outputs" not in cell:
        cell["outputs"] = []
        changed = True
    if "execution_count" not in cell:
        cell["execution_count"] = None
        changed = True
    if "metadata" not in cell:
        cell["metadata"] = {}
        changed = True
    src = cell.get("source")
    if isinstance(src, str):
        cell["source"] = [src if src.endswith("\n") else src + "\n"]
        changed = True
    elif isinstance(src, list):
        text = "".join(src)
        norm = [text if text.endswith("\n") else text + "\n"]
        if norm != src:
            cell["source"] = norm
            changed = True
    return changed


def clean_exercise_cells(cells: list[dict]) -> tuple[list[dict], bool]:
    if not cells:
        return cells, False
    new_cells = []
    removed = False
    for cell in cells:
        src = "".join(cell.get("source", [])) if isinstance(cell.get("source"), list) else str(
            cell.get("source", "")
        )
        if any(m in src for m in CONTAMINATION_MARKERS):
            removed = True
            continue
        new_cells.append(cell)
    return new_cells, removed


def main() -> int:
    touched = 0
    for path in sorted(COURSE11.rglob("*.ipynb")):
        if not is_student(path):
            continue
        nb = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        cells = nb.get("cells", [])
        if "exercises" in path.parts:
            cells, rem = clean_exercise_cells(cells)
            if rem:
                changed = True
        for cell in cells:
            if ensure_code_schema(cell):
                changed = True
        if changed:
            nb["cells"] = cells
            path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            touched += 1
            print(path.relative_to(COURSE11))
    print(f"repaired {touched}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
