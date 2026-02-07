# Project 01: Image Classification System – Grading Rubric
## Course 08 – AIAT 122

**Total: 100 points.**

---

## Point allocation

| Criterion | Points | Description |
|-----------|--------|-------------|
| Data & preprocessing | 20 | Dataset choice, load/split, resize/normalize, augmentation, loaders |
| Model design | 25 | Architecture (CNN or transfer learning), justification, correct num_classes |
| Training & evaluation | 20 | Training loop, validation, test metrics (accuracy and optionally F1/confusion matrix), saved model |
| Deployment / demo | 20 | Export + API or notebook inference or Gradio/Streamlit demo; clear run instructions |
| Report & clarity | 15 | Report (problem, data, model, results, limitations); code readability and README |
| **Total** | **100** | |

---

## Detailed criteria

### Data & preprocessing (20 pts)

| Score | Criteria |
|-------|----------|
| 18–20 | Clear dataset; train/val/test split; correct resize and normalization; augmentation used where appropriate; data loaders work. |
| 14–17 | Minor issues (e.g. no augmentation, or split not documented). |
| 10–13 | Data loaded but preprocessing incomplete or inconsistent. |
| 0–9 | Missing or wrong preprocessing; no clear split. |

### Model design (25 pts)

| Score | Criteria |
|-------|----------|
| 22–25 | Appropriate CNN or transfer learning; top layer/head correct for num_classes; short justification. |
| 17–21 | Correct architecture; justification brief or missing. |
| 12–16 | Model runs but architecture choice unclear or not suitable. |
| 0–11 | Wrong architecture or not implemented. |

### Training & evaluation (20 pts)

| Score | Criteria |
|-------|----------|
| 18–20 | Training with validation; test accuracy (and optionally F1/confusion matrix); model saved. |
| 14–17 | Training and evaluation present; one of validation, test metrics, or save missing. |
| 10–13 | Training runs but evaluation or save incomplete. |
| 0–9 | No proper training or evaluation. |

### Deployment / demo (20 pts)

| Score | Criteria |
|-------|----------|
| 18–20 | Model exported and either (A) API that accepts image and returns prediction, or (B) clear inference notebook/script, or (C) working Gradio/Streamlit demo; run instructions clear. |
| 14–17 | Export and one of API/script/demo; instructions slightly unclear. |
| 10–13 | Only inference script or only export; no API or demo. |
| 0–9 | No export or no way to run inference. |

### Report & clarity (15 pts)

| Score | Criteria |
|-------|----------|
| 13–15 | 1–2 page report: problem, data, model, results, limitations; code readable with brief comments; README explains how to run. |
| 10–12 | Report covers most sections; code or README slightly unclear. |
| 6–9 | Report or README minimal. |
| 0–5 | Missing or not understandable. |

---

## Partial credit

- Award partial points when a criterion is partially met.
- Bonus (up to +2) for extra (e.g. confusion matrix, per-class metrics, or fairness check) if not required.

---

**For:** Course 08 – Instructor use only
