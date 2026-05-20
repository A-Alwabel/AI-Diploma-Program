# Course 11 — Run Requirements

Use this as the single reference for **how to run** Course 11 notebooks.

**Framework focus:** **PyTorch** and **scikit-learn** for models; **FastAPI** / **Flask** for serving; optional cloud SDKs for Unit 3 demos.

---

## Python

- **Version:** Python 3.10 or 3.11 recommended (3.8+ minimum).
- **Check:** `python3 --version`

---

## Core dependencies (Units 1–2)

Install once before Unit 1:

```bash
pip install numpy matplotlib scikit-learn joblib
pip install torch torchvision
pip install onnx onnxruntime
pip install fastapi uvicorn
pip install flask
```

---

## Unit-specific (install when you reach the unit)

**Unit 3 — Cloud (optional for local run):** notebooks use **simulated** cloud patterns where possible. For live cloud labs, your instructor provides credentials.

```bash
pip install boto3          # AWS examples
# Azure / GCP: follow instructor sandbox instructions
```

**Unit 4 — Containers:** Docker Desktop (or compatible runtime) for hands-on Dockerfile cells.

**Unit 5 — MLOps:**

```bash
pip install mlflow
```

---

## Verify setup

```python
import numpy, sklearn, torch, onnxruntime, fastapi
print("numpy", numpy.__version__)
print("torch", torch.__version__)
print("sklearn OK")
```

---

## Notebook order

Always follow **numbered** notebooks (`01`, `02`, …) listed in each unit `README.md` and `DOCS/EXAMPLES_ORDER.md`.

Do **not** use long descriptive filenames in `DOCS/REFERENCE_NOTEBOOKS/` unless assigned.

---

## Troubleshooting

| Problem | What to try |
| -------- | ------------- |
| `ModuleNotFoundError` | Re-run the first `%pip install` cell, then restart kernel |
| Stale variables / weird plots | **Kernel → Restart & Run All** |
| ONNX export fails | Confirm `torch` and `onnx` versions; re-run model training cell |
| Cloud cell asks for keys | Expected without instructor credentials — read markdown callout; simulation cells still run locally |

See also: `../START_HERE.md`, `DEPLOYMENT_LEARNING_JOURNEY.md`.
