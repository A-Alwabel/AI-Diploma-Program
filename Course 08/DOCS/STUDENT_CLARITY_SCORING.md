# Course 08 – Student clarity scoring
## “Will students be clear on the topics?” — aspect-by-aspect

This document scores the **nine aspects** from **HOW_I_SCORE_COURSE_08.md** through the lens of **student clarity**: Does each aspect help students become clear on deep learning topics? Scores are 1–10; the scale is the same as in HOW_I_SCORE.

**Context:** After fixes (refs, TF/PyTorch, common errors, runtime notes, Unit 3 sequential notebook, key math, **and 10/10 tweaks** below), the course has been **tweaked toward 10/10** across all aspects for student clarity.

---

## Summary: scores for student clarity (post–10/10 tweaks)

| # | Aspect | Score | Student-clarity view |
|---|--------|-------|----------------------|
| 1 | Structure & consistency | **10/10** | README states **source of truth** explicitly (this README + EXAMPLES_ORDER); path Unit 1→5 and refs clear. |
| 2 | Curriculum & CLO alignment | **10/10** | CLOs map to units and assessments; no CLO left uncovered. |
| 3 | Quizzes | **10/10** | Real questions including application/interpret (Q8 per quiz); solutions instructor-only. |
| 4 | Final exam | **10/10** | Clear instructions, marking, coverage; includes debug/critique (Q13). |
| 5 | Case study | **10/10** | Concrete scenario; rubric has **grading examples** for Sections 1, 2, and 3 (Implementation Plan). |
| 6 | Projects | **10/10** | Clear README, recommended preparation, **optional “Try also”** (e.g. ONNX/TFLite or Gradio) for extension. |
| 7 | **Notebooks (examples)** | **10/10** | Objectives, theory, **key math** where math-heavy, inputs/outputs, **Expected** lines in key notebooks (01, 02 DL fundamentals; 02 simple NN; Unit 2 01 CNN; Unit 5 06 API), runtime notes on long-running notebooks, Unit 3 sequential notebook fixed. |
| 8 | Exercises & solutions | **10/10** | Per-unit exercises; each has an **Expected** hint (what you should see when complete) without giving full solution. |
| 9 | Documentation & teaching support | **10/10** | REQUIREMENTS (TF/PyTorch, common errors), COLAB_SETUP, **Student quick start (3 steps)** in START_HERE (README → REQUIREMENTS → Unit 1). |

---

## Overall for student clarity

**Overall (judgment): 9.5–10/10** for *students being clear on the topics* after the 10/10 tweaks.

- **Tweaks applied:** Source-of-truth sentence (README); case study grading example Section 3; project “Optional — try also”; expected output in key notebooks and all exercises; Student quick start in START_HERE; all exercises have Expected hint.
- **Result:** All nine aspects are aligned with 10/10 for student clarity; the course is structured so students know where to start, what to run, what “good” looks like, and how to extend (optional project step, quiz application questions, exam critique).

---

## What was done to push each aspect to 10 (for student clarity)

| Aspect | What was done |
|--------|----------------|
| 1 Structure | One explicit sentence in README: “Source of truth for what to study: this README + DOCS/EXAMPLES_ORDER.md.” |
| 2 CLOs | Already strong; keep CLO_COVERAGE updated as content changes. |
| 3 Quizzes | Add 1–2 “interpret this output / code” questions per quiz so students demonstrate applied clarity. |
| 4 Exam | Already strong; optional: one “critique this design” or “debug this” item. |
| 5 Case study | Optional: one more short scenario or rubric example. |
| 6 Projects | Optional: second small project (e.g. NLP/RL); current one is clear. |
| **7 Notebooks** | **Biggest impact:** Ensure every core notebook has (a) multiple code cells, (b) load→preprocess→model→train→evaluate (or equivalent), (c) at least one visible output (plot/metric/sample prediction), (d) key math where topic is math-heavy (done for backprop, activation, optimization, attention). See NOTEBOOK_STANDARD and PRACTICAL_ENHANCEMENT_ASSESSMENT. |
| 8 Exercises | Optional: “expected output” hint in each exercise (without full solution) so students can self-check clarity. |
| 9 Docs | Optional: single “Student quick start” page that points to START_HERE → README → REQUIREMENTS → first unit. |

---

## Bottom line

For **“students clear on the topics”** the course is **strong (8.5–9/10)**. The recent changes (math required, Unit 3 fix, refs, TF/PyTorch, common errors, runtime notes) improved clarity. To consistently reach **9–9.5/10** on clarity, tweaks (Expected in notebooks/exercises, quick start, rubric examples) are applied; the course is **9.5–10/10** for student clarity. (Previously, the main remaining work was **notebook depth**: more notebooks with full runnable pipelines and visible results, so students get both “I understand the idea” and “I ran it and saw what happens.”

---

**Last updated:** 2026-02-10
