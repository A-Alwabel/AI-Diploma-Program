#!/usr/bin/env python3
"""Append optional FrozenLake motion recap (GIF + slider) to student notebooks.

Skips notebooks that already import ``course09_step_viz`` / ``cs9viz`` (they have
richer visuals). Idempotent via marker ``MOTION_RECAP_COURSE09`` in source.
"""

from __future__ import annotations

import sys
from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell


MARKER = "MOTION_RECAP_COURSE09"

MD_SOURCE = """## Motion recap (optional)

**Why this cell exists:** many RL ideas are easiest to sanity-check when you can **watch time unfold** — a state changes because an action was taken, then a reward signal arrives.

**FrozenLake here is a shared toy picture** (not the “whole story” of every method in this notebook):
- Treat it as a **concrete instance** of the vocabulary you already used: **state** = which tile, **action** = move direction, **reward** = goal / hole / step, **episode** = from start until stop.

**Map this picture to your lesson (pick what fits):**
- **MDPs / value iteration / DP ideas:** ask what a “good tile” should be worth *on the way* to the goal, and what a hole implies for long-horizon returns.
- **Policy evaluation / Monte Carlo / TD / Q-learning / SARSA:** relate the moves you see to **estimated values or Q(s,a)** and to the **backup** idea you implemented above.
- **Exploration vs exploitation / UCB / tuning ε:** random moves are a deliberate exaggeration — compare **wide wandering** vs a mostly greedy path, and connect that to the exploration rule you studied in this unit.
- **Deep RL / training at scale:** use this as a **minimal loop** (observe → act → reward → learn) while remembering real applications change the **observation**, not the basic cycle.

The policy in the next cell is **random on purpose** so the GIF/slider foreground **transitions**, not a claim that this notebook’s full method is already optimal on this map.

### Why the agent may never reach the gift (goal tile `G`)
The code uses **uniform random actions**. That is **not** trying to “solve” FrozenLake or show a hero run to the goal. The point is to show **typical transitions**: safe tiles, edges, sometimes holes, sometimes lucky progress. **Not reaching `G` is expected** and still useful — read the **sequence** (state → action → next state → reward), not “did it win in 10 seconds?”

### Quick student check (about 60 seconds)
- Scroll to **one core code cell above** that carries the main idea of this lesson (policy update, backup, ε-rule, training step, …).
- In one sentence, name **one symbol or variable** from that cell that lines up with **state**, **action**, or **reward** in the FrozenLake frames.
- If you cannot name a match yet, re-run the main lesson cells once, then return here — the GIF is a **mirror** for vocabulary, not a replacement for the definitions.
"""

CODE_SOURCE = f"""# {MARKER} — shared optional visual (FrozenLake GIF + step slider).

%pip install pillow ipywidgets -q

import pathlib
import sys

import numpy as np

for _d in [pathlib.Path.cwd().resolve(), *pathlib.Path.cwd().resolve().parents]:
    if (_d / "course09_step_viz.py").exists():
        _course09 = _d
        break
else:
    raise FileNotFoundError(
        "Could not find course09_step_viz.py — open this notebook from inside Course 09 "
        "(normal Jupyter / Cursor layout) so parent folders include the Course 09 root."
    )

if str(_course09) not in sys.path:
    sys.path.insert(0, str(_course09))

import gymnasium as gym
import course09_step_viz as cs9viz


def _random_policy(obs, step):
    return int(np.random.randint(0, 4))


env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=False, render_mode="rgb_array")
frames, total_r, terminated, truncated = cs9viz.collect_rollout_frames(
    env, _random_policy, max_steps=48, seed=42
)
env.close()
print(
    f"Motion recap | return={{total_r:.1f}} | frames={{len(frames)}} | term={{terminated}} | trunc={{truncated}}"
)
cs9viz.display_gif(frames, duration_ms=110)
cs9viz.display_step_slider(frames, title="FrozenLake — timestep")
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


def notebook_text(nb: nbformat.NotebookNode) -> str:
    parts: list[str] = []
    for cell in nb.cells:
        src = cell.get("source", "")
        if isinstance(src, list):
            parts.append("".join(src))
        else:
            parts.append(str(src))
    return "\n".join(parts)


def needs_recap(nb: nbformat.NotebookNode) -> bool:
    text = notebook_text(nb)
    if "course09_step_viz" in text or "cs9viz" in text:
        return False
    if MARKER in text:
        return False
    return True


def main() -> int:
    course09 = Path(__file__).resolve().parents[1]
    changed = 0
    skipped = 0
    for path in discover_notebooks(course09):
        nb = nbformat.read(path, as_version=4)
        if not needs_recap(nb):
            skipped += 1
            continue
        nb.cells.append(new_markdown_cell(MD_SOURCE))
        nb.cells.append(new_code_cell(CODE_SOURCE))
        nbformat.write(nb, path)
        changed += 1
        print("updated", path.relative_to(course09))
    print(f"changed={changed} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
