#!/usr/bin/env python3
"""Batch-execute student-path notebooks for one course (or a file list).

Generalizes Course 09/Course 11's verify_student_notebooks.py:
- targets unit*/examples and unit*/exercises notebooks (skips solutions/, DOCS/)
- executes each notebook with its own directory as cwd
- writes outputs IN PLACE by default (project rule: students see real outputs);
  use --check-only to execute to a throwaway copy instead
- per-notebook timeout, summary log

Usage:
  python tools/verify/run_notebooks.py --course "Course 01" [--check-only]
  python tools/verify/run_notebooks.py --files a.ipynb b.ipynb
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PY = sys.executable

def student_notebooks(course_dir: Path):
    for pattern in ("unit*/examples/*.ipynb", "unit*/exercises/*.ipynb"):
        yield from sorted(course_dir.glob(pattern))

def run_one(nb: Path, timeout: int, inplace: bool, kernel: str | None = None) -> tuple[bool, float, str]:
    args = [PY, "-m", "nbconvert", "--to", "notebook", "--execute",
            f"--ExecutePreprocessor.timeout={timeout}"]
    if kernel:
        args.append(f"--ExecutePreprocessor.kernel_name={kernel}")
    if inplace:
        args += ["--inplace", str(nb)]
    else:
        args += ["--output-dir", "/tmp/nbcheck", str(nb)]
    t0 = time.time()
    try:
        r = subprocess.run(args, cwd=nb.parent, capture_output=True, text=True,
                           timeout=timeout + 60)
        ok = r.returncode == 0
        msg = "" if ok else (r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "nonzero exit")
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
    print(f"\n{len(nbs) - len(failures)}/{len(nbs)} executed cleanly")
    if failures:
        print("FAILURES:")
        for rel, msg in failures:
            print(f"  {rel}: {msg}")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
