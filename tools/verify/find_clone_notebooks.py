#!/usr/bin/env python3
"""Gate: no groups of notebooks sharing byte-identical code cells.

Groups all Course */ notebooks by md5 of their concatenated code-cell
source. Any group of size > 1 with non-trivial code (>200 chars) fails
the gate (the 2025-era generator cloned one sklearn snippet under ~150
different official-topic titles; this must never come back).
"""
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

def main():
    groups = defaultdict(list)
    for p in sorted(REPO.glob("Course */**/*.ipynb")):
        if ".ipynb_checkpoints" in str(p):
            continue
        try:
            nb = json.loads(p.read_text())
        except Exception:
            continue
        src = "".join("".join(c.get("source", []))
                      for c in nb.get("cells", []) if c.get("cell_type") == "code")
        if len(src) <= 200:
            continue
        groups[hashlib.md5(src.encode()).hexdigest()].append(str(p.relative_to(REPO)))
    clones = {h: fs for h, fs in groups.items() if len(fs) > 1}
    if clones:
        print(f"CLONE GATE: {len(clones)} identical-code group(s)")
        for h, fs in clones.items():
            print(f"  md5 {h[:8]}:")
            for f in fs:
                print(f"    {f}")
        return 1
    print("Clone gate: no identical-code notebook groups. ✓")
    return 0

if __name__ == "__main__":
    sys.exit(main())
