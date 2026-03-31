# Course 05 Deep Dive Report
## AIAT 115 – Scalable Data Science

**Date:** 2025-01-24  
**Reference:** `DETAILED_UNIT_DESCRIPTIONS.md` (Course 5), Unit READMEs, example notebooks, DOCS, QUIZZES.

---

### ✅ Implementation status (post–perfection pass)

All P0–P2 fixes and the “perfect + aligned with DETAILED_UNIT_DESCRIPTIONS” pass are **done**:

- **Unit 2:** Content↔filename corrected (01–08); `08_feature_extraction_unstructured` added (text + images); titles and Example refs updated; Leads to / Next fixed.
- **Unit 4:** Example 10–13 → 04–07, 12; `12_cpu_vs_gpu` and `07_model_evaluation` refs updated; duplicates removed (`16`).
- **Unit 5:** Duplicates removed (20, 21, 22); cross-refs 14–20 → 02–07; `08_deployment` self-ref fixed; Previous/Next and spec ref added.
- **Docs:** README CLOs from spec; explicit “aligned with DETAILED_UNIT_DESCRIPTIONS”; tests→quizzes; Unit 2/3 READMEs; SETUP paths clarified; nested folder removed.

Course 05 is **aligned with the spec** and ready for use.

---

## 1. Executive Summary

Course 05 is **structurally aligned** with the spec (5 units, 96 h, unit↔folder mapping) and **runs**: all 57 notebooks execute successfully. Several **content**, **organization**, and **documentation** issues remain that affect clarity, spec compliance, and student experience.

| Area | Status | Notes |
|------|--------|------|
| **Spec alignment (theory)** | ⚠️ Partial | Most topics covered; Unit 2 “feature extraction for unstructured data” missing. |
| **Spec alignment (practical)** | ⚠️ Partial | Unit 2 notebook **content shuffled** across 02–08; filenames ≠ content. |
| **Organization** | ❌ Issues | Duplicate notebooks (Unit 4: 12 vs 16; Unit 5: 08–10 vs 20–22). Cross-refs mix old/new numbering. |
| **Documentation** | ⚠️ Minor | README “each unit contains tests” is false; Unit 3 count outdated; SETUP paths vary. |
| **Execution** | ✅ OK | All Course 05 notebooks run successfully. |

**Bottom line:** Fix Unit 2 content/filenames, remove duplicates, correct cross-references and docs. Then the course will match the spec and be easier to teach and maintain.

---

## 2. Spec Alignment vs DETAILED_UNIT_DESCRIPTIONS

### 2.1 Unit 1: Introduction to Data Science (6 + 12 h)

| Spec | Implemented | Status |
|------|-------------|--------|
| Data science overview, lifecycle, applications | `01_data_science_intro` | ✅ |
| Python basics: control flow, loops, functions | `04_python_basics_loops_conditions` | ✅ |
| List comprehensions, **lambda**, **exceptions** | Same notebook | ✅ |
| Jupyter setup, structure, best practices | `05_jupyter_notebooks_best_practices` | ✅ |
| Data types, lists, dicts, DataFrames | `06_data_structures_*`, `02_pandas_numpy` | ✅ |
| NumPy, Pandas, cuDF, Numba | `02`, `03_cudf`, `08_numba`, `09_advanced_numpy` | ✅ |
| Practical: Python, Jupyter, structures, NumPy/Pandas/cuDF, small DS projects | Examples 01–09 + exercise | ✅ |

**Verdict:** Unit 1 matches the spec. Lambda and exception handling are present.

---

### 2.2 Unit 2: Data Cleaning and Preparation (6 + 13 h)

| Spec | Implemented | Status |
|------|-------------|--------|
| Import/export (CSV, Parquet, etc.) with cuDF | Content in **08** (cuDF), filename says “feature extraction” | ⚠️ Wrong file |
| Cleaning, missing data, duplicates | Content split across **02**, **03** (titles don’t match filenames) | ⚠️ Shuffled |
| Outliers, transformation, feature engineering | **04**, **05** (content offset from filenames) | ⚠️ Shuffled |
| **Feature extraction for unstructured data (text, images)** | **Missing** | ❌ |
| EDA (visual + statistical) | **05**, **06**, **07** (EDA vs transformation vs cuDF mixed) | ⚠️ Shuffled |
| GPU / cuDF optimization | Content in **08**; **07** has Statistical EDA | ⚠️ Swapped |

**Content vs filename (audit):**

| File | Actual content (from titles) | Intended topic |
|------|-----------------------------|----------------|
| `01_data_loading` | Data Loading | ✅ Data loading |
| `02_missing_values_duplicates` | “04. Advanced Data Loading” | Missing values & duplicates |
| `03_outliers_transformation` | “05. Missing Values & Duplicates” | Outliers |
| `04_feature_transformation_*` | “06. Outliers & Data Transformation” | Feature transformation |
| `05_eda_visualizations` | “05. Feature Transformation: Scaling and Encoding” | EDA visualizations |
| `06_statistical_eda` | “06. EDA: Visualizing Data Distributions” | Statistical EDA |
| `07_cudf_import_export_gpu` | “08. Statistical Exploratory Data Analysis” | cuDF import/export |
| `08_feature_extraction_unstructured` | “cuDF Import/Export and GPU Acceleration” | Feature extraction (text/images) |

**Gaps:**

1. **Feature extraction for unstructured data**  
   Spec: *“Feature extraction techniques for unstructured data (e.g., text or images).”*  
   There is no notebook that covers text (e.g. word count, basic embeddings) or image (e.g. pixel stats, simple features) feature extraction. `08_feature_extraction_unstructured` is misused for cuDF.

2. **Unit 2 README “Topics”**  
   Lists only: Data Loading, Missing Values, Duplicates, Outliers, Data Transformation.  
   Omits: EDA (visual + statistical), Feature extraction, GPU/cuDF.

**Verdict:** Unit 2 has a **content shuffle** (02–08) and a **missing** spec topic (unstructured feature extraction). cuDF/EDA content exists but is in the wrong notebooks.

---

### 2.3 Unit 3: Data Visualization (6 + 13 h)

| Spec | Implemented | Status |
|------|-------------|--------|
| Matplotlib, Seaborn, chart types, customization | `01`–`03`, `06`, `07` | ✅ |
| Plotly interactive, dashboards | `04`, `05`; HTML exports (11–15) | ✅ |
| Practical: charts, interactive viz, best practices | Examples 01–08 | ✅ |

**Verdict:** Aligned. README says “7 notebooks” but there are **8** (01–08); update README.

---

### 2.4 Unit 4: Introduction to Machine Learning (7 + 13 h)

| Spec | Implemented | Status |
|------|-------------|--------|
| ML overview, sklearn, regression, classification, clustering | `01`–`11` | ✅ |
| Evaluation, hyperparameter tuning | `07`, `08` | ✅ |
| Real‑world mix, CPU vs GPU ML | `11`, `12`; **also** `16_cpu_vs_gpu_ml` | ⚠️ Duplicate |

**Duplicate:**  
`12_cpu_vs_gpu_ml.ipynb` and `16_cpu_vs_gpu_ml.ipynb` both cover CPU vs GPU ML. `16` uses old “Example 13” / “Examples 10–12” numbering. Keep one (e.g. `12`), remove or redirect the other.

**Verdict:** Spec covered. Remove duplicate and fix any refs to “Example 13” / “16.”

---

### 2.5 Unit 5: Extending the Scope of Data Science (7 + 13 h)

| Spec | Implemented | Status |
|------|-------------|--------|
| Big Data (4 Vs), technologies, challenges | `01_big_data_theory` | ✅ |
| Dask, PySpark, distributed computing | `02_dask`, `03_pyspark` | ✅ |
| RAPIDS / GPU workflows | `04_rapids` | ✅ |
| Deployment (Flask/FastAPI), scaling, monitoring | `08_deployment`, `09_model_monitoring` | ✅ |
| Pipelines, large datasets, automation | `05`–`07`, `10_data_pipeline_automation` | ✅ |

**Duplicates:**  
`20_deployment`, `21_model_monitoring`, `22_data_pipeline_automation` largely duplicate `08`, `09`, `10`. The 20–22 set uses “Examples 14–18/19/20” and “Example 19” style refs. The 01–10 set uses “Examples 02–07,” “EIGHTH,” etc. Having both causes confusion.

**Verdict:** Spec covered. **Remove 20, 21, 22** and use only 01–10. Update any remaining refs to “14–18” or “19/20.”

---

## 3. Organization Issues

### 3.1 Duplicate notebooks

- **Unit 4:** `12_cpu_vs_gpu_ml` vs `16_cpu_vs_gpu_ml`. Keep `12`, remove `16` (or clearly mark as legacy and redirect).
- **Unit 5:** `08`/`09`/`10` vs `20`/`21`/`22`. Keep 08–10, remove 20–22.

### 3.2 Cross‑references and numbering

- **Unit 5:** Refs to “Examples 14–18,” “Example 19,” “Example 20” (old scheme) appear in 20–22 and possibly elsewhere. With 01–10 as canonical, these should be updated or removed.
- **Unit 2:** Prerequisites / “Next” refs (e.g. “Example 1,” “Example 4,” “Example 6”) are inconsistent with the actual sequence and the content shuffle. Fix after correcting content↔filename mapping.
- **Unit 4:** `16_cpu_vs_gpu` mentions “Example 7,” “Example 12,” “Example 13.” Align with the chosen numbering (e.g. 01–12).

### 3.3 Unit 2 nested folder

- `unit2-cleaning/examples/unit2-cleaning/examples/` contains duplicate CSVs (`large_data`, `sample_data*`). Prefer a single `examples/` and remove the nested copy.

### 3.4 Unit 5 deployment “Example 08” self‑reference

- `08_deployment` says “Solving the Problem from **Example 08**” and “from Example 08!” — it should reference the **previous** example (e.g. 07 – large datasets), not itself.

---

## 4. Documentation Issues

### 4.1 Tests vs quizzes

- **README:** “Each unit contains **tests**.”  
- **Reality:** Units have **quizzes** (`QUIZZES/`). There are no dedicated “unit tests” or `tests/` folders per unit.
- **Progress checklist:** “Take Unit X **Test**” — same mismatch.
- **Action:** Either add unit tests or change wording to “quizzes” everywhere.

### 4.2 Unit 3 example count

- README: “7 notebooks + HTML exports.”  
- Actual: **8** notebooks (01–08) + HTML. Update to “8 notebooks + HTML exports.”

### 4.3 Setup instructions

- `SETUP_INSTRUCTIONS.md` uses both `pip install -r ../requirements.txt` and `pip install -r requirements.txt` depending on context.  
- **Action:** State clearly: “Run from Course 05 root” (or repo root) and use a single, consistent command.

### 4.4 Unit 2 README topics

- “Topics” omit EDA, feature extraction, and GPU/cuDF. Update to match spec and actual content once Unit 2 is fixed.

---

## 5. What’s Working Well

- **Unit 1:** Structure, Python/Jupyter/NumPy/Pandas/cuDF/Numba, lambda, exceptions.
- **Unit 3:** Visualization flow (Matplotlib → Seaborn → Plotly), 8 examples + HTML.
- **Unit 5:** Big Data theory (`01_big_data_theory`), Dask/PySpark/RAPIDS, deployment (Flask/FastAPI in 08/20), monitoring, pipelines.
- **DOCS:** `SETUP_INSTRUCTIONS`, `COLAB_SETUP`, `SOLUTIONS/quizzes` (Quiz 01–05) exist and are referenced.
- **QUIZZES:** All five units have quizzes; Quiz 05 title matches “Extending the Scope.”
- **COURSE_MAP:** Unit READMEs point to `../../COURSE_MAP.md`; file exists at repo root.
- **Execution:** All 57 Course 05 notebooks run successfully.

---

## 6. Recommendations (Prioritized)

### P0 – Critical (spec + integrity)

1. **Fix Unit 2 content↔filename alignment**  
   Restore correct content into the right notebooks (01–08) so that:
   - 01 = Data loading  
   - 02 = Missing values & duplicates  
   - 03 = Outliers  
   - 04 = Feature transformation  
   - 05 = EDA visualizations  
   - 06 = Statistical EDA  
   - 07 = cuDF import/export & GPU  
   - 08 = **Feature extraction for unstructured data** (text + images)

2. **Add feature extraction for unstructured data**  
   Implement spec: simple text features (e.g. word count, length) and image features (e.g. pixel mean/std, shape) in `08_feature_extraction_unstructured`, and remove cuDF content from it.

### P1 – High (organization)

3. **Remove duplicate notebooks**  
   - Unit 4: delete `16_cpu_vs_gpu_ml` (keep `12`).  
   - Unit 5: delete `20_deployment`, `21_model_monitoring`, `22_data_pipeline_automation` (keep 08–10).

4. **Fix cross‑references**  
   - Unit 5: eliminate “Examples 14–18,” “19,” “20” refs; use 01–10 consistently.  
   - Unit 5 `08_deployment`: change “Example 08” self‑reference to “Example 07” (or previous example).  
   - Unit 2: align “Example N” and “Next” with corrected content and order.

### P2 – Medium (docs + polish)

5. **Tests vs quizzes**  
   Replace “unit contains tests” / “Take Unit X Test” with “quizzes” (and link to `QUIZZES/`) unless you actually add unit tests.

6. **Update READMEs**  
   - Unit 3: “8 notebooks + HTML exports.”  
   - Unit 2: extend “Topics” with EDA, feature extraction, GPU/cuDF once content is fixed.

7. **Cleanup**  
   - Remove `unit2-cleaning/examples/unit2-cleaning/examples/` or merge assets into `examples/` and delete the duplicate folder.  
   - Standardize `SETUP_INSTRUCTIONS` on one `pip install -r ...` flow and document where to run it from.

---

## 7. Summary Table

| Issue | Priority | Action |
|-------|----------|--------|
| Unit 2 content shuffle (02–08) | P0 | Restore correct content to each notebook |
| Missing feature extraction (text/images) | P0 | Add in `08_feature_extraction_unstructured` |
| Unit 4: `16` duplicate of `12` | P1 | Remove `16_cpu_vs_gpu_ml` |
| Unit 5: 20–22 duplicate 08–10 | P1 | Remove 20, 21, 22 |
| Unit 5 “Example 14–20” refs | P1 | Update to 01–10 |
| Unit 5 deployment “Example 08” self‑ref | P1 | Change to “Example 07” |
| “Unit contains tests” / “Unit X Test” | P2 | Switch to “quizzes” |
| Unit 3 “7 notebooks” | P2 | Change to “8 notebooks” |
| Unit 2 nested `unit2-cleaning/examples/` | P2 | Remove or consolidate |
| SETUP `requirements.txt` paths | P2 | Unify and document |

---

*Generated from review of Course 05 structure, notebooks, DETAILED_UNIT_DESCRIPTIONS, and supporting docs.*
