#!/usr/bin/env python3
"""
Replace **Books:** / **Papers:** / **State-of-the-Art:** inside the
References ``display(Markdown(r\"\"\" ... \"\"\"))`` block with ### headings.

If that markdown is accidentally run as Python, lines starting with ``##`` or
``###`` are mostly comments (leading ``#``); bare ``**Books:**`` is a SyntaxError.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

OPEN = 'display(Markdown(r"""'
CLOSE = '"""))'


def _soften_markdown(md: str) -> str:
    out = md
    out = out.replace("**Books:**", "### Books")
    out = out.replace("**Papers:**", "### Papers")
    out = out.replace("**State-of-the-Art:**", "### State-of-the-art")
    return out


def _patch_code_source(src: str) -> tuple[str, bool]:
    if OPEN not in src or "## 📚 References" not in src:
        return src, False
    i = src.find(OPEN)
    if i == -1:
        return src, False
    start = i + len(OPEN)
    j = src.find(CLOSE, start)
    if j == -1:
        return src, False
    inner = src[start:j]
    new_inner = _soften_markdown(inner)
    if new_inner == inner:
        return src, False
    return src[:start] + new_inner + src[j:], True


def patch_notebook(path: Path) -> bool:
    nb = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        lines = cell.get("source", [])
        if not lines:
            continue
        old = "".join(lines)
        new, did = _patch_code_source(old)
        if not did:
            continue
        nl = new.splitlines(keepends=True)
        if nl and not nl[-1].endswith("\n"):
            nl[-1] += "\n"
        cell["source"] = nl
        changed = True
    if changed:
        path.write_text(json.dumps(nb, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    changed_files: list[Path] = []
    for path in sorted(root.rglob("*.ipynb")):
        rel = path.relative_to(root)
        if "REFERENCE_NOTEBOOKS" in rel.parts:
            continue
        try:
            if patch_notebook(path):
                changed_files.append(path)
        except Exception as e:
            print(f"FAIL {path}: {e}", file=sys.stderr)
            return 1
    for p in changed_files:
        print(p.relative_to(root))
    print(f"Updated {len(changed_files)} notebook(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
