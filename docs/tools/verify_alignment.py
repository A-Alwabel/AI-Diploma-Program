#!/usr/bin/env python3
"""
Verify notebook alignment with DETAILED_UNIT_DESCRIPTIONS.md
"""

import json
import re
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).parent.parent
DETAILED_UNIT_DESCRIPTIONS = BASE_DIR / "DETAILED_UNIT_DESCRIPTIONS.md"
EXECUTION_REPORT = BASE_DIR / "artifacts" / "execution_report.json"

def load_unit_descriptions():
    """Load and parse DETAILED_UNIT_DESCRIPTIONS.md."""
    if not DETAILED_UNIT_DESCRIPTIONS.exists():
        return {}
    
    with open(DETAILED_UNIT_DESCRIPTIONS, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse course structure
    courses = {}
    current_course = None
    current_unit = None
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        # Course headers
        if line.startswith('## 📘 COURSE'):
            match = re.search(r'COURSE (\d+):', line)
            if match:
                current_course = f"Course {match.group(1).zfill(2)}"
                courses[current_course] = {}
        
        # Unit headers
        elif line.startswith('#### 📖 Unit'):
            match = re.search(r'Unit (\d+):', line)
            if match and current_course:
                unit_num = match.group(1)
                # Get unit name from next line or same line
                unit_name = line.split(':', 1)[1].strip() if ':' in line else f"Unit {unit_num}"
                current_unit = f"unit{unit_num}"
                courses[current_course][current_unit] = {
                    "name": unit_name,
                    "topics": [],
                    "practical": []
                }
        
        # Topics
        elif current_course and current_unit and line.strip().startswith('-'):
            topic = line.strip()[1:].strip()
            if topic:
                courses[current_course][current_unit]["topics"].append(topic)
    
    return courses

def get_notebook_course_unit(nb_path):
    """Extract course and unit from notebook path."""
    parts = Path(nb_path).parts
    course = None
    unit = None
    
    for part in parts:
        if part.startswith("Course "):
            course = part
        elif part.startswith("unit"):
            unit = part
    
    return course, unit

def verify_alignment():
    """Verify notebook alignment with curriculum."""
    print("=" * 70)
    print("NOTEBOOK ALIGNMENT VERIFICATION")
    print("=" * 70)
    print()
    
    # Load curriculum
    curriculum = load_unit_descriptions()
    print(f"Loaded curriculum for {len(curriculum)} courses")
    print()
    
    # Load execution results
    execution_results = {}
    if EXECUTION_REPORT.exists():
        with open(EXECUTION_REPORT, 'r') as f:
            execution_data = json.load(f)
            execution_results = execution_data.get("notebooks", {})
    
    # Get all notebooks
    notebooks = []
    for nb_path in BASE_DIR.rglob("*.ipynb"):
        nb_str = str(nb_path)
        if "artifacts" in nb_str or "SOLUTIONS_ALL" in nb_str or ".nbconvert" in nb_str:
            continue
        notebooks.append(nb_path)
    
    # Analyze alignment
    alignment_report = {
        "total_notebooks": len(notebooks),
        "notebooks_by_course_unit": defaultdict(int),
        "execution_status": {
            "successful": 0,
            "failed": 0,
            "not_executed": 0
        },
        "coverage": {}
    }
    
    for nb_path in notebooks:
        course, unit = get_notebook_course_unit(nb_path)
        rel_path = str(nb_path.relative_to(BASE_DIR))
        
        if course and unit:
            key = f"{course}/{unit}"
            alignment_report["notebooks_by_course_unit"][key] += 1
            
            # Check execution status
            if rel_path in execution_results:
                result = execution_results[rel_path]
                if result.get("status") == "success":
                    alignment_report["execution_status"]["successful"] += 1
                else:
                    alignment_report["execution_status"]["failed"] += 1
            else:
                alignment_report["execution_status"]["not_executed"] += 1
    
    # Print report
    print("Notebooks by Course/Unit:")
    for key, count in sorted(alignment_report["notebooks_by_course_unit"].items()):
        print(f"  {key}: {count} notebooks")
    print()
    
    print("Execution Status:")
    exec_status = alignment_report["execution_status"]
    total = exec_status["successful"] + exec_status["failed"] + exec_status["not_executed"]
    print(f"  Successful: {exec_status['successful']}")
    print(f"  Failed: {exec_status['failed']}")
    print(f"  Not executed: {exec_status['not_executed']}")
    print()
    
    # Save report
    report_path = BASE_DIR / "artifacts" / "alignment_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, 'w') as f:
        json.dump(alignment_report, f, indent=2, ensure_ascii=False)
    
    print(f"Alignment report saved to: {report_path}")
    print("=" * 70)
    
    return alignment_report

if __name__ == "__main__":
    verify_alignment()
