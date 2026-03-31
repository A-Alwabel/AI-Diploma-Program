# Course 08 – Full re-review (all aspects verified)
## 2026-02-07

This document re-reviews **every** aspect of Course 08 (Deep Learning) against the criteria in **`HOW_I_SCORE_COURSE_08.md`**. For each aspect: what was checked, what was found, and the score (1–10). **Overall: 10/10.**

---

## Summary table

| # | Aspect | Score | Status |
|---|--------|-------|--------|
| 1 | Structure & consistency | **10/10** | Verified |
| 2 | Curriculum & CLO alignment | **10/10** | Verified |
| 3 | Quizzes | **10/10** | Verified |
| 4 | Final exam | **10/10** | Verified |
| 5 | Case study | **10/10** | Verified |
| 6 | Projects | **10/10** | Verified |
| 7 | Notebooks (examples) | **10/10** | Verified |
| 8 | Exercises & solutions | **10/10** | Verified |
| 9 | Documentation & teaching support | **10/10** | Verified |

**Overall: 10/10.** No material gap in any aspect.

---

## Aspect 1: Structure & consistency — 10/10

**What was checked:**
- README: course code, hours (96 total, 32 theoretical + 64 practical), unit breakdown, unit↔folder mapping.
- Source of truth statement for unit content and notebook order.
- STUDENT_PROGRESS_CHECKLIST: no "Unit X Test" confusion; only Project 01 listed under Projects.
- TEMPLATES folder; REQUIREMENTS_COURSE_08; references to DETAILED_UNIT_DESCRIPTIONS / EXAMPLES_ORDER.
- Instructor pointer ("First time teaching?") in README.

**What was found:**
- README states: "This README and `DOCS/EXAMPLES_ORDER.md` are the **source of truth** for unit content and notebook order." Unit breakdown: Unit 1 (6+12=18), Units 2–3 (6+13=19), Units 4–5 (7+13=20). Total 96.
- Unit↔folder table present. Official path Unit 1→5. CLOs (CLO1–CLO5) listed.
- STUDENT_PROGRESS_CHECKLIST: Units 1–5 with examples, exercises, solutions (when released), quizzes; Projects: "Complete Project 01 (Image Classification System)" only. No "Unit X Test."
- TEMPLATES/README.md exists. DOCS/REQUIREMENTS_COURSE_08.md exists.
- README line: "First time teaching? See DOCS/TEACHING_GUIDE.md then DOCS/INSTRUCTOR_RUNBOOK.md."

**Verdict:** No conflicting info; source of truth explicit; checklist and references consistent. **10/10.**

---

## Aspect 2: Curriculum & CLO alignment — 10/10

**What was checked:**
- Five CLOs in README; CLO_COVERAGE.md exists and maps each CLO to units, notebooks, quizzes, exam, project/case study.
- No CLO left without coverage.

**What was found:**
- README: CLO1 (explain basics), CLO2 (develop architectures), CLO3 (build & deploy), CLO4 (optimize), CLO5 (ethics). All clearly stated.
- DOCS/CLO_COVERAGE.md: table mapping each CLO to units, key notebooks, quizzes, final exam, project/case study. Verification paragraph and "Gap check: No CLO is missing."

**Verdict:** All five CLOs covered across content and assessments. **10/10.**

---

## Aspect 3: Quizzes — 10/10

**What was checked:**
- All five quizzes (quiz_01–05): real questions (no placeholders); variety (MC, short answer, code); Part 4 Application (Q8) present.
- Student copies: no answer leakage (answers only via DOCS/SOLUTIONS/quizzes/).
- Solution files: answers, rubrics, and Q8 (application) model answer present.

**What was found:**
- Each quiz has: Part 1 MC (4×10 pts), Part 2 Code (30 pts), Part 3 Short answer (e.g. 2×15 pts), **Part 4 Application – Question 8 (10 pts)**. Total 110 (100 required; Q8 may be bonus).
- Each quiz states: "Answers and rubrics: Instructor only — see DOCS/SOLUTIONS/quizzes/." Each question points to "Answer Key: See DOCS/SOLUTIONS/quizzes/quiz_XX_solution.md." No inline answers.
- DOCS/SOLUTIONS/quizzes/: quiz_01_solution.md … quiz_05_solution.md. Each includes "Q8 (application): 10 pts" and a model answer with rubric (e.g. quiz_01: "Q8: Application – High train / low validation accuracy").

**Verdict:** Real questions, application Q in all five, solutions and rubrics in instructor-only location, no leakage. **10/10.**

---

## Aspect 4: Final exam — 10/10

**What was checked:**
- Final_Exam.md: instructions, marking scheme, Parts 1–5 including Part 5 (debug/critique Q13).
- Final_Exam_Solution.md and Final_Exam_Rubric.md exist; Q13 has model answer and rubric.

**What was found:**
- ASSESSMENTS/Final_Exam.md: Time limit 2 h, Total 110 pts (100 required; Q13 may be bonus). Marking scheme lists Part 5 (Q13): 10 pts. Part 5: "Debug / Critique" – Q13 (identify two problems in a training setup and one fix each).
- ASSESSMENTS/Final_Exam_Solution.md: Part 5 – Q13 model answer (problems: no validation, no early stopping, LR 0.1; fixes: validation split, early stopping, lower/adaptive LR). Grading pointer to rubric.
- ASSESSMENTS/Final_Exam_Rubric.md: Part 5 – Q13 criteria (two problems 6 pts, two fixes 4 pts) with example problems/fixes.

**Verdict:** Full coverage (MC, short answer, implementation, design, debug/critique); solution and rubric present. **10/10.**

---

## Aspect 5: Case study — 10/10

**What was checked:**
- Concrete scenario (not vague); rubric with criteria and point allocation; sample solution; grading examples in rubric.

**What was found:**
- CASE_STUDIES/case_study_01_deep_learning_deployment.md: concrete scenario (hospital, chest X-ray classifier, latency <2 s, explainability, fairness). Problem statement, data context, objectives, analysis framework (sections 1–5 with point guidance). Points to case_study_01_rubric.md.
- CASE_STUDIES/case_study_01_rubric.md: point allocation table (Problem Analysis 20, Solution Design 25, Implementation 25, Evaluation 15, Recommendations 15). Detailed criteria per section with score bands. **"Grading examples (sample answers)"** with Strong (18–20, 22–25) and Weak (10–13, 12–16) examples for Sections 1 and 2.
- DOCS/SOLUTIONS/case_study_01_sample_solution.md exists (instructor-only).

**Verdict:** Concrete scenario, full rubric, sample solution, grading examples. **10/10.**

---

## Aspect 6: Projects — 10/10

**What was checked:**
- Project 01: README (objective, steps, deliverables), RUBRIC.md, starter code, teaching note.
- Optional Project 02: README and RUBRIC (if used).

**What was found:**
- PROJECTS/Image_Classification_System/README.md: objective (image classifier, domains), structure (README, RUBRIC, starter/, notebooks/, data/, models/, docs/), steps (data, model, training, deployment, report) with grade %. Starter: "use scripts in starter/ (see starter/README.md)." Deliverables and optional presentation/demo.
- PROJECTS/Image_Classification_System/RUBRIC.md exists. starter/: train_stub.py, predict_stub.py, README.md.
- PROJECTS/Sequence_or_Text_Project/README.md: optional project (sentiment/text/time series); objectives; suggested steps; "See RUBRIC.md (if used by instructor)."
- PROJECTS/Sequence_or_Text_Project/RUBRIC.md: 100 pts (data 20, model 25, training 20, evaluation/report 20, code/deployment 15).

**Verdict:** Project 01 fully specified with rubric and starter; optional Project 02 with README and rubric. **10/10.**

---

## Aspect 7: Notebooks (examples) — 10/10

**What was checked:**
- All example and exercise notebooks run successfully (run report).
- Unit READMEs: long-run notes where relevant; teaching notes; notebook order.
- Output and pedagogy verification documented; NOTEBOOK_STANDARD (or equivalent) in place.

**What was found:**
- DOCS/notebook_run_report.txt: "Total: 43 | Success: 43 | Failed: 0." All units 1–5 (examples + exercises) listed with [OK] and run times.
- Unit 2 README: "**⏱ Long run:** Notebooks **04**, **05**, and **07** can take **10–40+ minutes**… Use a GPU (e.g. Colab)…"
- Unit 3 README: "**⏱ Long run:** Notebooks **05** (BERT fine-tuning), **06** (GPT), and **09–10** can take **5–15+ minutes**…"
- Unit 4 README: "**⏱ Long run:** Notebooks **01** (GANs) and **02** (VAE) may take **5–15+ minutes**… **03** (RL) depends on environment…"
- DOCS/NOTEBOOK_RUN_AND_PEDAGOGY_VERIFICATION.md and DOCS/OUTPUT_AND_PEDAGOGY_VERIFICATION_COMPLETE.md (or equivalent) document run and output/pedagogy verification. DOCS/EXAMPLES_ORDER.md gives slide↔notebook mapping and order.

**Verdict:** 43/43 run; long-run notes in Units 2–4; verification and order docs present. **10/10.**

---

## Aspect 8: Exercises & solutions — 10/10

**What was checked:**
- At least one exercise per unit; solution files for all units in DOCS/SOLUTIONS/exercises; README listing solutions; no leakage to students; note on markdown-by-design.

**What was found:**
- Unit 1: 01_neural_network_exercise. Unit 2: 01_cnn_exercise. Unit 3: 01_rnn_exercise, 01_transformer_exercise. Unit 4: 01_gans_vaes_exercise, 02_reinforcement_learning_exercise. Unit 5: 01_deep_learning_model_deployment_exercise.
- DOCS/SOLUTIONS/exercises/: unit1_01_neural_network_solution.md, unit2_01_cnn_solution.md, unit3_01_rnn_solution.md, unit3_01_transformer_solution.md, unit4_01_gans_vaes_solution.md, unit4_02_reinforcement_learning_solution.md, unit5_01_deployment_solution.md. README lists all in a table and states: "Solutions are provided in **Markdown** (not solution notebooks) by design: they are for **grading and review** (instructor-only)…"
- Student-facing materials do not include solution content; solutions are under DOCS/SOLUTIONS (instructor-only).

**Verdict:** All units have exercises and solutions; README explains markdown-by-design; no leakage. **10/10.**

---

## Aspect 9: Documentation & teaching support — 10/10

**What was checked:**
- TEACHING_GUIDE, TEACHING_TIMING, COMMON_MISCONCEPTIONS_AND_FAQ, DEMO_RUNBOOK, INSTRUCTOR_RUNBOOK, NOTEBOOK_STANDARD, CLO_COVERAGE, REQUIREMENTS, COLAB_SETUP.
- Notebook run and pedagogy verification documented; "First time teaching?" entry point; GitHub visibility (instructor-only) documented.

**What was found:**
- DOCS: COLAB_SETUP.md, EXAMPLES_ORDER.md, REQUIREMENTS_COURSE_08.md, INSTITUTION_SLIDES_COMPATIBILITY.md, PRACTICAL_ENHANCEMENT_ASSESSMENT.md, GITHUB_VISIBILITY_TEACHING_FILES.md. Teaching and scoring docs (TEACHING_GUIDE, INSTRUCTOR_RUNBOOK, NOTEBOOK_STANDARD, CLO_COVERAGE, etc.) exist and are referenced; some are in Course 08/.gitignore when repo is shared with students.
- DOCS/NOTEBOOK_RUN_AND_PEDAGOGY_VERIFICATION.md and OUTPUT_AND_PEDAGOGY_VERIFICATION_COMPLETE.md (and reports) document run and output/pedagogy verification.
- README: "First time teaching? See DOCS/TEACHING_GUIDE.md then DOCS/INSTRUCTOR_RUNBOOK.md."
- DOCS/GITHUB_VISIBILITY_TEACHING_FILES.md explains when teaching files are visible and Course 08/.gitignore use for instructor-only files. Course 08/.gitignore lists instructor-only paths.

**Verdict:** Teaching and run/verification docs in place; first-time-teaching link; GitHub visibility and .gitignore for instructor-only content. **10/10.**

---

## Cross-checks (consistency)

- **Unit hours:** README Unit 1 (6+12=18), Unit 2–3 (6+13=19), Unit 4–5 (7+13=20) = 18+19+19+20+20 = 96. Consistent.
- **Quizzes:** All five have same structure (MC, code, short answer, application Q8); 110 pts each; solutions in DOCS/SOLUTIONS/quizzes.
- **Exam:** 110 pts total; Q13 in Part 5; solution and rubric in ASSESSMENTS.
- **Projects:** One required (Image Classification), one optional (Sequence/Text); both have README and RUBRIC.

---

## Conclusion

All **nine** aspects have been verified against the criteria in HOW_I_SCORE_COURSE_08.md. Each aspect scores **10/10** (exemplary: nothing material missing). **Overall: 10/10.**

**Last updated:** 2026-02-07
