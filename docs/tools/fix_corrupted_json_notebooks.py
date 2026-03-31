#!/usr/bin/env python3
"""
Attempt to repair corrupted JSON notebooks by:
1. Reading file with error handling
2. Finding and fixing JSON structure issues
3. Truncating at corruption point if needed
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def repair_json_notebook(notebook_path: Path) -> bool:
    """Attempt to repair a corrupted JSON notebook."""
    try:
        # Read file with error handling
        with open(notebook_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Try to parse
        try:
            nb = json.loads(content)
            # Already valid
            return False
        except json.JSONDecodeError as e:
            # Try to fix
            pos = e.pos
            
            # Strategy 1: Find last complete cell and truncate there
            # Look for pattern: }, followed by new cell or end
            # Find all cell endings
            cell_endings = []
            for match in re.finditer(r'\}\s*,\s*\{', content):
                cell_endings.append(match.end() - 1)
            
            # Also find cells array ending
            cells_array_end = content.rfind(']')
            if cells_array_end > 0:
                # Try to construct valid JSON up to this point
                # Find the opening of cells array
                cells_start = content.find('"cells": [')
                if cells_start > 0:
                    # Extract up to cells array end
                    prefix = content[:cells_start + 10]  # Include '"cells": ['
                    # Find all complete cells
                    cells_content = content[cells_start + 10:cells_array_end]
                    # Try to extract valid cells
                    # This is complex - for now, try simpler approach
                    pass
            
            # Strategy 2: Balance braces
            open_count = content.count('{')
            close_count = content.count('}')
            if open_count > close_count:
                # Add missing closing braces at end (before final })
                last_brace = content.rfind('}')
                if last_brace > 0:
                    missing = open_count - close_count
                    # Insert before last brace
                    content = content[:last_brace] + '}' * missing + content[last_brace:]
            
            # Strategy 3: Remove incomplete last cell
            # Find last complete cell structure
            # Look for pattern: },\n  { (cell separator)
            # Find position where JSON becomes invalid
            # Try parsing incrementally
            for i in range(len(content), 0, -1000):
                try:
                    test_content = content[:i] + '\n  ]\n }\n}'
                    json.loads(test_content)
                    # Found valid point
                    # Reconstruct notebook
                    nb_partial = json.loads(test_content)
                    # Remove incomplete cells
                    if 'cells' in nb_partial:
                        # Keep only complete cells
                        nb_partial['cells'] = [c for c in nb_partial['cells'] if c]
                        with open(notebook_path, 'w') as f:
                            json.dump(nb_partial, f, indent=1, ensure_ascii=False)
                        return True
                except:
                    continue
            
            return False
    
    except Exception as e:
        print(f"Error repairing {notebook_path}: {e}")
        return False

def main():
    """Main function."""
    print("🔧 Attempting to repair corrupted JSON notebooks...\n")

    # Manually repaired: JSON and runtime fixes applied. Skip to avoid overwriting.
    skip_manually_repaired = {
        BASE_DIR / "Course 04/unit2-regression/examples/01_ridge_lasso_regression.ipynb",
        BASE_DIR / "Course 04/unit3-classification/examples/03_svm.ipynb",
    }

    corrupted = [
        BASE_DIR / "Course 04/unit2-regression/examples/01_ridge_lasso_regression.ipynb",
        BASE_DIR / "Course 04/unit3-classification/examples/03_svm.ipynb",
    ]

    for nb_path in corrupted:
        if nb_path in skip_manually_repaired:
            print(f"  ⏭️  Skip (manually repaired): {nb_path.relative_to(BASE_DIR)}")
            continue
        if nb_path.exists():
            if repair_json_notebook(nb_path):
                print(f"  ✓ Repaired: {nb_path.relative_to(BASE_DIR)}")
            else:
                print(f"  ⚠️  Could not repair: {nb_path.relative_to(BASE_DIR)}")
    
    print("\n✅ Repair attempt complete")

if __name__ == "__main__":
    main()
