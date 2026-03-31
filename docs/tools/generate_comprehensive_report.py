#!/usr/bin/env python3
"""
Generate comprehensive execution and alignment report.
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

BASE_DIR = Path(__file__).parent.parent
PROGRESS_FILE = BASE_DIR / "artifacts" / "execution_progress.json"
ALIGNMENT_FILE = BASE_DIR / "artifacts" / "alignment_report.json"
REPORT_FILE = BASE_DIR / "artifacts" / "comprehensive_report.md"

def load_data():
    """Load execution and alignment data."""
    progress_data = {}
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r') as f:
            progress_data = json.load(f)
    
    alignment_data = {}
    if ALIGNMENT_FILE.exists():
        with open(ALIGNMENT_FILE, 'r') as f:
            alignment_data = json.load(f)
    
    return progress_data, alignment_data

def categorize_errors(results):
    """Categorize errors from results."""
    error_categories = defaultdict(list)
    
    for path, result in results.items():
        if result.get("status") == "error":
            error = result.get("error", "").lower()
            error_type = result.get("error_type", "unknown")
            
            if "syntax" in error or "indentation" in error:
                error_categories["syntax_errors"].append(path)
            elif "module" in error or "import" in error:
                error_categories["missing_imports"].append(path)
            elif "file not found" in error:
                error_categories["file_not_found"].append(path)
            elif "timeout" in error:
                error_categories["timeout"].append(path)
            elif "api" in error or "connection" in error:
                error_categories["api_errors"].append(path)
            else:
                error_categories["other_errors"].append(path)
    
    return error_categories

def generate_report():
    """Generate comprehensive markdown report."""
    progress_data, alignment_data = load_data()
    
    results = progress_data.get("results", {})
    completed = progress_data.get("completed", [])
    
    # Statistics
    total_notebooks = alignment_data.get("total_notebooks", 0)
    successful = sum(1 for r in results.values() if r.get("status") == "success")
    failed = sum(1 for r in results.values() if r.get("status") == "error")
    not_executed = total_notebooks - len(completed)
    
    # Error categorization
    error_categories = categorize_errors(results)
    
    # Generate markdown report
    report = f"""# Comprehensive Notebook Execution and Alignment Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Executive Summary

- **Total Notebooks:** {total_notebooks}
- **Executed:** {len(completed)} ({len(completed)/total_notebooks*100:.1f}%)
- **Successful:** {successful} ({successful/total_notebooks*100:.1f}%)
- **Failed:** {failed} ({failed/total_notebooks*100:.1f}%)
- **Not Executed:** {not_executed} ({not_executed/total_notebooks*100:.1f}%)

## Execution Status by Course

"""
    
    # Course statistics
    by_course = defaultdict(lambda: {"total": 0, "successful": 0, "failed": 0})
    
    for path, result in results.items():
        course = path.split("/")[0] if "/" in path else "unknown"
        by_course[course]["total"] += 1
        if result.get("status") == "success":
            by_course[course]["successful"] += 1
        else:
            by_course[course]["failed"] += 1
    
    for course in sorted(by_course.keys()):
        stats = by_course[course]
        success_rate = stats["successful"] / stats["total"] * 100 if stats["total"] > 0 else 0
        report += f"- **{course}**: {stats['successful']}/{stats['total']} successful ({success_rate:.1f}%)\n"
    
    report += f"""
## Error Analysis

"""
    
    for category, paths in sorted(error_categories.items(), key=lambda x: -len(x[1])):
        report += f"### {category.replace('_', ' ').title()}: {len(paths)}\n\n"
        if len(paths) <= 10:
            for path in paths[:10]:
                report += f"- `{path}`\n"
        else:
            for path in paths[:10]:
                report += f"- `{path}`\n"
            report += f"- ... and {len(paths) - 10} more\n"
        report += "\n"
    
    report += f"""
## Notebook Distribution by Course/Unit

"""
    
    notebooks_by_unit = alignment_data.get("notebooks_by_course_unit", {})
    for unit, count in sorted(notebooks_by_unit.items()):
        report += f"- **{unit}**: {count} notebooks\n"
    
    report += f"""
## Recommendations

### High Priority
1. **Fix Syntax Errors** ({len(error_categories.get('syntax_errors', []))} notebooks)
   - Review and fix all syntax and indentation errors
   - These prevent notebooks from executing

2. **Add Missing Imports** ({len(error_categories.get('missing_imports', []))} notebooks)
   - Add required import statements
   - Verify all dependencies are in requirements.txt

### Medium Priority
3. **Fix Runtime Errors** ({len(error_categories.get('other_errors', []))} notebooks)
   - Review logic and calculation errors
   - Fix data loading issues

4. **Handle Timeout/API Errors** ({len(error_categories.get('timeout', [])) + len(error_categories.get('api_errors', []))} notebooks)
   - Optimize long-running code
   - Add fallback mechanisms for API calls

### Low Priority
5. **Complete Execution** ({not_executed} notebooks)
   - Execute remaining notebooks
   - Verify all outputs are educational

## Next Steps

1. Fix all syntax errors
2. Add missing imports
3. Execute remaining notebooks
4. Verify outputs align with DETAILED_UNIT_DESCRIPTIONS.md
5. Check pedagogical flow and learning objectives

---
*Report generated automatically by comprehensive review system*
"""
    
    # Save report
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Comprehensive report generated: {REPORT_FILE}")
    return report

if __name__ == "__main__":
    generate_report()
