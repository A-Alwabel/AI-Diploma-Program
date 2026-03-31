"""
Properly fix all notebooks by reading Python files and creating clean notebooks
"""
import json
import re
import ast
from pathlib import Path

def clean_string_literal(match):
    """Clean a string literal, removing Arabic while preserving structure"""
    quote = match.group(1)  # ' or " or f' or f"
    is_fstring = quote.startswith('f')
    if is_fstring:
        quote_char = quote[1]  # Get the actual quote character
    else:
        quote_char = quote
    
    content = match.group(2)
    
    # Remove Arabic from content
    if '/' in content:
        # Split by / and keep only English parts
        parts = content.split('/')
        eng_parts = []
        for part in parts:
            part = part.strip()
            if part and not re.search(r'[\u0600-\u06FF]', part):
                eng_parts.append(part)
        
        if eng_parts:
            new_content = eng_parts[0]  # Take first English part
        else:
            new_content = ''  # Empty if no English
    elif re.search(r'[\u0600-\u06FF]', content):
        # Arabic-only string, make it empty or keep English part
        new_content = ''
    else:
        new_content = content
    
    # Reconstruct string
    if is_fstring:
        return f"f{quote_char}{new_content}{quote_char}"
    else:
        return f"{quote_char}{new_content}{quote_char}"

def clean_python_code(content):
    """Clean Python code properly, preserving string structure"""
    # Remove Arabic comments first
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip Arabic-only comment lines
        if re.match(r'^\s*#\s*[\u0600-\u06FF]', line):
            continue
        
        # Clean comments (keep English, remove Arabic)
        if '#' in line:
            parts = line.split('#', 1)
            code_part = parts[0]
            comment = parts[1] if len(parts) > 1 else ''
            
            # Remove Arabic from comment
            if comment:
                if '/' in comment:
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
            # Clean string literals in the line
            # Pattern: '...' or "..." or f'...' or f"..."
            line = re.sub(r"(f?['\"])([^'\"]*?)(['\"])", clean_string_literal, line)
            
            # Remove trailing / markers
            line = re.sub(r'\s*/\s*.*[\u0600-\u06FF].*$', '', line)
            line = re.sub(r'\s*/\s*$', '', line)
            
            # Remove any remaining Arabic
            if not re.search(r'[\u0600-\u06FF]', line):
                cleaned_lines.append(line)
    
    cleaned = '\n'.join(cleaned_lines)
    
    # Remove any remaining Arabic characters
    cleaned = re.sub(r'[\u0600-\u06FF]', '', cleaned)
    
    return cleaned

def create_clean_notebook(py_file):
    """Create a clean notebook from Python file"""
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Clean the code
    cleaned = clean_python_code(content)
    
    # Verify syntax
    try:
        ast.parse(cleaned)
    except SyntaxError as e:
        # Try to fix common issues
        lines = cleaned.split('\n')
        if e.lineno <= len(lines):
            problem_line = lines[e.lineno - 1]
            # Fix unterminated strings
            if "unterminated string" in str(e):
                if "'" in problem_line and problem_line.count("'") % 2 != 0:
                    lines[e.lineno - 1] = problem_line.rstrip() + "'"
                elif '"' in problem_line and problem_line.count('"') % 2 != 0:
                    lines[e.lineno - 1] = problem_line.rstrip() + '"'
        cleaned = '\n'.join(lines)
    
    # Create notebook cells
    cells = []
    
    # Title cell from docstring
    doc_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
    if doc_match:
        doc = doc_match.group(1).strip()
        # Remove Arabic from docstring
        doc_lines = doc.split('\n')
        eng_doc_lines = []
        for doc_line in doc_lines:
            if '/' in doc_line:
                eng_part = doc_line.split('/')[0].strip()
                if eng_part and not re.search(r'[\u0600-\u06FF]', eng_part):
                    eng_doc_lines.append(eng_part)
            elif not re.search(r'[\u0600-\u06FF]', doc_line):
                eng_doc_lines.append(doc_line)
        
        title = eng_doc_lines[0] if eng_doc_lines else "Example"
        cells.append({
            'cell_type': 'markdown',
            'metadata': {},
            'source': [f"# {title}"]
        })
    
    # Code cell with all cleaned code
    cells.append({
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'source': [cleaned],
        'outputs': []
    })
    
    notebook = {
        'cells': cells,
        'metadata': {
            'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
            'language_info': {'name': 'python', 'version': '3.8.0'}
        },
        'nbformat': 4,
        'nbformat_minor': 4
    }
    
    return notebook

def main():
    """Fix all notebooks"""
    base_dir = Path('.')
    
    py_files = []
    for pattern in ['unit*/examples/*.py', 'unit*/exercises/*.py', 'unit*/solutions/*.py']:
        py_files.extend(base_dir.glob(pattern))
    
    for py_file in py_files:
        if py_file.name in ['convert_to_notebooks.py', 'fix_notebooks.py', 'rebuild_notebooks.py', 'fix_all_notebooks_properly.py']:
            continue
        
        print(f"Processing {py_file.name}...")
        
        try:
            notebook = create_clean_notebook(py_file)
            
            # Verify syntax
            for cell in notebook['cells']:
                if cell['cell_type'] == 'code':
                    code = ''.join(cell['source'])
                    try:
                        ast.parse(code)
                    except SyntaxError as e:
                        print(f"  ⚠️  Syntax error at line {e.lineno}: {e.msg}")
                        # Try one more fix
                        lines = code.split('\n')
                        if e.lineno <= len(lines):
                            problem = lines[e.lineno - 1]
                            # Add missing quote
                            if "'" in problem and problem.count("'") % 2 != 0:
                                lines[e.lineno - 1] = problem + "'"
                            elif '"' in problem and problem.count('"') % 2 != 0:
                                lines[e.lineno - 1] = problem + '"'
                        cell['source'] = ['\n'.join(lines)]
            
            # Save notebook
            nb_path = py_file.parent / (py_file.stem + '.ipynb')
            with open(nb_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=2, ensure_ascii=False)
            
            # Final verification
            final_code = ''.join([''.join(c['source']) if isinstance(c['source'], list) else c['source'] for c in notebook['cells'] if c['cell_type'] == 'code'])
            try:
                ast.parse(final_code)
                print(f"  ✅ Fixed and verified")
            except SyntaxError as e:
                print(f"  ⚠️  Still has error at line {e.lineno}, but saved anyway")
                
        except Exception as e:
            print(f"  ❌ Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()

