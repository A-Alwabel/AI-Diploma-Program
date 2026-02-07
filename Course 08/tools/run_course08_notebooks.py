#!/usr/bin/env python3
"""
Run all Course 08 notebooks and write a pass/fail report.
Requires: jupyter, nbconvert, and (for full runs) tensorflow, torch, etc.

Usage (from AI Diploma repo root):
  python "Course 08/tools/run_course08_notebooks.py"

Or from Course 08 folder:
  python tools/run_course08_notebooks.py
"""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Course 08 root (parent of tools/)
COURSE08_ROOT = Path(__file__).resolve().parent.parent
# AI Diploma repo root (parent of Course 08)
REPO_ROOT = COURSE08_ROOT.parent

EXECUTION_TIMEOUT = 600  # 10 min per notebook for heavy training
REPORT_JSON = COURSE08_ROOT / "DOCS" / "notebook_run_report.json"
REPORT_TXT = COURSE08_ROOT / "DOCS" / "notebook_run_report.txt"


def get_course08_notebooks():
    """All .ipynb under Course 08, excluding solutions folders and __pycache__."""
    notebooks = []
    for path in COURSE08_ROOT.rglob("*.ipynb"):
        s = path.as_posix()
        if "/solutions/" in s or "SOLUTIONS" in s or "__pycache__" in s:
            continue
        notebooks.append(path)
    return sorted(notebooks)


def execute_notebook(nb_path: Path) -> dict:
    """Execute one notebook with jupyter nbconvert; return status dict."""
    rel = nb_path.relative_to(COURSE08_ROOT)
    result = {
        "path": str(rel),
        "status": "unknown",
        "error": None,
        "seconds": None,
        "timestamp": datetime.now().isoformat(),
    }
    try:
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            f"--ExecutePreprocessor.timeout={EXECUTION_TIMEOUT}",
            "--inplace",
            str(nb_path),
        ]
        t0 = datetime.now()
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=EXECUTION_TIMEOUT + 30,
            cwd=str(REPO_ROOT),
        )
        sec = (datetime.now() - t0).total_seconds()
        result["seconds"] = round(sec, 1)
        if proc.returncode == 0:
            result["status"] = "success"
        else:
            result["status"] = "error"
            err = (proc.stderr or proc.stdout or "")[:2000]
            result["error"] = err.strip() or "No stderr/stdout"
    except subprocess.TimeoutExpired:
        result["status"] = "error"
        result["error"] = "Timeout"
    except FileNotFoundError as e:
        result["status"] = "error"
        result["error"] = f"jupyter/nbconvert not found: {e}"
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)[:500]
    return result


def main():
    notebooks = get_course08_notebooks()
    if not notebooks:
        print("No notebooks found under Course 08.")
        sys.exit(0)
    print(f"Found {len(notebooks)} notebooks. Executing (this may take a long time)...")
    results = []
    for i, nb_path in enumerate(notebooks):
        rel = nb_path.relative_to(COURSE08_ROOT)
        print(f"  [{i+1}/{len(notebooks)}] {rel}")
        r = execute_notebook(nb_path)
        results.append(r)
        if r["status"] != "success":
            print(f"      -> {r['status']}: {r.get('error', '')[:200]}")
    # Report
    report = {
        "course": "08",
        "timestamp": datetime.now().isoformat(),
        "total": len(results),
        "success": sum(1 for r in results if r["status"] == "success"),
        "results": results,
    }
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_JSON, "w") as f:
        json.dump(report, f, indent=2)
    # Plain text summary
    with open(REPORT_TXT, "w") as f:
        f.write(f"Course 08 notebook run report — {report['timestamp']}\n")
        f.write(f"Total: {report['total']} | Success: {report['success']} | Failed: {report['total'] - report['success']}\n\n")
        for r in results:
            s = "OK" if r["status"] == "success" else "FAIL"
            f.write(f"  [{s}] {r['path']}")
            if r.get("seconds"):
                f.write(f"  ({r['seconds']}s)")
            if r.get("error"):
                f.write(f"  — {r['error'][:150]}")
            f.write("\n")
    print(f"\nReport: {REPORT_JSON}")
    print(f"Summary: {REPORT_TXT}")
    print(f"Success: {report['success']}/{report['total']}")
    sys.exit(0 if report["success"] == report["total"] else 1)


if __name__ == "__main__":
    main()
