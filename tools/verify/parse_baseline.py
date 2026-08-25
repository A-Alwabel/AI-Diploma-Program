#!/usr/bin/env python3
"""Parse-only health sweep over every notebook in the repo.

For each .ipynb: load with nbformat (validates JSON/structure), then
syntax-compile every code cell (IPython magics and shell escapes are
stripped first, since they are valid at runtime but not plain Python).

Writes a sorted failure list to tools/verify/_baseline_parse_failures.txt.
Re-run any time; the reorg gate is "no NEW failures vs the committed baseline".
"""
import sys
from pathlib import Path

import nbformat

REPO = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", ".venv", "node_modules", ".ipynb_checkpoints", "__pycache__"}

def iter_notebooks(root: Path):
    for p in sorted(root.rglob("*.ipynb")):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p

def strip_magics(src: str) -> str:
    lines = src.splitlines()
    if lines and lines[0].lstrip().startswith("%%"):
        return ""  # cell magic: whole cell is not plain Python
    out = []
    depth = 0  # bracket depth: a "%" inside an open call is the format operator, not a magic
    for ln in lines:
        ls = ln.lstrip()
        if depth == 0 and ls.startswith(("%", "!")):
            out.append("pass")
        else:
            out.append(ln)
        # crude but sufficient: brackets outside strings dominate in notebook code
        depth += ln.count("(") + ln.count("[") + ln.count("{")
        depth -= ln.count(")") + ln.count("]") + ln.count("}")
        depth = max(depth, 0)
    return "\n".join(out)

def check(path: Path):
    try:
        nb = nbformat.read(path, as_version=4)
    except Exception as e:
        return f"NBFORMAT: {type(e).__name__}: {str(e)[:120]}"
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        src = strip_magics(cell.source or "")
        if not src.strip():
            continue
        try:
            compile(src, f"{path}::cell{i}", "exec")
        except SyntaxError as e:
            return f"SYNTAX cell {i}: {e.msg} (line {e.lineno})"
    return None

def main():
    failures = []
    total = 0
    for p in iter_notebooks(REPO):
        total += 1
        err = check(p)
        if err:
            failures.append((str(p.relative_to(REPO)), err))
    out = Path(__file__).parent / "_baseline_parse_failures.txt"
    with open(out, "w") as f:
        f.write(f"# parse baseline: {len(failures)} failures / {total} notebooks\n")
        for rel, err in failures:
            f.write(f"{rel}\t{err}\n")
    print(f"{len(failures)} failures / {total} notebooks -> {out.relative_to(REPO)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
