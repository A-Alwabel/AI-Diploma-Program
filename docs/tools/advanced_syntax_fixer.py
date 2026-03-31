#!/usr/bin/env python3
"""
Advanced syntax error fixer - handles more complex patterns.
Fixes:
- Unclosed strings (EOL while scanning string literal)
- Unexpected indent
- Invalid syntax patterns
- Arabic text in code
- Broken expressions
"""

import json
import re
import ast
from pathlib import Path
from typing import List, Dict, Any, Tuple

BASE_DIR = Path(__file__).parent.parent

def fix_unclosed_strings_advanced(source_lines: List[str]) -> Tuple[List[str], List[str]]:
    """Advanced fix for unclosed strings."""
    fixes = []
    new_lines = []
    i = 0
    
    while i < len(source_lines):
        line = source_lines[i]
        
        # Check for unclosed string patterns
        if i < len(source_lines) - 1:
            next_line = source_lines[i + 1]
            
            # Pattern: Line has opening quote, next line has Arabic/text + closing quote
            has_quote = '"' in line or "'" in line
            has_arabic_or_text = bool(re.search(r'[\u0600-\u06FF\w]', next_line))
            has_closing = '"' in next_line or "'" in next_line
            
            if has_quote and has_arabic_or_text and has_closing:
                # Check quote balance
                single_quotes = line.count("'") - line.count("\\'")
                double_quotes = line.count('"') - line.count('\\"')
                
                if (single_quotes % 2 == 1) or (double_quotes % 2 == 1):
                    # Merge with \n
                    quote_char = '"' if double_quotes % 2 == 1 else "'"
                    # Extract the closing quote and text from next line
                    next_text = next_line
                    if quote_char in next_text:
                        # Merge properly
                        merged = line.rstrip('\n') + '\\n' + next_text.replace(quote_char, '', 1).lstrip()
                        new_lines.append(merged)
                        fixes.append(f"Merged split string at line {i+1}")
                        i += 2
                        continue
        
        new_lines.append(line)
        i += 1
    
    return new_lines, fixes

def fix_unexpected_indent(source: str) -> str:
    """Fix unexpected indent errors."""
    lines = source.split('\n')
    fixed_lines = []
    indent_stack = [0]  # Track indentation levels
    
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if not stripped or stripped.startswith('#'):
            fixed_lines.append(line)
            continue
        
        # Calculate expected indent
        current_indent = len(line) - len(stripped)
        
        # Check if line should be indented based on previous context
        if i > 0:
            prev_line = lines[i-1].rstrip()
            # If previous line ends with :, next line should be indented
            if prev_line.endswith(':'):
                expected_indent = indent_stack[-1] + 4
                if current_indent < expected_indent and current_indent == 0:
                    # Fix: add proper indent
                    fixed_lines.append(' ' * expected_indent + stripped)
                    indent_stack.append(expected_indent)
                    continue
        
        fixed_lines.append(line)
        if stripped and not stripped.startswith('#'):
            indent_stack.append(current_indent)
    
    return '\n'.join(fixed_lines)

def fix_arabic_in_code_advanced(source_lines: List[str]) -> Tuple[List[str], List[str]]:
    """Fix Arabic text that's in code (not in strings/comments)."""
    fixes = []
    new_lines = []
    arabic_pattern = re.compile(r'[\u0600-\u06FF]+')
    
    for i, line in enumerate(source_lines):
        # Check if line has Arabic and is not in comment/string
        if arabic_pattern.search(line):
            stripped = line.strip()
            
            # Skip if already a comment
            if stripped.startswith('#'):
                new_lines.append(line)
                continue
            
            # Check if in string
            in_string = False
            quote_char = None
            for char in line:
                if char in ['"', "'"] and (not quote_char or char == quote_char):
                    in_string = not in_string
                    quote_char = char if in_string else None
            
            if not in_string and stripped:
                # Arabic text in code - comment it out
                # But check context: if it's standalone, might be a label
                if i > 0 and source_lines[i-1].strip().endswith(':'):
                    # Might be part of a structure - check
                    pass
                
                # For now, comment it out
                new_lines.append('# ' + line.lstrip())
                fixes.append(f"Commented Arabic text at line {i+1}")
                continue
        
        new_lines.append(line)
    
    return new_lines, fixes

def fix_notebook_advanced(notebook_path: Path, dry_run: bool = False) -> Dict[str, Any]:
    """Advanced fix for syntax errors."""
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
            except SyntaxError as e:
                cell_fixes = []
                original_source = source
                
                # Fix 1: Unclosed strings (advanced)
                if "EOL while scanning string literal" in str(e):
                    fixed_lines, line_fixes = fix_unclosed_strings_advanced(source_lines)
                    if fixed_lines != source_lines:
                        source_lines = fixed_lines
                        source = "".join(source_lines)
                        cell_fixes.extend(line_fixes)
                
                # Fix 2: Unexpected indent
                if "unexpected indent" in str(e) or "expected an indented block" in str(e):
                    fixed_source = fix_unexpected_indent(source)
                    if fixed_source != source:
                        source = fixed_source
                        source_lines = source.splitlines(True)
                        cell_fixes.append("Fixed unexpected indent")
                
                # Fix 3: Arabic in code
                fixed_lines, arabic_fixes = fix_arabic_in_code_advanced(source_lines)
                if fixed_lines != source_lines:
                    source_lines = fixed_lines
                    source = "".join(source_lines)
                    cell_fixes.extend(arabic_fixes)
                
                # Fix 4: Invalid patterns
                fixed_source = source
                # Fix ||v1|| patterns
                fixed_source = re.sub(r'\|\|v1\|\|', 'abs(v1)', fixed_source)
                fixed_source = re.sub(r'\|\|v2\|\|', 'abs(v2)', fixed_source)
                # Fix def__init__
                fixed_source = re.sub(r'def__init__', 'def __init__', fixed_source)
                # Fix broken division
                fixed_source = re.sub(r'(\w+)\s*\n\s*(\w+)(?=\s*[,\])])', r'\1 / \2', fixed_source)
                
                if fixed_source != source:
                    source = fixed_source
                    source_lines = source.splitlines(True)
                    cell_fixes.append("Fixed invalid syntax patterns")
                
                # Try parsing again
                try:
                    ast.parse(source)
                    if not dry_run:
                        cell["source"] = source_lines
                        modified = True
                    fixes_applied.append({
                        "cell": i,
                        "fixes": cell_fixes
                    })
                except SyntaxError as e2:
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
    
    if len(sys.argv) < 2:
        print("Usage: python advanced_syntax_fixer.py --batch [--prioritize] [--dry-run]")
        sys.exit(1)
    
    dry_run = "--dry-run" in sys.argv
    prioritize = "--prioritize" in sys.argv
    
    with open(BASE_DIR / "artifacts" / "syntax_errors_scan.json") as f:
        scan = json.load(f)
    
    notebooks_to_fix = [BASE_DIR / nb["path"] for nb in scan["errors"]]
    
    if prioritize:
        # Prioritize: examples > exercises > solutions
        examples = [nb for nb in notebooks_to_fix if "/examples/" in str(nb)]
        exercises = [nb for nb in notebooks_to_fix if "/exercises/" in str(nb)]
        solutions = [nb for nb in notebooks_to_fix if "/solutions/" in str(nb) or "/SOLUTIONS/" in str(nb)]
        other = [nb for nb in notebooks_to_fix if nb not in examples + exercises + solutions]
        notebooks_to_fix = examples + exercises + solutions + other
        print(f"🔧 Fixing {len(notebooks_to_fix)} notebooks (prioritized: {len(examples)} examples, {len(exercises)} exercises)...")
    else:
        print(f"🔧 Fixing {len(notebooks_to_fix)} notebooks...")
    
    if dry_run:
        print("🔍 DRY RUN - No files will be modified\n")
    
    fixed_count = 0
    total_fixes = 0
    manual_review = 0
    
    for nb_path in notebooks_to_fix:
        result = fix_notebook_advanced(nb_path, dry_run)
        if result.get("modified"):
            fixed_count += 1
            total_fixes += sum(len(f.get("fixes", [])) for f in result.get("fixes_applied", []))
        if any(f.get("needs_manual_review") for f in result.get("fixes_applied", [])):
            manual_review += 1
        if fixed_count <= 20:
            fixes = sum(len(f.get("fixes", [])) for f in result.get("fixes_applied", []))
            if fixes > 0:
                print(f"✅ {result['path']}: {fixes} fix(es)")
    
    print(f"\n✅ Fixed {fixed_count} notebooks ({total_fixes} total fixes)")
    if manual_review > 0:
        print(f"⚠️  {manual_review} notebooks need manual review")

if __name__ == "__main__":
    main()
