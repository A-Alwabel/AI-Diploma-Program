#!/usr/bin/env python3
"""
Execute all notebooks in the repository and generate execution reports.
"""

import json
import sys
import time
import traceback
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import subprocess

try:
    from nbclient import NotebookClient
    from nbformat import read, write, NO_CONVERT
    NB_CLIENT_AVAILABLE = True
except ImportError:
    NB_CLIENT_AVAILABLE = False
    print("Warning: nbclient not available, will use nbconvert instead")

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Execution timeout per notebook (in seconds)
NOTEBOOK_TIMEOUT = 300  # 5 minutes

def find_all_notebooks(base_dir: Path) -> List[Path]:
    """Find all .ipynb files in the repository."""
    notebooks = []
    
    # Exclude certain directories
    exclude_dirs = {
        ".git", "__pycache__", ".ipynb_checkpoints", 
        "artifacts", "node_modules", ".venv", "venv"
    }
    
    for nb_path in base_dir.rglob("*.ipynb"):
        # Skip if in excluded directory
        if any(excluded in nb_path.parts for excluded in exclude_dirs):
            continue
        notebooks.append(nb_path)
    
    return sorted(notebooks)

def classify_notebook(notebook_path: Path) -> Dict[str, Optional[str]]:
    """Classify notebook by course and unit."""
    rel_path = notebook_path.relative_to(BASE_DIR)
    parts = rel_path.parts
    
    classification = {
        "course": None,
        "unit": None,
        "type": None,  # "example", "exercise", or "other"
        "path": str(rel_path)
    }
    
    # Find course
    for part in parts:
        if part.startswith("Course "):
            classification["course"] = part
            break
    
    # Find unit
    for part in parts:
        if part.startswith("unit"):
            classification["unit"] = part
            break
    
    # Determine type
    if "examples" in parts:
        classification["type"] = "example"
    elif "exercises" in parts:
        classification["type"] = "exercise"
    elif "EXAMPLES" in parts:
        classification["type"] = "example"
    elif "EXERCISES" in parts:
        classification["type"] = "exercise"
    else:
        classification["type"] = "other"
    
    return classification

def execute_notebook_nbclient(notebook_path: Path) -> Dict:
    """Execute notebook using nbclient."""
    start_time = time.time()
    result = {
        "path": str(notebook_path.relative_to(BASE_DIR)),
        "status": "unknown",
        "execution_time": 0,
        "error": None,
        "error_traceback": None
    }
    
    try:
        # Read notebook
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = read(f, as_version=4)
        
        # Execute
        client = NotebookClient(nb, timeout=NOTEBOOK_TIMEOUT, kernel_name="python3")
        client.execute()
        
        # Save executed notebook
        executed_dir = BASE_DIR / "artifacts" / "executed"
        executed_dir.mkdir(parents=True, exist_ok=True)
        
        # Create relative path structure
        rel_path = notebook_path.relative_to(BASE_DIR)
        executed_path = executed_dir / rel_path
        executed_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(executed_path, "w", encoding="utf-8") as f:
            write(nb, f)
        
        result["status"] = "passed"
        result["execution_time"] = time.time() - start_time
        
    except Exception as e:
        result["status"] = "failed"
        result["execution_time"] = time.time() - start_time
        result["error"] = str(e)
        result["error_traceback"] = traceback.format_exc()
    
    return result

def execute_notebook_nbconvert(notebook_path: Path) -> Dict:
    """Execute notebook using nbconvert (fallback method)."""
    start_time = time.time()
    result = {
        "path": str(notebook_path.relative_to(BASE_DIR)),
        "status": "unknown",
        "execution_time": 0,
        "error": None,
        "error_traceback": None
    }
    
    try:
        # Use jupyter nbconvert --execute
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--ExecutePreprocessor.timeout=" + str(NOTEBOOK_TIMEOUT),
            "--ExecutePreprocessor.kernel_name=python3",
            str(notebook_path)
        ]
        
        process = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=NOTEBOOK_TIMEOUT + 60,  # Add buffer
            cwd=str(BASE_DIR)
        )
        
        if process.returncode == 0:
            result["status"] = "passed"
        else:
            result["status"] = "failed"
            result["error"] = process.stderr or process.stdout
            result["error_traceback"] = process.stderr
        
        result["execution_time"] = time.time() - start_time
        
    except subprocess.TimeoutExpired:
        result["status"] = "failed"
        result["execution_time"] = time.time() - start_time
        result["error"] = f"Execution timeout ({NOTEBOOK_TIMEOUT}s)"
    except Exception as e:
        result["status"] = "failed"
        result["execution_time"] = time.time() - start_time
        result["error"] = str(e)
        result["error_traceback"] = traceback.format_exc()
    
    return result

def execute_notebook(notebook_path: Path) -> Dict:
    """Execute a notebook and return result."""
    if NB_CLIENT_AVAILABLE:
        return execute_notebook_nbclient(notebook_path)
    else:
        return execute_notebook_nbconvert(notebook_path)

def main():
    """Main execution."""
    print("=" * 60)
    print("NOTEBOOK EXECUTION RUNNER")
    print("=" * 60)
    
    # Find all notebooks
    print("\n1. Discovering notebooks...")
    notebooks = find_all_notebooks(BASE_DIR)
    print(f"   ✓ Found {len(notebooks)} notebooks")
    
    if not notebooks:
        print("   ✗ No notebooks found!")
        return
    
    # Initialize report
    report = {
        "timestamp": datetime.now().isoformat(),
        "total_notebooks": len(notebooks),
        "execution_method": "nbclient" if NB_CLIENT_AVAILABLE else "nbconvert",
        "timeout_per_notebook": NOTEBOOK_TIMEOUT,
        "results": []
    }
    
    # Execute notebooks
    print(f"\n2. Executing notebooks (timeout: {NOTEBOOK_TIMEOUT}s per notebook)...")
    print("   This may take a while...\n")
    
    passed = 0
    failed = 0
    
    for i, notebook_path in enumerate(notebooks, 1):
        classification = classify_notebook(notebook_path)
        print(f"[{i}/{len(notebooks)}] {classification['path']}...", end=" ", flush=True)
        
        result = execute_notebook(notebook_path)
        result.update(classification)
        
        if result["status"] == "passed":
            passed += 1
            print(f"✓ ({result['execution_time']:.1f}s)")
        else:
            failed += 1
            print(f"✗ ({result['execution_time']:.1f}s)")
            if result.get("error"):
                error_preview = result["error"][:100].replace("\n", " ")
                print(f"     Error: {error_preview}...")
        
        report["results"].append(result)
    
    # Finalize report
    report["summary"] = {
        "passed": passed,
        "failed": failed,
        "pass_rate": (passed / len(notebooks) * 100) if notebooks else 0
    }
    
    # Save reports
    print(f"\n3. Saving reports...")
    
    # JSON report
    json_file = BASE_DIR / "artifacts" / "notebook_execution_report.json"
    json_file.parent.mkdir(parents=True, exist_ok=True)
    with open(json_file, "w") as f:
        json.dump(report, f, indent=2)
    print(f"   ✓ Saved JSON report: {json_file}")
    
    # Markdown report
    md_file = BASE_DIR / "NOTEBOOK_EXECUTION_REPORT.md"
    with open(md_file, "w") as f:
        f.write("# Notebook Execution Report\n\n")
        f.write(f"**Generated:** {report['timestamp']}\n\n")
        f.write(f"**Execution Method:** {report['execution_method']}\n")
        f.write(f"**Timeout per Notebook:** {report['timeout_per_notebook']}s\n\n")
        
        f.write("## Summary\n\n")
        f.write(f"- **Total Notebooks:** {report['total_notebooks']}\n")
        f.write(f"- **Passed:** {report['summary']['passed']} ✅\n")
        f.write(f"- **Failed:** {report['summary']['failed']} ❌\n")
        f.write(f"- **Pass Rate:** {report['summary']['pass_rate']:.1f}%\n\n")
        
        # Group by course
        by_course = {}
        for result in report["results"]:
            course = result.get("course", "Unknown")
            if course not in by_course:
                by_course[course] = {"passed": 0, "failed": 0, "notebooks": []}
            if result["status"] == "passed":
                by_course[course]["passed"] += 1
            else:
                by_course[course]["failed"] += 1
            by_course[course]["notebooks"].append(result)
        
        f.write("## Results by Course\n\n")
        for course in sorted([k for k in by_course.keys() if k is not None]):
            course_data = by_course[course]
            total = course_data["passed"] + course_data["failed"]
            pass_rate = (course_data["passed"] / total * 100) if total > 0 else 0
            f.write(f"### {course}\n\n")
            f.write(f"- **Total:** {total}\n")
            f.write(f"- **Passed:** {course_data['passed']} ✅\n")
            f.write(f"- **Failed:** {course_data['failed']} ❌\n")
            f.write(f"- **Pass Rate:** {pass_rate:.1f}%\n\n")
        
        # Failed notebooks
        failed_notebooks = [r for r in report["results"] if r["status"] == "failed"]
        if failed_notebooks:
            f.write("## Failed Notebooks\n\n")
            for result in failed_notebooks:
                f.write(f"### {result['path']}\n\n")
                f.write(f"- **Course:** {result.get('course', 'Unknown')}\n")
                f.write(f"- **Unit:** {result.get('unit', 'Unknown')}\n")
                f.write(f"- **Type:** {result.get('type', 'Unknown')}\n")
                f.write(f"- **Execution Time:** {result['execution_time']:.1f}s\n")
                if result.get("error"):
                    f.write(f"- **Error:**\n```\n{result['error']}\n```\n")
                if result.get("error_traceback"):
                    f.write(f"- **Traceback:**\n```\n{result['error_traceback']}\n```\n")
                f.write("\n")
    
    print(f"   ✓ Saved Markdown report: {md_file}")
    
    print("\n" + "=" * 60)
    print("EXECUTION COMPLETE")
    print("=" * 60)
    print(f"Passed: {passed} ✅")
    print(f"Failed: {failed} ❌")
    print(f"Pass Rate: {report['summary']['pass_rate']:.1f}%")
    print("=" * 60)

if __name__ == "__main__":
    main()
