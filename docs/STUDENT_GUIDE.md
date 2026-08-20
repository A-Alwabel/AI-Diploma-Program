# Student Guide

Your guide to working through the AI Diploma program.

**Last Updated:** 2026-08

---

## Program Overview

- **12 courses** (AIAT 111–126), taken in order 01 → 12
- **944 training hours** across **2 official semesters**
- Semester 1: Courses 01–06 (AIAT 111–116)
- Semester 2: Courses 07–12 (AIAT 121–126), ending with the Graduation Project

Start with these documents:

1. [QUICK_REFERENCE_GUIDE.md](QUICK_REFERENCE_GUIDE.md) — courses, hours, and CLOs at a glance
2. [SETUP_GUIDE.md](SETUP_GUIDE.md) — set up your environment
3. [COURSE_NAVIGATION.md](COURSE_NAVIGATION.md) — how the courses connect

---

## The Learning Path

Every course follows the **same numbered path**. Follow it in order — there is
exactly one path per course:

```
START_HERE.md
   → unit1 examples (01_…, 02_…, … in order)
   → unit1 exercise
   → unit1 quiz
   → unit2 … unit5 (same pattern)
   → course assessment (ASSESSMENTS/)
```

For each course:

1. **Open `START_HERE.md`** in the course folder. It gives the setup steps and
   the exact order of everything in the course. Always start there.
2. **Study the examples.** Each unit's `examples/` folder contains numbered
   notebooks (`01_…`, `02_…`, …). Run them in order — later notebooks build on
   earlier ones.
3. **Do the exercise.** Each unit's `exercises/` folder has practice work with
   TODOs for you to complete.
4. **Take the quiz** for the unit before moving on.
5. **Finish with the assessment** in the course's `ASSESSMENTS/` folder.

**Solutions and answer keys are released by your instructor** during the
course — they are not included in this repository. Attempt every exercise and
quiz honestly first; that is where the learning happens.

---

## Course Progression

### Semester 1 (Foundation)

```
Course 01: Introduction to Artificial Intelligence and Applications
Course 02: Python for Artificial Intelligence
Course 03: Mathematics and Probability for Machine Learning
Course 04: Machine Learning Algorithms and Applications
Course 05: Scalable Data Science
Course 06: Artificial Intelligence Ethics
```

### Semester 2 (Advanced)

```
Course 07: Natural Language Processing
Course 08: Deep Learning
Course 09: Reinforcement Learning
Course 10: Generative Artificial Intelligence
Course 11: Deploying AI Models
Course 12: Graduation Project
```

**Do not skip courses.** Each one assumes everything before it — see
[COURSE_NAVIGATION.md](COURSE_NAVIGATION.md) for the exact dependencies.

---

## Environment Setup

Follow [SETUP_GUIDE.md](SETUP_GUIDE.md). In short:

```bash
cd "/path/to/AI Diploma"
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name ai-diploma --display-name "AI Diploma"
```

Notebooks run on the **AI Diploma** kernel, except the TensorFlow notebooks in
Courses 01 and 08, which use the separate **tfenv** kernel (Python 3.13 +
TensorFlow) — see the Setup Guide for how to create it.

**Note:** the `docs/TEMPLATES/` folder is for instructors preparing materials.
As a student, follow the course units and notebooks, not the templates.

---

## Hardware and GPU

- **Any modern computer** (Windows, macOS, or Linux) with 8 GB+ RAM works for
  the whole program.
- **GPU is optional.** Courses 05, 08, and 10 have notebooks that benefit from
  one; each of those courses ships a Google Colab guide
  (`Course XX/DOCS/COLAB_SETUP.md`) so you can use a free cloud GPU instead.
- Details: [GPU_REQUIREMENTS_SUMMARY.md](GPU_REQUIREMENTS_SUMMARY.md)

---

## Tracking Your Progress

Each course has a `STUDENT_PROGRESS_CHECKLIST.md` — use it to mark completed
examples, exercises, quizzes, and the assessment.

Program level:

**Semester 1**

- [ ] Course 01 — Introduction to AI and Applications
- [ ] Course 02 — Python for AI
- [ ] Course 03 — Mathematics and Probability for ML
- [ ] Course 04 — ML Algorithms and Applications
- [ ] Course 05 — Scalable Data Science
- [ ] Course 06 — AI Ethics

**Semester 2**

- [ ] Course 07 — Natural Language Processing
- [ ] Course 08 — Deep Learning
- [ ] Course 09 — Reinforcement Learning
- [ ] Course 10 — Generative AI
- [ ] Course 11 — Deploying AI Models
- [ ] Course 12 — Graduation Project

---

## When You Get Stuck

1. **Environment or install problems** → [TROUBLESHOOTING_GUIDE.md](TROUBLESHOOTING_GUIDE.md)
2. **"I don't understand this notebook"** → check the unit README and the
   course's prerequisites; re-run the earlier numbered examples.
3. **"The exercise is too hard"** → go back to the unit's examples and modify
   them before attempting the exercise again.
4. **Still stuck** → ask your instructor or study group
   (see [COMMUNITY_RESOURCES.md](COMMUNITY_RESOURCES.md)).

---

## Study Tips

1. **Follow the sequence** — courses 01 → 12, units 1 → 5, examples 01 → NN.
2. **Run everything.** Don't just read notebooks — execute them, change
   parameters, break things, and fix them.
3. **Practice daily.** Even one hour a day beats a weekend marathon.
4. **Attempt before asking.** Try each exercise seriously before the instructor
   releases the solution — then compare your approach with it.
5. **Keep notes** and save your modified notebooks; they become your personal
   reference for the graduation project.

---

**For course-specific help, always start with that course's `START_HERE.md`.**
