#!/usr/bin/env python3
"""
Aggressively fix markdown in code cells.
Convert all code cells that are >70% comments/docstrings to markdown.
"""

import json
import ast
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def fix_notebook(notebook_path: Path) -> bool:
    """Fix markdown in code cells."""
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
        
        modified = False
        
        for cell in nb.get("cells", []):
            if cell.get("cell_type") != "code":
                continue
            
            source = "".join(cell.get("source", []))
            if not source.strip():
                continue
            
            lines = source.split('\n')
            total_lines = len([l for l in lines if l.strip()])
            
            if total_lines == 0:
                continue
            
            # Count comments and docstrings
            comment_lines = 0
            docstring_lines = 0
            executable_lines = 0
            
            in_docstring = False
            for line in lines:
                stripped = line.strip()
                
                # Check for docstrings
                if '"""' in stripped or "'''" in stripped:
                    in_docstring = not in_docstring
                    docstring_lines += 1
                    continue
                
                if in_docstring:
                    docstring_lines += 1
                    continue
                
                # Check for comments
                if stripped.startswith('#'):
                    comment_lines += 1
                    continue
                
                # Check for executable code
                if stripped and not stripped.startswith('#'):
                    try:
                        ast.parse(stripped)
                        executable_lines += 1
                    except:
                        pass
            
            comment_ratio = (comment_lines + docstring_lines) / total_lines if total_lines > 0 else 0
            
            # If >70% comments/docstrings, convert to markdown
            if comment_ratio > 0.7 and executable_lines < 3:
                # Convert to markdown
                cell["cell_type"] = "markdown"
                # Clean up source - remove # and docstring markers
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
                    elif line.strip():
                        new_source.append(line)
                cell["source"] = '\n'.join(new_source).splitlines(keepends=True)
                modified = True
        
        if modified:
            with open(notebook_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
        
        return False
    
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
        return False

def main():
    """Main function."""
    print("🔧 Aggressively fixing markdown in code cells...\n")
    
    # Read cell type issues
    with open(BASE_DIR / "artifacts" / "cell_type_issues.json") as f:
        issues = json.load(f)
    
    # Get all notebooks with markdown_in_code issues
    notebooks_to_fix = []
    for nb_issue in issues.get("issues", []):
        for issue in nb_issue.get("issues", []):
            if issue.get("issue_type") == "markdown_in_code":
                if BASE_DIR / nb_issue["path"] not in notebooks_to_fix:
                    notebooks_to_fix.append(BASE_DIR / nb_issue["path"])
                break
    
    print(f"✅ Found {len(notebooks_to_fix)} notebooks with markdown in code\n")
    
    fixed_count = 0
    
    for nb_path in notebooks_to_fix:
        if nb_path.exists() and fix_notebook(nb_path):
            fixed_count += 1
            if fixed_count <= 20:
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
    
    print(f"\n✅ Fixed {fixed_count}/{len(notebooks_to_fix)} notebooks")

if __name__ == "__main__":
    main()
