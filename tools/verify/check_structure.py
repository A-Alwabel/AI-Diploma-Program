#!/usr/bin/env python3
"""Gate: per-course structural invariants after the 2026-08 reorg.

Per Course NN (01..12):
- exactly five unitN-* directories, N = 1..5, no duplicates
- each unit has README.md (warn) and examples/ with unique, gap-free
  ascending numeric prefixes starting at 00 or 01
- no stray artifacts: brace-dirs, 'Untitled', .ipynb_checkpoints,
  .DS_Store, __pycache__, mlruns, .pytest_cache
- QUIZZES/ exists with 5 quiz files (warn if fewer)
Errors exit 1; warnings only are exit 0.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
errors, warns = [], []

def check_course(cdir: Path):
    name = cdir.name
    units = sorted(d for d in cdir.iterdir() if d.is_dir() and re.match(r"unit\d", d.name))
    nums = [int(re.match(r"unit(\d)", d.name).group(1)) for d in units]
    if sorted(nums) != [1, 2, 3, 4, 5]:
        errors.append(f"{name}: unit set is {sorted(nums)} (dirs: {[d.name for d in units]})")
    for u in units:
        if not (u / "README.md").exists():
            warns.append(f"{name}/{u.name}: no README.md")
        ex = u / "examples"
        if not ex.is_dir():
            errors.append(f"{name}/{u.name}: no examples/")
            continue
        nbs = sorted(p.name for p in ex.glob("*.ipynb"))
        prefixes = []
        for nb in nbs:
            m = re.match(r"(\d{2})_", nb)
            if not m:
                errors.append(f"{name}/{u.name}: unnumbered notebook {nb}")
            else:
                prefixes.append(int(m.group(1)))
        if prefixes:
            if len(set(prefixes)) != len(prefixes):
                errors.append(f"{name}/{u.name}: duplicate numeric prefixes {prefixes}")
            start = min(prefixes)
            if start not in (0, 1):
                errors.append(f"{name}/{u.name}: numbering starts at {start:02d}")
            expected = list(range(start, start + len(prefixes)))
            if sorted(prefixes) != expected:
                errors.append(f"{name}/{u.name}: numbering has gaps {sorted(prefixes)}")
    for pat, label in [("{examples,exercises,solutions,quizzes,tests}", "brace-dir"),
                       ("Untitled", "stray Untitled"), (".ipynb_checkpoints", "checkpoints"),
                       (".DS_Store", ".DS_Store"), ("__pycache__", "__pycache__"),
                       ("mlruns", "mlruns"), (".pytest_cache", "pytest cache")]:
        for hit in cdir.rglob(pat):
            errors.append(f"{name}: {label} at {hit.relative_to(REPO)}")
    q = cdir / "QUIZZES"
    if q.is_dir():
        n = len(list(q.glob("[Qq]uiz*.md")))
        if n < 5:
            warns.append(f"{name}: only {n} quiz files in QUIZZES/")
    else:
        warns.append(f"{name}: no QUIZZES/")

def main():
    for i in range(1, 13):
        cdir = REPO / f"Course {i:02d}"
        if cdir.is_dir():
            check_course(cdir)
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\nstructure gate: {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
