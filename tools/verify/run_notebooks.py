#!/usr/bin/env python3
"""Batch-execute student-path notebooks for one course (or a file list).

Generalizes Course 09/Course 11's verify_student_notebooks.py:
- targets unit*/examples, unit*/exercises and unit*/enrichment notebooks (skips solutions/, DOCS/)
- executes each notebook with its own directory as cwd
- writes outputs IN PLACE by default (project rule: students see real outputs);
  use --check-only to execute to a throwaway copy instead
- per-notebook timeout, summary log

EXPECTED FAILURES
-----------------
A handful of notebooks teach what happens when code stops working, so their authored
end-state INCLUDES a failure. Mark such a cell with the standard nbconvert/nbclient
cell tag:

    cell.metadata.tags = ["raises-exception"]

nbconvert then records the error in the notebook's outputs and carries on instead of
aborting the run. This script adds the half nbconvert does not do, so the tag makes the
gate stronger rather than weaker:

  * a cell tagged `raises-exception` that did NOT raise is a FAILURE
    (otherwise a deliberate-failure demo can silently stop demonstrating anything)
  * a cell with an error output that is NOT tagged is a FAILURE
    (catches a stray traceback committed by accident)

Usage:
  python tools/verify/run_notebooks.py --course "Course 01" [--check-only]
  python tools/verify/run_notebooks.py --files a.ipynb b.ipynb
"""
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

# Headless-safe SDL for gymnasium/pygame rendering: avoids intermittent
# crashes from the homebrew-vs-bundled libSDL2 double load on macOS.
ENV = {**os.environ, "SDL_VIDEODRIVER": "dummy", "SDL_AUDIODRIVER": "dummy"}

REPO = Path(__file__).resolve().parents[2]
PY = sys.executable

def student_notebooks(course_dir: Path):
    for pattern in ("unit*/examples/*.ipynb", "unit*/exercises/*.ipynb", "unit*/enrichment/*.ipynb"):
        yield from sorted(course_dir.glob(pattern))

CHECK_DIR = Path("/tmp/nbcheck")

def audit_failures(executed: Path) -> str:
    """Compare a notebook's error outputs against its `raises-exception` tags.

    Returns "" when they agree, else a description of every disagreement. nbconvert
    only enforces one direction (an untagged error aborts the run); this enforces the
    other, so a deliberate failure cannot quietly stop failing.
    """
    try:
        nb = json.loads(executed.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return f"could not re-read executed notebook: {type(e).__name__}: {e}"
    problems = []
    for i, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        expected = "raises-exception" in (cell.get("metadata", {}).get("tags") or [])
        raised = any(o.get("output_type") == "error" for o in (cell.get("outputs") or []))
        if expected and not raised:
            problems.append(f"cell {i} is tagged raises-exception but did not raise")
        elif raised and not expected:
            problems.append(f"cell {i} raised but is not tagged raises-exception")
    return "; ".join(problems)

def run_one(nb: Path, timeout: int, inplace: bool, kernel: str | None = None) -> tuple[bool, float, str]:
    args = [PY, "-m", "nbconvert", "--to", "notebook", "--execute",
            f"--ExecutePreprocessor.timeout={timeout}"]
    if kernel:
        args.append(f"--ExecutePreprocessor.kernel_name={kernel}")
    if inplace:
        args += ["--inplace", str(nb)]
    else:
        args += ["--output-dir", str(CHECK_DIR), str(nb)]
    t0 = time.time()
    try:
        r = subprocess.run(args, cwd=nb.parent, capture_output=True, text=True,
                           timeout=timeout + 60, env=ENV)
        ok = r.returncode == 0
        msg = "" if ok else (r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "nonzero exit")
        if ok:
            problems = audit_failures(nb if inplace else CHECK_DIR / nb.name)
            if problems:
                ok, msg = False, "EXPECTED-FAILURE: " + problems
    except subprocess.TimeoutExpired:
        ok, msg = False, "TIMEOUT"
    return ok, time.time() - t0, msg

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", help='e.g. "Course 01"')
    ap.add_argument("--files", nargs="*", default=None)
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--kernel", default=None, help="force a kernel name (e.g. tfenv for TensorFlow notebooks)")
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()

    if a.files:
        nbs = [Path(f).resolve() for f in a.files]
    elif a.course:
        nbs = list(student_notebooks(REPO / a.course))
    else:
        ap.error("--course or --files required")

    failures = []
    for nb in nbs:
        ok, dt, msg = run_one(nb, a.timeout, inplace=not a.check_only, kernel=a.kernel)
        rel = nb.relative_to(REPO) if nb.is_relative_to(REPO) else nb
        print(f"{'OK  ' if ok else 'FAIL'} {dt:6.1f}s {rel}" + (f"  <- {msg}" if msg else ""), flush=True)
        if not ok:
            failures.append((str(rel), msg))
    print(f"\n{len(nbs) - len(failures)}/{len(nbs)} executed to their authored end-state")
    if failures:
        print("FAILURES:")
        for rel, msg in failures:
            print(f"  {rel}: {msg}")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
