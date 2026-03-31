"""
Script to properly convert Python files to notebooks without Arabic
"""
import json
import re
from pathlib import Path

def remove_arabic_from_text(text):
    """Remove Arabic text and bilingual markers"""
    if not text:
        return text
    
    # Remove Arabic characters and text after slashes
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # Remove Arabic characters
        if re.search(r'[\u0600-\u06FF]', line):
            # Try to keep English part before Arabic
            if '/' in line:
                parts = line.split('/')
                english_parts = [p for p in parts if not re.search(r'[\u0600-\u06FF]', p)]
                if english_parts:
                    line = ' / '.join(english_parts).strip()
                else:
                    continue
            else:
                continue
        
        # Clean up remaining markers
        line = re.sub(r'\s*/\s*$', '', line)
        if line.strip():
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def clean_code(code_text):
    """Clean code by removing Arabic comments and text"""
    lines = code_text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip lines with only Arabic
        if re.search(r'^[\s#]*[\u0600-\u06FF]', line):
            continue
        
        # Remove Arabic from comments
        if '#' in line:
            parts = line.split('#', 1)
            code_part = parts[0]
            comment_part = parts[1] if len(parts) > 1 else ''
            
            # Remove Arabic from comment
            if comment_part and not re.search(r'[\u0600-\u06FF]', comment_part):
                cleaned_lines.append(f"{code_part}#{comment_part}")
            elif code_part.strip():
                cleaned_lines.append(code_part.rstrip())
        else:
            # Remove Arabic from strings (simple approach)
            if re.search(r'[\u0600-\u06FF]', line):
                # Try to extract English parts
                if '/' in line and '"' in line:
                    # String with slash separator
                    continue
                elif not line.strip().startswith('"""'):
                    cleaned_lines.append(line)
            else:
                cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def convert_py_to_notebook(py_path, output_path):
    """Convert Python file to proper Jupyter notebook"""
    with open(py_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cells = []
    
    # Extract module docstring as first markdown cell
    docstring_match = re.match(r'"""(.*?)"""', content, re.DOTALL)
    if docstring_match:
        docstring = docstring_match.group(1).strip()
        docstring = remove_arabic_from_text(docstring)
        if docstring:
            cells.append({
                'cell_type': 'markdown',
                'metadata': {},
                'source': [f"# {docstring.split(chr(10))[0]}\n\n{docstring}"]
            })
        content = content[docstring_match.end():].lstrip()
    
    # Split by section markers
    sections = re.split(r'# =+.*?=+\n', content)
    
    current_code = []
    
    for section in sections:
        if not section.strip():
            continue
        
        lines = section.split('\n')
        section_code = []
        in_function = False
        function_indent = 0
        
        for i, line in enumerate(lines):
            # Check for function/class definitions
            if re.match(r'^(def|class)\s+', line):
                # Save previous code if any
                if current_code:
                    code_text = '\n'.join(current_code)
                    code_text = clean_code(code_text)
                    if code_text.strip():
                        cells.append({
                            'cell_type': 'code',
                            'execution_count': None,
                            'metadata': {},
                            'source': [code_text],
                            'outputs': []
                        })
                    current_code = []
                
                in_function = True
                function_indent = len(line) - len(line.lstrip())
                section_code.append(line)
            elif in_function:
                # Check if we're still in the function
                if line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                    # New top-level statement
                    if section_code:
                        code_text = '\n'.join(section_code)
                        code_text = clean_code(code_text)
                        if code_text.strip():
                            cells.append({
                                'cell_type': 'code',
                                'execution_count': None,
                                'metadata': {},
                                'source': [code_text],
                                'outputs': []
                            })
                        section_code = []
                    in_function = False
                    current_code.append(line)
                else:
                    section_code.append(line)
            else:
                # Regular code
                if line.strip().startswith('if __name__'):
                    # Main execution block - separate cell
                    if current_code:
                        code_text = '\n'.join(current_code)
                        code_text = clean_code(code_text)
                        if code_text.strip():
                            cells.append({
                                'cell_type': 'code',
                                'execution_count': None,
                                'metadata': {},
                                'source': [code_text],
                                'outputs': []
                            })
                        current_code = []
                    
                    # Get rest of main block
                    main_block = '\n'.join(lines[i:])
                    main_block = clean_code(main_block)
                    if main_block.strip():
                        cells.append({
                            'cell_type': 'code',
                            'execution_count': None,
                            'metadata': {},
                            'source': [main_block],
                            'outputs': []
                        })
                    break
                else:
                    current_code.append(line)
        
        # Add remaining section code
        if section_code:
            code_text = '\n'.join(section_code)
            code_text = clean_code(code_text)
            if code_text.strip():
                cells.append({
                    'cell_type': 'code',
                    'execution_count': None,
                    'metadata': {},
                    'source': [code_text],
                    'outputs': []
                })
    
    # Add any remaining code
    if current_code:
        code_text = '\n'.join(current_code)
        code_text = clean_code(code_text)
        if code_text.strip():
            cells.append({
                'cell_type': 'code',
                'execution_count': None,
                'metadata': {},
                'source': [code_text],
                'outputs': []
            })
    
    # Create notebook
    notebook = {
        'cells': cells,
        'metadata': {
            'kernelspec': {
                'display_name': 'Python 3',
                'language': 'python',
                'name': 'python3'
            },
            'language_info': {
                'name': 'python',
                'version': '3.8.0'
            }
        },
        'nbformat': 4,
        'nbformat_minor': 4
    }
    
    # Write notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Fixed: {output_path.name}")

def main():
    """Fix all notebooks"""
    base_dir = Path('.')
    
    # Find all Python files
    py_files = []
    for pattern in ['unit*/examples/*.py', 'unit*/exercises/*.py', 'unit*/solutions/*.py']:
        py_files.extend(base_dir.glob(pattern))
    
    for py_file in py_files:
        if py_file.name in ['convert_to_notebooks.py', 'fix_notebooks.py']:
            continue
        
        # Create notebook path
        notebook_path = py_file.parent / (py_file.stem + '.ipynb')
        
        try:
            convert_py_to_notebook(py_file, notebook_path)
        except Exception as e:
            print(f"❌ Error fixing {py_file}: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()

