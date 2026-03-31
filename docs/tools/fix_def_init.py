#!/usr/bin/env python3
"""
Fix def__init__ → def __init__ in all notebooks
"""

import nbformat
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent

def fix_notebook(notebook_path):
    """Fix def__init__ in a single notebook."""
    try:
        nb = nbformat.read(notebook_path, as_version=4)
        modified = False
        
        for cell in nb.cells:
            if cell.cell_type != 'code':
                continue
            
            original_source = cell.source
            # Fix def__init__ → def __init__
            fixed_source = re.sub(r'def__init__', 'def __init__', original_source)
            
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
    """Fix all notebooks with def__init__ issues."""
    # Find all notebooks with def__init__
    notebooks_to_fix = []
    for nb_path in BASE_DIR.rglob("*.ipynb"):
        if "artifacts" in str(nb_path):
            continue
        try:
            with open(nb_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'def__init__' in content:
                    notebooks_to_fix.append(nb_path)
        except:
            continue
    
    print(f"Found {len(notebooks_to_fix)} notebooks with def__init__ issues\n")
    
    fixed_count = 0
    for nb_path in notebooks_to_fix:
        if fix_notebook(nb_path):
            fixed_count += 1
            print(f"Fixed: {nb_path.relative_to(BASE_DIR)}")
    
    print(f"\nFixed {fixed_count} notebooks.")

if __name__ == "__main__":
    main()
