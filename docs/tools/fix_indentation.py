#!/usr/bin/env python3
"""
Fix indentation errors in notebooks
"""

import nbformat
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent

def fix_indentation(source):
    """Fix common indentation issues."""
    lines = source.split('\n')
    fixed_lines = []
    indent_level = 0
    
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        
        # Skip empty lines
        if not stripped:
            fixed_lines.append('')
            continue
        
        # Check for dedent patterns
        if stripped.startswith('return ') or stripped.startswith('return\n'):
            # Return should be at function level (4 spaces less)
            indent_level = max(0, indent_level - 4)
        elif stripped.startswith('if ') or stripped.startswith('elif ') or stripped.startswith('else:'):
            # Control flow at same level
            pass
        elif stripped.startswith('for ') or stripped.startswith('while '):
            # Loop - next line should be indented
            indent_level += 4
        elif stripped.startswith('def ') or stripped.startswith('class '):
            # Function/class definition - reset to base
            indent_level = 4
        
        # Apply indentation
        fixed_line = ' ' * indent_level + stripped
        fixed_lines.append(fixed_line)
    
    return '\n'.join(fixed_lines)

def fix_notebook(notebook_path):
    """Fix indentation in a notebook."""
    try:
        nb = nbformat.read(notebook_path, as_version=4)
        modified = False
        
        for cell in nb.cells:
            if cell.cell_type != 'code':
                continue
            
            original = cell.source
            # Fix specific patterns
            fixed = original
            
            # Fix function definitions with wrong indentation
            fixed = re.sub(r'^def (\w+)\([^)]*\):\s*\n\s*\n\s*"""(.*?)"""\s*\n\s+([a-z_]+) =', 
                          r'def \1:\n    """\2"""\n    \3 =', fixed, flags=re.MULTILINE | re.DOTALL)
            
            # Fix return statements
            fixed = re.sub(r'^(\s+)return ', r'    return ', fixed, flags=re.MULTILINE)
            
            if fixed != original:
                cell.source = fixed
                modified = True
        
        if modified:
            nbformat.write(nb, notebook_path)
            return True
        return False
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
        return False

def main():
    """Fix indentation in problematic notebooks."""
    notebooks = [
        BASE_DIR / "Course 03" / "unit1-linear-algebra" / "examples" / "06_transformation_matrices_orthogonal_basis.ipynb",
        BASE_DIR / "Course 03" / "unit2-calculus" / "examples" / "05_function_approximation_ml.ipynb",
        BASE_DIR / "Course 03" / "unit5-probability" / "examples" / "06_maximum_likelihood_estimation.ipynb",
    ]
    
    for nb_path in notebooks:
        if nb_path.exists():
            if fix_notebook(nb_path):
                print(f"Fixed: {nb_path.relative_to(BASE_DIR)}")
        else:
            print(f"Not found: {nb_path}")

if __name__ == "__main__":
    main()
