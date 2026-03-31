#!/usr/bin/env python3
"""
Batch fixer for remaining issues - handles multiple patterns at once.
"""

import json
import re
import ast
from pathlib import Path
from typing import List, Tuple, Optional

BASE_DIR = Path(__file__).parent.parent

def fix_missing_newlines_in_source(source_list: list) -> tuple[list, bool]:
    """Fix missing newlines in source list."""
    source_str = ''.join(source_list)
    modified = False
    
    # Pattern: .valuesy = or .valuesx = etc
    if re.search(r'\.values[a-z_]\s*=', source_str):
        source_str = re.sub(r'(\.values)([a-z_]\s*=)', r'\1\n\2', source_str)
        modified = True
    
    # Pattern: ]y = or ]x =
    if re.search(r'\]\s*[a-z_]\s*=', source_str):
        source_str = re.sub(r'(\])\s*([a-z_]\s*=)', r'\1\n\2', source_str)
        modified = True
    
    # Pattern: )y = or )x =
    if re.search(r'\)\s*[a-z_]\s*=', source_str):
        source_str = re.sub(r'(\))\s*([a-z_]\s*=)', r'\1\n\2', source_str)
        modified = True
    
    if modified:
        return source_str.splitlines(keepends=True), True
    return source_list, False

def extract_code_from_markdown(source: str) -> Optional[Tuple[str, str]]:
    """Extract code from markdown cell."""
    lines = source.split('\n')
    code_lines = []
    markdown_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        if not stripped:
            if code_lines:
                code_lines.append('')
            else:
                markdown_lines.append(line)
            i += 1
            continue
        
        # Check if line starts code
        is_code = (
            stripped.startswith('class ') or
            stripped.startswith('def ') or
            (stripped and not stripped.startswith('#') and not stripped.startswith('-') and
             not stripped.startswith('*') and '=' in stripped and
             any(c.isalpha() for c in stripped.split('=')[0].strip()))
        )
        
        if is_code:
            code_lines.append(line)
            i += 1
            
            # Continue collecting
            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()
                
                if not next_stripped:
                    code_lines.append('')
                    i += 1
                    continue
                
                still_code = (
                    next_line.startswith(' ') or next_line.startswith('\t') or
                    any(kw in next_stripped for kw in [
                        'return ', 'if ', 'elif ', 'else:', 'for ', 'while ', '=',
                        '(', ')', '[', ']', '.', ':', 'print(', 'import ', 'from '
                    ]) or
                    (next_stripped and not next_stripped[0].isupper() and
                     not next_stripped.startswith('-') and not next_stripped.startswith('*'))
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
    
    # Clean: convert descriptions to comments
    cleaned = []
    for line in code_lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#') and not any(
            stripped.startswith(kw) for kw in ['class ', 'def ', 'import ', 'from ', 'if ', 'for ', 'while ', 'return ']
        ) and '=' not in stripped and '(' not in stripped and '[' not in stripped:
            indent = len(line) - len(line.lstrip())
            cleaned.append(' ' * indent + f"# {stripped}")
        else:
            cleaned.append(line)
    
    code = '\n'.join(cleaned)
    
    try:
        ast.parse(code)
        remaining = '\n'.join(markdown_lines).strip()
        return (code, remaining)
    except:
        return None

def fix_notebook(nb_path: Path) -> Tuple[bool, int]:
    """Fix all issues in a notebook."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        
        modified = False
        fixes_count = 0
        new_cells = []
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'code':
                # Fix missing newlines
                source_list = cell.get('source', [])
                fixed_list, cell_modified = fix_missing_newlines_in_source(source_list)
                if cell_modified:
                    cell['source'] = fixed_list
                    modified = True
                new_cells.append(cell)
            
            elif cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                result = extract_code_from_markdown(source)
                
                if result:
                    extracted_code, remaining = result
                    
                    if remaining:
                        cell['source'] = remaining.splitlines(keepends=True)
                        new_cells.append(cell)
                    
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
    except Exception:
        return False, 0

def main():
    """Main function."""
    print("🔧 Batch Fixing All Remaining Issues\n")
    
    # Get list of failed notebooks
    with open(BASE_DIR / 'artifacts/notebook_execution_report_v2.json') as f:
        data = json.load(f)
    
    failed_paths = []
    for r in data.get('results', []):
        if r.get('status') != 'passed' and '.nbconvert' not in r.get('path', ''):
            nb_path = BASE_DIR / r.get('path')
            if nb_path.exists():
                failed_paths.append(nb_path)
    
    print(f"✅ Found {len(failed_paths)} failed notebooks\n")
    
    fixed_count = 0
    total_fixes = 0
    
    for i, nb_path in enumerate(failed_paths, 1):
        modified, fixes = fix_notebook(nb_path)
        if modified:
            fixed_count += 1
            total_fixes += fixes
            if fixed_count <= 30:
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)} ({fixes} fixes)")
        
        if i % 20 == 0:
            print(f"  Processed {i}/{len(failed_paths)} notebooks...")
    
    print(f"\n✅ Fixed {fixed_count} notebooks ({total_fixes} total fixes)")

if __name__ == "__main__":
    main()
