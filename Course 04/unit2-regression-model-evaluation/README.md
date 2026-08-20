# Unit 2: Regression and Model Evaluation

Official AIAT 114 Unit 2. Unit hours: 19 (of 96 total training hours).

This unit evaluates the regression models built in Unit 1: cross-validation, bias-variance analysis, and learning curves.

## Prerequisites

- Unit 1 (`../unit1-regression-algorithms/`) - linear, polynomial, Ridge/Lasso regression
- Environment set up per `../START_HERE.md` (repo root `.venv`, **ai-diploma** kernel)

## Learning Objectives

By the end of this unit you can:

- Evaluate regression models with MSE, RMSE, MAE, and R²
- Apply K-Fold and other cross-validation schemes correctly
- Diagnose overfitting/underfitting via the bias-variance tradeoff
- Read learning curves to decide whether more data or a different model helps

## Examples (work in this order)

| # | Notebook | What it covers |
|---|----------|----------------|
| 1 | `examples/01_cross_validation.ipynb` | K-Fold cross-validation, CV score distributions, model comparison |
| 2 | `examples/02_bias_variance_learning_curves.ipynb` | Bias-variance tradeoff, learning curves, validation curves |

The `examples/` folder also contains the PNG figures the notebooks produce.

## Exercises

Each exercise exists as a notebook (`.ipynb`) and an equivalent script (`.py`) - use the notebook form on the **ai-diploma** kernel.

1. `exercises/exercise_01.ipynb`
2. `exercises/exercise_02_cross_validation.ipynb`

Solutions are released by your instructor.

## Assessment

- Quiz: `../QUIZZES/Quiz_02_Regression_Analysis.md`
- Unit test: `tests/test_02.md`

Next unit: `../unit3-classification/`
