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

This short **FrozenLake** rollout connects the ideas in this notebook to **motion on a grid**.
We use ``is_slippery=False`` so each step matches the tile you expect.

The policy here is **intentionally simple** (random actions): the goal is to **scrub timesteps**
with the slider and see how states evolve, not to claim this notebook's full algorithm is
already solved on this map.
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
