#!/usr/bin/env python3
"""
Scan notebooks for cell type issues:
- Code in markdown cells (should be in code cells)
- Markdown in code cells (should be in markdown cells)

Includes confidence scores and dependency checking.
"""

import json
import re
import ast
import os
from pathlib import Path
from typing import List, Dict, Any, Tuple

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Exclude directories
EXCLUDE_DIRS = {
    ".git", "__pycache__", ".ipynb_checkpoints",
    "artifacts", "node_modules", ".venv", "venv", "SOLUTIONS_ALL"
}

def find_all_notebooks(base_dir: Path) -> List[Path]:
    """Find all .ipynb files."""
    notebooks = []
    for nb_path in base_dir.rglob("*.ipynb"):
        if any(excluded in nb_path.parts for excluded in EXCLUDE_DIRS):
            continue
        notebooks.append(nb_path)
    return sorted(notebooks)

def check_code_in_markdown(cell_source: str, cell_index: int) -> Tuple[bool, float, str]:
    """
    Check if markdown cell contains executable Python code.
    Returns: (is_issue, confidence, reason)
    """
    # Extract code blocks
    code_blocks = re.findall(r'```(?:python|py)?\n(.*?)```', cell_source, re.DOTALL)
    
    if not code_blocks:
        # Check for inline code that looks executable
        # Look for Python keywords outside code blocks
        python_keywords = ['import ', 'def ', 'class ', 'print(', '=', 'if ', 'for ', 'while ']
        has_keywords = any(keyword in cell_source for keyword in python_keywords)
        
        if has_keywords:
            # Check if it's actual code (not just documentation)
            # High confidence if it has multiple keywords and structure
            keyword_count = sum(1 for kw in python_keywords if kw in cell_source)
            if keyword_count >= 2:
                return (True, 0.7, f"Contains {keyword_count} Python keywords outside code blocks")
            return (True, 0.5, "Contains Python keywords, may be documentation")
        
        return (False, 0.0, "")
    
    # Check code blocks
    for code in code_blocks:
        code = code.strip()
        if not code:
            continue
        
        # Check if it's executable Python
        try:
            ast.parse(code)
            # If it parses, it's executable code
            # Check for actual code (not just examples)
            has_imports = 'import' in code or 'from' in code
            has_functions = 'def ' in code or 'class ' in code
            has_execution = 'print(' in code or '=' in code
            
            if has_imports or has_functions or has_execution:
                confidence = 0.9 if (has_imports or has_functions) else 0.7
                return (True, confidence, "Code block contains executable Python")
        except SyntaxError:
            # Not valid Python, might be pseudocode or incomplete
            pass
    
    return (False, 0.0, "")

def check_markdown_in_code(cell_source: str, cell_index: int) -> Tuple[bool, float, str]:
    """
    Check if code cell should be markdown.
    Returns: (is_issue, confidence, reason)
    """
    if not cell_source.strip():
        return (False, 0.0, "")
    
    lines = cell_source.split('\n')
    total_lines = len([l for l in lines if l.strip()])
    
    if total_lines == 0:
        return (False, 0.0, "")
    
    # Count comment/docstring lines
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
                # Try to parse as Python
                ast.parse(stripped)
                executable_lines += 1
            except:
                pass
    
    comment_ratio = (comment_lines + docstring_lines) / total_lines if total_lines > 0 else 0
    
    # If >70% comments/docstrings, likely should be markdown
    if comment_ratio > 0.7:
        # Check if there's any executable code
        if executable_lines == 0:
            confidence = 0.9
            reason = f"{comment_ratio*100:.0f}% comments/docstrings, no executable code"
        elif executable_lines < 3:
            confidence = 0.7
            reason = f"{comment_ratio*100:.0f}% comments/docstrings, minimal executable code"
        else:
            confidence = 0.5
            reason = f"{comment_ratio*100:.0f}% comments/docstrings, but has executable code"
        
        # Check for markdown formatting
        has_markdown = any(marker in cell_source for marker in ['# ', '## ', '### ', '- ', '* ', '**', '__'])
        if has_markdown:
            confidence = min(confidence + 0.1, 1.0)
            reason += ", contains markdown formatting"
        
        return (True, confidence, reason)
    
    return (False, 0.0, "")

def check_dependencies(cell_source: str, previous_cells: List[str]) -> List[str]:
    """Check if code references variables from previous cells."""
    dependencies = []
    
    # Simple check: look for variable names that might come from previous cells
    # This is a heuristic - not perfect but helpful
    try:
        tree = ast.parse(cell_source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                var_name = node.id
                # Check if this variable is defined in previous cells
                for prev_cell in previous_cells:
                    if f"{var_name} =" in prev_cell or f"def {var_name}" in prev_cell:
                        if var_name not in dependencies:
                            dependencies.append(var_name)
    except:
        pass
    
    return dependencies

def scan_notebook(notebook_path: Path) -> Dict[str, Any]:
    """Scan a single notebook for cell type issues."""
    issues = []
    
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
        
        cells = nb.get("cells", [])
        previous_code = []  # Track code from previous cells for dependency checking
        
        for i, cell in enumerate(cells):
            cell_type = cell.get("cell_type")
            source = "".join(cell.get("source", []))
            
            if cell_type == "markdown":
                # Check for code in markdown
                is_issue, confidence, reason = check_code_in_markdown(source, i)
                if is_issue:
                    dependencies = check_dependencies(source, previous_code)
                    issues.append({
                        "cell_index": i,
                        "cell_type": "markdown",
                        "issue_type": "code_in_markdown",
                        "confidence": confidence,
                        "reason": reason,
                        "dependencies": dependencies,
                        "source_preview": source[:300]
                    })
            
            elif cell_type == "code":
                # Track code for dependency checking
                if source.strip() and not source.strip().startswith("#"):
                    previous_code.append(source)
                
                # Check for markdown in code
                is_issue, confidence, reason = check_markdown_in_code(source, i)
                if is_issue:
                    issues.append({
                        "cell_index": i,
                        "cell_type": "code",
                        "issue_type": "markdown_in_code",
                        "confidence": confidence,
                        "reason": reason,
                        "source_preview": source[:300]
                    })
    
    except Exception as e:
        return {
            "path": str(notebook_path.relative_to(BASE_DIR)),
            "error": str(e),
            "issues": []
        }
    
    return {
        "path": str(notebook_path.relative_to(BASE_DIR)),
        "issues": issues
    }

def main():
    """Main function."""
    print("🔍 Scanning notebooks for cell type issues...\n")
    
    notebooks = find_all_notebooks(BASE_DIR)
    print(f"✅ Found {len(notebooks)} notebooks to scan\n")
    
    all_issues = []
    checked = 0
    
    for nb_path in notebooks:
        checked += 1
        if checked % 100 == 0:
            print(f"  Scanned {checked}/{len(notebooks)} notebooks...")
        
        result = scan_notebook(nb_path)
        if result.get("issues"):
            all_issues.append(result)
    
    print(f"\n✅ Scan complete!")
    print(f"📊 Results:")
    print(f"  - Notebooks checked: {checked}")
    print(f"  - Notebooks with issues: {len(all_issues)}")
    
    # Count issues by type
    code_in_markdown = sum(1 for nb in all_issues for issue in nb.get("issues", []) if issue.get("issue_type") == "code_in_markdown")
    markdown_in_code = sum(1 for nb in all_issues for issue in nb.get("issues", []) if issue.get("issue_type") == "markdown_in_code")
    
    print(f"  - Code in markdown cells: {code_in_markdown}")
    print(f"  - Markdown in code cells: {markdown_in_code}")
    print(f"  - Total issues: {code_in_markdown + markdown_in_code}")
    
    # Save report
    report_path = BASE_DIR / "artifacts" / "cell_type_issues.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_path, "w") as f:
        json.dump({
            "timestamp": str(Path(__file__).stat().st_mtime),
            "total_notebooks": checked,
            "notebooks_with_issues": len(all_issues),
            "code_in_markdown_count": code_in_markdown,
            "markdown_in_code_count": markdown_in_code,
            "issues": all_issues
        }, f, indent=2)
    
    print(f"\n📄 Report saved: {report_path}")
    
    # Print summary
    if all_issues:
        print(f"\n⚠️  Notebooks with cell type issues (first 10):")
        for nb_issue in all_issues[:10]:
            print(f"  - {nb_issue['path']}: {len(nb_issue.get('issues', []))} issue(s)")
            for issue in nb_issue.get("issues", [])[:2]:
                print(f"    Cell {issue['cell_index']} ({issue['cell_type']}): {issue['issue_type']} (confidence: {issue['confidence']:.2f})")
        if len(all_issues) > 10:
            print(f"  ... and {len(all_issues) - 10} more")

if __name__ == "__main__":
    main()
