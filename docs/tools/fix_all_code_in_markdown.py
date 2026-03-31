#!/usr/bin/env python3
"""
Comprehensive fixer for code in markdown cells.
Properly extracts code, fixes indentation, and converts to proper code cells.
"""

import json
import ast
import re
from pathlib import Path
from typing import List, Tuple, Optional

BASE_DIR = Path(__file__).parent.parent

def is_python_keyword_line(line: str) -> bool:
    """Check if line starts with Python keyword."""
    stripped = line.strip()
    return any(stripped.startswith(kw) for kw in [
        'class ', 'def ', 'import ', 'from ', 'if __name__',
        'if ', 'elif ', 'else:', 'for ', 'while ', 'try:',
        'except', 'finally:', 'with ', 'return ', 'yield ',
        'raise ', 'assert ', 'break', 'continue', 'pass'
    ])

def is_code_continuation(line: str, prev_was_code: bool) -> bool:
    """Check if line is continuation of code block."""
    if not line.strip():
        return prev_was_code
    
    stripped = line.strip()
    
    # Indented line (likely code)
    if line.startswith(' ') or line.startswith('\t'):
        return True
    
    # Has code-like patterns
    code_patterns = [
        r'^\s*\w+\s*=',  # variable assignment
        r'^\s*\w+\(',    # function call
        r'^\s*\.\w+',    # method call
        r'^\s*#',        # comment
        r'^\s*""".*"""', # docstring
        r'^\s*print\(',
        r'^\s*return\s',
        r'^\s*if\s',
        r'^\s*for\s',
        r'^\s*while\s',
    ]
    
    return any(re.match(pattern, stripped) for pattern in code_patterns)

def extract_code_blocks_from_markdown(source: str) -> List[Tuple[str, int, int]]:
    """
    Extract code blocks from markdown.
    Returns list of (code, start_line, end_line) tuples.
    """
    lines = source.split('\n')
    blocks = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Skip empty lines
        if not line.strip():
            i += 1
            continue
        
        # Check if this line starts a code block
        if is_python_keyword_line(line):
            # Start collecting code
            code_lines = [line]
            start_idx = i
            i += 1
            
            # Collect continuation lines
            while i < len(lines):
                next_line = lines[i]
                
                if not next_line.strip():
                    code_lines.append('')
                    i += 1
                    continue
                
                # Check if still in code block
                if is_code_continuation(next_line, True):
                    code_lines.append(next_line)
                    i += 1
                else:
                    # Check if next line is also code (new statement)
                    if is_python_keyword_line(next_line):
                        code_lines.append(next_line)
                        i += 1
                        continue
                    else:
                        # End of code block
                        break
            
            code = '\n'.join(code_lines)
            
            # Validate it's executable Python
            try:
                ast.parse(code)
                blocks.append((code, start_idx, i - 1))
            except SyntaxError:
                # Try to fix common issues
                fixed_code = fix_code_structure(code)
                try:
                    ast.parse(fixed_code)
                    blocks.append((fixed_code, start_idx, i - 1))
                except:
                    pass
        
        i += 1
    
    return blocks

def fix_code_structure(code: str) -> str:
    """Fix common code structure issues."""
    lines = code.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Fix class/def without body
        if stripped.endswith(':') and (stripped.startswith('class ') or stripped.startswith('def ')):
            fixed_lines.append(line)
            i += 1
            
            # Check if next line is not indented (missing body)
            if i < len(lines):
                next_line = lines[i]
                if next_line.strip() and not (next_line.startswith(' ') or next_line.startswith('\t')):
                    # Add pass
                    indent = len(line) - len(line.lstrip())
                    fixed_lines.append(' ' * (indent + 4) + 'pass')
                elif not next_line.strip():
                    # Empty line, add pass
                    indent = len(line) - len(line.lstrip())
                    fixed_lines.append('')
                    fixed_lines.append(' ' * (indent + 4) + 'pass')
                    i += 1
        else:
            fixed_lines.append(line)
            i += 1
    
    return '\n'.join(fixed_lines)

def clean_markdown_text(text: str, code_lines: List[str]) -> str:
    """Remove code lines from markdown, keeping only explanatory text."""
    code_set = set(line.strip() for line in code_lines if line.strip())
    result_lines = []
    
    for line in text.split('\n'):
        stripped = line.strip()
        
        # Keep if:
        # - Empty line
        # - Markdown header/list
        # - Not in code set
        if not stripped:
            result_lines.append(line)
        elif stripped.startswith('#') and not stripped.startswith('# '):
            # Markdown header
            result_lines.append(line)
        elif stripped.startswith('- ') or stripped.startswith('* '):
            # List item
            result_lines.append(line)
        elif stripped not in code_set and not is_python_keyword_line(line):
            # Not code, keep it
            result_lines.append(line)
        # Otherwise, it's code, skip it
    
    return '\n'.join(result_lines).strip()

def fix_notebook(nb_path: Path) -> Tuple[bool, int]:
    """Fix code in markdown cells."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        
        modified = False
        fixes_count = 0
        new_cells = []
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                
                # Extract code blocks
                code_blocks = extract_code_blocks_from_markdown(source)
                
                if code_blocks:
                    # Get all code lines for cleaning markdown
                    all_code_lines = []
                    for code, _, _ in code_blocks:
                        all_code_lines.extend(code.split('\n'))
                    
                    # Clean markdown
                    remaining = clean_markdown_text(source, all_code_lines)
                    
                    # Update markdown cell
                    if remaining:
                        cell['source'] = remaining.splitlines(keepends=True)
                        new_cells.append(cell)
                    
                    # Add code cells
                    for code, _, _ in code_blocks:
                        new_cell = {
                            'cell_type': 'code',
                            'execution_count': None,
                            'metadata': {},
                            'outputs': [],
                            'source': code.splitlines(keepends=True)
                        }
                        new_cells.append(new_cell)
                        fixes_count += 1
                    
                    modified = True
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
        # Skip corrupted JSON files
        return False, 0
    except Exception as e:
        print(f"  Error in {nb_path}: {e}")
        return False, 0

def main():
    """Main function."""
    print("🔧 Fixing All Code in Markdown Cells\n")
    
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
    
    print(f"\n✅ Fixed {fixed_count} notebooks ({total_fixes} total code blocks extracted)")

if __name__ == "__main__":
    main()
