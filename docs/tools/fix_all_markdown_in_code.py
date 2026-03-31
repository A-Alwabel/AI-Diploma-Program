#!/usr/bin/env python3
"""
Aggressively fix ALL markdown in code cells.
Convert code cells that are mostly docstrings/comments to markdown.
Based on user's manual fixes pattern.
"""

import json
import ast
import re
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
        
        # Check for executable code (not just whitespace)
        if stripped and not stripped.startswith('#'):
            # Try to parse as Python
            try:
                # Check if it's actual code or just text
                if any(keyword in stripped for keyword in ['def ', 'class ', 'import ', 'from ', '=', '(', ')', 'print(', 'return ', 'if ', 'for ', 'while ']):
                    try:
                        ast.parse(stripped)
                        executable_lines += 1
                    except:
                        # Might be partial code, count as executable
                        executable_lines += 1
            except:
                pass
    
    total_non_executable = comment_lines + docstring_lines
    ratio = total_non_executable / total_lines if total_lines > 0 else 0
    
    # If >60% comments/docstrings and <3 executable lines, convert to markdown
    return ratio > 0.6 and executable_lines < 3

def convert_to_markdown(source: str) -> str:
    """Convert code with docstrings/comments to markdown."""
    lines = source.split('\n')
    new_lines = []
    
    in_docstring = False
    for line in lines:
        stripped = line.strip()
        
        # Handle docstrings
        if '"""' in stripped or "'''" in stripped:
            # Remove docstring markers
            cleaned = re.sub(r'["\']{3}', '', stripped)
            if cleaned.strip():
                new_lines.append(cleaned.strip())
            in_docstring = not in_docstring
            continue
        
        if in_docstring:
            # Keep docstring content
            if stripped:
                new_lines.append(stripped)
            continue
        
        # Handle comments
        if stripped.startswith('#'):
            # Remove # and keep rest
            cleaned = stripped.replace('#', '', 1).strip()
            if cleaned:
                new_lines.append(cleaned)
            continue
        
        # Handle class/def declarations that are just declarations
        if stripped.startswith('class ') or stripped.startswith('def '):
            # Check if it's just a declaration with docstring
            if ':' in stripped and not any(c in stripped for c in ['(', '=', '[']):
                # Might be just a declaration, skip it
                continue
        
        # Keep other lines as-is (might be markdown text)
        if stripped:
            new_lines.append(stripped)
    
    return '\n'.join(new_lines)

def fix_notebook(notebook_path: Path) -> bool:
    """Fix all markdown in code cells."""
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
            
            # Check if it's mostly docstrings/comments
            if is_mostly_docstring_or_comments(source):
                # Convert to markdown
                cell["cell_type"] = "markdown"
                cell["source"] = convert_to_markdown(source).splitlines(keepends=True)
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
    print("🔧 Aggressively fixing ALL markdown in code cells...\n")
    
    # Read cell type issues
    with open(BASE_DIR / "artifacts" / "cell_type_issues.json") as f:
        issues = json.load(f)
    
    # Get ALL notebooks with markdown_in_code issues
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
            if fixed_count <= 30:
                print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
    
    print(f"\n✅ Fixed {fixed_count}/{len(notebooks_to_fix)} notebooks")

if __name__ == "__main__":
    main()
