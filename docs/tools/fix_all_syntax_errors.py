#!/usr/bin/env python3
"""
Comprehensive syntax error fixer - fixes ALL fixable errors.
Handles all common patterns systematically.
"""

import json
import re
import ast
from pathlib import Path
from typing import List, Dict, Any, Tuple

BASE_DIR = Path(__file__).parent.parent

def fix_all_patterns(source_lines: List[str]) -> Tuple[List[str], List[str]]:
    """Fix all common syntax error patterns."""
    fixes = []
    new_lines = []
    i = 0
    
    while i < len(source_lines):
        line = source_lines[i]
        original_line = line
        
        # Pattern 1: Unclosed strings (most common)
        if i < len(source_lines) - 1:
            next_line = source_lines[i + 1]
            
            # Check if string is split across lines
            has_opening_quote = ('"' in line or "'" in line)
            has_closing_in_next = ('"' in next_line or "'" in next_line)
            has_text_in_next = bool(re.search(r'[\u0600-\u06FF\w\s]', next_line))
            
            if has_opening_quote and has_closing_in_next and has_text_in_next:
                # Count quotes
                single_quotes = line.count("'") - line.count("\\'")
                double_quotes = line.count('"') - line.count('\\"')
                
                # If odd number, string is unclosed
                if (single_quotes % 2 == 1) or (double_quotes % 2 == 1):
                    quote_char = '"' if double_quotes % 2 == 1 else "'"
                    # Merge lines
                    # Remove closing quote from next line and merge
                    next_cleaned = next_line.replace(quote_char, '', 1).lstrip()
                    merged = line.rstrip('\n') + '\\n' + next_cleaned
                    new_lines.append(merged)
                    fixes.append(f"Merged split string")
                    i += 2
                    continue
        
        # Pattern 2: Arabic text in code (not in string/comment)
        arabic_pattern = re.compile(r'[\u0600-\u06FF]+')
        if arabic_pattern.search(line) and not line.strip().startswith('#'):
            # Check if in string
            in_string = False
            quote_count = 0
            for char in line:
                if char in ['"', "'"]:
                    quote_count += 1
                    if quote_count % 2 == 1:
                        in_string = True
                    else:
                        in_string = False
            
            if not in_string and line.strip():
                # Comment it out
                line = '# ' + line.lstrip()
                fixes.append(f"Commented Arabic text")
        
        # Pattern 3: Fix ||v1|| patterns
        if '||v1||' in line or '||v2||' in line:
            line = re.sub(r'\|\|v1\|\|', 'abs(v1)', line)
            line = re.sub(r'\|\|v2\|\|', 'abs(v2)', line)
            if line != original_line:
                fixes.append("Fixed ||v1||/||v2||")
        
        # Pattern 4: Fix def__init__
        if 'def__init__' in line:
            line = line.replace('def__init__', 'def __init__')
            fixes.append("Fixed def__init__")
        
        new_lines.append(line)
        i += 1
    
    return new_lines, fixes

def fix_notebook_comprehensive(notebook_path: Path, dry_run: bool = False) -> Dict[str, Any]:
    """Comprehensively fix all syntax errors in a notebook."""
    fixes_applied = []
    
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
        
        cells = nb.get("cells", [])
        modified = False
        
        for i, cell in enumerate(cells):
            if cell.get("cell_type") != "code":
                continue
            
            source_lines = cell.get("source", [])
            source = "".join(source_lines)
            
            if not source.strip() or source.strip().startswith("!") or source.strip().startswith("%"):
                continue
            
            # Try to parse
            try:
                ast.parse(source)
                continue
            except SyntaxError:
                # Has error - fix it
                fixed_lines, cell_fixes = fix_all_patterns(source_lines)
                
                # Try parsing fixed version
                fixed_source = "".join(fixed_lines)
                try:
                    ast.parse(fixed_source)
                    # Success!
                    if not dry_run:
                        cell["source"] = fixed_lines
                        modified = True
                    fixes_applied.append({
                        "cell": i,
                        "fixes": cell_fixes
                    })
                except SyntaxError as e2:
                    # Still has error - try more aggressive fixes
                    # For now, mark for manual review
                    fixes_applied.append({
                        "cell": i,
                        "error": str(e2),
                        "fixes": cell_fixes,
                        "needs_manual_review": True
                    })
        
        if modified and not dry_run:
            with open(notebook_path, "w") as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
        
        return {
            "path": str(notebook_path.relative_to(BASE_DIR)),
            "modified": modified,
            "fixes_applied": fixes_applied
        }
    
    except Exception as e:
        return {
            "path": str(notebook_path.relative_to(BASE_DIR)),
            "error": str(e),
            "fixes_applied": []
        }

def main():
    """Main function."""
    import sys
    
    dry_run = "--dry-run" in sys.argv
    prioritize = "--prioritize" in sys.argv
    
    with open(BASE_DIR / "artifacts" / "syntax_errors_scan.json") as f:
        scan = json.load(f)
    
    notebooks_to_fix = [BASE_DIR / nb["path"] for nb in scan["errors"]]
    
    if prioritize:
        examples = [nb for nb in notebooks_to_fix if "/examples/" in str(nb)]
        exercises = [nb for nb in notebooks_to_fix if "/exercises/" in str(nb)]
        solutions = [nb for nb in notebooks_to_fix if "/solutions/" in str(nb) or "/SOLUTIONS/" in str(nb)]
        other = [nb for nb in notebooks_to_fix if nb not in examples + exercises + solutions]
        notebooks_to_fix = examples + exercises + solutions + other
        print(f"🔧 Fixing {len(notebooks_to_fix)} notebooks (prioritized)...")
    else:
        print(f"🔧 Fixing {len(notebooks_to_fix)} notebooks...")
    
    if dry_run:
        print("🔍 DRY RUN\n")
    
    fixed_count = 0
    total_fixes = 0
    manual_review = 0
    
    for nb_path in notebooks_to_fix:
        result = fix_notebook_comprehensive(nb_path, dry_run)
        if result.get("modified"):
            fixed_count += 1
            total_fixes += sum(len(f.get("fixes", [])) for f in result.get("fixes_applied", []))
        if any(f.get("needs_manual_review") for f in result.get("fixes_applied", [])):
            manual_review += 1
        if fixed_count <= 30:
            fixes = sum(len(f.get("fixes", [])) for f in result.get("fixes_applied", []))
            if fixes > 0:
                print(f"✅ {result['path']}: {fixes} fix(es)")
    
    print(f"\n✅ Fixed {fixed_count} notebooks ({total_fixes} total fixes)")
    if manual_review > 0:
        print(f"⚠️  {manual_review} notebooks need manual review")

if __name__ == "__main__":
    main()
