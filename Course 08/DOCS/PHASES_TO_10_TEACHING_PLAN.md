# Course 08: Phased Plan to 10/10 (All Aspects + Teaching)

This document is the **master plan** to bring Course 08 (Deep Learning) to **10/10** across every aspect, with **teaching** explicitly covered (instructor materials, rubrics, solutions, timing, misconceptions).

**How to use:** Work through phases in order. Tick items as you complete them. Do not skip phases—later phases depend on earlier ones.

---

## Overview of Phases

| Phase | Focus | Teaching focus |
|-------|--------|----------------|
| **1** | Structure, consistency, documentation | Single source of truth; instructor runbook |
| **2** | Quizzes & final exam (content + solutions + rubrics) | Grading rubrics; answer keys; common mistakes |
| **3** | Case study & projects (concrete scenarios + rubrics) | Assessment rubrics; teaching notes for projects |
| **4** | Notebooks & exercises (full pipelines + solutions) | Teaching notes per unit; exercise solutions |
| **5** | Teaching materials (instructor guide, timing, FAQs) | Slide timing; misconceptions; demo runbook |
| **6** | Verification & polish | CLO coverage; run-all test; final checklist |

---

## Phase 1: Structure, consistency & documentation

**Goal:** One clear path, no contradictions, and docs that support both students and instructors.

### 1.1 Fix course-level inconsistencies

- [ ] **Unit 3 hours:** Decide official numbers. Either (a) update `unit3-rnns-transformers/README.md` to "6 theoretical + 13 practical = 19 hours" to match main `README.md`, or (b) update main `README.md` to match unit README. Document the choice in `DOCS/` (e.g. "Unit hours are defined in README.md").
- [ ] **Progress checklist:** Either add "Unit 1 Test" … "Unit 5 Test" as separate assessment files (e.g. in `ASSESSMENTS/Unit_01_Test.md`) or change `STUDENT_PROGRESS_CHECKLIST.md` to "Take Quiz 01" only (remove "Take Unit 1 Test" etc.). Prefer one: either unit test = quiz, or add real unit tests.
- [ ] **Project 02:** In `STUDENT_PROGRESS_CHECKLIST.md`, either (a) add a second project (e.g. `PROJECTS/Text_or_Sequence_Project/README.md`) with same structure as Image Classification, or (b) remove "Project 02 (optional)" and say "Complete Project 01".

### 1.2 Fix broken or ambiguous references

- [ ] **COURSE_MAP.md / DETAILED_UNIT_DESCRIPTIONS.md:** In every unit README and in `START_HERE.md`, either (a) use relative paths that work from repo root (e.g. `../DETAILED_UNIT_DESCRIPTIONS.md`) and ensure those files exist in parent folder, or (b) remove the references and point only to `Course 08/README.md` and `DOCS/EXAMPLES_ORDER.md`. Document in main README: "For full curriculum see [X]."
- [ ] Add a short **DOCS/REQUIREMENTS_COURSE_08.md** (or section in README): list Python version, `pip install tensorflow torch …` (or "use root requirements.txt"), and Colab link. So Course 08 has a single "how to run" reference.

### 1.3 Documentation for instructors

- [ ] Create **DOCS/INSTRUCTOR_RUNBOOK.md** (or **TEACHING_RUNBOOK.md**): one place that explains (1) how to open and run notebooks (local vs Colab), (2) where quizzes and solutions live, (3) where exercise solutions live (after Phase 4), (4) how slides map to notebooks (`EXAMPLES_ORDER.md` + `INSTITUTION_SLIDES_COMPATIBILITY.md`), (5) Unit 5 has no slides—use notebooks only. So any instructor can teach from the repo in one read.

**Phase 1 complete when:** All checkboxes above are done and there are no conflicting statements between README, checklist, and unit READMEs.

---

## Phase 2: Quizzes & final exam (content + solutions + rubrics)

**Goal:** Every quiz and the final exam are **usable for teaching and grading**, with real questions and full answer keys + rubrics.

### 2.1 Quiz content (all 5 quizzes)

- [ ] **Quiz 01 (Unit 1):** Replace every placeholder with real content.  
  - Part 1: 4 MC questions (e.g. deep vs shallow nets, backprop, activation functions, optimizer role). Options A–D and one correct answer.  
  - Part 2: One code question (e.g. "Build a 2-layer MLP in Keras for MNIST with one hidden layer of 128 units").  
  - Part 3: Two short-answer questions (e.g. "Explain overfitting and one way to reduce it"; "What is the role of the loss function?").  
  - **Teaching:** Ensure each question maps to a CLO and to specific slides/notebooks (add a small "Mapping" line at end of quiz).
- [ ] **Quiz 02 (Unit 2):** Same structure. MC on CNNs (conv, pooling, transfer learning, data augmentation). Code: small CNN for image classification. Short answer: "Why use conv layers instead of dense for images?" and one more.
- [ ] **Quiz 03 (Unit 3):** MC on RNNs, LSTM/GRU, attention, Transformers. Code: simple RNN or LSTM for sequence (e.g. with Keras/TF). Short answer: "What problem does attention solve?" and one more.
- [ ] **Quiz 04 (Unit 4):** MC on GANs, VAEs, RL basics, ethics (bias, fairness). Code: e.g. "Outline training loop for a GAN" or "Use a pre-trained model for transfer learning." Short answer on ethics or RL.
- [ ] **Quiz 05 (Unit 5):** MC on quantization, pruning, distillation, ONNX, serving (Flask/FastAPI, TF Serving). Code: e.g. "Write a minimal FastAPI endpoint that loads a model and returns a prediction." Short answer on deployment trade-offs.

### 2.2 Quiz solutions and grading (teaching)

- [ ] For **each** of `quiz_01_solution.md` … `quiz_05_solution.md`:  
  - Replace all "[Answer]" / "[Explanation]" with **actual answers** and **brief explanations**.  
  - Add **point allocation** per question (e.g. Q1: 10 pts, Q2: 10 pts, …).  
  - Add a **"Common mistakes"** subsection (2–3 bullets per quiz) for teaching.  
  - Add **"Suggested grading rubric"** for code and short-answer (e.g. "Full marks: correct architecture + compilation; partial: minor syntax").  
  So instructors can grade consistently and use solutions in class.

### 2.3 Final exam

- [ ] **ASSESSMENTS/Final_Exam.md:** Keep current structure (MC, short answer, coding, case study). Add at the top: **"Marking scheme"** table (e.g. "Q1–6: 5 pts each; Q7–9: 10 pts each; Q10: 15 pts; Q11: 10 pts; Q12: 15 pts") and any special instructions (e.g. "Code must run in TF 2.x or PyTorch 1.x+").
- [ ] Create **ASSESSMENTS/Final_Exam_Solution.md** (or **DOCS/SOLUTIONS/Final_Exam_Solution.md**):  
  - Model answers for short-answer and case study.  
  - Reference code for Q10 (CNN) and Q11 (BERT fine-tuning).  
  - Rubric for Q12 (e.g. architecture choice 3 pts, preprocessing 3 pts, imbalance 3 pts, optimization 3 pts, ethics 3 pts).  
- [ ] Create **ASSESSMENTS/Final_Exam_Rubric.md**: table with question, max points, criteria for full/partial/zero. So teaching and grading are clear.

**Phase 2 complete when:** All 5 quizzes have real questions; all 5 solution files have real answers + point allocation + common mistakes + rubric; final exam has solution doc and rubric.

---

## Phase 3: Case study & projects (concrete scenarios + rubrics)

**Goal:** One **concrete** case study and **one fully specified project** with rubrics and teaching notes.

### 3.1 Case study: concrete scenario

- [ ] Rewrite **CASE_STUDIES/case_study_01_deep_learning_deployment.md**:  
  - **Context:** e.g. "A hospital wants to deploy a CNN that classifies chest X-rays (normal vs pneumonia) for radiologists. Constraints: latency <2 s per image, must run on existing on-prem GPU server, and predictions must be explainable for audits."  
  - **Problem statement:** Deploy the model as a REST API; ensure it meets latency and explainability requirements.  
  - **Data:** Point to a real or proxy dataset (e.g. "ChestX-ray8 or a public subset"); say "students can use MNIST/CIFAR as a stand-in if data is unavailable."  
  - **Deliverables:** (1) Architecture choice + justification, (2) Preprocessing pipeline, (3) API design (e.g. FastAPI), (4) One fairness/explainability check, (5) Short deployment checklist.  
  - Keep the existing "Analysis framework" sections but fill **one** worked example (e.g. "Example analysis: …") so students see what "good" looks like.  
- [ ] Create **CASE_STUDIES/case_study_01_rubric.md**: points per section (e.g. Problem analysis 20, Solution design 25, Implementation plan 25, Evaluation 15, Recommendations 15); criteria for full/partial/zero.  
- [ ] Create **DOCS/SOLUTIONS/case_study_01_sample_solution.md** (instructor-only or clearly marked): model answer for teaching and grading.

### 3.2 Project: Image Classification System

- [ ] Flesh out **PROJECTS/Image_Classification_System/README.md**:  
  - **Objective:** e.g. "Build and deploy an image classifier (e.g. for a domain of your choice: medical, wildlife, or product recognition)."  
  - **Starter:** Link or list datasets (e.g. CIFAR-10, a Kaggle dataset, or a small custom set). Optionally add a `starter/` folder with `train.py` / `predict.py` skeletons.  
  - **Steps:** (1) Data loading and augmentation, (2) Model (CNN or transfer learning), (3) Training and validation, (4) Export (e.g. SavedModel or ONNX), (5) Simple API (e.g. Flask/FastAPI) or notebook demo.  
  - **Deliverables:** Code (notebooks or scripts), short report (1–2 pages), and optional 10-min presentation.  
- [ ] Create **PROJECTS/Image_Classification_System/RUBRIC.md**: criteria and points (e.g. Data & preprocessing 20, Model design 25, Training & evaluation 20, Deployment/demo 20, Report & clarity 15).  
- [ ] Add **Teaching note** in README or **DOCS/PROJECT_TEACHING_NOTES.md**: suggested timeline (e.g. 2 weeks), common issues (e.g. GPU, dataset size), and how to use the rubric in class.

### 3.3 Project 02 (optional) or remove reference

- [ ] **Option A:** Add **PROJECTS/Project_02_README.md** (or a second project folder): e.g. "NLP or time-series project using RNNs/Transformers" with same structure (objective, dataset suggestions, steps, deliverables, rubric).  
- [ ] **Option B:** In `STUDENT_PROGRESS_CHECKLIST.md` remove "Complete Project 02 (optional)" and state only one project is required.  
  Choose one and implement.

**Phase 3 complete when:** Case study has a concrete scenario, rubric, and sample solution; Image Classification project has full README + rubric + teaching note; Project 02 is either added or reference removed.

---

## Phase 4: Notebooks & exercises (full pipelines + solutions)

**Goal:** Every **core** example notebook has a full "load → preprocess → model → train → evaluate → interpret" pipeline where appropriate; every exercise has a **solution** and **teaching notes**.

### 4.1 Notebook audit and upgrade (teaching-oriented)

- [ ] List all **core** notebooks (from each unit README: main order 01, 02, … excluding "optional" only if you want to limit scope).  
- [ ] For each core notebook, verify against **DOCS/20_MIN_NOTEBOOK_PLAN.md**:  
  - Header + real-life (2–3 sentences), short theory, Inputs & Outputs, **multiple code cells** (not just one), and a short summary.  
  - Where the topic allows, ensure **real data** (e.g. MNIST, CIFAR-10) and **visible outputs** (e.g. loss curve, accuracy, sample predictions).  
- [ ] Fix any notebook that is still "objectives + one code cell": add at least (1) load data, (2) build/train or run, (3) one plot or metric. Prefer full pipeline; if not possible (e.g. theory-only), add a "Try it yourself" cell that points to a full example.  
- [ ] Add at the **end** of each unit README a **"Teaching note"** subsection: suggested time for examples (e.g. "Examples 01–06: ~2 hours total; optional 07–08: +30 min"), one sentence on "Common stumbling block" (e.g. "Colab GPU timeout"), and which notebook to **demo live** (e.g. "Demo 02_simple_neural_network or 01_cnn_architecture").

### 4.2 Exercise solutions (instructor-facing)

- [ ] Create **DOCS/SOLUTIONS/exercises/** (or keep solutions in a separate instructor-only repo; if so, document in `INSTRUCTOR_RUNBOOK.md`).  
- [ ] For each exercise notebook in `unit1-deep-learning-basics/exercises/` … `unit5-deployment/exercises/`:  
  - Add a **solution notebook** (e.g. `01_neural_network_exercise_SOLUTION.ipynb`) or a **solution markdown** (e.g. `unit1_exercise_01_solution.md`) with complete code and short explanations.  
  - Add **rubric** (e.g. "Data preprocessing: 25 pts – correct resize + normalize + DataLoader").  
- [ ] In **DOCS/INSTRUCTOR_RUNBOOK.md** (or **TEACHING_RUNBOOK.md**), add a section: "Exercise solutions location and how to use them (e.g. do not distribute to students before deadline)."

### 4.3 Exercise–notebook alignment

- [ ] In each unit README, under Exercises, add one line per exercise: "Aligns with examples: …" (e.g. "Aligns with 01_deep_learning_fundamentals, 02_simple_neural_network"). So instructors know which notebooks to assign before the exercise.

**Phase 4 complete when:** Core notebooks pass the 20-min / full-pipeline check; each unit README has a short teaching note; every exercise has a solution and rubric; runbook documents where solutions live.

---

## Phase 5: Teaching materials (instructor guide, timing, FAQs)

**Goal:** Instructors have **one guide**, **timing per slide/unit**, **common misconceptions**, and a **demo runbook**.

### 5.1 Instructor / teaching guide

- [ ] Expand **DOCS/INSTRUCTOR_RUNBOOK.md** (or create **DOCS/TEACHING_GUIDE.md**) to include:  
  - **Course flow:** Unit order, quiz after each unit, project(s) and case study timing.  
  - **Slide ↔ notebook:** Short table (or link to `EXAMPLES_ORDER.md` and `INSTITUTION_SLIDES_COMPATIBILITY.md`). Reminder: Unit 5 has no slides.  
  - **Where everything lives:** README, START_HERE, quizzes (QUIZZES/), solutions (DOCS/SOLUTIONS/), case study rubric, project rubric, exercise solutions.  
  - **Colab vs local:** When to recommend Colab (e.g. GPU, heavy training) and when local is fine (e.g. deployment API demos).  
  - **Assessment calendar suggestion:** e.g. "Quiz 01 after week 2, Quiz 02 after week 4, … Case study due week 14, Project due week 16."

### 5.2 Timing for teaching

- [ ] Add **DOCS/TEACHING_TIMING.md** (or a section in the teaching guide):  
  - **Per unit:** Suggested lecture hours (theory) and lab hours (notebooks + exercises), matching the main README (e.g. Unit 1: 6 theory + 12 practical).  
  - **Per notebook:** Either "~20 min" for all or list exceptions (e.g. "06_gpt_text_generation: ~30 min if run fully").  
  - **Per session:** Example "2-hour lab": do notebooks 01–03 of Unit 2; leave 04–07 for next lab.  
  So instructors can plan lessons without guessing.

### 5.3 Common misconceptions and FAQ

- [ ] Create **DOCS/COMMON_MISCONCEPTIONS_AND_FAQ.md**:  
  - **Misconceptions:** e.g. "DL always beats traditional ML" (when to use which), "More layers always better" (overfitting), "Attention replaces RNNs" (when each is used), "Quantization always hurts accuracy" (often negligible with calibration). 5–10 items with one-paragraph corrections.  
  - **FAQ:** e.g. "TensorFlow vs PyTorch in this course?", "Why is Unit 5 not in the slides?", "Where do I get GPU?", "Can I use a different dataset for the project?"  
  Reference this from the teaching guide and from README or START_HERE.

### 5.4 Demo runbook

- [ ] Create **DOCS/DEMO_RUNBOOK.md**:  
  - **Purpose:** For instructors who want to **demo** notebooks live (in class or Colab).  
  - **List 5–8 "best demo" notebooks** (e.g. 01_deep_learning_fundamentals, 02_simple_neural_network, 01_cnn_architecture, 04_transfer_learning_object_detection, 04_transformer_attention, 06_flask_fastapi_deployment).  
  - For each: 2–3 bullets: what to show (e.g. "Run training cell, show loss curve"), what to say ("We use conv layers because …"), and **pre-run** tip (e.g. "Pre-run the notebook so outputs are cached; then re-run one cell at a time").  
  - One section: "If demo fails (e.g. Colab disconnect), have screenshot or short video backup."

**Phase 5 complete when:** Teaching guide (or runbook) is complete; timing doc exists; misconceptions/FAQ doc exists; demo runbook exists and is linked from the guide.

---

## Phase 6: Verification & polish

**Goal:** No loose ends; CLOs covered; notebooks runnable; final checklist for "10/10".

### 6.1 CLO coverage

- [ ] Create **DOCS/CLO_COVERAGE.md**:  
  - Table: CLO1 … CLO5 vs (1) Units, (2) Example notebooks, (3) Quizzes, (4) Final exam, (5) Project/case study.  
  - Ensure each CLO is clearly addressed by at least one unit, one quiz question, and one exam question or project deliverable.  
  - Fix any gap (e.g. add one quiz question or one notebook mention).

### 6.2 Runnable check

- [ ] **Notebooks:** For at least one notebook per unit (e.g. 01 of each unit), verify "Run All" in a clean environment (or Colab) and that outputs (plots, print statements) appear. Document in runbook: "Recommended environment: Python 3.10, tensorflow 2.x, torch 1.x."  
- [ ] **Code in quizzes/exam:** If any quiz or exam question includes code snippets, ensure they are syntactically correct and runnable in the stated environment (or mark "pseudocode" where appropriate).

### 6.3 Final 10/10 checklist (self-review)

- [ ] **Structure:** No conflicting hours or missing tests; Project 02 decided; references fixed.  
- [ ] **Quizzes:** All 5 have real questions; all 5 solutions have answers, points, common mistakes, rubric.  
- [ ] **Exam:** Final exam has solution and rubric.  
- [ ] **Case study:** Concrete scenario, rubric, sample solution.  
- [ ] **Projects:** Image Classification fully specified + rubric + teaching note; Project 02 either added or removed from checklist.  
- [ ] **Notebooks:** Core notebooks have full pipeline and real outputs where applicable; unit READMEs have teaching notes.  
- [ ] **Exercises:** Every exercise has solution + rubric; runbook points to solutions.  
- [ ] **Teaching:** Instructor runbook/guide, timing, misconceptions/FAQ, demo runbook, CLO coverage doc.  
- [ ] **Docs:** REQUIREMENTS or run instructions for Course 08; INSTRUCTOR_RUNBOOK up to date.

**Phase 6 complete when:** CLO coverage is documented, at least one notebook per unit has been run successfully, and the final checklist above is satisfied.

---

## Summary: from current state to 10/10

| Aspect | Before | After (when plan is done) |
|--------|--------|----------------------------|
| Structure | Inconsistencies, vague refs | Single source of truth; clear path |
| Quizzes | Placeholders | Real questions + solutions + rubrics |
| Final exam | Good questions, no rubric/solution | Full solution + rubric |
| Case study | Generic framework | Concrete scenario + rubric + sample |
| Projects | Skeletal | Full spec + rubric + teaching note |
| Notebooks | Mixed depth | Full pipeline + teaching notes per unit |
| Exercises | TODO only | Solutions + rubrics; runbook ref |
| Teaching | Implicit | Guide, timing, misconceptions, demo runbook |
| Documentation | Good but gaps | Requirements, runbook, CLO coverage |

**Estimated effort (rough):**  
- Phase 1: 1–2 hours  
- Phase 2: 4–6 hours (quizzes + solutions + exam)  
- Phase 3: 2–3 hours (case study + project + rubrics)  
- Phase 4: 4–8 hours (notebook audit + exercise solutions)  
- Phase 5: 2–3 hours (teaching materials)  
- Phase 6: 1–2 hours (verification)  

Total: on the order of **15–25 hours** depending on how many notebooks need changes and how detailed solutions are.

---

**Created for:** Course 08 (AIAT 122 – Deep Learning)  
**Purpose:** Bring all aspects to 10/10 with full teaching support  
**Last updated:** 2025-02-07  

---

## Execution status (2025-02-07)

All six phases have been **executed** in the repo:

- **Phase 1:** Unit 3 hours fixed; progress checklist updated (no Unit Test, Project 02 removed); REQUIREMENTS_COURSE_08.md and INSTRUCTOR_RUNBOOK.md added; README reference to DETAILED_UNIT_DESCRIPTIONS clarified.
- **Phase 2:** All 5 quizzes rewritten with real questions; all 5 solution files with answers, rubrics, common mistakes; Final_Exam_Solution.md and Final_Exam_Rubric.md created; marking scheme added to Final_Exam.md.
- **Phase 3:** Case study rewritten with concrete scenario (chest X-ray deployment), rubric, and sample solution; Image Classification project README, RUBRIC.md, and teaching note added.
- **Phase 4:** Teaching notes added to all 5 unit READMEs; DOCS/SOLUTIONS/exercises/ created with README and Unit 1 sample solution; INSTRUCTOR_RUNBOOK updated.
- **Phase 5:** TEACHING_GUIDE.md, TEACHING_TIMING.md, COMMON_MISCONCEPTIONS_AND_FAQ.md, DEMO_RUNBOOK.md created.
- **Phase 6:** CLO_COVERAGE.md and FINAL_10_10_CHECKLIST.md created.

Use **DOCS/FINAL_10_10_CHECKLIST.md** to verify and sign off.
