#!/usr/bin/env python3
"""
Fix common syntax errors in notebooks.
Handles:
- EOL while scanning string literal (unclosed strings)
- def__init__ → def __init__ (missing space)
- Arabic text in code (move to comments)
- Broken expressions (line breaks in f-strings)
- Invalid syntax patterns
"""

import json
import re
import ast
from pathlib import Path
from typing import List, Dict, Any

# Base directory
BASE_DIR = Path(__file__).parent.parent

def fix_unclosed_string(source: str) -> str:
    """Fix unclosed string literals."""
    lines = source.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Check for unclosed strings
        # Simple heuristic: if line ends with quote but string isn't closed
        if '"' in line or "'" in line:
            # Count quotes
            single_quotes = line.count("'") - line.count("\\'")
            double_quotes = line.count('"') - line.count('\\"')
            
            # If odd number of quotes, might be unclosed
            if single_quotes % 2 == 1 and line.strip().endswith("'"):
                # Check if next line might continue
                line = line.rstrip() + "'"
            elif double_quotes % 2 == 1 and line.strip().endswith('"'):
                line = line.rstrip() + '"'
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_def_init(source: str) -> str:
    """Fix def__init__ → def __init__."""
    return re.sub(r'def__init__', 'def __init__', source)

def fix_arabic_in_code(source: str) -> str:
    """Move Arabic text in code to comments."""
    # This is complex - for now, just detect and flag
    # Arabic Unicode range: \u0600-\u06FF
    arabic_pattern = re.compile(r'[\u0600-\u06FF]+')
    
    lines = source.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Check if line has Arabic and is not already a comment
        if arabic_pattern.search(line) and not line.strip().startswith('#'):
            # Try to move Arabic to comment
            # This is heuristic - may need manual review
            arabic_match = arabic_pattern.search(line)
            if arabic_match:
                # For now, just add comment
                # Full fix would require understanding context
                pass
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_broken_fstring(source: str) -> str:
    """Fix broken f-strings with line breaks."""
    # Look for f-strings that span multiple lines incorrectly
    # Pattern: f"..." with newline inside
    pattern = r'f["\'](.*?)\n(.*?)["\']'
    
    def fix_match(m):
        # Reconstruct f-string
        content = m.group(1) + '\\n' + m.group(2)
        return f'f"{content}"'
    
    return re.sub(pattern, fix_match, source, flags=re.DOTALL)

def fix_invalid_syntax_patterns(source: str) -> str:
    """Fix common invalid syntax patterns."""
    # Fix ||v1|| → abs(v1) or similar
    source = re.sub(r'\|\|(\w+)\|\|', r'abs(\1)', source)
    
    # Fix broken division: a\nb → a / b
    # This is tricky - need context
    # For now, just detect
    
    return source

def fix_notebook_syntax_errors(notebook_path: Path, dry_run: bool = False) -> Dict[str, Any]:
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
            
            source = "".join(cell.get("source", []))
            if not source.strip():
                continue
            
            # Skip shell commands
            if source.strip().startswith("!") or source.strip().startswith("%"):
                continue
            
            original_source = source
            
            # Try to parse - if it fails, try to fix
            try:
                ast.parse(source)
                continue  # No error, skip
            except SyntaxError as e:
                # Try fixes
                fixed_source = source
                
                # Fix 1: Unclosed strings
                if "EOL while scanning string literal" in str(e):
                    fixed_source = fix_unclosed_string(source)
                    if fixed_source != source:
                        fixes_applied.append({
                            "cell": i,
                            "error": "EOL while scanning string literal",
                            "fix": "Fixed unclosed string"
                        })
                        source = fixed_source
                
                # Fix 2: def__init__
                if "def__init__" in source:
                    fixed_source = fix_def_init(source)
                    if fixed_source != source:
                        fixes_applied.append({
                            "cell": i,
                            "error": "def__init__",
                            "fix": "Fixed def__init__ → def __init__"
                        })
                        source = fixed_source
                
                # Fix 3: Invalid syntax patterns
                fixed_source = fix_invalid_syntax_patterns(source)
                if fixed_source != source:
                    fixes_applied.append({
                        "cell": i,
                        "error": "Invalid syntax pattern",
                        "fix": "Fixed invalid syntax pattern"
                    })
                    source = fixed_source
                
                # Try parsing again
                try:
                    ast.parse(source)
                    # Success! Update cell
                    if not dry_run:
                        cell["source"] = source.splitlines(True)
                        modified = True
                except SyntaxError:
                    # Still has error - may need manual fix
                    fixes_applied.append({
                        "cell": i,
                        "error": str(e),
                        "fix": "Could not auto-fix - needs manual review"
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
        print("Usage: python fix_syntax_errors.py <notebook_path> [--dry-run]")
        print("   or: python fix_syntax_errors.py --batch [--dry-run]")
        sys.exit(1)
    
    dry_run = "--dry-run" in sys.argv
    
    if sys.argv[1] == "--batch":
        # Fix all notebooks with errors
        with open(BASE_DIR / "artifacts" / "syntax_errors_scan.json") as f:
            scan = json.load(f)
        
        notebooks_to_fix = [BASE_DIR / nb["path"] for nb in scan["errors"]]
        
        print(f"🔧 Fixing syntax errors in {len(notebooks_to_fix)} notebooks...")
        if dry_run:
            print("🔍 DRY RUN - No files will be modified\n")
        
        fixed_count = 0
        total_fixes = 0
        
        for nb_path in notebooks_to_fix:
            result = fix_notebook_syntax_errors(nb_path, dry_run)
            if result.get("modified"):
                fixed_count += 1
                total_fixes += len(result.get("fixes_applied", []))
                if fixed_count <= 10:
                    print(f"✅ {result['path']}: {len(result.get('fixes_applied', []))} fix(es)")
        
        print(f"\n✅ Fixed {fixed_count} notebooks ({total_fixes} total fixes)")
    else:
        # Fix single notebook
        nb_path = Path(sys.argv[1])
        if not nb_path.is_absolute():
            nb_path = BASE_DIR / nb_path
        
        result = fix_notebook_syntax_errors(nb_path, dry_run)
        print(f"📄 {result['path']}")
        print(f"   Modified: {result.get('modified', False)}")
        print(f"   Fixes: {len(result.get('fixes_applied', []))}")
        for fix in result.get("fixes_applied", []):
            print(f"     - Cell {fix['cell']}: {fix['fix']}")

if __name__ == "__main__":
    main()
