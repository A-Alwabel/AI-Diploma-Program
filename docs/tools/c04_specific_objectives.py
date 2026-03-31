#!/usr/bin/env python3
"""Replace generic learning objectives with specific ones in Course 04 notebooks."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
C04 = ROOT / "Course 04"

GENERIC = [
    "Understand the key concepts of this topic",
    "Apply the topic using Python code examples",
    "Practice with small, realistic datasets or scenarios",
]

SPECIFIC_OBJECTIVES = {
    "unit1-data-processing/examples/01_data_loading_exploration.ipynb": [
        "Load and explore datasets (shape, info, describe)",
        "Identify missing values, types, and basic stats",
        "Use pandas and visualizations for initial EDA",
    ],
    "unit1-data-processing/examples/02_data_cleaning.ipynb": [
        "Handle missing values and duplicates",
        "Clean and normalize data for modeling",
        "Document cleaning choices and outcomes",
    ],
    "unit1-data-processing/examples/03_data_preprocessing.ipynb": [
        "Scale and encode features for ML",
        "Split data (train/validation/test) appropriately",
        "Prepare datasets for regression and classification",
    ],
    "unit1-data-processing/examples/04_linear_regression.ipynb": [
        "Fit and interpret simple and multiple linear regression",
        "Use metrics (MSE, RMSE, R²) and residual plots",
        "Compare models and check assumptions",
    ],
    "unit1-data-processing/examples/05_polynomial_regression.ipynb": [
        "Fit polynomial regression and choose degree",
        "Understand overfitting vs underfitting",
        "Use learning curves and validation",
    ],
    "unit2-regression/examples/01_ridge_lasso_regression.ipynb": [
        "Apply Ridge and Lasso regularization",
        "Interpret regularization strength and coefficients",
        "Compare with ordinary least squares",
    ],
    "unit2-regression/examples/02_cross_validation.ipynb": [
        "Use k-fold and stratified cross-validation",
        "Estimate model performance robustly",
        "Avoid overfitting to a single train/test split",
    ],
    "unit3-classification/examples/02_decision_trees.ipynb": [
        "Build and interpret decision tree classifiers",
        "Use pruning and depth control",
        "Visualize trees and feature importance",
    ],
    "unit3-classification/examples/03_svm.ipynb": [
        "Train SVM classifiers with linear and nonlinear kernels",
        "Tune C and kernel parameters",
        "Interpret decision boundaries and support vectors",
    ],
    "unit3-classification/examples/04_knn.ipynb": [
        "Implement k-NN classification and choose k",
        "Use distance metrics and scaling",
        "Compare with other classifiers",
    ],
    "unit4-clustering/examples/01_kmeans_clustering.ipynb": [
        "Apply K-Means and choose the number of clusters",
        "Use elbow method and silhouette score",
        "Interpret and visualize clusters",
    ],
    "unit4-clustering/examples/02_hierarchical_clustering.ipynb": [
        "Perform agglomerative hierarchical clustering",
        "Interpret dendrograms and linkage",
        "Compare with K-Means",
    ],
    "unit4-clustering/examples/03_pca.ipynb": [
        "Apply PCA for dimensionality reduction",
        "Interpret explained variance and components",
        "Use PCA for visualization and preprocessing",
    ],
    "unit5-model-selection/examples/01_grid_search.ipynb": [
        "Use GridSearchCV for hyperparameter tuning",
        "Combine with cross-validation and scoring",
        "Select and evaluate best models",
    ],
    "unit5-model-selection/examples/02_boosting.ipynb": [
        "Apply boosting (e.g. AdaBoost, gradient boosting)",
        "Compare with bagging and single models",
        "Tune and interpret ensemble performance",
    ],
}


def fix_objectives(nb_path: Path, rel: str) -> bool:
    spec = SPECIFIC_OBJECTIVES.get(rel)
    if not spec:
        return False
    try:
        with open(nb_path, encoding="utf-8") as f:
            nb = json.load(f)
    except json.JSONDecodeError:
        return False
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
                if new_lines and "By completing this notebook" not in new_lines[-1]:
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


def main():
    done = []
    for nb_path in sorted(C04.rglob("*.ipynb")):
        rel = nb_path.relative_to(C04).as_posix()
        if "DOCS" in rel or "PROJECTS" in rel or "datasets" in rel:
            continue
        if fix_objectives(nb_path, rel):
            done.append(rel)
    print("Updated objectives:", len(done))
    for r in done:
        print(" ", r)


if __name__ == "__main__":
    main()
