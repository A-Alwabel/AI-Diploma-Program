#!/usr/bin/env python3
"""Fix indentation issues in a notebook"""
import json
import re
from pathlib import Path

def fix_indentation_in_cell(source_lines):
    """Fix indentation in a code cell"""
    fixed = []
    indent_level = 0
    prev_line_ended_with_colon = False
    
    for i, line in enumerate(source_lines):
        stripped = line.lstrip()
        
        # Skip empty lines and comments
        if not stripped or stripped.startswith('#'):
            fixed.append(line)
            continue
        
        # Check if previous line ended with colon (needs indentation)
        if prev_line_ended_with_colon:
            # Next line should be indented
            if not line.startswith(' ') and not line.startswith('\t'):
                line = '    ' + line
        
        # Check for dedent keywords
        if stripped.startswith(('else:', 'elif ', 'except ', 'finally:')):
            indent_level = max(0, indent_level - 1)
        
        # Check for indent keywords
        if stripped.endswith(':'):
            prev_line_ended_with_colon = True
        else:
            prev_line_ended_with_colon = False
        
        # Apply consistent indentation
        if stripped.startswith(('if ', 'for ', 'while ', 'with ', 'try:', 'def ', 'class ')):
            if not line.startswith(' '):
                line = '    ' * indent_level + stripped
            indent_level += 1
        elif stripped.startswith(('else:', 'elif ', 'except ', 'finally:')):
            line = '    ' * indent_level + stripped
        else:
            # Regular line - maintain current indent
            if not line.startswith(' ') and not line.startswith('\t'):
                line = '    ' * indent_level + stripped
            else:
                # Preserve existing indentation if reasonable
                current_indent = len(line) - len(line.lstrip())
                if current_indent < indent_level * 4:
                    line = '    ' * indent_level + stripped
        
        fixed.append(line)
    
    return fixed

def fix_notebook(nb_path):
    """Fix indentation in all code cells"""
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    modified = False
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if isinstance(source, list):
                source_lines = source
            else:
                source_lines = source.split('\n')
            
            fixed_lines = fix_indentation_in_cell(source_lines)
            if fixed_lines != source_lines:
                cell['source'] = fixed_lines
                modified = True
    
    if modified:
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"✅ Fixed indentation in {nb_path}")
    else:
        print(f"ℹ️  No indentation issues found in {nb_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        fix_notebook(Path(sys.argv[1]))
    else:
        print("Usage: python fix_indentation_in_notebook.py <notebook_path>")
