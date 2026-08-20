# AIAT 113 - Mathematics and Probability for Machine Learning

**New students: read `START_HERE.md` first.** It walks you through setup and the learning path.

---

## Course Overview

This course covers the mathematics behind machine learning: linear algebra, calculus, optimization, dimensionality reduction, and probability with statistical inference. Every unit pairs the theory with runnable Python notebooks.

**Course Code:** AIAT 113
**Credit hours:** 3 · **Contact hours:** 4/week · **Total training hours:** 64 (theory+practical)

---

## Prerequisites

- Semester 1 program (AIAT 111–116); this course assumes:
  - Course 01 (AIAT 111) — basic AI concepts
  - Course 02 (AIAT 112) — Python programming (variables, functions, NumPy basics)
- High school algebra; prior exposure to calculus helps but is reviewed in Unit 2

**Setup:** use the repo-root virtual environment (`.venv`) and select the **ai-diploma** Jupyter kernel when opening notebooks. Verify your setup with:

```bash
python TESTING/verify_installation.py
```

---

## Course Learning Outcomes (CLOs)

By the end of this course, the trainee will be able to:

1. Demonstrate understanding of basic mathematical concepts, including linear algebra and probability, and their applications in AI and machine learning.
2. Apply mathematical techniques such as matrix operations, eigenvalue analysis, and multivariate calculus to machine learning problems.
3. Evaluate and interpret data using statistical methods, including hypothesis testing and confidence intervals.
4. Use dimensionality reduction techniques such as PCA, SVD, and t-SNE to analyze and visualize high-dimensional datasets.
5. Formulate, implement, and optimize machine learning models using gradient descent and other optimization techniques.
6. Implement mathematical and statistical algorithms relevant to machine learning in Python.

---

## Units

Follow the units in order; each starts with a `00_why_how_after.ipynb` overview notebook.

| Unit | Official Title | Hours | Folder |
|---|---|---|---|
| 1 | Linear Algebra for ML and Data Transformations | 12 | [unit1-linear-algebra/](unit1-linear-algebra/README.md) |
| 2 | Calculus and Multivariate Calculus for ML | 12 | [unit2-calculus/](unit2-calculus/README.md) |
| 3 | Optimization and Statistical Foundations for ML | 12 | [unit3-optimization/](unit3-optimization/README.md) |
| 4 | Dimensionality Reduction and Data Representation Techniques | 14 | [unit4-dimensionality-reduction/](unit4-dimensionality-reduction/README.md) |
| 5 | Probability, Sampling, and Statistical Inference | 14 | [unit5-probability/](unit5-probability/README.md) |

---

## Course Structure

```
Course 03/
├── README.md                        This file
├── START_HERE.md                    Day 1 guide - read first
├── STUDENT_PROGRESS_CHECKLIST.md    Track your progress
├── unit1-linear-algebra/            Unit 1: examples/ + exercises/
├── unit2-calculus/                  Unit 2: examples/ + exercises/
├── unit3-optimization/              Unit 3: examples/ + exercises/
├── unit4-dimensionality-reduction/  Unit 4: examples/ + exercises/
├── unit5-probability/               Unit 5: examples/ + exercises/
├── QUIZZES/                         One quiz per unit
├── ASSESSMENTS/                     Final exam
├── PROJECTS/                        Three applied projects
├── CASE_STUDIES/                    Mathematical modeling case study
├── PRESENTATIONS/                   Lecture slides
├── SELF_ASSESSMENT/                 Self-check materials
└── TESTING/                         verify_installation.py
```

---

## Learning Path

`START_HERE.md` → Unit 1 → Unit 2 → Unit 3 → Unit 4 → Unit 5 → `ASSESSMENTS/`

Within each unit: read the unit README → run the examples in numeric order → do the exercises → take the unit quiz. Don't skip units; each builds on the previous one.

---

## Assessment

- **Quizzes:** one per unit in [QUIZZES/](QUIZZES/README.md)
- **Exercises:** in each unit's `exercises/` folder
- **Projects:** three applied projects in [PROJECTS/](PROJECTS/README.md)
- **Final exam:** [ASSESSMENTS/Final_Exam.md](ASSESSMENTS/Final_Exam.md)

Answer keys and exercise solutions are released by your instructor.

---

## Required Libraries

numpy, scipy, sympy, statsmodels, scikit-learn, matplotlib, seaborn, jupyter — all installed in the repo-root `.venv` (see `../requirements.txt`).
