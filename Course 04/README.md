# AIAT 114 - Machine Learning Algorithms and Applications

Course 04 of the AI Diploma. Supervised and unsupervised machine learning with scikit-learn: regression, classification, clustering, dimensionality reduction, model selection, and boosting.

**Credit hours: 4 · Contact hours: 6/week · Total training hours: 96 (theory+practical)**

New students: read `START_HERE.md` first.

---

## Units

Follow the units in order. Each unit folder has a `README.md`, an `examples/` folder (numbered notebooks), an `exercises/` folder, and a `tests/` folder with the unit test.

| Unit | Folder | Official title | Hours |
|------|--------|----------------|-------|
| 1 | `unit1-regression-algorithms/` | Regression Algorithms | 18 |
| 2 | `unit2-regression-model-evaluation/` | Regression and Model Evaluation | 19 |
| 3 | `unit3-classification/` | Classification Algorithms | 19 |
| 4 | `unit4-clustering/` | Clustering and Dimensionality Reduction | 20 |
| 5 | `unit5-model-selection/` | Model Selection and Boosting | 20 |

Unit 1 opens with a three-notebook data-processing preflight (loading, cleaning, preprocessing) before the regression notebooks.

---

## Learning Path

```
START_HERE.md
    -> Unit 1: Regression Algorithms
    -> Unit 2: Regression and Model Evaluation
    -> Unit 3: Classification Algorithms
    -> Unit 4: Clustering and Dimensionality Reduction
    -> Unit 5: Model Selection and Boosting
    -> ASSESSMENTS/ (final exam)
```

Within each unit: read the unit `README.md`, work through `examples/` in numeric order, do the exercises, take the quiz for that unit in `QUIZZES/`, then the unit test in the unit's `tests/` folder.

---

## Prerequisites

- AIAT 112 - Python for Artificial Intelligence (Course 02)
- AIAT 113 - Mathematics and Probability for Machine Learning (Course 03)
- Comfortable with Python, NumPy, and Pandas

---

## Setup

1. Use the repo root virtual environment: `.venv` at the repository root (install with `pip install -r ../requirements.txt` if not already set up).
2. In Jupyter, select the **ai-diploma** kernel for all notebooks in this course.
3. Some notebooks use datasets in `datasets/raw/`. Small files are included; for the large CSVs follow `datasets/DOWNLOAD_INSTRUCTIONS.md`.

Main libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, xgboost, lightgbm.

---

## Course Learning Outcomes (CLOs)

- **CLO1:** Apply data processing methodologies (missing data, categorical variables, feature scaling) in machine learning systems.
- **CLO2:** Demonstrate proficiency in linear and polynomial regression, including interpreting coefficients and assumptions.
- **CLO3:** Evaluate advanced regression algorithms (Ridge, Lasso, SVR) and select appropriate models for a use case.
- **CLO4:** Build and evaluate classification models (logistic regression, decision trees, SVM, random forests) using diverse performance metrics.
- **CLO5:** Implement clustering (K-Means, hierarchical) and dimensionality reduction (PCA) for exploratory data analysis.
- **CLO6:** Employ model selection strategies (cross-validation, grid search) and boosting (AdaBoost, XGBoost) to improve performance.
- **CLO7:** Analyze and interpret machine learning results and present recommendations.

---

## Assessment

- **Quizzes:** `QUIZZES/` - one quiz per unit (Quiz 01-05).
- **Unit tests:** `unit*/tests/` - one written test per unit.
- **Final exam:** `ASSESSMENTS/Final_Exam.md`.
- **Projects:** `PROJECTS/` - applied projects with starter templates.
- **Case study:** `CASE_STUDIES/01_ml_model_selection_case_study.md`.

Solutions and answer keys are released by your instructor.

---

## Folder Guide

| Folder | Contents |
|--------|----------|
| `unit1-...` to `unit5-...` | Unit notebooks, exercises, and tests |
| `QUIZZES/` | Unit quizzes |
| `ASSESSMENTS/` | Final exam |
| `PROJECTS/` | Course projects and templates |
| `CASE_STUDIES/` | Case study material |
| `PRESENTATIONS/SLIDES/` | Official lecture decks (01-15) |
| `DOCS/` | Dataset quick reference, visualization guide, notebook-PDF mapping |
| `datasets/` | Datasets and download scripts (see `datasets/DOWNLOAD_INSTRUCTIONS.md`) |
| `SELF_ASSESSMENT/` | Self-assessment notes |

Track your progress with `STUDENT_PROGRESS_CHECKLIST.md`.
