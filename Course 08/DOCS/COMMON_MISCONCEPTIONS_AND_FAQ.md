# Course 08 – Common Misconceptions and FAQ
## For instructors and students

---

## Common misconceptions (with short corrections)

### 1. "Deep learning always beats traditional ML."

**Correction:** Deep learning excels when we have **lots of data** and **raw, high-dimensional signals** (images, text, audio). For **tabular data**, small datasets, or when we already have good hand-crafted features, traditional ML (e.g. random forest, XGBoost) is often better or simpler. Choose by problem and data.

### 2. "More layers always mean better performance."

**Correction:** Deeper networks can overfit and be harder to train (vanishing gradients). We use depth when the task benefits from hierarchical features; we also use regularization (dropout, batch norm), early stopping, and enough data. "More layers" without proper training or data often hurts.

### 3. "Attention replaces RNNs everywhere."

**Correction:** Transformers (attention) have replaced RNNs in many NLP and some vision tasks, but RNNs/LSTMs are still used when we need **streaming** or **strict left-to-right** processing, or when data/compute are limited. Each has trade-offs (parallelism vs recurrence, cost vs length).

### 4. "Quantization always hurts accuracy a lot."

**Correction:** With **calibration** (e.g. representative data), int8 or FP16 quantization often gives **minimal accuracy loss** (e.g. &lt;1%) while reducing size and speeding up inference. "Always hurts a lot" is wrong; we measure on a validation set after quantization.

### 5. "Transfer learning means we don't need to train anything."

**Correction:** We still **fine-tune** (train) the top layers or more on our task; we may freeze earlier layers. Transfer learning reduces the amount of data and training time we need; it does not remove training.

### 6. "If overall accuracy is high, the model is fair."

**Correction:** A model can have high overall accuracy but **poor performance for some groups** (e.g. by demographic). We need to evaluate **fairness** (e.g. accuracy by group, equalized odds) and mitigate bias in data and model.

### 7. "GANs are the only way to generate images."

**Correction:** VAEs, diffusion models, and autoregressive models (e.g. PixelCNN) also generate images. GANs are one approach; choice depends on stability, diversity, and use case.

### 8. "Backpropagation is only used in deep learning."

**Correction:** Backpropagation is the algorithm to compute gradients in any differentiable computation graph; it is used in deep learning, but the idea applies wherever we use gradient-based optimization (e.g. some classical ML with neural nets).

---

## FAQ

### Is this course TensorFlow or PyTorch?

Course 08 uses **both** where relevant. Many examples are in **TensorFlow/Keras**; some (e.g. BERT, transformers) use **PyTorch** (Hugging Face). Students should be able to read both; emphasize one if your institution standardizes.

### Why is Unit 5 not in the institution slides?

The 23 institution slides cover Units 1–4. **Unit 5 (deployment)** is only in the course materials (notebooks, README). Teach Unit 5 from the Unit 5 notebooks and README. See `DOCS/INSTITUTION_SLIDES_COMPATIBILITY.md`.

### Where do students get a GPU?

**Google Colab** (free tier) is the main option; see `DOCS/COLAB_SETUP.md`. Kaggle notebooks also offer free GPU. Local GPU requires NVIDIA + CUDA and appropriate TensorFlow/PyTorch installs.

### Can students use a different dataset for the project?

Yes, as long as it is **allowed** (public, no license violations) and fits the task (image classification). The project README suggests CIFAR-10, Kaggle datasets, etc. Specify any restrictions (e.g. no medical data from non-public sources) in your syllabus.

### What if TensorFlow fails with charset_normalizer or md__mypyc?

This is an environment issue. Have students run:  
`pip install --upgrade charset-normalizer requests`  
Then **restart the Jupyter/Colab kernel** and run the imports again. See `DOCS/COLAB_SETUP.md`.

### Where are quiz and exercise solutions?

- **Quiz solutions:** `DOCS/SOLUTIONS/quizzes/` (instructor use; do not post before quiz deadline).  
- **Exercise solutions:** `DOCS/SOLUTIONS/exercises/` (instructor use; do not distribute before exercise deadline).  
See `DOCS/INSTRUCTOR_RUNBOOK.md`.

### How do I grade the case study and project?

Use the rubrics:  
- **Case study:** `CASE_STUDIES/case_study_01_rubric.md`.  
- **Project 01:** `PROJECTS/Image_Classification_System/RUBRIC.md`.  
Model answers: case study in `DOCS/SOLUTIONS/case_study_01_sample_solution.md`; project expectations in project README.

---

**Last updated:** 2025-02-07
