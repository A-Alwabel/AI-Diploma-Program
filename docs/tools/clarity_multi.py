#!/usr/bin/env python3
"""Multi-course clarity: objectives re-run, duplicate Story removal, optional terse I/O expansion.
Excludes DOCS, PROJECTS, .ipynb_checkpoints. Run from repo root."""

from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
COURSES = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]


def skip_rel(rel: str) -> bool:
    return "DOCS" in rel or "PROJECTS" in rel or ".ipynb_checkpoints" in rel


def remove_duplicate_story_cell(nb_path: Path) -> bool:
    """Remove standalone '## The Story | القصة' cell when intro already has 'The Story: X' + before/after."""
    try:
        with open(nb_path, encoding="utf-8") as f:
            nb = json.load(f)
    except json.JSONDecodeError:
        return False
    intro_has_story = False
    for c in nb["cells"]:
        if c.get("cell_type") != "markdown":
            continue
        src = "".join(c.get("source", []))
        if "The Story:" in src and "before" in src.lower() and "after" in src.lower():
            intro_has_story = True
            break
    if not intro_has_story:
        return False
    removed = False
    new_cells = []
    for c in nb["cells"]:
        if c.get("cell_type") != "markdown":
            new_cells.append(c)
            continue
        src = "".join(c.get("source", []))
        if "## The Story | القصة" in src and "The Story:" not in src and "**BEFORE**" in src and "**AFTER**" in src:
            removed = True
            continue
        new_cells.append(c)
    if removed:
        nb["cells"] = new_cells
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    return removed


# (new_inputs_str, new_outputs_str). Match terse pattern before replace.
TERSE_IO_UPDATES = {
    "05/unit4-ml-intro/examples/10_clustering_unsupervised.ipynb": (
        "- Unlabeled data\n- sklearn (K-Means, DBSCAN, etc.)",
        "- Cluster labels and centroids\n- Evaluation metrics (silhouette, etc.)\n- Plots showing clusters",
    ),
}


def expand_terse_io(nb_path: Path, course: str, rel: str) -> bool:
    key = f"{course}/{rel}"
    if key not in TERSE_IO_UPDATES:
        return False
    new_in, new_out = TERSE_IO_UPDATES[key]
    try:
        with open(nb_path, encoding="utf-8") as f:
            nb = json.load(f)
    except json.JSONDecodeError:
        return False
    changed = False
    for c in nb["cells"]:
        if c.get("cell_type") != "markdown":
            continue
        src = "".join(c.get("source", []))
        if "📥 Inputs & 📤 Outputs" not in src or "Unlabeled data" not in src:
            continue
        if "- Unlabeled data\n- sklearn" not in src or "- Clusters\n- Visualizations" not in src:
            continue
        src = src.replace("- Unlabeled data\n- sklearn", new_in)
        src = src.replace("- Clusters\n- Visualizations", new_out)
        c["source"] = [src]
        changed = True
        break
    if changed:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    return changed


def run_story_only() -> list:
    report = []
    for c in COURSES:
        folder = ROOT / f"Course {c}"
        if not folder.is_dir():
            continue
        done = []
        for nb_path in sorted(folder.rglob("*.ipynb")):
            rel = nb_path.relative_to(folder).as_posix()
            if skip_rel(rel):
                continue
            if remove_duplicate_story_cell(nb_path):
                done.append(rel)
        if done:
            report.append((c, "story", done))
    return report


def run_terse_io_only() -> list:
    report = []
    for c in COURSES:
        folder = ROOT / f"Course {c}"
        if not folder.is_dir():
            continue
        done = []
        for nb_path in sorted(folder.rglob("*.ipynb")):
            rel = nb_path.relative_to(folder).as_posix()
            if skip_rel(rel):
                continue
            if expand_terse_io(nb_path, c, rel):
                done.append(rel)
        if done:
            report.append((c, "io", done))
    return report


def run_objectives() -> bool:
    """Run objectives scripts (objectives_multi 01,02,08-12; c03; c04; c06; c07; clarity_updates_c05)."""
    scripts = [
        (TOOLS / "objectives_multi.py", ["01", "02", "08", "09", "10", "11", "12"]),
        (TOOLS / "c03_specific_objectives.py", []),
        (TOOLS / "c04_specific_objectives.py", []),
        (TOOLS / "c06_specific_objectives.py", []),
        (TOOLS / "c07_specific_objectives.py", []),
        (TOOLS / "clarity_updates_c05.py", []),
    ]
    ok = True
    for path, args in scripts:
        cmd = [sys.executable, str(path)] + args
        try:
            subprocess.run(cmd, cwd=str(ROOT), check=True, capture_output=True, text=True, timeout=120)
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as e:
            print(f"  objectives: {path.name} failed: {e}")
            ok = False
    return ok


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode not in ("all", "objectives", "story", "io"):
        print("Usage: python clarity_multi.py [all|objectives|story|io]")
        sys.exit(1)
    if mode in ("all", "objectives"):
        print("Running objectives scripts...")
        run_objectives()
    report = []
    if mode in ("all", "story"):
        report.extend(run_story_only())
    if mode in ("all", "io"):
        report.extend(run_terse_io_only())
    print("Clarity multi report:")
    for course, kind, paths in report:
        print(f"  [Course {course}] {kind}: {len(paths)}")
        for p in paths:
            print(f"    {p}")
    if not report and mode != "objectives":
        print("  (no changes)")


if __name__ == "__main__":
    main()
