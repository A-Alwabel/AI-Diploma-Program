#!/usr/bin/env python3
"""
Extract executable code from markdown cells and create new code cells.
Handles code blocks in markdown with dependency checking.
"""

import json
import re
import ast
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def extract_code_from_markdown(notebook_path: Path, min_confidence: float = 0.7) -> bool:
    """Extract code blocks from markdown cells."""
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
        
        modified = False
        new_cells = []
        
        for i, cell in enumerate(nb.get("cells", [])):
            if cell.get("cell_type") != "markdown":
                new_cells.append(cell)
                continue
            
            source = "".join(cell.get("source", []))
            
            # Extract code blocks
            code_blocks = re.findall(r'```(?:python|py)?\n(.*?)```', source, re.DOTALL)
            
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
                
                # Check if it's executable Python
                try:
                    tree = ast.parse(code)
                    # Check if it has actual code (not just comments)
                    has_code = any(
                        isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Assign, ast.Expr, ast.Import, ast.ImportFrom, ast.Call))
                        for node in ast.walk(tree)
                    )
                    
                    if has_code:
                        # High confidence - extract it
                        # Remove from markdown
                        code_block_pattern = re.escape(f'```python\n{code_block}```')
                        remaining_markdown = re.sub(code_block_pattern, '', remaining_markdown, flags=re.DOTALL)
                        # Also try without python tag
                        code_block_pattern2 = re.escape(f'```\n{code_block}```')
                        remaining_markdown = re.sub(code_block_pattern2, '', remaining_markdown, flags=re.DOTALL)
                        
                        # Store code to add as new cell
                        extracted_code.append(code)
                except SyntaxError:
                    # Not valid Python, keep in markdown
                    pass
            
            # Update markdown cell (remove extracted code blocks)
            if extracted_code:
                cell["source"] = remaining_markdown.strip().splitlines(keepends=True)
                new_cells.append(cell)
                
                # Add new code cells for extracted code
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
    print("🔧 Extracting code from markdown cells...\n")
    
    # Read cell type issues
    with open(BASE_DIR / "artifacts" / "cell_type_issues.json") as f:
        issues = json.load(f)
    
    # Get notebooks with code_in_markdown issues (high confidence only)
    notebooks_to_fix = []
    for nb_issue in issues.get("issues", []):
        for issue in nb_issue.get("issues", []):
            if issue.get("issue_type") == "code_in_markdown" and issue.get("confidence", 0) >= 0.7:
                if BASE_DIR / nb_issue["path"] not in notebooks_to_fix:
                    notebooks_to_fix.append(BASE_DIR / nb_issue["path"])
                break
    
    print(f"✅ Found {len(notebooks_to_fix)} notebooks with high-confidence code in markdown\n")
    
    fixed_count = 0
    
    for nb_path in notebooks_to_fix:
        if nb_path.exists() and extract_code_from_markdown(nb_path):
            fixed_count += 1
            if fixed_count <= 20:
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
    
    print(f"\n✅ Fixed {fixed_count}/{len(notebooks_to_fix)} notebooks")

if __name__ == "__main__":
    main()
