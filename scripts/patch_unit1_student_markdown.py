#!/usr/bin/env python3
"""
One-off patcher: add weak-coder scaffolding to Unit 1 example notebooks (Course 09).

- Appends ### If Python feels hard right now to Lesson Brief when missing.
- Replaces generic ### Step Guide blocks with lesson-specific text.
- Appends a short **For weaker coders** line to Closing Takeaway when missing.

Usage (repo root): python3 scripts/patch_unit1_student_markdown.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "Course 09/unit1-rl-fundamentals/examples"

WEAK_BLOCK = """### If Python feels hard right now

- Run code cells **from top to bottom** the first time; later you can re-run one cell after you change it.
- In code cells, a line that starts with `# ` (hash + space) is a **hint for the very next line**—read the hint, then read the code under it.
- You do **not** need to memorize syntax. Follow the story: *what is stored*, *what gets printed*, and *what the plot is trying to show*.
- If something errors, read the last line of the red traceback first—it usually names the problem in plain language.
"""


def _src_lines(text: str) -> list[str]:
    if not text.endswith("\n"):
        text += "\n"
    return text.splitlines(keepends=True)


def _ensure_weak_lesson(nb: dict, cell_idx: int) -> None:
    cell = nb["cells"][cell_idx]
    src = "".join(cell["source"])
    if "### If Python feels hard" in src:
        return
    cell["source"] = _src_lines(src.rstrip() + "\n\n" + WEAK_BLOCK)


def _replace_step(nb: dict, cell_idx: int, body: str) -> None:
    cell = nb["cells"][cell_idx]
    if cell["cell_type"] != "markdown":
        raise SystemExit(f"cell {cell_idx} not markdown")
    cell["source"] = _src_lines(body.strip() + "\n")


def _append_closing_weak(nb: dict, cell_idx: int, paragraph: str) -> None:
    cell = nb["cells"][cell_idx]
    src = "".join(cell["source"])
    if "**For weaker coders:**" in src:
        return
    cell["source"] = _src_lines(src.rstrip() + "\n\n" + paragraph.strip() + "\n")


def main() -> None:
    # --- 01 MDP example ---
    p01 = EXAMPLES / "01_mdp_example.ipynb"
    nb01 = json.loads(p01.read_text(encoding="utf-8"))
    _ensure_weak_lesson(nb01, 2)
    _replace_step(
        nb01,
        8,
        """### Step Guide

**What this cell does:** Loads NumPy and Matplotlib, then defines the tiny 3×3 **grid**, the **action names**, and the **move map** used in every cell below.

**How to read it (weak Python OK):** Treat this as a settings screen. Circle these names: `ACTIONS`, `ACTION_TO_DELTA`, `START`, `GOAL`, and `PIT`.

**What to expect in the output:** Often nothing yet from imports—later prints will use these variables.

**If you feel lost:** Skip the dict punctuation on the first pass; only notice that each action points to a `(row, col)` step.
""",
    )
    _replace_step(
        nb01,
        11,
        """### Step Guide

**What this cell does:** Defines `rollout` plus the toy **transition and reward** rules so you can watch one walk through the grid.

**How to read it (weak Python OK):** Chase one story: *current state → choose action → next state → reward*. Every `print` is showing one step of that story.

**What to expect in the output:** Text lines that look like a tiny game log (states visited and rewards collected).

**If you feel lost:** Ignore nested `if` details at first—just check whether the agent ever reaches the goal or falls in the pit.
""",
    )
    _replace_step(
        nb01,
        15,
        """### Step Guide

**What this cell does:** Tries to auto-build a **small recap plot** from numbers that already exist in the kernel (values, rewards, etc.).

**How to read it (weak Python OK):** If a chart appears, read axes first. If you see only text, the cell still ran—there may be nothing easy to plot.

**What to expect in the output:** One quick figure or a short “nothing plotted” style message.

**If you feel lost:** Use this as a second pass **after** you can narrate the MDP in words without the code.
""",
    )
    _append_closing_weak(
        nb01,
        17,
        """**For weaker coders:** Sketch the 3×3 grid on paper, mark the goal and pit, and trace one action from `START`. If that picture makes sense, you already understand the MDP better than memorizing symbols.""",
    )
    p01.write_text(json.dumps(nb01, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # --- 02 MDP solving ---
    p02 = EXAMPLES / "02_mdp_solving.ipynb"
    nb02 = json.loads(p02.read_text(encoding="utf-8"))
    _ensure_weak_lesson(nb02, 1)
    _replace_step(
        nb02,
        7,
        """### Step Guide

**What this cell does:** Imports NumPy/Matplotlib and prints the lesson banner—sets up printing style for small value tables.

**How to read it (weak Python OK):** Confirm the cell runs with no red error. You do not need `np.set_printoptions` on day one.

**What to expect in the output:** A title line and tidy number formatting later in the notebook.

**If you feel lost:** This cell is only “turn on the calculator display.” The ideas start in the next cell.
""",
    )
    _replace_step(
        nb02,
        10,
        """### Step Guide

**What this cell does:** Defines a **fixed policy** (a table of actions) and `evaluate_policy`, which estimates how good that policy is in every state.

**How to read it (weak Python OK):** Think “report card for a frozen plan.” The loops fill `values[state]` until they stop changing much.

**What to expect in the output:** Arrays of numbers you can compare state by state.

**If you feel lost:** Watch `theta` and “until stable”—that only means “keep averaging future rewards until the updates get tiny.”
""",
    )
    _replace_step(
        nb02,
        13,
        """### Step Guide

**What this cell does:** Adds `improve_policy` and **`policy_iteration`**: improve the plan, re-score it, repeat until the policy stops changing.

**How to read it (weak Python OK):** Memorize the alternation: **evaluate → improve → evaluate → improve**. Each round should feel like tightening a loose bolt.

**What to expect in the output:** Round counts and before/after policies you can compare.

**If you feel lost:** Ignore long loops at first; look only at whether the printed policy array changes between rounds.
""",
    )
    _replace_step(
        nb02,
        15,
        """### Step Guide

**What this cell does:** Optional **auto-plots** that scan for numeric lesson variables and chart them.

**How to read it (weak Python OK):** Charts are optional memory aids. Read axis labels before you interpret colors or bar heights.

**What to expect in the output:** A figure or a message that nothing matched the auto-plot rules.

**If you feel lost:** Re-run the policy iteration cell, then return here once the workspace actually holds arrays to plot.
""",
    )
    _append_closing_weak(
        nb02,
        17,
        """**For weaker coders:** On two sticky notes write **evaluate** and **improve**; move them in order each loop. If you can narrate that cycle aloud, you understood policy iteration.""",
    )
    p02.write_text(json.dumps(nb02, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # --- 04 Gymnasium ---
    p04 = EXAMPLES / "04_openai_gym_setup.ipynb"
    nb04 = json.loads(p04.read_text(encoding="utf-8"))
    _ensure_weak_lesson(nb04, 1)
    _replace_step(
        nb04,
        5,
        """### Step Guide

**What this cell does:** Installs **Gymnasium** (and friends) with `%pip`, then imports `gymnasium as gym`.

**How to read it (weak Python OK):** `%pip` is a notebook-only install command. If it finishes without red text, you are ready for the next cell.

**What to expect in the output:** Progress lines from pip; the kernel may ask you to restart once—follow the message if it appears.

**If you feel lost:** Treat errors here as “missing app store click”—fix installs before any `gym.make` calls.
""",
    )
    _replace_step(
        nb04,
        8,
        """### Step Guide

**What this cell does:** **Part 1** — sanity checks: Gymnasium version, listing a few env ids, and your first `gym.make` smoke test.

**How to read it (weak Python OK):** Read each `print` block as a checklist item. Green text (or no crash) means “this tool is on.”

**What to expect in the output:** Version strings and maybe a short env description.

**If you feel lost:** Your only goal is: “I can create an environment object without an error.”
""",
    )
    _replace_step(
        nb04,
        11,
        """### Step Guide

**What this cell does:** **Part 2** — inspect **observation** and **action spaces** (what the agent sees vs what it can do).

**How to read it (weak Python OK):** Compare two English questions: *What fits in `observation_space`?* and *What fits in `action_space`?*

**What to expect in the output:** `Box`, `Discrete`, shapes, and bounds—copy them into your notes; later algorithms assume you know them.

**If you feel lost:** Write one sentence: “State looks like ___; actions are ___.” That sentence is enough for now.
""",
    )
    _replace_step(
        nb04,
        14,
        """### Step Guide

**What this cell does:** **Part 3** — the real loop: `reset()`, then repeated `step(action)` calls, reading **observation, reward, terminated, truncated, info**.

**How to read it (weak Python OK):** Watch for five return values from `step`. You only need to know: *new situation*, *score change*, *is it over?*

**What to expect in the output:** Step-by-step prints showing observations and rewards.

**If you feel lost:** Pause after the first `reset` print—say aloud what each number means before reading the rest of the cell.
""",
    )
    _replace_step(
        nb04,
        17,
        """### Step Guide

**What this cell does:** **Part 4** — compares a few classic environments so you see different observation/action shapes side by side.

**How to read it (weak Python OK):** Make a tiny table on paper: env name → observation kind → action kind.

**What to expect in the output:** Several short env summaries printed back-to-back.

**If you feel lost:** Ignore deep internals; this cell is only “tour different playgrounds before practicing tricks.”
""",
    )
    _replace_step(
        nb04,
        20,
        """### Step Guide

**What this cell does:** Defines **`run_random_episode`** — a helper that rolls out random actions so you can watch trajectories without learning yet.

**How to read it (weak Python OK):** Follow inputs `env_name`, `max_steps`, `seed` and the returned **total reward** and **steps**.

**What to expect in the output:** Sample episodes and cumulative rewards for a couple of envs.

**If you feel lost:** Read the function like a recipe card: ingredients (inputs) → steps (loop) → finished plate (return values).
""",
    )
    _replace_step(
        nb04,
        24,
        """### Step Guide

**What this cell does:** Optional **auto-visual recap** of numeric variables sitting in the kernel after the lesson runs.

**How to read it (weak Python OK):** Treat plots as bonus flashcards, not the definition of success.

**What to expect in the output:** Charts or a polite “nothing to plot” message.

**If you feel lost:** Re-run Parts 1–3 so there are numbers in memory, then try this cell again.
""",
    )
    _append_closing_weak(
        nb04,
        26,
        """**For weaker coders:** Your first real win is knowing what `reset()` vs `step()` return. Until that feels obvious, treat every algorithm cell as “not yet for me.”""",
    )
    p04.write_text(json.dumps(nb04, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # --- 05 Epsilon-greedy ---
    p05 = EXAMPLES / "05_exploration_strategies_epsilon_greedy.ipynb"
    nb05 = json.loads(p05.read_text(encoding="utf-8"))
    _ensure_weak_lesson(nb05, 1)
    _replace_step(
        nb05,
        5,
        """### Step Guide

**What this cell does:** Installs plotting/math helpers (`%pip`) and imports what the epsilon-greedy demos need.

**How to read it (weak Python OK):** If the cell ends quietly, you are ready. If `%pip` complains, fix that before any plots.

**What to expect in the output:** Pip logs and a friendly “libraries imported” confirmation.

**If you feel lost:** This is setup only—no exploration math yet.
""",
    )
    _replace_step(
        nb05,
        8,
        """### Step Guide

**What this cell does:** **Part 1** — explains epsilon-greedy in words: with probability ε explore, else exploit the best-known action.

**How to read it (weak Python OK):** Translate ε to a habit: “I roll dice; sometimes I ignore my best idea on purpose.”

**What to expect in the output:** Printed rules of thumb about ε values and decay schedules.

**If you feel lost:** Write ε = 0.1 as “10% random, 90% greedy” in your notes—that one line unlocks the whole lesson.
""",
    )
    _replace_step(
        nb05,
        11,
        """### Step Guide

**What this cell does:** **Part 2** — implements `epsilon_greedy_action` and runs a short scripted demo so you can **count explore vs exploit** decisions.

**How to read it (weak Python OK):** Watch the printed table of counts—does randomness match the ε you typed?

**What to expect in the output:** Step-by-step actions labeled explore/exploit plus totals.

**If you feel lost:** Change only `epsilon` and rerun; your counts should shift in a predictable direction.
""",
    )
    _replace_step(
        nb05,
        14,
        """### Step Guide

**What this cell does:** **Part 3** — plots how different ε values change how often each action is picked (same Q-values, different randomness).

**How to read it (weak Python OK):** Read the legend and axis titles before interpreting bar heights.

**What to expect in the output:** A matplotlib figure comparing exploration percentages.

**If you feel lost:** If the plot fails, rerun Part 2 first so `q_values` and counters exist.
""",
    )
    _replace_step(
        nb05,
        17,
        """### Step Guide

**What this cell does:** **Part 4** — walks through **epsilon decay** (start curious, end greedy) on a tiny bandit-style simulation.

**How to read it (weak Python OK):** Track how ε shrinks over episodes and how average reward creeps upward.

**What to expect in the output:** Text logs or small tables showing schedules and rewards.

**If you feel lost:** Ignore bandit details; only ask “did exploration shrink over time?” That is the lesson.
""",
    )
    _replace_step(
        nb05,
        20,
        """### Step Guide

**What this cell does:** Loads standard imports for any follow-on plots or checks (NumPy/Matplotlib helpers).

**How to read it (weak Python OK):** Another “tool belt” cell—no new RL concept, just libraries.

**What to expect in the output:** Usually silent aside from import side effects.

**If you feel lost:** If everything above ran, you can skim this cell quickly.
""",
    )
    _replace_step(
        nb05,
        24,
        """### Step Guide

**What this cell does:** Optional **auto-plots** summarizing numeric artifacts from the epsilon experiments.

**How to read it (weak Python OK):** Use charts to confirm patterns you already saw in prints.

**What to expect in the output:** Figures or a no-op message.

**If you feel lost:** Re-run Parts 2–4 so variables exist, then try this cell again.
""",
    )
    _append_closing_weak(
        nb05,
        26,
        """**For weaker coders:** If you can explain ε as “how often I try something random on purpose,” you already grasp epsilon-greedy; everything else is practice.""",
    )
    p05.write_text(json.dumps(nb05, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # --- 06 States / actions / rewards ---
    p06 = EXAMPLES / "06_solving_rl_problems_states_actions_rewards.ipynb"
    nb06 = json.loads(p06.read_text(encoding="utf-8"))
    _ensure_weak_lesson(nb06, 1)
    _replace_step(
        nb06,
        5,
        """### Step Guide

**What this cell does:** `%pip` installs helpers, then imports NumPy/Matplotlib for the design exercises below.

**How to read it (weak Python OK):** Treat as setup—success means “no red traceback.”

**What to expect in the output:** Pip chatter and a short confirmation print.

**If you feel lost:** Fix installs here before any simulation cells.
""",
    )
    _replace_step(
        nb06,
        8,
        """### Step Guide

**What this cell does:** **Part 1** — defines several **state representations** (full info vs partial observations) for the same toy problems.

**How to read it (weak Python OK):** Ask for each example: “What does the agent actually get to see each step?”

**What to expect in the output:** Printed descriptions of different state vectors.

**If you feel lost:** Copy one “good” and one “bad” state design into your notes side by side—the contrast is the lesson.
""",
    )
    _replace_step(
        nb06,
        11,
        """### Step Guide

**What this cell does:** **Part 2** — compares **discrete vs continuous action spaces** and when each makes sense.

**How to read it (weak Python OK):** Link actions to hardware: keyboard taps vs steering wheel angles.

**What to expect in the output:** Textual comparisons and small numeric demos.

**If you feel lost:** Write one sentence per world: “Actions here are ___ because ___.”
""",
    )
    _replace_step(
        nb06,
        14,
        """### Step Guide

**What this cell does:** **Part 3** — reward shaping demos (sparse vs dense, penalties, shaping traps).

**How to read it (weak Python OK):** For each reward tweak ask: “Does this number push the agent toward the real goal, or toward a shortcut?”

**What to expect in the output:** Totals or tables showing how different rewards change behavior summaries.

**If you feel lost:** Ignore fancy terms—only track whether rewards go up when the agent does the right human-level thing.
""",
    )
    _replace_step(
        nb06,
        17,
        """### Step Guide

**What this cell does:** **Part 4** — ties the design choices to **simple simulations** so you see consequences, not just definitions.

**How to read it (weak Python OK):** Read outputs like lab measurements: what went better when the design improved?

**What to expect in the output:** Short simulation logs or aggregate scores.

**If you feel lost:** Pick one metric (average return, success rate) and only watch that number across runs.
""",
    )
    _replace_step(
        nb06,
        20,
        """### Step Guide

**What this cell does:** Re-imports/plugs in plotting helpers after the conceptual sections (same tool belt pattern).

**How to read it (weak Python OK):** Another import cell—skim if the earlier parts already ran.

**What to expect in the output:** Usually silent.

**If you feel lost:** If you see `NameError` later, come back and run this cell.
""",
    )
    _replace_step(
        nb06,
        24,
        """### Step Guide

**What this cell does:** Optional **auto-plots** for numeric summaries produced along the way.

**How to read it (weak Python OK):** Use charts to reinforce what you already said in English.

**What to expect in the output:** Figures or a soft no-op message.

**If you feel lost:** Re-run Parts 1–4 before expecting plots here.
""",
    )
    _append_closing_weak(
        nb06,
        26,
        """**For weaker coders:** Pick one story (robot, game, trading). Write state, action, and reward as one plain English sentence each—if you can, you are doing RL design correctly.""",
    )
    p06.write_text(json.dumps(nb06, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # --- 07 Mini projects ---
    p07 = EXAMPLES / "07_mini_projects_cartpole_frozenlake_qlearning_dqn.ipynb"
    nb07 = json.loads(p07.read_text(encoding="utf-8"))
    _ensure_weak_lesson(nb07, 1)
    _replace_step(
        nb07,
        5,
        """### Step Guide

**What this cell does:** `%pip` installs Gymnasium, Torch (for the DQN preview), and plotting helpers used later.

**How to read it (weak Python OK):** Torch is large—expect a wait once. A coffee break is normal.

**What to expect in the output:** Pip progress and success prints.

**If you feel lost:** Do not run the DQN section until this cell succeeds without errors.
""",
    )
    _replace_step(
        nb07,
        8,
        """### Step Guide

**What this cell does:** **Part 1** — implements a tiny **tabular Q-learning** update loop on a discrete toy so you can see the Q-table change.

**How to read it (weak Python OK):** Think spreadsheet: rows = states, columns = actions, numbers = “how good seems taking this action here.”

**What to expect in the output:** Training logs and a heatmap or printed table of Q-values.

**If you feel lost:** Track only one state row across iterations—does the best action column brighten over time?
""",
    )
    _replace_step(
        nb07,
        11,
        """### Step Guide

**What this cell does:** **Part 2** — runs Q-learning on **FrozenLake** (slippery grid) so you connect the table to a classic Gym env.

**How to read it (weak Python OK):** Compare success rate before vs after training—did the agent learn to avoid holes?

**What to expect in the output:** Episode rewards, rolling averages, maybe a policy map.

**If you feel lost:** If training is slow, lower episode counts in the config block first—small proof beats big waits.
""",
    )
    _replace_step(
        nb07,
        14,
        """### Step Guide

**What this cell does:** **Part 3** — **discretizes CartPole** so tabular Q-learning can still run on a continuous observation env.

**How to read it (weak Python OK):** Discretization = “bucket similar numbers into the same bin.” That makes the spreadsheet finite again.

**What to expect in the output:** Training curves or average return prints for CartPole buckets.

**If you feel lost:** If buckets feel arbitrary, that is normal—here we only want the *idea* that continuity breaks pure tables.
""",
    )
    _replace_step(
        nb07,
        17,
        """### Step Guide

**What this cell does:** **Part 4** — **DQN preview**: tiny network + training loop showing why neural nets help when tables explode.

**How to read it (weak Python OK):** You are not expected to master PyTorch yet—watch how `loss` moves and whether the pole stays up longer over episodes.

**What to expect in the output:** Loss traces, episodic returns, maybe a short animation hook.

**If you feel lost:** Treat Torch tensors as “fancy numpy arrays” and skip layer definitions on the first pass.
""",
    )
    _replace_step(
        nb07,
        20,
        """### Step Guide

**What this cell does:** Loads **Torch** modules explicitly for the DQN preview (after the markdown warning about preview-only scope).

**How to read it (weak Python OK):** If you are skipping deep RL for now, you may still run this to avoid `ModuleNotFoundError` later.

**What to expect in the output:** Silent import success.

**If you feel lost:** This pairs with the markdown cell above it—read that blurb before the imports.
""",
    )
    _replace_step(
        nb07,
        24,
        """### Step Guide

**What this cell does:** Optional **auto-plots** for metrics gathered in the mini projects (returns, lengths, etc.).

**How to read it (weak Python OK):** Compare curves across parts: tabular vs discretized vs neural.

**What to expect in the output:** Charts or a gentle no-op.

**If you feel lost:** Re-run the part you care about so variables exist, then execute this recap cell.
""",
    )
    _append_closing_weak(
        nb07,
        26,
        """**For weaker coders:** The big fork is **small table of states** (Q-learning) vs **huge sensor vectors** (DQN). If you can explain that sentence, Unit 1 clicked.""",
    )
    p07.write_text(json.dumps(nb07, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Patched:", p01.name, p02.name, p04.name, p05.name, p06.name, p07.name)


if __name__ == "__main__":
    main()
