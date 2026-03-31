#!/usr/bin/env python3
"""
Fix incomplete import statements in notebooks.
Handles patterns like:
- 'from sklearn.model_selection \n'
- 'import matplotlib.pyplot as \n'
- 'from sklearn.linear_model \n'
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EXCLUDE_DIRS = {".git", "__pycache__", ".ipynb_checkpoints", "artifacts", "node_modules", ".venv", "venv", "SOLUTIONS_ALL"}

# Common import completions
IMPORT_COMPLETIONS = {
    'from sklearn.model_selection': 'from sklearn.model_selection import train_test_split',
    'from sklearn.linear_model': 'from sklearn.linear_model import LinearRegression',
    'from sklearn.metrics': 'from sklearn.metrics import mean_squared_error',
    'from sklearn.cluster': 'from sklearn.cluster import KMeans',
    'from sklearn.datasets': 'from sklearn.datasets import make_classification',
    'import matplotlib.pyplot as': 'import matplotlib.pyplot as plt',
    'import numpy as': 'import numpy as np',
    'from gensim.models': 'from gensim.models import KeyedVectors',
    'from transformers': 'from transformers import AutoModelForCausalLM, AutoTokenizer',
}

def fix_notebook(notebook_path: Path) -> bool:
    """Fix incomplete imports in a notebook."""
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
        
        modified = False
        
        for cell in nb.get("cells", []):
            if cell.get("cell_type") != "code":
                continue
            
            source = cell.get("source", [])
            if not source:
                continue
            
            source_str = "".join(source)
            original_source = source_str
            
            # Fix incomplete imports
            for incomplete, complete in IMPORT_COMPLETIONS.items():
                # Pattern: incomplete + space + newline (end of line)
                pattern1 = incomplete + r' \n'
                if re.search(pattern1, source_str):
                    source_str = re.sub(pattern1, complete + '\n', source_str)
                
                # Pattern: incomplete + newline (no space)
                pattern2 = incomplete + r'\n'
                if re.search(pattern2, source_str) and incomplete + ' ' not in source_str:
                    source_str = re.sub(pattern2, complete + '\n', source_str)
            
            # Fix merged comments: # comment# comment
            source_str = re.sub(r'(#\s*[^\n#]+)#\s*([^\n#])', r'\1\n# \2', source_str)
            
            # Fix: comment# code (comment merged with code)
            source_str = re.sub(r'(#\s*[^\n]+)#([a-zA-Z_])', r'\1\n# \2', source_str)
            
            if source_str != original_source:
                # Split back into lines
                lines = source_str.split('\n')
                cell["source"] = [line + '\n' for line in lines[:-1]] + ([lines[-1] + '\n'] if lines[-1] else [])
                # Remove trailing empty line if exists
                if cell["source"] and cell["source"][-1] == '\n':
                    cell["source"].pop()
                modified = True
        
        if modified:
            with open(notebook_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
        
        return False
    
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
        return False

def main():
    """Main function."""
    print("🔧 Fixing incomplete imports in notebooks...\n")
    
    # Read error report to find notebooks with import issues
    error_report_path = BASE_DIR / "artifacts" / "syntax_errors_scan.json"
    if not error_report_path.exists():
        print(f"❌ Error report not found: {error_report_path}")
        return
    
    with open(error_report_path) as f:
        error_data = json.load(f)
    
    notebooks_to_fix = []
    for err in error_data.get("errors", []):
        nb_path = BASE_DIR / err["path"]
        if nb_path.exists():
            notebooks_to_fix.append(nb_path)
    
    print(f"✅ Found {len(notebooks_to_fix)} notebooks to check\n")
    
    fixed_count = 0
    
    for nb_path in notebooks_to_fix:
        if fix_notebook(nb_path):
            fixed_count += 1
            print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
    
    print(f"\n✅ Fixed {fixed_count}/{len(notebooks_to_fix)} notebooks")

if __name__ == "__main__":
    main()
