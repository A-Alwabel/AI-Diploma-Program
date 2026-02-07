# Project 01: Image Classification System
## Course 08 – AIAT 122 - Deep Learning

**Type:** Capstone project  
**Points:** 100 (see `RUBRIC.md`)  
**Suggested duration:** 2–3 weeks

---

## Objective

Build and deploy an **image classifier** using deep learning. You may choose a domain such as:

- **Medical:** X-ray or skin lesion classification (use only public, allowed datasets).
- **General:** Wildlife, product recognition, or scene classification.
- **Classic:** CIFAR-10, or a subset of ImageNet-style data.

Deliverables: **code** (notebooks or scripts), a **short report** (1–2 pages), and an optional **10-minute presentation** or **live demo** (e.g. simple web UI or API).

---

## Project Structure

```
Image_Classification_System/
├── README.md           (this file)
├── RUBRIC.md           (grading criteria)
├── starter/            (optional) – train_stub.py, predict_stub.py; copy and expand
├── notebooks/          (or scripts/) – training and evaluation
├── data/               (or links to datasets) – place dataset or symlinks here
├── models/             (saved model files, e.g. SavedModel, .h5, or .pt)
└── docs/               (optional: short report, screenshots)
```

**Starter code:** If you want a minimal skeleton, use the scripts in `starter/` (see `starter/README.md`). You can also start from scratch.

---

## Steps (recommended order)

### 1. Data loading and preprocessing (≈20% of grade)

- Choose a **public dataset** (e.g. CIFAR-10, Kaggle Dogs vs Cats, a chest X-ray or skin lesion dataset, or another image dataset allowed by your institution).
- Load data; split into train/validation/test.
- **Preprocess:** Resize to a fixed size (e.g. 224×224 or 32×32 for CIFAR); normalize pixel values (e.g. /255 or ImageNet mean/std).
- Optionally use **data augmentation** (rotation, flip, brightness) for training.
- Create data loaders (e.g. `tf.data.Dataset` or PyTorch `DataLoader`).

### 2. Model design (≈25% of grade)

- Use a **CNN** (from scratch or small architecture) or **transfer learning** (e.g. ResNet, MobileNet, EfficientNet from Keras/TF or PyTorch).
- Define the model (input shape, number of classes); if using transfer learning, replace the top layer for your num_classes.
- Justify briefly why you chose this architecture (e.g. accuracy vs speed, size).

### 3. Training and evaluation (≈20% of grade)

- **Train** the model (specify optimizer, loss, epochs, batch size). Use validation data to monitor overfitting.
- **Evaluate** on the test set: report accuracy, and optionally F1, confusion matrix, or per-class metrics.
- Save the best model (e.g. `model.save()`, or export to SavedModel/ONNX).

### 4. Deployment or demo (≈20% of grade)

- **Option A:** Export the model (e.g. SavedModel, ONNX, or TFLite) and provide a **simple API** (e.g. Flask/FastAPI) that accepts an image and returns the predicted class (and optional confidence).
- **Option B:** A **notebook or script** that loads the saved model and runs inference on a few sample images, with clear instructions to run it.
- **Option C:** A short **demo** (e.g. Gradio/Streamlit app) that allows uploading an image and seeing the prediction.

### 5. Report and clarity (≈15% of grade)

- **Short report (1–2 pages):** Problem statement, dataset description, model choice, training setup, main results (metrics), and limitations or future work.
- Code should be readable: brief comments and a short README in the project folder on how to run training and inference.

---

## Deliverables

1. **Code:** All notebooks or scripts (training, evaluation, and optional API/demo) in the project folder or linked clearly.
2. **Model:** At least one saved model file (or instructions to reproduce it) in `models/` or equivalent.
3. **Report:** 1–2 page PDF or Markdown in `docs/` or project root.
4. **Optional:** 10-minute presentation or live demo (format as specified by instructor).

---

## Dataset suggestions (public, check licenses)

- **CIFAR-10** – 10 classes, small images; good for quick projects.
- **Kaggle:** Dogs vs Cats, Plant Disease, Chest X-Ray (e.g. pneumonia), Skin Lesion (e.g. ISIC if allowed).
- **TensorFlow Datasets / PyTorch:** Many image classification datasets available via `tfds.load()` or `torchvision.datasets`.

---

## Submission

- Submit the whole **Image_Classification_System** folder (or a zip) including code, saved model(s), and report.
- **Due date:** [To be announced by instructor]

---

## Teaching notes (instructors)

- **Suggested timeline:** 2 weeks for implementation; 1 week for report and optional presentation.
- **Common issues:** GPU access (suggest Colab); dataset size (allow CIFAR or small subsets); export format (SavedModel/ONNX) for deployment part.
- **Grading:** Use `RUBRIC.md` in this folder. Exercise solutions and runbook: see `DOCS/INSTRUCTOR_RUNBOOK.md` and `DOCS/SOLUTIONS/`.

---

**For:** Course 08 – AIAT 122 - Deep Learning
