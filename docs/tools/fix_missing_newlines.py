#!/usr/bin/env python3
"""
Fix missing newlines between statements in code cells.
Common pattern: .valuesy = should be .values\ny =
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def fix_missing_newlines_in_source(source_list: list) -> tuple[list, bool]:
    """Fix missing newlines between statements in source list."""
    modified = False
    source_str = ''.join(source_list)
    
    # Pattern: .valuesy = or .valuesx = etc (missing newline)
    if re.search(r'\.values[a-z_]\s*=', source_str):
        # Split at .values
        source_str = re.sub(r'(\.values)([a-z_]\s*=)', r'\1\n\2', source_str)
        modified = True
    
    # Pattern: ]y = or ]x = (missing newline after bracket)
    if re.search(r'\]\s*[a-z_]\s*=', source_str):
        source_str = re.sub(r'(\])\s*([a-z_]\s*=)', r'\1\n\2', source_str)
        modified = True
    
    # Pattern: )y = or )x = (missing newline after parenthesis)
    if re.search(r'\)\s*[a-z_]\s*=', source_str):
        source_str = re.sub(r'(\))\s*([a-z_]\s*=)', r'\1\n\2', source_str)
        modified = True
    
    if modified:
        # Split back into list format preserving newlines
        return source_str.splitlines(keepends=True), True
    
    return source_list, False

def fix_notebook(nb_path: Path) -> bool:
    """Fix missing newlines in code cells."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        
        modified = False
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'code':
                source_list = cell.get('source', [])
                fixed_source_list, cell_modified = fix_missing_newlines_in_source(source_list)
                
                if cell_modified:
                    cell['source'] = fixed_source_list
                    modified = True
        
        if modified:
            with open(nb_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
        
        return modified
    
    except json.JSONDecodeError:
        return False
    except Exception:
        return False

def main():
    """Main function."""
    print("🔧 Fixing Missing Newlines in Code Cells\n")
    
    notebooks = list(BASE_DIR.rglob("*.ipynb"))
    notebooks = [nb for nb in notebooks 
                 if 'artifacts' not in str(nb) 
                 and '.ipynb_checkpoints' not in str(nb) 
                 and '.nbconvert' not in str(nb)
                 and 'SOLUTIONS_ALL' not in str(nb)]
    
    print(f"✅ Found {len(notebooks)} notebooks\n")
    
    fixed_count = 0
    
    for i, nb_path in enumerate(notebooks, 1):
        if fix_notebook(nb_path):
            fixed_count += 1
            if fixed_count <= 30:
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
        
        if i % 100 == 0:
            print(f"  Processed {i}/{len(notebooks)} notebooks...")
    
    print(f"\n✅ Fixed {fixed_count} notebooks")

if __name__ == "__main__":
    main()
