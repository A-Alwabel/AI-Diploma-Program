# Unit 1: Deployment Basics

## Where this unit sits in the course

You are at the **foundation**: saving models, exposing them through APIs, testing locally, and validating before anything reaches production. Read [`../DEPLOYMENT_LEARNING_JOURNEY.md`](../DEPLOYMENT_LEARNING_JOURNEY.md) for how Units 1–5 connect.

## Before you start

- Python 3.10+ and `pip` working
- Course 08 (or equivalent): train and save a small sklearn/PyTorch model
- [`../START_HERE.md`](../START_HERE.md) environment setup complete

## Learning goals

- Explain the deployment lifecycle (train → package → serve → monitor)
- Serialize models with pickle/joblib and understand trade-offs
- Sketch REST APIs for inference (Flask/FastAPI patterns)
- Test a model service locally and run basic validation checks

## Study order (required)

1. `examples/01_model_serving_api.ipynb`
2. `examples/02_model_packaging.ipynb`
3. `examples/03_local_deployment_testing.ipynb`
4. `examples/04_model_preparation_saving.ipynb`
5. `examples/05_model_validation_testing.ipynb`
6. `examples/06_monitoring_updating_models.ipynb`

### Reference notebooks

Supplemental long-filename notebooks live under `../DOCS/REFERENCE_NOTEBOOKS/unit1-deployment-basics/examples/`. They are **not** the main student path unless your instructor assigns one.

## Exercise and quiz

1. `exercises/01_packaging_exercise.ipynb`
2. `../QUIZZES/quiz_01.md`

**Unit duration:** ~2 weeks | **Difficulty:** Intermediate
