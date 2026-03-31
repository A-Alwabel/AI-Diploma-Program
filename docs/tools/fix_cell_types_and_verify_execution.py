#!/usr/bin/env python3
"""
Comprehensive Cell Type Fixer and Execution Verifier

This script:
1. Scans all notebooks for cell type issues (code in markdown, markdown in code)
2. Fixes cell types systematically
3. Executes notebooks to verify they work
4. Makes notebooks clean and human-readable
"""

import json
import ast
import re
from pathlib import Path
from typing import List, Tuple, Dict, Optional
import subprocess
import sys

BASE_DIR = Path(__file__).parent.parent
NOTEBOOKS_DIR = BASE_DIR

# Patterns to identify executable code in markdown
CODE_PATTERNS = [
    (r'^def\s+\w+\s*\(', 'function definition'),
    (r'^class\s+\w+', 'class definition'),
    (r'^import\s+\w+', 'import statement'),
    (r'^from\s+\w+\s+import', 'from import'),
    (r'^\s*\w+\s*=\s*[^=]', 'variable assignment'),
    (r'^\s*print\s*\(', 'print statement'),
    (r'^\s*if\s+__name__', 'if __name__ guard'),
    (r'^\s*for\s+\w+\s+in', 'for loop'),
    (r'^\s*while\s+', 'while loop'),
    (r'^\s*return\s+', 'return statement'),
    (r'^\s*@\w+', 'decorator'),
]

# Patterns to identify markdown in code cells
MARKDOWN_PATTERNS = [
    (r'^#\s+[A-Z]', 'markdown header'),
    (r'^\*\*[^*]+\*\*', 'bold text'),
    (r'^-\s+', 'bullet point'),
    (r'^\d+\.\s+', 'numbered list'),
    (r'^```', 'code block marker'),
    (r'^\|.*\|', 'table row'),
]

def is_executable_code(source: str) -> Tuple[bool, float, str]:
    """Check if source contains executable Python code"""
    if not source.strip():
        return False, 0.0, "empty"
    
    lines = source.split('\n')
    code_lines = 0
    total_lines = len([l for l in lines if l.strip()])
    
    if total_lines == 0:
        return False, 0.0, "empty"
    
    # Check for code patterns
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        
        for pattern, desc in CODE_PATTERNS:
            if re.match(pattern, stripped):
                code_lines += 1
                break
    
    # Try to parse as Python
    try:
        ast.parse(source)
        return True, 1.0, "valid python"
    except SyntaxError:
        pass
    
    # If significant portion looks like code
    code_ratio = code_lines / total_lines if total_lines > 0 else 0
    if code_ratio > 0.5:
        return True, code_ratio, f"{code_lines}/{total_lines} lines look like code"
    
    return False, code_ratio, "mostly markdown"

def is_markdown_content(source: str) -> Tuple[bool, float, str]:
    """Check if source contains markdown content"""
    if not source.strip():
        return False, 0.0, "empty"
    
    lines = source.split('\n')
    markdown_lines = 0
    total_lines = len([l for l in lines if l.strip()])
    
    if total_lines == 0:
        return False, 0.0, "empty"
    
    # Check for markdown patterns
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        for pattern, desc in MARKDOWN_PATTERNS:
            if re.match(pattern, stripped):
                markdown_lines += 1
                break
    
    # If significant portion looks like markdown
    markdown_ratio = markdown_lines / total_lines if total_lines > 0 else 0
    if markdown_ratio > 0.3 and total_lines > 2:
        return True, markdown_ratio, f"{markdown_lines}/{total_lines} lines look like markdown"
    
    return False, markdown_ratio, "mostly code"

def extract_code_from_markdown(source: str) -> Optional[str]:
    """Extract executable code from markdown cell"""
    lines = source.split('\n')
    code_lines = []
    in_code_block = False
    
    for line in lines:
        # Check for code block markers
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        
        if in_code_block:
            code_lines.append(line)
        else:
            # Check if line looks like code
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            
            for pattern, _ in CODE_PATTERNS:
                if re.match(pattern, stripped):
                    code_lines.append(line)
                    break
    
    if code_lines:
        code = '\n'.join(code_lines)
        try:
            ast.parse(code)
            return code
        except SyntaxError:
            pass
    
    return None

def clean_code_cell(source: str) -> str:
    """Remove markdown content from code cell, convert to comments"""
    lines = source.split('\n')
    cleaned = []
    
    for line in lines:
        stripped = line.strip()
        
        # Check if line is markdown
        is_md = False
        for pattern, _ in MARKDOWN_PATTERNS:
            if re.match(pattern, stripped):
                is_md = True
                break
        
        if is_md and not stripped.startswith('#'):
            # Convert to comment
            cleaned.append(f"# {line}")
        else:
            cleaned.append(line)
    
    return '\n'.join(cleaned)

def fix_notebook_cell_types(nb_path: Path) -> Tuple[bool, int, List[str]]:
    """Fix cell type issues in a notebook"""
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except json.JSONDecodeError as e:
        return False, 0, [f"JSON decode error: {e}"]
    
    fixes = []
    cells_modified = 0
    
    for i, cell in enumerate(nb.get('cells', [])):
        cell_type = cell.get('cell_type')
        source = ''.join(cell.get('source', []))
        
        if cell_type == 'markdown':
            # Check if it contains executable code
            is_code, confidence, reason = is_executable_code(source)
            if is_code and confidence > 0.7:
                # Extract code
                extracted_code = extract_code_from_markdown(source)
                if extracted_code:
                    # Create new code cell
                    new_code_cell = {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": extracted_code.split('\n')
                    }
                    # Update markdown cell to remove code
                    remaining_md = source.replace(extracted_code, '').strip()
                    if remaining_md:
                        cell['source'] = remaining_md.split('\n')
                    else:
                        # If no markdown left, replace with a note
                        cell['source'] = [f"# Code extracted from markdown (cell {i+1})\n"]
                    
                    # Insert code cell after markdown
                    nb['cells'].insert(i + 1, new_code_cell)
                    fixes.append(f"Cell {i+1}: Extracted code from markdown ({reason})")
                    cells_modified += 1
        
        elif cell_type == 'code':
            # Check if it contains markdown
            is_md, confidence, reason = is_markdown_in_code(source)
            if is_md and confidence > 0.3:
                # Clean code cell
                cleaned = clean_code_cell(source)
                if cleaned != source:
                    cell['source'] = cleaned.split('\n')
                    fixes.append(f"Cell {i+1}: Cleaned markdown from code ({reason})")
                    cells_modified += 1
    
    if cells_modified > 0:
        # Save fixed notebook
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    
    return True, cells_modified, fixes

def is_markdown_in_code(source: str) -> Tuple[bool, float, str]:
    """Check if code cell contains markdown content"""
    return is_markdown_content(source)

def execute_notebook(nb_path: Path, timeout: int = 60) -> Tuple[bool, str]:
    """Execute a notebook and return success status"""
    try:
        result = subprocess.run(
            ['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', str(nb_path)],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        if result.returncode == 0:
            return True, "executed successfully"
        else:
            error_msg = result.stderr or result.stdout
            return False, error_msg[:500]  # Limit error message length
    except subprocess.TimeoutExpired:
        return False, f"timeout after {timeout}s"
    except Exception as e:
        return False, str(e)[:500]

def main():
    """Main function to fix cell types and verify execution"""
    print("=" * 60)
    print("Cell Type Fixer and Execution Verifier")
    print("=" * 60)
    
    # Find all notebooks
    notebooks = list(NOTEBOOKS_DIR.rglob("*.ipynb"))
    notebooks = [nb for nb in notebooks if '.nbconvert' not in str(nb)]
    
    print(f"\n📊 Found {len(notebooks)} notebooks")
    
    fixed_count = 0
    executed_count = 0
    failed_executions = []
    
    for i, nb_path in enumerate(notebooks, 1):
        print(f"\n[{i}/{len(notebooks)}] Processing: {nb_path.relative_to(BASE_DIR)}")
        
        # Fix cell types
        success, cells_modified, fixes = fix_notebook_cell_types(nb_path)
        if not success:
            print(f"  ❌ Failed to process: {fixes[0] if fixes else 'unknown error'}")
            continue
        
        if cells_modified > 0:
            fixed_count += 1
            print(f"  ✅ Fixed {cells_modified} cell(s):")
            for fix in fixes[:3]:  # Show first 3 fixes
                print(f"     - {fix}")
            if len(fixes) > 3:
                print(f"     ... and {len(fixes) - 3} more")
        
        # Execute notebook
        print(f"  🔄 Executing notebook...")
        exec_success, exec_msg = execute_notebook(nb_path, timeout=60)
        if exec_success:
            executed_count += 1
            print(f"  ✅ Executed successfully")
        else:
            failed_executions.append((nb_path, exec_msg))
            print(f"  ⚠️  Execution failed: {exec_msg[:100]}")
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"📊 Total notebooks: {len(notebooks)}")
    print(f"✅ Fixed cell types: {fixed_count}")
    print(f"✅ Executed successfully: {executed_count}")
    print(f"❌ Failed executions: {len(failed_executions)}")
    
    if failed_executions:
        print("\n⚠️  Failed Executions:")
        for nb_path, msg in failed_executions[:10]:
            print(f"  - {nb_path.relative_to(BASE_DIR)}: {msg[:80]}")

if __name__ == "__main__":
    main()
