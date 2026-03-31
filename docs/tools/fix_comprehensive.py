#!/usr/bin/env python3
"""
Comprehensive fix for all notebook issues
"""

import nbformat
from pathlib import Path
import re
import json

BASE_DIR = Path(__file__).parent.parent

def fix_cell_source(source):
    """Fix all code issues in cell source."""
    fixed = source
    
    # Fix def__init__ → def __init__
    fixed = re.sub(r'def__init__', 'def __init__', fixed)
    
    # Fix if__name__ → if __name__
    fixed = re.sub(r'if__name__', 'if __name__', fixed)
    
    # Fix broken newlines in middle of code
    fixed = re.sub(r'input\nshape\s*=', 'input_shape=', fixed)
    fixed = re.sub(r'model\npath\s*=', 'model_path =', fixed)
    fixed = re.sub(r'save\nformat\s*=', 'save_format=', fixed)
    
    # Fix broken print statements
    fixed = re.sub(r'^s\n#.*\nrint\(', 'print(', fixed, flags=re.MULTILINE)
    fixed = re.sub(r'\nrint\(', '\nprint(', fixed)
    
    # Fix broken variable names
    fixed = re.sub(r'st\nest_values', 'test_values', fixed)
    fixed = re.sub(r'sigmoi\nd', 'sigmoid', fixed)
    fixed = re.sub(r'create_data\n_matrix', 'create_data_matrix', fixed)
    fixed = re.sub(r'compute\n_dot\n_product', 'compute_dot_product', fixed)
    fixed = re.sub(r'compute\n_transpose', 'compute_transpose', fixed)
    
    # Fix broken class definitions
    fixed = re.sub(r'clas\ns\n', 'class ', fixed)
    fixed = re.sub(r'c\nlass ', 'class ', fixed)
    
    # Fix broken words
    fixed = re.sub(r'reasonin\ng', 'reasoning', fixed)
    fixed = re.sub(r'e\nxpert', 'expert', fixed)
    fixed = re.sub(r'adul t', 'adult', fixed)
    
    # Fix np.math.factorial → math.factorial (need to add import)
    fixed = re.sub(r'np\.math\.factorial', 'math.factorial', fixed)
    
    # Fix broken string formatting
    fixed = re.sub(r'\{sum\(([^)]+)\)\nlen\(([^)]+)\)\}', r'{sum(\1) / len(\2)}', fixed)
    fixed = re.sub(r'= total\nlen\(', '= total / len(', fixed)
    
    return fixed

def ensure_math_import(nb):
    """Ensure math module is imported if math.factorial is used."""
    for cell in nb.cells:
        if cell.cell_type == 'code' and 'math.factorial' in cell.source:
            # Check if math is imported
            if 'import math' not in cell.source and 'from math import' not in cell.source:
                # Add import at the beginning
                lines = cell.source.split('\n')
                import_added = False
                for i, line in enumerate(lines):
                    if line.strip().startswith('import ') or line.strip().startswith('from '):
                        # Add math import after other imports
                        if 'import numpy' in line or 'import pandas' in line:
                            lines.insert(i + 1, 'import math')
                            import_added = True
                            break
                if not import_added:
                    # Add at the beginning
                    lines.insert(0, 'import math')
                cell.source = '\n'.join(lines)

def fix_notebook(notebook_path):
    """Fix all issues in a notebook."""
    try:
        nb = nbformat.read(notebook_path, as_version=4)
        modified = False
        
        for cell in nb.cells:
            if cell.cell_type != 'code':
                continue
            
            original = cell.source
            fixed = fix_cell_source(original)
            
            if fixed != original:
                cell.source = fixed
                modified = True
        
        # Ensure math import if needed
        ensure_math_import(nb)
        
        if modified:
            nbformat.write(nb, notebook_path)
            return True
        return False
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
        return False

def main():
    """Fix all notebooks."""
    # Focus on known problematic notebooks
    problematic = [
        BASE_DIR / "Course 03" / "unit1-linear-algebra" / "examples" / "06_transformation_matrices_orthogonal_basis.ipynb",
        BASE_DIR / "Course 03" / "unit2-calculus" / "examples" / "05_function_approximation_ml.ipynb",
        BASE_DIR / "Course 03" / "unit5-probability" / "examples" / "06_maximum_likelihood_estimation.ipynb",
        BASE_DIR / "Course 08" / "unit5-deployment" / "examples" / "02_tensorflow_serving.ipynb",
    ]
    
    for nb_path in problematic:
        if nb_path.exists():
            if fix_notebook(nb_path):
                print(f"Fixed: {nb_path.relative_to(BASE_DIR)}")
        else:
            print(f"Not found: {nb_path}")

if __name__ == "__main__":
    main()
