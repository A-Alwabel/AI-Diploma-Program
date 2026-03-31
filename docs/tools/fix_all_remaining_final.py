#!/usr/bin/env python3
"""
Final comprehensive script to fix ALL remaining notebook errors.
Combines all fix patterns into one efficient pass.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
EXECUTION_REPORT_JSON = ARTIFACTS_DIR / "notebook_execution_report.json"


def fix_notebook_comprehensive(notebook_path: Path) -> bool:
    """Apply all fixes to a notebook in one pass."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
                original = source
                
                # === SYNTAX FIXES ===
                # 1. Docstring/function merging
                source = re.sub(r'(\"\"\"[^\"]*\"\"\")(def\s+)', r'\1\n\2', source)
                source = re.sub(r'(\'\'\'[^\']*\'\'\')(def\s+)', r'\1\n\2', source)
                source = re.sub(r'(\"\"\"[^\"]*\"\"\")\.(def\s+)', r'\1\n\2', source)
                source = re.sub(r'(\'\'\'[^\']*\'\'\')\.(def\s+)', r'\1\n\2', source)
                
                # 2. Import/def merging
                source = re.sub(r'(import\s+[^\n]+)(def\s+)', r'\1\n\2', source)
                source = re.sub(r'(from\s+[^\n]+)(def\s+)', r'\1\n\2', source)
                source = re.sub(r'(as\s+\w+)(def\s+)', r'\1\n\2', source)
                
                # 3. Scientific notation
                source = re.sub(r'(\w+)=(\d+)\s*\n\s*e([+-]\d+)', r'\1=\2e\3', source)
                source = re.sub(r'(\w+)\s*=\s*(\d+)\s*\n\s*e([+-]\d+)', r'\1 = \2e\3', source)
                source = re.sub(r'(\d+)\s*\n\s*e([+-]\d+)', r'\1e\2', source)
                
                # 4. Broken comments
                source = re.sub(r'(#\s*Formula:.*\([^)]+\))\s{2,}(h)', r'\1 / \2', source)
                source = re.sub(r'(#\s*[^\n]*derivative)\s*\n\s*s\b', r'\1s', source)
                source = re.sub(r'(#\s*[^\n]*poin)\s*\n\s*t\b', r'\1t', source)
                source = re.sub(r'/\s*\n\s*h\b', r' / h', source)
                
                # 5. Broken identifiers
                source = re.sub(r'\bp_rint\b', 'print', source)
                source = re.sub(r'\be_xpert\b', 'expert', source)
                source = re.sub(r'\bc_lass\b', 'class', source)
                
                # 6. __name__ patterns
                source = re.sub(r'if\s+__name__\s*==\s*\"_ _main__\"', 'if __name__ == "__main__"', source)
                source = re.sub(r'if\s+__name\s*=\s*=\s*\"\s*_main__\"', 'if __name__ == "__main__"', source)
                
                # 7. pass/def merging
                source = re.sub(r'(pass)(def\s+)', r'\1\n\2', source)
                source = re.sub(r'(\))(def\s+)', r'\1\n\2', source)
                source = re.sub(r'(\})(def\s+)', r'\1\n\2', source)
                
                # === IMPORT FIXES ===
                source = re.sub(r'from\s+([\w\.]+)\s+import\s+from\s+', r'from \1 import ', source)
                source = source.replace('importt', 'import')
                
                # Add LabelEncoder if used but not imported
                if 'LabelEncoder()' in source or 'LabelEncoder(' in source:
                    if 'from sklearn.preprocessing import' in source and 'LabelEncoder' not in source.split('from sklearn.preprocessing import')[1].split('\n')[0]:
                        source = re.sub(
                            r'(from sklearn\.preprocessing import[^\n]*)',
                            lambda m: m.group(1) + ', LabelEncoder' if 'LabelEncoder' not in m.group(1) else m.group(1),
                            source,
                            count=1
                        )
                
                # === ATTRIBUTE FIXES ===
                # Handle .serialize().decode() - serialize might return string
                if '.serialize(' in source and '.decode(' in source:
                    # More careful fix - only if it's a pattern like g.serialize(...).decode(...)
                    source = re.sub(
                        r'(\w+)\.serialize\(([^)]+)\)\.decode\([\'"]utf-8[\'"]\)',
                        r'(\1.serialize(\2) if isinstance(\1.serialize(\2), str) else \1.serialize(\2).decode(\'utf-8\'))',
                        source
                    )
                
                if source != original:
                    cell['source'] = source.splitlines(keepends=True)
                    modified = True
        
        if modified:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
        return False
    except Exception as e:
        return False


def main():
    """Main execution - fix all remaining failures."""
    print("=" * 70)
    print("FINAL COMPREHENSIVE FIX - ALL REMAINING ERRORS")
    print("=" * 70)
    
    if not EXECUTION_REPORT_JSON.exists():
        print(f"Error: Execution report not found")
        return
    
    with open(EXECUTION_REPORT_JSON, 'r') as f:
        report = json.load(f)
    
    failed = [r for r in report['results'] if r.get('status') == 'failed']
    
    print(f"\nFixing {len(failed)} remaining failures...\n")
    
    fixed_count = 0
    for i, failure in enumerate(failed, 1):
        nb_path = BASE_DIR / failure['path']
        if not nb_path.exists():
            continue
        
        if fix_notebook_comprehensive(nb_path):
            fixed_count += 1
            if i % 20 == 0:
                print(f"  Progress: {i}/{len(failed)}... ({fixed_count} fixed)")
    
    print(f"\n{'=' * 70}")
    print(f"Fixed {fixed_count} notebooks")
    print(f"{'=' * 70}")
    print("\nNext: Run 'python tools/rerun_failed.py' to verify fixes")


if __name__ == "__main__":
    main()
