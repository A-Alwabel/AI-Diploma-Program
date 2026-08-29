# Design Document — Titanic survival-risk scoring service (worked example)

*Generated from the design dictionary by the AIAT 126 Unit 2 notebook.*

## 1. Prior Work Inventory (AIAT 111-125)

- **source:** AIAT 115 U2 — Course 05/unit2-cleaning/examples/01_data_loading.ipynb — REUSE — same loading/inspection routine, new file
- **prep:** AIAT 114 U1 + AIAT 115 U2 — Course 04/unit1-regression-algorithms/examples/03_data_preprocessing.ipynb — EXTEND — same ColumnTransformer pattern, new column list from the Part 4 plan
- **train:** AIAT 114 U3 + U5 — Course 04/unit3-classification/examples/01_logistic_regression.ipynb — REUSE — classifier and metrics; grid search from unit5/01_grid_search.ipynb
- **store:** AIAT 125 U2 — Course 11/unit2-versioning-serving/examples/04_saving_loading_models_pickle_onnx.ipynb — REUSE — joblib artifact + version naming convention
- **serve:** AIAT 125 U2 — Course 11/unit2-versioning-serving/examples/02_fastapi_deployment.ipynb — EXTEND — same endpoint shape, new request schema from Part 6
- **monitor:** AIAT 125 U5 — Course 11/unit5-pipelines-monitoring/examples/04_drift_detection.ipynb — EXTEND — drift check plus the per-subgroup metric this project needs
- **risk review:** AIAT 116 U2 + U4 — Course 06/unit2-bias-fairness/examples/01_bias_detection.ipynb — REUSE — bias detection applied to the Sex disparity found in Part 5

## 2. System components

- source — Titanic manifest CSV · 891 rows × 12 cols | reads: titanic.csv (read-only, licensed for coursework) | writes: raw DataFrame
- prep — impute · encode · scale (fit on TRAIN only) | reads: raw DataFrame | writes: feature matrix + a FITTED transformer object
- train — 2 candidates, chosen on validation | reads: feature matrix (train split) | writes: fitted estimator + validation metrics
- store — model.joblib · schema.json · metrics.json | reads: fitted estimator, fitted transformer, metrics | writes: versioned files on disk
- request — one passenger record as JSON | reads: caller input | writes: validated record matching schema.json
- serve — loads artifacts, applies the same preprocessing | reads: schema-valid record + artifacts | writes: probability + label
- response — JSON: probability · label · model version | reads: probability + label | writes: JSON to the caller
- monitor — logs I/O · drift · per-subgroup metrics | reads: every request and response | writes: append-only log + alerts

## 3. Data flow

source -> prep (raw rows) ; prep -> train (train matrix) ; train -> store (fitted artifacts) ; store -> serve (loaded at startup) ; request -> serve (JSON in) ; serve -> response (JSON out) ; serve -> monitor (every prediction logged)

## 4. Dataset selection and justification

- **chosen:** titanic.csv — 891 rows x 12 columns, 1912 passenger manifest
- **why:** real missingness (Age 19.9%, Cabin 77.1%), a real 61.8/38.2 class split and a real subgroup disparity, so every pipeline step is exercised by the data itself
- **licence:** public-domain historical record; coursework use permitted
- **excluded:** Cabin (77.1% missing), Name (free text, 891/891 distinct), Ticket (681 categories for 891 rows), PassengerId (identifier)
- **fallback if unavailable:** any tabular binary-outcome dataset with >10% missingness

## 5. Model and algorithm selection

- **chosen model:** Logistic regression on imputed + one-hot-encoded + scaled features
- **justification:** 534 training rows and 7 features: a linear model is fast, needs no tuning budget, and gives a coefficient per feature that can be shown to an affected person. Measured on validation: accuracy 0.8034, F1 0.7328
- **alternatives considered:**
  - Decision tree (depth 4) — higher accuracy (0.8146) but lower F1 (0.7273); kept as the fallback candidate
  - Random forest — rejected: loses the per-feature explanation this use case needs
  - Fine-tuned transformer — rejected: no text input, and 891 rows cannot support it
- **decision matrix winner:** Decision tree (depth 4)

## 6. Platform and tooling selection

- **training environment:** local CPU, the shared course venv (ai-diploma kernel)
- **why training:** the full fit takes under a second on 534 rows; a GPU would idle
- **serving target:** single-process FastAPI container (pattern from AIAT 125 U2)
- **why serving:** the artifact is 4,442 bytes and loads at startup, so one small container serves the expected request rate
- **rejected:** managed cloud endpoint — cost and account setup exceed the course scope

## 7. Data collection and preprocessing plan

- PassengerId: DROP (identifier) (unique per row — an ID carries no signal, only leakage risk)
- Survived: keep as target (never imputed; rows with a missing target are dropped)
- Pclass: standard-scale (numeric, 0 missing (0.0%))
- Name: OUT OF SCOPE (or separate text component) (891 distinct values in 891 rows — free text, not a category)
- Sex: one-hot encode (2 categories, 0 missing)
- Age: median impute + standard-scale (numeric, 177 missing (19.9%))
- SibSp: standard-scale (numeric, 0 missing (0.0%))
- Parch: standard-scale (numeric, 0 missing (0.0%))
- Ticket: GROUP or EXCLUDE (high cardinality) (681 categories for 891 rows — one-hot would add more columns than the data can support)
- Fare: standard-scale (numeric, 0 missing (0.0%))
- Cabin: DROP (77.1% missing — imputing this would be inventing data)
- Embarked: most-frequent impute + one-hot encode (3 categories, 2 missing)

## 8. Evaluation metrics and baselines

- **primary metric:** F1 on the positive (survived) class
- **why this metric:** the majority-class baseline reaches accuracy 0.618 with F1 0.0 — accuracy cannot distinguish a useful model from a constant one on this split
- **baselines:**
  - majority class: accuracy 0.618, F1 0.0
  - domain rule (female -> survived): accuracy 0.8034, F1 0.7368
- **must beat:** F1 > 0.7368 on validation, before the test set is opened once at gate 4
- **protocol:** 60/20/20 stratified split, random_state=42; test measured exactly once

## 9. Input/output formats and storage

Input: JSON record validated against 7 fields (Pclass, Sex, Age, SibSp, Parch, Fare, Embarked). Output: JSON with survival_probability, predicted_label, threshold_used, model_version. Artifacts in artifacts_example/ as titanic-survival-v0.1.joblib (4,442 bytes) plus .schema.json and .metrics.json.

## 10. Scalability, modularity and integration

- measured on 284,807 real rows of creditcard_fraud.csv: linear projection from four sample sizes missed the measured full-data time by 1.6%
- read only the required columns (usecols) — the first scalability technique, from AIAT 115 U5
- modularity: swapping the estimator changes the artifact-store format only; source, preprocessing, serving and monitoring interfaces hold
- integration: every component maps to a named AIAT 111-125 artifact (see section 1)

## 11. Risks and dependencies

- LEGAL/ETHICAL — the strongest single predictor is Sex (survival 0.742 female vs 0.1889 male). Scoring living people on a protected attribute is a fairness and legal problem: run the AIAT 116 U2 bias check and report per-subgroup metrics, or restrict the system to historical analysis.
- DATA — Cabin is 77.1% missing and is dropped; if a later requirement needs deck information the dataset cannot supply it.
- DATA — the domain-rule baseline ties or beats two of the candidate models, so the project must either add features with independent signal or narrow its claim.
- TECHNICAL — scikit-learn and joblib versions pinned in requirements.txt; a .joblib artifact does not load across major versions.
