# START HERE

## Welcome

This is **AIAT 125 — Deploying AI Models**, part of Semester 2 of the AI Diploma Program.

**Credit hours:** 4 · **Contact hours:** 6/week · **Total training hours:** 96 (theory+practical)

---

## Prerequisites

Before starting this course, you should have completed:

- Semester 1 (AIAT 111–116)
- AIAT 122 — Deep Learning (Course 08): train and save models with PyTorch
- Familiarity with basic Python APIs and the command line

---

## Setup

1. Use the repository-root virtual environment (`.venv`) and select the **"ai-diploma"** Jupyter kernel when running notebooks.
2. Install the course packages into that environment:

```bash
cd "Course 11"
pip install -r requirements-course11.txt
```

See [`DOCS/REQUIREMENTS_COURSE_11.md`](DOCS/REQUIREMENTS_COURSE_11.md) for unit-by-unit optional packages (cloud SDKs, Docker, MLflow).

One notebook uses TensorFlow: `unit2-versioning-serving/examples/05_tensorflow_serving_torchserve.ipynb`. Run that notebook on the **"tfenv"** kernel; everything else runs on "ai-diploma".

### Verify setup

```python
import torch, onnxruntime, fastapi, sklearn
print("PyTorch:", torch.__version__)
print("ONNX Runtime:", onnxruntime.__version__)
print("FastAPI:", fastapi.__version__)
```

---

## Study Path

Follow this single numbered path:

1. Read [`README.md`](README.md) and skim [`DEPLOYMENT_LEARNING_JOURNEY.md`](DEPLOYMENT_LEARNING_JOURNEY.md).
2. **Unit 1 — Introduction to AI Model Deployment** ([`unit1-deployment-basics/`](unit1-deployment-basics/README.md))
3. **Unit 2 — Model Packaging and Serving** ([`unit2-versioning-serving/`](unit2-versioning-serving/README.md))
4. **Unit 3 — Cloud Deployment and Infrastructure** ([`unit3-cloud-deployment/`](unit3-cloud-deployment/README.md))
5. **Unit 4 — Containers and Orchestration** ([`unit4-containers-orchestration/`](unit4-containers-orchestration/README.md))
6. **Unit 5 — Monitoring and Maintenance of Deployed AI Models** ([`unit5-pipelines-monitoring/`](unit5-pipelines-monitoring/README.md))
7. **Course practical:** [`final_exercise.ipynb`](final_exercise.ipynb) — graded, 100 points, covers all six CLOs. Its solution is released by your instructor.
8. **Final exam:** [`ASSESSMENTS/Final_Exam.md`](ASSESSMENTS/Final_Exam.md)

In each unit: read the `README.md`, run the numbered `examples/` notebooks in file order (`01`, `02`, …), complete the `exercises/` notebook, then take the unit quiz in [`QUIZZES/`](QUIZZES/README.md).

**If a notebook runs but still feels confusing:** open [`DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md`](DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md).

Each example notebook ends with a short **Self-check** section — use it before moving on.

---

## Progress Tracking

Use [`STUDENT_PROGRESS_CHECKLIST.md`](STUDENT_PROGRESS_CHECKLIST.md) to track completion.

---

**Ready?** Open [`unit1-deployment-basics/README.md`](unit1-deployment-basics/README.md) and start with `examples/01_model_serving_api.ipynb`.
