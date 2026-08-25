# Unit 3: Classification Algorithms

Official AIAT 114 Unit 3. Unit hours: 19 (of 96 total training hours).

Supervised classification: logistic regression, decision trees and random forests, SVM, KNN, Naive Bayes, and ensemble techniques - with the metrics to evaluate them.

## Prerequisites

- Units 1-2 (regression and model evaluation)
- Environment set up per `../START_HERE.md` (repo root `.venv`, **ai-diploma** kernel)

## Learning Objectives

By the end of this unit you can:

- Train and interpret logistic regression classifiers
- Build decision trees and random forests; read feature importances
- Apply SVM with different kernels and tune C/gamma
- Use KNN and Naive Bayes and know when each fits
- Combine models with bagging and boosting
- Evaluate classifiers with accuracy, precision/recall, F1, confusion matrices, ROC/AUC

## Examples (work in this order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

| # | Notebook | What it covers | Tier |
|---|----------|----------------|------|
| 1 | `examples/01_logistic_regression.ipynb` | Logistic regression; confusion matrix, ROC curve, threshold analysis | **CORE** |
| 2 | `examples/02_decision_trees.ipynb` | Decision trees and random forest; feature importance; tree depth | **CORE** |
| 3 | `examples/03_svm.ipynb` | SVM kernels; C and gamma effects; support vectors; decision boundaries | **CORE** |
| 4 | `examples/04_knn.ipynb` | K-Nearest Neighbors; choosing K; distance metrics | **ENRICHMENT** |
| 5 | `examples/05_random_forest_naive_bayes.ipynb` | Random forest vs Naive Bayes comparison | **CORE** |
| 6 | `examples/06_ensemble_methods_bagging_boosting.ipynb` | Bagging and boosting ensembles | **CORE** |

The `examples/` folder also contains the PNG figures the notebooks produce.

## Exercises

Each exercise exists as a notebook (`.ipynb`) and an equivalent script (`.py`) - use the notebook form on the **ai-diploma** kernel.

1. `exercises/exercise_01.ipynb`
2. `exercises/exercise_02_logistic_regression.ipynb`
3. `exercises/exercise_03_svm.ipynb`
4. `exercises/exercise_04_knn.ipynb`

Solutions are released by your instructor.

## Assessment

- Quiz: `../QUIZZES/Quiz_03_Classification.md`
- Unit test: `tests/test_03.md`

Next unit: `../unit4-clustering/`
