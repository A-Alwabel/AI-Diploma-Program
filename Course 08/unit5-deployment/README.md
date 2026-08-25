# Unit 5 — Model Optimization and Deployment
## AIAT 122 — Deep Learning

Unit training hours: 14 (of 64 total)

## Prerequisites

- Units 1–4 (training and evaluating models; saving/loading models).
- Environment set up (see `../START_HERE.md`): "ai-diploma" kernel for PyTorch notebooks, "tfenv" kernel for TensorFlow notebooks.

## What this unit teaches

Making trained models smaller, faster, and servable: quantization, pruning, and knowledge distillation; exporting to interchange formats (ONNX); and serving models behind an API (TensorFlow Serving concepts, Flask/FastAPI).

## Examples (do in file order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

Run the notebooks in `examples/` in this order:

1. **[CORE]** `01_model_optimization.ipynb` — why and how to optimize models for deployment; overview of the techniques.
2. **[HOMEWORK]** `02_tensorflow_serving.ipynb` — model-server concepts: export a model and serve predictions.
3. **[CORE]** `03_onnx_conversion.ipynb` — convert a model to ONNX and run it with ONNX Runtime.
4. **[HOMEWORK]** `04_model_pruning.ipynb` — remove low-importance weights and measure the size/accuracy trade-off.
5. **[HOMEWORK]** `05_model_distillation.ipynb` — train a small student model from a large teacher.
6. **[CORE]** `06_flask_fastapi_deployment.ipynb` — wrap a model in a REST API with Flask/FastAPI.
7. **[CORE]** `07_model_optimization_quantization.ipynb` — quantize a model and compare size, speed, and accuracy.

The `simple_model.onnx` / `simple_model.onnx.data` files in `examples/` are sample artifacts used by the ONNX notebooks.

## Exercise

- `exercises/01_deep_learning_model_deployment_exercise.ipynb` — optimize and deploy a trained model (export and/or API). `exercises/app.py` is a supporting API script for this exercise. Solutions are released by your instructor.

## Quiz

- `../QUIZZES/quiz_05.md`

## Next

Course assessments: `../ASSESSMENTS/README.md`
