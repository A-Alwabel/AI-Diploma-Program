#!/usr/bin/env python3
"""Verify Course 11 student-path notebooks (syntax or full execute).

    python3 "Course 11/scripts/verify_student_notebooks.py" --syntax-only
    python3 "Course 11/scripts/verify_student_notebooks.py"
"""

from __future__ import annotations

import argparse
import ast
import json
import subprocess
import sys
import time
from pathlib import Path

COURSE11 = Path(__file__).resolve().parents[1]


def discover_notebooks() -> list[Path]:
    out: list[Path] = []
    for p in sorted(COURSE11.rglob("*.ipynb")):
        if "DOCS" in p.parts or "solutions" in p.parts:
            continue
        if not any(part.startswith("unit") for part in p.parts):
            continue
        out.append(p)
    return out


def strip_magics(src: str) -> str:
    lines = []
    for line in src.splitlines():
        s = line.strip()
        if s.startswith("%") or s.startswith("!"):
            continue
        lines.append(line)
    return "\n".join(lines)


def syntax_check(nb_path: Path) -> str | None:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    for i, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell.get("source", []))
        if not src.strip():
            continue
        try:
            ast.parse(strip_magics(src))
        except SyntaxError as exc:
            return f"cell {i}: {exc.msg}"
    return None


def execute_notebook(nb_path: Path) -> tuple[bool, str]:
    cwd = str(nb_path.parent)
    cmd = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        str(nb_path),
        "--output",
        str(Path("/tmp") / f"exec_{nb_path.name}"),
        "--ExecutePreprocessor.timeout=1200",
        "--ExecutePreprocessor.kernel_name=python3",
    ]
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode == 0:
        return True, ""
    return False, (r.stderr or r.stdout or "")[-4000:]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--syntax-only", action="store_true")
    args = parser.parse_args()

    nbs = discover_notebooks()
    log_path = COURSE11 / "scripts" / "_last_notebook_verify.log"
    lines: list[str] = []
    failures: list[str] = []

    for nb in nbs:
        rel = nb.relative_to(COURSE11)
        if args.syntax_only:
            err = syntax_check(nb)
            if err:
                lines.append(f"FAIL\t{rel}\t{err}")
                failures.append(str(rel))
            else:
                lines.append(f"OK\t{rel}")
        else:
            t0 = time.perf_counter()
            ok, err = execute_notebook(nb)
            dt = time.perf_counter() - t0
            if ok:
                lines.append(f"OK\t{dt:.1f}s\t{rel}")
            else:
                lines.append(f"FAIL\t{dt:.1f}s\t{rel}")
                failures.append(str(rel))
                lines.append(err)

    log_path.write_text("\n".join(lines), encoding="utf-8")
    mode = "syntax" if args.syntax_only else "execute"
    print(f"Wrote {log_path} ({len(nbs)} notebooks, {mode})")
    print(f"OK: {len(nbs) - len(failures)}  FAIL: {len(failures)}")
    for f in failures:
        print(" ", f)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
