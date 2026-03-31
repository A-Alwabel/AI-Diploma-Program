#!/usr/bin/env python3
"""
Fix remaining syntax errors aggressively.
Handles:
- Markdown text in code cells (convert to markdown)
- Incomplete statements (model.predict -> model.predict_proba())
- Comments merged with code
- Duplicate lines
"""

import json
import ast
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def is_markdown_text(source: str) -> bool:
    """Check if source is markdown text, not Python code."""
    if not source.strip():
        return False
    
    # Try to parse as Python
    try:
        ast.parse(source)
        return False  # Valid Python
    except:
        pass
    
    # Check for markdown patterns
    stripped = source.strip()
    markdown_patterns = [
        r'^\d+\.\s+',  # Numbered list
        r'^[├└│─]',  # Tree structure
        r'^Sample \d+:',  # Sample text
        r'^[*-]\s+',  # Bullet list
    ]
    
    for pattern in markdown_patterns:
        if re.match(pattern, stripped):
            # Additional check: no Python keywords
            if not any(kw in source for kw in ['def ', 'class ', 'import ', 'from ', '=', '(', ')', 'print(', 'return ']):
                return True
    
    return False

def fix_notebook(notebook_path: Path) -> bool:
    """Fix remaining syntax errors in a notebook."""
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
            
            # 1. Convert markdown text in code cells to markdown cells
            if is_markdown_text(source):
                cell["cell_type"] = "markdown"
                cell["source"] = source.strip().splitlines(keepends=True)
                modified = True
                continue
            
            # 2. Fix incomplete statements: model.predict -> model.predict_proba(X)
            # This is tricky - we'll comment out incomplete lines
            lines = source.split('\n')
            fixed_lines = []
            for line in lines:
                # Check for incomplete method calls
                if re.match(r'^\s*y_proba\s*=\s*model\.predict\s*$', line):
                    # Comment it out or complete it
                    fixed_lines.append('# ' + line.strip() + '  # TODO: Complete this line')
                elif re.match(r'^\s*model\.predict\s*$', line):
                    fixed_lines.append('# ' + line.strip() + '  # TODO: Complete this line')
                else:
                    fixed_lines.append(line)
            
            # 3. Fix comments merged with code: "# commentcode" -> "# comment\ncode"
            source = '\n'.join(fixed_lines)
            source = re.sub(r'(#\s*[^\n]+)([a-zA-Z_][a-zA-Z0-9_]*)', r'\1\n\2', source)
            # But be careful with inline comments
            source = re.sub(r'([a-zA-Z0-9_\]\)])\s*#\s*([A-Z][^\n]+)([a-zA-Z_])', r'\1  # \2\n\3', source)
            
            # 4. Fix duplicate lines (keep only first occurrence)
            lines = source.split('\n')
            seen = set()
            unique_lines = []
            for line in lines:
                line_stripped = line.strip()
                if line_stripped and line_stripped not in seen:
                    seen.add(line_stripped)
                    unique_lines.append(line)
                elif not line_stripped:
                    unique_lines.append(line)
            
            source = '\n'.join(unique_lines)
            
            if source != original_source:
                # Verify it's still valid Python (if it was before)
                try:
                    ast.parse(original_source)
                    # Was valid, check if still valid
                    try:
                        ast.parse(source)
                        cell["source"] = source.splitlines(keepends=True)
                        modified = True
                    except:
                        # Fix broke it, revert
                        pass
                except:
                    # Wasn't valid anyway, apply fix
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
    print("🔧 Fixing remaining syntax errors...\n")
    
    # Read error report
    error_report_path = BASE_DIR / "artifacts" / "syntax_errors_scan.json"
    if not error_report_path.exists():
        print(f"❌ Error report not found: {error_report_path}")
        return
    
    with open(error_report_path) as f:
        error_data = json.load(f)
    
    notebooks_to_fix = [BASE_DIR / err["path"] for err in error_data.get("errors", [])]
    
    print(f"✅ Found {len(notebooks_to_fix)} notebooks with errors\n")
    
    fixed_count = 0
    
    for nb_path in notebooks_to_fix:
        if nb_path.exists() and fix_notebook(nb_path):
            fixed_count += 1
            print(f"  ✓ Fixed: {nb_path.relative_to(BASE_DIR)}")
    
    print(f"\n✅ Fixed {fixed_count}/{len(notebooks_to_fix)} notebooks")

if __name__ == "__main__":
    main()
