"""Course 09 — small helpers for step-by-step RL visuals in Jupyter.

Record rgb_array frames from Gymnasium, show an animated GIF, and optionally
scrub frames with ipywidgets + matplotlib.

Place this file at the **Course 09** root. Notebooks should add that directory to
``sys.path`` (walk parents from ``Path.cwd()``) before ``import course09_step_viz``.
"""

from __future__ import annotations

import io
from typing import Any, Callable, List, Optional, Sequence, Tuple

import numpy as np


def collect_rollout_frames(
    env: Any,
    policy_fn: Callable[[Any, int], int],
    *,
    max_steps: int = 200,
    seed: Optional[int] = None,
) -> Tuple[List[np.ndarray], float, bool, bool]:
    """Run one episode; capture rgb_array before each env.step (plus one final frame).

    policy_fn(observation, step_index) -> int action
    """
    if seed is not None:
        obs, info = env.reset(seed=seed)
    else:
        obs, info = env.reset()

    frames: List[np.ndarray] = []
    terminated = truncated = False
    total_r = 0.0
    step = 0

    while not (terminated or truncated) and step < max_steps:
        rgb = env.render()
        if rgb is not None:
            frames.append(np.asarray(rgb))
        action = int(policy_fn(obs, step))
        obs, reward, terminated, truncated, info = env.step(action)
        total_r += float(reward)
        step += 1

    rgb = env.render()
    if rgb is not None:
        frames.append(np.asarray(rgb))
    return frames, total_r, bool(terminated), bool(truncated)


def frames_to_gif_bytes(frames: Sequence[np.ndarray], duration_ms: int = 140) -> bytes:
    from PIL import Image

    if not frames:
        raise ValueError(
            "No frames to encode — create the env with render_mode='rgb_array'."
        )
    imgs = [Image.fromarray(np.asarray(f, dtype=np.uint8)) for f in frames]
    buf = io.BytesIO()
    imgs[0].save(
        buf,
        format="GIF",
        save_all=True,
        append_images=imgs[1:],
        duration=duration_ms,
        loop=0,
    )
    return buf.getvalue()


def display_gif(frames: Sequence[np.ndarray], *, duration_ms: int = 140) -> None:
    from IPython.display import Image, display

    display(Image(data=frames_to_gif_bytes(frames, duration_ms=duration_ms)))


def display_step_slider(frames: Sequence[np.ndarray], *, title: str = "Frame") -> None:
    """Scrub rgb frames with an IntSlider; optional Play control for autoplay."""
    import ipywidgets as widgets
    from IPython.display import clear_output, display

    frames_list = [np.asarray(f) for f in frames]
    n = len(frames_list)
    if n == 0:
        print("No frames to display.")
        return

    out = widgets.Output()

    def draw(i: int) -> None:
        import matplotlib.pyplot as plt

        with out:
            clear_output(wait=True)
            fig, ax = plt.subplots(figsize=(6.2, 4.2))
            ax.imshow(frames_list[int(i)])
            ax.set_axis_off()
            ax.set_title(f"{title} {int(i)} / {n - 1}")
            plt.show()

    slider = widgets.IntSlider(
        value=0,
        min=0,
        max=n - 1,
        step=1,
        continuous_update=False,
        description="step",
    )
    play = widgets.Play(value=0, min=0, max=n - 1, step=1, interval=420)
    widgets.jslink((play, "value"), (slider, "value"))

    def on_change(change):
        draw(change["new"])

    slider.observe(on_change, names="value")
    display(widgets.VBox([widgets.HBox([slider, play]), out]))
    draw(0)


