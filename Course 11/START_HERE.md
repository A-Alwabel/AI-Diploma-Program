# START HERE!

## Welcome

This course is part of Semester 2 of the AI Diploma Program.

**Official path:** Follow the unit folders in order (Unit 1 → Unit 5).  
**Notebook order:** See [`DOCS/EXAMPLES_ORDER.md`](DOCS/EXAMPLES_ORDER.md) and each unit `README.md`.

---

## Student Quick Start (3 steps)

1. **Read [`README.md`](README.md)** — Course overview, unit mapping, and outcomes.
2. **Set up your environment** — Follow **`DOCS/REQUIREMENTS_COURSE_11.md`** (or `pip install -r requirements-course11.txt` from this folder).
3. **Start Unit 1** — Open `unit1-deployment-basics/README.md` and run example notebooks **01 → 06** in order.

### Quick install

```bash
cd "Course 11"
pip install -r requirements-course11.txt
```

See **`DOCS/REQUIREMENTS_COURSE_11.md`** for unit-by-unit optional packages (cloud, Docker, MLflow).

### Verify setup

```python
import torch, onnxruntime, fastapi, sklearn
print("PyTorch:", torch.__version__)
print("ONNX Runtime:", onnxruntime.__version__)
print("FastAPI:", fastapi.__version__)
```

---

## Prerequisites

**Before starting this course, you should have completed:**

- Semester 1 courses (AIAT 111–116)
- **Course 08** — Deep Learning (train and save models with PyTorch)
- Familiarity with basic Python APIs and the command line

---

## Learning Path

1. Read [`README.md`](README.md) and skim [`DEPLOYMENT_LEARNING_JOURNEY.md`](DEPLOYMENT_LEARNING_JOURNEY.md).
2. **Unit 1** — Package models, build APIs, test locally.
3. **Unit 2** — Versioning, FastAPI/Flask serving, batch vs real-time.
4. **Unit 3** — Cloud platforms (AWS, Azure, GCP), security, logging.
5. **Unit 4** — Docker, Kubernetes, CI/CD.
6. **Unit 5** — Monitoring, drift, retraining, experiment tracking, A/B deploy.
7. Complete exercises and quizzes per unit.
8. Finish the course project and final exam.

**Notebook order:** In each unit, follow **numbered** notebooks only (`01`, `02`, …). Do not use long descriptive filenames in `examples/` unless assigned—they are archived under `DOCS/REFERENCE_NOTEBOOKS/`.

**If a notebook runs but still feels confusing:** Open **`DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md`**.

Each example notebook ends with a short **Did you understand?** checklist—use it before moving on.

---

## Progress Tracking

Use [`STUDENT_PROGRESS_CHECKLIST.md`](STUDENT_PROGRESS_CHECKLIST.md) to track completion.

---

**Ready?** Open [`unit1-deployment-basics/README.md`](unit1-deployment-basics/README.md) and start with `examples/01_model_serving_api.ipynb`.
