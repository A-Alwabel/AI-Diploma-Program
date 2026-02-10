# Unit 1: Deep Learning Basics

## ✅ Prerequisites Checklist

Before starting this unit, confirm:

- [ ] Completed Course 03 Units 1-2 (Linear Algebra & Calculus)
- [ ] Completed Course 04 (Machine Learning) recommended
- [ ] Comfortable with Python and NumPy
- [ ] Installed required libraries (`pip check` passes)
- [ ] Reviewed related topics (see course README and DOCS/EXAMPLES_ORDER.md; COURSE_MAP if available in your repo)

### Learning Objectives

By the end of this unit, students will be able to:
- Understand deep learning fundamentals
- Build neural networks using TensorFlow/Keras
- Understand backpropagation
- Train and evaluate deep learning models
- Apply deep learning to classification problems

---

## Topics Covered

1. **Deep Learning Introduction**
   - What is deep learning?
   - Neural network architecture
   - Layers and neurons
   - Activation functions

2. **Building Neural Networks**
   - Using TensorFlow/Keras
   - Sequential models
   - Dense layers
   - Model compilation

3. **Training Neural Networks**
   - Loss functions
   - Optimizers
   - Training process
   - Validation

4. **Model Evaluation**
   - Metrics (accuracy, loss)
   - Overfitting and underfitting
   - Model improvement

---

## Recommended order (examples)

Follow this order to align with slides **08 → 01 → 02 → 06 → 19 → 23**. Full table: `DOCS/EXAMPLES_ORDER.md`.

1. `01_deep_learning_fundamentals_compared_to_traditional_ml.ipynb`  
2. `02_simple_neural_network.ipynb`  
3. `03_perceptron_mlp_tensorflow_pytorch_setup.ipynb`  
4. `04_activation_functions_and_optimization_algorithms.ipynb`  
5. `05_backpropagation_detailed.ipynb`  
6. `06_optimization_techniques.ipynb`  

*Optional (do after the core 01–06; order between them doesn't matter):* `07_image_processing_feature_extraction.ipynb`, `08_forward_and_backward_propagation.ipynb`  

---

## Exercises

Complete the exercise in `unit1-deep-learning-basics/exercises/`:

1. **`01_neural_network_exercise.ipynb`** – Medical image classification (data preprocessing, model architecture, training). Aligns with examples `01_deep_learning_fundamentals_*`, `02_simple_neural_network.ipynb`.

**Solutions:** See `DOCS/SOLUTIONS/exercises/` (instructor-only; do not distribute before deadline).

---

## Teaching note (instructors)

- **Suggested time:** Core examples 01–06: ~2 hours total in lab; optional 07–08: +30 min. Theory (slides): ~6 hours.
- **Demo notebook:** `02_simple_neural_network.ipynb` – run training cell and show loss/accuracy curve and sample predictions.
- **Common stumbling block:** TensorFlow `charset_normalizer` / `md__mypyc` error on import – see `DOCS/COLAB_SETUP.md` (pip upgrade + restart kernel).
- **Exercise alignment:** `01_neural_network_exercise` builds on 01_deep_learning_fundamentals and 02_simple_neural_network.

---

**Unit Duration:** 2 weeks  
**Difficulty:** Advanced  
**Prerequisites:** Completion of Semester 1 courses, understanding of neural networks basics
