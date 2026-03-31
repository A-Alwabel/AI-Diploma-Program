#!/usr/bin/env python3
"""Add 'Inputs & Outputs' section to notebooks in specified courses. Usage: python add_inputs_outputs_multi.py [01] [02] ..."""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

GENERIC = (
    ["Libraries and concepts as introduced in this notebook; see prerequisites and code comments."],
    ["Printed results, figures, and summaries as shown when you run the cells."],
)

DEFAULT_COURSES = ["01", "02", "08", "09", "10", "11", "12"]


def has_io_section(cells):
    for c in cells:
        if c.get("cell_type") != "markdown":
            continue
        src = "".join(c.get("source", []))
        if "Inputs & Outputs" in src or ("Inputs & " in src and "Outputs" in src):
            return True
    return False


def first_code_index(cells):
    for i, c in enumerate(cells):
        if c.get("cell_type") == "code":
            return i
    return None


def make_io_cell(inputs: list, outputs: list):
    in_b = "\n".join(f"- {x}" for x in inputs)
    out_b = "\n".join(f"- {x}" for x in outputs)
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 📥 Inputs & 📤 Outputs | المدخلات والمخرجات\n",
            "\n",
            "**Inputs:** What we use in this notebook\n",
            "\n",
            in_b + "\n",
            "\n",
            "**Outputs:** What you'll see when you run the cells\n",
            "\n",
            out_b + "\n",
            "\n",
            "---\n",
        ],
    }


def process(path: Path, rel: str):
    try:
        with open(path, encoding="utf-8") as f:
            nb = json.load(f)
    except json.JSONDecodeError as e:
        return ("fail", str(e))
    cells = nb["cells"]
    if has_io_section(cells):
        return "skip"
    idx = first_code_index(cells)
    if idx is None:
        return "no_code"
    inputs, outputs = GENERIC
    io_cell = make_io_cell(inputs, outputs)
    cells.insert(idx, io_cell)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    return "ok"


def run(course: str):
    folder = ROOT / f"Course {course}"
    if not folder.is_dir():
        return None
    added, skipped, no_code, failed = [], [], [], []
    for nb_path in sorted(folder.rglob("*.ipynb")):
        rel = nb_path.relative_to(folder).as_posix()
        if "DOCS" in rel or "PROJECTS" in rel or ".ipynb_checkpoints" in rel:
            continue
        res = process(nb_path, rel)
        if res == "ok":
            added.append(rel)
        elif res == "skip":
            skipped.append(rel)
        elif isinstance(res, tuple) and res[0] == "fail":
            failed.append((rel, res[1]))
        elif res == "no_code":
            no_code.append(rel)
    return added, skipped, no_code, failed


def main():
    courses = sys.argv[1:] if len(sys.argv) > 1 else DEFAULT_COURSES
    for c in courses:
        num = c.zfill(2) if len(c) <= 2 else c
        folder = ROOT / f"Course {num}"
        if not folder.is_dir():
            print(f"Skip Course {num} (not found)")
            continue
        out = run(num)
        if out is None:
            continue
        added, skipped, no_code, failed = out
        if failed:
            print(f"[Course {num}] Failed (invalid JSON):")
            for r, e in failed:
                print(" ", r, ":", e[:60])
        print(f"[Course {num}] Added: {len(added)} | Skipped: {len(skipped)} | No code: {len(no_code)} | Failed: {len(failed)}")
        for r in added:
            print(" ", r)
        print()


if __name__ == "__main__":
    main()
