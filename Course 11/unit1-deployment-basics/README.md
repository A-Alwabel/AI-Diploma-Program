# Unit 1: Introduction to AI Model Deployment

Folder: `unit1-deployment-basics/` · **Unit hours:** 18

## Where this unit sits in the course

You are at the foundation: saving models, exposing them through APIs, testing locally, and validating before anything reaches production. Read [`../DEPLOYMENT_LEARNING_JOURNEY.md`](../DEPLOYMENT_LEARNING_JOURNEY.md) for how Units 1–5 connect.

## Before you start

- [`../START_HERE.md`](../START_HERE.md) environment setup complete (repo-root `.venv`, "ai-diploma" kernel)
- AIAT 122 — Deep Learning (Course 08) or equivalent: train and save a small sklearn/PyTorch model

## Learning goals

- Explain the deployment lifecycle (train → package → serve → monitor)
- Serialize models with pickle/joblib and understand trade-offs
- Sketch REST APIs for inference (Flask/FastAPI patterns)
- Test a model service locally and run basic validation checks

## Study order (required)

1. `examples/01_model_serving_api.ipynb` — REST API concepts and local model serving
2. `examples/02_model_packaging.ipynb` — pickle and joblib packaging
3. `examples/03_local_deployment_testing.ipynb` — local test harness for a model service
4. `examples/04_model_preparation_saving.ipynb` — preparing artifacts for deployment
5. `examples/05_model_validation_testing.ipynb` — pre-deployment validation checks
6. `examples/06_monitoring_updating_models.ipynb` — logs, feedback, and model updates

## Exercise and quiz

1. `exercises/01_packaging_exercise.ipynb` (solution released by your instructor)
2. `../QUIZZES/quiz_01.md`
