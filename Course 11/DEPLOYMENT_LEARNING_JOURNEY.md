# Deployment Learning Journey (AIAT 125)

This page is a **single narrative map** for the whole course. The numbered notebooks in each unit are the real lessons; this file answers: *where am I, what did I just gain, and what comes next?*

## The through-line (one sentence per stage)

| Stage | You can now… |
| ----- | -------------- |
| **Package & serve** | Save a trained model, expose it through an API, and test it locally before anyone depends on it. |
| **Version & scale serving** | Track model versions, compare batch vs real-time inference, and use serving frameworks. |
| **Cloud deploy** | Place models on managed cloud platforms with security and logging in mind. |
| **Containers & CI/CD** | Reproduce environments with Docker/Kubernetes and automate delivery pipelines. |
| **MLOps** | Monitor drift, retrain, run experiments, and compare models in production-style workflows. |

## Units 1–5 in order

| Unit | Folder | Carries forward… |
| ---- | ------ | ------------------ |
| **1** | [`unit1-deployment-basics/`](unit1-deployment-basics/README.md) | Serialization, REST APIs, local testing, validation, basic monitoring. |
| **2** | [`unit2-versioning-serving/`](unit2-versioning-serving/README.md) | Flask/FastAPI serving, ONNX/pickle formats, TorchServe concepts, batch vs real-time. |
| **3** | [`unit3-cloud-deployment/`](unit3-cloud-deployment/README.md) | AWS / Azure / GCP deployment patterns, cloud security, cloud logging. |
| **4** | [`unit4-containers-orchestration/`](unit4-containers-orchestration/README.md) | Docker images, Kubernetes rollout, CI/CD for models. |
| **5** | [`unit5-pipelines-monitoring/`](unit5-pipelines-monitoring/README.md) | Drift detection, retraining, MLflow-style tracking, A/B and canary releases. |

## Reuse the same mental checklist everywhere

Whatever notebook you open, ask:

1. **Artifact** — What file format leaves training (PyTorch state dict, pickle, ONNX)?
2. **Interface** — How does a client send features and read predictions?
3. **Environment** — What libraries and OS packages must match at runtime?
4. **Observability** — What would you log if predictions started failing in production?
5. **Rollback** — Which older model version could you switch back to safely?

## Close the loop

- **Per unit:** `README.md` → numbered `examples/` → `exercises/` → `QUIZZES/quiz_0N.md`
- **Whole course:** [`START_HERE.md`](START_HERE.md) → Units 1–5 → [`final_exercise.ipynb`](final_exercise.ipynb) → [`ASSESSMENTS/Final_Exam.md`](ASSESSMENTS/Final_Exam.md)
- **Progress:** [`STUDENT_PROGRESS_CHECKLIST.md`](STUDENT_PROGRESS_CHECKLIST.md)

Skim this journey page **once at the start** and **once before the final exercise** so the course feels like one story, not five disconnected folders.
