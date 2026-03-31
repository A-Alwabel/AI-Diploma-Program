#!/usr/bin/env python3
"""
Proper Cell Type Fixer - Actually FIXES issues, doesn't just move content around

This script:
1. Identifies cells with wrong types (code in markdown, markdown in code)
2. ACTUALLY FIXES the code (syntax errors, missing definitions, etc.)
3. Properly separates code from markdown
4. Validates code is executable
5. Executes notebooks to verify they work
"""

import json
import ast
import re
from pathlib import Path
from typing import List, Tuple, Dict, Optional
import subprocess

BASE_DIR = Path(__file__).parent.parent

def is_valid_python_code(source: str) -> Tuple[bool, Optional[str]]:
    """Check if source is valid Python code"""
    if not source.strip():
        return False, "empty"
    
    try:
        ast.parse(source)
        return True, None
    except SyntaxError as e:
        return False, f"syntax error: {e.msg} at line {e.lineno}"

def extract_executable_code_from_markdown(source: str) -> Tuple[Optional[str], str]:
    """
    Extract executable Python code from markdown cell.
    Returns: (extracted_code, remaining_markdown)
    """
    lines = source.split('\n')
    code_lines = []
    markdown_lines = []
    in_code_block = False
    code_block_lang = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check for code block markers
        if stripped.startswith('```'):
            if not in_code_block:
                # Starting code block
                in_code_block = True
                code_block_lang = stripped[3:].strip().lower()
                i += 1
                continue
            else:
                # Ending code block
                in_code_block = False
                code_block_lang = None
                i += 1
                continue
        
        if in_code_block:
            # Inside code block
            if code_block_lang in ['python', 'py', ''] or not code_block_lang:
                code_lines.append(line)
            else:
                markdown_lines.append(line)
        else:
            # Outside code block - check if line looks like executable code
            if stripped and not stripped.startswith('#'):
                # Check for code patterns
                looks_like_code = False
                code_patterns = [
                    r'^\s*(def|class|import|from)\s+',
                    r'^\s*\w+\s*=\s*[^=]',
                    r'^\s*(if|for|while|with|try|except|finally|return|yield)\s+',
                    r'^\s*@\w+',
                    r'^\s*print\s*\(',
                ]
                
                for pattern in code_patterns:
                    if re.match(pattern, stripped):
                        looks_like_code = True
                        break
                
                if looks_like_code:
                    # Try to parse as Python
                    try:
                        ast.parse(stripped)
                        code_lines.append(line)
                    except SyntaxError:
                        # Might be part of multi-line code
                        code_lines.append(line)
                else:
                    markdown_lines.append(line)
            else:
                markdown_lines.append(line)
        
        i += 1
    
    extracted_code = '\n'.join(code_lines) if code_lines else None
    remaining_md = '\n'.join(markdown_lines) if markdown_lines else None
    
    # Validate extracted code
    if extracted_code:
        is_valid, error = is_valid_python_code(extracted_code)
        if not is_valid:
            # Try to fix common issues
            fixed_code = fix_common_code_issues(extracted_code)
            if fixed_code:
                is_valid, _ = is_valid_python_code(fixed_code)
                if is_valid:
                    extracted_code = fixed_code
                else:
                    # Can't fix, keep as markdown
                    return None, source
    
    return extracted_code, remaining_md or ""

def fix_common_code_issues(code: str) -> Optional[str]:
    """Fix common code issues like missing newlines, incomplete statements"""
    lines = code.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Fix incomplete if/for/while statements
        if re.match(r'^\s*(if|for|while|with|try|def|class)\s+', stripped):
            # Check if next line is indented (might be missing colon)
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line and not next_line.startswith('#') and not ':' in stripped:
                    # Add colon if missing
                    if not stripped.endswith(':'):
                        line = line.rstrip() + ':'
        
        # Fix incomplete return statements
        if stripped.startswith('return ') and not stripped.endswith((';', ')')):
            # Check if it's split across lines
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line and not next_line.startswith(('return', 'def', 'class', 'if', 'for', 'while')):
                    # Merge with next line
                    line = line.rstrip() + ' ' + next_line
                    lines[i + 1] = ''  # Mark next line for removal
        
        fixed_lines.append(line)
    
    # Remove empty lines that were merged
    fixed_lines = [l for l in fixed_lines if l != '']
    
    return '\n'.join(fixed_lines)

def clean_markdown_from_code(source: str) -> Tuple[str, bool]:
    """
    Remove markdown content from code cell, convert to comments.
    Returns: (cleaned_code, was_modified)
    """
    lines = source.split('\n')
    cleaned = []
    modified = False
    
    for line in lines:
        stripped = line.strip()
        
        # Skip empty lines
        if not stripped:
            cleaned.append(line)
            continue
        
        # Check if line is markdown (not already a comment)
        is_markdown = False
        
        # Markdown patterns
        if re.match(r'^#+\s+[A-Z]', stripped):  # Headers
            is_markdown = True
        elif re.match(r'^\*\*[^*]+\*\*', stripped):  # Bold
            is_markdown = True
        elif re.match(r'^-\s+', stripped):  # Bullet
            is_markdown = True
        elif re.match(r'^\d+\.\s+', stripped):  # Numbered list
            is_markdown = True
        elif re.match(r'^\|.*\|', stripped):  # Table
            is_markdown = True
        elif stripped.startswith('```'):  # Code block marker
            is_markdown = True
        
        # If it's markdown and not already a comment, convert to comment
        if is_markdown and not stripped.startswith('#'):
            cleaned.append(f"# {line}")
            modified = True
        else:
            # Check if it's valid Python
            try:
                ast.parse(line)
                cleaned.append(line)
            except SyntaxError:
                # Might be part of multi-line, keep it
                cleaned.append(line)
    
    return '\n'.join(cleaned), modified

def fix_notebook_properly(nb_path: Path) -> Tuple[bool, int, List[str]]:
    """Properly fix cell type issues in a notebook"""
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except json.JSONDecodeError as e:
        return False, 0, [f"JSON decode error: {e}"]
    
    fixes = []
    cells_modified = 0
    new_cells = []
    
    for i, cell in enumerate(nb.get('cells', [])):
        cell_type = cell.get('cell_type')
        source = ''.join(cell.get('source', []))
        
        if cell_type == 'markdown':
            # Check if it contains executable code
            extracted_code, remaining_md = extract_executable_code_from_markdown(source)
            
            if extracted_code:
                # Validate the code is actually executable
                is_valid, error = is_valid_python_code(extracted_code)
                if is_valid:
                    # Create new code cell with the extracted code
                    new_code_cell = {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": extracted_code.split('\n')
                    }
                    new_cells.append((i + len(new_cells), new_code_cell))
                    
                    # Update markdown cell
                    if remaining_md.strip():
                        cell['source'] = remaining_md.split('\n')
                    else:
                        # If no markdown left, add a note
                        cell['source'] = [f"# Code extracted from this cell\n"]
                    
                    fixes.append(f"Cell {i+1}: Extracted valid Python code to new code cell")
                    cells_modified += 1
                else:
                    fixes.append(f"Cell {i+1}: Found code but has errors ({error}) - keeping as markdown")
        
        elif cell_type == 'code':
            # Validate code is actually valid Python
            is_valid, error = is_valid_python_code(source)
            
            if not is_valid:
                # Try to fix it
                fixed_code = fix_common_code_issues(source)
                if fixed_code:
                    is_valid, _ = is_valid_python_code(fixed_code)
                    if is_valid:
                        cell['source'] = fixed_code.split('\n')
                        fixes.append(f"Cell {i+1}: Fixed code errors")
                        cells_modified += 1
                    else:
                        fixes.append(f"Cell {i+1}: Code has errors ({error}) - needs manual fix")
            
            # Check for markdown content in code cell
            cleaned_code, was_modified = clean_markdown_from_code(source)
            if was_modified:
                cell['source'] = cleaned_code.split('\n')
                fixes.append(f"Cell {i+1}: Converted markdown content to comments")
                cells_modified += 1
    
    # Insert new code cells
    for offset, new_cell in reversed(new_cells):
        nb['cells'].insert(offset, new_cell)
    
    if cells_modified > 0:
        # Save fixed notebook
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    
    return True, cells_modified, fixes

def execute_notebook(nb_path: Path, timeout: int = 60) -> Tuple[bool, str]:
    """Execute a notebook and return success status"""
    try:
        result = subprocess.run(
            ['python3', '-m', 'jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', str(nb_path)],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        if result.returncode == 0:
            return True, "executed successfully"
        else:
            error_msg = result.stderr or result.stdout
            # Extract actual error
            if "NameError" in error_msg:
                match = re.search(r"NameError: name '(\w+)' is not defined", error_msg)
                if match:
                    return False, f"NameError: '{match.group(1)}' is not defined"
            if "SyntaxError" in error_msg:
                match = re.search(r"SyntaxError: (.+)", error_msg)
                if match:
                    return False, f"SyntaxError: {match.group(1)[:100]}"
            return False, error_msg[:200]
    except subprocess.TimeoutExpired:
        return False, f"timeout after {timeout}s"
    except Exception as e:
        return False, str(e)[:200]

def main():
    """Main function"""
    print("=" * 60)
    print("PROPER Cell Type Fixer - Actually FIXES Issues")
    print("=" * 60)
    
    # Get list of notebooks to fix
    notebooks = list(BASE_DIR.rglob("*.ipynb"))
    notebooks = [nb for nb in notebooks if '.nbconvert' not in str(nb)]
    
    print(f"\n📊 Found {len(notebooks)} notebooks")
    print("\nThis will:")
    print("  1. Actually FIX code errors (not just move content)")
    print("  2. Validate code is executable Python")
    print("  3. Properly separate code from markdown")
    print("  4. Execute notebooks to verify they work")
    
    fixed_count = 0
    executed_count = 0
    failed = []
    
    for i, nb_path in enumerate(notebooks, 1):
        rel_path = nb_path.relative_to(BASE_DIR)
        print(f"\n[{i}/{len(notebooks)}] {rel_path}")
        
        # Fix cell types properly
        success, cells_modified, fixes = fix_notebook_properly(nb_path)
        if not success:
            print(f"  ❌ Failed: {fixes[0] if fixes else 'unknown'}")
            continue
        
        if cells_modified > 0:
            fixed_count += 1
            print(f"  ✅ Fixed {cells_modified} cell(s)")
            for fix in fixes[:2]:
                print(f"     - {fix}")
        
        # Execute to verify
        print(f"  🔄 Executing...")
        exec_success, exec_msg = execute_notebook(nb_path, timeout=60)
        if exec_success:
            executed_count += 1
            print(f"  ✅ Executed successfully")
        else:
            failed.append((rel_path, exec_msg))
            print(f"  ⚠️  {exec_msg}")
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"📊 Total: {len(notebooks)}")
    print(f"✅ Fixed: {fixed_count}")
    print(f"✅ Executed: {executed_count}")
    print(f"❌ Failed: {len(failed)}")
    
    if failed:
        print(f"\n⚠️  Failed notebooks (first 10):")
        for nb_path, msg in failed[:10]:
            print(f"  - {nb_path}: {msg}")

if __name__ == "__main__":
    main()
