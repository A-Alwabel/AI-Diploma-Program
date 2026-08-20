# Unit 2: Model Packaging and Serving

Folder: `unit2-versioning-serving/` (official unit name: **Model Packaging and Serving**) · **Unit hours:** 19

## Where this unit sits in the course

Unit 1 showed local packaging and APIs. Here you deepen serving: versioning, multiple frameworks, and batch vs real-time inference.

## Prerequisites

- Unit 1 complete
- FastAPI and Flask installed ([`../START_HERE.md`](../START_HERE.md))

## Learning goals

- Version models and record metadata for rollback
- Serve with Flask and FastAPI
- Compare pickle, ONNX, and framework-specific formats
- Contrast batch and real-time inference paths
- Understand scaling concepts (Kubernetes intro)

## Study order (required)

1. `examples/01_flask_api_deployment.ipynb` — serving a model with Flask
2. `examples/02_fastapi_deployment.ipynb` — serving a model with FastAPI
3. `examples/03_model_versioning.ipynb` — version numbering, metadata, rollback
4. `examples/04_saving_loading_models_pickle_onnx.ipynb` — serialization formats compared
5. `examples/05_tensorflow_serving_torchserve.ipynb` — serving frameworks (TensorFlow Serving, TorchServe). **Run this notebook on the "tfenv" kernel** — it imports TensorFlow.
6. `examples/06_batch_vs_realtime_inference.ipynb` — batch vs real-time inference paths
7. `examples/07_kubernetes_scaling.ipynb` — scaling served models (Kubernetes concepts)

## Exercise and quiz

1. `exercises/01_api_deployment_exercise.ipynb` (solution released by your instructor)
2. `../QUIZZES/quiz_02.md`
