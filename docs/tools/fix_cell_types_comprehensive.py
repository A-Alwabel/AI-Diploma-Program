#!/usr/bin/env python3
"""
Comprehensive cell type fixer - fixes both directions:
1. Convert code cells that should be markdown
2. Extract code from markdown cells that should be code
"""

import json
import re
import ast
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).parent.parent

def is_mostly_docstring_or_comments(source: str) -> bool:
    """Check if code cell should be markdown."""
    lines = source.split('\n')
    total_lines = len([l for l in lines if l.strip()])
    
    if total_lines == 0:
        return False
    
    comment_lines = 0
    docstring_lines = 0
    executable_lines = 0
    
    in_docstring = False
    for line in lines:
        stripped = line.strip()
        
        if '"""' in stripped or "'''" in stripped:
            in_docstring = not in_docstring
            docstring_lines += 1
            continue
        
        if in_docstring:
            docstring_lines += 1
            continue
        
        if stripped.startswith('#'):
            comment_lines += 1
            continue
        
        if stripped and not stripped.startswith('#'):
            try:
                ast.parse(stripped)
                executable_lines += 1
            except:
                if any(kw in stripped for kw in ['def ', 'class ', 'import ', 'from ', '=', '(', ')', 'print(', 'return ']):
                    executable_lines += 1
    
    total_non_executable = comment_lines + docstring_lines
    ratio = total_non_executable / total_lines if total_lines > 0 else 0
    
    return ratio > 0.6 and executable_lines < 3

def convert_to_markdown(source: str) -> str:
    """Convert code with docstrings/comments to markdown."""
    lines = source.split('\n')
    new_lines = []
    in_docstring = False
    
    for line in lines:
        stripped = line.strip()
        
        if '"""' in stripped or "'''" in stripped:
            cleaned = re.sub(r'["\']{3}', '', stripped)
            if cleaned.strip():
                new_lines.append(cleaned.strip())
            in_docstring = not in_docstring
            continue
        
        if in_docstring:
            if stripped:
                new_lines.append(stripped)
            continue
        
        if stripped.startswith('#'):
            cleaned = stripped.replace('#', '', 1).strip()
            if cleaned:
                new_lines.append(cleaned)
            continue
        
        if stripped:
            new_lines.append(stripped)
    
    return '\n'.join(new_lines)

def extract_code_blocks_from_markdown(source: str) -> tuple[List[str], str]:
    """Extract executable code blocks from markdown. Returns (extracted_codes, remaining_markdown)."""
    # Find all code blocks
    patterns = [
        (r'```python\n(.*?)```', 'python'),
        (r'```py\n(.*?)```', 'py'),
        (r'```\n(.*?)```', ''),
    ]
    
    all_blocks = []
    for pattern, lang in patterns:
        blocks = re.findall(pattern, source, re.DOTALL)
        for block in blocks:
            all_blocks.append((block.strip(), lang))
    
    extracted = []
    remaining = source
    
    for code, lang in all_blocks:
        if not code:
            continue
        
        # Check if it's executable Python
        try:
            tree = ast.parse(code)
            has_code = any(
                isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Assign, ast.Expr, 
                                ast.Import, ast.ImportFrom, ast.Call, ast.If, ast.For, ast.While))
                for node in ast.walk(tree)
            )
            if has_code:
                # Remove from markdown
                if lang:
                    pattern_to_remove = f'```{lang}\n{re.escape(code)}```'
                else:
                    pattern_to_remove = f'```\n{re.escape(code)}```'
                remaining = re.sub(pattern_to_remove, '', remaining, flags=re.DOTALL)
                extracted.append(code)
        except:
            pass
    
    return extracted, remaining.strip()

def fix_notebook(nb_path: Path) -> tuple[bool, int]:
    """Fix cell types in a notebook. Returns (modified, fixes_count)."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        
        modified = False
        fixes_count = 0
        new_cells = []
        
        for cell in nb.get('cells', []):
            # Fix markdown in code
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))
                if source.strip() and is_mostly_docstring_or_comments(source):
                    cell['cell_type'] = 'markdown'
                    cell['source'] = convert_to_markdown(source).splitlines(keepends=True)
                    modified = True
                    fixes_count += 1
                new_cells.append(cell)
            
            # Extract code from markdown
            elif cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                extracted_codes, remaining = extract_code_blocks_from_markdown(source)
                
                if extracted_codes:
                    # Update markdown cell
                    cell['source'] = remaining.splitlines(keepends=True)
                    new_cells.append(cell)
                    
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
        
        if modified:
            nb['cells'] = new_cells
            with open(nb_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
        
        return modified, fixes_count
    
    except Exception as e:
        return False, 0

def main():
    """Main function."""
    print("🔧 Comprehensive Cell Type Fixer\n")
    
    notebooks = list(BASE_DIR.rglob("*.ipynb"))
    notebooks = [nb for nb in notebooks if 'artifacts' not in str(nb) and '.ipynb_checkpoints' not in str(nb) and 'SOLUTIONS_ALL' not in str(nb)]
    
    # Exclude .nbconvert files (they're duplicates)
    notebooks = [nb for nb in notebooks if '.nbconvert' not in str(nb)]
    
    print(f"✅ Found {len(notebooks)} notebooks (excluding .nbconvert duplicates)\n")
    
    fixed_count = 0
    total_fixes = 0
    
    for i, nb_path in enumerate(notebooks, 1):
        modified, fixes = fix_notebook(nb_path)
        if modified:
            fixed_count += 1
            total_fixes += fixes
            if fixed_count <= 30:
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)} ({fixes} fixes)")
        
        if i % 100 == 0:
            print(f"  Processed {i}/{len(notebooks)} notebooks...")
    
    print(f"\n✅ Fixed {fixed_count} notebooks ({total_fixes} total fixes)")

if __name__ == "__main__":
    main()
