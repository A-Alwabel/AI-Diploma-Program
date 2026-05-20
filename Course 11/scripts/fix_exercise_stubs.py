#!/usr/bin/env python3
"""Make exercise TODO code cells valid Python (pass + comments)."""

from __future__ import annotations

import json
import re
from pathlib import Path

COURSE11 = Path(__file__).resolve().parents[1]


def fix_stub_source(src: str) -> str:
    lines = src.splitlines()
    if not lines:
        return "pass  # YOUR CODE HERE\n"
    out: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            out.append("")
            continue
        if stripped.startswith("#") or stripped.startswith("%"):
            out.append(line)
            continue
        if stripped.upper().startswith("TODO") or stripped == "YOUR CODE HERE":
            out.append(f"# {stripped}")
            continue
        # prose instructions → comment
        if not any(
            stripped.startswith(k)
            for k in ("import ", "from ", "def ", "class ", "pass", "return", "@", "if ", "for ", "with ")
        ):
            out.append(f"# {stripped}")
            continue
        out.append(line)
    body = "\n".join(out).strip()
    if "pass" not in body and "import " not in body.split("\n")[0:3]:
        body += "\npass  # YOUR CODE HERE"
    return body + "\n"


def main() -> int:
    n = 0
    for nb_path in sorted(COURSE11.glob("unit*/exercises/*.ipynb")):
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
        changed = False
        for cell in nb["cells"]:
            if cell.get("cell_type") != "code":
                continue
            if isinstance(cell["source"], str):
                src = cell["source"]
            else:
                src = "".join(cell["source"])
            fixed = fix_stub_source(src)
            if fixed != src:
                cell["source"] = [fixed]
                changed = True
        if changed:
            nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            n += 1
            print("fixed", nb_path.relative_to(COURSE11))
    print(f"done {n} exercises")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
