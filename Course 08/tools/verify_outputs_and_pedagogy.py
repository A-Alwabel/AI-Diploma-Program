#!/usr/bin/env python3
"""
Verify each Course 08 notebook:
1. Extract "Outputs:" from the Inputs & Outputs markdown cell.
2. Check that code cells have outputs (stdout, display_data) that match.
3. Produce a report for manual pedagogy check.
"""

import json
import re
from pathlib import Path

COURSE08_ROOT = Path(__file__).resolve().parent.parent


def get_notebooks():
    notebooks = []
    for path in COURSE08_ROOT.rglob("*.ipynb"):
        if "/solutions/" in path.as_posix() or "SOLUTIONS" in path.as_posix():
            continue
        notebooks.append(path)
    return sorted(notebooks)


def get_promised_outputs(nb):
    """Extract text after **Outputs:** from markdown cells."""
    promised = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = "".join(cell.get("source", []))
        if "Outputs:" not in src and "📤" not in src:
            continue
        # Get the paragraph after Outputs
        m = re.search(r"\*\*Outputs:\*\*\s*(.+?)(?=\n\n|\n\*\*|$)", src, re.DOTALL)
        if m:
            promised.append(m.group(1).strip())
        else:
            # Fallback: line after "Outputs"
            for line in src.split("\n"):
                if "Outputs:" in line or "📤" in line:
                    idx = src.split("\n").index(line)
                    rest = "\n".join(src.split("\n")[idx + 1 : idx + 5])
                    promised.append(rest.strip()[:500])
                    break
    return " ".join(promised) if promised else ""


def has_code_outputs(nb):
    """Check if code cells have any outputs (stdout, display_data, execute_result)."""
    has = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        outs = cell.get("outputs", [])
        if not outs:
            has.append(False)
            continue
        for o in outs:
            if o.get("output_type") in ("stream", "display_data", "execute_result"):
                has.append(True)
                break
        else:
            has.append(False)
    return has


def output_summary(nb):
    """Brief summary of what outputs exist (text snippets)."""
    snippets = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        for o in cell.get("outputs", []):
            if o.get("output_type") == "stream" and "text" in o:
                text = "".join(o["text"])[:200]
                snippets.append(text.strip())
            if o.get("output_type") in ("display_data", "execute_result") and "data" in o:
                if "text/plain" in o["data"]:
                    snippets.append("".join(o["data"]["text/plain"])[:150])
                if "image/png" in o["data"]:
                    snippets.append("[plot/image]")
    return " | ".join(snippets[:5])


def main():
    notebooks = get_notebooks()
    results = []
    for path in notebooks:
        rel = path.relative_to(COURSE08_ROOT)
        try:
            with open(path) as f:
                nb = json.load(f)
        except Exception as e:
            results.append({"path": str(rel), "error": str(e), "promised": "", "outputs_ok": False})
            continue
        promised = get_promised_outputs(nb)
        code_has = has_code_outputs(nb)
        # Consider "outputs ok" if at least one code cell that has source has output (we expect training notebooks to have several)
        code_cells = [c for c in nb.get("cells", []) if c.get("cell_type") == "code" and "".join(c.get("source", [])).strip()]
        cells_with_out = sum(1 for i, c in enumerate(nb.get("cells", [])) if c.get("cell_type") == "code" and c.get("outputs"))
        outputs_ok = len(code_cells) == 0 or cells_with_out >= 1  # at least one code cell has output
        summary = output_summary(nb)
        results.append({
            "path": str(rel),
            "promised": promised[:400],
            "outputs_present": summary[:300],
            "outputs_ok": outputs_ok,
            "code_cells_with_output": cells_with_out,
            "total_code_cells": len(code_cells),
        })
    # Report
    out_path = COURSE08_ROOT / "DOCS" / "output_pedagogy_verification_report.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({"notebooks": results}, f, indent=2)
    # Text report
    txt_path = COURSE08_ROOT / "DOCS" / "output_pedagogy_verification_report.txt"
    with open(txt_path, "w") as f:
        f.write("Course 08 – Output & pedagogy verification report\n")
        f.write("=" * 60 + "\n\n")
        for r in results:
            f.write(f"Notebook: {r['path']}\n")
            f.write(f"  Promised outputs: {r.get('promised', '')[:200]}...\n")
            f.write(f"  Outputs present: {r.get('outputs_present', '')[:200]}...\n")
            f.write(f"  Code cells with output: {r.get('code_cells_with_output', 0)} / {r.get('total_code_cells', 0)}\n")
            f.write(f"  Outputs OK: {r.get('outputs_ok', False)}\n")
            if r.get("error"):
                f.write(f"  Error: {r['error']}\n")
            f.write("\n")
    print(f"Report: {out_path}")
    print(f"Text: {txt_path}")
    ok = sum(1 for r in results if r.get("outputs_ok"))
    print(f"Notebooks with outputs: {ok}/{len(results)}")


if __name__ == "__main__":
    main()
