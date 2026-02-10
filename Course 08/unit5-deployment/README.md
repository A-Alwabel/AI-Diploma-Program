# Unit 5: Deploying Deep Learning Models
## AIAT 122 - Deep Learning

## ✅ Prerequisites Checklist

Before starting this unit, confirm:

- [ ] Completed Units 1-4 in this course
- [ ] Comfortable with model evaluation and saving models
- [ ] Recommended: Course 11 (Deployment) for full coverage
- [ ] Installed required libraries (`pip check` passes)
- [ ] Reviewed related topics (see course README and DOCS/EXAMPLES_ORDER.md; COURSE_MAP if available in your repo)

### Learning Objectives

By the end of this unit, students will be able to:
- Optimize deep learning models for deployment
- Convert models to production-ready formats
- Deploy models using various frameworks
- Monitor and maintain deployed models
- Implement model versioning and updates

---

## Topics Covered

Based on official curriculum (AIAT 122), this unit covers:

1. **Model Optimization**
   - Model quantization
   - Pruning techniques
   - Knowledge distillation
   - Model compression
   - ONNX conversion

2. **Deployment Strategies**
   - Batch inference
   - Real-time inference
   - Edge deployment
   - Cloud deployment
   - Hybrid approaches

3. **Deployment Frameworks**
   - TensorFlow Serving
   - TorchServe
   - ONNX Runtime
   - TensorRT
   - CoreML (for iOS)

4. **Model Serving**
   - REST APIs for models
   - gRPC for model serving
   - Model caching
   - Load balancing
   - Auto-scaling

5. **Monitoring and Maintenance**
   - Model performance monitoring
   - Drift detection
   - A/B testing
   - Model versioning
   - Continuous integration

---

## Recommended order (examples)

Unit 5 has no institution slides. Use examples in numerical order. Full table: `DOCS/EXAMPLES_ORDER.md`.

1. `01_model_optimization.ipynb`  
2. `02_tensorflow_serving.ipynb`  
3. `03_onnx_conversion.ipynb`  
4. `04_model_pruning.ipynb`  
5. `05_model_distillation.ipynb`  
6. `06_flask_fastapi_deployment.ipynb`  
7. `07_model_optimization_quantization.ipynb`  

---

## Exercises

Complete the exercise in `unit5-deployment/exercises/`:

1. **`01_deep_learning_model_deployment_exercise.ipynb`** – Deploy a model (e.g. API or export). Aligns with `01_model_optimization.ipynb`, `06_flask_fastapi_deployment.ipynb`.

**Solutions:** See `DOCS/SOLUTIONS/exercises/` (instructor-only; do not distribute before deadline).

---

## Teaching note (instructors)

- **Suggested time:** Examples 01–07: ~2–2.5 hours. Unit 5 has no institution slides; use notebooks only (~7 theory + 13 practical hours).
- **Demo notebook:** `06_flask_fastapi_deployment.ipynb` – show defining the API and a test request.
- **Common stumbling block:** TensorFlow Serving / Docker if not familiar; focus on 01, 03, 06, 07 for core optimization + API.
- **Exercise alignment:** Deployment exercise with 01_model_optimization and 06_flask_fastapi_deployment.

---

## Unit Breakdown

**Theoretical Hours:** 7  
**Practical Hours:** 13  
**Total Hours:** 20

### Theoretical Content

- Model optimization techniques
- Deployment architectures
- Serving frameworks comparison
- Monitoring strategies
- Production best practices

### Practical Content

- Quantizing a TensorFlow model
- Deploying with TensorFlow Serving
- Creating REST API for model inference
- Setting up model monitoring
- Implementing model versioning

---

**Unit Duration:** 3 weeks  
**Difficulty:** Advanced  
**Prerequisites:** Units 1-4 completion

**Created for:** AIAT 122 - Deep Learning  
**Last Updated:** 2025-01-10

