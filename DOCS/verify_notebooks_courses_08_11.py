#!/usr/bin/env python3
"""
Deep verification for Course 08–11 Jupyter notebooks.

Phase 1 — Static (always run):
  - Valid nbformat v4 JSON
  - Each code cell: after stripping IPython/shell magics, ast.parse(..., mode='exec')

Phase 2 — Execute (optional, --execute):
  - nbclient NotebookClient with per-notebook timeout (default 120s)
  - Stops on first cell error; records exception type and traceback tail

Usage:
  python3 DOCS/verify_notebooks_courses_08_11.py              # AST only, write report
  python3 DOCS/verify_notebooks_courses_08_11.py --execute --smoke --timeout 300
  python3 DOCS/verify_notebooks_courses_08_11.py --execute --smoke-heavy --timeout 300  # + Marian Hub

Report: DOCS/NOTEBOOK_VERIFICATION_REPORT_COURSES_08_11.md
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REPORT_PATH = REPO / "DOCS" / "NOTEBOOK_VERIFICATION_REPORT_COURSES_08_11.md"
COURSES = ["Course 08", "Course 09", "Course 10", "Course 11"]

# Default `--smoke`: fast, no Hugging Face Hub downloads (reliable in CI / slow networks).
SMOKE_PATHS = [
    REPO / "Course 09" / "unit4-exploration-exploitation" / "solutions" / "02_exploration_solution.ipynb",
    REPO / "Course 11" / "unit1-deployment-basics" / "solutions" / "01_packaging_solution.ipynb",
    REPO / "Course 11" / "unit2-versioning-serving" / "solutions" / "03_api_deployment_solution.ipynb",
    REPO / "Course 11" / "unit5-pipelines-monitoring" / "solutions" / "01_monitoring_solution.ipynb",
    REPO / "Course 08" / "unit1-deep-learning-basics" / "solutions" / "01_neural_network_solution.ipynb",
]

# Optional: MarianMT + `from_pretrained` — needs network; often >20 min on first pip+download.
SMOKE_HEAVY_PATHS = SMOKE_PATHS + [
    REPO / "Course 08" / "unit4-advanced-dl" / "solutions" / "01_transformer_solution.ipynb",
]

# Per-notebook execute timeout floor (seconds).
EXECUTE_TIMEOUT_MIN_BY_SUFFIX: dict[str, int] = {
    "01_transformer_solution.ipynb": 3600,
}


def iter_notebooks() -> list[Path]:
    out: list[Path] = []
    for c in COURSES:
        base = REPO / c
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*.ipynb")):
            if ".ipynb_checkpoints" in str(p):
                continue
            if p.name.startswith("."):
                continue
            out.append(p)
    return out


def strip_magics_for_ast(source: str) -> str:
    """Remove lines that are shell/magic-only (heuristic for ast.parse)."""
    lines = source.splitlines()
    kept: list[str] = []
    for line in lines:
        s = line.strip()
        if not s:
            kept.append(line)
            continue
        if s.startswith("!"):
            continue
        if s.startswith("%%"):
            continue
        if re.match(r"^%\w+", s):
            continue
        if re.match(r"^get_ipython\(\)\.run_(line|cell)_magic", s):
            continue
        kept.append(line)
    return "\n".join(kept)


def cell_ast_ok(source: str) -> tuple[bool, str]:
    cleaned = strip_magics_for_ast(source).strip()
    if not cleaned:
        return True, "empty-or-magic-only"
    try:
        ast.parse(cleaned, mode="exec")
        return True, ""
    except SyntaxError as e:
        return False, f"SyntaxError line {e.lineno or '?'}: {e.msg}"


def validate_notebook_ast(nb_path: Path) -> tuple[bool, list[str]]:
    """Returns (all_ok, list of error messages)."""
    errors: list[str] = []
    try:
        raw = nb_path.read_text(encoding="utf-8")
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"]
    cells = data.get("cells", [])
    for i, cell in enumerate(cells):
        if cell.get("cell_type") != "code":
            continue
        src = cell.get("source", [])
        if isinstance(src, list):
            text = "".join(src)
        else:
            text = str(src)
        ok, msg = cell_ast_ok(text)
        if not ok:
            errors.append(f"cell[{i}] code: {msg}")
    return len(errors) == 0, errors


def _resolve_kernel_name() -> str:
    try:
        import jupyter_client.kernelspec as kspec
    except ImportError:
        return "python3"
    specs = kspec.find_kernel_specs()
    if not specs:
        return "python3"
    for candidate in ("python3", "python3.11", "python3.12", "python3.10", "python3.9", "Python 3", "python"):
        if candidate in specs:
            return candidate
    return next(iter(specs.keys()))


def effective_execute_timeout(nb_path: Path, cli_timeout: int) -> int:
    name = nb_path.name
    floor = EXECUTE_TIMEOUT_MIN_BY_SUFFIX.get(name, 0)
    return max(cli_timeout, floor)


def execute_notebook(nb_path: Path, timeout: int) -> tuple[bool, str]:
    try:
        import nbformat
        from nbclient import NotebookClient
        from nbclient.exceptions import CellExecutionError
    except ImportError as e:
        return False, f"ImportError (install nbclient): {e}"

    nb = nbformat.read(nb_path, as_version=4)
    kernel = _resolve_kernel_name()
    client = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name=kernel,
        allow_errors=False,
    )
    try:
        client.execute()
        return True, "ok"
    except CellExecutionError as e:
        tail = traceback.format_exc()[-4000:]
        return False, f"CellExecutionError: {e}\n---\n{tail}"
    except Exception as e:
        tail = traceback.format_exc()[-4000:]
        return False, f"{type(e).__name__}: {e}\n---\n{tail}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true", help="Run each notebook (slow)")
    ap.add_argument("--smoke", action="store_true", help="Execute SMOKE_PATHS (no HF Hub)")
    ap.add_argument(
        "--smoke-heavy",
        action="store_true",
        help="Execute SMOKE_HEAVY_PATHS (includes Marian translation; needs network, long timeout)",
    )
    ap.add_argument("--timeout", type=int, default=120, help="Execute timeout per notebook (seconds)")
    ap.add_argument(
        "--cap-timeout",
        type=int,
        default=0,
        help="If >0, clip per-notebook timeout to at most this (keeps full batches from stalling on one Hub download)",
    )
    ap.add_argument("--max-execute", type=int, default=0, help="Cap execute count (0 = all)")
    ap.add_argument(
        "--progress-log",
        type=str,
        default="",
        help="Append one JSON object per notebook (path relative to repo root), e.g. DOCS/exec_progress.jsonl",
    )
    ap.add_argument(
        "--fail-on-exec",
        action="store_true",
        help="Exit non-zero if any executed notebook fails (in addition to AST failures)",
    )
    args = ap.parse_args()

    notebooks = iter_notebooks()
    lines: list[str] = []
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines.append("# Notebook verification: Courses 08–11")
    lines.append("")
    lines.append(f"**Generated:** {ts}")
    lines.append("")
    lines.append("## Method")
    lines.append("")
    lines.append("- **AST / syntax:** Every code cell is checked with `ast.parse` after stripping lines that start with `%`, `%%`, or `!`.")
    lines.append("- **Execute:** Optional (`--execute`). Uses **nbclient** with the given timeout. Failures often reflect **missing packages**, **no GPU**, **network downloads**, or **intentional TODO stubs**—not always bad notebooks.")
    lines.append("")
    lines.append(f"- **Notebooks scanned:** {len(notebooks)}")
    lines.append("")

    ast_failures: list[tuple[Path, list[str]]] = []
    exec_results: list[tuple[Path, bool, str]] = []

    for nb_path in notebooks:
        ok, errs = validate_notebook_ast(nb_path)
        if not ok:
            ast_failures.append((nb_path, errs))

    lines.append("## Phase 1: JSON + AST syntax")
    lines.append("")
    lines.append(f"| Result | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| PASS | {len(notebooks) - len(ast_failures)} |")
    lines.append(f"| FAIL | {len(ast_failures)} |")
    lines.append("")

    if ast_failures:
        lines.append("### AST / syntax failures")
        lines.append("")
        for p, errs in ast_failures:
            rel = p.relative_to(REPO)
            lines.append(f"#### `{rel}`")
            lines.append("")
            for e in errs:
                lines.append(f"- {e}")
            lines.append("")

    if args.execute:
        lines.append("## Phase 2: Execute (nbclient)")
        lines.append("")
        lines.append(
            f"CLI timeout: **{args.timeout}s**; some paths use a higher floor "
            f"(see `EXECUTE_TIMEOUT_MIN_BY_SUFFIX` in the script)."
        )
        lines.append("")
        if args.smoke_heavy:
            to_run = [p for p in SMOKE_HEAVY_PATHS if p.is_file()]
            lines.append("*Mode: **--smoke-heavy** (smoke + Marian `from_pretrained`; needs HF Hub.)*")
            lines.append("")
        elif args.smoke:
            to_run = [p for p in SMOKE_PATHS if p.is_file()]
            lines.append("*Mode: **--smoke** (lightweight solutions; no Hugging Face model download.)*")
            lines.append("")
        elif args.max_execute > 0:
            to_run = notebooks[: args.max_execute]
        else:
            to_run = notebooks
        progress_path = (REPO / args.progress_log) if args.progress_log else None
        if progress_path:
            progress_path.parent.mkdir(parents=True, exist_ok=True)
            progress_path.write_text("", encoding="utf-8")

        for i, nb_path in enumerate(to_run):
            rel = nb_path.relative_to(REPO)
            t_out = effective_execute_timeout(nb_path, args.timeout)
            if args.cap_timeout > 0:
                t_out = min(t_out, args.cap_timeout)
            print(f"[{i+1}/{len(to_run)}] Executing {rel} (timeout {t_out}s) ...", flush=True)
            ok, msg = execute_notebook(nb_path, t_out)
            exec_results.append((nb_path, ok, msg))
            if ok:
                print(f"  PASS", flush=True)
            else:
                print(f"  FAIL: {msg[:200]}...", flush=True)
            if progress_path:
                rec = {
                    "index": i + 1,
                    "total": len(to_run),
                    "path": str(rel).replace("\\", "/"),
                    "ok": ok,
                    "error_preview": (msg[:2000] if not ok else ""),
                }
                with progress_path.open("a", encoding="utf-8") as pl:
                    pl.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    pl.flush()

        ok_c = sum(1 for _, o, _ in exec_results if o)
        lines.append(f"| Execute PASS | {ok_c} |")
        lines.append(f"| Execute FAIL | {len(exec_results) - ok_c} |")
        lines.append("")
        for p, ok, msg in exec_results:
            rel = p.relative_to(REPO)
            st = "PASS" if ok else "FAIL"
            lines.append(f"### `{rel}` — **{st}**")
            lines.append("")
            if not ok:
                lines.append("```")
                lines.append(msg[:8000])
                lines.append("```")
            lines.append("")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORT_PATH.relative_to(REPO)}", flush=True)

    code = 0
    if ast_failures:
        code = 1
    elif args.execute and args.fail_on_exec and any(not o for _, o, _ in exec_results):
        code = 1
    return code


if __name__ == "__main__":
    sys.exit(main())
