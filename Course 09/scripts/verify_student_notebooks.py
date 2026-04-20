#!/usr/bin/env python3
"""Execute all student-path Course 09 notebooks (excluding DOCS/) and report status.

Run from repo root (recommended after any Course 09 notebook batch):

    python3 "Course 09/scripts/verify_student_notebooks.py"

Uses Course 09 root as anchor; each notebook runs with ``cwd`` set to its own
folder so ``course09_step_viz`` parent discovery works. Writes
``scripts/_last_notebook_verify.log`` (gitignored via ``*.log``).
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path


def discover_notebooks(course09: Path) -> list[Path]:
    out: list[Path] = []
    for p in sorted(course09.rglob("*.ipynb")):
        if "DOCS" in p.parts:
            continue
        if "unit" not in str(p):
            continue
        out.append(p)
    return out


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    nbs = discover_notebooks(root)
    log_path = root / "scripts" / "_last_notebook_verify.log"
    lines: list[str] = []
    failures: list[str] = []

    for nb in nbs:
        cwd = str(nb.parent)
        rel = nb.relative_to(root)
        t0 = time.perf_counter()
        cmd = [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            str(nb),
            "--output",
            str(Path("/tmp") / f"exec_{nb.name}"),
            "--ExecutePreprocessor.timeout=3600",
            "--ExecutePreprocessor.kernel_name=python3",
        ]
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        dt = time.perf_counter() - t0
        if r.returncode == 0:
            lines.append(f"OK\t{dt:.1f}s\t{rel}")
        else:
            lines.append(f"FAIL\t{dt:.1f}s\t{rel}")
            failures.append(str(rel))
            err = (r.stderr or "")[-8000:]
            lines.append(err)

    log_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {log_path} ({len(nbs)} notebooks)")
    print(f"OK: {len(nbs) - len(failures)}  FAIL: {len(failures)}")
    for f in failures:
        print("  ", f)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
