#!/usr/bin/env python3
"""
Comprehensive notebook fixer for Course 06 - Ethics
Fixes common issues: syntax errors, formatting, cell structure, etc.
Similar to Course 04 fix script
"""
import json
import ast
import re
from pathlib import Path

def clean_arabic_from_code(code):
    """Remove Arabic text from code while preserving structure"""
    if not code:
        return code
    
    lines = code.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip lines that are only Arabic
        if re.match(r'^\s*[\u0600-\u06FF]', line):
            continue
        
        # Clean comments (remove Arabic parts)
        if '#' in line:
            parts = line.split('#', 1)
            code_part = parts[0]
            comment = parts[1] if len(parts) > 1 else ''
            
            if comment:
                # Remove Arabic from comment
                if '/' in comment:
                    # Take English part before /
                    eng_comment = comment.split('/')[0].strip()
                    if eng_comment and not re.search(r'[\u0600-\u06FF]', eng_comment):
                        cleaned_lines.append(f"{code_part}# {eng_comment}")
                    elif code_part.strip():
                        cleaned_lines.append(code_part.rstrip())
                elif not re.search(r'[\u0600-\u06FF]', comment):
                    cleaned_lines.append(f"{code_part}#{comment}")
                elif code_part.strip():
                    cleaned_lines.append(code_part.rstrip())
            elif code_part.strip():
                cleaned_lines.append(code_part.rstrip())
        else:
            # Clean string literals
            # Remove Arabic from strings
            line = re.sub(r'[\u0600-\u06FF]', '', line)
            # Remove / markers
            line = re.sub(r'\s*/\s*$', '', line)
            if line.strip():
                cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def fix_code_cell(cell):
    """Fix issues in a code cell"""
    if cell['cell_type'] != 'code':
        return False
    
    fixed = False
    source = cell['source']
    
    # Convert source to string if it's a list
    if isinstance(source, list):
        code = ''.join(source)
    else:
        code = source
    
    # Clean Arabic
    cleaned_code = clean_arabic_from_code(code)
    if cleaned_code != code:
        fixed = True
        code = cleaned_code
    
    # Fix common syntax issues
    lines = code.split('\n')
    new_lines = []
    
    for i, line in enumerate(lines):
        original_line = line
        
        # Fix broken imports
        if 'from sklearn' in line or 'from fairlearn' in line or 'from shap' in line:
            if '(' in line and line.count('(') > line.count(')'):
                # Missing closing parenthesis
                if line.rstrip().endswith(','):
                    line = line.rstrip()[:-1] + ')'
                else:
                    line = line.rstrip() + ')'
                fixed = True
        
        # Fix concatenated code (missing newlines)
        patterns = [
            (r'\)print\(', r')\nprint('),
            (r'\)plt\.', r')\nplt.'),
            (r'\)df\.', r')\ndf.'),
            (r'\)X\.', r')\nX.'),
            (r'\)y\.', r')\ny.'),
        ]
        
        for pattern, replacement in patterns:
            if re.search(pattern, line):
                line = re.sub(pattern, replacement, line)
                fixed = True
        
        new_lines.append(line)
    
    # Verify syntax
    new_code = '\n'.join(new_lines)
    try:
        ast.parse(new_code)
    except SyntaxError:
        # If still has errors, try to fix common issues
        # Remove empty lines that might cause issues
        new_lines = [l for l in new_lines if l.strip() or not l]
        new_code = '\n'.join(new_lines)
        try:
            ast.parse(new_code)
        except SyntaxError:
            # Keep original if we can't fix it
            pass
    
    if fixed:
        cell['source'] = new_code.split('\n')
        # Ensure each line ends with newline
        cell['source'] = [line + '\n' if not line.endswith('\n') else line for line in cell['source']]
    
    return fixed

def fix_markdown_cell(cell):
    """Fix issues in a markdown cell"""
    if cell['cell_type'] != 'markdown':
        return False
    
    fixed = False
    source = cell['source']
    
    if isinstance(source, list):
        text = ''.join(source)
    else:
        text = source
    
    # Remove Arabic from markdown
    if re.search(r'[\u0600-\u06FF]', text):
        # Remove lines with Arabic
        lines = text.split('\n')
        cleaned_lines = []
        for line in lines:
            if not re.search(r'[\u0600-\u06FF]', line):
                cleaned_lines.append(line)
        text = '\n'.join(cleaned_lines)
        fixed = True
    
    # Remove empty markdown cells
    if not text.strip() or text.strip() == '#':
        return 'remove'
    
    if fixed:
        cell['source'] = text.split('\n') if text else ['']
    
    return fixed

def fix_notebook(notebook_path):
    """Fix all issues in a notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        fixed = False
        cells_to_remove = []
        
        for i, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'code':
                if fix_code_cell(cell):
                    fixed = True
            elif cell['cell_type'] == 'markdown':
                result = fix_markdown_cell(cell)
                if result == 'remove':
                    cells_to_remove.append(i)
                elif result:
                    fixed = True
        
        # Remove empty cells (in reverse order to maintain indices)
        for idx in reversed(cells_to_remove):
            nb['cells'].pop(idx)
            fixed = True
        
        # Ensure proper notebook structure
        if 'metadata' not in nb:
            nb['metadata'] = {}
        
        if 'kernelspec' not in nb['metadata']:
            nb['metadata']['kernelspec'] = {
                'display_name': 'Python 3',
                'language': 'python',
                'name': 'python3'
            }
        
        if 'language_info' not in nb['metadata']:
            nb['metadata']['language_info'] = {
                'name': 'python',
                'version': '3.8.0'
            }
        
        if fixed:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=2, ensure_ascii=False)
            return True
        
        return False
    
    except Exception as e:
        print(f"  ❌ Error fixing {notebook_path.name}: {e}")
        return False

def verify_notebook(notebook_path):
    """Verify notebook syntax and structure"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        issues = []
        
        # Check structure
        if 'cells' not in nb:
            issues.append("Missing 'cells' key")
            return False, issues
        
        if not nb['cells']:
            issues.append("No cells in notebook")
            return False, issues
        
        # Check each code cell
        for i, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
                
                # Check for syntax errors
                try:
                    ast.parse(source)
                except SyntaxError as e:
                    issues.append(f"Cell {i}: Syntax error at line {e.lineno}: {e.msg}")
                
                # Check for Arabic
                if re.search(r'[\u0600-\u06FF]', source):
                    issues.append(f"Cell {i}: Contains Arabic text")
        
        return len(issues) == 0, issues
    
    except Exception as e:
        return False, [f"Error reading notebook: {e}"]

def main():
    """Fix and verify all notebooks"""
    base_dir = Path('.')
    notebooks = list(base_dir.rglob('*.ipynb'))
    
    # Filter out checkpoints
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    print(f"Found {len(notebooks)} notebooks")
    print("=" * 80)
    print("FIXING NOTEBOOKS...")
    print("=" * 80)
    
    fixed_count = 0
    for nb_path in sorted(notebooks):
        rel_path = nb_path.relative_to(base_dir)
        print(f"\nProcessing: {rel_path}")
        
        if fix_notebook(nb_path):
            print(f"  ✅ Fixed issues")
            fixed_count += 1
        else:
            print(f"  ✓ No issues found")
    
    print("\n" + "=" * 80)
    print("VERIFYING NOTEBOOKS...")
    print("=" * 80)
    
    verified_count = 0
    error_count = 0
    
    for nb_path in sorted(notebooks):
        rel_path = nb_path.relative_to(base_dir)
        is_valid, issues = verify_notebook(nb_path)
        
        if is_valid:
            print(f"✅ {rel_path}")
            verified_count += 1
        else:
            print(f"❌ {rel_path}")
            for issue in issues:
                print(f"   - {issue}")
            error_count += 1
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total notebooks: {len(notebooks)}")
    print(f"Fixed: {fixed_count}")
    print(f"Verified: {verified_count}")
    print(f"Errors: {error_count}")
    print("=" * 80)

if __name__ == '__main__':
    main()

