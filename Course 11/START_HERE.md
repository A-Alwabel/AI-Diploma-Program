# START HERE! | ابدأ من هنا!

## 👋 Welcome! | مرحباً!

This course is part of Semester 2 of the AI Diploma Program.

**✅ Official Path:** Follow the unit folders in order (Unit 1 → Unit 5).  
**📚 Official unit structure:** See **README.md** (Unit ↔ Folder mapping) and `../DETAILED_UNIT_DESCRIPTIONS.md` for learning outcomes per unit.

---

## 🚀 Student Quick Start (3 steps)

1. **Read README.md** — Course overview, unit mapping, and what you'll learn.
2. **Set up your environment** — Install dependencies below. For free GPU: use **Google Colab**.
3. **Start Unit 1** — Open `unit1-deployment-basics/README.md` and do the example notebooks in file order (01, 02, 03, …).

### Required packages

```bash
pip install numpy matplotlib
pip install torch torchvision        # PyTorch (model serialization and ONNX)
pip install onnx onnxruntime         # ONNX model export and inference
pip install fastapi uvicorn          # REST API deployment (Unit 2)
pip install scikit-learn
```

For cloud deployment units (Unit 3), additional cloud SDKs may be needed:
```bash
pip install boto3                    # AWS (Unit 3 - SageMaker)
pip install mlflow                   # MLOps tracking (Unit 4)
```

### Verify setup

```python
import torch, onnxruntime, fastapi
print("PyTorch:", torch.__version__)
print("ONNXRuntime:", onnxruntime.__version__)
```

---

## 📋 Prerequisites | المتطلبات الأساسية

**Before starting this course, you must have completed:**
- All Semester 1 courses (AIAT 111–116)
- Course 08 — Deep Learning (model training and PyTorch)
- Course 09 or 10 (recommended background in model development)

---

## 📚 Learning Path | مسار التعلم

1. **Read README.md** — Understand course overview and goals.
2. **Review prerequisites** — Make sure you can train a model and save it with PyTorch.
3. **Start with Unit 1** — Deployment Basics: model serialization (Pickle, ONNX), local testing.
4. **Unit 2** — Model Packaging and Serving: REST APIs with Flask/FastAPI, gRPC.
5. **Unit 3** — Cloud Deployment: AWS SageMaker, Lambda, GCP Vertex AI, Azure ML.
6. **Unit 4** — Containers and Orchestration: Docker, Kubernetes, CI/CD pipelines.
7. **Unit 5** — Monitoring, Maintenance, and MLOps: drift detection, retraining, A/B testing, MLflow.
8. **Complete exercises** — Practice what you learn in each unit.
9. **Take quizzes** — Test your understanding after each unit.

**📌 Notebook order:** In each unit, do the example notebooks in **file order** (01, 02, 03, …). Always use the order shown in each unit's README, not slide numbers.

**❓ If a notebook isn't clear:** Open `DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md` (if available) or ask your instructor.

---

## ✅ Progress Tracking | تتبع التقدم

Use `STUDENT_PROGRESS_CHECKLIST.md` to track your progress through all 5 units.

---

**Ready to begin?** Read the course README.md first!
