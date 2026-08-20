# AIAT 111 - Introduction to Artificial Intelligence and Applications

**New students: read `START_HERE.md` first.** It covers setup and the exact order to work through the material.

---

## Course Overview

An introduction to Artificial Intelligence: what AI is, intelligent agents, search algorithms, knowledge representation, probabilistic reasoning, machine learning basics, neural networks, and a first look at generative AI.

**Course code:** AIAT 111
**Credit hours:** 3 · **Contact hours:** 4/week · **Total training hours:** 64 (32 theory + 32 practical)

**Prerequisites:** None. This is the first course of Semester 1 (AIAT 111–116).

---

## Units

| Unit | Folder | Official title | Hours |
|------|--------|----------------|-------|
| 1 | `unit1-ai-foundations/` | Introduction to AI and Applications | 12 (6 theory + 6 practical) |
| 2 | `unit2-ai-concepts/` | AI Concepts, Terminology, and Application Domains | 12 (6 theory + 6 practical) |
| 3 | `unit3-ml-basics/` | AI Concepts, Terminology, and Application Domains Part 2 | 12 (6 theory + 6 practical) |
| 4 | `unit4-neural-networks-basics/` | Neural Networks Fundamentals | 14 (7 theory + 7 practical) |
| 5 | `unit5-generative-ai-intro/` | Introduction to Generative AI and Course Summary | 14 (7 theory + 7 practical) |

---

## Learning Path

One numbered path through the course:

1. `START_HERE.md` — setup and orientation
2. Unit 1 → Unit 5, in order. Within each unit: read the unit `README.md`, run the notebooks in `examples/` in file order, complete the exercise in `exercises/`, then take the quiz in `quizzes/`
3. `ASSESSMENTS/` — final exam

Track yourself with `STUDENT_PROGRESS_CHECKLIST.md`.

---

## Folder Guide

```
Course 01/
├── README.md                       This file
├── START_HERE.md                   Setup and learning sequence
├── STUDENT_PROGRESS_CHECKLIST.md   Progress tracker
├── unit1-ai-foundations/           Unit 1 (examples, exercises, quizzes)
├── unit2-ai-concepts/              Unit 2 (examples, exercises, quizzes)
├── unit3-ml-basics/                Unit 3 (examples, exercises, quizzes)
├── unit4-neural-networks-basics/   Unit 4 (examples, exercises, quizzes)
├── unit5-generative-ai-intro/      Unit 5 (examples, exercises, quizzes)
├── QUIZZES/                        Index of the five unit quizzes
├── ASSESSMENTS/                    Final exam
├── PROJECTS/                       Two practical projects
├── CASE_STUDIES/                   AI system design case study
└── PRESENTATIONS/                  Lecture slides (PDF)
```

---

## Setup

Use the shared environment at the repository root: create `.venv` and register the `ai-diploma` Jupyter kernel as described in `../README.md` and `../docs/SETUP_GUIDE.md`.

TensorFlow notebooks (in Units 3, 4, and 5) run on the separate `tfenv` kernel; all other notebooks use `ai-diploma`.

---

## Assessment

- **Quizzes:** one per unit, five total, in each unit's `quizzes/` folder (see `QUIZZES/README.md`)
- **Projects:** two practical projects in `PROJECTS/`
- **Case study:** `CASE_STUDIES/01_ai_system_design_case_study.md`
- **Final exam:** `ASSESSMENTS/Final_Exam.md`

Answer keys and exercise solutions are released by your instructor.

---

## Next Course

After AIAT 111, continue with the next Semester 1 course, AIAT 112.
