#!/usr/bin/env python3
"""Clarity updates for Course 05: generic objectives → specific, duplicate Story removal, terse I/O expansion."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
C05 = ROOT / "Course 05"

GENERIC = [
    "Understand the key concepts of this topic",
    "Apply the topic using Python code examples",
    "Practice with small, realistic datasets or scenarios",
]

# Replace generic objectives with these specific ones (by notebook path).
SPECIFIC_OBJECTIVES = {
    "unit1-introduction/examples/01_data_science_intro.ipynb": [
        "Understand the complete data science lifecycle (9 steps)",
        "Know what pandas DataFrames are and how they work",
        "Create basic data visualizations",
        "Understand the workflow from data to insights",
        "See how all course units fit into the lifecycle",
    ],
    "unit1-introduction/examples/02_pandas_numpy_basics.ipynb": [
        "Create and manipulate NumPy arrays and pandas DataFrames",
        "Use groupby, describe, and basic indexing",
        "Produce simple plots and link to Example 3",
    ],
    "unit1-introduction/examples/03_cudf_introduction.ipynb": [
        "Compare Colab vs local and cuDF vs pandas",
        "Run CPU vs GPU timing comparisons",
        "Understand when to use GPU-accelerated dataframes",
    ],
    "unit2-cleaning/examples/01_data_loading.ipynb": [
        "Load data from CSV files with advanced options",
        "Load from Excel files and multiple sheets",
        "Load from JSON (including nested structures)",
        "Handle large files using chunking",
        "Implement error handling for robust data loading",
    ],
    "unit2-cleaning/examples/02_missing_values_duplicates.ipynb": [
        "Identify and handle missing values",
        "Find and remove duplicates",
        "Apply imputation and document choices",
    ],
    "unit2-cleaning/examples/03_outliers_transformation.ipynb": [
        "Detect outliers and apply transformations",
        "Use scaling and encoding where relevant",
        "Interpret cleaned data and summaries",
    ],
    "unit3-visualization/examples/02_matplotlib_basics.ipynb": [
        "Create basic Matplotlib figures and axes",
        "Customize plots and add labels",
        "Save figures and reuse styles",
    ],
    "unit3-visualization/examples/03_seaborn_plots.ipynb": [
        "Build statistical plots with Seaborn",
        "Use built-in themes and palettes",
        "Combine Seaborn with pandas DataFrames",
    ],
    "unit3-visualization/examples/04_plotly_interactive.ipynb": [
        "Create interactive Plotly charts",
        "Use hover, zoom, and other interactivity",
        "Export or embed interactive visualizations",
    ],
    "unit4-ml-intro/examples/04_linear_regression.ipynb": [
        "Fit and interpret linear regression models",
        "Use train/test split and basic metrics",
        "Plot fits and residuals",
    ],
    "unit4-ml-intro/examples/06_classification.ipynb": [
        "Train and evaluate classifiers (e.g. sklearn)",
        "Interpret confusion matrix and metrics",
        "Compare models and feature importance",
    ],
    "unit4-ml-intro/examples/07_model_evaluation.ipynb": [
        "Compute accuracy, precision, recall, F1",
        "Use cross-validation and learning curves",
        "Interpret evaluation plots and metrics",
    ],
    "unit5-scaling/examples/02_dask_distributed.ipynb": [
        "Use Dask for distributed DataFrames and arrays",
        "Run computations that exceed memory",
        "Interpret timings and scalability",
    ],
    "unit5-scaling/examples/04_rapids_workflows.ipynb": [
        "Run RAPIDS (e.g. cuDF) workflows on GPU",
        "Compare GPU vs CPU for key operations",
        "Identify when RAPIDS is beneficial",
    ],
    "unit5-scaling/examples/05_production_pipelines.ipynb": [
        "Design and run production-style pipelines",
        "Use Dask or similar for orchestration",
        "Handle logging and error handling",
    ],
    "unit5-scaling/examples/06_performance_optimization.ipynb": [
        "Profile code and identify bottlenecks",
        "Apply optimization techniques",
        "Measure before/after performance",
    ],
    "unit5-scaling/examples/07_large_datasets.ipynb": [
        "Load and process large datasets (chunking, etc.)",
        "Use distributed or out-of-core tools where relevant",
        "Summarize and visualize at scale",
    ],
    "unit5-scaling/examples/08_deployment.ipynb": [
        "Wrap a model in a simple API (e.g. Flask/FastAPI)",
        "Validate inputs and return predictions",
        "Run and test the API locally",
    ],
}


def fix_generic_objectives(nb_path: Path, rel: str) -> bool:
    spec = SPECIFIC_OBJECTIVES.get(rel)
    if not spec:
        return False
    with open(nb_path, encoding="utf-8") as f:
        nb = json.load(f)
    changed = False
    for c in nb["cells"]:
        if c.get("cell_type") != "markdown":
            continue
        lines = c.get("source", [])
        if not isinstance(lines, list):
            continue
        src = "".join(lines)
        if "Understand the key concepts of this topic" not in src:
            continue
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if "- Understand the key concepts of this topic" in line:
                # Keep "By completing..." if it was the previous line
                if new_lines and "By completing this notebook" in new_lines[-1]:
                    pass
                else:
                    new_lines.append("By completing this notebook, you will:\n")
                for s in spec:
                    new_lines.append(f"- {s}\n")
                i += 1
                while i < len(lines) and (
                    "- Apply the topic using Python code examples" in lines[i]
                    or "- Practice with small, realistic datasets or scenarios" in lines[i]
                ):
                    i += 1
                continue
            new_lines.append(line)
            i += 1
        if new_lines != lines:
            c["source"] = new_lines
            changed = True
        break
    if changed:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    return changed


def remove_duplicate_story_cell(nb_path: Path) -> bool:
    """Remove standalone '## The Story | القصة' cell when intro already has 'The Story: X'."""
    with open(nb_path, encoding="utf-8") as f:
        nb = json.load(f)
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
        # Standalone Story cell: only this heading + BEFORE/AFTER, no "The Story: X"
        if "## The Story | القصة" in src and "The Story:" not in src and "**BEFORE**" in src and "**AFTER**" in src:
            removed = True
            continue
        new_cells.append(c)
    if removed:
        nb["cells"] = new_cells
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    return removed


def expand_terse_io(nb_path: Path, rel: str) -> bool:
    """Expand very terse Inputs/Outputs sections."""
    updates = {
        "unit4-ml-intro/examples/10_clustering_unsupervised.ipynb": (
            "- Unlabeled data\n- sklearn (K-Means, DBSCAN, etc.)",
            "- Cluster labels and centroids\n- Evaluation metrics (silhouette, etc.)\n- Plots showing clusters",
        ),
    }
    if rel not in updates:
        return False
    new_in, new_out = updates[rel]
    with open(nb_path, encoding="utf-8") as f:
        nb = json.load(f)
    changed = False
    for c in nb["cells"]:
        if c.get("cell_type") != "markdown":
            continue
        src = "".join(c.get("source", []))
        if "📥 Inputs & 📤 Outputs" not in src or "Unlabeled data" not in src:
            continue
        # Replace terse bullets; tolerate slight formatting differences
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


def main():
    objectives_done = []
    story_removed = []
    io_expanded = []
    for nb_path in sorted(C05.rglob("*.ipynb")):
        rel = nb_path.relative_to(C05).as_posix()
        if "DOCS" in rel or "PROJECTS" in rel:
            continue
        if fix_generic_objectives(nb_path, rel):
            objectives_done.append(rel)
        if remove_duplicate_story_cell(nb_path):
            story_removed.append(rel)
        if expand_terse_io(nb_path, rel):
            io_expanded.append(rel)
    print("Generic objectives → specific:", len(objectives_done))
    for r in objectives_done:
        print(" ", r)
    print("\nDuplicate Story cell removed:", len(story_removed))
    for r in story_removed:
        print(" ", r)
    print("\nTerse I/O expanded:", len(io_expanded))
    for r in io_expanded:
        print(" ", r)


if __name__ == "__main__":
    main()
