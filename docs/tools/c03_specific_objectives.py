#!/usr/bin/env python3
"""Replace generic learning objectives with specific ones in Course 03 (maths/ML foundations) notebooks."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
C03 = ROOT / "Course 03"

# Objectives keyed by base name (e.g. 01_vectors_matrices_basics) for both unit* and modules/module_*.
OBJECTIVES_BY_BASENAME = {
    "01_vectors_matrices_basics": [
        "Perform vector and matrix operations with NumPy",
        "Understand shapes, broadcasting, and basic linear algebra",
        "Apply operations to simple ML-relevant examples",
    ],
    "02_matrix_operations": [
        "Compute matrix multiplication, transpose, and norms",
        "Use linear algebra ops for transformations",
        "Connect matrix operations to ML (e.g. linear models)",
    ],
    "03_eigenvalues_eigenvectors": [
        "Compute eigenvalues and eigenvectors",
        "Interpret spectral properties of matrices",
        "Apply eigendecomposition to dimensionality reduction",
    ],
    "01_derivatives_basics": [
        "Compute derivatives symbolically and numerically",
        "Understand gradients for scalar and multivariate functions",
        "Link derivatives to optimization",
    ],
    "02_gradients_multivariable": [
        "Compute gradients for multivariate functions",
        "Implement gradient computations in code",
        "Use gradients for direction of steepest ascent/descent",
    ],
    "03_gradient_descent": [
        "Implement gradient descent for optimization",
        "Tune learning rate and monitor convergence",
        "Apply GD to simple regression or cost minimization",
    ],
    "01_optimizers_comparison": [
        "Compare optimizers (SGD, Adam, etc.)",
        "Implement or use optimizer updates",
        "Interpret convergence and loss curves",
    ],
    "02_loss_functions": [
        "Define and implement common loss functions",
        "Choose losses for regression vs classification",
        "Connect losses to model training",
    ],
    "03_statistical_measures": [
        "Compute basic statistical properties of datasets",
        "Use mean, variance, covariance, correlation",
        "Apply measures in ML preprocessing and analysis",
    ],
    "01_pca_implementation": [
        "Implement PCA for dimensionality reduction",
        "Interpret explained variance and components",
        "Use PCA for visualization and preprocessing",
    ],
    "02_curse_dimensionality": [
        "Understand the curse of dimensionality",
        "Relate dimensionality to sample size and generalization",
        "Motivate dimensionality reduction and regularization",
    ],
    "03_feature_selection": [
        "Apply feature selection techniques",
        "Compare filter, wrapper, and embedded methods",
        "Use feature importance and correlation",
    ],
    "01_probability_distributions": [
        "Work with common probability distributions",
        "Sample, fit, and visualize distributions",
        "Connect distributions to ML (e.g. likelihood)",
    ],
    "02_statistical_inference": [
        "Perform basic statistical inference",
        "Use point estimates, CIs, and hypothesis tests",
        "Interpret results in ML context",
    ],
    "03_bayesian_inference": [
        "Apply basic Bayesian inference",
        "Update priors with likelihood; interpret posteriors",
        "Connect Bayesian ideas to ML (e.g. uncertainty)",
    ],
}


def basename(path_rel: str) -> str:
    return Path(path_rel).stem


def fix_objectives(nb_path: Path, rel: str) -> bool:
    name = basename(rel)
    spec = OBJECTIVES_BY_BASENAME.get(name)
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
    for nb_path in sorted(C03.rglob("*.ipynb")):
        rel = nb_path.relative_to(C03).as_posix()
        if "DOCS" in rel or "PROJECTS" in rel:
            continue
        if fix_objectives(nb_path, rel):
            done.append(rel)
    print("Updated objectives:", len(done))
    for r in done:
        print(" ", r)


if __name__ == "__main__":
    main()
