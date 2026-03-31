#!/usr/bin/env python3
"""
Fix common errors in Course 05+ notebooks.
"""

import nbformat
from pathlib import Path
import re
import json

BASE_DIR = Path(__file__).parent.parent

def fix_import_spaces(source):
    """Fix import statements with missing spaces."""
    # Fix: import pandas as pd_rng -> import pandas as pd\n_rng = np.random.default_rng(7)
    source = re.sub(r'import pandas as pd_rng', 'import pandas as pd\n_rng = np.random.default_rng(7)', source)
    
    # Fix: import pandas as pd_rng = ... -> import pandas as pd\n_rng = ...
    source = re.sub(r'import pandas as pd_rng =', 'import pandas as pd\n_rng =', source)
    
    # Fix: from sklearn.preprocessing  import -> from sklearn.preprocessing import
    source = re.sub(r'from sklearn\.(\w+)\s+import', r'from sklearn.\1 import', source)
    source = re.sub(r'from sklearn\.(\w+)\.(\w+)\s+import', r'from sklearn.\1.\2 import', source)
    
    # Fix: import numpy as np import pandas -> separate lines
    source = re.sub(r'import numpy as np import pandas', 'import numpy as np\nimport pandas', source)
    
    # Fix: import pandas as pd_rng = np.random... -> import pandas as pd\n_rng = np.random...
    source = re.sub(r'import pandas as pd_rng =', 'import pandas as pd\n_rng =', source)
    
    return source

def fix_class_syntax(source):
    """Fix class definition syntax errors."""
    # Fix: def__init__ -> def __init__
    source = re.sub(r'def__init__', 'def __init__', source)
    source = re.sub(r'def__str__', 'def __str__', source)
    source = re.sub(r'def__repr__', 'def __repr__', source)
    source = re.sub(r'def__call__', 'def __call__', source)
    
    # Fix: class ClassName:    def__init__ -> class ClassName:\n    def __init__
    source = re.sub(r':\s+def__init__', ':\n    def __init__', source)
    
    # Fix: class ClassName:\n\ndef__init__ -> class ClassName:\n    def __init__
    source = re.sub(r':\n\ndef__init__', ':\n    def __init__', source)
    
    return source

def fix_missing_spaces_newlines(source):
    """Fix missing spaces and newlines in code."""
    # Process line by line to avoid breaking context
    lines = source.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Skip comments and docstrings
        stripped = line.lstrip()
        if stripped.startswith('#') or stripped.startswith('"""') or stripped.startswith("'''"):
            fixed_lines.append(line)
            continue
        
        fixed_line = line
        
        # Fix: dataset_rng = ... -> dataset\n_rng = ...
        fixed_line = re.sub(r'(\w+)_rng\s*=\s*np\.random\.default_rng', r'\1\n_rng = np.random.default_rng', fixed_line)
        
        # Fix: code_variable = value -> code\nvariable = value (but avoid breaking variable names)
        # Pattern: word_underscore_variable = (where variable starts with lowercase)
        fixed_line = re.sub(r'(\w+)_([a-z]\w*)\s*=\s*', r'\1\n\2 = ', fixed_line)
        
        # Fix: = value_variable -> = value\nvariable (but only for common patterns)
        fixed_line = re.sub(r'=\s*(\w+)_([a-z]\w*)(\s|$)', r'= \1\n\2\3', fixed_line)
        
        # Fix: self.attr_self.attr2 -> self.attr\n        self.attr2
        fixed_line = re.sub(r'(\w+)_self\.', r'\1\n        self.', fixed_line)
        
        # Fix: value_reward = -> value\n        reward = (common in RL code)
        fixed_line = re.sub(r'(\w+)_reward\s*=', r'\1\n        reward =', fixed_line)
        fixed_line = re.sub(r'(\w+)_done\s*=', r'\1\n        done =', fixed_line)
        fixed_line = re.sub(r'(\w+)_new_pos\s*=', r'\1\n        new_pos =', fixed_line)
        
        # Fix: _X = df... -> X = df... (remove leading underscore when it's a variable assignment)
        if re.match(r'^_([A-Z]\w*)\s*=\s*', fixed_line):
            fixed_line = re.sub(r'^_([A-Z]\w*)\s*=\s*', r'\1 = ', fixed_line)
        
        # Fix: _y = df... -> y = df...
        if re.match(r'^_([a-z]\w*)\s*=\s*', fixed_line) and not fixed_line.startswith('_rng'):
            fixed_line = re.sub(r'^_([a-z]\w*)\s*=\s*', r'\1 = ', fixed_line)
        
        # Remove duplicate assignments (if my regex created them)
        if ' = ' in fixed_line:
            parts = fixed_line.split(' = ')
            if len(parts) > 2:
                # Keep only the first assignment
                fixed_line = ' = '.join([parts[0], ' = '.join(parts[1:])])
        
        fixed_lines.append(fixed_line)
    
    return '\n'.join(fixed_lines)

def fix_print_statements(source):
    """Fix incomplete print statements."""
    # Fix unterminated strings in print
    lines = source.split('\n')
    fixed_lines = []
    for i, line in enumerate(lines):
        # Check for unterminated strings
        if 'print(' in line and line.count('"') % 2 != 0:
            # Try to fix common cases
            if line.endswith('"') and not line.endswith('\\"'):
                # Already terminated
                fixed_lines.append(line)
            elif '"' in line and not line.rstrip().endswith('"'):
                # Add closing quote if missing
                fixed_lines.append(line + '"')
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_visualization_comments(source):
    """Fix visualization comment syntax errors."""
    # Fix: # Visualization: ...t r... -> # Visualization: ...
    source = re.sub(r'# Visualization:.*?t r', '# Visualization:', source, flags=re.DOTALL)
    source = re.sub(r'# تصور:.*?t r', '# تصور:', source, flags=re.DOTALL)
    
    return source

def fix_notebook(notebook_path):
    """Fix a single notebook."""
    try:
        nb = nbformat.read(notebook_path, as_version=4)
        modified = False
        
        for cell in nb.cells:
            if cell.cell_type != 'code':
                continue
            
            original_source = cell.source
            fixed_source = original_source
            
            # Apply fixes
            fixed_source = fix_import_spaces(fixed_source)
            fixed_source = fix_missing_spaces_newlines(fixed_source)
            fixed_source = fix_class_syntax(fixed_source)
            fixed_source = fix_print_statements(fixed_source)
            fixed_source = fix_visualization_comments(fixed_source)
            
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
    # Load failed notebooks
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
