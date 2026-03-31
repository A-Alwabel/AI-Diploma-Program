#!/usr/bin/env python3
"""Add 'Inputs & Outputs' section to all Course 03 notebooks that don't have it."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
C03 = ROOT / "Course 03"

GENERIC = (
    ["Libraries and concepts as introduced in this notebook; see prerequisites and code comments."],
    ["Printed results, figures, and summaries as shown when you run the cells."],
)


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


def main():
    added, skipped, no_code, failed = [], [], [], []
    for nb_path in sorted(C03.rglob("*.ipynb")):
        rel = nb_path.relative_to(C03).as_posix()
        if "DOCS" in rel or "PROJECTS" in rel:
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
    if failed:
        print("Failed (invalid JSON):")
        for r, e in failed:
            print(" ", r, ":", e[:60])
        print()
    print("Added Inputs & Outputs:", len(added))
    for r in added:
        print(" ", r)
    print("\nSkipped:", len(skipped), "| No code:", len(no_code), "| Failed:", len(failed))


if __name__ == "__main__":
    main()
