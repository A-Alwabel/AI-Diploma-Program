#!/usr/bin/env python3
"""Normalize notebook JSON: source as list of strings, valid nbformat."""

from __future__ import annotations

import json
from pathlib import Path

COURSE11 = Path(__file__).resolve().parents[1]


def normalize_source(src) -> list[str]:
    if src is None:
        return []
    if isinstance(src, list):
        text = "".join(src)
    else:
        text = str(src)
    if not text:
        return []
    return [text if text.endswith("\n") else text + "\n"]


def main() -> int:
    n = 0
    for nb_path in sorted(COURSE11.rglob("*.ipynb")):
        if "DOCS" in nb_path.parts:
            continue
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
        changed = False
        for cell in nb.get("cells", []):
            old = cell.get("source")
            new = normalize_source(old)
            if old != new:
                cell["source"] = new
                changed = True
        if changed:
            nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            n += 1
            print("normalized", nb_path.relative_to(COURSE11))
    print(f"done {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
