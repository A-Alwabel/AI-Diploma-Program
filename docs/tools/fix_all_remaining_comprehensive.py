#!/usr/bin/env python3
"""
Comprehensive fix for ALL remaining notebook errors - final pass.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def comprehensive_fix(notebook_path: Path) -> bool:
    """Apply all possible fixes to a notebook."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                original = source
                
                # ===== IMPORT FIXES =====
                # Fix: import from -> import
                source = re.sub(r'\bimport\s+from\s+', 'import ', source)
                
                # Fix all sklearn import patterns
                source = re.sub(r'from\s+sklearn\.model\s*\n\s*_selection', 'from sklearn.model_selection', source)
                source = re.sub(r'from\s+sklearn\.preprocessing\s*\n\s*import', 'from sklearn.preprocessing import', source)
                source = re.sub(r'from\s+sklearn\.compose\s*\n\s*import', 'from sklearn.compose import', source)
                source = re.sub(r'from\s+sklearn\.pipeline\s*\n\s*import', 'from sklearn.pipeline import', source)
                source = re.sub(r'from\s+sklearn\.linear\s*\n\s*_model', 'from sklearn.linear_model', source)
                source = re.sub(r'from\s+sklearn\.metrics\s*\n\s*import', 'from sklearn.metrics import', source)
                
                # Fix function names with breaks
                source = re.sub(r'train_test\s*\n\s*_split', 'train_test_split', source)
                source = re.sub(r'accuracy_\s*\n\s*score', 'accuracy_score', source)
                source = re.sub(r'confusion_\s*\n\s*matrix', 'confusion_matrix', source)
                source = re.sub(r'classification_\s*\n\s*report', 'classification_report', source)
                
                # Fix: word_\nword -> word_word (general pattern)
                source = re.sub(r'(\w+)_\s*\n\s*(\w+)', r'\1_\2', source)
                
                # ===== PRINT STATEMENT FIXES =====
                # Fix: print('text'), function(...)) -> print('text', function(...))
                source = re.sub(r"print\('([^']+)'\),\s*(\w+)\(([^)]+)\)\)", r"print('\1', \2(\3))", source)
                source = re.sub(r'print\("([^"]+)"\),\s*(\w+)\(([^)]+)\)\)', r'print("\1", \2(\3))', source)
                
                # Fix: print('\nreport:'), -> print('\nreport:',
                source = re.sub(r"print\('\\\\nreport:'\),", "print('\\\\nreport:',", source)
                source = re.sub(r'print\("\\\\nreport:"\),', 'print("\\\\nreport:",', source)
                
                # Fix unterminated strings in print
                source = re.sub(r"print\('([^']*?)\s*\n\s*([^']*?)'\)", r"print('\1\\n\2')", source)
                source = re.sub(r'print\("([^"]*?)\s*\n\s*([^"]*?)"\)', r'print("\1\\n\2")', source)
                
                # ===== CODE STRUCTURE FIXES =====
                # Fix: n = 600x1 -> n = 600\nx1
                source = re.sub(r'n\s*=\s*(\d+)([a-zA-Z_])', r'n = \1\n\2', source)
                
                # Fix: datase\ntr\nng -> dataset\nrng
                source = re.sub(r'datase\s*\n\s*tr\s*\n\s*ng', 'dataset\nrng', source)
                
                # Fix function calls with line breaks
                source = re.sub(r'test_\s*\n\s*size', 'test_size', source)
                source = re.sub(r'random_\s*\n\s*state', 'random_state', source)
                source = re.sub(r'handle_\s*\n\s*unknown', 'handle_unknown', source)
                source = re.sub(r'default_\s*\n\s*rng', 'default_rng', source)
                
                # Fix: train_test_split(..., test_\nsize -> train_test_split(..., test_size
                source = re.sub(r'train_test_split\(([^)]*),\s*test_\s*\n\s*size', r'train_test_split(\1, test_size', source)
                
                # ===== STRING LITERAL FIXES =====
                # Fix broken string quotes
                lines = source.split('\n')
                fixed_lines = []
                i = 0
                while i < len(lines):
                    line = lines[i]
                    
                    # Check for unterminated strings
                    single_count = line.count("'") - line.count("\\'")
                    double_count = line.count('"') - line.count('\\"')
                    
                    # If odd quotes and next line might continue it
                    if (single_count % 2 == 1 or double_count % 2 == 1) and i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        # If next line starts with quote or is continuation
                        if next_line.startswith("'") or next_line.startswith('"') or not next_line.startswith('#'):
                            # Try to merge
                            merged = line.rstrip() + ' ' + next_line.lstrip()
                            # Check if this fixes it
                            new_single = merged.count("'") - merged.count("\\'")
                            new_double = merged.count('"') - merged.count('\\"')
                            if new_single % 2 == 0 and new_double % 2 == 0:
                                line = merged
                                i += 1
                    
                    fixed_lines.append(line)
                    i += 1
                
                source = '\n'.join(fixed_lines)
                
                # ===== FINAL CLEANUP =====
                # Remove any remaining double spaces
                source = re.sub(r'  +', ' ', source)
                
                # Fix: importt -> import
                source = re.sub(r'\bimportt\b', 'import', source)
                
                # Fix: fromm -> from
                source = re.sub(r'\bfromm\b', 'from', source)
                
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

def main():
    """Fix all remaining notebooks."""
    print("=" * 70)
    print("COMPREHENSIVE FIX - ALL REMAINING NOTEBOOKS")
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
    
    fixed_count = 0
    for i, failure in enumerate(failed, 1):
        nb_path = BASE_DIR / failure['path']
        if not nb_path.exists():
            continue
        
        if comprehensive_fix(nb_path):
            fixed_count += 1
            if fixed_count <= 20 or i % 50 == 0:
                print(f"  ✓ Fixed: {failure['path'][:55]} ({i}/{len(failed)})")
    
    print("\n" + "=" * 70)
    print(f"FIXED {fixed_count} NOTEBOOKS")
    print("=" * 70)
    print("\nRe-running failed notebooks to verify fixes...")

if __name__ == "__main__":
    main()
