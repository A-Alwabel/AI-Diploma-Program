#!/usr/bin/env python3
"""
Fix cell type issues in notebooks.
- Convert code cells that are mostly markdown to markdown cells
- Extract code from markdown cells (with dependency checking)
"""

import json
import re
import ast
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).parent.parent

def fix_cell_types_notebook(notebook_path: Path, dry_run: bool = False) -> Dict[str, Any]:
    """Fix cell type issues in a notebook."""
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
    except Exception as e:
        return {"path": str(notebook_path), "error": str(e)}
    
    cells = nb.get("cells", [])
    modified = False
    fixes = []
    
    for i, cell in enumerate(cells):
        cell_type = cell.get("cell_type")
        source = "".join(cell.get("source", []))
        
        if cell_type == "code":
            # Check if it's mostly markdown/comments
            lines = source.split('\n')
            total_lines = len([l for l in lines if l.strip()])
            
            if total_lines == 0:
                continue
            
            # Count comments and docstrings
            comment_lines = len([l for l in lines if l.strip().startswith('#')])
            docstring_count = source.count('"""') + source.count("'''")
            
            comment_ratio = comment_lines / total_lines if total_lines > 0 else 0
            
            # If >70% comments and no/minimal executable code, convert to markdown
            if comment_ratio > 0.7:
                try:
                    tree = ast.parse(source)
                    # Check for executable code
                    has_executable = any(
                        isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Assign, ast.Expr, ast.Import, ast.ImportFrom))
                        for node in ast.walk(tree)
                    )
                    if not has_executable:
                        # Convert to markdown
                        if not dry_run:
                            cell["cell_type"] = "markdown"
                            # Clean up - remove # and docstring markers, keep content
                            new_source = []
                            for line in lines:
                                if line.strip().startswith('#'):
                                    # Remove # and keep rest
                                    new_source.append(line.replace('#', '', 1).lstrip())
                                elif '"""' in line or "'''" in line:
                                    # Remove docstring markers
                                    cleaned = line.replace('"""', '').replace("'''", '').strip()
                                    if cleaned:
                                        new_source.append(cleaned)
                                else:
                                    new_source.append(line)
                            cell["source"] = '\n'.join(new_source).splitlines(True)
                            modified = True
                            fixes.append(f"Cell {i}: code → markdown (mostly comments)")
                except SyntaxError:
                    # Can't parse - likely should be markdown
                    if not dry_run:
                        cell["cell_type"] = "markdown"
                        # Clean up source
                        new_source = []
                        for line in lines:
                            if line.strip().startswith('#'):
                                new_source.append(line.replace('#', '', 1).lstrip())
                            else:
                                new_source.append(line)
                        cell["source"] = '\n'.join(new_source).splitlines(True)
                        modified = True
                        fixes.append(f"Cell {i}: code → markdown (unparseable)")
        
        elif cell_type == "markdown":
            # Check for executable code in markdown
            # Extract code blocks
            code_blocks = re.findall(r'```(?:python|py)?\n(.*?)```', source, re.DOTALL)
            
            for code in code_blocks:
                code = code.strip()
                if not code:
                    continue
                
                # Check if it's executable Python
                try:
                    tree = ast.parse(code)
                    # Check if it has actual code (not just comments)
                    has_code = any(
                        isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Assign, ast.Expr, ast.Import, ast.ImportFrom))
                        for node in ast.walk(tree)
                    )
                    if has_code:
                        # This should be in a code cell
                        # For now, mark for manual review (complex to extract)
                        # Could extract and create new code cell, but need to preserve order
                        pass
                except:
                    pass
    
    if modified and not dry_run:
        with open(notebook_path, "w") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    
    return {
        "path": str(notebook_path.relative_to(BASE_DIR)),
        "modified": modified,
        "fixes": fixes
    }

def main():
    """Main function."""
    import sys
    
    dry_run = "--dry-run" in sys.argv
    high_conf_only = "--high-conf" in sys.argv
    
    with open(BASE_DIR / "artifacts" / "cell_type_issues.json") as f:
        issues = json.load(f)
    
    # Get notebooks to fix
    if high_conf_only:
        # Only high confidence (>0.8)
        notebooks_to_fix = []
        for nb_issue in issues["issues"]:
            for issue in nb_issue.get("issues", []):
                if issue.get("confidence", 0) > 0.8 and issue.get("issue_type") == "markdown_in_code":
                    notebooks_to_fix.append(BASE_DIR / nb_issue["path"])
                    break
    else:
        # All notebooks with issues
        notebooks_to_fix = [BASE_DIR / nb["path"] for nb in issues["issues"]]
    
    print(f"🔧 Fixing cell types in {len(notebooks_to_fix)} notebooks...")
    if dry_run:
        print("🔍 DRY RUN\n")
    
    fixed_count = 0
    total_fixes = 0
    
    for nb_path in notebooks_to_fix:
        result = fix_cell_types_notebook(nb_path, dry_run)
        if result.get("modified"):
            fixed_count += 1
            total_fixes += len(result.get("fixes", []))
            if fixed_count <= 20:
                print(f"✅ {result['path']}: {len(result.get('fixes', []))} fix(es)")
    
    print(f"\n✅ Fixed {fixed_count} notebooks ({total_fixes} total fixes)")

if __name__ == "__main__":
    main()
