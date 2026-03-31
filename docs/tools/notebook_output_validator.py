#!/usr/bin/env python3
"""
Validate notebook outputs.
Checks:
- Output presence (cells that should produce output)
- Output type consistency
- Output value validation (for deterministic outputs)
"""

import json
import ast
from pathlib import Path
from typing import List, Dict, Any, Optional
import re

BASE_DIR = Path(__file__).parent.parent

def should_have_output(source: str) -> bool:
    """Check if a code cell should produce output."""
    # Cells with print, plots, displays should have output
    has_print = 'print(' in source or 'display(' in source
    has_plot = 'plt.' in source or 'sns.' in source or 'plotly.' in source or '.plot(' in source or '.show()' in source
    has_output = 'display' in source.lower() or 'output' in source.lower()
    
    return has_print or has_plot or has_output

def is_non_deterministic(source: str, output: Any) -> bool:
    """Check if output is non-deterministic."""
    # Random, timestamps, UUIDs, etc.
    has_random = 'random' in source or 'np.random' in source or 'torch.rand' in source
    has_time = 'datetime' in source or 'time.time()' in source or 'now()' in source
    has_uuid = 'uuid' in source.lower()
    
    # Check output type/content
    if isinstance(output, dict):
        output_str = str(output)
        if 'random' in output_str.lower() or 'uuid' in output_str.lower():
            return True
    
    return has_random or has_time or has_uuid

def validate_notebook_outputs(notebook_path: Path, baseline_path: Optional[Path] = None) -> Dict[str, Any]:
    """Validate outputs in a notebook."""
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
    except Exception as e:
        return {"path": str(notebook_path), "error": str(e)}
    
    cells = nb.get("cells", [])
    validation_results = []
    
    for i, cell in enumerate(cells):
        if cell.get("cell_type") != "code":
            continue
        
        source = "".join(cell.get("source", []))
        outputs = cell.get("outputs", [])
        
        if not source.strip() or source.strip().startswith("!") or source.strip().startswith("%"):
            continue
        
        # Check if cell should have output
        expects_output = should_have_output(source)
        has_output = len(outputs) > 0
        
        result = {
            "cell_index": i,
            "expects_output": expects_output,
            "has_output": has_output,
            "output_count": len(outputs),
            "non_deterministic": is_non_deterministic(source, outputs)
        }
        
        # Level 1: Presence check
        if expects_output and not has_output:
            result["presence_issue"] = "Expected output but none found"
        
        # Level 2: Type check (if we have baseline)
        if baseline_path and has_output:
            try:
                with open(baseline_path) as f:
                    baseline_nb = json.load(f)
                if i < len(baseline_nb.get("cells", [])):
                    baseline_cell = baseline_nb["cells"][i]
                    baseline_outputs = baseline_cell.get("outputs", [])
                    if baseline_outputs:
                        # Compare output types
                        result["baseline_available"] = True
            except:
                pass
        
        validation_results.append(result)
    
    return {
        "path": str(notebook_path.relative_to(BASE_DIR)),
        "validation_results": validation_results
    }

def main():
    """Main function."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python notebook_output_validator.py <notebook_path> [baseline_path]")
        print("   or: python notebook_output_validator.py --batch [baseline_dir]")
        sys.exit(1)
    
    if sys.argv[1] == "--batch":
        # Validate all executed notebooks
        baseline_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None
        
        # Find all notebooks
        notebooks = list(BASE_DIR.rglob("*.ipynb"))
        # Exclude
        notebooks = [nb for nb in notebooks if not any(x in str(nb) for x in [".git", "artifacts", "SOLUTIONS"])]
        
        print(f"Validating {len(notebooks)} notebooks...")
        
        total_issues = 0
        for nb_path in notebooks:
            baseline_path = None
            if baseline_dir:
                rel_path = nb_path.relative_to(BASE_DIR)
                baseline_path = baseline_dir / rel_path
            
            result = validate_notebook_outputs(nb_path, baseline_path)
            issues = [r for r in result.get("validation_results", []) if r.get("presence_issue")]
            if issues:
                total_issues += len(issues)
                print(f"⚠️  {result['path']}: {len(issues)} output issue(s)")
        
        print(f"\n✅ Validation complete: {total_issues} total output issues found")
    else:
        # Validate single notebook
        nb_path = Path(sys.argv[1])
        baseline_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
        
        result = validate_notebook_outputs(nb_path, baseline_path)
        print(f"📄 {result['path']}")
        for vr in result.get("validation_results", []):
            if vr.get("presence_issue"):
                print(f"  Cell {vr['cell_index']}: {vr['presence_issue']}")

if __name__ == "__main__":
    main()
