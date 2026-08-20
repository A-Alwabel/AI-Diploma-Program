# AIAT 115 - Scalable Data Science

**New students: read `START_HERE.md` first.** It walks you through setup and the single numbered learning path for this course.

---

## Course Overview

This course trains students to process, clean, visualize, and model data at scale with Python. It covers pandas/NumPy foundations, data cleaning and preparation, visualization with Matplotlib/Seaborn/Plotly, an introduction to machine learning with scikit-learn, and scaling techniques with Dask, PySpark, and NVIDIA RAPIDS.

**Course Code:** AIAT 115
**Credit hours:** 4 · **Contact hours:** 6/week · **Total training hours:** 96 (theory+practical)

**Units (official titles):**

| Unit | Official Title | Folder | Hours |
|------|----------------|--------|-------|
| 1 | Introduction to Data Science | `unit1-introduction/` | 18 |
| 2 | Data Cleaning and Preparation | `unit2-cleaning/` | 19 |
| 3 | Data Visualization | `unit3-visualization/` | 19 |
| 4 | Introduction to Machine Learning | `unit4-ml-intro/` | 20 |
| 5 | Extending the Scope of Data Science | `unit5-scaling/` | 20 |

---

## Prerequisites

- **AIAT 112 - Python for AI** (Course 02) or equivalent Python fundamentals (variables, functions, data structures)
- Familiarity with NumPy and pandas helps but is reviewed in Unit 1
- **Python 3.10+** via the repository root virtual environment (see Setup)

---

## Setup

All notebooks in this course run on the repository root virtual environment (`.venv`) with the **"ai-diploma"** Jupyter kernel.

1. From the repository root, install dependencies into `.venv` (see `DOCS/SETUP_INSTRUCTIONS.md`)
2. In Jupyter, select the **ai-diploma** kernel before running a notebook
3. GPU (cuDF/RAPIDS) and PySpark sections are optional - see `DOCS/OPTIONAL_DEPENDENCIES.md` and `DOCS/COLAB_SETUP.md`

---

## Folder Structure

```
Course 05/
├── README.md                        This file
├── START_HERE.md                    Day 1 guide and learning path
├── STUDENT_PROGRESS_CHECKLIST.md    Progress tracker
├── unit1-introduction/              Unit 1: Introduction to Data Science
├── unit2-cleaning/                  Unit 2: Data Cleaning and Preparation
├── unit3-visualization/             Unit 3: Data Visualization
├── unit4-ml-intro/                  Unit 4: Introduction to Machine Learning
├── unit5-scaling/                   Unit 5: Extending the Scope of Data Science
├── QUIZZES/                         One quiz per unit
├── ASSESSMENTS/                     Final exam
├── PROJECTS/                        Capstone (01_Data_Pipeline) + optional projects
├── CASE_STUDIES/                    Case study analysis
├── PRESENTATIONS/SLIDES/            Lecture slide decks
└── DOCS/                            Setup and dependency guides
```

Each unit folder contains `examples/` (numbered notebooks) and `exercises/` (practice work).

---

## Learning Path

Follow the units in order; each builds on the previous one. Within each unit: read the unit `README.md`, run the `examples/` notebooks in numeric order, complete the exercise, then take the unit quiz in `QUIZZES/`.

1. `unit1-introduction/` -> Quiz 01
2. `unit2-cleaning/` -> Quiz 02
3. `unit3-visualization/` -> Quiz 03
4. `unit4-ml-intro/` -> Quiz 04
5. `unit5-scaling/` -> Quiz 05
6. Final exam: `ASSESSMENTS/Final_Exam.md`
7. Capstone project: `PROJECTS/01_Data_Pipeline/`

---

## Assessment

- **Quizzes:** one per unit in `QUIZZES/` (see `QUIZZES/README.md`)
- **Final exam:** `ASSESSMENTS/Final_Exam.md` (see `ASSESSMENTS/README.md`)
- **Capstone project:** `PROJECTS/01_Data_Pipeline/` - end-to-end scalable data pipeline; Projects 02 and 03 are optional extensions
- **Case study:** `CASE_STUDIES/case_study_01_scalable_data_processing.md`
- **Exercises:** each unit's `exercises/` folder

Answer keys and reference solutions are released by your instructor.

---

## Required Libraries

- **Data processing:** pandas, numpy
- **Machine learning:** scikit-learn
- **Visualization:** matplotlib, seaborn, plotly
- **Distributed computing:** dask (PySpark optional)
- **GPU acceleration (optional):** cuDF/cuML (RAPIDS, requires NVIDIA GPU)

See the repository root `requirements.txt` for versions.

---

## GPU Notes

A GPU is **not required**. All core notebooks run on CPU with pandas/scikit-learn; cuDF/RAPIDS sections are optional demonstrations of GPU acceleration.

- No NVIDIA GPU: run everything on CPU, or use Google Colab's free GPU (`DOCS/COLAB_SETUP.md`)
- NVIDIA GPU available: install RAPIDS locally (`DOCS/OPTIONAL_DEPENDENCIES.md`)
