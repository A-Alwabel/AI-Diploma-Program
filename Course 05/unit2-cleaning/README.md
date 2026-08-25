# Unit 2: Data Cleaning and Preparation

**Unit hours:** 19 (of 96 total training hours)

## Prerequisites

- Unit 1: Introduction to Data Science (`../unit1-introduction/`)
- Comfortable with pandas DataFrames and basic NumPy

## What This Unit Covers

Turning raw data into analysis-ready data: loading from multiple formats, handling missing values and duplicates, detecting and treating outliers, scaling and encoding features, exploratory data analysis (visual and statistical), feature extraction from unstructured data, and GPU-accelerated I/O with cuDF.

## Examples (run in order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

| # | Notebook | Description | Tier |
|---|----------|-------------|------|
| 01 | `examples/01_data_loading.ipynb` | Loading data from CSV, JSON, and Excel | **HOMEWORK** |
| 02 | `examples/02_missing_values_duplicates.ipynb` | Detecting and handling missing values and duplicates | **CORE** |
| 03 | `examples/03_outliers_transformation.ipynb` | Outlier detection and data transformation | **CORE** |
| 04 | `examples/04_feature_transformation_scaling_encoding.ipynb` | Feature scaling and categorical encoding | **CORE** |
| 05 | `examples/05_eda_visualizations.ipynb` | Visual EDA: distributions and relationships | **CORE** |
| 06 | `examples/06_statistical_eda.ipynb` | Statistical EDA: summaries, correlations, hypothesis checks | **HOMEWORK** |
| 07 | `examples/07_cudf_import_export_gpu.ipynb` | cuDF import/export and GPU acceleration (optional GPU) | **HOMEWORK** |
| 08 | `examples/08_feature_extraction_unstructured.ipynb` | Extracting features from unstructured data (e.g. text) | **HOMEWORK** |

Sample data files (`sample_data.csv/.json/.xlsx`, `large_data.csv`) used by the notebooks live in `examples/`.

## Exercise

- `exercises/exercise_01.ipynb` - data cleaning practice (a script version `exercise_01.py` is also provided)

## Quiz

- `../QUIZZES/Quiz_02_Data_Cleaning.md`
- Answer keys are released by your instructor.

## Learning Path

1. Read this README
2. Run the examples in numeric order
3. Complete `exercises/exercise_01.ipynb`
4. Take Quiz 02

**Next unit:** `../unit3-visualization/`
