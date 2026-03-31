#!/usr/bin/env python3
"""
Fix code cells that are missing the required 'outputs' field.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def fix_notebook(nb_path: Path) -> bool:
    """Add missing outputs field to code cells."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        
        modified = False
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'code':
                if 'outputs' not in cell:
                    cell['outputs'] = []
                    modified = True
        
        if modified:
            with open(nb_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
        
        return modified
    
    except json.JSONDecodeError:
        return False
    except Exception as e:
        print(f"  Error in {nb_path}: {e}")
        return False

def main():
    """Main function."""
    print("🔧 Fixing Missing 'outputs' Field in Code Cells\n")
    
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
