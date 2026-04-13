#!/usr/bin/env python3
"""
Option ج (legacy entry): same annotator as Course 09, but only for selected cells
in 03_value_iteration.ipynb. Prefer: python3 scripts/apply_j_line_comments_course09.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from j_line_annotate import process_notebook  # noqa: E402

NB = ROOT / "Course 09/unit1-rl-fundamentals/examples/03_value_iteration.ipynb"
TARGET_CELLS = {8, 11, 14, 16}


def main() -> None:
    changed, errs = process_notebook(NB, only_cell_indices=TARGET_CELLS)
    print("updated", NB, "cells", sorted(TARGET_CELLS), "code_cells_changed", changed)
    for e in errs:
        print(e)


if __name__ == "__main__":
    main()
