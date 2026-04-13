#!/usr/bin/env python3
"""
Apply J-line # comments to every code cell in student-facing Course 09 notebooks.

Scope: Course 09/unit*/**/*.ipynb (excludes Course 09/DOCS to avoid duplicate reference trees).

Usage (from repo root):
  python3 scripts/apply_j_line_comments_course09.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from j_line_annotate import process_notebook  # noqa: E402


def iter_course09_student_notebooks() -> list[Path]:
    base = ROOT / "Course 09"
    out: list[Path] = []
    for p in sorted(base.rglob("*.ipynb")):
        if "DOCS" in p.parts:
            continue
        out.append(p)
    return out


def main() -> None:
    notebooks = iter_course09_student_notebooks()
    total_changed = 0
    all_errors: list[str] = []
    touched = 0
    for nb in notebooks:
        n_cells, errs = process_notebook(nb)
        if n_cells:
            touched += 1
            total_changed += n_cells
        all_errors.extend(errs)
    print(f"notebooks scanned: {len(notebooks)}")
    print(f"notebooks modified: {touched}")
    print(f"code cells updated: {total_changed}")
    if all_errors:
        print(f"errors/warnings ({len(all_errors)}):")
        for e in all_errors[:80]:
            print(" ", e)
        if len(all_errors) > 80:
            print(f"  ... and {len(all_errors) - 80} more")


if __name__ == "__main__":
    main()
