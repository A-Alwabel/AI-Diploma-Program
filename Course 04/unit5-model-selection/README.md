# Unit 5: Model Selection and Boosting

Official AIAT 114 Unit 5. Unit hours: 20 (of 96 total training hours).

The closing unit: systematic hyperparameter tuning with grid/random search and gradient boosting (XGBoost, LightGBM).

## Prerequisites

- Units 1-4 of this course (regression, evaluation, classification, clustering)
- Environment set up per `../START_HERE.md` (repo root `.venv`, **ai-diploma** kernel)

## Learning Objectives

By the end of this unit you can:

- Tune hyperparameters with Grid Search and Random Search over cross-validation
- Train gradient boosting models with XGBoost and LightGBM
- Compare boosted models against baselines with ROC curves and confusion matrices
- Select a final model with a defensible, reproducible procedure

## Examples (work in this order)

| # | Notebook | What it covers |
|---|----------|----------------|
| 1 | `examples/01_grid_search.ipynb` | Grid Search and Random Search; CV-based tuning; result heatmaps |
| 2 | `examples/02_boosting.ipynb` | Gradient boosting with XGBoost and LightGBM; learning curves; feature importance |

The `examples/` folder also contains the PNG figures the notebooks produce.

## Exercises

Each exercise exists as a notebook (`.ipynb`) and an equivalent script (`.py`) - use the notebook form on the **ai-diploma** kernel.

1. `exercises/exercise_01.ipynb`
2. `exercises/exercise_02_boosting.ipynb`

Solutions are released by your instructor.

## Assessment

- Quiz: `../QUIZZES/Quiz_05_Model_Selection.md`
- Unit test: `tests/test_05.md`

After this unit: the final exam in `../ASSESSMENTS/Final_Exam.md`.
