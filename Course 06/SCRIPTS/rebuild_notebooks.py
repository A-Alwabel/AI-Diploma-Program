"""
Properly rebuild notebooks from Python files - removing Arabic and fixing structure
"""
import json
import re
import ast
from pathlib import Path

def remove_arabic(text):
    """Remove all Arabic text"""
    if not text:
        return text
    # Remove lines with Arabic
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        if re.search(r'[\u0600-\u06FF]', line):
            # Try to extract English part before /
            if '/' in line:
                parts = line.split('/')
                eng_parts = [p.strip() for p in parts if not re.search(r'[\u0600-\u06FF]', p) and p.strip()]
                if eng_parts:
                    cleaned.append(eng_parts[0])
            # Skip Arabic-only lines
            continue
        else:
            # Remove / markers
            line = re.sub(r'\s*/\s*[^\n]*$', '', line)
            if line.strip():
                cleaned.append(line)
    return '\n'.join(cleaned)

def create_notebook_from_py(py_path):
    """Create clean notebook from Python file"""
    with open(py_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cells = []
    
    # Remove Arabic from entire content first
    content = remove_arabic(content)
    
    # Parse into logical sections
    # 1. Module docstring -> markdown
    doc_match = re.match(r'"""(.*?)"""', content, re.DOTALL)
    if doc_match:
        doc = doc_match.group(1).strip()
        title = doc.split('\n')[0] if '\n' in doc else doc
        cells.append({
            'cell_type': 'markdown',
            'metadata': {},
            'source': [f"# {title}\n\n{doc}"]
        })
        content = content[doc_match.end():].lstrip()
    
    # 2. Imports -> code cell
    import_lines = []
    rest = []
    in_imports = True
    for line in content.split('\n'):
        if in_imports and (line.strip().startswith('import ') or line.strip().startswith('from ')):
            import_lines.append(line)
        elif in_imports and line.strip() and not line.strip().startswith('#'):
            in_imports = False
            rest.append(line)
        else:
            rest.append(line)
    
    if import_lines:
        cells.append({
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'source': import_lines,
            'outputs': []
        })
    
    # 3. Configuration/setup -> code cell
    setup_lines = []
    rest2 = []
    for line in rest:
        if line.strip().startswith('plt.rcParams') or line.strip().startswith('# Set up'):
            setup_lines.append(line)
        else:
            rest2.append(line)
    
    if setup_lines:
        cells.append({
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'source': setup_lines,
            'outputs': []
        })
    
    # 4. Data/constants -> code cell
    data_lines = []
    rest3 = []
    collecting_data = False
    for line in rest2:
        if '=' in line and ('{' in line or '[' in line) and not line.strip().startswith('def') and not line.strip().startswith('class'):
            collecting_data = True
            data_lines.append(line)
        elif collecting_data:
            if line.strip() and not line.strip().startswith('def') and not line.strip().startswith('class') and not line.strip().startswith('if __name__'):
                data_lines.append(line)
            else:
                collecting_data = False
                rest3.append(line)
        else:
            rest3.append(line)
    
    if data_lines:
        cells.append({
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'source': data_lines,
            'outputs': []
        })
    
    # 5. Functions -> separate code cells
    # Find all function definitions
    func_pattern = r'def\s+\w+\([^)]*\):'
    func_matches = list(re.finditer(func_pattern, '\n'.join(rest3)))
    
    for i, match in enumerate(func_matches):
        start = match.start()
        end = func_matches[i+1].start() if i+1 < len(func_matches) else len('\n'.join(rest3))
        
        func_code = '\n'.join(rest3)[start:end].strip()
        if func_code:
            cells.append({
                'cell_type': 'code',
                'execution_count': None,
                'metadata': {},
                'source': [func_code],
                'outputs': []
            })
    
    # 6. Main execution -> code cell
    main_match = re.search(r'if __name__\s*==\s*["\']__main__["\']:(.*?)$', '\n'.join(rest3), re.DOTALL)
    if main_match:
        main_code = main_match.group(1).strip()
        if main_code:
            cells.append({
                'cell_type': 'code',
                'execution_count': None,
                'metadata': {},
                'source': [main_code],
                'outputs': []
            })
    
    # If we didn't parse well, just put everything in code cells
    if len(cells) < 2:
        # Simple approach: split by double newlines and function definitions
        parts = re.split(r'\n\n+', '\n'.join(rest3))
        for part in parts:
            if part.strip() and not part.strip().startswith('#'):
                cells.append({
                    'cell_type': 'code',
                    'execution_count': None,
                    'metadata': {},
                    'source': [part.strip()],
                    'outputs': []
                })
    
    return {
        'cells': cells,
        'metadata': {
            'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
            'language_info': {'name': 'python', 'version': '3.8.0'}
        },
        'nbformat': 4,
        'nbformat_minor': 4
    }

def main():
    """Rebuild all notebooks"""
    base_dir = Path('.')
    
    py_files = []
    for pattern in ['unit*/examples/*.py', 'unit*/exercises/*.py', 'unit*/solutions/*.py']:
        py_files.extend(base_dir.glob(pattern))
    
    for py_file in py_files:
        if py_file.name in ['convert_to_notebooks.py', 'fix_notebooks.py', 'rebuild_notebooks.py']:
            continue
        
        notebook_path = py_file.parent / (py_file.stem + '.ipynb')
        
        try:
            # Simple approach: read Python file, remove Arabic, create notebook
            with open(py_file, 'r', encoding='utf-8') as f:
                py_content = f.read()
            
            # Remove Arabic
            lines = py_content.split('\n')
            cleaned_lines = []
            for line in lines:
                if re.search(r'[\u0600-\u06FF]', line):
                    # Remove Arabic part
                    if '/' in line:
                        eng_part = line.split('/')[0].strip()
                        if eng_part and not re.search(r'[\u0600-\u06FF]', eng_part):
                            cleaned_lines.append(eng_part)
                    continue
                else:
                    # Remove trailing / markers
                    line = re.sub(r'\s*/\s*.*$', '', line)
                    if line.strip() or line == '':
                        cleaned_lines.append(line)
            
            cleaned_content = '\n'.join(cleaned_lines)
            
            # Create simple notebook structure
            cells = []
            
            # Title cell
            title_match = re.search(r'Example \d+[:\s]+(.*?)(?:\n|$)', cleaned_content)
            if title_match:
                title = title_match.group(1).strip()
                cells.append({
                    'cell_type': 'markdown',
                    'metadata': {},
                    'source': [f"# {title}"]
                })
            
            # Split into logical code cells (by functions and main block)
            # Simple: imports, then functions, then main
            imports = []
            functions = []
            main_block = []
            current_section = imports
            
            for line in cleaned_lines:
                if line.strip().startswith('import ') or line.strip().startswith('from '):
                    imports.append(line)
                elif line.strip().startswith('def ') or line.strip().startswith('class '):
                    if imports:
                        cells.append({
                            'cell_type': 'code',
                            'execution_count': None,
                            'metadata': {},
                            'source': imports,
                            'outputs': []
                        })
                        imports = []
                    functions.append(line)
                    current_section = functions
                elif line.strip().startswith('if __name__'):
                    if functions:
                        func_text = '\n'.join(functions)
                        cells.append({
                            'cell_type': 'code',
                            'execution_count': None,
                            'metadata': {},
                            'source': [func_text],
                            'outputs': []
                        })
                        functions = []
                    main_block.append(line)
                    current_section = main_block
                else:
                    current_section.append(line)
            
            # Add remaining sections
            if imports:
                cells.append({
                    'cell_type': 'code',
                    'execution_count': None,
                    'metadata': {},
                    'source': imports,
                    'outputs': []
                })
            
            if functions:
                func_text = '\n'.join(functions)
                cells.append({
                    'cell_type': 'code',
                    'execution_count': None,
                    'metadata': {},
                    'source': [func_text],
                    'outputs': []
                })
            
            if main_block:
                main_text = '\n'.join(main_block)
                cells.append({
                    'cell_type': 'code',
                    'execution_count': None,
                    'metadata': {},
                    'source': [main_text],
                    'outputs': []
                })
            
            # If no cells created, create one with all content
            if not cells:
                cells.append({
                    'cell_type': 'code',
                    'execution_count': None,
                    'metadata': {},
                    'source': [cleaned_content],
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
            
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Rebuilt: {notebook_path.name}")
            
        except Exception as e:
            print(f"❌ Error rebuilding {py_file}: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()

