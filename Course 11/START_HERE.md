# START HERE

## Welcome

This is **AIAT 125 — Deploying AI Models**, part of Semester 2 of the AI Diploma Program.

**Credit hours:** 4 · **Contact hours:** 6/week · **Total training hours:** 96 (theory+practical)

---

## Prerequisites

Before starting this course, you should have completed:

- Semester 1 (AIAT 111–116)
- AIAT 114 — Machine Learning Algorithms (Course 04): train and evaluate classifiers
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

3. **Bring your model.** This course deploys the classifier *you* trained in AIAT 114 or
   AIAT 122, not a demo model invented here. Follow
   [`PORTFOLIO_MODEL.md`](PORTFOLIO_MODEL.md) to export it — one cell added to the end of
   the notebook that trained it. If you skip this step nothing breaks: the notebooks
   build a named fallback model and print, in their own output, that they are serving it
   instead of your work.

### Verify setup

```python
import torch, onnxruntime, fastapi, sklearn
print("PyTorch:", torch.__version__)
print("ONNX Runtime:", onnxruntime.__version__)
print("FastAPI:", fastapi.__version__)
```

Then check which model this course will deploy for you — run this from the `Course 11`
folder:

```python
import portfolio_model as pf
model, card = pf.load_portfolio_model()
```

It prints either `YOUR PORTFOLIO MODEL '<name>'` or `FALLBACK MODEL 'wdbc-baseline'`.
If you see the fallback and did not expect it, re-read [`PORTFOLIO_MODEL.md`](PORTFOLIO_MODEL.md).

---

## Study Path

Follow this single numbered path:

1. Read [`README.md`](README.md) and skim [`DEPLOYMENT_LEARNING_JOURNEY.md`](DEPLOYMENT_LEARNING_JOURNEY.md).
2. Export your portfolio model — [`PORTFOLIO_MODEL.md`](PORTFOLIO_MODEL.md). Do this before Unit 1; every serving notebook reads it.
3. **Unit 1 — Introduction to AI Model Deployment** ([`unit1-deployment-basics/`](unit1-deployment-basics/README.md))
4. **Unit 2 — Model Packaging and Serving** ([`unit2-versioning-serving/`](unit2-versioning-serving/README.md))
5. **Unit 3 — Cloud Deployment and Infrastructure** ([`unit3-cloud-deployment/`](unit3-cloud-deployment/README.md))
6. **Unit 4 — Containers and Orchestration** ([`unit4-containers-orchestration/`](unit4-containers-orchestration/README.md))
7. **Unit 5 — Monitoring and Maintenance of Deployed AI Models** ([`unit5-pipelines-monitoring/`](unit5-pipelines-monitoring/README.md))
8. **Course practical:** [`final_exercise.ipynb`](final_exercise.ipynb) — graded, 100 points, covers all six CLOs. Its solution is released by your instructor.
9. **Final exam:** [`ASSESSMENTS/Final_Exam.md`](ASSESSMENTS/Final_Exam.md)

In each unit: read the `README.md`, run the numbered `examples/` notebooks in file order (`01`, `02`, …), complete the `exercises/` notebook, then take the unit quiz in [`QUIZZES/`](QUIZZES/README.md).

**If a notebook runs but still feels confusing:** open [`DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md`](DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md).

Each example notebook ends with a short **Self-check** section — use it before moving on.

---

## Progress Tracking

Use [`STUDENT_PROGRESS_CHECKLIST.md`](STUDENT_PROGRESS_CHECKLIST.md) to track completion.

---

**Ready?** Open [`unit1-deployment-basics/README.md`](unit1-deployment-basics/README.md) and start with `examples/01_model_serving_api.ipynb`.
