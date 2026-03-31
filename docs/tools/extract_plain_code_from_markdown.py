#!/usr/bin/env python3
"""
Extract executable Python code from markdown cells that's written as plain text
(not in ```python blocks). This handles cases where code was accidentally put in markdown.
"""

import json
import ast
import re
from pathlib import Path
from typing import List, Tuple, Optional

BASE_DIR = Path(__file__).parent.parent

def extract_executable_code_from_text(text: str) -> Optional[str]:
    """
    Try to extract executable Python code from plain text in markdown.
    Looks for patterns like:
    - class ClassName:
    - def function_name():
    - import statements
    - variable assignments with code structure
    """
    lines = text.split('\n')
    code_lines = []
    in_code_block = False
    
    for line in lines:
        stripped = line.strip()
        
        # Skip markdown headers, lists, etc.
        if stripped.startswith('#') and not stripped.startswith('# '):
            continue
        if stripped.startswith('- ') or stripped.startswith('* '):
            continue
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        
        # Look for Python code patterns
        if any(stripped.startswith(kw) for kw in ['class ', 'def ', 'import ', 'from ', 'if __name__']):
            code_lines.append(line)
        elif code_lines and (stripped and not stripped.startswith('#') and '=' in stripped):
            # Continuation of code block
            code_lines.append(line)
        elif code_lines and (stripped.startswith(' ') or stripped.startswith('\t')):
            # Indented line (likely part of code)
            code_lines.append(line)
        elif code_lines:
            # End of code block
            break
    
    if not code_lines:
        return None
    
    code = '\n'.join(code_lines)
    
    # Validate it's executable Python
    try:
        ast.parse(code)
        return code
    except SyntaxError:
        # Might be incomplete, try to fix common issues
        # Add pass if needed
        if code.strip().endswith(':'):
            code += '\n    pass'
            try:
                ast.parse(code)
                return code
            except:
                pass
        return None

def fix_notebook(nb_path: Path) -> Tuple[bool, int]:
    """Extract plain code from markdown cells."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        
        modified = False
        fixes_count = 0
        new_cells = []
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                
                # Try to extract executable code
                extracted_code = extract_executable_code_from_text(source)
                
                if extracted_code:
                    # Remove the code from markdown
                    # Simple approach: remove lines that match the code
                    remaining_lines = []
                    code_lines_set = set(extracted_code.split('\n'))
                    
                    for line in source.split('\n'):
                        if line.strip() and line.strip() not in code_lines_set:
                            remaining_lines.append(line)
                        elif not line.strip():
                            remaining_lines.append(line)
                    
                    remaining = '\n'.join(remaining_lines).strip()
                    
                    # Update markdown cell
                    if remaining:
                        cell['source'] = remaining.splitlines(keepends=True)
                        new_cells.append(cell)
                    
                    # Add new code cell
                    new_cell = {
                        'cell_type': 'code',
                        'execution_count': None,
                        'metadata': {},
                        'outputs': [],
                        'source': extracted_code.splitlines(keepends=True)
                    }
                    new_cells.append(new_cell)
                    modified = True
                    fixes_count += 1
                else:
                    new_cells.append(cell)
            else:
                new_cells.append(cell)
        
        if modified:
            nb['cells'] = new_cells
            with open(nb_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
        
        return modified, fixes_count
    
    except Exception as e:
        print(f"  Error in {nb_path}: {e}")
        return False, 0

def main():
    """Main function."""
    print("🔧 Extracting Plain Code from Markdown Cells\n")
    
    notebooks = list(BASE_DIR.rglob("*.ipynb"))
    notebooks = [nb for nb in notebooks 
                 if 'artifacts' not in str(nb) 
                 and '.ipynb_checkpoints' not in str(nb) 
                 and '.nbconvert' not in str(nb)
                 and 'SOLUTIONS_ALL' not in str(nb)]
    
    print(f"✅ Found {len(notebooks)} notebooks\n")
    
    fixed_count = 0
    total_fixes = 0
    
    for i, nb_path in enumerate(notebooks, 1):
        modified, fixes = fix_notebook(nb_path)
        if modified:
            fixed_count += 1
            total_fixes += fixes
            if fixed_count <= 30:
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)} ({fixes} code blocks)")
        
        if i % 100 == 0:
            print(f"  Processed {i}/{len(notebooks)} notebooks...")
    
    print(f"\n✅ Extracted code from {fixed_count} notebooks ({total_fixes} total fixes)")

if __name__ == "__main__":
    main()
