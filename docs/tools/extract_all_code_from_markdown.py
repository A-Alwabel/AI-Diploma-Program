#!/usr/bin/env python3
"""
Extract ALL executable code from markdown cells.
More aggressive extraction - handles all code blocks.
"""

import json
import re
import ast
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def extract_code_blocks(source: str):
    """Extract all code blocks from markdown."""
    # Find all code blocks (with or without language tag)
    # Try multiple patterns
    all_blocks = []
    patterns = [
        r'```python\n(.*?)```',
        r'```py\n(.*?)```',
        r'```\n(.*?)```',
    ]
    for pattern in patterns:
        blocks = re.findall(pattern, source, re.DOTALL)
        all_blocks.extend(blocks)
    return all_blocks

def is_executable_code(code: str) -> bool:
    """Check if code is executable Python."""
    code = code.strip()
    if not code:
        return False
    
    try:
        tree = ast.parse(code)
        # Check if it has actual code (not just comments)
        has_code = any(
            isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Assign, ast.Expr, ast.Import, ast.ImportFrom, ast.Call, ast.If, ast.For, ast.While))
            for node in ast.walk(tree)
        )
        return has_code
    except:
        return False

def fix_notebook(notebook_path: Path) -> bool:
    """Extract code from markdown cells."""
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
        
        modified = False
        new_cells = []
        
        for cell in nb.get("cells", []):
            if cell.get("cell_type") != "markdown":
                new_cells.append(cell)
                continue
            
            source = "".join(cell.get("source", []))
            code_blocks = extract_code_blocks(source)
            
            if not code_blocks:
                new_cells.append(cell)
                continue
            
            # Check each code block
            extracted_code = []
            remaining_markdown = source
            
            for code_block in code_blocks:
                code = code_block.strip()
                if not code:
                    continue
                
                if is_executable_code(code):
                    # Remove from markdown - try all patterns
                    patterns_to_remove = [
                        f'```python\n{re.escape(code_block)}```',
                        f'```py\n{re.escape(code_block)}```',
                        f'```\n{re.escape(code_block)}```',
                    ]
                    for pattern in patterns_to_remove:
                        remaining_markdown = re.sub(pattern, '', remaining_markdown, flags=re.DOTALL)
                    
                    extracted_code.append(code)
            
            # Update markdown cell
            if extracted_code:
                cell["source"] = remaining_markdown.strip().splitlines(keepends=True)
                new_cells.append(cell)
                
                # Add new code cells
                for code in extracted_code:
                    new_cell = {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": code.splitlines(keepends=True)
                    }
                    new_cells.append(new_cell)
                modified = True
            else:
                new_cells.append(cell)
        
        if modified:
            nb["cells"] = new_cells
            with open(notebook_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
        
        return False
    
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
        return False

def main():
    """Main function."""
    print("🔧 Extracting ALL code from markdown cells...\n")
    
    # Read cell type issues
    with open(BASE_DIR / "artifacts" / "cell_type_issues.json") as f:
        issues = json.load(f)
    
    # Get ALL notebooks with code_in_markdown issues
    notebooks_to_fix = []
    for nb_issue in issues.get("issues", []):
        for issue in nb_issue.get("issues", []):
            if issue.get("issue_type") == "code_in_markdown":
                if BASE_DIR / nb_issue["path"] not in notebooks_to_fix:
                    notebooks_to_fix.append(BASE_DIR / nb_issue["path"])
                break
    
    print(f"✅ Found {len(notebooks_to_fix)} notebooks with code in markdown\n")
    
    fixed_count = 0
    
    for nb_path in notebooks_to_fix:
        if nb_path.exists() and fix_notebook(nb_path):
            fixed_count += 1
            if fixed_count <= 30:
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
    
    print(f"\n✅ Fixed {fixed_count}/{len(notebooks_to_fix)} notebooks")

if __name__ == "__main__":
    main()
