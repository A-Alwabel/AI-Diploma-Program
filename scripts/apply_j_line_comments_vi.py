#!/usr/bin/env python3
"""
Option ج: insert one explanatory # comment line IMMEDIATELY ABOVE every executable
code line in 03_value_iteration.ipynb cells 8, 11, 14, 16.

- Keeps blank lines as-is.
- Keeps existing full-line # comments as-is (does not stack another # on top of them).
- Adds a comment above any non-blank line that is not already a comment.
"""
import json
import re
from pathlib import Path

NB = Path("Course 09/unit1-rl-fundamentals/examples/03_value_iteration.ipynb")
TARGET_CELLS = (8, 11, 14, 16)

_APPEND_RE = re.compile(r"\.append\(")


def describe(stripped: str) -> str:
    """Short English note for one logical line (student-facing)."""
    s = stripped
    if s.endswith(":") and s.startswith("def "):
        name = re.search(r"def\s+(\w+)\s*\(", s)
        nm = name.group(1) if name else "function"
        return f"Define function `{nm}` (starts a new indented block below)."
    if s in ("{", "}"):
        return "Part of a dict/set literal layout (syntax grouping)."
    if re.match(r"^\d+\s*:\s*\(", s):
        return "One entry in ACTION_TO_DELTA: maps an action id to a (d_row, d_col) move on the grid."
    if s.startswith("import "):
        return "Import a Python module into this notebook kernel namespace."
    # f-strings often contain "=" inside {...}; must run before the generic "=" heuristic.
    if s.startswith("f\"") or s.startswith("f'") or s.startswith('f"""') or s.startswith("f'''"):
        return "Build a formatted string (f-string) with embedded values for printing/titles."
    if re.fullmatch(r"\)+[,;]?", s):
        return "Close the parentheses opened earlier (end this function call / grouping)."
    if s.startswith("print("):
        return "Print text to the notebook cell output (console)."
    if s.startswith("np."):
        return "Call a NumPy helper (array creation, options, or array conversion)."
    if s.startswith("plt."):
        return "Call a Matplotlib pyplot helper (figure/axes/plot/show)."
    if s.startswith("fig."):
        return "Configure or update the active Matplotlib Figure object."
    if s.startswith("return "):
        return "Return a value from this function to its caller."
    if s.startswith("if "):
        return "Branch: only run the next indented lines when this condition is true."
    if s == "continue":
        return "Skip the rest of this loop body and jump to the next iteration."
    if s == "break":
        return "Exit the nearest enclosing loop immediately."
    if s.startswith("for "):
        return "Loop header: repeat the indented block for each item in the iterable."
    if s.startswith("while "):
        return "Loop header: repeat while the condition stays true."
    if s.startswith("elif "):
        return "Else-if branch: checked only when previous conditions were false."
    if s.startswith("else:"):
        return "Else branch: runs when the matching if/elif chain was not taken."
    if _APPEND_RE.search(s):
        return "Append one value to a list (mutates the list in place)."
    if "=" in s and not s.startswith("==") and not s.startswith("!="):
        if s.startswith("ACTIONS"):
            return "Create the list of action names (their indices are the numeric action ids)."
        if "TERMINAL_STATES" in s:
            return "Build the set of terminal state ids (used to skip Bellman backups)."
        if s.startswith("N_ROWS"):
            return "Set grid height and width in cells (3x3 in this toy MDP)."
        if s.startswith("N_STATES"):
            return "Total number of states = rows * columns (flattened indices 0..N-1)."
        if s.startswith("ACTION_TO_ARROW"):
            return "Map each action id to a Unicode arrow symbol for policy printing/plotting."
        if s.startswith("GOAL_STATE") or s.startswith("PIT_STATE"):
            return "Pick which flat state ids are special terminals for rewards in transition()."
        if s.startswith("GAMMA"):
            return "Set discount factor gamma used inside r + gamma * V(s') targets."
        if s.startswith("values") or s.startswith("state ") or s.startswith("state="):
            return "Create or choose a variable used in the Bellman warm-up demo."
        if s.startswith("action_returns"):
            return "Create a Python list that will store one scalar target per action."
        if s.startswith("policy"):
            return "Create or update the greedy policy array (one int action id per state)."
        if s.startswith("deltas"):
            return "Append or initialize the per-sweep convergence trace list."
        if s.startswith("delta"):
            return "Track how much the value table moved during the current sweep (or max change)."
        if s.startswith("new_values"):
            return "Hold the updated V table for this sweep before swapping it into values."
        if s.startswith("optimal_values") or s.startswith("optimal_policy"):
            return "Store the planning outputs from running value_iteration / greedy extraction."
        if s.startswith("grid"):
            return "Create the 2D array backing the value heatmap (NaN marks unused cells)."
        if s.startswith("im ") or s.startswith("im="):
            return "Capture the AxesImage object returned by imshow (used for the colorbar)."
        if s.startswith("fig,") or s.startswith("fig, axes"):
            return "Unpack Matplotlib figure and axes array created by subplots()."
        if s.startswith("value_grid"):
            return "Convert the 1D value vector into a 2D layout suitable for imshow()."
        if s.startswith("row ") or s.startswith("row="):
            return "Use a temporary list to format one printed row of the grid."
        if s.startswith("r ") and "range(N_ROWS)" in s:
            return "Outer loop over grid rows when printing values/policy."
        if s.startswith("c ") and "range(N_COLS)" in s:
            return "Inner loop over grid columns when printing values/policy."
        if s.startswith("s ") and "to_state" in s:
            return "Convert (row, col) to the flat state id used by arrays like values[s]."
        if s.startswith("label ") or s.startswith("symbol "):
            return "Choose what text to draw in this cell for goals/pits vs numeric values/arrows."
        if s.startswith("next_state") or s.startswith("reward"):
            return "Unpack the one-step model output from transition(state, action)."
        if s.startswith("target"):
            return "Compute one Bellman backup candidate: reward + gamma * V(next_state)."
        if s.startswith("best_value"):
            return "Take the Bellman optimality max over the per-action backup list."
        if s.startswith("dict_payload") or s.startswith("array_1d") or s.startswith("array_2d"):
            return "Try to interpret a global variable as a plottable payload (or None if not)."
        if s.startswith("candidates.append"):
            return "Record a discovered plottable object as a (kind, name, payload) tuple."
        if s.startswith("summary"):
            return "Build a small dict used only for the fallback summary bar chart."
        if s.startswith("priority_names"):
            return "Preferred global names to try first when auto-picking lesson plots."
        if s.startswith("skip_names"):
            return "Names that are never lesson metrics (imports / plotting handles)."
        if s.startswith("search_space"):
            return "Ordered list of global names to scan for plottable numeric artifacts."
        if s.startswith("seen"):
            return "Track which names were already visited to avoid duplicates."
        if s.startswith("name "):
            return "Current global variable name being inspected in the scanner loop."
        if s.startswith("value "):
            return "The runtime object bound to that global name."
        if s.startswith("array "):
            return "Temporary ndarray after coercion attempt inside _as_numeric_array()."
        if s.startswith("converted"):
            return "Collect numeric dict values after validation for plotting."
        if s.startswith("labels") or (s.startswith("values") and "payload" in s):
            return "Unpack plotting payload for dict bar charts (keys vs numeric values)."
        if s.startswith("image "):
            return "Image handle returned by imshow for attaching a colorbar."
        if s.startswith("idx") and "enumerate" in s:
            return "Loop index used to place text labels above each summary bar."
        return "Assign/update a variable used later in this cell or in other cells."
    if s.startswith("ACTIONS"):
        return "Literal list of action names (indices match ACTION_TO_DELTA keys)."
    if s.startswith("ACTION_TO_DELTA"):
        return "Start a dict literal mapping each action id to a movement delta on the grid."
    if s.startswith("plt.show()"):
        return "Render/show the current figure in the notebook output."
    if s.startswith("plt.tight_layout()"):
        return "Adjust subplot spacing to reduce overlaps before showing the figure."
    if s.startswith("plt.legend()"):
        return "Draw a legend explaining labeled artists (e.g., the max reference line)."
    if s.startswith("plt.axhline"):
        return "Draw a horizontal reference line at y = max(action_returns) for comparison."
    if s.startswith("plt.bar"):
        return "Draw a bar chart comparing scalar targets across categorical actions."
    if s.startswith("plt.plot"):
        return "Plot y versus x (here: deltas vs implicit sweep indices 0..len-1)."
    if s.startswith("plt.figure"):
        return "Create a new figure window/canvas for the next plot commands."
    if s.startswith("plt.ylabel") or s.startswith("plt.xlabel") or s.startswith("plt.title"):
        return "Set an axis label or figure title to explain what the plot means."
    if s.startswith("plt.grid"):
        return "Turn on light grid lines to read values/sweeps from the plot more easily."
    if s.startswith("axes[") or s.startswith("ax."):
        return "Configure a specific subplot axis (limits, ticks, title, labels, plotting calls)."
    if s.startswith("fig.colorbar"):
        return "Add a colorbar beside a heatmap axis to map colors back to numeric values."
    if s.startswith("zip("):
        return "Iterate multiple sequences in parallel (pair each axis with one candidate plot)."
    if s.startswith("enumerate("):
        return "Loop with (index, value) pairs (here: index bars and align text labels)."
    if s.startswith("sum("):
        return "Aggregate a counted quantity across many objects (used in fallback summary)."
    if s.startswith("isinstance("):
        return "Runtime type check used to validate objects before plotting."
    if s.startswith("callable("):
        return "Check whether an object is a function/method-like callable."
    if s.startswith("globals()"):
        return "Access the notebook kernel's global symbol table as a dict-like mapping."
    if s.startswith("len("):
        return "Read a length/count (number of sweeps, candidates, list size, etc.)."
    if s.startswith("max("):
        return "Take the maximum of a collection (best action target or largest Bellman change)."
    if s.startswith("min(") or s.startswith("abs("):
        return "Math helper used for clamping coordinates or measuring change magnitude."
    if s.startswith("divmod("):
        return "Divide state by column count to recover (row, col) under row-major indexing."
    if s.startswith("int("):
        return "Cast a numeric type to int (here: store discrete action ids in policy)."
    if s.startswith("float("):
        return "Cast a value to float for numeric plotting pipelines."
    if s.startswith("str("):
        return "Convert an object to a string (here: dict keys become x tick labels)."
    if s.startswith("range("):
        return "Build a simple integer sequence for loops or tick positions."
    if s.startswith("sorted("):
        return "Return a sorted list (here: scan global names in deterministic order)."
    if s in ("try:", "except Exception:"):
        return "Try/except: catch conversion failures without crashing the recap cell."
    if s.startswith("except"):
        return "Exception handler: return a safe fallback when conversion fails."
    if s.startswith("try"):
        return "Try block start: attempt a risky conversion before validating shape."
    if s.startswith("pass"):
        return "No-op placeholder (not used here, but valid Python)."
    if s.startswith("raise"):
        return "Explicitly raise an error (not used here)."
    if s.startswith("open("):
        return "File IO (not used here)."
    # Fallback: still always provide *something* above each code line for option ج.
    if len(s) > 90:
        return f"Execute: {s[:90]} …"
    return f"Execute: {s}"


def strip_prior_j_comments(src: str) -> str:
    """Remove a prior J-mode comment line when it matches describe(next line) or known bad legacy pairs."""
    lines = src.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        cur = lines[i]
        if i + 1 < len(lines):
            nxt = lines[i + 1]
            if (
                cur.strip()
                and cur.lstrip().startswith("#")
                and nxt.strip()
                and not nxt.lstrip().startswith("#")
                and not cur.strip().startswith("# ---")
                and "BLOCK:" not in cur
            ):
                indent = nxt[: len(nxt) - len(nxt.lstrip())]
                expected = f"{indent}# {describe(nxt.strip())}"
                if cur.rstrip() == expected.rstrip():
                    i += 1
                    continue
                # Legacy: "=" heuristic mis-fired on f-strings inside print(...).
                if "Assign/update a variable used later" in cur and (
                    nxt.lstrip().startswith('f"')
                    or nxt.lstrip().startswith("f'")
                    or nxt.lstrip().startswith('f"""')
                    or nxt.lstrip().startswith("f'''")
                ):
                    i += 1
                    continue
                if cur.strip() == "# Execute: )" and nxt.strip() == ")":
                    i += 1
                    continue
                # Legacy: fallback Execute: literally echoed the next code line.
                rest = cur.strip()[1:].lstrip()
                if rest.startswith("Execute:") and rest[len("Execute:") :].strip() == nxt.strip():
                    i += 1
                    continue
        out.append(cur)
        i += 1
    tail = "\n" if src.endswith("\n") or not src else ""
    return "\n".join(out) + tail


def annotate_source(src: str) -> str:
    out_lines: list[str] = []
    for raw in src.splitlines():
        if raw.strip() == "":
            out_lines.append(raw)
            continue
        if raw.lstrip().startswith("#"):
            out_lines.append(raw)
            continue
        indent = raw[: len(raw) - len(raw.lstrip())]
        note = describe(raw.strip())
        out_lines.append(f"{indent}# {note}")
        out_lines.append(raw)
    return "\n".join(out_lines) + "\n"


def main() -> None:
    nb = json.loads(NB.read_text(encoding="utf-8"))
    for idx in TARGET_CELLS:
        cell = nb["cells"][idx]
        if cell.get("cell_type") != "code":
            raise SystemExit(f"cell {idx} is not code")
        src = "".join(cell["source"])
        src = strip_prior_j_comments(src)
        cell["source"] = [ln + "\n" for ln in annotate_source(src).splitlines()]
    NB.write_text(json.dumps(nb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("updated", NB, "cells", TARGET_CELLS)


if __name__ == "__main__":
    main()
