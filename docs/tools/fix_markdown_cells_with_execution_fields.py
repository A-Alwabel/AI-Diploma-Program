#!/usr/bin/env python3
"""
Fix markdown cells that incorrectly have execution_count and outputs fields.
These cause JSON validation errors during execution.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def fix_notebook(nb_path: Path) -> bool:
    """Remove execution_count and outputs from markdown cells."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        
        modified = False
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                # Markdown cells should not have execution_count or outputs
                if 'execution_count' in cell:
                    del cell['execution_count']
                    modified = True
                if 'outputs' in cell:
                    del cell['outputs']
                    modified = True
        
        if modified:
            with open(nb_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
        
        return modified
    
    except Exception as e:
        print(f"  Error in {nb_path}: {e}")
        return False

def main():
    """Main function."""
    print("🔧 Fixing Markdown Cells with Execution Fields\n")
    
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
