# Tools

Helper scripts for course notebooks (I/O, objectives, clarity, splitting).

## Clarity and objectives

- **`clarity_multi.py`** – Multi-course clarity pass. Run from repo root.
  - `python tools/clarity_multi.py all` – Run objectives scripts, then duplicate Story removal, then optional terse I/O expansion.
  - `python tools/clarity_multi.py objectives` – Run only objectives (objectives_multi, c03/c04/c06/c07, clarity_updates_c05).
  - `python tools/clarity_multi.py story` – Remove duplicate "The Story | القصة" cells when intro already has "The Story: X" + before/after.
  - `python tools/clarity_multi.py io` – Expand terse Inputs/Outputs where mapped (see `TERSE_IO_UPDATES`).
  - Skips `DOCS`, `PROJECTS`, `.ipynb_checkpoints`.

- **`split_large_code_cells.py`** – Split oversized code cells that contain `# PART 1:`, `# PART 2:`, … section markers.
  - `python tools/split_large_code_cells.py` – Run on all Course 01–12 notebooks.
  - `--min-lines N` / `--min-chars N` – Thresholds (default 80 lines, 3500 chars).
  - Skips `DOCS`, `PROJECTS`, `.ipynb_checkpoints`. Optional `BLOCKLIST` in script.
  - Prints a report of which notebooks and cells were split.

## Suggested workflow

1. Run objectives: `python tools/clarity_multi.py objectives`
2. Run Story + I/O: `python tools/clarity_multi.py all` (or `story` / `io` only)
3. Split large code cells: `python tools/split_large_code_cells.py`

## Execution and validation

- **`run_modified_only.py`** – Execute only notebooks that were recently modified (syntax/runtime fixes). Writes `artifacts/execution_modified_report.json`.
  - `python tools/run_modified_only.py`
- **`run_execution_subset.py`** – Execute a subset of notebooks by course. Optional course list as arguments; default `Course 04` and `Course 05`. Writes `artifacts/execution_subset_report.json`.
  - `python tools/run_execution_subset.py "Course 04" "Course 05"`
- **`scan_syntax_errors.py`** – Scan all notebooks for Python syntax errors in code cells. Writes `artifacts/syntax_errors_scan.json`.

## Other tools

- `add_inputs_outputs_multi.py`, `objectives_multi.py` – Add I/O sections and replace generic objectives (courses 01, 02, 08–12).
- Per-course: `add_inputs_outputs_c03`–`c07`, `c03`–`c07_specific_objectives`, `clarity_updates_c05`.
- `fix_corrupted_json_notebooks.py` – Repair corrupted JSON in listed notebooks. **Skips** `01_ridge_lasso_regression` and `03_svm` (manually repaired); re-running repair on those would overwrite fixes.

## Impact and caveats (runtime fixes)

- **`01_logistic_regression`**: A bootstrap code cell was added (synthetic `X,y`, `model`, `y_proba`). Later blocks use `logistic_model`, `X_train_scaled`, etc. in **self-contained** cells that define them; no shared-state dependency on the bootstrap beyond the first thresholds block.
- **`04_word_embeddings_glove_fasttext`**: `%pip install gensim` + try/except for `KeyedVectors`; `GENSIM_AVAILABLE` set. No other code cells use `KeyedVectors`; the notebook has only a few cells.
- **`01_rnn_exercise`**: `generate_stock_data`, `SimpleRNN`, and `train_rnn` were implemented; `data` and `model` are created in the train cell. Task 4 (LSTM) remains a stub; no comparison code depends on it.
- **GPT / C10 finetuning**: `USE_TF=0` before `transformers` import; GPT setup split into pip-only vs imports. No downstream notebooks or scripts depend on these.
- **`fix_corrupted_json_notebooks`**: Do not re-run repair on `01_ridge_lasso_regression` or `03_svm`; they are skipped by the script.
