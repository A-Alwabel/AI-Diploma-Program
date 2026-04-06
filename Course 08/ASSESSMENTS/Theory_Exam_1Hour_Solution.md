# Theory Exam: Deep Learning
## Model Answers

Use with `Theory_Exam_1Hour.md`.

---

## Part A: Multiple Choice Answer Key

1. **B**
2. **B**
3. **A**
4. **B**
5. **B**
6. **B**
7. **A**
8. **B**
9. **B**
10. **B**

---

## Part B: Short Answer Model Answers

### Question 11
- **Convolution:** Applies learnable filters to detect local
  features such as edges, textures, and shapes.
- **Pooling:** Reduces spatial dimensions, lowers computation,
  and keeps the most important information.
- **Fully connected layers:** Combine extracted features and
  produce the final class prediction.

### Question 12
- **RNN:** Strength: simple sequence modeling. Limitation:
  struggles with long-term dependencies because of vanishing
  gradients.
- **LSTM:** Strength: gating helps preserve useful information
  over longer sequences. Limitation: still processes step by
  step, so training is slower.
- **Transformer:** Strength: self-attention captures long-range
  relationships and supports parallel processing. Limitation:
  usually needs more data and compute.

### Question 13
- Two valid optimization techniques: **quantization**,
  **pruning**, or **distillation**.
- One likely trade-off: small loss in accuracy or model quality
  after compression.
- One valid deployment option: **FastAPI**, **Flask**,
  **ONNX Runtime**, or **TensorFlow Serving**.

### Question 14
- Ethical problem: **bias / unfair performance across groups**.
- Two actions:
  - collect or balance more representative data
  - evaluate metrics separately by subgroup
  - apply fairness-aware validation and monitoring
  - review labels and data collection process for bias
- One interpretability method or idea:
  - **Grad-CAM**
  - **attention visualization**
  - **SHAP**
  - confidence reporting with human review

---

## Suggested Marking Guide

### Question 11 (5 pts)
- 2 pts: convolution explained correctly
- 1.5 pts: pooling explained correctly
- 1.5 pts: fully connected layer explained correctly

### Question 12 (5 pts)
- 2 pts: correct comparison of architectures
- 1.5 pts: strengths are valid
- 1.5 pts: limitations are valid

### Question 13 (5 pts)
- 2 pts: two correct optimization techniques
- 1 pt: one realistic trade-off
- 2 pts: one valid deployment option

### Question 14 (5 pts)
- 1 pt: identifies bias/fairness issue
- 2 pts: two sensible mitigation actions
- 2 pts: one valid interpretability method or trust-building measure
