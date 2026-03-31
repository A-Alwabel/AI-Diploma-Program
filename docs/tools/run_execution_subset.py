#!/usr/bin/env python3
"""Execute a subset of notebooks and write a JSON report. Used for runtime validation."""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent.parent
OUT = BASE / "artifacts" / "execution_subset_report.json"
EXCLUDE = {".ipynb_checkpoints", "artifacts", "SOLUTIONS_ALL", ".nbconvert"}
TIMEOUT = 90


def find_notebooks(courses):
    notebooks = []
    for c in courses:
        d = BASE / c
        if not d.is_dir():
            continue
        for nb in d.rglob("*.ipynb"):
            if any(x in nb.parts for x in EXCLUDE) or ".nbconvert" in nb.name:
                continue
            notebooks.append(nb)
    return sorted(notebooks)


def run_one(nb_path):
    rel = str(nb_path.relative_to(BASE))
    res = {"path": rel, "status": "unknown", "error": None}
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook",
             "--execute", f"--ExecutePreprocessor.timeout={TIMEOUT}", str(nb_path),
             "--output-dir", str(BASE / "artifacts" / "executed_subset")],
            capture_output=True, text=True, timeout=TIMEOUT + 15, cwd=str(BASE),
        )
        res["status"] = "passed" if proc.returncode == 0 else "failed"
        if proc.returncode != 0:
            err = (proc.stderr or proc.stdout or "")[:2000]
            res["error"] = err
    except subprocess.TimeoutExpired:
        res["status"] = "failed"
        res["error"] = "Timeout"
    except Exception as e:
        res["status"] = "failed"
        res["error"] = str(e)[:2000]
    return res


def main():
    courses = sys.argv[1:] if len(sys.argv) > 1 else ["Course 04", "Course 05"]
    notebooks = find_notebooks(courses)
    print(f"Executing {len(notebooks)} notebooks (timeout={TIMEOUT}s)...")
    results = []
    for i, nb in enumerate(notebooks, 1):
        rel = str(nb.relative_to(BASE))
        print(f"  [{i}/{len(notebooks)}] {rel[:70]}...")
        r = run_one(nb)
        results.append(r)
        if r["status"] == "failed":
            print(f"    FAILED: {str(r.get('error') or '')[:80]}")

    out_data = {
        "courses": courses,
        "total": len(results),
        "passed": sum(1 for r in results if r["status"] == "passed"),
        "failed": sum(1 for r in results if r["status"] == "failed"),
        "results": results,
        "timestamp": datetime.now().isoformat(),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out_data, f, indent=2, ensure_ascii=False)
    print(f"\nReport: {OUT}")
    print(f"Passed: {out_data['passed']}, Failed: {out_data['failed']}")


if __name__ == "__main__":
    main()
