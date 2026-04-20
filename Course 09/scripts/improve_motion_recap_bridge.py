#!/usr/bin/env python3
"""Replace generic Motion recap markdown with a stronger lesson bridge.

Looks for the code cell marker ``MOTION_RECAP_COURSE09`` and updates the
immediately preceding markdown cell if it still starts with the old heading.
"""

from __future__ import annotations

import sys
from pathlib import Path

import nbformat

MARKER = "MOTION_RECAP_COURSE09"
OLD_HEADING = "## Motion recap (optional)"

NEW_MD = """## Motion recap (optional)

**Why this cell exists:** many RL ideas are easiest to sanity-check when you can **watch time unfold** — a state changes because an action was taken, then a reward signal arrives.

**FrozenLake here is a shared toy picture** (not the “whole story” of every method in this notebook):
- Treat it as a **concrete instance** of the vocabulary you already used: **state** = which tile, **action** = move direction, **reward** = goal / hole / step, **episode** = from start until stop.

**Map this picture to your lesson (pick what fits):**
- **MDPs / value iteration / DP ideas:** ask what a “good tile” should be worth *on the way* to the goal, and what a hole implies for long-horizon returns.
- **Policy evaluation / Monte Carlo / TD / Q-learning / SARSA:** relate the moves you see to **estimated values or Q(s,a)** and to the **backup** idea you implemented above.
- **Exploration vs exploitation / UCB / tuning ε:** random moves are a deliberate exaggeration — compare **wide wandering** vs a mostly greedy path, and connect that to the exploration rule you studied in this unit.
- **Deep RL / training at scale:** use this as a **minimal loop** (observe → act → reward → learn) while remembering real applications change the **observation**, not the basic cycle.

The policy in the next cell is **random on purpose** so the GIF/slider foreground **transitions**, not a claim that this notebook’s full method is already optimal on this map.
"""


def discover_notebooks(course09: Path) -> list[Path]:
    out: list[Path] = []
    for p in sorted(course09.rglob("*.ipynb")):
        if "DOCS" in p.parts:
            continue
        if "unit" not in str(p):
            continue
        out.append(p)
    return out


def cell_source(cell) -> str:
    src = cell.get("source", "")
    if isinstance(src, list):
        return "".join(src)
    return str(src)


def set_cell_source(cell, text: str) -> None:
    if cell.get("cell_type") != "markdown":
        return
    cell["source"] = text


def main() -> int:
    course09 = Path(__file__).resolve().parents[1]
    updated = 0
    for path in discover_notebooks(course09):
        nb = nbformat.read(path, as_version=4)
        changed = False
        for i, cell in enumerate(nb.cells):
            if cell.get("cell_type") != "code":
                continue
            src = cell_source(cell)
            if MARKER not in src:
                continue
            if i == 0:
                continue
            prev = nb.cells[i - 1]
            if prev.get("cell_type") != "markdown":
                continue
            psrc = cell_source(prev)
            if OLD_HEADING not in psrc and "Motion recap" not in psrc:
                continue
            if psrc.strip() == NEW_MD.strip():
                continue
            set_cell_source(prev, NEW_MD)
            changed = True
        if changed:
            nbformat.write(nb, path)
            updated += 1
            print("updated", path.relative_to(course09))
    print(f"notebooks_updated={updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
