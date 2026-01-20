#!/usr/bin/env python3
"""
Execute only the notebooks that failed in the last full run.
Writes a compact JSON report to artifacts/failed_notebook_report.json.
"""
import json
import time
from pathlib import Path
from datetime import datetime

# Reuse execution logic from notebook_runner
import sys
sys.path.append(str(Path(__file__).parent))
import notebook_runner as runner  # type: ignore


REPORT_PATH = Path("artifacts/notebook_execution_report.json")
OUTPUT_JSON = Path("artifacts/failed_notebook_report.json")


def main() -> int:
    if not REPORT_PATH.exists():
        print(f"Report not found: {REPORT_PATH}")
        return 1

    with REPORT_PATH.open("r", encoding="utf-8") as f:
        report = json.load(f)

    failed = [Path(r["path"]) for r in report["results"] if r.get("status") == "failed"]
    print("=" * 60)
    print("FAILED NOTEBOOK RE-RUNNER")
    print("=" * 60)
    print(f"Found {len(failed)} failed notebooks from last report.")
    if not failed:
        return 0

    results = []
    start = time.time()
    for idx, rel_path in enumerate(failed, start=1):
        nb_path = runner.BASE_DIR / rel_path
        print(f"[{idx}/{len(failed)}] {rel_path}...", end=" ", flush=True)
        if not nb_path.exists():
            result = {
                "path": str(rel_path),
                "status": "failed",
                "execution_time": 0,
                "error": "File not found",
                "error_traceback": None,
            }
            print("✗ (missing)")
        else:
            result = runner.execute_notebook(nb_path)
            mark = "✓" if result["status"] == "passed" else "✗"
            print(f"{mark} ({result['execution_time']:.1f}s)")
        results.append(result)

    duration = time.time() - start
    passed = sum(1 for r in results if r["status"] == "passed")
    failed_count = len(results) - passed

    out = {
        "generated": datetime.utcnow().isoformat(),
        "total": len(results),
        "passed": passed,
        "failed": failed_count,
        "results": results,
        "duration_seconds": duration,
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("=" * 60)
    print("FAILED NOTEBOOK RE-RUN COMPLETE")
    print("=" * 60)
    print(f"Passed: {passed}")
    print(f"Failed: {failed_count}")
    print(f"Duration: {duration:.1f}s")
    print(f"Report: {OUTPUT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
