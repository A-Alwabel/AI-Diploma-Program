#!/usr/bin/env python3
"""
Comprehensive fixer for all remaining issues.
Follows user's pattern: convert code cells with docstrings/comments to markdown.
"""

import json
import re
import ast
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def is_mostly_docstring_or_comments(source: str) -> bool:
    """Check if source is mostly docstrings and comments."""
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
    """Convert code with docstrings/comments to markdown following user's pattern."""
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

def extract_code_from_markdown(source: str):
    """Extract executable code blocks from markdown."""
    patterns = [
        r'```python\n(.*?)```',
        r'```py\n(.*?)```',
        r'```\n(.*?)```',
    ]
    
    all_blocks = []
    for pattern in patterns:
        blocks = re.findall(pattern, source, re.DOTALL)
        all_blocks.extend(blocks)
    
    extracted = []
    for code in all_blocks:
        code = code.strip()
        if not code:
            continue
        
        try:
            tree = ast.parse(code)
            has_code = any(
                isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Assign, ast.Expr, ast.Import, ast.ImportFrom, ast.Call, ast.If, ast.For, ast.While))
                for node in ast.walk(tree)
            )
            if has_code:
                extracted.append(code)
        except:
            pass
    
    return extracted

def fix_notebook(notebook_path: Path) -> tuple[bool, int]:
    """Fix all issues in a notebook. Returns (modified, fixes_count)."""
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
        
        modified = False
        fixes_count = 0
        new_cells = []
        
        for cell in nb.get("cells", []):
            if cell.get("cell_type") == "code":
                source = "".join(cell.get("source", []))
                if source.strip() and is_mostly_docstring_or_comments(source):
                    cell["cell_type"] = "markdown"
                    cell["source"] = convert_to_markdown(source).splitlines(keepends=True)
                    modified = True
                    fixes_count += 1
                new_cells.append(cell)
            
            elif cell.get("cell_type") == "markdown":
                source = "".join(cell.get("source", []))
                code_blocks = extract_code_from_markdown(source)
                
                if code_blocks:
                    remaining = source
                    for code in code_blocks:
                        for pattern in [f'```python\n{re.escape(code)}```', f'```py\n{re.escape(code)}```', f'```\n{re.escape(code)}```']:
                            remaining = re.sub(pattern, '', remaining, flags=re.DOTALL)
                    
                    cell["source"] = remaining.strip().splitlines(keepends=True)
                    new_cells.append(cell)
                    
                    for code in code_blocks:
                        new_cell = {
                            "cell_type": "code",
                            "execution_count": None,
                            "metadata": {},
                            "outputs": [],
                            "source": code.splitlines(keepends=True)
                        }
                        new_cells.append(new_cell)
                    modified = True
                    fixes_count += len(code_blocks)
                else:
                    new_cells.append(cell)
            else:
                new_cells.append(cell)
        
        if modified:
            nb["cells"] = new_cells
            with open(notebook_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
        
        return modified, fixes_count
    
    except Exception as e:
        return False, 0

def main():
    """Main function - fix all notebooks."""
    print("🔧 Fixing ALL remaining issues in all notebooks...\n")
    
    notebooks = list(BASE_DIR.rglob("*.ipynb"))
    notebooks = [nb for nb in notebooks if 'artifacts' not in str(nb) and '.ipynb_checkpoints' not in str(nb) and 'SOLUTIONS_ALL' not in str(nb)]
    
    print(f"✅ Found {len(notebooks)} notebooks\n")
    
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
