#!/usr/bin/env python3
"""Add 'Inputs & Outputs' section to all Course 05 notebooks that don't have it."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
C05 = ROOT / "Course 05"

# Custom (inputs, outputs) per notebook. Path relative to Course 05.
IO_MAP = {
    # Unit 1
    "unit1-introduction/examples/01_data_science_intro.ipynb": (
        ["Libraries: pandas, numpy, matplotlib, seaborn", "Concepts: data science lifecycle (9 steps), DataFrames, FAQ topics"],
        ["Printed summaries and lifecycle diagram (figure)", "FAQ answers and \"Next steps\" guidance"],
    ),
    "unit1-introduction/examples/02_pandas_numpy_basics.ipynb": (
        ["NumPy arrays, DataFrames, groupby, basic viz", "Libraries: pandas, numpy, matplotlib, seaborn"],
        ["Array operations, describe, plots", "Summary and next → Example 3"],
    ),
    "unit1-introduction/examples/03_cudf_introduction.ipynb": (
        ["Colab vs local setup, cuDF vs pandas", "Libraries: pandas, cudf (or pandas fallback), numpy"],
        ["Setup message or \"Libraries imported\"", "CPU/GPU timing comparisons"],
    ),
    "unit1-introduction/examples/04_python_basics_loops_conditions.ipynb": (
        ["Python: if/elif/else, for, while, comprehensions, lambda, try/except", "No external data; small in-notebook examples"],
        ["Printed examples for each construct"],
    ),
    "unit1-introduction/examples/05_jupyter_notebooks_best_practices.ipynb": (
        ["Structure, seeds, dependencies, clear names", "Concepts from Example 4"],
        ["Best-practice examples", "Summary and next → Example 6"],
    ),
    "unit1-introduction/examples/06_data_structures_lists_dictionaries.ipynb": (
        ["Lists, dicts, list↔dict, nested structures", "Basic Python"],
        ["Examples for each structure", "Next → Examples 2, 7"],
    ),
    "unit1-introduction/examples/07_data_science_applications.ipynb": (
        ["Lifecycle in practice, small projects", "Concepts from Examples 1–6"],
        ["Part 1 lifecycle print", "Comment-only cells (no output); summary and next units"],
    ),
    "unit1-introduction/examples/08_numba_jit_compilation.ipynb": (
        ["Numba JIT, pure Python vs compiled", "Libraries: numba, numpy"],
        ["Timing comparisons"],
    ),
    "unit1-introduction/examples/09_advanced_numpy_operations.ipynb": (
        ["Advanced array operations, building on Example 2", "NumPy, matplotlib"],
        ["Numerical results", "Visualizations"],
    ),
    "unit1-introduction/exercises/exercise_01.ipynb": (
        ["Instructions and sample dataset (or create in notebook)", "pandas, numpy, matplotlib, seaborn (optional: cuDF)"],
        ["Exploration, stats, visualizations", "Optional CPU/cuDF comparison"],
    ),
    # Unit 2
    "unit2-cleaning/examples/01_data_loading.ipynb": (
        ["Libraries: pandas", "File paths: CSV, Excel, JSON; sample files in examples/"],
        ["Loaded DataFrames", "Printed success messages and basic stats"],
    ),
    "unit2-cleaning/examples/02_missing_values_duplicates.ipynb": (
        ["DataFrame with missing values and duplicates", "pandas"],
        ["Cleaned DataFrame", "Counts, imputation results, printed summaries"],
    ),
    "unit2-cleaning/examples/03_outliers_transformation.ipynb": (
        ["Data with outliers", "pandas, numpy"],
        ["Transformed data", "Plots, stats, printed summaries"],
    ),
    "unit2-cleaning/examples/04_feature_transformation_scaling_encoding.ipynb": (
        ["Raw features", "pandas, sklearn (scaling, encoding)"],
        ["Scaled/encoded features", "Printed results"],
    ),
    "unit2-cleaning/examples/05_eda_visualizations.ipynb": (
        ["Clean dataset", "pandas, matplotlib, seaborn"],
        ["EDA plots", "Insights"],
    ),
    "unit2-cleaning/examples/06_statistical_eda.ipynb": (
        ["Dataset", "pandas, scipy/stats, viz libraries"],
        ["Statistical summaries", "Plots and tables"],
    ),
    "unit2-cleaning/examples/07_cudf_import_export_gpu.ipynb": (
        ["CSV/Parquet files", "cuDF (or pandas fallback)"],
        ["GPU load/save timings", "DataFrames"],
    ),
    "unit2-cleaning/examples/08_feature_extraction_unstructured.ipynb": (
        ["Text or image data", "Libraries for feature extraction"],
        ["Extracted features", "Printed summaries"],
    ),
    "unit2-cleaning/exercises/exercise_01.ipynb": (
        ["Instructions; sample data (or path to dataset)", "pandas, viz libraries"],
        ["Cleaned data", "EDA outputs", "Plots and summaries"],
    ),
    # Unit 3
    "unit3-visualization/examples/01_chart_types_matplotlib_seaborn.ipynb": (
        ["Sample data", "matplotlib, seaborn"],
        ["Line, bar, histogram, scatter, etc.", "Figures"],
    ),
    "unit3-visualization/examples/02_matplotlib_basics.ipynb": (
        ["Data", "matplotlib"],
        ["Basic plots", "Customization examples"],
    ),
    "unit3-visualization/examples/03_seaborn_plots.ipynb": (
        ["Data", "seaborn, pandas"],
        ["Statistical plots", "Figures"],
    ),
    "unit3-visualization/examples/04_plotly_interactive.ipynb": (
        ["Data", "plotly", "pandas"],
        ["Interactive charts", "HTML outputs"],
    ),
    "unit3-visualization/examples/05_interactive_visualizations_plotly.ipynb": (
        ["Data", "plotly"],
        ["Interactive visualizations", "HTML"],
    ),
    "unit3-visualization/examples/06_customizing_annotating_visualizations.ipynb": (
        ["Charts from earlier examples", "matplotlib, seaborn"],
        ["Annotated, publication-ready figures"],
    ),
    "unit3-visualization/examples/07_visualization_best_practices.ipynb": (
        ["Data", "matplotlib, seaborn"],
        ["Best-practice examples", "Do's and don'ts"],
    ),
    "unit3-visualization/examples/08_advanced_visualization_types.ipynb": (
        ["Data", "matplotlib, seaborn, plotly"],
        ["Advanced chart types", "Figures"],
    ),
    "unit3-visualization/exercises/exercise_01.ipynb": (
        ["Instructions; dataset", "matplotlib, seaborn, (optional) plotly"],
        ["Visualizations", "Captions and insights"],
    ),
    # Unit 4
    "unit4-ml-intro/examples/01_pandas_data_manipulation.ipynb": (
        ["Dataset", "pandas"],
        ["Manipulated DataFrame", "Printed results"],
    ),
    "unit4-ml-intro/examples/02_data_preparation_ml_tasks.ipynb": (
        ["Raw data", "pandas, sklearn"],
        ["Train/test splits", "Encoded/scaled features"],
    ),
    "unit4-ml-intro/examples/03_implementing_ml_models_sklearn.ipynb": (
        ["Prepared features and targets", "sklearn"],
        ["Fitted model", "Basic metrics"],
    ),
    "unit4-ml-intro/examples/04_linear_regression.ipynb": (
        ["Features X, target y", "sklearn"],
        ["Model coefficients", "Plots", "Metrics"],
    ),
    "unit4-ml-intro/examples/05_supervised_learning_logistic_regression.ipynb": (
        ["Features X, binary target y", "sklearn"],
        ["Logistic model", "Metrics", "Plots"],
    ),
    "unit4-ml-intro/examples/06_classification.ipynb": (
        ["Features, labels", "sklearn"],
        ["Classifier", "Metrics", "Confusion matrix", "Plots"],
    ),
    "unit4-ml-intro/examples/07_model_evaluation.ipynb": (
        ["Trained model", "Test set"],
        ["Metrics (accuracy, precision, recall, etc.)", "Plots"],
    ),
    "unit4-ml-intro/examples/08_hyperparameter_tuning_grid_random_search.ipynb": (
        ["Model, param grid", "sklearn"],
        ["Best params", "CV results", "Printed summary"],
    ),
    "unit4-ml-intro/examples/09_unsupervised_learning_kmeans.ipynb": (
        ["Unlabeled data", "sklearn"],
        ["Cluster labels", "Centroids", "Plots"],
    ),
    "unit4-ml-intro/examples/10_clustering_unsupervised.ipynb": (
        ["Unlabeled data", "sklearn"],
        ["Clusters", "Visualizations"],
    ),
    "unit4-ml-intro/examples/11_real_world_problem_solving.ipynb": (
        ["Real-world dataset", "sklearn, pandas"],
        ["Supervised + unsupervised mix", "Models", "Insights"],
    ),
    "unit4-ml-intro/examples/12_cpu_vs_gpu_ml.ipynb": (
        ["Dataset", "sklearn; optional GPU libs"],
        ["CPU vs GPU timings", "Model comparison"],
    ),
    "unit4-ml-intro/exercises/exercise_01.ipynb": (
        ["Instructions; exercise_01.py or inline tasks", "sklearn, pandas"],
        ["Trained models", "Evaluations", "Plots"],
    ),
    # Unit 5
    "unit5-scaling/examples/01_big_data_theory.ipynb": (
        ["Concepts: 4 Vs, MapReduce, fault tolerance", "Optional MapReduce-style code"],
        ["Theory recap", "Optional code demos"],
    ),
    "unit5-scaling/examples/02_dask_distributed.ipynb": (
        ["Data", "dask"],
        ["Distributed ops", "Timings", "Results"],
    ),
    "unit5-scaling/examples/03_pyspark_distributed.ipynb": (
        ["Data", "PySpark"],
        ["Distributed processing", "Outputs"],
    ),
    "unit5-scaling/examples/04_rapids_workflows.ipynb": (
        ["Data", "RAPIDS (e.g. cuDF)"],
        ["GPU workflows", "Timings"],
    ),
    "unit5-scaling/examples/05_production_pipelines.ipynb": (
        ["Pipeline stages", "Dask/PySpark or similar"],
        ["Pipeline outputs", "Logs"],
    ),
    "unit5-scaling/examples/06_performance_optimization.ipynb": (
        ["Code or workflow", "profiling/optimization tools"],
        ["Optimized version", "Timing comparisons"],
    ),
    "unit5-scaling/examples/07_large_datasets.ipynb": (
        ["Large files", "chunking/distributed libs"],
        ["Processed data", "Stats"],
    ),
    "unit5-scaling/examples/08_deployment.ipynb": (
        ["Trained model", "Flask/FastAPI"],
        ["API demo", "Request/response examples"],
    ),
    "unit5-scaling/examples/09_model_monitoring.ipynb": (
        ["Model", "Input/output logs"],
        ["Monitoring metrics", "Plots"],
    ),
    "unit5-scaling/examples/10_data_pipeline_automation.ipynb": (
        ["Pipeline config", "scheduling/automation"],
        ["Automated runs", "Logs"],
    ),
    "unit5-scaling/exercises/exercise_01.ipynb": (
        ["Instructions; data or pipeline template", "Dask/PySpark/RAPIDS as needed"],
        ["Distributed or scaled outputs", "Logs"],
    ),
}

GENERIC = (
    ["Libraries and concepts as introduced in this notebook; see prerequisites and code comments."],
    ["Printed results, figures, and summaries as shown when you run the cells."],
)


def has_io_section(cells):
    for c in cells:
        if c.get("cell_type") != "markdown":
            continue
        src = "".join(c.get("source", []))
        if "Inputs & Outputs" in src or "Inputs & " in src and "Outputs" in src:
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
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)
    cells = nb["cells"]
    if has_io_section(cells):
        return "skip"
    idx = first_code_index(cells)
    if idx is None:
        return "no_code"
    inputs, outputs = IO_MAP.get(rel, GENERIC)
    io_cell = make_io_cell(inputs, outputs)
    cells.insert(idx, io_cell)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    return "ok"


def main():
    added = []
    skipped = []
    no_code = []
    for nb_path in sorted(C05.rglob("*.ipynb")):
        rel = nb_path.relative_to(C05).as_posix()
        if "DOCS" in rel or "PROJECTS" in rel or "artifacts" in rel:
            continue
        res = process(nb_path, rel)
        if res == "ok":
            added.append(rel)
        elif res == "skip":
            skipped.append(rel)
        else:
            no_code.append(rel)
    print("Added Inputs & Outputs:")
    for r in added:
        print(" ", r)
    print("\nSkipped (already have section):")
    for r in skipped:
        print(" ", r)
    print("\nSkipped (no code cell):")
    for r in no_code:
        print(" ", r)
    print(f"\nTotal: {len(added)} added, {len(skipped)} skipped, {len(no_code)} no code.")


if __name__ == "__main__":
    main()
