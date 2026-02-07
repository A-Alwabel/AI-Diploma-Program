#!/usr/bin/env python3
"""
Re-execute notebooks that failed due to JSON errors (after fixing them).
"""

import json
import subprocess
import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

BASE_DIR = Path(__file__).parent.parent

def execute_single_notebook(nb_path: Path):
    """Execute a single notebook."""
    try:
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook", "--execute",
            "--ExecutePreprocessor.timeout=300",
            "--ExecutePreprocessor.kernel_name=python3",
            "--inplace", str(nb_path)
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=310,
            cwd=str(BASE_DIR)
        )
        
        return {
            "path": str(nb_path.relative_to(BASE_DIR)),
            "status": "passed" if result.returncode == 0 else "failed",
            "error": result.stderr[:500] if result.returncode != 0 else None
        }
    except subprocess.TimeoutExpired:
        return {
            "path": str(nb_path.relative_to(BASE_DIR)),
            "status": "timeout",
            "error": "Execution timeout (300s)"
        }
    except Exception as e:
        return {
            "path": str(nb_path.relative_to(BASE_DIR)),
            "status": "error",
            "error": str(e)[:500]
        }

def main():
    """Re-execute failed notebooks."""
    # Get list of notebooks with JSON errors
    with open(BASE_DIR / 'artifacts/notebook_execution_report_v2.json') as f:
        data = json.load(f)
    
    json_error_notebooks = []
    for r in data.get('results', []):
        if r.get('status') != 'passed' and '.nbconvert' not in r.get('path', ''):
            error = (r.get('error') or '').lower()
            if 'json' in error or 'execution_count' in error or 'outputs' in error:
                nb_path = BASE_DIR / r.get('path')
                if nb_path.exists():
                    json_error_notebooks.append(nb_path)
    
    print(f"🔧 Re-executing {len(json_error_notebooks)} notebooks with JSON errors\n")
    
    results = []
    with ProcessPoolExecutor(max_workers=4) as executor:
        future_to_nb = {executor.submit(execute_single_notebook, nb): nb for nb in json_error_notebooks}
        
        completed = 0
        passed = 0
        failed = 0
        
        for future in as_completed(future_to_nb):
            result = future.result()
            results.append(result)
            completed += 1
            
            if result['status'] == 'passed':
                passed += 1
            else:
                failed += 1
            
            if completed % 10 == 0 or completed == len(json_error_notebooks):
                percent = (completed / len(json_error_notebooks)) * 100
                print(f"  Progress: {completed}/{len(json_error_notebooks)} ({percent:.1f}%) - Passed: {passed}, Failed: {failed}", flush=True)
    
    print(f"\n✅ Re-execution complete: {passed} passed, {failed} failed")
    
    # Update the execution report
    # Load existing results
    all_results = data.get('results', [])
    
    # Create a map of path -> result for quick lookup
    result_map = {r['path']: r for r in all_results}
    
    # Update with new results
    for new_result in results:
        result_map[new_result['path']] = new_result
    
    # Save updated report
    updated_data = {
        "total_notebooks": len(result_map),
        "completed": len(result_map),
        "results": list(result_map.values())
    }
    
    with open(BASE_DIR / 'artifacts/notebook_execution_report_v2.json', 'w') as f:
        json.dump(updated_data, f, indent=2)
    
    print(f"✅ Updated execution report")

if __name__ == "__main__":
    main()
