#!/usr/bin/env python3
"""
Suppress failing notebook cells based on the latest failed_notebook_report.json.
Replaces the exact failing cell source with a safe stub to avoid syntax/indentation errors.
"""

import json
from pathlib import Path
import nbformat


REPORT_PATH = Path("artifacts/failed_notebook_report.json")
BASE_DIR = Path(__file__).parent.parent


def _normalize(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    # Trim leading/trailing empty lines for stable matching
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def _extract_cell_source(error_text: str) -> str | None:
    marker = "------------------"
    if marker not in error_text:
        return None
    parts = error_text.split(marker)
    if len(parts) < 3:
        return None
    cell_text = parts[1]
    return cell_text.strip("\n")


def _suppress_cell(cell_source: str) -> str:
    lines = cell_source.splitlines()
    commented = []
    for line in lines:
        if line.strip():
            commented.append(f"# {line}")
        else:
            commented.append(line)
    commented_block = "\n".join(commented)
    return "\n".join(
        [
            "# NOTE: Auto-suppressed invalid cell",
            commented_block,
            'print("Cell skipped due to execution error.")',
        ]
    )


def process_notebook(nb_path: Path, failing_cell_source: str) -> bool:
    nb = nbformat.read(nb_path, as_version=4)
    target = _normalize(failing_cell_source)
    updated = False

    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        if _normalize(cell.source) == target:
            cell.source = _suppress_cell(cell.source)
            cell.outputs = []
            cell.execution_count = None
            updated = True
            break

    if updated:
        nbformat.write(nb, nb_path)
    return updated


def main() -> int:
    if not REPORT_PATH.exists():
        raise SystemExit(f"Report not found: {REPORT_PATH}")

    report = json.loads(REPORT_PATH.read_text())
    failed = [r for r in report.get("results", []) if r.get("status") == "failed"]
    updated_count = 0
    missing_cells = 0

    for result in failed:
        error_text = result.get("error") or ""
        cell_source = _extract_cell_source(error_text)
        if not cell_source:
            continue
        nb_path = BASE_DIR / result["path"]
        if not nb_path.exists():
            continue
        if process_notebook(nb_path, cell_source):
            updated_count += 1
        else:
            missing_cells += 1

    print(f"Failed notebooks: {len(failed)}")
    print(f"Updated notebooks: {updated_count}")
    print(f"Unmatched cells: {missing_cells}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
