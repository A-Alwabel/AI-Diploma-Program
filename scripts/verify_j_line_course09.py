#!/usr/bin/env python3
"""
Verify J-line coverage for student-facing Course 09 notebooks.

Executable lines (non-blank, not full-line #, not triple-quoted docstring open,
and not inside tokenizer multiline strings) must be immediately preceded (skipping
blank lines) by a line whose first non-space chars are '# ' (hash + space).

Exit code 1 if any gap is found. Usage (repo root):

  python3 scripts/verify_j_line_course09.py
"""
from __future__ import annotations

import json
import sys
import tokenize
from io import BytesIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "Course 09"


def multiline_string_skip_lines(src: str) -> set[int]:
    skip: set[int] = set()
    readline = BytesIO(src.encode("utf-8")).readline
    try:
        for tok in tokenize.tokenize(readline):
            if tok.type != tokenize.STRING:
                continue
            sl, _ = tok.start
            el, _ = tok.end
            if el > sl:
                for ln in range(sl + 1, el + 1):
                    skip.add(ln)
    except (tokenize.TokenError, IndentationError):
        pass
    return skip


def _is_opening_docstring_line(raw: str) -> bool:
    t = raw.lstrip()
    return t.startswith(('"""', "'''")) or t.startswith(
        ("r'''", 'r"""', "f'''", 'f"""', "u'''", 'u"""')
    )


def gaps_in_cell(src: str) -> list[tuple[int, str]]:
    lines = src.splitlines()
    if not lines:
        return []
    skip = multiline_string_skip_lines(src)
    bad: list[tuple[int, str]] = []
    for i, raw in enumerate(lines, start=1):
        if i in skip:
            continue
        if not raw.strip():
            continue
        if raw.lstrip().startswith("#"):
            continue
        if _is_opening_docstring_line(raw):
            continue
        j = i - 2
        while j >= 0 and not lines[j].strip():
            j -= 1
        if j < 0:
            bad.append((i, raw.strip()[:100]))
            continue
        prev = lines[j].lstrip()
        if not prev.startswith("# "):
            bad.append((i, raw.strip()[:100]))
    return bad


def main() -> int:
    problems: list[str] = []
    for p in sorted(COURSE.rglob("*.ipynb")):
        if "DOCS" in p.parts:
            continue
        nb = json.loads(p.read_text(encoding="utf-8"))
        for ci, cell in enumerate(nb.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            src = "".join(cell.get("source", []))
            if not src.strip():
                continue
            bad = gaps_in_cell(src)
            if bad:
                ln, snip = bad[0]
                rel = p.relative_to(ROOT)
                problems.append(f"{rel}  cell {ci}  line {ln}: {snip!r}  (+{len(bad)-1} more)")

    if problems:
        print(f"FAIL: {len(problems)} code cell(s) missing J-line # above executable code")
        for row in problems[:80]:
            print(" ", row)
        if len(problems) > 80:
            print(f"  ... and {len(problems)-80} more")
        return 1
    print("OK: all scanned Course 09 code cells have '# ' headers above executable lines.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
