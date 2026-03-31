#!/usr/bin/env python3
"""Fix duplicate lines in a specific notebook"""

import json
from pathlib import Path

def fix_duplicates_in_cell(source: list) -> tuple:
    """Remove consecutive duplicate lines"""
    if not source:
        return source, False
    
    fixed = []
    modified = False
    prev_line = None
    
    for line in source:
        stripped = line.strip()
        # Skip if it's the same as previous line (and not empty/whitespace-only)
        if stripped and stripped == prev_line:
            modified = True
            continue
        fixed.append(line)
        prev_line = stripped
    
    return fixed, modified

def fix_notebook(nb_path: Path):
    """Fix duplicates in notebook"""
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    total_fixes = 0
    
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if isinstance(source, str):
                source = source.splitlines(keepends=True)
            
            fixed, modified = fix_duplicates_in_cell(source)
            if modified:
                total_fixes += 1
                cell['source'] = fixed
    
    # Fix broken predictions line
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if isinstance(source, str):
                source = source.splitlines(keepends=True)
            
            # Fix "# Test predictions_predictions = nn.forward(X_xor)"
            new_source = []
            for line in source:
                if '# Test predictions_predictions = nn.forward(X_xor)' in line:
                    new_source.append('# Test predictions\n')
                    new_source.append('predictions = nn.forward(X_xor)\n')
                else:
                    new_source.append(line)
            
            if new_source != source:
                cell['source'] = new_source
                total_fixes += 1
    
    if total_fixes > 0:
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        print(f"  ✓ Fixed {nb_path.name}: {total_fixes} fixes")
        return True
    return False

if __name__ == '__main__':
    nb_path = Path(__file__).parent.parent / "Course 03/unit2-calculus/examples/04_backpropagation_neural_networks.ipynb"
    fix_notebook(nb_path)
