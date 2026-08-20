# START HERE - AIAT 114

Welcome to **Machine Learning Algorithms and Applications** (Course 04 of the AI Diploma).

**Credit hours: 4 · Contact hours: 6/week · Total training hours: 96 (theory+practical)**

This file tells you what to do on day 1 and the exact order to work through the course.

---

## Day 1 Checklist

### Step 1: Prerequisites

You should have completed:

- AIAT 112 - Python for Artificial Intelligence (Course 02)
- AIAT 113 - Mathematics and Probability for Machine Learning (Course 03)

You should be comfortable with Python basics, NumPy, and Pandas.

### Step 2: Environment

This repository uses one shared environment for all courses:

1. From the repository root, create/activate the virtual environment:

   ```bash
   cd ..                        # repository root
   python -m venv .venv         # once, if it does not exist
   source .venv/bin/activate    # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. In Jupyter, select the **ai-diploma** kernel when opening any notebook in this course.

### Step 3: Datasets

Some notebooks load CSVs from `datasets/raw/`. Small files are already in the repo. The large CSVs must be downloaded once - follow `datasets/DOWNLOAD_INSTRUCTIONS.md`.

### Step 4: Read the course overview

Open `README.md` for the unit table, hours, CLOs, and folder guide.

---

## The Path

Work through the course in this order. Within each unit: unit `README.md` first, then the `examples/` notebooks in numeric order, then the exercises, then the unit quiz and test.

1. `unit1-regression-algorithms/` - Regression Algorithms (starts with a 3-notebook data-processing preflight)
2. `unit2-regression-model-evaluation/` - Regression and Model Evaluation
3. `unit3-classification/` - Classification Algorithms
4. `unit4-clustering/` - Clustering and Dimensionality Reduction
5. `unit5-model-selection/` - Model Selection and Boosting
6. `ASSESSMENTS/Final_Exam.md` - final exam

First notebook to open: `unit1-regression-algorithms/examples/01_data_loading_exploration.ipynb`

Each unit builds on the previous one - do not skip units.

---

## File Guide

| File/Folder | Purpose |
|-------------|---------|
| `START_HERE.md` | This file - read first |
| `README.md` | Course overview, units, hours, CLOs |
| `STUDENT_PROGRESS_CHECKLIST.md` | Track your progress |
| `unit1-...` to `unit5-...` | Unit materials (examples, exercises, tests) |
| `QUIZZES/` | One quiz per unit |
| `ASSESSMENTS/` | Final exam |
| `PROJECTS/` | Course projects with starter templates |
| `datasets/` | Datasets + `DOWNLOAD_INSTRUCTIONS.md` |
| `DOCS/` | Dataset quick reference, visualization guide |

---

## Troubleshooting

- **"No module named sklearn/pandas/xgboost"** - you are not on the **ai-diploma** kernel, or the root `requirements.txt` install did not finish.
- **"FileNotFoundError" for a CSV** - download the dataset first; see `datasets/DOWNLOAD_INSTRUCTIONS.md`.
- **Stuck on a concept** - re-read the unit README and the earlier notebooks in the unit; the notebooks are ordered deliberately.

Exercise solutions and quiz/test answer keys are released by your instructor.
