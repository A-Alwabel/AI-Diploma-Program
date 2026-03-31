# Case Study 01: Deep Learning Deployment
## Course 08 – AIAT 122

**Type:** Case Study Analysis  
**Points:** 100 points  
**Rubric:** See `CASE_STUDIES/case_study_01_rubric.md`

---

## Case Study Overview

### Context

A **hospital network** wants to deploy a **deep learning model** that classifies **chest X-rays** into “normal” vs “pneumonia” to support radiologists (triage and second read). The model will run on the hospital’s **on-premise GPU server** and be called by the existing radiology information system (RIS) via an API. The hospital requires:

- **Latency:** &lt; 2 seconds per image (end-to-end).
- **Explainability:** Predictions should be interpretable (e.g. which region of the image the model focused on) for clinical audits and trust.
- **Fairness:** Performance should be similar across patient demographics (e.g. age groups, sex) where data allows.

### Problem Statement

Design and document a **deployment solution** for this chest X-ray classifier that meets the above requirements. You are not required to train the model from scratch; you may assume a pre-trained or existing model (e.g. on a public dataset like ChestX-ray14 or a pneumonia subset) and focus on **deployment, API, optimization, and ethics**.

### Data (for context)

- **Training data (assumed):** Chest X-ray images (e.g. from a public dataset such as ChestX-ray8, RSNA Pneumonia, or a Kaggle pneumonia dataset). If such data is unavailable, you may use **MNIST or CIFAR-10 as a stand-in** for the deployment and API design and state this assumption.
- **In production:** Images will arrive in DICOM or PNG/JPG; you must specify preprocessing (resolution, normalization) so the model input is consistent.

### Objectives

By completing this case study, you will:

- Analyze a real-world deployment problem (constraints, requirements, data).
- Propose an appropriate architecture and technology stack (model format, API, optional optimization).
- Plan implementation steps (preprocessing, serving, monitoring).
- Address evaluation (performance, latency) and ethical considerations (bias, explainability).

---

## Analysis Framework

### 1. Problem Analysis (20 points)

**Key questions to address:**

- What is the core problem? (e.g. deploy a CNN for chest X-ray classification under latency and explainability constraints.)
- What are the constraints and requirements? (latency, hardware, explainability, fairness.)
- What data is available for training and what arrives in production? Format and preprocessing.
- What are the success criteria? (e.g. accuracy/F1, latency &lt; 2 s, availability of saliency maps.)

**Your analysis:**  
[Write 1–2 paragraphs. Identify the core problem, list constraints and requirements, state data assumptions, and define success criteria.]

---

### 2. Solution Design (25 points)

**Consider and describe:**

- **Model:** Architecture choice (e.g. CNN like ResNet/DenseNet or ViT) and why it fits (accuracy, interpretability, size). If using a pre-trained model, state that.
- **System architecture:** Where the model runs (on-prem GPU), how the RIS calls it (e.g. REST API), and any preprocessing service.
- **Technology stack:** Framework (TensorFlow/PyTorch), serving option (e.g. custom FastAPI/Flask loading SavedModel/ONNX, or TensorFlow Serving), and format (SavedModel, ONNX, or TFLite if needed for edge).
- **Preprocessing:** Resolution (e.g. 224×224), normalization, and any augmentation for training vs inference.

**Your design:**  
[Write 2–3 paragraphs and/or a short bullet list. Include architecture choice, API design, and tech stack.]

---

### 3. Implementation Plan (25 points)

**Outline concrete steps, for example:**

1. **Data and model:** Obtain or assume dataset; train or load pre-trained model; export to deployment format (e.g. SavedModel/ONNX).
2. **Preprocessing pipeline:** Resize/normalize incoming images to match model input; document in API spec.
3. **API:** Implement a REST endpoint (e.g. POST /predict) that accepts an image, runs preprocessing, runs inference, and returns class + optional confidence and saliency map or region of interest.
4. **Optimization (if needed):** Quantization or pruning to meet latency; measure latency on target hardware.
5. **Explainability:** Integrate Grad-CAM, attention map, or similar to return a “heatmap” or region of focus with the prediction.
6. **Testing and monitoring:** Unit tests for API; monitor latency and error rate; optional fairness checks by subgroup.

**Your plan:**  
[Numbered list of 5–8 steps with one or two sentences each.]

---

### 4. Evaluation (15 points)

**Address:**

- **Performance metrics:** Accuracy, sensitivity, specificity, or F1; on a held-out test set and, if possible, by subgroup.
- **Latency:** End-to-end time per image on the target hardware; confirm &lt; 2 s or state trade-offs.
- **Ethical considerations:** How you would check fairness (e.g. accuracy by group); how explainability is provided (e.g. heatmap) and to whom.

**Your evaluation:**  
[1–2 paragraphs describing how you would measure and report these.]

---

### 5. Recommendations (15 points)

**Your recommendations:**  
[1 paragraph: summarize main recommendations (e.g. use CNN + FastAPI, export to ONNX, add Grad-CAM, monitor fairness). Mention one limitation or future improvement.]

---

## Example (short) – What “good” looks like

**Problem analysis (excerpt):**  
The core problem is deploying a chest X-ray classifier so radiologists can get a fast, interpretable second opinion. Constraints: &lt; 2 s latency, on-prem GPU, and explainable predictions. Data: we assume a pneumonia/normal dataset (e.g. public); production images in DICOM/PNG. Success: F1 &gt; 0.85, P95 latency &lt; 2 s, and heatmaps returned with each prediction.

**Solution design (excerpt):**  
Use a pre-trained ResNet or DenseNet fine-tuned on chest X-rays; export to SavedModel or ONNX. Serve via FastAPI: one endpoint accepts image upload, preprocesses to 224×224 and normalizes, runs inference, runs Grad-CAM to get a heatmap, returns JSON with class, confidence, and heatmap URL or base64. Stack: Python 3.10, TensorFlow or ONNX Runtime, FastAPI, on-prem GPU.

*(Full sample solution for instructors: see `DOCS/SOLUTIONS/case_study_01_sample_solution.md`.)*

---

## Submission Guidelines

- Submit as a **markdown file** (or PDF).
- Include **code snippets** if applicable (e.g. API outline, preprocessing snippet).
- **Maximum 5 pages** (excluding code appendix).
- **Due date:** [To be announced by instructor]

---

**For:** Course 08 – AIAT 122 - Deep Learning
