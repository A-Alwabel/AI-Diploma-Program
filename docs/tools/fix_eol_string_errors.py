#!/usr/bin/env python3
"""
Fix EOL (End of Line) string literal errors.
These occur when strings are incorrectly split across lines.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def fix_split_strings(source: str) -> str:
    """Fix strings that were incorrectly split across lines."""
    lines = source.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Pattern 1: print(" followed by newline and text on next line
        if re.match(r'^\s*print\("', line):
            # Collect continuation lines until we find the closing quote
            full_line = line
            i += 1
            while i < len(lines) and '"' not in full_line:
                next_line = lines[i]
                # Skip single character lines that are part of split string
                if len(next_line.strip()) == 1 and next_line.strip().isalpha():
                    full_line += next_line.strip()
                elif next_line.strip().startswith('"'):
                    full_line += next_line.strip()
                elif '"' in next_line:
                    # Found closing quote
                    full_line += ' ' + next_line.strip()
                else:
                    full_line += ' ' + next_line.strip()
                i += 1
            fixed_lines.append(full_line)
            continue
        
        # Pattern 2: # comment_word split: # comment_w\no\nr\nd
        if re.match(r'^#\s*[^_]+_[a-z]', line):
            # Merge with following single-character lines
            full_line = line
            i += 1
            while i < len(lines) and len(lines[i].strip()) == 1 and lines[i].strip().isalpha():
                full_line = full_line.rstrip('_') + lines[i].strip() + '_'
                i += 1
            # Remove trailing underscore and add space
            full_line = full_line.rstrip('_') + ' '
            fixed_lines.append(full_line)
            continue
        
        # Pattern 3: String with split characters: "text\nx\ny\nz"
        if '"' in line and not line.strip().endswith('"'):
            # Try to merge with following lines
            full_line = line
            i += 1
            quote_count = line.count('"')
            while i < len(lines) and quote_count % 2 == 1:
                next_line = lines[i]
                full_line += next_line.strip()
                quote_count += next_line.count('"')
                i += 1
            fixed_lines.append(full_line)
            continue
        
        fixed_lines.append(line)
        i += 1
    
    return '\n'.join(fixed_lines)

def fix_notebook(notebook_path: Path) -> bool:
    """Fix EOL string errors in a notebook."""
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
        
        modified = False
        
        for cell in nb.get("cells", []):
            if cell.get("cell_type") != "code":
                continue
            
            source = "".join(cell.get("source", []))
            if not source.strip():
                continue
            
            original_source = source
            source = fix_split_strings(source)
            
            if source != original_source:
                cell["source"] = source.splitlines(keepends=True)
                modified = True
        
        if modified:
            with open(notebook_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
        
        return False
    
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
        return False

def main():
    """Main function."""
    print("🔧 Fixing EOL string literal errors...\n")
    
    # Read error report
    error_report_path = BASE_DIR / "artifacts" / "syntax_errors_scan.json"
    if not error_report_path.exists():
        print(f"❌ Error report not found: {error_report_path}")
        return
    
    with open(error_report_path) as f:
        error_data = json.load(f)
    
    # Find notebooks with EOL errors
    notebooks_to_fix = []
    for err in error_data.get("errors", []):
        for error in err.get("errors", []):
            if error.get("message") == "EOL while scanning string literal":
                nb_path = BASE_DIR / err["path"]
                if nb_path.exists() and nb_path not in notebooks_to_fix:
                    notebooks_to_fix.append(nb_path)
                break
    
    print(f"✅ Found {len(notebooks_to_fix)} notebooks with EOL errors\n")
    
    fixed_count = 0
    
    for nb_path in notebooks_to_fix:
        if fix_notebook(nb_path):
            fixed_count += 1
            print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
    
    print(f"\n✅ Fixed {fixed_count}/{len(notebooks_to_fix)} notebooks")

if __name__ == "__main__":
    main()
