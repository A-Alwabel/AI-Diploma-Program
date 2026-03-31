#!/usr/bin/env python3
"""
Execute notebooks in parallel with output validation.
Uses multiprocessing for parallel execution.
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Any
from concurrent.futures import ProcessPoolExecutor, as_completed
import subprocess

BASE_DIR = Path(__file__).parent.parent

def find_all_notebooks(base_dir: Path) -> List[Path]:
    """Find all .ipynb files."""
    notebooks = []
    exclude_dirs = {".git", "__pycache__", ".ipynb_checkpoints", "artifacts", "SOLUTIONS_ALL"}
    
    for nb_path in base_dir.rglob("*.ipynb"):
        if any(excluded in nb_path.parts for excluded in exclude_dirs):
            continue
        notebooks.append(nb_path)
    
    return sorted(notebooks)

def execute_single_notebook(nb_path: Path) -> Dict[str, Any]:
    """Execute a single notebook."""
    try:
        # Use existing notebook_runner
        result = subprocess.run(
            ["python3", str(BASE_DIR / "tools" / "notebook_runner.py"), str(nb_path)],
            capture_output=True,
            text=True,
            timeout=300,
            cwd=BASE_DIR
        )
        
        # Parse result (simplified - actual implementation would parse JSON output)
        return {
            "path": str(nb_path.relative_to(BASE_DIR)),
            "status": "passed" if result.returncode == 0 else "failed",
            "error": result.stderr if result.returncode != 0 else None
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
            "error": str(e)
        }

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers")
    parser.add_argument("--prioritize", action="store_true", help="Prioritize examples/exercises")
    parser.add_argument("--sample", type=int, help="Only execute N notebooks (for testing)")
    args = parser.parse_args()
    
    notebooks = find_all_notebooks(BASE_DIR)
    
    if args.prioritize:
        examples = [nb for nb in notebooks if "/examples/" in str(nb)]
        exercises = [nb for nb in notebooks if "/exercises/" in str(nb)]
        solutions = [nb for nb in notebooks if "/solutions/" in str(nb) or "/SOLUTIONS/" in str(nb)]
        other = [nb for nb in notebooks if nb not in examples + exercises + solutions]
        notebooks = examples + exercises + solutions + other
    
    if args.sample:
        notebooks = notebooks[:args.sample]
    
    print(f"🔧 Executing {len(notebooks)} notebooks with {args.workers} workers...")
    
    results = []
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        future_to_nb = {executor.submit(execute_single_notebook, nb): nb for nb in notebooks}
        
        completed = 0
        for future in as_completed(future_to_nb):
            result = future.result()
            results.append(result)
            completed += 1
            if completed % 50 == 0:
                print(f"  Executed {completed}/{len(notebooks)} notebooks...")
    
    # Save results
    report_path = BASE_DIR / "artifacts" / "notebook_execution_report_v2.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_path, "w") as f:
        json.dump({
            "total_notebooks": len(notebooks),
            "results": results
        }, f, indent=2)
    
    # Summary
    passed = sum(1 for r in results if r.get("status") == "passed")
    failed = len(results) - passed
    
    print(f"\n✅ Execution complete!")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Report: {report_path}")

if __name__ == "__main__":
    main()
