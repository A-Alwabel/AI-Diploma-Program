# Course 08 – Gaps for students
## What might be missing or unclear from a student’s perspective

This list is for instructors and maintainers: it summarizes **gaps** (missing or unclear things) that can affect students. Items are ordered by impact; suggested fixes are included where applicable.

---

## 1. Broken or missing references (medium impact)

**Gap:** Several places point to files that may **not exist** in the repo:
- **START_HERE.md** says: “See `../DETAILED_UNIT_DESCRIPTIONS.md` and `README.md`.”
- **Unit READMEs** (1–5) say: “Reviewed related topics in `COURSE_MAP.md` if needed” and some say “Maps to (DETAILED_UNIT_DESCRIPTIONS).”

If the repo has no `DETAILED_UNIT_DESCRIPTIONS.md` or `COURSE_MAP.md` at the AI Diploma root, students (and instructors) get broken or confusing links.

**Suggested fix:** In **START_HERE.md**, make the primary path explicit: “See **README.md** (Unit ↔ folder mapping) and **DOCS/EXAMPLES_ORDER.md** (notebook order and topics). If your repo has `../DETAILED_UNIT_DESCRIPTIONS.md`, it aligns with these.” In unit READMEs, either remove the COURSE_MAP prerequisite or change it to “(if available in your repo).”

---

## 2. No self-check for exercises or quizzes (by design; still a gap for some)

**Gap:** Exercise solutions and quiz answers are **instructor-only** (in `DOCS/SOLUTIONS/`). Students cannot check their work until the instructor releases solutions or goes over them in class.

- **Impact:** Self-learners or students studying ahead have no way to verify exercises or quiz answers.
- **Design:** Intentional (avoid copying; encourage attempt before solution).

**Suggested fix:** Keep solutions instructor-only. Optionally: add one “expected output” line per exercise in the **exercise notebook** (e.g. “You should see test accuracy in the range 0.85–0.95”) without giving full solutions. Or state in **STUDENT_PROGRESS_CHECKLIST** or README: “Exercise and quiz answers are released by your instructor after the deadline.”

---

## 3. Slides dependency (low–medium impact)

**Gap:** Many notebooks say “**📌 Covers slide(s):** **XX** — Topic. *Do this notebook after that slide.*” If the student does **not** have access to the institution’s slides (e.g. self-study or different institution), they may wonder what “that slide” is.

- **Mitigation:** Each notebook already has a **Theory (short)** section, so the notebook is **usable without slides**. The “Covers slide(s)” is for alignment when slides exist.
- **Gap:** No single sentence that says “You can follow the notebooks in file order even without slides.”

**Suggested fix:** In **README.md** or **START_HERE.md**, add one line: “If you don’t have the institution slides, follow the **notebook order** in each unit README; the theory in each notebook is enough to proceed.” Unit 5 already states it has no slides.

---

## 4. TensorFlow vs PyTorch: which notebooks need which (low impact)

**Gap:** Course 08 uses **both** TensorFlow/Keras and PyTorch. REQUIREMENTS_COURSE_08 lists both. Students might not know **which notebooks** need which, or might only have one installed.

- **Reality:** Most example notebooks use **TensorFlow/Keras**; some (e.g. Unit 1 `03_perceptron_mlp_tensorflow_pytorch_setup`, Unit 3 BERT/transformers) use or mention PyTorch.
- **Impact:** A student with only TensorFlow might hit an import error in a PyTorch notebook (or the reverse).

**Suggested fix:** In **DOCS/REQUIREMENTS_COURSE_08.md** or README, add one sentence: “Most notebooks use **TensorFlow/Keras**; Unit 3 (e.g. BERT, some transformers) and a few others use **PyTorch**. Install both for full coverage (see REQUIREMENTS_COURSE_08.md).”

---

## 5. Bridge from units to Project 01 (low impact)

**Gap:** Project 01 (Image Classification) is open-ended. Students might not know **which notebooks** are the best preparation (e.g. transfer learning, deployment).

- **Mitigation:** Project README has clear steps; starter code exists; unit READMEs and rubric spell out expectations.
- **Gap:** No explicit “Before starting the project, we recommend completing at least: Unit 2 examples 01, 05, 07; Unit 5 example 06 (API).”

**Suggested fix:** In **PROJECTS/Image_Classification_System/README.md**, add a short “**Recommended preparation**” line: “Complete Unit 2 (CNNs, transfer learning) and Unit 5 deployment example (e.g. `06_flask_fastapi_deployment.ipynb`) so you can build and serve a model.”

---

## 6. Long-running notebooks (low impact; partly covered)

**Gap:** Some notebooks (e.g. Unit 2 transfer learning, Unit 3 BERT) run for **10–40+ minutes**. On CPU they can be much slower. Students might think the kernel is stuck.

- **Mitigation:** Unit 2, 3, and 4 READMEs now have **⏱ Long run** notes. COLAB_SETUP suggests GPU and mentions reducing batch size / subset.
- **Remaining gap:** The **first** long-running notebook in a unit might not have a **cell** that says “This may take 10–20 min on GPU” (only the README does).

**Suggested fix:** Optional: add one short markdown cell near the top of the longest notebooks (e.g. Unit 2 `04` or `05`): “⏱ **Runtime:** This notebook may take 10–40 minutes on GPU. Use a smaller subset or fewer epochs if needed (see unit README).”

---

## 7. Common errors beyond TensorFlow (low impact)

**Gap:** COLAB_SETUP and several notebooks cover **TensorFlow** (e.g. charset_normalizer) and **Colab** (GPU, OOM). Other environments (e.g. local Windows, Apple Silicon, conda) might have different errors, and there is no single “common errors” page for students.

- **Mitigation:** COLAB_SETUP has a Troubleshooting section; many notebooks print a short fix for the charset_normalizer issue.
- **Gap:** No student-facing list like “If you see X, do Y” for 2–3 more common cases (e.g. CUDA OOM, pip conflict).

**Suggested fix:** Optional: add a short “**Common errors**” subsection to **DOCS/REQUIREMENTS_COURSE_08.md** or **COLAB_SETUP.md** (e.g. “CUDA out of memory → reduce batch size”; “ModuleNotFoundError → pip install -r requirements.txt”).

---

## 8. Optional: more math depth (optional; not a bug)

**Gap:** Theory in notebooks is **short** (3–5 bullets). Students who want **derivations** (e.g. chain rule for backprop, full Q/K/V formula for attention) won’t find them in the notebook.

- **Design:** Course standard is “short theory + runnable code”; deep dives are for slides or external material.
- **Impact:** Only affects students who want more formal detail; they can use the slides or other resources.

**Suggested fix:** No change required. Optionally, add one line in the backprop or attention notebook: “For a full derivation of the chain rule (or Q,K,V), see the lecture slides or a reference (e.g. Goodfellow et al.).”

---

## 9. Code comments – standard and coverage (low impact)

**Gap:** Comment coverage in notebooks is **inconsistent**. Some (e.g. `02_simple_neural_network`) have clear step comments in code; others rely only on markdown, with no or minimal inline comments.

**Recommended standard (best practice):**
- **Markdown** remains the main teaching layer (objectives, theory, "Step 1 / 2 / 3").
- **Inline comments** are minimal and purposeful:
  - One short line at the **start of a code cell** stating what the cell does (e.g. `# Step 2: Load and normalize MNIST`), when the previous markdown doesn't already make it obvious.
  - On **non-obvious lines**: brief "why" (e.g. `# flatten for feedforward NN; CNNs keep 2D`).
  - For **magic numbers**: e.g. `epochs=3  # small for demo; use 10+ for real training`.
- **Avoid:** commenting every line; repeating markdown in comments; comments that only restate the code.

**Rule of thumb:** Every code cell has at least one short comment (step or purpose), or is clearly explained by the **immediately previous** markdown cell. Non-obvious choices get a brief "why" comment.

**Suggested fix:** Add minimal inline comments to notebooks that have none. Maintain this standard when adding or editing notebooks.

**Title and ordering:** The first heading (H1) in each notebook should match the **filename number** (e.g. `02_simple_neural_network.ipynb` → `# 02 Simple Neural Network`) so students can follow the recommended order in DOCS/EXAMPLES_ORDER.md. Step numbers inside a notebook (Step 1, 2, 3…) should be consecutive and match the order of cells.

---

## Summary table

| # | Gap | Impact | Fix |
|---|-----|--------|-----|
| 1 | Broken refs (DETAILED_UNIT_DESCRIPTIONS, COURSE_MAP) | Medium | Clarify START_HERE + unit READMEs; say “if available” or use README + EXAMPLES_ORDER as primary |
| 2 | No self-check (exercises/quizzes) | By design | Optional: “expected output” hint in exercises; or state in checklist that solutions are released by instructor |
| 3 | Slides dependency wording | Low–medium | One sentence: “You can follow notebooks in order even without slides” |
| 4 | TF vs PyTorch which notebooks | Low | One sentence in README or REQUIREMENTS: “Most use TF; some Unit 3 use PyTorch; install both for full coverage” |
| 5 | Project 01 preparation | Low | One “Recommended preparation” line in project README |
| 6 | Long-run note inside notebook | Low | Optional: one “⏱ Runtime” cell in longest notebooks |
| 7 | Common errors (beyond TF) | Low | Optional: short “Common errors” in REQUIREMENTS or COLAB_SETUP |
| 8 | More math depth | Optional | No change or one "see slides/reference" line |
| 9 | Code comments inconsistent | Low | Minimal inline comments per code cell; document standard (section 9) |

---

**Last updated:** 2026-02-07
