#!/usr/bin/env python3
"""
Re-run execution on previously failed notebooks to verify fixes.
"""

import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from notebook_runner import execute_notebook, classify_notebook

BASE_DIR = Path(__file__).parent.parent

def main():
    """Re-run failed notebooks."""
    report_file = BASE_DIR / "artifacts" / "notebook_execution_report.json"
    if not report_file.exists():
        print("Original execution report not found.")
        return
    
    with open(report_file, 'r') as f:
        original_report = json.load(f)
    
    failed = [r for r in original_report['results'] if r.get('status') == 'failed']
    
    print("=" * 60)
    print("RE-RUNNING FAILED NOTEBOOKS")
    print("=" * 60)
    print(f"\nRe-running {len(failed)} previously failed notebooks...\n")
    
    new_results = []
    passed_now = 0
    still_failed = 0
    
    for i, failure in enumerate(failed, 1):
        nb_path = BASE_DIR / failure['path']
        if not nb_path.exists():
            print(f"[{i}/{len(failed)}] {failure['path']}... SKIP (not found)")
            new_results.append(failure)
            continue
        
        print(f"[{i}/{len(failed)}] {failure['path']}...", end=" ", flush=True)
        result = execute_notebook(nb_path)
        result.update(classify_notebook(nb_path))
        
        if result["status"] == "passed":
            passed_now += 1
            print(f"✓ NOW PASSES ({result['execution_time']:.1f}s)")
        else:
            still_failed += 1
            print(f"✗ STILL FAILS ({result['execution_time']:.1f}s)")
            if result.get("error"):
                error_preview = result["error"][:80].replace("\n", " ")
                print(f"     Error: {error_preview}...")
        
        new_results.append(result)
    
    # Update original report with new results
    for new_result in new_results:
        # Find matching result in original report
        for i, orig_result in enumerate(original_report['results']):
            if orig_result.get('path') == new_result.get('path'):
                original_report['results'][i] = new_result
                break
    
    # Recalculate summary
    total_passed = sum(1 for r in original_report['results'] if r.get('status') == 'passed')
    total_failed = sum(1 for r in original_report['results'] if r.get('status') == 'failed')
    
    original_report['summary'] = {
        "passed": total_passed,
        "failed": total_failed,
        "pass_rate": (total_passed / len(original_report['results']) * 100) if original_report['results'] else 0
    }
    
    # Save updated report
    with open(report_file, 'w') as f:
        json.dump(original_report, f, indent=2)
    
    print("\n" + "=" * 60)
    print("RE-RUN COMPLETE")
    print("=" * 60)
    print(f"Previously Failed: {len(failed)}")
    print(f"Now Pass: {passed_now} ✅")
    print(f"Still Fail: {still_failed} ❌")
    print(f"\nOverall Pass Rate: {original_report['summary']['pass_rate']:.1f}%")
    print("=" * 60)

if __name__ == "__main__":
    main()
