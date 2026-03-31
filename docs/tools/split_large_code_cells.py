#!/usr/bin/env python3
"""Split oversized code cells that contain # PART 1:, # PART 2:, ... or # ===== ... # PART markers."""

from pathlib import Path
import json
import re
import sys
from typing import List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
COURSES = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

MIN_LINES = 80
MIN_CHARS = 3500

# Rel paths under "Course XX/" to skip (e.g. known bad or already split).
BLOCKLIST = set()

PART_RE = re.compile(r"^#\s*PART\s+\d+\s*:", re.IGNORECASE)


def skip_rel(rel: str) -> bool:
    return "DOCS" in rel or "PROJECTS" in rel or ".ipynb_checkpoints" in rel


def partition_source(lines: List[str]) -> List[List[str]]:
    """Partition at # PART 2:, # PART 3:, ... First chunk = lines[0..i1] (includes any intro before PART 1)."""
    indices = []
    for i, line in enumerate(lines):
        s = line.strip()
        if PART_RE.search(s):
            indices.append(i)
    if len(indices) < 2:
        return []
    chunks = []
    for k in range(len(indices)):
        start = indices[k] if k > 0 else 0
        end = indices[k + 1] if k + 1 < len(indices) else len(lines)
        chunk = lines[start:end]
        if chunk:
            chunks.append(chunk)
    return chunks


def split_cell(cell: dict, lines: List[str]) -> Optional[List[dict]]:
    chunks = partition_source(lines)
    if not chunks:
        return None
    new_cells = []
    for ch in chunks:
        src = "".join(l if l.endswith("\n") else l + "\n" for l in ch)
        c = {"cell_type": "code", "metadata": {}, "source": [src], "outputs": [], "execution_count": None}
        if "metadata" in cell and isinstance(cell["metadata"], dict):
            c["metadata"] = {k: v for k, v in cell["metadata"].items() if k != "execution"}
        new_cells.append(c)
    return new_cells


def process_notebook(nb_path: Path, rel: str, course: str) -> List[Tuple[int, int]]:
    """Returns list of (cell_index, num_new_cells) for each split."""
    block_key = f"{course}/{rel}"
    if block_key in BLOCKLIST:
        return []
    try:
        with open(nb_path, encoding="utf-8") as f:
            nb = json.load(f)
    except json.JSONDecodeError:
        return []
    cells = nb["cells"]
    changed = False
    out = []
    i = 0
    while i < len(cells):
        c = cells[i]
        if c.get("cell_type") != "code":
            i += 1
            continue
        src = "".join(c.get("source", []))
        lines = src.splitlines(keepends=True)
        if not lines:
            i += 1
            continue
        n_lines = len(lines)
        n_chars = len(src)
        if n_lines < MIN_LINES and n_chars < MIN_CHARS:
            i += 1
            continue
        if not (PART_RE.search(src) or ("# " + "=" * 20 in src and "PART" in src)):
            i += 1
            continue
        replacement = split_cell(c, lines)
        if not replacement:
            i += 1
            continue
        # replace cell at i with replacement cells
        cells[i : i + 1] = replacement
        out.append((i, len(replacement)))
        changed = True
        i += len(replacement)
    if changed:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    return out


def run() -> List[Tuple[str, str, List[Tuple[int, int]]]]:
    report = []
    for c in COURSES:
        folder = ROOT / f"Course {c}"
        if not folder.is_dir():
            continue
        for nb_path in sorted(folder.rglob("*.ipynb")):
            rel = nb_path.relative_to(folder).as_posix()
            if skip_rel(rel):
                continue
            splits = process_notebook(nb_path, rel, c)
            if splits:
                report.append((c, rel, splits))
    return report


def main():
    global MIN_LINES, MIN_CHARS
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if "--min-lines" in sys.argv:
        idx = sys.argv.index("--min-lines") + 1
        if idx < len(sys.argv):
            MIN_LINES = int(sys.argv[idx])
    if "--min-chars" in sys.argv:
        idx = sys.argv.index("--min-chars") + 1
        if idx < len(sys.argv):
            MIN_CHARS = int(sys.argv[idx])
    r = run()
    print("Split large code cells report:")
    for course, rel, splits in r:
        total = sum(n for _, n in splits)
        print(f"  [Course {course}] {rel}: {len(splits)} cell(s) split -> {total} new cells")
        for ci, n in splits:
            print(f"    cell index {ci} -> {n} cells")
    if not r:
        print("  (no splits)")


if __name__ == "__main__":
    main()
