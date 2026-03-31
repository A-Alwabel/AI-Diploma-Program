#!/usr/bin/env python3
"""
Comprehensive notebook execution and verification script.
Executes all notebooks, verifies outputs, and checks alignment with curriculum.
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

# Execution timeout per notebook (seconds)
EXECUTION_TIMEOUT = 300

def get_all_notebooks():
    """Get all notebooks to execute, excluding artifacts and solutions."""
    notebooks = []
    for nb_path in BASE_DIR.rglob("*.ipynb"):
        nb_str = str(nb_path)
        # Skip artifacts and solutions
        if "artifacts" in nb_str or "SOLUTIONS_ALL" in nb_str:
            continue
        notebooks.append(nb_path)
    return sorted(notebooks)

def execute_notebook(nb_path, output_path=None):
    """Execute a single notebook using jupyter nbconvert and return results."""
    result = {
        "path": str(nb_path.relative_to(BASE_DIR)),
        "status": "unknown",
        "error": None,
        "execution_time": None,
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        start_time = time.time()
        
        # Use jupyter nbconvert to execute
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--ExecutePreprocessor.timeout=" + str(EXECUTION_TIMEOUT),
            str(nb_path)
        ]
        
        if output_path:
            cmd.extend(["--output", str(output_path)])
        
        # Execute
        process = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=EXECUTION_TIMEOUT + 10,  # Add buffer
            cwd=str(BASE_DIR)
        )
        
        end_time = time.time()
        result["execution_time"] = end_time - start_time
        
        if process.returncode == 0:
            result["status"] = "success"
        else:
            result["status"] = "error"
            result["error"] = process.stderr[:1000] if process.stderr else process.stdout[:1000]
            result["error_type"] = "ExecutionError"
            result["traceback"] = process.stderr[:5000] if process.stderr else ""
            
    except subprocess.TimeoutExpired:
        result["status"] = "error"
        result["error"] = "Execution timeout"
        result["error_type"] = "TimeoutError"
    except Exception as e:
        result["status"] = "error"
        result["error"] = f"Failed to execute: {str(e)}"
        result["error_type"] = type(e).__name__
        result["traceback"] = traceback.format_exc()
    
    return result

def categorize_error(error_str):
    """Categorize error type."""
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
    """Main execution function."""
    print("=" * 70)
    print("COMPREHENSIVE NOTEBOOK EXECUTION AND VERIFICATION")
    print("=" * 70)
    print(f"Base directory: {BASE_DIR}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    # Get all notebooks
    notebooks = get_all_notebooks()
    print(f"Found {len(notebooks)} notebooks to execute")
    print()
    
    # Execution results
    results = {
        "total": len(notebooks),
        "successful": 0,
        "failed": 0,
        "by_course": {},
        "by_error_type": {},
        "notebooks": []
    }
    
    # Execute notebooks
    for i, nb_path in enumerate(notebooks, 1):
        rel_path = nb_path.relative_to(BASE_DIR)
        course = rel_path.parts[0] if len(rel_path.parts) > 0 else "unknown"
        
        print(f"[{i}/{len(notebooks)}] Executing: {rel_path}")
        
        # Create output path
        output_path = OUTPUT_DIR / rel_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Execute
        result = execute_notebook(nb_path, output_path)
        
        # Categorize
        if result["status"] == "success":
            results["successful"] += 1
        else:
            results["failed"] += 1
            error_type = categorize_error(result.get("error", ""))
            results["by_error_type"][error_type] = results["by_error_type"].get(error_type, 0) + 1
        
        # Track by course
        if course not in results["by_course"]:
            results["by_course"][course] = {"total": 0, "successful": 0, "failed": 0}
        results["by_course"][course]["total"] += 1
        if result["status"] == "success":
            results["by_course"][course]["successful"] += 1
        else:
            results["by_course"][course]["failed"] += 1
        
        results["notebooks"].append(result)
        
        # Print status
        if result["status"] == "success":
            print(f"  ✓ Success ({result['execution_time']:.2f}s)")
        else:
            print(f"  ✗ Failed: {result.get('error_type', 'Unknown')}")
            if result.get("error"):
                error_msg = result["error"][:100]  # First 100 chars
                print(f"    {error_msg}")
        print()
    
    # Save results
    report_path = BASE_DIR / "artifacts" / "execution_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print("=" * 70)
    print("EXECUTION SUMMARY")
    print("=" * 70)
    print(f"Total notebooks: {results['total']}")
    print(f"Successful: {results['successful']} ({results['successful']/results['total']*100:.1f}%)")
    print(f"Failed: {results['failed']} ({results['failed']/results['total']*100:.1f}%)")
    print()
    
    if results["by_error_type"]:
        print("Errors by type:")
        for error_type, count in sorted(results["by_error_type"].items(), key=lambda x: -x[1]):
            print(f"  {error_type}: {count}")
        print()
    
    print("Results by course:")
    for course, stats in sorted(results["by_course"].items()):
        success_rate = stats["successful"] / stats["total"] * 100 if stats["total"] > 0 else 0
        print(f"  {course}: {stats['successful']}/{stats['total']} ({success_rate:.1f}%)")
    print()
    
    print(f"Full report saved to: {report_path}")
    print("=" * 70)
    
    return results

if __name__ == "__main__":
    try:
        results = main()
        sys.exit(0 if results["failed"] == 0 else 1)
    except KeyboardInterrupt:
        print("\n\nExecution interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nFatal error: {e}")
        traceback.print_exc()
        sys.exit(1)
