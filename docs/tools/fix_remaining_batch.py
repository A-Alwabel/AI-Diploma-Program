#!/usr/bin/env python3
"""
Batch fix remaining notebook issues - extract code from markdown, fix missing definitions
"""

import json
import re
import ast
from pathlib import Path
from typing import List, Tuple, Optional

def extract_code_from_markdown(source: str) -> Optional[Tuple[str, str]]:
    """Extract executable Python code from markdown cell"""
    lines = source.split('\n')
    code_lines = []
    markdown_lines = []
    in_code_block = False
    code_start_idx = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check if this line starts executable code
        if (stripped.startswith('def ') or 
            stripped.startswith('class ') or
            stripped.startswith('import ') or
            stripped.startswith('from ') or
            (stripped and re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*\s*=', stripped))):
            code_start_idx = i
            break
    
    if code_start_idx is None:
        return None
    
    # Collect code lines
    indent_level = None
    for i in range(code_start_idx, len(lines)):
        line = lines[i]
        stripped = line.strip()
        
        if not stripped:
            continue
        
        # Determine initial indent
        if indent_level is None and stripped:
            indent_level = len(line) - len(line.lstrip())
        
        # Check if still in code block
        current_indent = len(line) - len(line.lstrip()) if line.strip() else 0
        
        # Stop if we hit markdown patterns
        if (stripped.startswith('#') and 'WHY' in stripped.upper() and 'HOW' in stripped.upper()):
            break
        if stripped.startswith('**') or stripped.startswith('##'):
            break
        
        code_lines.append(line)
    
    if not code_lines:
        return None
    
    # Clean and validate code
    code = '\n'.join(code_lines)
    # Remove markdown formatting
    code = re.sub(r'\*\*([^*]+)\*\*', r'\1', code)
    code = re.sub(r'`([^`]+)`', r'\1', code)
    
    # Try to parse
    try:
        ast.parse(code)
        # Extract remaining markdown
        markdown = '\n'.join(lines[:code_start_idx])
        return markdown, code
    except SyntaxError:
        # Try adding pass for empty blocks
        try:
            test_code = code + '\n    pass'
            ast.parse(test_code)
            return '\n'.join(lines[:code_start_idx]), code
        except:
            return None

def fix_notebook(nb_path: Path) -> Tuple[bool, int]:
    """Fix notebook issues"""
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        return False, 0
    
    total_fixes = 0
    notebook_modified = False
    new_cells = []
    
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            source = cell.get('source', [])
            if isinstance(source, str):
                source_str = source
            else:
                source_str = ''.join(source)
            
            # Try to extract code
            result = extract_code_from_markdown(source_str)
            if result:
                markdown, code = result
                # Update markdown cell
                cell['source'] = markdown.splitlines(keepends=True) if markdown else ['']
                # Add new code cell
                new_cells.append({
                    'cell_type': 'code',
                    'execution_count': None,
                    'metadata': {},
                    'outputs': [],
                    'source': code.splitlines(keepends=True)
                })
                total_fixes += 1
                notebook_modified = True
        
        new_cells.append(cell)
    
    if notebook_modified:
        nb['cells'] = new_cells
        try:
            with open(nb_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, ensure_ascii=False, indent=1)
            return True, total_fixes
        except Exception as e:
            return False, total_fixes
    
    return False, 0

def main():
    """Main function"""
    base_dir = Path(__file__).parent.parent
    
    # Get failed notebooks from report
    report_path = base_dir / 'artifacts/notebook_execution_report_v2.json'
    with open(report_path) as f:
        data = json.load(f)
    
    failed = [r for r in data.get('results', []) if r.get('status') != 'passed' and '.nbconvert' not in r.get('path', '')]
    
    known_passing = [
        'Course 01/unit1-ai-foundations/examples/06_knowledge_representation.ipynb',
        'Course 01/unit2-search-algorithms/examples/07_rdf_sparql_knowledge_graph.ipynb',
        'Course 02/unit2-knowledge-representation/examples/03_propositional_logic_truth_tables.ipynb',
        'Course 02/unit2-knowledge-representation/examples/05_first_order_logic_fol.ipynb',
        'Course 02/unit3-learning-under-uncertainty/examples/04_mdp_value_iteration.ipynb',
        'Course 03/modules/module_02/examples/03_gradient_descent.ipynb',
        'Course 03/modules/module_03/examples/03_statistical_measures.ipynb',
        'Course 03/modules/module_03/examples/01_optimizers_comparison.ipynb',
        'Course 03/modules/module_04/examples/02_curse_dimensionality.ipynb',
        'Course 03/unit2-calculus/examples/03_gradient_descent.ipynb',
        'Course 03/unit1-linear-algebra/examples/06_transformation_matrices_orthogonal_basis.ipynb',
        'Course 03/unit2-calculus/examples/04_backpropagation_neural_networks.ipynb',
        'Course 03/unit3-optimization/examples/01_optimizers_comparison.ipynb',
    ]
    
    real_failed = [r for r in failed if r.get('path') not in known_passing]
    
    print(f"🔧 Fixing {len(real_failed)} Remaining Notebooks\n")
    
    fixed_count = 0
    total_fixes = 0
    
    for i, result in enumerate(real_failed[:20], 1):  # Process first 20
        nb_path = base_dir / result.get('path')
        if not nb_path.exists():
            continue
        
        success, fixes = fix_notebook(nb_path)
        if success:
            fixed_count += 1
            total_fixes += fixes
            print(f"  ✓ Fixed: {result.get('path')} ({fixes} fixes)")
    
    print(f"\n✅ Fixed {fixed_count} notebooks ({total_fixes} total fixes)")

if __name__ == '__main__':
    main()
