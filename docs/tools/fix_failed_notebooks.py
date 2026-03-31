#!/usr/bin/env python3
"""
Fix failed notebooks from execution results.
"""

import json
import nbformat
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent
PROGRESS_FILE = BASE_DIR / "artifacts" / "execution_progress.json"

def fix_notebook(nb_path):
    """Fix common issues in a notebook."""
    try:
        nb = nbformat.read(nb_path, as_version=4)
        modified = False
        
        for cell in nb.cells:
            if cell.cell_type != 'code':
                continue
            
            original = cell.source
            fixed = original
            
            # Fix common patterns
            # 1. OneHotEncoder deprecation
            fixed = fixed.replace('OneHotEncoder(sparse=False)', 'OneHotEncoder(sparse_output=False)')
            
            # 2. Broken division patterns
            fixed = re.sub(r'(\w+)\s*=\s*\([^)]+\)\s*\n\s*(\w+)\s*\n', r'\1 = \1 / \2\n', fixed)
            
            # 3. Broken serialize calls
            fixed = re.sub(
                r"g\.serialize\(format='xml'\)\s+if\s+isinstance\([^)]+\)\s+else\s+[^)]+\)",
                "xml_output = g.serialize(format='xml')\nif isinstance(xml_output, bytes):\n    xml_output = xml_output.decode('utf-8')\nprint(xml_output)",
                fixed
            )
            
            # 4. Fix missing pandas import if df is used
            if ('df =' in fixed or 'df[' in fixed or 'pd.DataFrame' in fixed) and 'import pandas' not in fixed and 'import pd' not in fixed:
                lines = fixed.split('\n')
                import_added = False
                for i, line in enumerate(lines):
                    if line.strip().startswith('import ') or line.strip().startswith('from '):
                        if 'numpy' in line.lower() or 'np' in line:
                            lines.insert(i + 1, 'import pandas as pd')
                            import_added = True
                            break
                if not import_added:
                    lines.insert(0, 'import pandas as pd')
                fixed = '\n'.join(lines)
            
            # 5. Fix missing numpy import if np is used
            if ('np.' in fixed or 'numpy' in fixed) and 'import numpy' not in fixed and 'import np' not in fixed:
                lines = fixed.split('\n')
                import_added = False
                for i, line in enumerate(lines):
                    if line.strip().startswith('import ') or line.strip().startswith('from '):
                        lines.insert(i + 1, 'import numpy as np')
                        import_added = True
                        break
                if not import_added:
                    lines.insert(0, 'import numpy as np')
                fixed = '\n'.join(lines)
            
            if fixed != original:
                cell.source = fixed
                modified = True
        
        if modified:
            nbformat.write(nb, nb_path)
            return True
        return False
    except Exception as e:
        print(f"Error fixing {nb_path}: {e}")
        return False

def main():
    """Fix failed notebooks."""
    if not PROGRESS_FILE.exists():
        print("No progress file found")
        return
    
    with open(PROGRESS_FILE, 'r') as f:
        progress = json.load(f)
    
    results = progress.get("results", {})
    failed = [path for path, r in results.items() if r.get("status") == "error"]
    
    print(f"Found {len(failed)} failed notebooks")
    print("Fixing common issues...\n")
    
    fixed_count = 0
    for i, path in enumerate(failed[:50], 1):  # Fix first 50
        nb_path = BASE_DIR / path
        if nb_path.exists():
            if fix_notebook(nb_path):
                fixed_count += 1
                print(f"[{i}/{min(50, len(failed))}] Fixed: {path}")
    
    print(f"\nFixed {fixed_count} notebooks")

if __name__ == "__main__":
    main()
