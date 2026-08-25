# Unit 1: Regression Algorithms

Official AIAT 114 Unit 1. Unit hours: 18 (of 96 total training hours).

The unit opens with a three-notebook data-processing preflight (loading, cleaning, preprocessing), then covers the regression algorithms: linear, polynomial, regularized (Ridge/Lasso), and SVR/tree-based regression.

## Prerequisites

- AIAT 112 - Python for Artificial Intelligence (Course 02)
- AIAT 113 - Mathematics and Probability for Machine Learning (Course 03)
- Environment set up per `../START_HERE.md` (repo root `.venv`, **ai-diploma** kernel)

## Learning Objectives

By the end of this unit you can:

- Load, inspect, clean, and preprocess tabular data with pandas
- Handle missing values, outliers, categorical encoding, and feature scaling
- Fit and interpret simple and multiple linear regression
- Fit polynomial regression and recognize overfitting
- Apply Ridge and Lasso regularization
- Use SVR and decision-tree regression and compare regressors

## Examples (work in this order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

| # | Notebook | What it covers | Tier |
|---|----------|----------------|------|
| 1 | `examples/01_data_loading_exploration.ipynb` | Loading CSVs with pandas; head/info/describe; first exploration plots | **HOMEWORK** |
| 2 | `examples/02_data_cleaning.ipynb` | Missing values, duplicates, outliers, type conversion | **HOMEWORK** |
| 3 | `examples/03_data_preprocessing.ipynb` | Feature scaling, categorical encoding, train/test preparation | **CORE** |
| 4 | `examples/04_linear_regression.ipynb` | Simple and multiple linear regression; coefficients; residuals | **CORE** |
| 5 | `examples/05_polynomial_regression.ipynb` | Polynomial features; degree selection; overfitting | **CORE** |
| 6 | `examples/06_ridge_lasso_regression.ipynb` | L2/L1 regularization; alpha tuning; coefficient shrinkage | **CORE** |
| 7 | `examples/07_svr_decision_tree_regression.ipynb` | Support Vector Regression and tree-based regression | **HOMEWORK** |

The `examples/` folder also contains `sample_housing_data.csv` and the PNG figures the notebooks produce.

## Exercises

Each exercise exists as a notebook (`.ipynb`) and an equivalent script (`.py`) - use the notebook form on the **ai-diploma** kernel.

1. `exercises/exercise_01.ipynb`
2. `exercises/exercise_02.ipynb`
3. `exercises/exercise_03_polynomial_regression.ipynb`
4. `exercises/exercise_04_data_preprocessing.ipynb`

Solutions are released by your instructor.

## Assessment

- Quiz: `../QUIZZES/Quiz_01_Data_Processing.md` (and `../QUIZZES/Quiz_02_Regression_Analysis.md` covers this unit's regression material)
- Unit test: `tests/test_01_regression.md`

Next unit: `../unit2-regression-model-evaluation/`
