#!/usr/bin/env python3
"""
Extract executable Python code blocks from markdown cells in notebooks.
Only extracts actual code blocks (```python) that are executable.
"""

import json
import re
import ast
from pathlib import Path
from typing import List, Tuple

BASE_DIR = Path(__file__).parent.parent

def extract_code_blocks(source: str) -> List[Tuple[str, int, int]]:
    """
    Extract code blocks from markdown source.
    Returns list of (code, start_pos, end_pos) tuples.
    """
    blocks = []
    
    # Pattern for ```python or ```py or ```
    pattern = r'```(?:python|py)?\n(.*?)```'
    
    for match in re.finditer(pattern, source, re.DOTALL):
        code = match.group(1).strip()
        if code and len(code) > 5:  # Non-empty, substantial
            blocks.append((code, match.start(), match.end()))
    
    return blocks

def is_executable_python(code: str) -> bool:
    """Check if code is valid, executable Python."""
    try:
        tree = ast.parse(code)
        # Check if it has actual executable statements
        has_executable = any(
            isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Assign, ast.Expr,
                             ast.Import, ast.ImportFrom, ast.Call, ast.If, ast.For,
                             ast.While, ast.Return, ast.Raise, ast.Assert))
            for node in ast.walk(tree)
        )
        return has_executable
    except SyntaxError:
        return False

def fix_notebook(nb_path: Path) -> Tuple[bool, int]:
    """Extract code from markdown cells. Returns (modified, fixes_count)."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        
        modified = False
        fixes_count = 0
        new_cells = []
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                blocks = extract_code_blocks(source)
                
                if blocks:
                    # Remove code blocks from markdown
                    remaining = source
                    extracted_codes = []
                    
                    for code, start, end in reversed(blocks):  # Reverse to maintain positions
                        if is_executable_python(code):
                            # Remove this block from markdown
                            remaining = remaining[:start] + remaining[end:]
                            extracted_codes.append(code)
                    
                    if extracted_codes:
                        # Update markdown cell
                        if remaining.strip():
                            cell['source'] = remaining.strip().splitlines(keepends=True)
                            new_cells.append(cell)
                        else:
                            # Markdown cell is now empty, skip it
                            pass
                        
                        # Add new code cells
                        for code in extracted_codes:
                            new_cell = {
                                'cell_type': 'code',
                                'execution_count': None,
                                'metadata': {},
                                'outputs': [],
                                'source': code.splitlines(keepends=True)
                            }
                            new_cells.append(new_cell)
                        
                        modified = True
                        fixes_count += len(extracted_codes)
                    else:
                        new_cells.append(cell)
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
    print("🔧 Extracting Code Blocks from Markdown Cells\n")
    
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
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)} ({fixes} code blocks extracted)")
        
        if i % 100 == 0:
            print(f"  Processed {i}/{len(notebooks)} notebooks...")
    
    print(f"\n✅ Extracted code from {fixed_count} notebooks ({total_fixes} total code blocks)")

if __name__ == "__main__":
    main()
