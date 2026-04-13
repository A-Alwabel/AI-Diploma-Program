"""
Shared J-line annotator: one explanatory full-line # comment above each non-comment
code line. Used for student-facing Course 09 notebooks.

- Strips prior J-mode comments when they match describe(next line) or legacy patterns.
- Uses ast + docstrings for richer one-line summaries on def / async def / class lines.
- Skips post-parse validation for cells that contain shell/line/cell magics (!, %, %%).
"""
from __future__ import annotations

import ast
import json
import re
import tokenize
from io import BytesIO
from pathlib import Path

_APPEND_RE = re.compile(r"\.append\(")

# Matplotlib axis J-lines (plain English for weak coders; must match describe() ax/axes branch).
_STUD_AXIS_NOTE_FIRST = (
    "Work on one plot panel: title, tick marks, axis labels, or drawings on that panel."
)
_STUD_AXIS_NOTE_MORE = "Same plot panel as the line above—one more small plotting tweak."

# Generic assignment J-lines (must match describe() fall-through for simple `=` lines).
_STUD_ASSIGN_NOTE_FIRST = "Save a value in a name so the next lines can read it."
_STUD_ASSIGN_NOTE_MORE = "Another assignment—same idea: store a value for the lines below."


def multiline_string_continuation_lines(src: str) -> set[int]:
    """
    1-based line numbers that fall inside a multiline STRING token, excluding the
    token's opening line (so we do not inject # lines into docstrings / multiline text).
    """
    skip_set: set[int] = set()
    readline = BytesIO(src.encode("utf-8")).readline
    try:
        for tok in tokenize.tokenize(readline):
            if tok.type != tokenize.STRING:
                continue
            start_line, _ = tok.start
            end_line, _ = tok.end
            if end_line > start_line:
                for ln in range(start_line + 1, end_line + 1):
                    skip_set.add(ln)
    except (tokenize.TokenError, IndentationError):
        return skip_set
    return skip_set


def _cell_has_ipython_magic(src: str) -> bool:
    for line in src.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("!") or s.startswith("%%"):
            return True
        if s.startswith("%") and not s.startswith("%%"):
            return True
    return False


def _params_preview(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    """Comma-separated parameter names for student-facing hints (no types)."""
    names: list[str] = []
    names.extend(a.arg for a in node.args.posonlyargs)
    names.extend(a.arg for a in node.args.args)
    if node.args.vararg:
        names.append("*" + node.args.vararg.arg)
    names.extend(a.arg for a in node.args.kwonlyargs)
    if node.args.kwarg:
        names.append("**" + node.args.kwarg.arg)
    if not names:
        return "no named parameters in the signature"
    head = ", ".join(names[:10])
    if len(names) > 10:
        head += ", ..."
    return head


def symbol_summaries(src: str) -> dict[int, str]:
    """Map 1-based source line number -> short English summary for def/class lines."""
    out: dict[int, str] = {}
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node)
            is_async = isinstance(node, ast.AsyncFunctionDef)
            label = "Async function" if is_async else "Function"
            if doc:
                one = " ".join(doc.strip().split())
                # Keep the one-line # header above `def` short for notebook readability.
                if len(one) > 90:
                    one = one[:87] + "..."
                out[node.lineno] = f"{label} `{node.name}` (what it does): {one}"
            else:
                params = _params_preview(node)
                out[node.lineno] = (
                    f"{label} `{node.name}` (what it does): no long English blurb here—read the "
                    f"indented lines top to bottom. Inputs you will see: {params}."
                )
        elif isinstance(node, ast.ClassDef):
            doc = ast.get_docstring(node)
            if doc:
                one = " ".join(doc.strip().split())
                if len(one) > 90:
                    one = one[:87] + "..."
                out[node.lineno] = f"Class `{node.name}` (what it does): {one}"
            else:
                out[node.lineno] = (
                    f"Class `{node.name}` (what it does): a reusable pattern for objects; "
                    "read the indented block to see fields and methods."
                )
    return out


def describe(stripped: str, line_no: int | None = None, summaries: dict[int, str] | None = None) -> str:
    """Short English note for one logical line (student-facing)."""
    if summaries and line_no is not None and line_no in summaries:
        return summaries[line_no]

    s = stripped
    if s.endswith(":") and (s.startswith("def ") or s.startswith("async def ")):
        name = re.search(r"def\s+(\w+)\s*\(", s)
        nm = name.group(1) if name else "function"
        label = "Async function" if s.startswith("async ") else "Function"
        return (
            f"{label} `{nm}` (what it does): read the indented lines under it in order—"
            "that is where the real behavior lives."
        )
    if s.endswith(":") and s.startswith("class "):
        m = re.search(r"class\s+(\w+)", s)
        nm = m.group(1) if m else "class"
        return (
            f"Class `{nm}` (what it does): read the indented block under it to see what each "
            "part stores or does."
        )
    if s in ("{", "}"):
        return "Part of a dict/set literal layout (syntax grouping)."
    if re.match(r"^\d+\s*:\s*\(", s):
        return "Dictionary/map entry: this key maps to the tuple/value on the right."
    if s.startswith("!"):
        return "Shell command (runs in the notebook kernel's OS shell)."
    if s.startswith("%%"):
        return "Cell magic: applies a special Jupyter/IPython mode to this cell."
    if s.startswith("%"):
        return "Line magic: Jupyter/IPython directive for this line only."
    if s.startswith("import ") or s.startswith("from "):
        return "Load a library so you can use its ready-made functions and types below."
    if s.startswith("f\"") or s.startswith("f'") or s.startswith('f"""') or s.startswith("f'''"):
        return "Build text with {…} holes filled in by variables (an f-string)."
    if re.fullmatch(r"\)+[,;]?", s):
        return "Close the parentheses opened earlier (end this function call / grouping)."
    if s.startswith("print("):
        return "Show text or numbers in the cell output area under the code."
    if s.startswith("torch.") or s.startswith("nn."):
        return "Call a PyTorch API (tensor/module/training-related)."
    if s.startswith("F.") or s.startswith("nn.functional"):
        return "Call a PyTorch functional API (activations, losses, ops)."
    if s.startswith("gym.") or s.startswith("spaces."):
        return "Call Gymnasium / classic Gym API (env, spaces, registration)."
    if s.startswith("np."):
        return "Use NumPy for fast numeric arrays and math on grids of numbers."
    if s.startswith("plt."):
        return "Use pyplot to create or tweak a figure (plot, labels, show, etc.)."
    if s.startswith("sns."):
        return "Use Seaborn for nicer statistical plots with less boilerplate."
    if s.startswith("pd."):
        return "Use pandas for tables (rows/columns) and CSV-style data work."
    if s.startswith("fig."):
        return "Change something about the whole figure (not just one small subplot)."
    if s.startswith("ax.") or s.startswith("axes["):
        return _STUD_AXIS_NOTE_FIRST
    if s.startswith("return "):
        return "Send a value back to whoever called this function."
    if s.startswith("yield "):
        return "Produce the next value for someone looping with 'for ... in this'."
    if s.startswith("await "):
        return "Wait here until an async task finishes (only in async code)."
    if s.startswith("if "):
        return "If the condition is True, run the indented block under this line."
    if s == "continue":
        return "Skip to the next lap of the loop (ignore the rest of this lap)."
    if s == "break":
        return "Stop the loop completely and continue after the loop block."
    if s.startswith("for "):
        return "Start a loop: repeat the indented block once per item in the sequence."
    if s.startswith("while "):
        return "Start a loop: repeat the indented block while the condition stays True."
    if s.startswith("elif "):
        return "Else-if: only checked when the earlier if/elif tests were False."
    if s.startswith("else:"):
        return "Else: run this block when none of the if/elif tests above matched."
    if s.startswith("with "):
        return "Safely open/use a resource; Python cleans up when the block ends."
    if s.startswith("assert "):
        return "Crash with a clear error if something you expect to be true is False."
    if _APPEND_RE.search(s):
        return "Add one new item to the end of a list (the list grows in place)."
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
        return _STUD_ASSIGN_NOTE_FIRST
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
        return "Draw a horizontal reference line for comparison on the y-axis."
    if s.startswith("plt.bar"):
        return "Draw a bar chart comparing scalar values across categories."
    if s.startswith("plt.plot"):
        return "Plot y versus x (trends, learning curves, or sequences)."
    if s.startswith("plt.figure"):
        return "Create a new figure window/canvas for the next plot commands."
    if s.startswith("plt.ylabel") or s.startswith("plt.xlabel") or s.startswith("plt.title"):
        return "Set an axis label or figure title to explain what the plot means."
    if s.startswith("plt.grid"):
        return "Turn on light grid lines to read values from the plot more easily."
    if s.startswith("fig.colorbar"):
        return "Add a colorbar beside a heatmap axis to map colors back to numeric values."
    if s.startswith("zip("):
        return "Walk two (or more) lists side by side: item 0 with item 0, etc."
    if s.startswith("enumerate("):
        return "Loop with a counter: gives (0, first item), (1, second item), ..."
    if s.startswith("sum("):
        return "Aggregate by summing numeric values across an iterable."
    if s.startswith("isinstance("):
        return "Runtime type check used to validate objects before using them."
    if s.startswith("callable("):
        return "Check whether an object is a function/method-like callable."
    if s.startswith("globals()"):
        return "Look up every global name in this notebook run (advanced auto-plot helper)."
    if s.startswith("locals()"):
        return "Look up local names in the current function (advanced / debugging)."
    if s.startswith("len("):
        return "Read a length/count (list size, episodes, steps, etc.)."
    if s.startswith("max("):
        return "Take the maximum of a collection (best target, largest change, etc.)."
    if s.startswith("min(") or s.startswith("abs("):
        return "Math helper used for clamping coordinates or measuring magnitude."
    if s.startswith("divmod("):
        return "Divide and return quotient/remainder (e.g., row/col from flat index)."
    if s.startswith("int("):
        return "Turn a number into a whole number (for indices, counts, discrete ids)."
    if s.startswith("float("):
        return "Turn a value into a decimal number for math."
    if s.startswith("str("):
        return "Convert an object to a string (labels, logging, formatting)."
    if s.startswith("range("):
        return "Build a simple integer sequence for loops or tick positions."
    if s.startswith("sorted("):
        return "Return a sorted list (deterministic ordering for display or logic)."
    if s.startswith("@"):  # decorators
        return "Decorator: wraps/replaces the following function or class definition."
    if s in ("try:", "except Exception:", "finally:"):
        return "Try/except/finally: structured error handling around risky operations."
    if s.startswith("except"):
        return "Exception handler: run when the matching error type occurs."
    if s.startswith("try"):
        return "Try block start: attempt operations that may raise errors."
    if s.startswith("pass"):
        return "No-op placeholder (valid where syntax requires a statement)."
    if s.startswith("raise"):
        return "Explicitly raise an error to signal invalid state or failed checks."
    if s.startswith("open("):
        return "Open a file path for reading/writing bytes or text."
    # Literal dict rows like `"key": {` or `"key": "value",` inside a big dict literal.
    if re.match(r'^\s*"[^"]+"\s*:\s*', s) or re.match(r"^\s*'[^']+'\s*:\s*", s):
        return "One key/value row inside a dict literal (domain -> fields or nested table)."
    if len(s) > 90:
        return f"Execute: {s[:90]} …"
    return f"Execute: {s}"


def _legacy_def_or_class_j_comment(cur: str, nxt: str) -> bool:
    """True if `cur` looks like an older auto-# line we placed above def/async def/class."""
    if not cur.lstrip().startswith("#"):
        return False
    ns = nxt.strip()
    if not (
        ns.startswith("def ")
        or ns.startswith("async def ")
        or ns.startswith("class ")
    ):
        return False
    body = cur.strip()[1:].lstrip()
    if "(what it does):" in body:
        return False
    if body.startswith("Define function") or body.startswith("Define async"):
        return True
    if body.startswith("Define class"):
        return True
    if body.startswith("Function `") or body.startswith("Async function `"):
        return True
    if body.startswith("Class `"):
        return True
    return False


_SUMMARY_HDR_RE = re.compile(
    r"^(?P<ind>\s*)#\s*(?P<kind>Function|Async function|Class)\s+`(?P<name>\w+)`\s*\(what it does\):.*$"
)

# Recognized Matplotlib axis J-line bodies (current + legacy wording from older runs).
_LEGACY_AXIS_NOTE_CANON = "Configure a subplot axis (limits, ticks, labels, or artists)."
_LEGACY_AXIS_NOTE_MORE = "More on the same axes object (limits, ticks, labels, artists)."
_AXIS_COMMENT_VARIANTS: frozenset[str] = frozenset(
    {
        _STUD_AXIS_NOTE_FIRST,
        _STUD_AXIS_NOTE_MORE,
        _LEGACY_AXIS_NOTE_CANON,
        _LEGACY_AXIS_NOTE_MORE,
        "Configure a specific subplot axis (limits, ticks, title, labels, plotting calls).",
    }
)
_ALL_AXIS_COMMENT_BODIES: frozenset[str] = _AXIS_COMMENT_VARIANTS

# When describe() wording changes, strip+annotate can otherwise leave the old # line
# sitting directly above the same code line. Pop these bodies if they differ from
# the freshly computed desired note.
_LEGACY_J_LINE_BODIES: frozenset[str] = frozenset(
    {
        "Loop header: repeat the indented block for each item in the iterable.",
        "Loop header: repeat while the condition stays true.",
        "Branch: only run the next indented lines when this condition is true.",
        "Else-if branch: checked only when previous conditions were false.",
        "Else branch: runs when the matching if/elif chain was not taken.",
        "Assign/update a variable used later in this cell or in other cells.",
        "Import names from a package/module into the notebook kernel namespace.",
        "Append one value to a list (mutates the list in place).",
        "Return a value from this function to its caller.",
        "Skip the rest of this loop body and jump to the next iteration.",
        "Exit the nearest enclosing loop immediately.",
        "Context manager: setup/teardown around the indented block (files, locks, env).",
        "Runtime check: raises AssertionError if the condition is false.",
        "Call a NumPy helper (array creation, options, or array conversion).",
        "Call a Matplotlib pyplot helper (figure/axes/plot/show).",
        "Configure or update the active Matplotlib Figure object.",
        "Print text to the notebook cell output (console).",
        "Build a formatted string (f-string) with embedded values for printing/titles.",
        "Iterate multiple sequences in parallel (pair aligned items together).",
        "Loop with (index, value) pairs while iterating a sequence.",
        "Access the notebook kernel's global symbol table as a dict-like mapping.",
        "Read the current scope's local variable mapping (debug/introspection).",
        "Cast a numeric type to int (discrete ids, indices, counts).",
        "Cast a value to float for numeric pipelines.",
        "Yield the next value from a generator iterator.",
        "Suspend until an awaitable completes (async concurrency).",
        "Call a Seaborn plotting helper (statistical visuals).",
        "Call a pandas API (tables, series, IO, or transforms).",
        _STUD_ASSIGN_NOTE_FIRST,
        _STUD_ASSIGN_NOTE_MORE,
    }
)


def _pop_stale_j_headers_for_line(out_lines: list[str], desired_body: str) -> None:
    """Remove trailing auto-J # lines that describe() no longer emits for the next code line."""
    want = desired_body.rstrip()
    while out_lines:
        j0 = len(out_lines) - 1
        while j0 >= 0 and out_lines[j0].strip() == "":
            j0 -= 1
        if j0 < 0:
            break
        bod = _hash_comment_body(out_lines[j0])
        if bod is None:
            break
        if bod == want:
            break
        if bod not in _LEGACY_J_LINE_BODIES and bod not in _ALL_AXIS_COMMENT_BODIES:
            break
        out_lines.pop()


def _hash_comment_body(line: str) -> str | None:
    s = line.lstrip()
    if not s.startswith("# "):
        return None
    return s[2:].rstrip()


def _is_axes_or_ax_call_line(stripped: str) -> bool:
    return stripped.startswith("ax.") or stripped.startswith("axes[")


def _dedupe_axis_comment_stack(lines: list[str]) -> list[str]:
    """Collapse stacked Matplotlib axis teaching comments into one line before each axes/ax call."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        body0 = _hash_comment_body(lines[i]) if i < len(lines) else None
        if body0 in _ALL_AXIS_COMMENT_BODIES:
            j = i
            while j < len(lines) and _hash_comment_body(lines[j]) in _ALL_AXIS_COMMENT_BODIES:
                j += 1
            if j < len(lines) and _is_axes_or_ax_call_line(lines[j].lstrip()):
                indent = lines[j][: len(lines[j]) - len(lines[j].lstrip())]
                out.append(f"{indent}# {_STUD_AXIS_NOTE_FIRST}")
                out.append(lines[j])
                i = j + 1
                continue
        out.append(lines[i])
        i += 1
    return out


def _recent_axis_code_call(out_lines: list[str], max_code: int = 8) -> bool:
    """True if a prior emitted code line in this cell was an axes/ax API call (same-figure spam guard)."""
    seen = 0
    k = len(out_lines) - 1
    while k >= 0 and seen < max_code:
        ln = out_lines[k]
        if not ln.strip():
            k -= 1
            continue
        st = ln.lstrip()
        if st.startswith("#"):
            k -= 1
            continue
        if _is_axes_or_ax_call_line(st):
            return True
        seen += 1
        k -= 1
    return False


def _looks_like_plain_assignment(stripped: str) -> bool:
    """Heuristic: top-level binding with `=` (not def/if/for, not ==). Used for assign J-line follow-ups."""
    s = stripped.split("#")[0].strip()
    if not s or s.endswith(":"):
        return False
    if s.startswith(
        (
            "def ",
            "async def ",
            "class ",
            "for ",
            "while ",
            "if ",
            "elif ",
            "else:",
            "return ",
            "with ",
            "assert ",
            "import ",
            "from ",
            "@",
            "pass",
            "break",
            "continue",
            "raise ",
            "del ",
            "global ",
            "nonlocal ",
        )
    ):
        return False
    if "==" in s or "=" not in s:
        return False
    if s.startswith("!") or s.startswith("%"):
        return False
    eq = s.find("=")
    if eq <= 0:
        return False
    lhs = s[:eq]
    if "(" in lhs:
        return False
    return True


def _last_code_line_had_assign_family_hint(out_lines: list[str]) -> bool:
    """True if the comment directly above the last emitted code line is an assign-family J-line."""
    k = len(out_lines) - 1
    while k >= 0 and not out_lines[k].strip():
        k -= 1
    if k < 0:
        return False
    if out_lines[k].lstrip().startswith("#"):
        return False
    j = k - 1
    while j >= 0 and not out_lines[j].strip():
        j -= 1
    if j < 0:
        return False
    bod = _hash_comment_body(out_lines[j])
    if bod is None:
        return False
    return bod in (
        _STUD_ASSIGN_NOTE_FIRST,
        _STUD_ASSIGN_NOTE_MORE,
        "Assign/update a variable used later in this cell or in other cells.",
    )


def _def_or_class_sig(stripped: str) -> tuple[str, str] | None:
    """Return (kind label, symbol name) for a def / async def / class header line."""
    if stripped.startswith("async def "):
        m = re.match(r"async def (\w+)\s*\(", stripped)
        return ("Async function", m.group(1)) if m else None
    if stripped.startswith("def "):
        m = re.match(r"def (\w+)\s*\(", stripped)
        return ("Function", m.group(1)) if m else None
    if stripped.startswith("class "):
        m = re.match(r"class (\w+)\b", stripped)
        return ("Class", m.group(1)) if m else None
    return None


def _dedupe_adjacent_summary_headers(lines: list[str]) -> list[str]:
    """
    Collapse two consecutive '# Function|Class `x` (what it does): ...' lines when they
    describe the same symbol (e.g. full text + truncated duplicate from re-runs).
    """
    changed = True
    while changed and len(lines) > 1:
        changed = False
        out: list[str] = []
        i = 0
        while i < len(lines):
            if i + 1 < len(lines):
                cur, nxt = lines[i], lines[i + 1]
                a, b = _SUMMARY_HDR_RE.match(cur), _SUMMARY_HDR_RE.match(nxt)
                if (
                    a
                    and b
                    and a.group("kind") == b.group("kind")
                    and a.group("name") == b.group("name")
                ):
                    ca, cb = cur.rstrip(), nxt.rstrip()
                    if ca.endswith("...") and not cb.endswith("..."):
                        pick = nxt
                    elif cb.endswith("...") and not ca.endswith("..."):
                        pick = cur
                    else:
                        pick = cur if len(ca) >= len(cb) else nxt
                    out.append(pick)
                    i += 2
                    changed = True
                    continue
            out.append(lines[i])
            i += 1
        lines = out
    return lines


def _dedupe_stacked_def_headers(lines: list[str]) -> list[str]:
    """Remove a stale `# Function ... no docstring` line when a richer duplicate follows, then `def`."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        if i + 2 < len(lines):
            cur, nxt, nxt2 = lines[i], lines[i + 1], lines[i + 2]
            c0, c1, c2 = cur.lstrip(), nxt.lstrip(), nxt2.lstrip()
            if (
                c0.startswith("#")
                and c1.startswith("#")
                and (c2.startswith("def ") or c2.startswith("async def "))
                and cur.rstrip() == nxt.rstrip()
            ):
                out.append(nxt)
                out.append(nxt2)
                i += 3
                continue
            if (
                c0.startswith("#")
                and c1.startswith("#")
                and (c2.startswith("def ") or c2.startswith("async def "))
                and "(what it does): no docstring" in cur
                and "(what it does):" in nxt
                and "no docstring" not in nxt
                and "`" in cur
                and "`" in nxt
            ):
                m0 = re.search(r"`(\w+)`", cur)
                m1 = re.search(r"`(\w+)`", nxt)
                if m0 and m1 and m0.group(1) == m1.group(1):
                    out.append(nxt)
                    out.append(nxt2)
                    i += 3
                    continue
        out.append(lines[i])
        i += 1
    return out


def strip_prior_j_comments(src: str) -> str:
    """Remove a prior J-mode comment line when it matches describe(next line) or legacy patterns."""
    summaries: dict[int, str] = {}
    try:
        ast.parse(src)
        summaries = symbol_summaries(src)
    except SyntaxError:
        summaries = {}
    lines = _dedupe_stacked_def_headers(src.splitlines())
    lines = _dedupe_adjacent_summary_headers(lines)
    lines = _dedupe_axis_comment_stack(lines)
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
                nxt_lineno = i + 2  # 1-based line number of nxt in this source string
                note_full = describe(nxt.strip(), nxt_lineno, summaries)
                note_generic = describe(nxt.strip(), None, None)
                expected_full = f"{indent}# {note_full}"
                expected_generic = f"{indent}# {note_generic}"
                axis_ok: tuple[str, ...] = ()
                if _is_axes_or_ax_call_line(nxt.strip()):
                    axis_ok = tuple(
                        f"{indent}# {t}".rstrip()
                        for t in (
                            _STUD_AXIS_NOTE_MORE,
                            _LEGACY_AXIS_NOTE_MORE,
                            _LEGACY_AXIS_NOTE_CANON,
                            "Configure a specific subplot axis (limits, ticks, title, labels, plotting calls).",
                        )
                    )
                assign_ok: tuple[str, ...] = ()
                if _looks_like_plain_assignment(nxt.strip()) and describe(
                    nxt.strip(), nxt_lineno, summaries
                ) == _STUD_ASSIGN_NOTE_FIRST:
                    assign_ok = tuple(
                        f"{indent}# {t}".rstrip()
                        for t in (
                            _STUD_ASSIGN_NOTE_FIRST,
                            _STUD_ASSIGN_NOTE_MORE,
                            "Assign/update a variable used later in this cell or in other cells.",
                        )
                    )
                if cur.rstrip() in (
                    expected_full.rstrip(),
                    expected_generic.rstrip(),
                    *axis_ok,
                    *assign_ok,
                ):
                    i += 1
                    continue
                if _legacy_def_or_class_j_comment(cur, nxt):
                    i += 1
                    continue
                # Drop stale "(what it does): no docstring…" header when a richer duplicate follows.
                if i + 2 < len(lines):
                    nxt2 = lines[i + 2]
                    c0, c1, c2 = cur.lstrip(), nxt.lstrip(), nxt2.lstrip()
                    if (
                        c0.startswith("#")
                        and c1.startswith("#")
                        and (c2.startswith("def ") or c2.startswith("async def "))
                        and "(what it does): no docstring" in cur
                        and "(what it does):" in nxt
                        and "no docstring" not in nxt
                        and "`" in cur
                        and "`" in nxt
                    ):
                        m0 = re.search(r"`(\w+)`", cur)
                        m1 = re.search(r"`(\w+)`", nxt)
                        if m0 and m1 and m0.group(1) == m1.group(1):
                            i += 1
                            continue
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
                rest = cur.strip()[1:].lstrip()
                if rest.startswith("Execute:") and rest[len("Execute:") :].strip() == nxt.strip():
                    i += 1
                    continue
                # Mistaken header above a triple-quoted docstring line from older annotator runs.
                if rest.startswith("Execute:") and (
                    nxt.lstrip().startswith(('"""', "'''"))
                    or nxt.lstrip().startswith(("r'''", 'r"""', "f'''", 'f"""'))
                ):
                    i += 1
                    continue
        out.append(cur)
        i += 1
    tail = "\n" if src.endswith("\n") or not src else ""
    return "\n".join(out) + tail


def annotate_source(src: str, summaries: dict[int, str] | None = None) -> str:
    lines = src.splitlines()
    skip_inside_string = multiline_string_continuation_lines(src)
    out_lines: list[str] = []
    for lineno, raw in enumerate(lines, start=1):
        if raw.strip() == "":
            out_lines.append(raw)
            continue
        if raw.lstrip().startswith("#"):
            out_lines.append(raw)
            continue
        tq = raw.lstrip()
        if tq.startswith(('"""', "'''")) or tq.startswith(
            ("r'''", 'r"""', "f'''", 'f"""', "u'''", 'u"""')
        ):
            # Docstring / triple-quoted literal line; never insert a # line above it.
            out_lines.append(raw)
            continue
        if lineno in skip_inside_string:
            out_lines.append(raw)
            continue
        indent = raw[: len(raw) - len(raw.lstrip())]
        note = describe(raw.strip(), lineno, summaries)
        st = raw.lstrip()
        if _is_axes_or_ax_call_line(st) and _recent_axis_code_call(out_lines):
            note = _STUD_AXIS_NOTE_MORE
        elif note == _STUD_ASSIGN_NOTE_FIRST and _last_code_line_had_assign_family_hint(out_lines):
            note = _STUD_ASSIGN_NOTE_MORE
        desired = f"{indent}# {note}"
        _pop_stale_j_headers_for_line(out_lines, note)
        j = len(out_lines) - 1
        while j >= 0 and out_lines[j].strip() == "":
            j -= 1
        skip_desired = j >= 0 and out_lines[j].rstrip() == desired.rstrip()
        if not skip_desired and j >= 0:
            sig = _def_or_class_sig(raw.strip())
            if sig:
                mprev = _SUMMARY_HDR_RE.match(out_lines[j])
                if mprev and mprev.group("kind") == sig[0] and mprev.group("name") == sig[1]:
                    skip_desired = True
        if not skip_desired:
            out_lines.append(desired)
        out_lines.append(raw)
    return "\n".join(out_lines) + "\n"


def transform_cell_source(src: str) -> tuple[str, str | None]:
    """Return (new_source, error_message). On error, caller should keep original source."""
    stripped = strip_prior_j_comments(src)
    has_magic = _cell_has_ipython_magic(stripped)
    pre_ok = True
    try:
        ast.parse(stripped)
    except SyntaxError:
        pre_ok = False

    summaries = symbol_summaries(stripped) if pre_ok else {}
    new_src = annotate_source(stripped, summaries)

    if not has_magic:
        try:
            ast.parse(new_src)
        except SyntaxError as e:
            return src, f"post-annotate SyntaxError: {e}"

    if new_src.rstrip("\n") == src.rstrip("\n"):
        return src, None
    return new_src, None


def process_notebook(nb_path: Path, only_cell_indices: set[int] | None = None) -> tuple[int, list[str]]:
    """Rewrite code cells in-place on disk. Returns (cells_changed, error_messages)."""
    text = nb_path.read_text(encoding="utf-8")
    nb = json.loads(text)
    errors: list[str] = []
    changed = 0
    for idx, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") != "code":
            continue
        if only_cell_indices is not None and idx not in only_cell_indices:
            continue
        src = "".join(cell["source"])
        if not src.strip():
            continue
        new_src, err = transform_cell_source(src)
        if err:
            errors.append(f"{nb_path}:{idx}: {err}")
            continue
        if new_src != src:
            cell["source"] = [ln + "\n" for ln in new_src.splitlines()]
            changed += 1
    if changed:
        nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed, errors
