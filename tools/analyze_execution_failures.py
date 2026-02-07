#!/usr/bin/env python3
"""Analyze execution failures and categorize them."""

import json
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def main():
    with open(BASE_DIR / 'artifacts/notebook_execution_report_v2.json') as f:
        data = json.load(f)
    
    results = data.get('results', [])
    # Use 'status' field instead of 'success'
    failed = [r for r in results if r.get('status') != 'passed']
    passed = [r for r in results if r.get('status') == 'passed']
    
    print(f"📊 Execution Analysis\n")
    print(f"Total notebooks: {len(results)}")
    print(f"Passed: {len(passed)}")
    print(f"Failed: {len(failed)}\n")
    
    # Filter out .nbconvert duplicates
    real_failed = [r for r in failed if '.nbconvert' not in r.get('path', '')]
    real_passed = [r for r in passed if '.nbconvert' not in r.get('path', '')]
    
    print(f"Real notebooks (excluding .nbconvert duplicates):")
    print(f"  Passed: {len(real_passed)}")
    print(f"  Failed: {len(real_failed)}\n")
    
    # Categorize errors
    error_types = Counter()
    error_examples = {}
    
    for r in real_failed:
        error = r.get('error', '') or r.get('stderr', '') or ''
        error_lower = error.lower()
        
        if 'syntaxerror' in error_lower or 'invalid syntax' in error_lower:
            error_types['SyntaxError'] += 1
            if 'SyntaxError' not in error_examples:
                error_examples['SyntaxError'] = (r.get('path', ''), error[:300])
        elif 'nameerror' in error_lower:
            error_types['NameError'] += 1
            if 'NameError' not in error_examples:
                error_examples['NameError'] = (r.get('path', ''), error[:300])
        elif 'importerror' in error_lower or 'modulenotfounderror' in error_lower:
            error_types['ImportError'] += 1
            if 'ImportError' not in error_examples:
                error_examples['ImportError'] = (r.get('path', ''), error[:300])
        elif 'timeout' in error_lower:
            error_types['Timeout'] += 1
            if 'Timeout' not in error_examples:
                error_examples['Timeout'] = (r.get('path', ''), error[:300])
        elif 'json' in error_lower or 'expecting value' in error_lower:
            error_types['JSON'] += 1
            if 'JSON' not in error_examples:
                error_examples['JSON'] = (r.get('path', ''), error[:300])
        elif 'indentationerror' in error_lower:
            error_types['IndentationError'] += 1
            if 'IndentationError' not in error_examples:
                error_examples['IndentationError'] = (r.get('path', ''), error[:300])
        else:
            error_types['Other'] += 1
            if 'Other' not in error_examples:
                error_examples['Other'] = (r.get('path', ''), error[:300])
    
    print(f"Error breakdown:")
    for err_type, count in error_types.most_common():
        print(f"  {err_type}: {count}")
    
    print(f"\nSample errors:")
    for err_type, (path, error) in error_examples.items():
        print(f"\n{err_type} ({path}):")
        print(f"  {error}")
    
    # List all failed notebooks
    print(f"\n\nAll failed notebooks:")
    for r in sorted(real_failed, key=lambda x: x.get('path', '')):
        print(f"  {r.get('path', '')}")

if __name__ == "__main__":
    main()
