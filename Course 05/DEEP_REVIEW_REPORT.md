# Course 05 – Deep Review Report

**Scope:** All Course 05 files (notebooks, READMEs, docs, quizzes, solutions, structure).  
**Purpose:** Identify what’s missing, what to edit, and what to clean up.

---

## 1. Executive Summary

| Category | Status | Count |
|----------|--------|-------|
| Notebooks (examples + exercises) | ✅ Valid JSON, no malformed titles, no empty markdown | 52 |
| Malformed titles | ✅ Fixed (Unit 3 viz) | 0 |
| Empty markdown cells | ✅ None | 0 |
| Duplicate H1 in multi‑part notebooks | ⚠️ Optional | 4 (Unit 4) |
| Junk / duplicate files | ❌ To fix | 2 |
| Broken or inconsistent links | ⚠️ To fix | 2 |
| README / doc nits | ⚠️ Optional | 3 |

**Overall:** Course 05 is in very good shape. The items below are edits and cleanups, not blocking issues.

---

## 2. Fix Now (Recommended)

### 2.1 Remove junk / temporary files

- **Delete:** `unit2-cleaning/examples/08_feature_extraction_unstructured.ipynb.tmp`  
  - Temp file; should not be tracked. Root `.gitignore` has `*.tmp`; remove the file and ensure it’s not committed.

### 2.2 Remove redundant nested folder

- **Delete:** `unit2-cleaning/examples/unit2-cleaning/examples/` (entire folder).  
  - Contains duplicate `large_data.csv`, `sample_data.csv`, `sample_data.json`, `sample_data.xlsx`.  
  - `01_data_loading` creates and uses files in `unit2-cleaning/examples/` (relative to repo root). The nested copy is redundant and was likely created by running the notebook from a different cwd.

### 2.3 Fix broken START_HERE path in Unit 1 README

- **File:** `unit1-introduction/README.md`  
- **Current:** `Read \`Course 05/START_HERE.md\``  
- **Issue:** From `Course 05/unit1-introduction/`, that path resolves to `unit1-introduction/Course 05/START_HERE.md`, which doesn’t exist.  
- **Fix:** Use `../START_HERE.md` (or `START_HERE.md` if interpreted from Course 05 root).

---

## 3. Edit / Improve (Optional)

### 3.1 Unit README duplicate headers

- **Units 1–5 READMEs:** Each has two consecutive lines:
  - `# Unit: ...`
  - `## Unit: ...` (or `## ...`重复)
- **Example:** `unit2-cleaning/README.md` lines 1–2: both "Data Cleaning and Preprocessing".  
- **Suggestion:** Keep a single clear unit title and remove the duplicate `##` line, or make the second line a subtitle.

### 3.2 QUIZZES/README.md – link to solutions

- **Current:** “Check your answers using the answer key” with no link.  
- **Fix:** Add explicit link, e.g.  
  - “Check your answers in \`DOCS/SOLUTIONS/quizzes/\` (see per‑unit READMEs).”

### 3.3 Unit 4 multi‑part notebooks – repeated H1

- **Notebooks:**  
  - `05_supervised_learning_logistic_regression`  
  - `08_hyperparameter_tuning_grid_random_search`  
  - `09_unsupervised_learning_kmeans`  
  - `11_real_world_problem_solving`  
- **Pattern:** Cell 0 has `# NN. Title`; Part 1 / Part 2 cells repeat `# Title` (no number).  
- **Suggestion:** Prefer `## Part 1`, `## Part 2` (or similar) instead of repeating the main `#` title. Purely optional for consistency.

---

## 4. What’s Already Good

- **Notebooks:** All 52 run; no malformed titles, no empty markdown, no invalid JSON.  
- **Structure:** Units 1–5 match deep dives and spec; examples/exercises/solutions present.  
- **Docs:** `DETAILED_UNIT_DESCRIPTIONS.md` (repo root), `DEEP_DIVE_UNITS_2_5.md`, `UNIT1_DEEP_DIVE.md`, `SCORING_RUBRIC_AND_SCORECARD.md` all referenced and consistent.  
- **Quizzes:** Quiz 01–05 present; solutions in `DOCS/SOLUTIONS/quizzes/`.  
- **Paths:** `../requirements.txt`, `../DETAILED_UNIT_DESCRIPTIONS.md`, `../../COURSE_MAP.md` correctly used from Course 05 and unit folders.  
- **Data loading:** `01_data_loading` uses `unit2-cleaning/examples/`; only the nested duplicate folder is redundant.

---

## 5. Checklist – Do These

| # | Action | Location |
|---|--------|----------|
| 1 | Delete | `unit2-cleaning/examples/08_feature_extraction_unstructured.ipynb.tmp` |
| 2 | Delete | `unit2-cleaning/examples/unit2-cleaning/` (entire nested folder) |
| 3 | Fix link | `unit1-introduction/README.md`: `Course 05/START_HERE.md` → `../START_HERE.md` |
| 4 | (Optional) | Remove duplicate `##` unit titles in unit READMEs |
| 5 | (Optional) | Add solutions link in `QUIZZES/README.md` |
| 6 | (Optional) | Unit 4 multi‑part notebooks: use `## Part 1` / `Part 2` instead of repeated `# Title` |

---

## 6. Files Touched in This Review

- All `Course 05/**/*.ipynb` (examples + exercises, excl. solutions)  
- All `Course 05/**/README.md`  
- `Course 05/QUIZZES/README.md`, `START_HERE.md`, `README.md`, `SCORING_RUBRIC_AND_SCORECARD.md`  
- `Course 05/DOCS/SOLUTIONS/`, `DEEP_DIVE_UNITS_2_5.md`, `UNIT1_DEEP_DIVE.md`  
- `unit2-cleaning/examples/` (including nested folder and `.tmp`)

---

**Report generated:** Deep review of Course 05 (all referenced files).  
**Next step:** Apply checklist items 1–3, then optionally 4–6.
