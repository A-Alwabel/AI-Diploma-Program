#!/usr/bin/env python3
"""
Apply J-line # comments to every code cell in student-facing Course 09 notebooks.

Scope: Course 09/unit*/**/*.ipynb (excludes Course 09/DOCS to avoid duplicate reference trees).

Usage (from repo root):
  python3 scripts/apply_j_line_comments_course09.py
  python3 scripts/apply_j_line_comments_course09.py --notebook Course 09/.../lesson.ipynb --cell 8
"""
from __future__ import annotations

import argparse
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
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--notebook",
        type=Path,
        metavar="PATH",
        help="Process a single .ipynb under Course 09 (repo-relative or absolute).",
    )
    ap.add_argument(
        "--cell",
        type=int,
        action="append",
        dest="cells",
        metavar="INDEX",
        help="0-based notebook cell index to rewrite (repeatable). Only with --notebook.",
    )
    args = ap.parse_args()

    only_cells: set[int] | None = None
    if args.cells is not None:
        only_cells = set(args.cells)
        if args.notebook is None:
            ap.error("--cell requires --notebook")

    if args.notebook is not None:
        nb_path = args.notebook if args.notebook.is_absolute() else ROOT / args.notebook
        try:
            nb_path = nb_path.resolve()
        except OSError:
            ap.error(f"invalid notebook path: {args.notebook}")
        if "Course 09" not in nb_path.parts or "DOCS" in nb_path.parts:
            ap.error("notebook must be under Course 09/ and not under DOCS/")
        if nb_path.suffix != ".ipynb":
            ap.error("notebook must be a .ipynb file")
        notebooks = [nb_path]
    else:
        if only_cells is not None:
            ap.error("--cell without --notebook is not supported (ambiguous across files)")
        notebooks = iter_course09_student_notebooks()

    total_changed = 0
    all_errors: list[str] = []
    touched = 0
    for nb in notebooks:
        n_cells, errs = process_notebook(nb, only_cell_indices=only_cells)
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
