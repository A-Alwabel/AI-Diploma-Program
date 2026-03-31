#!/usr/bin/env python3
"""
Execute notebooks in parallel - FIXED VERSION 2
Uses nbconvert directly instead of notebook_runner.py
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
    """Execute a single notebook using nbconvert directly."""
    try:
        # Use nbconvert directly
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--ExecutePreprocessor.timeout=300",
            "--ExecutePreprocessor.kernel_name=python3",
            "--inplace",
            str(nb_path)
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=310,  # 300s + 10s buffer
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

def save_progress(results: List[Dict], total: int, report_path: Path):
    """Save progress incrementally."""
    try:
        with open(report_path, "w") as f:
            json.dump({
                "total_notebooks": total,
                "completed": len(results),
                "results": results
            }, f, indent=2)
    except Exception as e:
        print(f"Warning: Could not save progress: {e}", file=sys.stderr)

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
    
    print(f"🔧 Executing {len(notebooks)} notebooks with {args.workers} workers...", flush=True)
    sys.stdout.flush()
    
    # Setup report path
    report_path = BASE_DIR / "artifacts" / "notebook_execution_report_v2.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    results = []
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        future_to_nb = {executor.submit(execute_single_notebook, nb): nb for nb in notebooks}
        
        completed = 0
        passed = 0
        failed = 0
        
        # Print initial status
        print(f"  Progress: 0/{len(notebooks)} (0.0%)", flush=True)
        sys.stdout.flush()
        
        for future in as_completed(future_to_nb):
            result = future.result()
            results.append(result)
            completed += 1
            
            if result.get("status") == "passed":
                passed += 1
            else:
                failed += 1
            
            # Print progress every 10 notebooks (more frequent)
            if completed % 10 == 0 or completed == len(notebooks):
                percent = (completed / len(notebooks) * 100) if len(notebooks) > 0 else 0
                print(f"  Progress: {completed}/{len(notebooks)} ({percent:.1f}%) - Passed: {passed}, Failed: {failed}", flush=True)
                sys.stdout.flush()
                
                # Save progress incrementally
                save_progress(results, len(notebooks), report_path)
    
    # Final save
    save_progress(results, len(notebooks), report_path)
    
    # Summary
    print(f"\n✅ Execution complete!", flush=True)
    print(f"  Passed: {passed}", flush=True)
    print(f"  Failed: {failed}", flush=True)
    print(f"  Report: {report_path}", flush=True)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
