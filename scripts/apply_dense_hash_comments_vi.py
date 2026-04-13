#!/usr/bin/env python3
"""Rewrite Course 09 value-iteration code cells with dense # line comments (student-facing English)."""
import json
from pathlib import Path

NB = Path("Course 09/unit1-rl-fundamentals/examples/03_value_iteration.ipynb")


def lines(s: str) -> list[str]:
    if not s.endswith("\n"):
        s += "\n"
    return [ln + "\n" for ln in s.splitlines()]


CELL_8 = r'''# =============================================================================
# CELL OVERVIEW (read this block first)
# This cell loads NumPy/Matplotlib, defines the tiny 3x3 grid MDP, and defines helper functions.
# Later cells call these helpers; the comments here explain *every* major line of Python syntax.
# =============================================================================

# NumPy: fast arrays and vector math (we store V(s) as a 1D array indexed by state id).
import numpy as np
# Matplotlib: plotting (heatmaps for values, arrows for policy, line plot for convergence).
import matplotlib.pyplot as plt

# Print floats with 2 decimals and do not use scientific notation for small numbers (easier to read tables).
np.set_printoptions(precision=2, suppress=True)

# Visual banner in the console so students can see where this notebook's "runtime story" begins.
print("=" * 70)
print("Value Iteration in a Small Grid World")
print("=" * 70)

# =============================================================================
# Cell: environment + grid MDP helpers + printing/plotting utilities
# What it is: constants for the 3x3 world plus small functions every later cell reuses.
# What it does: defines states/actions/rewards, transition(), and tools to print or draw V and pi.
# Why it matters: keeps the rest of the notebook short so students focus on value iteration itself.
# =============================================================================

# --- Grid MDP layout (same toy world as related unit notebooks) ---
# States are integers 0 .. N_STATES-1 in row-major order: top-left = 0, bottom-right = 8 on a 3x3.
N_ROWS, N_COLS = 3, 3
# Total number of cells in the grid; each cell is one MDP state index.
N_STATES = N_ROWS * N_COLS
# Human-readable action names; their position in the list is the numeric action id (0..3).
ACTIONS = ["up", "right", "down", "left"]  # index 0..3 is the action id everywhere below

# Each action moves (row, col) by a delta; hitting an edge clamps (agent stays in-bounds).
ACTION_TO_DELTA = {
    0: (-1, 0),  # up: decrease row index (move toward top of grid)
    1: (0, 1),   # right: increase column index
    2: (1, 0),   # down: increase row index
    3: (0, -1),  # left: decrease column index
}
# Map numeric action ids to Unicode arrows for the policy panel (purely visual).
ACTION_TO_ARROW = {0: "↑", 1: "→", 2: "↓", 3: "←"}

# Terminal indices in the flattened 0..8 state list (see row-major diagram in markdown).
GOAL_STATE = 8  # terminal: large positive reward when transition lands here
PIT_STATE = 6     # terminal: large negative reward when transition lands here
# Python set for O(1) membership tests inside loops (faster/clearer than repeated == checks).
TERMINAL_STATES = {GOAL_STATE, PIT_STATE}  # excluded from Bellman backups in planning loops
# Discount factor gamma in [0,1): weights how much future V(s') matters inside each backup target.
GAMMA = 0.90  # discount on V(next_state) inside every Bellman target


# --- to_pos(state) ---
# What it is: a tiny coordinate helper for the grid MDP.
# What it does: converts a flat state id into (row, col) using row-major layout.
# What this gives you: readable grid math for plotting and for stepping with ACTION_TO_DELTA.
def to_pos(state):
    # divmod returns (quotient, remainder): here quotient is row, remainder is col for row-major indexing.
    return divmod(state, N_COLS)


# --- to_state(row, col) ---
# What it is: the inverse mapping of to_pos.
# What it does: packs (row, col) back into the single integer state id used in arrays.
# What this gives you: lets loops over rows/columns still index the same V[state] vector.
def to_state(row, col):
    # Multiply row by width then add column: standard row-major flattening formula.
    return row * N_COLS + col


# --- transition(state, action) ---
# What it is: the known one-step model (s, a) -> (s', r) for this notebook's toy grid.
# What it does: applies movement with boundary clamping, then assigns goal/pit/step rewards.
# What this gives you: every Bellman backup in VI can ask "what happens if I try this action?".
def transition(state, action):
    # If we are already on a terminal, the planning MDP is "done": no further motion or reward.
    if state in TERMINAL_STATES:
        # Return the same absorbing state with reward 0 (episode end signal for the dynamics function).
        return state, 0.0

    # Convert the flat state id into grid coordinates so we can add a movement delta safely.
    row, col = to_pos(state)
    # Look up how this action moves on the grid (d_row, d_col).
    d_row, d_col = ACTION_TO_DELTA[action]
    # Clamp each coordinate into [0, N-1] so moves off the grid behave like hitting a wall (no illegal indices).
    next_row = min(max(row + d_row, 0), N_ROWS - 1)
    next_col = min(max(col + d_col, 0), N_COLS - 1)
    # Flatten back to the single integer next-state id used everywhere else in the notebook.
    next_state = to_state(next_row, next_col)

    # Reward shaping rules: goal/pit are special; everything else pays a small step cost.
    if next_state == GOAL_STATE:
        return next_state, 10.0
    if next_state == PIT_STATE:
        return next_state, -10.0
    # Ordinary step on non-terminal tiles: negative reward encourages shorter paths to the goal.
    return next_state, -1.0


# --- state_grid_from_values(values) ---
# What it is: a layout helper for heatmaps.
# What it does: copies V(s) into a 2D numpy grid aligned with the physical cells.
# What this gives you: matplotlib imshow can color the maze-like layout students expect.
def state_grid_from_values(values):
    # Start as all-NaN so terminals can stay visually "empty" on the color scale (we skip writing them).
    grid = np.full((N_ROWS, N_COLS), np.nan)
    # Visit every state id; terminals are not given a numeric V overlay in the heatmap panel.
    for state in range(N_STATES):
        if state in TERMINAL_STATES:
            continue
        r, c = to_pos(state)
        # Store the scalar V(state) at the correct grid coordinate for plotting.
        grid[r, c] = values[state]
    return grid


# --- plot_values_and_policy(values, policy, title) ---
# What it is: a two-panel figure for teaching "values then decisions".
# What it does: draws V(s) as a heatmap and overlays the greedy arrow policy on the same grid.
# What this gives you: you can visually check that high value regions line up with sensible arrows.
def plot_values_and_policy(values, policy, title):
    # Create 1 row x 2 columns of axes: left values, right policy.
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # ----- Left panel: value heatmap -----
    # Convert the 1D value vector into a 2D grid suitable for imshow().
    value_grid = state_grid_from_values(values)
    # imshow treats matrix entries as pixel colors; viridis is a perceptually uniform colormap.
    im = axes[0].imshow(value_grid, cmap="viridis")
    axes[0].set_title(f"{title}: values")
    # Explicit tick marks so grid lines align with discrete cells (helps students map indices to squares).
    axes[0].set_xticks(range(N_COLS))
    axes[0].set_yticks(range(N_ROWS))
    # Overlay text on every cell: show numeric V, or G/P markers for terminals.
    for state in range(N_STATES):
        r, c = to_pos(state)
        if state == GOAL_STATE:
            label = "G"
        elif state == PIT_STATE:
            label = "P"
        else:
            label = f"{values[state]:.1f}"
        # Note: imshow uses image coordinates; for this small grid, (c, r) matches our row/col convention here.
        axes[0].text(c, r, label, ha="center", va="center", color="white")
    # Colorbar explains the numeric meaning of colors (links the picture back to V magnitudes).
    fig.colorbar(im, ax=axes[0], fraction=0.046, pad=0.04)

    # ----- Right panel: greedy policy arrows -----
    axes[1].set_title(f"{title}: greedy policy")
    # Set limits so arrows appear centered in each grid cell (half-cell padding around edges).
    axes[1].set_xlim(-0.5, N_COLS - 0.5)
    axes[1].set_ylim(N_ROWS - 0.5, -0.5)
    axes[1].set_xticks(range(N_COLS))
    axes[1].set_yticks(range(N_ROWS))
    axes[1].grid(True)
    for state in range(N_STATES):
        r, c = to_pos(state)
        if state == GOAL_STATE:
            symbol = "G"
        elif state == PIT_STATE:
            symbol = "P"
        else:
            # policy[state] stores an action id; map it to a Unicode arrow for display.
            symbol = ACTION_TO_ARROW[policy[state]]
        axes[1].text(c, r, symbol, ha="center", va="center", fontsize=13)
    # Reduce subplot overlap then display the figure in the notebook output.
    plt.tight_layout()
    plt.show()


# --- plot_deltas(deltas) ---
# What it is: a convergence diagnostic plot for synchronous value iteration.
# What it does: plots sweep index on the x-axis vs the largest per-state Bellman change that sweep.
# What this gives you: you can see updates shrinking toward zero instead of guessing from numbers alone.
def plot_deltas(deltas):
    # New figure canvas; figsize is in inches (width, height) for the matplotlib window.
    plt.figure(figsize=(5, 3))
    # x-axis is implicit 0..len-1 sweep indices; y-axis is the delta list values; markers show each sweep.
    plt.plot(deltas, marker="o")
    plt.title("Value iteration convergence")
    plt.xlabel("Sweep number")
    plt.ylabel("Largest Bellman update")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# --- print_values(values) ---
# What it is: a text table printer for V(s).
# What it does: walks the grid rows/columns and prints each state's value (or G/P for terminals).
# What this gives you: exact numbers you can copy or compare sweep-to-sweep without squinting at plots.
def print_values(values):
    print("\nState values:")
    # Print in row-major human order: top row first, left-to-right within each row.
    for r in range(N_ROWS):
        row = []  # collect formatted cell strings for one printed row
        for c in range(N_COLS):
            s = to_state(r, c)
            if s == GOAL_STATE:
                row.append("  G   ")
            elif s == PIT_STATE:
                row.append("  P   ")
            else:
                row.append(f"{values[s]:6.2f}")
        # Join with spaces so columns line up reasonably in a monospace font.
        print(" ".join(row))


# --- print_policy(policy) ---
# What it is: a text table printer for the greedy policy.
# What it does: maps each stored action index to an arrow symbol for every non-terminal cell.
# What this gives you: a quick sanity check that the policy is legal arrows and avoids obvious traps.
def print_policy(policy):
    print("\nGreedy policy:")
    for r in range(N_ROWS):
        row = []
        for c in range(N_COLS):
            s = to_state(r, c)
            if s == GOAL_STATE:
                row.append(" G ")
            elif s == PIT_STATE:
                row.append(" P ")
            else:
                row.append(f" {ACTION_TO_ARROW[policy[s]]} ")
        print(" ".join(row))


# --- Driver: confirm environment constants (used by later cells) ---
# What it is: tiny sanity print so students know the goal/pit indices before running backups.
# What it does: prints the two terminal ids after all helper defs are loaded into memory.
print("Environment ready.")
print("Goal state:", GOAL_STATE, "| Pit state:", PIT_STATE)
'''

CELL_11 = r'''# =============================================================================
# CELL OVERVIEW
# This cell is a *script* (no `def`): it demonstrates ONE Bellman backup at ONE state using the known model.
# =============================================================================
# Cell: single-state Bellman warm-up (script cell — no def functions here)
# What it is: a miniature version of one Bellman optimality backup at one state s.
# What it does: loops actions, prints r + gamma*V(s'), plots bars, points at max().
# Why it matters: the inner loop of value_iteration is the same math, repeated for every state.
# =============================================================================

# Build a fresh all-zero value table: with V=0, the backup target reduces to immediate reward only.
values = np.zeros(N_STATES)
# Pick a non-terminal interior-ish cell so all four moves stay interesting on this 3x3.
state = 4  # center cell of the 3x3 grid (arbitrary but easy to visualize)

print(f"Inspecting state {state} before full value iteration:\n")

# We will collect one scalar backup target per action id (same ordering as ACTIONS list).
action_returns = []
# Loop variable `action` is 0..3; `action_name` is the matching string label from ACTIONS.
for action, action_name in enumerate(ACTIONS):
    # Ask the model for the deterministic next state and reward for this (state, action) pair.
    next_state, reward = transition(state, action)
    # Bellman backup candidate for this fixed action a:
    #   reward now + discounted value at the next state under the *current* V table.
    target = reward + GAMMA * values[next_state]
    # Save it so we can plot all actions side-by-side after the loop finishes.
    action_returns.append(target)
    # Human-readable line trace: helps students connect printed numbers to the bar chart below.
    print(
        f"Action {action_name:>5} -> next_state={next_state}, "
        f"reward={reward:>5}, target={target:>6.2f}"
    )

# Create a new matplotlib figure for the bar chart (separate from later plots in other cells).
plt.figure(figsize=(5, 3))
# x positions are category labels (ACTIONS); heights are the backup targets computed above.
plt.bar(ACTIONS, action_returns, color="steelblue")
plt.title(f"One-step action returns from state {state}")
plt.ylabel("Bellman target")
# Horizontal line at the max: visually reinforces the `max(...)` used inside value iteration.
plt.axhline(max(action_returns), linestyle="--", color="darkred", label="best action value")
plt.legend()
plt.tight_layout()
plt.show()

print("\nBest action value from state 4:", max(action_returns))
print("Full VI repeats: for every state, replace V(s) with max over actions of these targets.")
'''

CELL_14 = r'''# =============================================================================
# CELL OVERVIEW
# Defines value_iteration + greedy_policy_from_values, then runs them and prints/plots the outcome.
# =============================================================================
# Cell: full value iteration + greedy policy extraction
# What it is: the two core planning functions, then a small driver that prints and plots results.
# What it does: (1) iterate Bellman optimality backups until convergence, (2) argmax extract pi.
# Why it matters: connects the math to numbers you can read and pictures you can interpret.
# =============================================================================

# --- value_iteration(gamma=GAMMA, theta=1e-6) ---
# What it is: the classic planning algorithm that solves for optimal V in a known finite MDP.
# What it does: repeats synchronous sweeps, replacing each V(s) with max_a [r + gamma V(s')].
# What this gives you: optimal values for this grid plus a per-sweep delta trace for convergence plots.
def value_iteration(gamma=GAMMA, theta=1e-6):
    # values[s] will hold V(s); terminals are never updated here, so their entries remain 0.0 by convention.
    values = np.zeros(N_STATES)
    # Record the global "movement" of V after each sweep (used for stopping + the delta plot).
    deltas = []  # one float per sweep: "how much did the whole table move?"

    # Repeat sweeps until the Bellman operator updates become tiny (theta is a small positive threshold).
    while True:
        # --- One synchronous sweep ---
        # Read backups only from `values` (frozen at sweep start); write into `new_values`;
        # then assign values = new_values so every state used the same previous sweep.
        delta = 0.0
        # Copy old table so we can write new numbers without corrupting the inputs mid-sweep.
        new_values = values.copy()
        # Visit every state index; terminals are skipped because their values are not unknowns here.
        for state in range(N_STATES):
            if state in TERMINAL_STATES:
                continue
            action_returns = []
            # Evaluate every legal action from this state under the one-step model.
            for action in range(len(ACTIONS)):
                next_state, reward = transition(state, action)
                # This is the same r + gamma*V(s') term you saw in the warm-up cell, but for all actions.
                action_returns.append(reward + gamma * values[next_state])
            # Bellman optimality: take the best one-step return (this is the max inside the Bellman backup).
            best_value = max(action_returns)
            # Track the largest per-state change this sweep (L-infinity style progress measure).
            delta = max(delta, abs(best_value - values[state]))
            # Commit the improved estimate for this state into the "next table" buffer.
            new_values[state] = best_value
        # End of sweep: publish the new table as the current V for the next iteration/plotting.
        values = new_values
        deltas.append(delta)
        # Stop when the value table is effectively stable (changes smaller than numerical tolerance).
        if delta < theta:
            break

    return values, deltas


# --- greedy_policy_from_values(values, gamma=GAMMA) ---
# What it is: policy extraction ("act greedy with respect to V") after planning converges.
# What it does: for each state, recomputes action returns and stores argmax_a (ties -> smallest index).
# What this gives you: an actual rule the agent can follow on the grid, not just abstract numbers.
def greedy_policy_from_values(values, gamma=GAMMA):
    # policy[s] stores an integer action id consistent with ACTION_TO_DELTA / ACTIONS ordering.
    policy = np.zeros(N_STATES, dtype=int)
    for state in range(N_STATES):
        if state in TERMINAL_STATES:
            continue
        action_returns = []
        for action in range(len(ACTIONS)):
            next_state, reward = transition(state, action)
            action_returns.append(reward + gamma * values[next_state])
        # argmax returns the index of the largest element; int(...) makes the dtype explicit for the array.
        policy[state] = int(np.argmax(action_returns))
    return policy


# --- Driver: run VI, extract policy, print summary, plot ---
# What it is: the "main program" lines after the function definitions above.
# What it does: calls your functions, prints tables, then shows the heatmap/arrow figure + delta curve.
# What this gives you: one end-to-end story from math -> numbers -> visuals for class discussion.
optimal_values, deltas = value_iteration()
optimal_policy = greedy_policy_from_values(optimal_values)

# Text output: exact numbers + arrow table (good for checking against the plots).
print_values(optimal_values)
print_policy(optimal_policy)
print(f"\nValue iteration converged in {len(deltas)} sweeps.")
print("Final Bellman update size:", deltas[-1])

# Short recap lines for students who skim: restates what the cell proved on this toy MDP.
print("\nSummary:")
print("- Value iteration applies the Bellman optimality update directly.")
print("- It produces optimal state values for this small known MDP.")
print("- A greedy policy can be extracted from those final values.")
print("- In the next notebook, you move from planning in a known model to working with Gym environments.")

# Graphics: spatial intuition + convergence curve (two different "views" of the same computation).
plot_values_and_policy(optimal_values, optimal_policy, title="Value iteration result")
plot_deltas(deltas)
'''

CELL_16 = r'''# =============================================================================
# CELL OVERVIEW
# Generic recap cell: searches runtime variables and auto-plots small numeric artifacts.
# =============================================================================
# Cell: optional auto-visual recap (generic helper cell used across course notebooks)
# What it is: a small "scanner" that looks for numeric lesson variables in globals().
# What it does: tries dict / 1D / 2D plots; if nothing fits, shows a tiny object-count summary.
# Why it matters: gives students a second visual pass without hand-writing a new plot each lesson.
# =============================================================================

# `numbers` is imported because some type checks use Python's numeric tower patterns in other notebooks.
import numbers
import numpy as np
import matplotlib.pyplot as plt


# --- _is_number(value) ---
# What it is: a strict scalar type check used by the auto-plot heuristics.
# What it does: accepts int/float/numpy scalars and explicitly rejects bool.
# What this gives you: avoids treating False/True as 0/1 counts when scanning lesson variables.
def _is_number(value):
    # isinstance checks runtime types; bool is a subclass of int, so we exclude it explicitly.
    return isinstance(value, (int, float, np.integer, np.floating)) and not isinstance(value, bool)


# --- _as_numeric_dict(value) ---
# What it is: a safe "maybe this dict is plottable" converter.
# What it does: returns (labels, array) only if every value is numeric and the dict is small enough.
# What this gives you: lets the recap cell build a bar chart without crashing on random objects.
def _as_numeric_dict(value):
    # Reject non-dicts, empty dicts, and "wide" dicts (too many bars => unreadable in a tiny recap cell).
    if not isinstance(value, dict) or not value or len(value) > 12:
        return None
    converted = []
    # Every value must be numeric; if any value fails, the whole dict is not plottable as a simple bar chart.
    for item in value.values():
        if not _is_number(item):
            return None
        converted.append(float(item))
    # Keys become x tick labels; values become bar heights.
    return [str(key) for key in value.keys()], np.asarray(converted, dtype=float)


# --- _as_numeric_array(value, dims) ---
# What it is: a safe ndarray coercion helper with size caps.
# What it does: tries float conversion, enforces rank `dims`, and rejects arrays that are too large.
# What this gives you: quick line/heatmap plots without accidentally plotting giant tensors.
def _as_numeric_array(value, dims):
    try:
        # asarray shares memory when possible, but here we mainly want a float array for plotting APIs.
        array = np.asarray(value, dtype=float)
    except Exception:
        # If conversion fails, this variable is not a numeric array in a plotting-friendly sense.
        return None
    if array.ndim != dims:
        return None
    # Guardrails: keep recap plots small so notebook rendering stays fast and readable.
    if dims == 1 and not (2 <= array.size <= 200):
        return None
    if dims == 2 and array.size > 400:
        return None
    return array


# --- Build search list: preferred metric names, then every global (non-dunder) name ---
# What it is: configuration for which variables we try first when guessing what to plot.
# What it does: merges priority_names with sorted globals keys so common RL names win the race.
# What this gives you: stable plots in typical lessons (rewards, values) without hard-coding this notebook.
priority_names = [
    "reward_history", "episode_rewards", "returns", "value_history", "q_values", "Q", "V",
    "scores", "metrics", "counts", "reward_grid", "values", "allocations", "application_scores"
]

# Names we must never treat as lesson data (they are plotting/import utilities, not student metrics).
skip_names = {"np", "plt", "numbers", "math"}
candidates = []  # list of tuples: ("dict"|"line"|"heatmap", variable_name, payload)
seen = set()  # prevents trying the same global name twice if it appears in multiple places
search_space = priority_names + sorted(name for name in globals() if not name.startswith("_"))

# --- Scan globals: collect up to three plottable candidates ---
# What it is: the main control loop of this recap cell (still not a def — linear script).
# What it does: classifies each variable as dict, 2D heatmap, or 1D series; stops at three hits.
# What this gives you: a quick dashboard feel without importing lesson-specific plotting code.
for name in search_space:
    if name in seen or name not in globals() or name in skip_names:
        continue
    seen.add(name)
    value = globals()[name]  # fetch the live object from the notebook kernel namespace

    dict_payload = _as_numeric_dict(value)
    if dict_payload is not None:
        candidates.append(("dict", name, dict_payload))
        if len(candidates) == 3:
            break
        continue

    array_2d = _as_numeric_array(value, 2)
    if array_2d is not None:
        candidates.append(("heatmap", name, array_2d))
        if len(candidates) == 3:
            break
        continue

    array_1d = _as_numeric_array(value, 1)
    if array_1d is not None:
        candidates.append(("line", name, array_1d))
        if len(candidates) == 3:
            break

# --- Render: either the fallback summary bar chart or the discovered lesson plots ---
if not candidates:
    # If we found nothing plottable, show a coarse summary of what kinds of objects exist in memory.
    summary = {
        "functions": sum(callable(value) for value in globals().values()),
        "classes": sum(isinstance(value, type) for value in globals().values()),
        "numeric vars": sum(_is_number(value) for value in globals().values()),
    }
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.bar(summary.keys(), summary.values(), color=["#2563eb", "#16a34a", "#f59e0b"])
    ax.set_title("Notebook artifact summary")
    ax.set_ylabel("Count")
    for idx, value in enumerate(summary.values()):
        ax.text(idx, value + 0.05, str(value), ha="center")
    plt.tight_layout()
    plt.show()
else:
    # Build as many subplot columns as candidates (1..3), widening the canvas accordingly.
    fig, axes = plt.subplots(1, len(candidates), figsize=(5 * len(candidates), 3.8))
    if len(candidates) == 1:
        axes = [axes]  # normalize to a list so the zip loop always works

    for ax, (kind, name, payload) in zip(axes, candidates):
        if kind == "dict":
            labels, values = payload
            ax.bar(range(len(values)), values, color="#2563eb")
            ax.set_xticks(range(len(values)))
            ax.set_xticklabels(labels, rotation=45, ha="right")
            ax.set_title(f"{name} (dict)")
            ax.set_ylabel("Value")
        elif kind == "line":
            ax.plot(payload, marker="o", linewidth=2, color="#16a34a")
            ax.set_title(f"{name} (series)")
            ax.set_xlabel("Index")
            ax.set_ylabel("Value")
        else:
            # kind == "heatmap"
            image = ax.imshow(payload, aspect="auto", cmap="viridis")
            ax.set_title(f"{name} (heatmap)")
            fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)

    plt.tight_layout()
    plt.show()
'''


def main() -> None:
    nb = json.loads(NB.read_text(encoding="utf-8"))
    nb["cells"][8]["source"] = lines(CELL_8)
    nb["cells"][11]["source"] = lines(CELL_11)
    nb["cells"][14]["source"] = lines(CELL_14)
    nb["cells"][16]["source"] = lines(CELL_16)
    NB.write_text(json.dumps(nb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("updated", NB)


if __name__ == "__main__":
    main()
