#!/usr/bin/env python3
"""
Script to fix ImportError and ModuleNotFoundError issues in notebooks.
Handles missing imports, double 'from' keywords, and import path issues.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
EXECUTION_REPORT_JSON = ARTIFACTS_DIR / "notebook_execution_report.json"


def fix_import_errors(notebook_path: Path) -> bool:
    """Fix import errors in a notebook."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                original = source
                
                # 1. Fix double 'from' keywords
                # Pattern: from sklearn.preprocessing import from ... -> from sklearn.preprocessing import ...
                source = re.sub(r'from\s+([\w\.]+)\s+import\s+from\s+([\w\.,\s]+)', r'from \1 import \2', source)
                
                # 2. Fix importt typo
                source = source.replace('importt', 'import')
                
                # 3. Add missing common imports if they're used but not imported
                # Check for LabelEncoder usage
                if 'LabelEncoder()' in source or 'LabelEncoder(' in source:
                    if 'from sklearn.preprocessing import' in source:
                        if 'LabelEncoder' not in source.split('from sklearn.preprocessing import')[1].split('\n')[0]:
                            source = re.sub(
                                r'(from sklearn\.preprocessing import[^\n]*)',
                                lambda m: m.group(1) + ', LabelEncoder' if 'LabelEncoder' not in m.group(1) else m.group(1),
                                source,
                                count=1
                            )
                    elif 'import LabelEncoder' not in source:
                        # Add import if not present
                        lines = source.split('\n')
                        for i, line in enumerate(lines):
                            if 'import' in line and 'sklearn' in line:
                                lines.insert(i + 1, 'from sklearn.preprocessing import LabelEncoder')
                                source = '\n'.join(lines)
                                break
                
                # 4. Fix broken import statements
                # Pattern: import numpy as npimport pandas -> import numpy as np\nimport pandas
                source = re.sub(r'(import\s+[^\s]+\s+as\s+\w+)(import\s+)', r'\1\n\2', source)
                source = re.sub(r'(from\s+[^\n]+)(import\s+)', r'\1\n\2', source)
                
                if source != original:
                    cell['source'] = source.splitlines(keepends=True)
                    modified = True
        
        if modified:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
        return False
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
        return False


def main():
    """Main execution."""
    print("=" * 70)
    print("IMPORT ERROR FIXER")
    print("=" * 70)
    
    if not EXECUTION_REPORT_JSON.exists():
        print(f"Error: Execution report not found at {EXECUTION_REPORT_JSON}")
        print("Please run notebook_runner.py first.")
        return
    
    # Load failed notebooks with ImportError
    with open(EXECUTION_REPORT_JSON, 'r') as f:
        report = json.load(f)
    
    failed = [
        r for r in report['results']
        if r.get('status') == 'failed' and 
        ('ImportError' in r.get('error', '') or 'ModuleNotFoundError' in r.get('error', ''))
    ]
    
    print(f"\nFound {len(failed)} ImportError failures to fix...\n")
    
    fixed_count = 0
    for i, failure in enumerate(failed, 1):
        nb_path = BASE_DIR / failure['path']
        if not nb_path.exists():
            continue
        
        if fix_import_errors(nb_path):
            fixed_count += 1
            if i % 10 == 0:
                print(f"  Progress: {i}/{len(failed)}...")
    
    print(f"\n{'=' * 70}")
    print(f"Fixed {fixed_count} notebooks")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
