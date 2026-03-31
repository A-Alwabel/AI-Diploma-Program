"""
Script to convert all Python examples to Jupyter notebooks without Arabic text
"""
import json
import re
import os
from pathlib import Path

def remove_arabic(text):
    """Remove Arabic text and bilingual markers"""
    if not text:
        return text
    
    # Remove Arabic text in parentheses or after slashes
    text = re.sub(r'\s*/\s*[^\n]*[\u0600-\u06FF][^\n]*', '', text)
    text = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '', text)
    
    # Remove lines with Arabic characters
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # Keep line if it doesn't contain Arabic characters
        if not re.search(r'[\u0600-\u06FF]', line):
            # Clean up remaining markers
            line = re.sub(r'\s*/\s*$', '', line)
            line = re.sub(r'\s*#\s*$', '', line)
            if line.strip():
                cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def extract_cells_from_py(py_content):
    """Extract markdown and code cells from Python file"""
    cells = []
    current_code = []
    in_docstring = False
    docstring_content = []
    
    lines = py_content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check for module docstring
        if line.strip().startswith('"""') and not in_docstring:
            in_docstring = True
            docstring_content = [line.strip()[3:]]  # Remove opening """
            i += 1
            continue
        
        if in_docstring:
            if '"""' in line:
                # End of docstring
                docstring_content.append(line.split('"""')[0])
                docstring = '\n'.join(docstring_content).strip()
                docstring = remove_arabic(docstring)
                if docstring:
                    cells.append({
                        'cell_type': 'markdown',
                        'metadata': {},
                        'source': [docstring]
                    })
                in_docstring = False
                # Continue with rest of line if any
                rest = line.split('"""', 1)[1]
                if rest.strip():
                    current_code.append(rest)
            else:
                docstring_content.append(line)
            i += 1
            continue
        
        # Check for section comments
        if line.strip().startswith('# =') and '=' in line:
            # Save current code if any
            if current_code:
                code_text = '\n'.join(current_code).strip()
                code_text = remove_arabic(code_text)
                if code_text:
                    cells.append({
                        'cell_type': 'code',
                        'execution_count': None,
                        'metadata': {},
                        'source': [code_text],
                        'outputs': []
                    })
                current_code = []
            
            # Create markdown cell for section header
            section_title = line.replace('#', '').replace('=', '').strip()
            section_title = remove_arabic(section_title)
            if section_title:
                cells.append({
                    'cell_type': 'markdown',
                    'metadata': {},
                    'source': [f'## {section_title}']
                })
        elif line.strip().startswith('#'):
            # Regular comment - could be markdown or code comment
            comment = line.strip()[1:].strip()
            comment = remove_arabic(comment)
            if comment and not comment.startswith('='):
                # Save current code first
                if current_code:
                    code_text = '\n'.join(current_code).strip()
                    code_text = remove_arabic(code_text)
                    if code_text:
                        cells.append({
                            'cell_type': 'code',
                            'execution_count': None,
                            'metadata': {},
                            'source': [code_text],
                            'outputs': []
                        })
                    current_code = []
                
                # Add as markdown if it looks like a heading or important comment
                if any(word in comment.lower() for word in ['import', 'setup', 'define', 'create', 'visualization']):
                    cells.append({
                        'cell_type': 'markdown',
                        'metadata': {},
                        'source': [f'### {comment}']
                    })
        else:
            # Regular code line
            current_code.append(line)
        
        i += 1
    
    # Add remaining code
    if current_code:
        code_text = '\n'.join(current_code).strip()
        code_text = remove_arabic(code_text)
        if code_text:
            cells.append({
                'cell_type': 'code',
                'execution_count': None,
                'metadata': {},
                'source': [code_text],
                'outputs': []
            })
    
    return cells

def convert_py_to_notebook(py_path, output_path):
    """Convert Python file to Jupyter notebook"""
    with open(py_path, 'r', encoding='utf-8') as f:
        py_content = f.read()
    
    # Remove Arabic from content
    py_content = remove_arabic(py_content)
    
    # Extract cells
    cells = extract_cells_from_py(py_content)
    
    # Create notebook structure
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
    
    print(f"✅ Converted: {py_path.name} -> {output_path.name}")

def main():
    """Convert all Python examples to notebooks"""
    base_dir = Path('.')
    
    # Find all Python example files
    py_files = []
    for pattern in ['unit*/examples/*.py', 'unit*/exercises/*.py', 'unit*/solutions/*.py']:
        py_files.extend(base_dir.glob(pattern))
    
    # Filter out solution files if needed, or convert all
    for py_file in py_files:
        if py_file.name == 'convert_to_notebooks.py':
            continue
        
        # Create notebook path
        notebook_path = py_file.parent / (py_file.stem + '.ipynb')
        
        # Convert
        try:
            convert_py_to_notebook(py_file, notebook_path)
        except Exception as e:
            print(f"❌ Error converting {py_file}: {e}")

if __name__ == '__main__':
    main()

