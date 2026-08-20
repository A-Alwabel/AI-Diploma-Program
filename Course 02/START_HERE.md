# START HERE - AIAT 112: Python for Artificial Intelligence

Welcome to Course 02. This file tells you what to do on day 1 and how to work
through the course.

Credit hours: 4 · Contact hours: 6/week · Total training hours: 96 (theory+practical)

---

## Day 1 Checklist

### Step 1: Check prerequisites

- Completed Semester 1 entry requirements; this course is taken alongside the
  other Semester 1 courses (AIAT 111-116).
- Completed or currently taking **AIAT 111 - Introduction to AI Applications
  and Concepts (Course 01)**.
- Comfortable with basic Python: variables, lists, dictionaries, loops,
  functions, classes.

If your Python is weak, review Python basics before Unit 1 - the whole course
is hands-on Python.

### Step 2: Set up your environment

This repository uses one shared virtual environment at the repository root:

```bash
# from the repository root (one level above this folder)
python -m venv .venv          # only if .venv does not exist yet
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

In Jupyter, select the **ai-diploma** kernel when opening notebooks.

Verify your setup:

```bash
python "Course 02/TESTING/verify_installation.py"
```

If you hit problems, see `DOCS/INSTALLATION_GUIDE.md`.

### Step 3: Read the course overview

Open `README.md` for the course structure, unit list, and hours.

### Step 4: Start Unit 1

Open `unit1-search-algorithms/README.md`, then work through its notebooks in
order, starting with `unit1-search-algorithms/examples/01_python_libraries_for_ai.ipynb`.

---

## Learning Path

Work through the units in order. In each unit:

1. Read the unit `README.md`.
2. Work through the notebooks in `examples/` in numeric file order.
3. Do the exercise in `exercises/`.
4. Take the unit quiz in `QUIZZES/`.

```
Unit 1: Course Introduction and Search Algorithms
   examples 01-02 -> exercise 01 -> Quiz_00 + Quiz_01
Unit 2: Knowledge Representation
   examples 01-04 -> exercise 02 -> Quiz_02
Unit 3: Learning Under Uncertainty
   examples 01-04 -> exercise 03 -> Quiz_03
Unit 4: Optimization Techniques
   example 01 -> exercise 04 -> Quiz_04
Unit 5: AI-Based Learning Models
   example 01 -> exercise 05 -> Quiz_05
Then: one project from PROJECTS/ and the final exam (ASSESSMENTS/)
```

Each unit builds on the previous one - do not skip ahead.

**Math note for Unit 4:** Optimization uses gradients and vector operations.
If you need a refresher, review Course 03 (AIAT 113) `unit1-linear-algebra`
and `unit2-calculus`.

---

## Tracking Progress

Use `STUDENT_PROGRESS_CHECKLIST.md` to track every notebook, exercise, and quiz.

---

## Need Help?

- Installation problems -> `DOCS/INSTALLATION_GUIDE.md`
- Common questions -> `DOCS/FAQ.md`
- Quick syntax/library reference -> `DOCS/QUICK_REFERENCE.md`
- Extra practice -> `DOCS/PRACTICE_PROBLEMS.md`
- Anything else -> ask your instructor

Solutions and answer keys are released by your instructor.
