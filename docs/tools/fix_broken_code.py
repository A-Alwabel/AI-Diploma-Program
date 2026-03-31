#!/usr/bin/env python3
"""
Fix broken code patterns in notebooks (line breaks in middle of words)
"""

import nbformat
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent

def fix_cell_source(source):
    """Fix broken code patterns."""
    fixed = source
    
    # Fix broken print statements
    fixed = re.sub(r'^s\n#.*\nrint\(', 'print(', fixed, flags=re.MULTILINE)
    fixed = re.sub(r'\nrint\(', '\nprint(', fixed)
    
    # Fix broken variable names
    fixed = re.sub(r'st\nest_values', 'test_values', fixed)
    fixed = re.sub(r'sigmoi\nd', 'sigmoid', fixed)
    
    # Fix broken class definitions
    fixed = re.sub(r'clas\ns\n', 'class ', fixed)
    fixed = re.sub(r'c\nlass ', 'class ', fixed)
    
    # Fix broken words
    fixed = re.sub(r'reasonin\ng', 'reasoning', fixed)
    fixed = re.sub(r'e\nxpert', 'expert', fixed)
    fixed = re.sub(r'adul t', 'adult', fixed)
    
    # Fix broken function/variable names with newlines
    fixed = re.sub(r'create_data\n_matrix', 'create_data_matrix', fixed)
    fixed = re.sub(r'compute\n_dot\n_product', 'compute_dot_product', fixed)
    fixed = re.sub(r'compute\n_transpose', 'compute_transpose', fixed)
    
    # Fix if__name__
    fixed = re.sub(r'if__name__', 'if __name__', fixed)
    
    # Fix broken print statements in comments
    fixed = re.sub(r'#.*\np\nrint', '# print', fixed)
    fixed = re.sub(r'#.*\nT\nheore\nm', '# Theorem', fixed)
    
    # Fix standalone 's' or 'd' on lines (likely broken from print/sigmoid)
    fixed = re.sub(r'^s$\n', '', fixed, flags=re.MULTILINE)
    fixed = re.sub(r'^d$\n', '', fixed, flags=re.MULTILINE)
    
    # Fix broken array endings
    fixed = re.sub(r'# TODO:.*\ns\n\)', '# TODO: Add values\n])', fixed)
    
    return fixed

def fix_notebook(notebook_path):
    """Fix broken code in a single notebook."""
    try:
        nb = nbformat.read(notebook_path, as_version=4)
        modified = False
        
        for cell in nb.cells:
            if cell.cell_type != 'code':
                continue
            
            original_source = cell.source
            fixed_source = fix_cell_source(original_source)
            
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
    """Fix broken code in exercise notebooks."""
    exercise_notebooks = [
        BASE_DIR / "Course 01" / "unit4-neural-networks-basics" / "exercises" / "exercise_01.ipynb",
        BASE_DIR / "Course 01" / "unit2-search-algorithms" / "exercises" / "exercise_01.ipynb",
        BASE_DIR / "Course 03" / "modules" / "module_01" / "exercises" / "exercise_01.ipynb",
    ]
    
    print(f"Fixing {len(exercise_notebooks)} exercise notebooks...\n")
    
    fixed_count = 0
    for nb_path in exercise_notebooks:
        if nb_path.exists():
            if fix_notebook(nb_path):
                fixed_count += 1
                print(f"Fixed: {nb_path.relative_to(BASE_DIR)}")
        else:
            print(f"Not found: {nb_path}")
    
    print(f"\nFixed {fixed_count} notebooks.")

if __name__ == "__main__":
    main()
