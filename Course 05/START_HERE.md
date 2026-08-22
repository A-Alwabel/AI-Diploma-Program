# START HERE - AIAT 115 Scalable Data Science

Welcome. This file tells you what to do on Day 1 and gives the single numbered path through the course.

**Course facts:** Credit hours: 4 · Contact hours: 6/week · Total training hours: 96 (theory+practical)

---

## Day 1 Setup

### Step 1: Check prerequisites

- **AIAT 112 - Python for AI** (Course 02) or equivalent Python fundamentals
- Comfortable with variables, functions, lists, and dictionaries (NumPy/pandas are reviewed in Unit 1)

### Step 2: Set up the environment

This course uses the **repository root virtual environment** (`.venv`) and the **"ai-diploma"** Jupyter kernel.

1. Follow `DOCS/SETUP_INSTRUCTIONS.md` to install dependencies into the root `.venv`
2. Start Jupyter and select the **ai-diploma** kernel for every notebook
3. Verify the basics work:

   ```python
   import pandas, numpy, matplotlib, seaborn, sklearn
   print("OK")
   ```

GPU (cuDF/RAPIDS) and PySpark content is optional - see `DOCS/OPTIONAL_DEPENDENCIES.md`, and `DOCS/COLAB_SETUP.md` for free GPU access on Google Colab.

### Step 3: Read the course overview

Read `README.md` for the unit table, hours, and assessment overview.

---

## The Learning Path

Follow this order. Within each unit: read the unit `README.md`, run the `examples/` notebooks in numeric order, complete the exercise, then take the unit quiz.

1. **Unit 1 - Introduction to Data Science** (`unit1-introduction/`)
   - Examples 01-09 -> `exercises/exercise_01.ipynb` -> `QUIZZES/Quiz_01_Introduction_Data_Science.md`
2. **Unit 2 - Data Cleaning and Preparation** (`unit2-cleaning/`)
   - Examples 01-08 -> `exercises/exercise_01.ipynb` -> `QUIZZES/Quiz_02_Data_Cleaning.md`
3. **Unit 3 - Data Visualization** (`unit3-visualization/`)
   - Examples 01-08 -> `exercises/exercise_01.ipynb` -> `QUIZZES/Quiz_03_Data_Visualization.md`
4. **Unit 4 - Introduction to Machine Learning** (`unit4-ml-intro/`) — ML at scale: a deliberate recap that reinforces Course 04 (AIAT 114), focused on workflow and training cost
   - Examples 01-12 -> `exercises/exercise_01.ipynb` -> `QUIZZES/Quiz_04_ML_Introduction.md`
5. **Unit 5 - Extending the Scope of Data Science** (`unit5-scaling/`)
   - Examples 01-10 -> `exercises/exercise_01.ipynb` -> `QUIZZES/Quiz_05_Scaling_Production.md`
6. **Final exam** - `ASSESSMENTS/Final_Exam.md` (after all five units; see `ASSESSMENTS/README.md`)
7. **Capstone project** - `PROJECTS/01_Data_Pipeline/` (end-to-end scalable data pipeline; Projects 02 and 03 in `PROJECTS/` are optional extensions)

Each unit builds on the previous one - do not skip ahead. Quiz answer keys are released by your instructor.

**Lecture slides:** `PRESENTATIONS/SLIDES/` contains the slide decks used in class; the numbered notebooks remain the canonical study path.

**Track your progress:** `STUDENT_PROGRESS_CHECKLIST.md`

---

## File Guide

| File/Folder | Purpose |
|-------------|---------|
| `START_HERE.md` | This file - Day 1 guide and learning path |
| `README.md` | Course overview, unit table, hours |
| `STUDENT_PROGRESS_CHECKLIST.md` | Progress tracker |
| `unit1-introduction/` ... `unit5-scaling/` | Unit materials (examples + exercises) |
| `QUIZZES/` | One quiz per unit |
| `ASSESSMENTS/` | Final exam |
| `PROJECTS/` | Capstone (01_Data_Pipeline) + optional projects |
| `CASE_STUDIES/` | Case study analysis |
| `PRESENTATIONS/SLIDES/` | Lecture slide decks |
| `DOCS/` | Setup, Colab, and optional-dependency guides |

---

## Troubleshooting

- **`No module named 'pandas'`** - dependencies are not installed in the active environment; redo Step 2 and confirm the **ai-diploma** kernel is selected
- **cuDF/RAPIDS import errors** - GPU libraries are optional; run the CPU (pandas) path or use Colab (`DOCS/COLAB_SETUP.md`)
- **PySpark errors in Unit 5** - PySpark is optional; see `DOCS/OPTIONAL_DEPENDENCIES.md`
- **A notebook is confusing** - confirm you completed the earlier units and the unit README first

---

**Next action:** open `unit1-introduction/README.md`, then run `unit1-introduction/examples/01_data_science_intro.ipynb`.
