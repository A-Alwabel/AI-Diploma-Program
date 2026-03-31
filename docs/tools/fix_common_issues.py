#!/usr/bin/env python3
"""
Fix common issues found in notebooks during execution.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def fix_broken_print_statements(notebook_path: Path) -> bool:
    """Fix broken print statements with newlines in strings."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                original = source
                
                # Fix: print('confusion\n', -> print('confusion matrix:',
                source = re.sub(r"print\('confusion\s*\n'", "print('confusion matrix:'", source)
                
                # Fix: print('\nreport\n', -> print('\nreport:',
                source = re.sub(r"print\('\s*\n\s*report\s*\n'", "print('\\nreport:'", source)
                
                # Fix any other broken print statements with newlines in strings
                # Pattern: print('text\n', -> print('text:',
                source = re.sub(r"print\('([^']+?)\s*\n'", r"print('\1:'", source)
                
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

def fix_missing_imports(notebook_path: Path, missing_imports: dict) -> bool:
    """Add missing imports to notebook if they're used but not imported."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Collect all code
        all_code = ''
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                all_code += ''.join(cell['source'])
        
        # Check what's used but not imported
        imports_to_add = []
        for module, import_stmt in missing_imports.items():
            if module in all_code and import_stmt not in all_code:
                imports_to_add.append(import_stmt)
        
        if imports_to_add:
            # Find first code cell and add imports
            for cell in nb['cells']:
                if cell['cell_type'] == 'code':
                    existing_imports = ''.join(cell['source'])
                    new_imports = '\n'.join(imports_to_add) + '\n'
                    if new_imports not in existing_imports:
                        cell['source'] = new_imports.splitlines(keepends=True) + cell['source']
                    break
            
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"Error fixing imports in {notebook_path}: {e}")
    
    return False

def main():
    """Fix common issues in notebooks."""
    print("=" * 60)
    print("FIXING COMMON NOTEBOOK ISSUES")
    print("=" * 60)
    
    # Find all notebooks
    notebooks = list(BASE_DIR.rglob("*.ipynb"))
    exclude_dirs = {".git", "__pycache__", ".ipynb_checkpoints", "artifacts"}
    notebooks = [nb for nb in notebooks if not any(excluded in nb.parts for excluded in exclude_dirs)]
    
    print(f"\nFound {len(notebooks)} notebooks")
    
    fixed_count = 0
    
    print("\nFixing broken print statements...")
    for nb_path in notebooks:
        if fix_broken_print_statements(nb_path):
            fixed_count += 1
            print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
    
    print(f"\nFixed {fixed_count} notebooks")
    print("=" * 60)

if __name__ == "__main__":
    main()
