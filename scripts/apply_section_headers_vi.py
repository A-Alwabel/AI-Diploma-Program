#!/usr/bin/env python3
"""
03_value_iteration.ipynb: place a clear # header ABOVE each logical block inside code cells
(imports, constants, each function, drivers). Student-facing English.
"""
import json
from pathlib import Path

NB = Path("Course 09/unit1-rl-fundamentals/examples/03_value_iteration.ipynb")
SEP = "# " + "-" * 77


def lines(s: str) -> list[str]:
    if not s.endswith("\n"):
        s += "\n"
    return [ln + "\n" for ln in s.splitlines()]


def block(title: str, body: str, *desc: str) -> str:
    out = [SEP, f"# {title}"]
    out.extend(desc)
    out.append(SEP)
    out.append(body.strip())
    return "\n".join(out) + "\n\n"


CELL_8 = "\n".join(
    [
        block(
            "CELL: Environment, grid MDP, helpers",
            "",
            "# This cell defines the toy world and small utilities used later.",
            "# Each block below has a header, then the Python it explains.",
        ).strip()
        + "\n\n"
        + block(
            "BLOCK: Imports and print options",
            "import numpy as np\nimport matplotlib.pyplot as plt\n\nnp.set_printoptions(precision=2, suppress=True)",
            "# NumPy: arrays for V(s). Matplotlib: figures for values/policy/convergence.",
        )
        + block(
            "BLOCK: Console banner",
            'print("=" * 70)\nprint("Value Iteration in a Small Grid World")\nprint("=" * 70)',
            "# Optional separator so notebook output is easy to spot while teaching.",
        )
        + block(
            "BLOCK: MDP constants (states, actions, terminals, discount)",
            '''N_ROWS, N_COLS = 3, 3
N_STATES = N_ROWS * N_COLS
ACTIONS = ["up", "right", "down", "left"]

ACTION_TO_DELTA = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}
ACTION_TO_ARROW = {0: "↑", 1: "→", 2: "↓", 3: "←"}

GOAL_STATE = 8
PIT_STATE = 6
TERMINAL_STATES = {GOAL_STATE, PIT_STATE}
GAMMA = 0.90''',
            "# States 0..8 row-major. Actions 0..3. Terminals are absorbing in transition().",
            "# GAMMA is the discount factor inside every Bellman target r + gamma * V(s').",
        )
        + block(
            "FUNCTION: to_pos(state) -> (row, col)",
            "def to_pos(state):\n    return divmod(state, N_COLS)",
            "# Flat index -> grid coordinates for this row-major layout.",
        )
        + block(
            "FUNCTION: to_state(row, col) -> state_id",
            "def to_state(row, col):\n    return row * N_COLS + col",
            "# Inverse of to_pos: grid coordinates -> flat index used by V[state].",
        )
        + block(
            "FUNCTION: transition(state, action) -> (next_state, reward)",
            '''def transition(state, action):
    if state in TERMINAL_STATES:
        return state, 0.0

    row, col = to_pos(state)
    d_row, d_col = ACTION_TO_DELTA[action]
    next_row = min(max(row + d_row, 0), N_ROWS - 1)
    next_col = min(max(col + d_col, 0), N_COLS - 1)
    next_state = to_state(next_row, next_col)

    if next_state == GOAL_STATE:
        return next_state, 10.0
    if next_state == PIT_STATE:
        return next_state, -10.0
    return next_state, -1.0''',
            "# Known model for backups: clamp moves to the grid, then apply goal/pit/step rewards.",
        )
        + block(
            "FUNCTION: state_grid_from_values(values)",
            '''def state_grid_from_values(values):
    grid = np.full((N_ROWS, N_COLS), np.nan)
    for state in range(N_STATES):
        if state in TERMINAL_STATES:
            continue
        r, c = to_pos(state)
        grid[r, c] = values[state]
    return grid''',
            "# Builds a 2D matrix for imshow; terminals stay NaN on the heatmap.",
        )
        + block(
            "FUNCTION: plot_values_and_policy(values, policy, title)",
            '''def plot_values_and_policy(values, policy, title):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    value_grid = state_grid_from_values(values)
    im = axes[0].imshow(value_grid, cmap="viridis")
    axes[0].set_title(f"{title}: values")
    axes[0].set_xticks(range(N_COLS))
    axes[0].set_yticks(range(N_ROWS))
    for state in range(N_STATES):
        r, c = to_pos(state)
        if state == GOAL_STATE:
            label = "G"
        elif state == PIT_STATE:
            label = "P"
        else:
            label = f"{values[state]:.1f}"
        axes[0].text(c, r, label, ha="center", va="center", color="white")
    fig.colorbar(im, ax=axes[0], fraction=0.046, pad=0.04)

    axes[1].set_title(f"{title}: greedy policy")
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
            symbol = ACTION_TO_ARROW[policy[state]]
        axes[1].text(c, r, symbol, ha="center", va="center", fontsize=13)
    plt.tight_layout()
    plt.show()''',
            "# Two panels: values heatmap + greedy arrows decoded from policy[state].",
        )
        + block(
            "FUNCTION: plot_deltas(deltas)",
            '''def plot_deltas(deltas):
    plt.figure(figsize=(5, 3))
    plt.plot(deltas, marker="o")
    plt.title("Value iteration convergence")
    plt.xlabel("Sweep number")
    plt.ylabel("Largest Bellman update")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()''',
            "# X = sweep index, Y = largest Bellman change that sweep (shrinks as VI converges).",
        )
        + block(
            "FUNCTION: print_values(values)",
            '''def print_values(values):
    print("\\nState values:")
    for r in range(N_ROWS):
        row = []
        for c in range(N_COLS):
            s = to_state(r, c)
            if s == GOAL_STATE:
                row.append("  G   ")
            elif s == PIT_STATE:
                row.append("  P   ")
            else:
                row.append(f"{values[s]:6.2f}")
        print(" ".join(row))''',
            "# Text table of V(s) in grid layout; terminals print as G/P.",
        )
        + block(
            "FUNCTION: print_policy(policy)",
            '''def print_policy(policy):
    print("\\nGreedy policy:")
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
        print(" ".join(row))''',
            "# Text table of greedy arrows; policy[s] is an action index 0..3.",
        )
        + block(
            "BLOCK: Sanity print (terminal ids)",
            'print("Environment ready.")\nprint("Goal state:", GOAL_STATE, "| Pit state:", PIT_STATE)',
            "# Confirms constants loaded; later cells assume these indices match transition().",
        )
    ]
).strip() + "\n"


CELL_11 = (
    block(
        "CELL: One-state Bellman warm-up (script, no def)",
        "",
        "# Same r + gamma*V(s') computation you will see inside value_iteration, but for one state only.",
    ).strip()
    + "\n\n"
    + block(
        "BLOCK: Initialize V=0 and pick a demo state",
        "values = np.zeros(N_STATES)\nstate = 4  # center of 3x3",
        "# V=0 makes each printed target equal immediate reward (until you run full VI).",
    )
    + block(
        "BLOCK: Loop all actions and print each one-step Bellman target",
        '''print(f"Inspecting state {state} before full value iteration:\\n")

action_returns = []
for action, action_name in enumerate(ACTIONS):
    next_state, reward = transition(state, action)
    target = reward + GAMMA * values[next_state]
    action_returns.append(target)
    print(
        f"Action {action_name:>5} -> next_state={next_state}, "
        f"reward={reward:>5}, target={target:>6.2f}"
    )''',
        "# transition() supplies (s', r); target is the candidate backup value for that fixed action.",
    )
    + block(
        "BLOCK: Bar chart of action targets + horizontal line at the max",
        '''plt.figure(figsize=(5, 3))
plt.bar(ACTIONS, action_returns, color="steelblue")
plt.title(f"One-step action returns from state {state}")
plt.ylabel("Bellman target")
plt.axhline(max(action_returns), linestyle="--", color="darkred", label="best action value")
plt.legend()
plt.tight_layout()
plt.show()''',
        "# Visualizes why value iteration uses max over actions: tallest bar is the winning action here.",
    )
    + block(
        "BLOCK: Read the max numerically (ties possible, but not in this tiny demo)",
        'print("\\nBest action value from state 4:", max(action_returns))\nprint("Full VI repeats this max idea for every state, every sweep.")',
        "# Connects the plot back to the Bellman optimality operator.",
    )
).strip() + "\n"


CELL_14 = (
    block(
        "CELL: Value iteration + greedy extraction + driver prints/plots",
        "",
        "# Defines the planning functions, then runs them end-to-end.",
    ).strip()
    + "\n\n"
    + block(
        "FUNCTION: value_iteration(gamma, theta)",
        '''def value_iteration(gamma=GAMMA, theta=1e-6):
    values = np.zeros(N_STATES)
    deltas = []

    while True:
        delta = 0.0
        new_values = values.copy()
        for state in range(N_STATES):
            if state in TERMINAL_STATES:
                continue
            action_returns = []
            for action in range(len(ACTIONS)):
                next_state, reward = transition(state, action)
                action_returns.append(reward + gamma * values[next_state])
            best_value = max(action_returns)
            delta = max(delta, abs(best_value - values[state]))
            new_values[state] = best_value
        values = new_values
        deltas.append(delta)
        if delta < theta:
            break

    return values, deltas''',
        "# Synchronous sweeps: read old V, write new V for all states, repeat until updates are tiny.",
        "# deltas records the largest |change| per sweep (used by plot_deltas).",
    )
    + block(
        "FUNCTION: greedy_policy_from_values(values, gamma)",
        '''def greedy_policy_from_values(values, gamma=GAMMA):
    policy = np.zeros(N_STATES, dtype=int)
    for state in range(N_STATES):
        if state in TERMINAL_STATES:
            continue
        action_returns = []
        for action in range(len(ACTIONS)):
            next_state, reward = transition(state, action)
            action_returns.append(reward + gamma * values[next_state])
        policy[state] = int(np.argmax(action_returns))
    return policy''',
        "# Argmax of the same one-step returns: turns converged V into a deterministic greedy policy.",
    )
    + block(
        "BLOCK: Run planning, print tables, print short summary, show figures",
        '''optimal_values, deltas = value_iteration()
optimal_policy = greedy_policy_from_values(optimal_values)

print_values(optimal_values)
print_policy(optimal_policy)
print(f"\\nValue iteration converged in {len(deltas)} sweeps.")
print("Final Bellman update size:", deltas[-1])

print("\\nSummary:")
print("- Value iteration applies the Bellman optimality update directly.")
print("- It produces optimal state values for this small known MDP.")
print("- A greedy policy can be extracted from those final values.")
print("- In the next notebook, you move from planning in a known model to working with Gym environments.")

plot_values_and_policy(optimal_values, optimal_policy, title="Value iteration result")
plot_deltas(deltas)''',
        "# Driver: no new math here—just calls the functions defined above and reuses plotting helpers.",
    )
).strip() + "\n"


CELL_16 = (
    block(
        "CELL: Optional auto-visual recap (generic scanner)",
        "",
        "# Looks for small numeric variables in globals() and plots up to three; else a tiny summary.",
    ).strip()
    + "\n\n"
    + block(
        "BLOCK: Imports",
        "import numbers\nimport numpy as np\nimport matplotlib.pyplot as plt",
        "# `numbers` is included for consistency with other course notebooks using numeric checks.",
    )
    + block(
        "FUNCTION: _is_number(value)",
        '''def _is_number(value):
    return isinstance(value, (int, float, np.integer, np.floating)) and not isinstance(value, bool)''',
        "# Scalar numeric check; rejects bool because bool is a subclass of int in Python.",
    )
    + block(
        "FUNCTION: _as_numeric_dict(value)",
        '''def _as_numeric_dict(value):
    if not isinstance(value, dict) or not value or len(value) > 12:
        return None
    converted = []
    for item in value.values():
        if not _is_number(item):
            return None
        converted.append(float(item))
    return [str(key) for key in value.keys()], np.asarray(converted, dtype=float)''',
        "# Returns (labels, values) for a bar chart only if the dict is small and all-numeric.",
    )
    + block(
        "FUNCTION: _as_numeric_array(value, dims)",
        '''def _as_numeric_array(value, dims):
    try:
        array = np.asarray(value, dtype=float)
    except Exception:
        return None
    if array.ndim != dims:
        return None
    if dims == 1 and not (2 <= array.size <= 200):
        return None
    if dims == 2 and array.size > 400:
        return None
    return array''',
        "# Safe coercion to float ndarray with rank and size caps (keeps recap plots lightweight).",
    )
    + block(
        "BLOCK: Build search order (preferred names, then sorted globals)",
        '''priority_names = [
    "reward_history", "episode_rewards", "returns", "value_history", "q_values", "Q", "V",
    "scores", "metrics", "counts", "reward_grid", "values", "allocations", "application_scores"
]

skip_names = {"np", "plt", "numbers", "math"}
candidates = []
seen = set()
search_space = priority_names + sorted(name for name in globals() if not name.startswith("_"))''',
        "# Tries common RL variable names first, then scans the rest of the global namespace.",
    )
    + block(
        "BLOCK: Scan globals and collect up to three plottable objects",
        '''for name in search_space:
    if name in seen or name not in globals() or name in skip_names:
        continue
    seen.add(name)
    value = globals()[name]

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
            break''',
        "# Priority order inside the loop: dict chart, else heatmap, else 1D line series.",
    )
    + block(
        "BLOCK: Render either fallback summary or the discovered plots",
        '''if not candidates:
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
    fig, axes = plt.subplots(1, len(candidates), figsize=(5 * len(candidates), 3.8))
    if len(candidates) == 1:
        axes = [axes]

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
            image = ax.imshow(payload, aspect="auto", cmap="viridis")
            ax.set_title(f"{name} (heatmap)")
            fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)

    plt.tight_layout()
    plt.show()''',
        "# If nothing matched, show a coarse object-count summary instead of failing silently.",
    )
).strip() + "\n"


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
