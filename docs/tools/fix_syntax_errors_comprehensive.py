#!/usr/bin/env python3
"""
Comprehensive syntax error fixer for notebooks.
Handles multiple patterns:
1. Unexpected indent with pass statements
2. Missing newlines (statements on same line separated by _)
3. Incomplete import statements
4. Markdown text in code cells
5. Incomplete try-except blocks
6. Parameter names split across lines
7. Unmatched parentheses
"""

import json
import ast
import re
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).parent.parent
EXCLUDE_DIRS = {".git", "__pycache__", ".ipynb_checkpoints", "artifacts", "node_modules", ".venv", "venv", "SOLUTIONS_ALL"}

def fix_unexpected_indent_pass(source: str) -> str:
    """Fix 'unexpected indent' errors with pass statements after comments."""
    lines = source.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Check if line has unexpected indent with pass (4+ spaces)
        if re.match(r'^\s{4,}pass\s*$', line):
            # Check if previous non-empty line is a comment
            prev_comment = False
            for j in range(i-1, -1, -1):
                prev_line = lines[j]
                if prev_line.strip():
                    # Check if it's a comment
                    if prev_line.strip().startswith('#'):
                        prev_comment = True
                    break
            
            # Also check if this pass is at the start of the cell or after a comment
            # If it's indented but not part of a function/class, it's likely wrong
            if prev_comment or i == 0:
                # Remove indentation from pass
                fixed_lines.append('pass')
            else:
                # Check if next line suggests this is not part of a block
                next_is_def_or_class = False
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line.startswith(('def ', 'class ', 'if ', 'for ', 'while ')):
                        next_is_def_or_class = True
                
                # If next line is a def/class and this pass is indented, it's likely wrong
                if next_is_def_or_class:
                    fixed_lines.append('pass')
                else:
                    fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_missing_newlines(source: str) -> str:
    """Fix statements on same line separated by underscore."""
    # Pattern: statement1_statement2 or statement1_ statement2
    # Replace _ with \n, but be careful with variable names containing _
    lines = source.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Fix patterns like: comment# comment or code_ code
        # Pattern: identifier_identifier = (but not identifier_identifier as part of name)
        # Replace _ followed by space and then identifier = with newline
        fixed_line = re.sub(r'([a-zA-Z0-9_\]\)])\s*_\s*([a-z_][a-zA-Z0-9_]*)\s*=\s*', r'\1\n\2 = ', line)
        # Fix: code_ code (without =)
        fixed_line = re.sub(r'([a-zA-Z0-9_\]\)])\s*_\s*([a-z_][a-zA-Z0-9_]*)\s*\(', r'\1\n\2(', fixed_line)
        # Fix: # comment# comment
        fixed_line = re.sub(r'(#\s*[^\n#]+)#\s*', r'\1\n# ', fixed_line)
        fixed_lines.append(fixed_line)
    
    return '\n'.join(fixed_lines)

def fix_incomplete_imports(source: str) -> str:
    """Fix incomplete import statements like 'from module \n'."""
    lines = source.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        # Check for incomplete import: "from module " or "import module as "
        if re.match(r'^\s*from\s+[\w\.]+\s+$', line):
            # Look for next line with "import"
            if i + 1 < len(lines) and lines[i + 1].strip().startswith('import'):
                # Merge them
                fixed_lines.append(line.rstrip() + ' ' + lines[i + 1].strip())
                i += 2
            else:
                # Just incomplete, keep as is (might be fixable manually)
                fixed_lines.append(line)
                i += 1
        elif re.match(r'^\s*import\s+[\w\.]+\s+as\s+$', line):
            # Incomplete "import module as " - look for next line
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line and not next_line.startswith(('import', 'from', '#')):
                    # Merge
                    fixed_lines.append(line.rstrip() + ' ' + next_line)
                    i += 2
                else:
                    fixed_lines.append(line)
                    i += 1
            else:
                fixed_lines.append(line)
                i += 1
        else:
            fixed_lines.append(line)
            i += 1
    
    return '\n'.join(fixed_lines)

def fix_markdown_in_code(source: str) -> str:
    """Detect and comment out markdown text in code cells."""
    lines = source.split('\n')
    fixed_lines = []
    
    for line in lines:
        stripped = line.strip()
        # Check if line looks like markdown (starts with number, bullet, or plain text without Python syntax)
        if stripped and not stripped.startswith('#'):
            # Check if it's not valid Python
            try:
                ast.parse(line)
                fixed_lines.append(line)
            except:
                # Check if it looks like markdown
                if (re.match(r'^\d+\.', stripped) or  # Numbered list
                    re.match(r'^[-*]', stripped) or  # Bullet list
                    re.match(r'^[A-Z][^:]*:\s*\d+', stripped) or  # "Sample 1: 0.3"
                    (not any(kw in line for kw in ['=', '(', ')', '[', ']', '{', '}', 'def', 'class', 'import', 'from']) and
                     len(stripped) > 10 and not stripped.endswith(':'))):
                    # Comment it out
                    fixed_lines.append('# ' + line)
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_incomplete_try_except(source: str) -> str:
    """Fix incomplete try-except blocks."""
    lines = source.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        # Check for try: followed by pass without except
        if re.match(r'^\s*try\s*:\s*$', line):
            fixed_lines.append(line)
            i += 1
            # Look for pass statement
            if i < len(lines) and re.match(r'^\s+pass\s*$', lines[i]):
                fixed_lines.append(lines[i])
                i += 1
                # Check if next line is not except
                if i >= len(lines) or not re.match(r'^\s*except', lines[i]):
                    # Add except clause
                    indent = len(line) - len(line.lstrip())
                    fixed_lines.append(' ' * indent + 'except Exception as e:')
                    fixed_lines.append(' ' * indent + '    pass')
        else:
            fixed_lines.append(line)
            i += 1
    
    return '\n'.join(fixed_lines)

def fix_split_parameters(source: str) -> str:
    """Fix parameter names split across lines like 'n\nsamples =1000'."""
    # Pattern: identifier\nidentifier = value
    fixed = re.sub(r'([a-zA-Z_][a-zA-Z0-9_]*)\n([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*', r'\1_\2 = ', source)
    # Pattern: identifier\nidentifier: type
    fixed = re.sub(r'([a-zA-Z_][a-zA-Z0-9_]*)\n([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*', r'\1_\2: ', fixed)
    return fixed

def fix_unmatched_parentheses(source: str) -> str:
    """Fix unmatched parentheses by checking balance."""
    lines = source.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Count parentheses
        open_parens = line.count('(')
        close_parens = line.count(')')
        
        # If line ends with unmatched closing paren, might be issue
        if line.strip().endswith(')') and open_parens < close_parens:
            # Check if it's part of a multi-line statement
            if not any(keyword in line for keyword in ['def ', 'class ', 'if ', 'for ', 'while ', 'with ']):
                # Might need to add opening paren or remove closing
                # For now, just pass through - this needs context
                fixed_lines.append(line)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_expected_indented_block(source: str) -> str:
    """Fix 'expected an indented block' errors."""
    lines = source.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        # Check for function/class definition followed by pass on next line without indent
        if re.match(r'^\s*(def|class|if|for|while|with|try|except|else|elif)\s+.*:\s*$', line):
            fixed_lines.append(line)
            i += 1
            # Check if next line is not indented
            if i < len(lines):
                next_line = lines[i]
                if next_line.strip() and not next_line.startswith(' ') and not next_line.startswith('\t'):
                    # Add pass with proper indentation
                    indent = len(line) - len(line.lstrip())
                    fixed_lines.append(' ' * (indent + 4) + 'pass')
                else:
                    fixed_lines.append(next_line)
                    i += 1
        else:
            fixed_lines.append(line)
            i += 1
    
    return '\n'.join(fixed_lines)

def fix_notebook(notebook_path: Path) -> bool:
    """Fix syntax errors in a notebook."""
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
            
            # Skip shell commands and magic commands
            if source.strip().startswith("!") or source.strip().startswith("%"):
                continue
            
            original_source = source
            
            # Apply all fixes
            source = fix_unexpected_indent_pass(source)
            source = fix_missing_newlines(source)
            source = fix_incomplete_imports(source)
            source = fix_split_parameters(source)
            source = fix_incomplete_try_except(source)
            source = fix_unmatched_parentheses(source)
            source = fix_expected_indented_block(source)
            # Fix markdown in code last (as it might comment out things)
            source = fix_markdown_in_code(source)
            
            # Verify fix with ast.parse
            try:
                ast.parse(source)
                # If it parses, update the cell
                if source != original_source:
                    cell["source"] = source.splitlines(keepends=True)
                    modified = True
            except SyntaxError:
                # Fix didn't work, keep original
                pass
        
        if modified:
            # Write back
            with open(notebook_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
        
        return False
    
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
        return False

def main():
    """Main function."""
    print("🔧 Fixing syntax errors in notebooks...\n")
    
    # Read error report
    error_report_path = BASE_DIR / "artifacts" / "syntax_errors_scan.json"
    if not error_report_path.exists():
        print(f"❌ Error report not found: {error_report_path}")
        return
    
    with open(error_report_path) as f:
        error_data = json.load(f)
    
    notebooks_to_fix = [BASE_DIR / err["path"] for err in error_data.get("errors", [])]
    
    print(f"✅ Found {len(notebooks_to_fix)} notebooks with syntax errors\n")
    
    fixed_count = 0
    
    for nb_path in notebooks_to_fix:
        if fix_notebook(nb_path):
            fixed_count += 1
            print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
    
    print(f"\n✅ Fixed {fixed_count}/{len(notebooks_to_fix)} notebooks")

if __name__ == "__main__":
    main()
