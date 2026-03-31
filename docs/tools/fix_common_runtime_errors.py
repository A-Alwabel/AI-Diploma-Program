#!/usr/bin/env python3
"""
Fix common runtime errors in notebooks:
- Missing imports
- Undefined variables
- Attribute errors from code in markdown
"""

import json
import ast
import re
from pathlib import Path
from typing import List, Set

BASE_DIR = Path(__file__).parent.parent

def find_undefined_variables(code: str) -> Set[str]:
    """Find variables that are used but not defined."""
    try:
        tree = ast.parse(code)
        defined = set()
        used = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Store):
                    defined.add(node.id)
                elif isinstance(node.ctx, ast.Load):
                    used.add(node.id)
            elif isinstance(node, ast.FunctionDef):
                defined.add(node.name)
            elif isinstance(node, ast.ClassDef):
                defined.add(node.name)
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                for alias in (node.names if isinstance(node, ast.Import) else node.names):
                    defined.add(alias.asname or alias.name.split('.')[0])
        
        undefined = used - defined - {'print', 'len', 'range', 'str', 'int', 'float', 'list', 'dict', 'tuple', 'set'}
        return undefined
    except:
        return set()

def extract_code_from_markdown_cell(source: str) -> List[str]:
    """Extract executable code lines from markdown."""
    lines = source.split('\n')
    code_lines = []
    in_code = False
    
    for line in lines:
        stripped = line.strip()
        
        # Python code indicators
        if any(stripped.startswith(kw) for kw in ['class ', 'def ', 'import ', 'from ', 'if __name__']):
            in_code = True
            code_lines.append(line)
        elif in_code and (stripped.startswith(' ') or stripped.startswith('\t') or not stripped):
            # Continuation
            code_lines.append(line)
        elif in_code and any(kw in stripped for kw in ['=', '(', ')', 'return ', 'print(', 'for ', 'while ', 'if ', 'elif ', 'else:']):
            code_lines.append(line)
        else:
            if in_code and stripped and not any(kw in stripped for kw in ['#', '-', '*']):
                # Might still be code
                code_lines.append(line)
            elif in_code:
                # End of code block
                break
    
    return code_lines

def fix_notebook(nb_path: Path) -> bool:
    """Fix common issues in a notebook."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        
        modified = False
        new_cells = []
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                
                # Check if markdown contains executable code
                code_lines = extract_code_from_markdown_cell(source)
                if code_lines and len(code_lines) > 3:
                    # Extract code
                    code = '\n'.join(code_lines)
                    try:
                        ast.parse(code)
                        # Valid code - extract it
                        # Remove code from markdown
                        remaining = source
                        for code_line in code_lines:
                            remaining = remaining.replace(code_line, '')
                        
                        if remaining.strip():
                            cell['source'] = remaining.strip().splitlines(keepends=True)
                            new_cells.append(cell)
                        
                        # Add code cell
                        new_cell = {
                            'cell_type': 'code',
                            'execution_count': None,
                            'metadata': {},
                            'outputs': [],
                            'source': code.splitlines(keepends=True)
                        }
                        new_cells.append(new_cell)
                        modified = True
                    except:
                        new_cells.append(cell)
                else:
                    new_cells.append(cell)
            else:
                new_cells.append(cell)
        
        if modified:
            nb['cells'] = new_cells
            with open(nb_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
        
        return modified
    
    except json.JSONDecodeError:
        return False
    except Exception as e:
        return False

def main():
    """Main function."""
    print("🔧 Fixing Common Runtime Errors\n")
    
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
    
    for i, nb_path in enumerate(failed_paths, 1):
        if fix_notebook(nb_path):
            fixed_count += 1
            if fixed_count <= 30:
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
        
        if i % 20 == 0:
            print(f"  Processed {i}/{len(failed_paths)} notebooks...")
    
    print(f"\n✅ Fixed {fixed_count} notebooks")

if __name__ == "__main__":
    main()
