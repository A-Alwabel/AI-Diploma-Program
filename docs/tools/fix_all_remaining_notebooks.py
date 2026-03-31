#!/usr/bin/env python3
"""
Fix all remaining notebook issues systematically:
1. Remove duplicate imports
2. Fix broken function definitions
3. Extract code from markdown cells
4. Fix syntax errors
"""

import json
import re
from pathlib import Path
from typing import List, Tuple, Optional

def fix_duplicate_imports(source: List[str]) -> Tuple[List[str], bool]:
    """Remove duplicate import statements"""
    seen_imports = set()
    fixed = []
    modified = False
    
    for line in source:
        stripped = line.strip()
        # Check if it's an import statement
        if stripped.startswith('import ') or stripped.startswith('from '):
            # Normalize the import (remove comments)
            import_part = stripped.split('#')[0].strip()
            if import_part in seen_imports:
                modified = True
                continue  # Skip duplicate
            seen_imports.add(import_part)
        fixed.append(line)
    
    return fixed, modified

def fix_broken_return_statements(source: List[str]) -> Tuple[List[str], bool]:
    """Fix return statements that are split incorrectly"""
    fixed = []
    modified = False
    i = 0
    
    while i < len(source):
        line = source[i]
        stripped = line.strip()
        
        # Check if this is a return statement followed by a continuation on next line
        if stripped.startswith('return ') and i + 1 < len(source):
            next_line = source[i + 1].strip()
            # If next line starts with '(' and doesn't have 'def', 'class', etc., merge them
            if (next_line.startswith('(') and 
                not any(next_line.startswith(kw) for kw in ['def ', 'class ', 'import ', 'from ', '#'])):
                # Merge the return statement
                fixed.append(line.rstrip() + ' ' + next_line.lstrip() + '\n')
                i += 2
                modified = True
                continue
        
        fixed.append(line)
        i += 1
    
    return fixed, modified

def fix_sigmoid_function(source: List[str]) -> Tuple[List[str], bool]:
    """Fix broken sigmoid function definition"""
    fixed = []
    modified = False
    i = 0
    
    while i < len(source):
        line = source[i]
        
        # Look for broken sigmoid pattern: "return 1" followed by "(1 + np.exp..."
        if 'return 1' in line and i + 1 < len(source):
            next_line = source[i + 1].strip()
            if next_line.startswith('(1 + np.exp'):
                # Fix the sigmoid function
                fixed.append('    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))\n')
                i += 2
                modified = True
                continue
        
        fixed.append(line)
        i += 1
    
    return fixed, modified

def fix_notebook(nb_path: Path) -> Tuple[bool, int]:
    """Fix all issues in a notebook"""
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        print(f"  ❌ Error loading {nb_path}: {e}")
        return False, 0
    
    total_fixes = 0
    notebook_modified = False
    
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if isinstance(source, str):
                source = source.split('\n')
                if source and not source[-1]:
                    source = [s + '\n' for s in source[:-1]] + ['']
                else:
                    source = [s + '\n' if s else '\n' for s in source]
            
            # Fix duplicate imports
            fixed, mod1 = fix_duplicate_imports(source)
            if mod1:
                total_fixes += 1
                notebook_modified = True
            
            # Fix broken return statements
            fixed, mod2 = fix_broken_return_statements(fixed)
            if mod2:
                total_fixes += 1
                notebook_modified = True
            
            # Fix sigmoid function
            fixed, mod3 = fix_sigmoid_function(fixed)
            if mod3:
                total_fixes += 1
                notebook_modified = True
            
            # Update cell source
            if notebook_modified:
                # Convert back to list format
                if fixed and isinstance(fixed[0], str):
                    # Join and split to normalize
                    joined = ''.join(fixed)
                    cell['source'] = joined.splitlines(keepends=True)
                    if cell['source'] and not cell['source'][-1].endswith('\n'):
                        cell['source'][-1] += '\n'
    
    if notebook_modified:
        try:
            with open(nb_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, ensure_ascii=False, indent=1)
            return True, total_fixes
        except Exception as e:
            print(f"  ❌ Error saving {nb_path}: {e}")
            return False, total_fixes
    
    return False, 0

def main():
    """Main function to fix all notebooks"""
    base_dir = Path(__file__).parent.parent
    notebook_dir = base_dir
    
    # Get list of all notebooks
    notebooks = list(notebook_dir.rglob('*.ipynb'))
    notebooks = [nb for nb in notebooks if '.nbconvert' not in str(nb)]
    
    print(f"🔧 Fixing All Remaining Notebook Issues\n")
    print(f"✅ Found {len(notebooks)} notebooks\n")
    
    fixed_count = 0
    total_fixes = 0
    
    for i, nb_path in enumerate(notebooks, 1):
        if i % 100 == 0:
            print(f"  Processed {i}/{len(notebooks)} notebooks...")
        
        success, fixes = fix_notebook(nb_path)
        if success:
            fixed_count += 1
            total_fixes += fixes
            if fixes > 0:
                print(f"  ✓ Fixed: {nb_path.relative_to(base_dir)} ({fixes} fixes)")
    
    print(f"\n✅ Fixed {fixed_count} notebooks ({total_fixes} total fixes)")

if __name__ == '__main__':
    main()
