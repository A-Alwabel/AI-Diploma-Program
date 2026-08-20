# START HERE - AIAT 113

## Welcome to Mathematics and Probability for Machine Learning

This file tells you what to do on Day 1 and how to navigate the course.

**Credit hours:** 3 · **Contact hours:** 4/week · **Total training hours:** 64 (theory+practical)

---

## Day 1 Checklist

### Step 1: Check Prerequisites

- [ ] Semester 1 courses: Course 01 (AIAT 111) and Course 02 (AIAT 112), or equivalent Python skills
- [ ] Comfortable with high school algebra
- [ ] Able to open and run a Jupyter notebook

### Step 2: Set Up Your Environment

This repo uses a single shared virtual environment at the repo root:

```bash
# From the repo root (one level above this folder)
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

When you open any notebook, select the **ai-diploma** Jupyter kernel.

### Step 3: Verify Your Installation

```bash
python "Course 03/TESTING/verify_installation.py"
```

If it reports missing libraries, install them from the repo root: `pip install -r requirements.txt`.

### Step 4: Read the Course Overview

Open `README.md` in this folder. It lists the five units, their official titles and hours, and the assessment plan.

### Step 5: Start Unit 1

Open `unit1-linear-algebra/examples/00_why_how_after.ipynb`. Every unit starts with a `00_why_how_after.ipynb` overview notebook that explains why the unit matters, how it works, and what comes after.

### Step 6: Track Your Progress

Use `STUDENT_PROGRESS_CHECKLIST.md` to mark off notebooks, exercises, and quizzes as you complete them.

---

## Learning Path

```
START_HERE.md
    ↓
Unit 1: Linear Algebra for ML and Data Transformations        (12 h)
    ↓
Unit 2: Calculus and Multivariate Calculus for ML             (12 h)
    ↓
Unit 3: Optimization and Statistical Foundations for ML       (12 h)
    ↓
Unit 4: Dimensionality Reduction and Data Representation      (14 h)
    ↓
Unit 5: Probability, Sampling, and Statistical Inference      (14 h)
    ↓
ASSESSMENTS/Final_Exam.md
```

Don't skip units — each builds on the previous one.

---

## How to Work Through Each Unit

1. **Read the unit README** — objectives, notebook list, pointers.
2. **Run the examples in file order** — `00_why_how_after.ipynb` first, then `01_...`, `02_...`, and so on.
3. **Complete the exercises** — in the unit's `exercises/` folder. Solutions are released by your instructor.
4. **Take the unit quiz** — in `QUIZZES/`. Answer keys are released by your instructor.

---

## Need Help?

- **Setup problems?** Run `TESTING/verify_installation.py` and read its output.
- **Lost?** Re-read `README.md` for the course map.
- **Progress tracking?** Use `STUDENT_PROGRESS_CHECKLIST.md`.
