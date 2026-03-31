#!/usr/bin/env python3
"""
Comprehensive fix for ALL remaining notebook errors.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def fix_string_literals(notebook_path: Path) -> bool:
    """Fix unterminated string literals in print statements."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                original = source
                
                # Fix: print('\nreport:') with broken quotes
                # Pattern: print('...\n...') where quotes are broken
                source = re.sub(r"print\('\s*\n\s*report:'", "print('\\nreport:')", source)
                source = re.sub(r'print\("\s*\n\s*report:"\)', 'print("\\nreport:")', source)
                
                # Fix: print('confusion\n', -> print('confusion matrix:',
                source = re.sub(r"print\('confusion\s*\n'", "print('confusion matrix:'", source)
                
                # Fix any print statements with newlines in the middle of strings
                # Pattern: print('text\nmore text') -> print('text\\nmore text')
                source = re.sub(r"print\('([^']*?)\s*\n\s*([^']*?)'\)", r"print('\1\\n\2')", source)
                source = re.sub(r'print\("([^"]*?)\s*\n\s*([^"]*?)"\)', r'print("\1\\n\2")', source)
                
                # Fix broken string literals more generally
                # Look for patterns like: 'text\n' where the quote is on next line
                lines = source.split('\n')
                fixed_lines = []
                i = 0
                while i < len(lines):
                    line = lines[i]
                    # Check if line has an unterminated string
                    single_quotes = line.count("'")
                    double_quotes = line.count('"')
                    
                    # If odd number of quotes, might be broken
                    if (single_quotes % 2 == 1 or double_quotes % 2 == 1) and i + 1 < len(lines):
                        # Try to fix by joining with next line
                        if lines[i+1].strip().startswith("'") or lines[i+1].strip().startswith('"'):
                            line = line.rstrip() + lines[i+1].lstrip()
                            i += 1
                    
                    fixed_lines.append(line)
                    i += 1
                
                source = '\n'.join(fixed_lines)
                
                if source != original:
                    cell['source'] = source.splitlines(keepends=True)
                    modified = True
        
        if modified:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
    
    return False

def fix_all_import_errors(notebook_path: Path) -> bool:
    """Fix all import-related syntax errors."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                original = source
                
                # Comprehensive import fixes
                # Fix: from module_\nname -> from module_name
                source = re.sub(r'from\s+(\w+)_\s*\n\s*(\w+)', r'from \1_\2', source)
                
                # Fix: import name_\nname -> import name_name
                source = re.sub(r'import\s+(\w+)_\s*\n\s*(\w+)', r'import \1_\2', source)
                
                # Fix common sklearn patterns
                source = re.sub(r'sklearn\.model\s*\n\s*_selection', 'sklearn.model_selection', source)
                source = re.sub(r'sklearn\.preprocessing\s*\n\s*import', 'sklearn.preprocessing import', source)
                source = re.sub(r'sklearn\.compose\s*\n\s*import', 'sklearn.compose import', source)
                source = re.sub(r'sklearn\.pipeline\s*\n\s*import', 'sklearn.pipeline import', source)
                source = re.sub(r'sklearn\.linear\s*\n\s*_model', 'sklearn.linear_model', source)
                source = re.sub(r'sklearn\.metrics\s*\n\s*import', 'sklearn.metrics import', source)
                
                # Fix function names with line breaks
                source = re.sub(r'train_test\s*\n\s*_split', 'train_test_split', source)
                source = re.sub(r'accuracy_\s*\n\s*score', 'accuracy_score', source)
                source = re.sub(r'confusion_\s*\n\s*matrix', 'confusion_matrix', source)
                source = re.sub(r'classification_\s*\n\s*report', 'classification_report', source)
                source = re.sub(r'default_\s*\n\s*rng', 'default_rng', source)
                
                # Fix: LogisticRegression sklearn.metrics -> LogisticRegression\nfrom sklearn.metrics
                source = re.sub(r'LogisticRegression\s+sklearn\.metrics', 'LogisticRegression\nfrom sklearn.metrics', source)
                
                # Fix missing 'from' keywords
                source = re.sub(r'(\w+)\s+sklearn\.(\w+)\s+import', r'from sklearn.\2 import \1', source)
                
                # Fix: importt -> import
                source = re.sub(r'\bimportt\b', 'import', source)
                
                # Fix variable names with line breaks
                source = re.sub(r'(\w+)_\s*\n\s*(\w+)\s*=', r'\1_\2 =', source)
                source = re.sub(r'(\w+)_\s*\n\s*(\w+)\s*\(', r'\1_\2(', source)
                
                if source != original:
                    cell['source'] = source.splitlines(keepends=True)
                    modified = True
        
        if modified:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"Error fixing imports in {notebook_path}: {e}")
    
    return False

def fix_code_structure(notebook_path: Path) -> bool:
    """Fix code structure issues (missing newlines, etc.)."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                original = source
                
                # Fix: n = 600x1 -> n = 600\nx1
                source = re.sub(r'n\s*=\s*600x1', 'n = 600\nx1', source)
                source = re.sub(r'n\s*=\s*(\d+)([a-zA-Z_])', r'n = \1\n\2', source)
                
                # Fix: datase\ntr\nng -> dataset\nrng
                source = re.sub(r'datase\s*\n\s*tr\s*\n\s*ng', 'dataset\nrng', source)
                
                # Fix: rng = np.random.default_\nrng -> rng = np.random.default_rng
                source = re.sub(r'np\.random\.default_\s*\n\s*rng', 'np.random.default_rng', source)
                
                # Fix function calls with line breaks in arguments
                source = re.sub(r'test_\s*\n\s*size', 'test_size', source)
                source = re.sub(r'random_\s*\n\s*state', 'random_state', source)
                source = re.sub(r'handle_\s*\n\s*unknown', 'handle_unknown', source)
                
                # Fix: train_test_split(X, y, test_\nsize -> train_test_split(X, y, test_size
                source = re.sub(r'train_test_split\(([^)]*),\s*test_\s*\n\s*size', r'train_test_split(\1, test_size', source)
                
                if source != original:
                    cell['source'] = source.splitlines(keepends=True)
                    modified = True
        
        if modified:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"Error fixing structure in {notebook_path}: {e}")
    
    return False

def main():
    """Fix all remaining errors."""
    print("=" * 70)
    print("COMPREHENSIVE FIX FOR ALL REMAINING ERRORS")
    print("=" * 70)
    
    # Load failure report
    report_file = BASE_DIR / "artifacts" / "notebook_execution_report.json"
    if not report_file.exists():
        print("Execution report not found!")
        return
    
    with open(report_file, 'r') as f:
        report = json.load(f)
    
    failed = [r for r in report['results'] if r.get('status') == 'failed']
    print(f"\nFixing {len(failed)} failed notebooks...\n")
    
    fixed_strings = 0
    fixed_imports = 0
    fixed_structure = 0
    
    for i, failure in enumerate(failed, 1):
        nb_path = BASE_DIR / failure['path']
        if not nb_path.exists():
            continue
        
        error = failure.get('error', '').lower()
        modified = False
        
        # Fix based on error type
        if 'unterminated string' in error or 'string literal' in error:
            if fix_string_literals(nb_path):
                fixed_strings += 1
                modified = True
        
        if 'import' in error or 'module' in error or 'sklearn' in error:
            if fix_all_import_errors(nb_path):
                fixed_imports += 1
                modified = True
        
        if 'syntax' in error or 'invalid' in error:
            if fix_code_structure(nb_path):
                fixed_structure += 1
                modified = True
        
        # Always try all fixes
        if not modified:
            if fix_string_literals(nb_path):
                fixed_strings += 1
            if fix_all_import_errors(nb_path):
                fixed_imports += 1
            if fix_code_structure(nb_path):
                fixed_structure += 1
        
        if i % 50 == 0:
            print(f"  Progress: {i}/{len(failed)}...")
    
    print("\n" + "=" * 70)
    print("FIX SUMMARY")
    print("=" * 70)
    print(f"Fixed string literals: {fixed_strings} notebooks")
    print(f"Fixed import errors: {fixed_imports} notebooks")
    print(f"Fixed code structure: {fixed_structure} notebooks")
    print("=" * 70)

if __name__ == "__main__":
    main()
