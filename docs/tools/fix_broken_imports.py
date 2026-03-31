#!/usr/bin/env python3
"""
Fix broken import statements in notebooks that have line breaks in the middle.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def fix_broken_imports(notebook_path: Path) -> bool:
    """Fix broken import statements with line breaks."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                original = source
                
                # Fix broken imports like:
                # from sklearn.model\n_selection import train\n_test_\nsplit
                # Should be: from sklearn.model_selection import train_test_split
                
                # Pattern 1: from module\n_name import
                source = re.sub(r'from\s+(\w+)\s*\n\s*_(\w+)', r'from \1_\2', source)
                
                # Pattern 2: import name\n_name
                source = re.sub(r'import\s+(\w+)\s*\n\s*_(\w+)', r'import \1_\2', source)
                
                # Pattern 3: name\n_name (in import lists)
                source = re.sub(r'(\w+)\s*\n\s*_(\w+)', r'\1_\2', source)
                
                # Fix: train\n_test_\nsplit -> train_test_split
                source = re.sub(r'train\s*\n\s*_test_\s*\n\s*split', 'train_test_split', source)
                
                # Fix: accuracy_\nscore -> accuracy_score
                source = re.sub(r'accuracy_\s*\n\s*score', 'accuracy_score', source)
                
                # Fix: confusion\n_matrix -> confusion_matrix
                source = re.sub(r'confusion\s*\n\s*_matrix', 'confusion_matrix', source)
                
                # Fix: classification\n_report -> classification_report
                source = re.sub(r'classification\s*\n\s*_report', 'classification_report', source)
                
                # Fix: default\n_rng -> default_rng
                source = re.sub(r'default\s*\n\s*_rng', 'default_rng', source)
                
                # Fix: OneHotEncoderf\nrom -> OneHotEncoder\nfrom
                source = re.sub(r'OneHotEncoderf\s*\n\s*rom', 'OneHotEncoder\nfrom', source)
                
                # Fix: ColumnTransformerf\nrom -> ColumnTransformer\nfrom
                source = re.sub(r'ColumnTransformerf\s*\n\s*rom', 'ColumnTransformer\nfrom', source)
                
                # Fix: LogisticRegression\nfrom -> LogisticRegression
                source = re.sub(r'LogisticRegression\s*\n\s*from', 'LogisticRegression', source)
                
                # More general: fix any word\n_word patterns in import context
                # But be careful not to break string literals
                lines = source.split('\n')
                fixed_lines = []
                in_import = False
                
                for i, line in enumerate(lines):
                    # Check if this line starts an import
                    if re.match(r'^\s*(from|import)', line):
                        in_import = True
                        # Join with next line if it starts with underscore
                        if i + 1 < len(lines) and lines[i + 1].strip().startswith('_'):
                            line = line.rstrip() + lines[i + 1].lstrip()
                            # Skip next line
                            continue
                    elif in_import and line.strip() and not line.strip().startswith('#'):
                        # Still in import, check for continuation
                        if line.strip().startswith('_'):
                            # Merge with previous
                            if fixed_lines:
                                fixed_lines[-1] = fixed_lines[-1].rstrip() + line.lstrip()
                            continue
                        else:
                            in_import = False
                    else:
                        in_import = False
                    
                    fixed_lines.append(line)
                
                source = '\n'.join(fixed_lines)
                
                if source != original:
                    cell['source'] = source.splitlines(keepends=True)
                    modified = True
        
        if modified:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
    
    return False

def main():
    """Fix broken imports in all notebooks."""
    print("=" * 60)
    print("FIXING BROKEN IMPORT STATEMENTS")
    print("=" * 60)
    
    # Load failure report to target specific notebooks
    report_file = BASE_DIR / "artifacts" / "notebook_execution_report.json"
    if report_file.exists():
        with open(report_file, 'r') as f:
            report = json.load(f)
        
        failed = [r for r in report['results'] if r.get('status') == 'failed']
        sklearn_failures = [f for f in failed if 'sklearn' in f.get('error', '').lower()]
        
        print(f"\nFound {len(sklearn_failures)} notebooks with sklearn-related failures")
        print("Fixing broken imports...\n")
        
        fixed_count = 0
        for failure in sklearn_failures:
            nb_path = BASE_DIR / failure['path']
            if nb_path.exists() and fix_broken_imports(nb_path):
                fixed_count += 1
                print(f"  ✓ Fixed: {failure['path'][:60]}")
        
        print(f"\nFixed {fixed_count} notebooks")
    else:
        print("Execution report not found. Fixing all notebooks...")
        notebooks = list(BASE_DIR.rglob("*.ipynb"))
        exclude_dirs = {".git", "__pycache__", ".ipynb_checkpoints", "artifacts"}
        notebooks = [nb for nb in notebooks if not any(excluded in nb.parts for excluded in exclude_dirs)]
        
        fixed_count = 0
        for nb_path in notebooks:
            if fix_broken_imports(nb_path):
                fixed_count += 1
        
        print(f"Fixed {fixed_count} notebooks")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
