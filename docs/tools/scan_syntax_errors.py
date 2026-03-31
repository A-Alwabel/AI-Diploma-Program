#!/usr/bin/env python3
"""
Scan all notebooks for syntax errors.
Identifies actual Python syntax errors (not env/deps issues).
"""

import json
import ast
import os
from pathlib import Path
from typing import List, Dict, Any

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Exclude directories
EXCLUDE_DIRS = {
    ".git", "__pycache__", ".ipynb_checkpoints",
    "artifacts", "node_modules", ".venv", "venv", "SOLUTIONS_ALL"
}

def find_all_notebooks(base_dir: Path) -> List[Path]:
    """Find all .ipynb files."""
    notebooks = []
    for nb_path in base_dir.rglob("*.ipynb"):
        if any(excluded in nb_path.parts for excluded in EXCLUDE_DIRS):
            continue
        notebooks.append(nb_path)
    return sorted(notebooks)

def check_syntax(notebook_path: Path) -> List[Dict[str, Any]]:
    """Check notebook for syntax errors."""
    errors = []
    
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
        
        for i, cell in enumerate(nb.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            
            source = "".join(cell.get("source", []))
            if not source.strip():
                continue
            
            # Skip shell commands and magic commands
            if source.strip().startswith("!") or source.strip().startswith("%"):
                continue
            
            # Try to parse
            try:
                ast.parse(source)
            except SyntaxError as e:
                errors.append({
                    "cell_index": i,
                    "line": e.lineno,
                    "offset": e.offset,
                    "message": e.msg,
                    "text": e.text,
                    "source_preview": source[:200] if len(source) > 200 else source
                })
    except Exception as e:
        errors.append({
            "cell_index": -1,
            "error": f"Failed to read notebook: {str(e)}"
        })
    
    return errors

def main():
    """Main function."""
    print("🔍 Scanning all notebooks for syntax errors...\n")
    
    notebooks = find_all_notebooks(BASE_DIR)
    print(f"✅ Found {len(notebooks)} notebooks to scan\n")
    
    all_errors = []
    checked = 0
    
    for nb_path in notebooks:
        checked += 1
        if checked % 100 == 0:
            print(f"  Checked {checked}/{len(notebooks)} notebooks...")
        
        errors = check_syntax(nb_path)
        if errors:
            all_errors.append({
                "path": str(nb_path.relative_to(BASE_DIR)),
                "errors": errors
            })
    
    print(f"\n✅ Scan complete!")
    print(f"📊 Results:")
    print(f"  - Notebooks checked: {checked}")
    print(f"  - Notebooks with syntax errors: {len(all_errors)}")
    print(f"  - Total errors: {sum(len(e['errors']) for e in all_errors)}")
    
    # Save report
    report_path = BASE_DIR / "artifacts" / "syntax_errors_scan.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_path, "w") as f:
        json.dump({
            "timestamp": str(Path(__file__).stat().st_mtime),
            "total_notebooks": checked,
            "notebooks_with_errors": len(all_errors),
            "total_errors": sum(len(e['errors']) for e in all_errors),
            "errors": all_errors
        }, f, indent=2)
    
    print(f"\n📄 Report saved: {report_path}")
    
    # Print summary
    if all_errors:
        print(f"\n⚠️  Notebooks with syntax errors (first 10):")
        for err in all_errors[:10]:
            print(f"  - {err['path']}: {len(err['errors'])} error(s)")
            for e in err['errors'][:1]:
                print(f"    Cell {e['cell_index']}, line {e.get('line', '?')}: {e.get('message', 'Unknown')}")
        if len(all_errors) > 10:
            print(f"  ... and {len(all_errors) - 10} more")

if __name__ == "__main__":
    main()
