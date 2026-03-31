#!/usr/bin/env python3
"""
Fix common errors in Course 05+ notebooks - conservative approach.
"""

import nbformat
from pathlib import Path
import re
import json

BASE_DIR = Path(__file__).parent.parent

def fix_notebook(notebook_path):
    """Fix a single notebook with conservative patterns."""
    try:
        nb = nbformat.read(notebook_path, as_version=4)
        modified = False
        
        for cell in nb.cells:
            if cell.cell_type != 'code':
                continue
            
            original_source = cell.source
            fixed_source = original_source
            
            # Only fix very specific, safe patterns
            
            # 1. Fix: import pandas as pd_rng -> import pandas as pd\n_rng = np.random.default_rng(7)
            if 'import pandas as pd_rng' in fixed_source:
                fixed_source = fixed_source.replace('import pandas as pd_rng', 'import pandas as pd\n_rng = np.random.default_rng(7)')
            
            # 2. Fix: from sklearn.xxx  import -> from sklearn.xxx import (double space)
            fixed_source = re.sub(r'from sklearn\.(\w+)\s{2,}import', r'from sklearn.\1 import', fixed_source)
            fixed_source = re.sub(r'from sklearn\.(\w+)\.(\w+)\s{2,}import', r'from sklearn.\1.\2 import', fixed_source)
            
            # 3. Fix: def__init__ -> def __init__ (only in class context)
            fixed_source = re.sub(r'def__init__', 'def __init__', fixed_source)
            fixed_source = re.sub(r'def__str__', 'def __str__', fixed_source)
            fixed_source = re.sub(r'def__repr__', 'def __repr__', fixed_source)
            
            # 4. Fix: dataset_rng = -> dataset\n_rng = (very specific pattern)
            fixed_source = re.sub(r'(\w+)dataset_rng\s*=\s*np\.random', r'\1dataset\n_rng = np.random', fixed_source)
            fixed_source = re.sub(r'#\s*(\w+)\s*dataset_rng\s*=', r'# \1 dataset\n_rng =', fixed_source)
            
            # 5. Fix: _x1 = value -> x1 = value (when at start of statement, not in variable names)
            # But only if it's clearly a variable assignment, not part of a longer name
            lines = fixed_source.split('\n')
            fixed_lines = []
            for line in lines:
                # Only fix if line starts with _variable = (not _variable_name)
                if re.match(r'^_([a-z]\w*)\s*=\s*', line) and not line.startswith('_rng'):
                    line = re.sub(r'^_([a-z]\w*)\s*=\s*', r'\1 = ', line)
                fixed_lines.append(line)
            fixed_source = '\n'.join(fixed_lines)
            
            # 6. Fix: code_x1 = -> code\nx1 = (but avoid breaking max_iter, train_test, etc.)
            # Only fix patterns where underscore is clearly separating statements
            fixed_source = re.sub(r'(\w+)_([a-z]\w*)\s*=\s*(\w+\.)', r'\1\n\2 = \3', fixed_source)
            fixed_source = re.sub(r'(\w+)_([a-z]\w*)\s*=\s*(\[)', r'\1\n\2 = \3', fixed_source)
            fixed_source = re.sub(r'(\w+)_([a-z]\w*)\s*=\s*\(', r'\1\n\2 = (', fixed_source)
            
            # 7. Fix: df.drop_X = -> df.drop\nX = (specific pattern)
            fixed_source = re.sub(r'\)\)_X\s*=\s*', '))\nX = ', fixed_source)
            fixed_source = re.sub(r'\)\)_y\s*=\s*', '))\ny = ', fixed_source)
            
            # 8. Fix visualization comments
            fixed_source = re.sub(r'# Visualization:.*?t r', '# Visualization:', fixed_source, flags=re.DOTALL)
            fixed_source = re.sub(r'# تصور:.*?t r', '# تصور:', fixed_source, flags=re.DOTALL)
            
            if fixed_source != original_source:
                cell.source = fixed_source
                modified = True
        
        if modified:
            nbformat.write(nb, notebook_path)
            return True
        return False
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
        return False

def main():
    """Fix all Course 05+ failed notebooks."""
    report_file = BASE_DIR / "artifacts" / "notebook_execution_report.json"
    if not report_file.exists():
        print("Report file not found!")
        return
    
    with open(report_file, 'r') as f:
        report = json.load(f)
    
    failed = [r for r in report['results'] if r.get('status') == 'failed']
    
    # Filter Course 05 onwards
    course_05_plus = []
    for r in failed:
        path = r.get('path', '')
        if path.startswith('Course 0') or path.startswith('Course 1'):
            course_num = path.split('/')[0].replace('Course ', '')
            try:
                num = int(course_num)
                if num >= 5:
                    course_05_plus.append(BASE_DIR / path)
            except:
                pass
    
    print(f"Fixing {len(course_05_plus)} notebooks from Course 05 onwards...\n")
    
    fixed_count = 0
    for nb_path in course_05_plus:
        if nb_path.exists():
            if fix_notebook(nb_path):
                fixed_count += 1
                print(f"Fixed: {nb_path.relative_to(BASE_DIR)}")
        else:
            print(f"Not found: {nb_path}")
    
    print(f"\nFixed {fixed_count} notebooks.")

if __name__ == "__main__":
    main()
