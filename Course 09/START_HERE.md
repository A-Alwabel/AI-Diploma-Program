# Start Here

This course is part of Semester 2 of the AI Diploma Program.

**Course:** AIAT 123 - Reinforcement Learning
**Credit hours:** 4 · **Contact hours:** 6/week · **Total training hours:** 96 (theory+practical)

## Student Quick Start

1. Read `README.md` and skim `RL_LEARNING_JOURNEY.md` (how Units 1–5 connect)
2. Set up the environment (below)
3. Start `unit1-rl-fundamentals/`
4. Follow the numbered notebooks in file order (`01`, `02`, `03`, ...)
5. Complete the unit exercise, then the unit quiz
6. Repeat for Units 2–5, then do the project in `PROJECTS/` and finish with
   `ASSESSMENTS/Final_Exam.md`
7. Re-open `RL_LEARNING_JOURNEY.md` before the project to reconnect the arc

## Environment Setup

This repository uses a shared virtual environment at the repo root:

1. From the repository root, create/activate the shared environment in `.venv`
   (see `../docs/SETUP_GUIDE.md` for the exact commands).
2. In Jupyter, select the **ai-diploma** kernel when opening the notebooks in
   this course.

The notebooks in this course use NumPy, Matplotlib, PyTorch, and
`gymnasium[classic-control]`, all installed from the repository root
`../requirements.txt`.

Verify your setup inside a notebook running the **ai-diploma** kernel:

```python
import torch
import gymnasium
import numpy

print("PyTorch:", torch.__version__)
print("Gymnasium:", gymnasium.__version__)
print("NumPy:", numpy.__version__)
```

## Before You Begin

Prerequisites:

- Semester 1 (AIAT 111–116): Python, probability and statistics, machine
  learning basics
- AIAT 122 - Deep Learning: neural networks and PyTorch basics

## The Learning Path

For each unit, in order (Unit 1 → Unit 5):

1. Read the `README.md` inside the unit folder
2. Complete the numbered example notebooks in file order
3. Complete the unit exercise notebook in `exercises/`
4. Take the unit quiz in `QUIZZES/`
5. Update `STUDENT_PROGRESS_CHECKLIST.md`

After Unit 5: complete the project in `PROJECTS/`, then
`ASSESSMENTS/Final_Exam.md`.

## What if a notebook is confusing?

1. Re-read the unit `README.md`
2. Review the previous notebook in the same unit
3. Check `../docs/TROUBLESHOOTING_GUIDE.md` for environment issues
4. Ask your instructor before skipping the topic

## Supporting Documents

- `../docs/SETUP_GUIDE.md`
- `../docs/TROUBLESHOOTING_GUIDE.md`
- `DOCS/GLOSSARY.md`
- `DOCS/ALGORITHM_CHEAT_SHEET.md`
- `DOCS/FINAL_REVIEW_GUIDE.md`
- `RL_LEARNING_JOURNEY.md` (how Units 1–5 connect)

Solutions and answer keys are released by your instructor.

## Start Now

Open `unit1-rl-fundamentals/README.md` and begin with
`unit1-rl-fundamentals/examples/01_mdp_example.ipynb`.
