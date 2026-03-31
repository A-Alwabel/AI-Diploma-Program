#!/usr/bin/env python3
"""
Batch notebook execution with progress saving.
Executes notebooks in batches and saves progress.
"""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime
import traceback
import time

BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "artifacts" / "executed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PROGRESS_FILE = BASE_DIR / "artifacts" / "execution_progress.json"
REPORT_FILE = BASE_DIR / "artifacts" / "execution_report.json"

EXECUTION_TIMEOUT = 300

def get_all_notebooks():
    """Get all notebooks to execute."""
    notebooks = []
    for nb_path in BASE_DIR.rglob("*.ipynb"):
        nb_str = str(nb_path)
        if "artifacts" in nb_str or "SOLUTIONS_ALL" in nb_str:
            continue
        # Skip .nbconvert files
        if ".nbconvert" in nb_str:
            continue
        notebooks.append(nb_path)
    return sorted(notebooks)

def load_progress():
    """Load execution progress."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {"completed": [], "results": {}}

def save_progress(progress):
    """Save execution progress."""
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=2)

def execute_notebook(nb_path):
    """Execute a single notebook."""
    result = {
        "path": str(nb_path.relative_to(BASE_DIR)),
        "status": "unknown",
        "error": None,
        "execution_time": None,
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        start_time = time.time()
        
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--ExecutePreprocessor.timeout=" + str(EXECUTION_TIMEOUT),
            str(nb_path),
            "--output-dir", str(OUTPUT_DIR / nb_path.parent.relative_to(BASE_DIR))
        ]
        
        process = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=EXECUTION_TIMEOUT + 10,
            cwd=str(BASE_DIR)
        )
        
        end_time = time.time()
        result["execution_time"] = end_time - start_time
        
        if process.returncode == 0:
            result["status"] = "success"
        else:
            result["status"] = "error"
            error_msg = process.stderr if process.stderr else process.stdout
            result["error"] = error_msg[:500] if error_msg else "Unknown error"
            result["error_type"] = "ExecutionError"
            
    except subprocess.TimeoutExpired:
        result["status"] = "error"
        result["error"] = "Execution timeout"
        result["error_type"] = "TimeoutError"
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)[:500]
        result["error_type"] = type(e).__name__
    
    return result

def categorize_error(error_str):
    """Categorize error type."""
    if not error_str:
        return "unknown"
    error_lower = error_str.lower()
    
    if "syntaxerror" in error_lower or "indentationerror" in error_lower:
        return "syntax_error"
    elif "modulenotfounderror" in error_lower or "importerror" in error_lower:
        return "missing_import"
    elif "filenotfounderror" in error_lower:
        return "file_not_found"
    elif "timeout" in error_lower:
        return "timeout"
    elif "api" in error_lower or "connection" in error_lower:
        return "api_error"
    else:
        return "other"

def main():
    """Main execution."""
    print("=" * 70)
    print("BATCH NOTEBOOK EXECUTION")
    print("=" * 70)
    
    notebooks = get_all_notebooks()
    progress = load_progress()
    completed_paths = set(progress.get("completed", []))
    
    # Filter out already completed
    remaining = [nb for nb in notebooks if str(nb.relative_to(BASE_DIR)) not in completed_paths]
    
    print(f"Total notebooks: {len(notebooks)}")
    print(f"Already completed: {len(completed_paths)}")
    print(f"Remaining: {len(remaining)}")
    print()
    
    results = progress.get("results", {})
    stats = {
        "total": len(notebooks),
        "successful": sum(1 for r in results.values() if r.get("status") == "success"),
        "failed": sum(1 for r in results.values() if r.get("status") == "error"),
        "by_error_type": {},
        "by_course": {}
    }
    
    # Execute remaining notebooks
    for i, nb_path in enumerate(remaining, 1):
        rel_path = str(nb_path.relative_to(BASE_DIR))
        course = rel_path.split("/")[0] if "/" in rel_path else "unknown"
        
        print(f"[{i}/{len(remaining)}] {rel_path[:60]}...")
        
        result = execute_notebook(nb_path)
        results[rel_path] = result
        completed_paths.add(rel_path)
        
        # Update stats
        if result["status"] == "success":
            stats["successful"] += 1
        else:
            stats["failed"] += 1
            error_type = categorize_error(result.get("error", ""))
            stats["by_error_type"][error_type] = stats["by_error_type"].get(error_type, 0) + 1
        
        # Update course stats
        if course not in stats["by_course"]:
            stats["by_course"][course] = {"total": 0, "successful": 0, "failed": 0}
        stats["by_course"][course]["total"] += 1
        if result["status"] == "success":
            stats["by_course"][course]["successful"] += 1
        else:
            stats["by_course"][course]["failed"] += 1
        
        # Print status
        if result["status"] == "success":
            print(f"  ✓ Success ({result['execution_time']:.2f}s)")
        else:
            print(f"  ✗ Failed: {result.get('error_type', 'Unknown')}")
        
        # Save progress every 10 notebooks
        if i % 10 == 0:
            progress["completed"] = list(completed_paths)
            progress["results"] = results
            save_progress(progress)
            print(f"  [Progress saved: {i}/{len(remaining)}]")
        print()
    
    # Final save
    progress["completed"] = list(completed_paths)
    progress["results"] = results
    save_progress(progress)
    
    # Save final report
    final_report = {
        **stats,
        "notebooks": results,
        "timestamp": datetime.now().isoformat()
    }
    with open(REPORT_FILE, 'w') as f:
        json.dump(final_report, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print("=" * 70)
    print("EXECUTION SUMMARY")
    print("=" * 70)
    print(f"Total: {stats['total']}")
    print(f"Successful: {stats['successful']} ({stats['successful']/stats['total']*100:.1f}%)")
    print(f"Failed: {stats['failed']} ({stats['failed']/stats['total']*100:.1f}%)")
    print()
    
    if stats["by_error_type"]:
        print("Errors by type:")
        for error_type, count in sorted(stats["by_error_type"].items(), key=lambda x: -x[1]):
            print(f"  {error_type}: {count}")
        print()
    
    print(f"Report saved to: {REPORT_FILE}")
    print("=" * 70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExecution interrupted. Progress saved.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nFatal error: {e}")
        traceback.print_exc()
        sys.exit(1)
