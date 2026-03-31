#!/usr/bin/env python3
"""
Analyze notebook execution failures and categorize them for fixing.
"""

import json
from pathlib import Path
from collections import defaultdict
import re

BASE_DIR = Path(__file__).parent.parent

def analyze_failures(report_file: Path):
    """Analyze failures from execution report."""
    with open(report_file, 'r') as f:
        report = json.load(f)
    
    results = report.get('results', [])
    failed = [r for r in results if r.get('status') == 'failed']
    
    print("=" * 60)
    print("FAILURE ANALYSIS")
    print("=" * 60)
    print(f"\nTotal Failed: {len(failed)}")
    print(f"Total Executed: {len(results)}")
    print(f"Pass Rate: {(len(results) - len(failed)) / len(results) * 100:.1f}%")
    
    # Categorize failures
    categories = {
        "missing_imports": [],
        "syntax_errors": [],
        "missing_packages": [],
        "file_not_found": [],
        "api_errors": [],
        "timeout": [],
        "other": []
    }
    
    missing_packages = {
        'tensorflow', 'keras', 'torch', 'rdflib', 'spacy', 
        'transformers', 'gym', 'sklearn', 'scikit-learn'
    }
    
    for failure in failed:
        error = failure.get('error', '').lower()
        error_tb = failure.get('error_traceback', '').lower()
        full_error = (error + ' ' + error_tb).lower()
        
        if 'timeout' in error:
            categories['timeout'].append(failure)
        elif any(pkg in full_error for pkg in ['module', 'import', 'no module named']):
            # Check which specific package
            found_pkg = None
            for pkg in missing_packages:
                if pkg in full_error:
                    found_pkg = pkg
                    break
            if found_pkg:
                categories['missing_packages'].append((found_pkg, failure))
            else:
                categories['missing_imports'].append(failure)
        elif any(term in full_error for term in ['syntax', 'invalid syntax', 'indentation']):
            categories['syntax_errors'].append(failure)
        elif any(term in full_error for term in ['file not found', 'no such file', 'cannot find']):
            categories['file_not_found'].append(failure)
        elif any(term in full_error for term in ['api', 'key', 'authentication', 'token']):
            categories['api_errors'].append(failure)
        else:
            categories['other'].append(failure)
    
    # Print analysis
    print("\n" + "=" * 60)
    print("FAILURE CATEGORIES")
    print("=" * 60)
    
    for category, failures in categories.items():
        if category == 'missing_packages':
            # Group by package
            by_package = defaultdict(list)
            for pkg, failure in failures:
                by_package[pkg].append(failure)
            print(f"\n{category.upper().replace('_', ' ')}: {len(failures)} failures")
            for pkg, pkg_failures in sorted(by_package.items(), key=lambda x: -len(x[1])):
                print(f"  - {pkg}: {len(pkg_failures)} failures")
        else:
            print(f"\n{category.upper().replace('_', ' ')}: {len(failures)} failures")
            if failures:
                print(f"  Sample failures:")
                for f in failures[:3]:
                    print(f"    - {f.get('path', 'unknown')[:60]}")
    
    # Generate fix recommendations
    print("\n" + "=" * 60)
    print("FIX RECOMMENDATIONS")
    print("=" * 60)
    
    if categories['missing_packages']:
        packages_needed = set()
        for pkg, _ in categories['missing_packages']:
            packages_needed.add(pkg)
        print(f"\n1. Install missing packages:")
        print(f"   pip install {' '.join(sorted(packages_needed))}")
    
    if categories['syntax_errors']:
        print(f"\n2. Fix syntax errors in {len(categories['syntax_errors'])} notebooks")
        print(f"   Run: python tools/fix_common_issues.py")
    
    if categories['file_not_found']:
        print(f"\n3. Fix missing file references in {len(categories['file_not_found'])} notebooks")
        print(f"   Add data download cells or use synthetic data")
    
    if categories['api_errors']:
        print(f"\n4. Handle API errors in {len(categories['api_errors'])} notebooks")
        print(f"   Add API key checks or skip gracefully")
    
    # Save detailed analysis
    analysis_file = BASE_DIR / "artifacts" / "failure_analysis.json"
    with open(analysis_file, 'w') as f:
        json.dump({
            "total_failed": len(failed),
            "categories": {
                k: len(v) if k != 'missing_packages' else len(v) 
                for k, v in categories.items()
            },
            "missing_packages": list(set(pkg for pkg, _ in categories['missing_packages'])),
            "sample_failures": {
                k: [{"path": f.get('path'), "error": f.get('error', '')[:200]} 
                    for f in (v[:5] if k != 'missing_packages' else [f for _, f in v[:5]])]
                for k, v in categories.items()
            }
        }, f, indent=2)
    
    print(f"\n✓ Detailed analysis saved to: {analysis_file}")
    
    return categories

if __name__ == "__main__":
    report_file = BASE_DIR / "artifacts" / "notebook_execution_report.json"
    if report_file.exists():
        analyze_failures(report_file)
    else:
        print(f"Execution report not found: {report_file}")
        print("Waiting for execution to complete...")
