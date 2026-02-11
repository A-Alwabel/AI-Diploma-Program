# Course 08 – Gaps for students
## What might be missing or unclear from a student’s perspective

This list is for instructors and maintainers: it summarizes **gaps** (missing or unclear things) that can affect students. Items are ordered by impact; suggested fixes are included where applicable.

---

## Theory → Practical connection (gaps)

These gaps concern how clearly **theory** (slides, concepts) is tied to **practice** (notebooks, exercises, assessments) for students.

| # | Gap | Impact | Suggested fix |
|---|-----|--------|----------------|
| T1 | **Exercises don't state which theory/notebook they apply** | Low–medium | In each exercise notebook, add one line: *"This exercise applies the theory and code patterns from examples 01_deep_learning_fundamentals, 02_simple_neural_network."* (Unit README already says "aligns with"; putting it in the exercise makes the link visible there too.) |
| T2 | **Quizzes don't say which notebook/slide the question comes from** | Low | Quiz has "Mapping: CLO1; notebooks: 02_..., 05_..., 06_..." at the end. Optionally add a short line at the top: *"Concepts from Unit 1 examples 02, 05, 06 (and related slides)."* so students know theory→practice→assessment. |
| T3 | **Within a notebook: theory bullet ↔ code step not explicit** | Low | "Theory (short)" lists bullets; then Step 1, 2, 3… run. Steps don't say "This implements the [chain rule / optimizer] bullet above." Optionally add one sentence before a key code block: *"The next cell implements the gradient-update formula from Theory above."* |
| T4 | **Unit 5 has no slides** | By design | Theory for Unit 5 is only inside each notebook (Theory section + code). README already states "Unit 5 has no slides." No fix needed; just be aware the theory→practical link is notebook-internal only for Unit 5. |
| T5 | **Self-study without slides** | Mitigated | README says "each notebook has enough theory to proceed." Some notebooks could add one line after Theory (short): *"The steps below put this theory into code."* to make the link explicit for self-learners. |

**Summary:** The connection exists (slide↔notebook, Theory (short) + steps, README "Theory → Practical" line). The gaps above are about making that link **explicit in more places** (exercise intro, quiz header, optional in-notebook callouts).

**Applied fixes (2026-02-11):** T1 — added **Theory → Practice:** line to all 8 exercise notebooks (which examples they apply). T2 — added **Concepts from:** line to all 5 quizzes (which unit examples and slides). T5 — added **The steps below put this theory into code.** after Theory (short) in Unit 1 examples 01, 02, 04, 05, 06. T3 (in-notebook callout before a specific code block) remains optional; T4 (Unit 5 no slides) is by design.

---

## "Dr, it's not connected" / ordering confusion (student feedback)

**Gap:** Students sometimes say the material feels "not connected"—often because of **ordering confusion**: slide numbers (08, 01, 02, …) do **not** match notebook file numbers (01, 02, 03, …). So if the lecturer says "today we did slide 08," the correct notebook to do is **01_** (first in the unit), not "08." Optional notebooks (e.g. 07, 08) can also feel "out of order" if done at the wrong time.

**Applied fix:** One clear rule is now stated in several places: **Always follow notebook file number order (01 → 02 → 03 …). Slide numbers are topic IDs only—do not use them to decide order.** Added to: README ("❓ Dr, it's not connected"), START_HERE, DOCS/EXAMPLES_ORDER.md (section "Order rule"), and each unit README ("Do notebooks in this number order: 01 → 02 → …"). When a student says "it's not connected," point them to this rule and to the unit README list.

---

## "Some notebooks are not clear" / students didn't understand (student feedback)

**Gap:** Students say they follow the order but "some notebooks are not clear" or "I didn't understand some of it" — i.e. **content clarity**, not ordering.

**Applied fix:** (1) **Student guide:** **DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md** — how to pinpoint which part (notebook + section), how to use Theory/Steps/Expected/Summary, what to do when math or code is unclear, which notebooks are often harder, and one sentence to use when asking the instructor. (2) **Instructor guide:** **DOCS/NOTEBOOK_CLARITY_FOR_INSTRUCTORS.md** — table of notebooks often reported unclear (backprop, optimization, attention, transfer learning, RL, GANs/VAE, etc.) with "Why students struggle" and "What helps"; checklist for editing notebooks for clarity; optional "If this is unclear" lines. (3) **README and START_HERE:** Short pointer to WHEN_A_NOTEBOOK_IS_NOT_CLEAR. (4) **In-notebook hints:** Added 💡 **If this is unclear** in Unit 1 notebooks 04, 05, 06 (activation, backprop, optimization) so students see what to focus on and how to ask for help.

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

## 8. Math depth required (medium impact)

**Gap:** Theory in notebooks is **short** (3–5 bullets). Where the topic is **math-heavy** (e.g. backprop, attention, optimization), key **formulas and derivations** (e.g. chain rule for backprop, Q/K/V for attention) are required in the course materials, not optional.

- **Course standard:** Notebooks must include **key math** where the topic demands it: formulas, short derivation, or a clear “Key math” subsection. Full derivations can be in the notebook or linked to slides/reference (e.g. Goodfellow et al.).
- **Impact:** Without this, students do not get the formal grounding the course expects.

**Suggested fix:** For each math-heavy notebook (e.g. backpropagation, activation/optimization, attention/transformers), add a **Key formulas / Math** subsection (or expand Theory) with: the main equation(s), a short derivation or “why this form,” and optionally “For full derivation see [slides/reference].” See **DOCS/NOTEBOOK_STANDARD.md** (required elements).

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
| T | Theory → Practical (T1–T5) | Low–medium | See "Theory → Practical connection (gaps)" above |
| 1 | Broken refs (DETAILED_UNIT_DESCRIPTIONS, COURSE_MAP) | Medium | Clarify START_HERE + unit READMEs; say “if available” or use README + EXAMPLES_ORDER as primary |
| 2 | No self-check (exercises/quizzes) | By design | Optional: “expected output” hint in exercises; or state in checklist that solutions are released by instructor |
| 3 | Slides dependency wording | Low–medium | One sentence: “You can follow notebooks in order even without slides” |
| 4 | TF vs PyTorch which notebooks | Low | One sentence in README or REQUIREMENTS: “Most use TF; some Unit 3 use PyTorch; install both for full coverage” |
| 5 | Project 01 preparation | Low | One “Recommended preparation” line in project README |
| 6 | Long-run note inside notebook | Low | Optional: one “⏱ Runtime” cell in longest notebooks |
| 7 | Common errors (beyond TF) | Low | Optional: short “Common errors” in REQUIREMENTS or COLAB_SETUP |
| 8 | Math depth (required where topic is math-heavy) | Medium | Add key formulas/derivations in notebooks (or "Key math" subsection); link to slides/reference for full derivation |
| 9 | Code comments inconsistent | Low | Minimal inline comments per code cell; document standard (section 9) |

---

**Last updated:** 2026-02-07
