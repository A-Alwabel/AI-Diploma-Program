#!/usr/bin/env python3
"""
Extract Python code from markdown cells where code is mixed with plain text.
Handles cases like:
- class ClassName: followed by plain text description
- def function(): followed by plain text
- Code with inline comments that aren't proper Python comments
"""

import json
import ast
import re
from pathlib import Path
from typing import List, Tuple, Optional

BASE_DIR = Path(__file__).parent.parent

def extract_code_from_mixed_text(text: str) -> Optional[Tuple[str, str]]:
    """
    Extract executable Python code from text that has code mixed with comments.
    Returns (extracted_code, remaining_markdown) or None.
    """
    lines = text.split('\n')
    code_lines = []
    markdown_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip empty lines initially
        if not stripped:
            if code_lines:
                code_lines.append('')
            else:
                markdown_lines.append(line)
            i += 1
            continue
        
        # Python code indicators
        is_code = (
            stripped.startswith('class ') or
            stripped.startswith('def ') or
            stripped.startswith('import ') or
            stripped.startswith('from ') or
            stripped.startswith('if __name__') or
            (stripped and '=' in stripped and not stripped.startswith('-') and not stripped.startswith('*')) or
            (code_lines and (stripped.startswith(' ') or stripped.startswith('\t')))  # Indented continuation
        )
        
        if is_code:
            # This is code
            code_lines.append(line)
            i += 1
            
            # Continue collecting code until we hit non-code
            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()
                
                if not next_stripped:
                    code_lines.append('')
                    i += 1
                    continue
                
                # Still code if:
                # - Indented (continuation)
                # - Has Python operators/keywords
                # - Assignment
                still_code = (
                    next_stripped.startswith(' ') or next_stripped.startswith('\t') or
                    any(kw in next_stripped for kw in ['return ', 'if ', 'for ', 'while ', '=', '(', ')', '[', ']', '.', ':', 'print(']) or
                    (next_stripped and not next_stripped[0].isupper() and not next_stripped.startswith('-') and not next_stripped.startswith('*'))
                )
                
                if still_code:
                    code_lines.append(next_line)
                    i += 1
                else:
                    break
        else:
            markdown_lines.append(line)
            i += 1
    
    if not code_lines:
        return None
    
    code = '\n'.join(code_lines)
    
    # Clean up code: convert plain text lines to comments
    cleaned_code_lines = []
    for line in code_lines:
        stripped = line.strip()
        # If it's not valid Python syntax and not already a comment, make it a comment
        if stripped and not stripped.startswith('#') and not any(stripped.startswith(kw) for kw in ['class ', 'def ', 'import ', 'from ', 'if ', 'for ', 'while ', 'return ', 'print(']):
            if '=' not in stripped and '(' not in stripped and '[' not in stripped:
                # Likely a plain text comment, convert to Python comment
                cleaned_code_lines.append(f"    # {stripped}")
            else:
                cleaned_code_lines.append(line)
        else:
            cleaned_code_lines.append(line)
    
    cleaned_code = '\n'.join(cleaned_code_lines)
    
    # Validate it's executable Python
    try:
        ast.parse(cleaned_code)
        remaining = '\n'.join(markdown_lines).strip()
        return (cleaned_code, remaining)
    except SyntaxError as e:
        # Try to fix common issues
        # Add pass to empty blocks
        fixed_code = cleaned_code
        for pattern in [r'class \w+:\s*$', r'def \w+\([^)]*\):\s*$']:
            if re.search(pattern, fixed_code, re.MULTILINE):
                # Add pass after class/def with no body
                fixed_code = re.sub(r'(class \w+:)\s*$', r'\1\n    pass', fixed_code, flags=re.MULTILINE)
                fixed_code = re.sub(r'(def \w+\([^)]*\):)\s*$', r'\1\n    pass', fixed_code, flags=re.MULTILINE)
        
        try:
            ast.parse(fixed_code)
            remaining = '\n'.join(markdown_lines).strip()
            return (fixed_code, remaining)
        except:
            return None

def fix_notebook(nb_path: Path) -> Tuple[bool, int]:
    """Extract code from markdown cells."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        
        modified = False
        fixes_count = 0
        new_cells = []
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                
                # Try to extract code
                result = extract_code_from_mixed_text(source)
                
                if result:
                    extracted_code, remaining = result
                    
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
        import traceback
        traceback.print_exc()
        return False, 0

def main():
    """Main function."""
    print("🔧 Extracting Mixed Code from Markdown Cells\n")
    
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
