# Unit 3: AI Concepts, Terminology, and Application Domains Part 2

**Course:** AIAT 111 · **Unit hours:** 12 (6 theory + 6 practical)

Core machine learning concepts continued: regression vs classification, then the neuron and perceptron, the XOR problem, solving it with a small neural network in Keras, how models actually learn (gradient descent and loss functions), and explaining model predictions with SHAP and LIME.

This unit works at intuition level: the math behind gradient descent (derivatives, calculus) arrives in Course 03 (AIAT 113), and the full training mechanics in Course 08 (AIAT 122, Deep Learning).

**Prerequisites:** Unit 2 (`../unit2-ai-concepts/README.md`).

**Kernels:** notebooks 01, 04, and 05 run on the `ai-diploma` kernel; notebooks 02 and 03 use TensorFlow/Keras and run on the `tfenv` kernel (see `../START_HERE.md`).

---

## Notebooks (run in order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

| # | Notebook | What it covers | Tier |
|---|----------|----------------|------|
| 01 | `examples/01_regression_classification.ipynb` | Regression vs classification | **HOMEWORK** |
| 02 | `examples/02_perceptron_xor.ipynb` | The neuron, the perceptron, and why XOR is hard (`tfenv` kernel) | **CORE** |
| 03 | `examples/03_solving_xor_keras.ipynb` | Solving XOR with a neural network in Keras (`tfenv` kernel) | **CORE** |
| 04 | `examples/04_gradient_descent_loss_functions.ipynb` | How models learn: loss functions and gradient descent, implemented from scratch | **HOMEWORK** |
| 05 | `examples/05_model_interpretability_shap_lime.ipynb` | Explaining model predictions with SHAP and LIME | **HOMEWORK** |

---

## After the Notebooks

1. **Exercise:** `exercises/exercise_01.ipynb` — regression vs classification, XOR and feature engineering, gradient descent by hand, and feature importances (`ai-diploma` kernel). Solutions are released by your instructor.
2. **Quiz:** `quizzes/quiz_03.md`

Then continue to Unit 4: `../unit4-neural-networks-basics/README.md`.
