# Course 05: Run & Understanding Status

**Date:** January 24, 2026

---

## Do all run perfectly without errors?

**Yes.** All **46** Course 05 notebooks (examples + exercises) execute successfully with **no errors**.

| Unit | Notebooks | Status |
|------|-----------|--------|
| Unit 1 – Introduction | 10 | All OK |
| Unit 2 – Cleaning | 7 | All OK |
| Unit 3 – Visualization | 8 | All OK |
| Unit 4 – ML Intro | 12 | All OK |
| Unit 5 – Scaling | 9 | All OK |

---

## Fixes applied (no changes to `DETAILED_UNIT_DESCRIPTIONS.md`)

1. **`03_cudf_introduction`**
   - `n_rows` / `df_pandas` (Part 1 “Creating Sample Data”)
   - `df_cudf` setup, `result_cudf`, `grouped_*`, `sorted_*`, `print` f-strings
   - Performance viz: `op_names`, `pandas_times`, `cudf_times`, `speedups`, `bbox_inches`, loop indentation

2. **`13_cpu_vs_gpu_ml`**
   - `cpu_times_reg` / `gpu_times_reg`, `cpu_times_clf` / `gpu_times_clf` in the comparison viz cell

3. **Duplication & cleanup (earlier)**
   - Removed misaligned/duplicate long-name notebooks
   - Cleaned placeholder `##` markdown cells
   - Added `15_pyspark_distributed` to `artifacts/executed`
   - Fixed `pd_` → `pd` in `06_customizing_annotating_visualizations`

---

## Conflicts for understanding?

**No.** There are no remaining **conflicts for understanding**:

- **Execution:** All notebooks run; no `NameError` / `SyntaxError` / `IndentationError`.
- **Structure:** Numbered examples (01–22, etc.) have clear objectives, prerequisites, “where this fits,” and progression.
- **Duplication:** Redundant or misaligned long-name notebooks were removed.
- **Outputs:** Prints, section headers, and viz outputs are clear and human-readable.
- **Progression:** Unit 1 → 2 → 3 → 4 → 5 is consistent; “builds on” / “leads to” are explicit.

**Optional:** Some units reuse number prefixes (e.g. two `05_`, two `10_`) for **different** topics. That’s naming only, not content conflict. Renumbering could reduce confusion but isn’t required for correctness or understanding.

---

## Summary

| Question | Answer |
|----------|--------|
| Do all run without errors? | **Yes** – 46/46 OK |
| Any conflicts for understanding? | **No** |
| Safe for students? | **Yes** – runnable, clear, aligned with detailed units |

---

*Reference: `DETAILED_UNIT_DESCRIPTIONS.md` (Course 5), `REVIEW_ARTIFACTS_VS_DETAILED_UNITS.md`, `DUPLICATION_SUMMARY.md`.*
