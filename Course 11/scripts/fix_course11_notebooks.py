#!/usr/bin/env python3
"""Repair common Course 11 student-path notebook issues.

- Restores truncated MLflow-style experiment-tracking code cells
- Converts mistaken markdown cells that contain runnable Python
- Removes internal DETAILED_UNIT_DESCRIPTIONS references from student cells

Run from repo root:

    python3 "Course 11/scripts/fix_course11_notebooks.py"
"""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path

COURSE11 = Path(__file__).resolve().parents[1]

MLFLOW_TRACKING_CELL = '''import json, time, pathlib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

RUNS_LOG = pathlib.Path("/tmp/experiment_runs.jsonl")
runs: list[dict] = []


def log_run(name, params, metrics, tags=None):
    entry = {
        "run_id": f"run_{len(runs):03d}",
        "name": name,
        "params": params,
        "metrics": metrics,
        "tags": tags or {},
        "timestamp": time.time(),
    }
    runs.append(entry)
    with open(RUNS_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\\n")
    return entry


iris = load_iris()
X, y = iris.data, iris.target

models = {
    "LogisticRegression": (LogisticRegression(max_iter=200), {"C": 1.0}),
    "RandomForest_50": (RandomForestClassifier(n_estimators=50), {"n_estimators": 50}),
    "RandomForest_100": (RandomForestClassifier(n_estimators=100), {"n_estimators": 100}),
    "GradientBoosting": (
        GradientBoostingClassifier(n_estimators=50),
        {"n_estimators": 50, "lr": 0.1},
    ),
}

results = []
print("Running experiments...")
for name, (clf, params) in models.items():
    start = time.perf_counter()
    cv_scores = cross_val_score(clf, X, y, cv=5, scoring="accuracy")
    elapsed = time.perf_counter() - start
    metrics = {
        "cv_mean_accuracy": round(float(cv_scores.mean()), 4),
        "cv_std": round(float(cv_scores.std()), 4),
        "training_time_s": round(elapsed, 3),
    }
    log_run(name, params, metrics, tags={"dataset": "iris", "framework": "sklearn"})
    results.append((name, metrics))
    print(
        f"  [{name:25s}]  acc={metrics['cv_mean_accuracy']:.4f} "
        f"+/- {metrics['cv_std']:.4f}  | {elapsed:.2f}s"
    )

names = [r[0].replace("_", " ") for r in results]
means = [r[1]["cv_mean_accuracy"] for r in results]
stds = [r[1]["cv_std"] for r in results]
times = [r[1]["training_time_s"] for r in results]
best = int(np.argmax(means))

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
bars = axes[0].bar(names, means, yerr=stds, capsize=5, alpha=0.8)
bars[best].set_color("green")
bars[best].set_label("Best model")
axes[0].set_title("Model Comparison (MLflow-style)")
axes[0].set_ylabel("CV Accuracy")
axes[0].legend()
axes[1].bar(names, times, alpha=0.8)
axes[1].set_title("Training Time")
axes[1].set_ylabel("Seconds")
plt.suptitle("Experiment tracking pattern used in production MLOps")
plt.tight_layout()
plt.savefig("/tmp/mlflow_comparison.png", dpi=72)

print(f"Best model: {results[best][0]} (accuracy={means[best]:.4f})")
print(f"Experiment log: {RUNS_LOG}")
'''


def is_student_notebook(path: Path) -> bool:
    if "DOCS" in path.parts or "solutions" in path.parts:
        return False
    return path.suffix == ".ipynb" and any(part.startswith("unit") for part in path.parts)


def strip_magics_for_ast(src: str) -> str:
    lines = []
    for line in src.splitlines():
        s = line.strip()
        if s.startswith("%") or s.startswith("!"):
            continue
        lines.append(line)
    return "\n".join(lines)


def looks_like_code_in_markdown(src: str) -> bool:
    if len(src) < 200:
        return False
    if "import " not in src and "def " not in src:
        return False
    try:
        ast.parse(strip_magics_for_ast(src))
        return True
    except SyntaxError:
        return False


def is_truncated_mlflow_cell(src: str) -> bool:
    return "RUNS_LOG.write_t" in src or (
        "Simulate MLflow-style experiment tracking" in src
        and "print(\"Running experiments..." in src
        and "for name, (clf, params)" not in src
    )


def clean_markdown_refs(src: str) -> str:
    src = src.replace(
        "This notebook supports **Course 11, Unit 1** requirements from `DETAILED_UNIT_DESCRIPTIONS.md`.\n\n---\n\n",
        "",
    )
    src = re.sub(
        r"## Official Structure Reference\n\n.*?---\n\n",
        "",
        src,
        flags=re.DOTALL,
    )
    src = src.replace("`DETAILED_UNIT_DESCRIPTIONS.md`", "the course unit README")
    return src


def fix_notebook(path: Path) -> list[str]:
    changes: list[str] = []
    nb = json.loads(path.read_text(encoding="utf-8"))
    new_cells = []

    for cell in nb.get("cells", []):
        ctype = cell.get("cell_type")
        src = "".join(cell.get("source", []))

        if ctype == "markdown":
            cleaned = clean_markdown_refs(src)
            if cleaned != src:
                changes.append("removed internal doc reference")
                src = cleaned

            if looks_like_code_in_markdown(src):
                new_cells.append(
                    {
                        "cell_type": "code",
                        "metadata": cell.get("metadata", {}),
                        "source": [src if src.endswith("\n") else src + "\n"],
                        "outputs": [],
                        "execution_count": None,
                    }
                )
                changes.append("converted markdown code block to code cell")
                continue

        if ctype == "code" and is_truncated_mlflow_cell(src):
            cell = dict(cell)
            cell["source"] = [MLFLOW_TRACKING_CELL]
            changes.append("restored truncated MLflow tracking cell")

        new_cells.append(cell)

    if changes:
        nb["cells"] = new_cells
        path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    return changes


def main() -> int:
    touched = 0
    for nb in sorted(COURSE11.rglob("*.ipynb")):
        if not is_student_notebook(nb):
            continue
        changes = fix_notebook(nb)
        if changes:
            touched += 1
            print(f"{nb.relative_to(COURSE11)}: {', '.join(set(changes))}")
    print(f"\nUpdated {touched} notebooks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
