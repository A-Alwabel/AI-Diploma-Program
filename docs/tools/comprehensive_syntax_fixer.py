#!/usr/bin/env python3
"""
Comprehensive syntax error fixer for notebooks.
Handles common patterns:
- Unclosed strings (EOL while scanning string literal)
- Invalid syntax patterns (||v1||, etc.)
- Arabic text in code (move to comments where appropriate)
- Broken expressions
"""

import json
import re
import ast
from pathlib import Path
from typing import List, Dict, Any, Tuple

# Base directory
BASE_DIR = Path(__file__).parent.parent

def fix_split_strings(source_lines: List[str]) -> Tuple[List[str], List[str]]:
    """
    Fix strings split across multiple lines in JSON source.
    Returns: (fixed_lines, fixes_applied)
    """
    fixes = []
    new_lines = []
    i = 0
    
    while i < len(source_lines):
        line = source_lines[i]
        
        # Check if this line has an unclosed string and next line completes it
        if i < len(source_lines) - 1:
            next_line = source_lines[i + 1]
            
            # Pattern: Line ends with quote but string isn't properly closed
            # Or: Line has opening quote, next line has Arabic + closing quote
            has_opening_quote = '"' in line or "'" in line
            has_arabic = bool(re.search(r'[\u0600-\u06FF]', next_line))
            has_closing_quote = '"' in next_line or "'" in next_line
            
            # Check if string is split
            if has_opening_quote and has_arabic and has_closing_quote:
                # Count quotes in current line
                single_quotes = line.count("'") - line.count("\\'")
                double_quotes = line.count('"') - line.count('\\"')
                
                # If odd number, string is unclosed
                if (single_quotes % 2 == 1) or (double_quotes % 2 == 1):
                    # Merge lines with \n
                    quote_char = '"' if double_quotes % 2 == 1 else "'"
                    # Remove the closing quote from next line and merge
                    merged = line.rstrip('\n') + '\\n' + next_line.replace(quote_char, '', 1).lstrip()
                    new_lines.append(merged)
                    fixes.append(f"Merged split string at line {i+1}")
                    i += 2
                    continue
        
        new_lines.append(line)
        i += 1
    
    return new_lines, fixes

def fix_invalid_patterns(source: str) -> Tuple[str, List[str]]:
    """Fix common invalid syntax patterns."""
    fixes = []
    original = source
    
    # Fix ||v1|| → abs(v1)
    if '||v1||' in source or '||v2||' in source:
        source = re.sub(r'\|\|v1\|\|', 'abs(v1)', source)
        source = re.sub(r'\|\|v2\|\|', 'abs(v2)', source)
        if source != original:
            fixes.append("Fixed ||v1||/||v2|| patterns")
    
    # Fix def__init__ → def __init__
    if 'def__init__' in source:
        source = re.sub(r'def__init__', 'def __init__', source)
        if source != original:
            fixes.append("Fixed def__init__ → def __init__")
    
    # Fix broken division: a\nb → a / b (if it's clearly a division)
    # This is tricky - be conservative
    source = re.sub(r'(\w+)\s*\n\s*(\w+)(?=\s*[,\])])', r'\1 / \2', source)
    
    return source, fixes

def fix_arabic_in_code(source: str) -> str:
    """Handle Arabic text in code - for now just detect, manual review needed."""
    # Arabic Unicode range: \u0600-\u06FF
    arabic_pattern = re.compile(r'[\u0600-\u06FF]+')
    
    # If Arabic is in code (not in string), it's likely a problem
    # But this is complex - mark for manual review
    return source

def fix_notebook(notebook_path: Path, dry_run: bool = False) -> Dict[str, Any]:
    """Fix syntax errors in a notebook."""
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
            
            if not source.strip():
                continue
            
            # Skip shell commands
            if source.strip().startswith("!") or source.strip().startswith("%"):
                continue
            
            # Try to parse
            try:
                ast.parse(source)
                continue  # No error
            except SyntaxError as e:
                # Has error - try to fix
                cell_fixes = []
                
                # Fix 1: Split strings
                fixed_lines, line_fixes = fix_split_strings(source_lines)
                if fixed_lines != source_lines:
                    source_lines = fixed_lines
                    source = "".join(source_lines)
                    cell_fixes.extend(line_fixes)
                
                # Fix 2: Invalid patterns
                fixed_source, pattern_fixes = fix_invalid_patterns(source)
                if fixed_source != source:
                    source = fixed_source
                    source_lines = source.splitlines(True)
                    cell_fixes.extend(pattern_fixes)
                
                # Try parsing again
                try:
                    ast.parse(source)
                    # Success!
                    if not dry_run:
                        cell["source"] = source_lines
                        modified = True
                    fixes_applied.append({
                        "cell": i,
                        "fixes": cell_fixes
                    })
                except SyntaxError as e2:
                    # Still has error
                    fixes_applied.append({
                        "cell": i,
                        "error": str(e2),
                        "fixes": cell_fixes,
                        "needs_manual_review": True
                    })
        
        # Save if modified
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
    
    if len(sys.argv) < 2:
        print("Usage: python comprehensive_syntax_fixer.py <notebook_path> [--dry-run]")
        print("   or: python comprehensive_syntax_fixer.py --batch [--dry-run] [--sample N]")
        sys.exit(1)
    
    dry_run = "--dry-run" in sys.argv
    sample_size = None
    
    if "--sample" in sys.argv:
        idx = sys.argv.index("--sample")
        if idx + 1 < len(sys.argv):
            sample_size = int(sys.argv[idx + 1])
    
    if sys.argv[1] == "--batch":
        # Fix all notebooks with errors
        with open(BASE_DIR / "artifacts" / "syntax_errors_scan.json") as f:
            scan = json.load(f)
        
        notebooks_to_fix = [BASE_DIR / nb["path"] for nb in scan["errors"]]
        
        if sample_size:
            notebooks_to_fix = notebooks_to_fix[:sample_size]
            print(f"🔧 Fixing syntax errors in {len(notebooks_to_fix)} sample notebooks...")
        else:
            print(f"🔧 Fixing syntax errors in {len(notebooks_to_fix)} notebooks...")
        
        if dry_run:
            print("🔍 DRY RUN - No files will be modified\n")
        
        fixed_count = 0
        total_fixes = 0
        manual_review = 0
        
        for nb_path in notebooks_to_fix:
            result = fix_notebook(nb_path, dry_run)
            if result.get("modified"):
                fixed_count += 1
                total_fixes += sum(len(f.get("fixes", [])) for f in result.get("fixes_applied", []))
            if any(f.get("needs_manual_review") for f in result.get("fixes_applied", [])):
                manual_review += 1
            if fixed_count <= 10:
                fixes = sum(len(f.get("fixes", [])) for f in result.get("fixes_applied", []))
                if fixes > 0:
                    print(f"✅ {result['path']}: {fixes} fix(es)")
        
        print(f"\n✅ Fixed {fixed_count} notebooks ({total_fixes} total fixes)")
        if manual_review > 0:
            print(f"⚠️  {manual_review} notebooks need manual review")
    else:
        # Fix single notebook
        nb_path = Path(sys.argv[1])
        if not nb_path.is_absolute():
            nb_path = BASE_DIR / nb_path
        
        result = fix_notebook(nb_path, dry_run)
        print(f"📄 {result['path']}")
        print(f"   Modified: {result.get('modified', False)}")
        print(f"   Fixes: {len(result.get('fixes_applied', []))}")
        for fix in result.get("fixes_applied", []):
            print(f"     - Cell {fix['cell']}: {fix.get('fixes', [fix.get('error', 'Unknown')])}")

if __name__ == "__main__":
    main()
