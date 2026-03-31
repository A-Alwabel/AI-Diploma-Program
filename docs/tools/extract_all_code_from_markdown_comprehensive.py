#!/usr/bin/env python3
"""
Comprehensive script to extract ALL code from markdown cells.
Handles classes, functions, variable assignments, and mixed code/text.
"""

import json
import ast
import re
from pathlib import Path
from typing import List, Tuple, Optional

BASE_DIR = Path(__file__).parent.parent

def extract_code_from_markdown(source: str) -> Optional[Tuple[str, str]]:
    """
    Extract executable Python code from markdown cell.
    Returns (extracted_code, remaining_markdown) or None.
    """
    lines = source.split('\n')
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
        
        # Check if line starts Python code
        is_code_start = (
            stripped.startswith('class ') or
            stripped.startswith('def ') or
            stripped.startswith('import ') or
            stripped.startswith('from ') or
            stripped.startswith('if __name__') or
            (stripped and not stripped.startswith('#') and not stripped.startswith('-') and 
             not stripped.startswith('*') and '=' in stripped and 
             any(c.isalpha() for c in stripped.split('=')[0].strip()))
        )
        
        if is_code_start:
            # Start collecting code
            code_lines.append(line)
            i += 1
            
            # Continue collecting until we hit non-code
            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()
                
                if not next_stripped:
                    code_lines.append('')
                    i += 1
                    continue
                
                # Still code if:
                # - Indented (continuation)
                # - Has code patterns
                # - Is part of a statement
                still_code = (
                    next_line.startswith(' ') or next_line.startswith('\t') or
                    any(kw in next_stripped for kw in [
                        'return ', 'if ', 'elif ', 'else:', 'for ', 'while ', 'try:',
                        'except', 'finally:', 'with ', '=', '(', ')', '[', ']',
                        '.', ':', 'print(', 'import ', 'from ', 'class ', 'def '
                    ]) or
                    (next_stripped and not next_stripped[0].isupper() and 
                     not next_stripped.startswith('-') and not next_stripped.startswith('*') and
                     not next_stripped.startswith('#') and len(next_stripped) > 2)
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
    
    # Clean up code: convert plain text descriptions to docstrings/comments
    cleaned_lines = []
    for line in code_lines:
        stripped = line.strip()
        
        # If it's a description line (not code, not comment), convert to comment
        if stripped and not stripped.startswith('#') and not any(
            stripped.startswith(kw) for kw in [
                'class ', 'def ', 'import ', 'from ', 'if ', 'for ', 'while ',
                'return ', 'print(', '=', '(', ')', '[', ']', '.', ':', '@'
            ]
        ):
            # Check if it's likely a description
            if not '=' in stripped and not '(' in stripped and not '[' in stripped:
                # Convert to comment
                indent = len(line) - len(line.lstrip())
                cleaned_lines.append(' ' * indent + f"# {stripped}")
            else:
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)
    
    cleaned_code = '\n'.join(cleaned_lines)
    
    # Validate it's executable Python
    try:
        ast.parse(cleaned_code)
        remaining = '\n'.join(markdown_lines).strip()
        return (cleaned_code, remaining)
    except SyntaxError:
        # Try to fix: add pass to empty blocks
        fixed_code = cleaned_code
        for pattern in [r'class \w+:\s*$', r'def \w+\([^)]*\):\s*$']:
            if re.search(pattern, fixed_code, re.MULTILINE):
                fixed_code = re.sub(
                    r'(class \w+:)\s*$', r'\1\n    pass', fixed_code, flags=re.MULTILINE
                )
                fixed_code = re.sub(
                    r'(def \w+\([^)]*\):)\s*$', r'\1\n    pass', fixed_code, flags=re.MULTILINE
                )
        
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
                result = extract_code_from_markdown(source)
                
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
    
    except json.JSONDecodeError:
        return False, 0
    except Exception as e:
        return False, 0

def main():
    """Main function."""
    print("🔧 Comprehensive Code Extraction from Markdown Cells\n")
    
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
            if fixed_count <= 50:
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)} ({fixes} code blocks)")
        
        if i % 100 == 0:
            print(f"  Processed {i}/{len(notebooks)} notebooks...")
    
    print(f"\n✅ Extracted code from {fixed_count} notebooks ({total_fixes} total code blocks)")

if __name__ == "__main__":
    main()
