# Project 01: Image Classification System — Step-by-Step Guide
## Course 08 – AIAT 122 - Deep Learning

This guide walks you through the full project **from zero to a working image classifier with a deployment demo**, step by step. Follow it in order. Each step points to the Unit examples you already ran so you can reuse the patterns.

**Before starting:** Complete the recommended preparation in `README.md` (Unit 2 examples + Unit 5 example 06). Keep those notebooks open as a reference — this project extends them.

**Total time estimate:** ~2–3 weeks working in lab sessions.

---

## How to use this guide

- Read each step fully before coding.
- Copy patterns from the unit examples (the examples already work — reuse them).
- Run one code block, check it works, then move on.
- If something breaks, check the **Troubleshooting** section at the bottom.
- This guide shows **what to do and how to structure it** — not the final solution. Your choices (dataset, architecture) make your project unique.

---

## Step 0: Set up your project folder (Day 1)

Create the following folder structure in your project space (Colab Drive, local, or the `Image_Classification_System/` folder in the repo):

```
Image_Classification_System/
├── notebooks/
│   ├── 01_data_and_preprocessing.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_evaluation_and_deployment.ipynb
├── data/          ← dataset goes here (or a symlink / Colab path)
├── models/        ← saved model files go here
└── docs/
    └── report.md  ← your short report (fill in as you go)
```

**Or** use the starter scripts in `starter/` (`train_stub.py`, `predict_stub.py`) if you prefer scripts over notebooks. Both approaches are fine.

---

## Step 1: Choose your dataset (Day 1–2)

**Pick one** of the following (start simple if this is your first project):

| Dataset | Where to get it | # classes | Image size | Notes |
|---------|-----------------|-----------|------------|-------|
| CIFAR-10 | `tf.keras.datasets.cifar10.load_data()` | 10 | 32×32 | Fastest to start — downloads automatically |
| Dogs vs Cats | Kaggle (or `tfds.load('cats_vs_dogs')`) | 2 | varies | Binary classification |
| Chest X-Ray (Pneumonia) | Kaggle | 2 | varies | Medical; public dataset |
| Plant Disease | Kaggle PlantVillage | 38 | varies | Agriculture use case |
| Your own | Any public allowed dataset | any | any | Discuss with instructor first |

**Recommended for beginners:** Start with **CIFAR-10** — it downloads automatically with one line and you can verify your full pipeline before switching to a custom dataset.

**Write in your report (Section 1):** Name of dataset, number of classes, number of samples, and why you chose it.

---

## Step 2: Data loading and preprocessing (Day 2–3)

**Open:** `notebooks/01_data_and_preprocessing.ipynb`

**Reference:** Unit 2 `02_image_processing_fundamentals_and_feature_extraction.ipynb` — reuse the loading and normalization pattern.

### 2a. Load the data

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Option A: CIFAR-10 (fastest — no download needed)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
class_names = ['airplane','automobile','bird','cat','deer',
               'dog','frog','horse','ship','truck']
print("Train:", x_train.shape, "Test:", x_test.shape)

# Option B: From a folder (for Kaggle or custom datasets)
# dataset = tf.keras.utils.image_dataset_from_directory(
#     "data/train/", image_size=(224, 224), batch_size=32
# )
```

### 2b. Inspect the data

Always look at a sample before training — this catches loading errors.

```python
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(x_train[i])
    ax.set_title(class_names[int(y_train[i])])
    ax.axis("off")
plt.tight_layout()
plt.show()
print("Min pixel:", x_train.min(), "Max pixel:", x_train.max())
```

### 2c. Split and normalize

```python
# Normalize pixel values to [0, 1]
x_train = x_train.astype("float32") / 255.0
x_test  = x_test.astype("float32") / 255.0

# Create a validation set from training data (20%)
from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(
    x_train, y_train, test_size=0.2, random_state=42
)
print(f"Train: {x_train.shape} | Val: {x_val.shape} | Test: {x_test.shape}")
```

### 2d. (Optional) Data augmentation

Adding augmentation helps the model generalise. Reference: Unit 2 `02_image_processing_fundamentals_and_feature_extraction.ipynb`.

```python
# Add after normalization — augment training data only
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1),
])
# Apply during training: pass augmentation as first layer in the model, or as a preprocessing step
```

**Checkpoint:** Before moving on, make sure you can print the shapes and see a sample grid of images with labels.

---

## Step 3: Model design (Day 3–5)

**Open:** `notebooks/02_model_training.ipynb`

**Reference:** Unit 2 `01_cnn_architecture.ipynb` (build from scratch) and `05_transfer_learning_cnns.ipynb` + `06_pretrained_cnn_architectures.ipynb` (transfer learning).

Choose **one** approach:

### Option A: CNN from scratch (simpler, good for CIFAR-10)

```python
model = tf.keras.Sequential([
    # Block 1
    tf.keras.layers.Conv2D(32, (3,3), activation="relu", padding="same", input_shape=(32,32,3)),
    tf.keras.layers.Conv2D(32, (3,3), activation="relu", padding="same"),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Dropout(0.25),  # regularization — see Unit 1 notebooks

    # Block 2
    tf.keras.layers.Conv2D(64, (3,3), activation="relu", padding="same"),
    tf.keras.layers.Conv2D(64, (3,3), activation="relu", padding="same"),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Dropout(0.25),

    # Classifier head
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation="softmax"),   # change 10 to your num_classes
])

model.summary()
```

### Option B: Transfer learning (better accuracy, recommended for custom datasets)

```python
# Use a pre-trained model (MobileNetV2 is fast; ResNet50 is stronger)
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,       # remove original classifier head
    weights="imagenet"       # pre-trained weights
)
base_model.trainable = False  # freeze base (train only the head first)

inputs  = tf.keras.Input(shape=(224, 224, 3))
x = base_model(inputs, training=False)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dense(128, activation="relu")(x)
x = tf.keras.layers.Dropout(0.3)(x)
outputs = tf.keras.layers.Dense(NUM_CLASSES, activation="softmax")(x)  # set NUM_CLASSES
model = tf.keras.Model(inputs, outputs)

model.summary()
```

**Write in your report (Section 2):** Which approach you chose and **why** (1–2 sentences — e.g. "I used MobileNetV2 transfer learning because CIFAR images are small and transfer learning gives better accuracy with less training time").

---

## Step 4: Compile and train (Day 5–7)

**Reference:** Unit 2 `07_training_cnn_image_datasets.ipynb` — reuse the compile + fit + callbacks pattern.

### 4a. Compile

```python
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss="sparse_categorical_crossentropy",   # use "categorical_crossentropy" if y is one-hot
    metrics=["accuracy"]
)
```

### 4b. Callbacks (recommended)

```python
import os
os.makedirs("models", exist_ok=True)

callbacks = [
    # Save the best model automatically
    tf.keras.callbacks.ModelCheckpoint(
        filepath="models/best_model.keras",
        save_best_only=True,
        monitor="val_accuracy",
        verbose=1
    ),
    # Stop early if validation accuracy stops improving
    tf.keras.callbacks.EarlyStopping(
        monitor="val_accuracy",
        patience=5,
        restore_best_weights=True,
        verbose=1
    ),
]
```

### 4c. Train

```python
history = model.fit(
    x_train, y_train,
    epochs=20,                    # start with 10-20; use more if needed
    batch_size=64,
    validation_data=(x_val, y_val),
    callbacks=callbacks,
    verbose=1
)
```

**On Colab:** Enable GPU (Runtime → Change runtime type → GPU) — training is 10–50× faster.

**Expected outputs you should see:**
- Per-epoch: `loss`, `accuracy`, `val_loss`, `val_accuracy` printed
- `Epoch X: val_accuracy improved from … to …` (from ModelCheckpoint)

### 4d. Plot training curves

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(history.history["accuracy"],     label="train accuracy")
ax1.plot(history.history["val_accuracy"], label="val accuracy")
ax1.set_title("Accuracy"); ax1.set_xlabel("Epoch"); ax1.legend()

ax2.plot(history.history["loss"],     label="train loss")
ax2.plot(history.history["val_loss"], label="val loss")
ax2.set_title("Loss"); ax2.set_xlabel("Epoch"); ax2.legend()
plt.tight_layout(); plt.show()
```

**What to look for:**
- Validation accuracy improving → model is learning.
- Large gap between train and val accuracy → overfitting → reduce epochs, add Dropout, use data augmentation.
- Val accuracy flat from epoch 1 → model not learning → check learning rate, data normalization.

---

## Step 5: Evaluate on test set (Day 7–8)

**Open:** `notebooks/03_evaluation_and_deployment.ipynb`

```python
# Load the best saved model
model = tf.keras.models.load_model("models/best_model.keras")

# Evaluate on test set (not used during training)
loss, acc = model.evaluate(x_test, y_test, verbose=1)
print(f"Test accuracy: {acc:.4f}")

# Show sample predictions
y_pred = model.predict(x_test[:10]).argmax(axis=1)
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(x_test[i])
    true_label = class_names[int(y_test[i])] if class_names else str(int(y_test[i]))
    pred_label = class_names[y_pred[i]]       if class_names else str(y_pred[i])
    color = "green" if true_label == pred_label else "red"
    ax.set_title(f"True: {true_label}\nPred: {pred_label}", color=color, fontsize=8)
    ax.axis("off")
plt.tight_layout(); plt.show()
```

**Optional: Confusion matrix**

```python
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

y_pred_all = model.predict(x_test).argmax(axis=1)
y_true_all = y_test.flatten()

cm = confusion_matrix(y_true_all, y_pred_all)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=class_names, yticklabels=class_names)
plt.xlabel("Predicted"); plt.ylabel("True"); plt.title("Confusion Matrix")
plt.show()

print(classification_report(y_true_all, y_pred_all, target_names=class_names))
```

**Write in your report (Section 3):** Test accuracy, any interesting errors (which classes are confused), and one sentence explaining why (e.g. "Cat and dog images were confused most often, probably because both are furry animals photographed in similar settings").

---

## Step 6: Deployment / Demo (Day 9–12)

**Reference:** Unit 5 `06_flask_fastapi_deployment.ipynb` — reuse the API pattern.

Pick **one** option (A, B, or C). Option B is the simplest if you're new to deployment.

### Option A: FastAPI (recommended for full marks on deployment)

```python
# File: serve.py
from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI(title="Image Classifier API")

# Load model once at startup
model = tf.keras.models.load_model("models/best_model.keras")
CLASS_NAMES = ['airplane','automobile','bird','cat','deer',
               'dog','frog','horse','ship','truck']  # update to your classes

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Accept an image file and return predicted class + confidence."""
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB").resize((32, 32))
    arr = np.array(img, dtype="float32") / 255.0
    arr = np.expand_dims(arr, axis=0)          # shape: (1, 32, 32, 3)
    probs = model.predict(arr)[0]
    idx  = int(probs.argmax())
    return {
        "class":      CLASS_NAMES[idx],
        "confidence": float(probs[idx]),
        "all_probs":  {c: float(p) for c, p in zip(CLASS_NAMES, probs)}
    }

# Run with: uvicorn serve:app --reload
# Then test with: curl -X POST "http://localhost:8000/predict" -F "file=@your_image.jpg"
```

### Option B: Notebook inference (simplest)

```python
# In your evaluation notebook — just load and predict on a new image
from PIL import Image
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("models/best_model.keras")
CLASS_NAMES = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

img = Image.open("my_test_image.jpg").convert("RGB").resize((32, 32))
arr = np.array(img, dtype="float32") / 255.0
arr = np.expand_dims(arr, axis=0)
probs = model.predict(arr)[0]
predicted = CLASS_NAMES[probs.argmax()]
confidence = probs.max()
print(f"Predicted: {predicted}  (confidence: {confidence:.2%})")
```

### Option C: ONNX export + inference

```python
# Export to ONNX (reference: Unit 5 03_onnx_conversion.ipynb)
# pip install tf2onnx onnxruntime
import tf2onnx, onnxruntime as rt
import tensorflow as tf

model = tf.keras.models.load_model("models/best_model.keras")
spec = (tf.TensorSpec(model.inputs[0].shape, tf.float32, name="input"),)
model_proto, _ = tf2onnx.convert.from_keras(model, input_signature=spec, opset=13)
with open("models/image_classifier.onnx", "wb") as f:
    f.write(model_proto.SerializeToString())
print("ONNX model saved.")

# Inference with ONNX
sess = rt.InferenceSession("models/image_classifier.onnx")
result = sess.run(None, {"input": arr})
print("ONNX predicted class:", CLASS_NAMES[result[0].argmax()])
```

---

## Step 7: Write your report (Day 12–14)

Create `docs/report.md` (or PDF) — **1–2 pages** covering:

```markdown
# Image Classification System – Project Report

## 1. Problem and dataset
- What am I classifying?
- Dataset name, source, number of classes, number of samples.
- Why is this useful in real life?

## 2. Model architecture
- CNN from scratch or transfer learning — which and why?
- Key hyperparameters: input size, optimizer, learning rate, epochs.

## 3. Results
- Final test accuracy: XX%
- Training curves: (paste or link to your plot)
- Interesting observations (e.g. which classes are confused most).

## 4. Deployment
- Which option (A / B / C) and how to run it (1–2 sentences with the command).

## 5. Limitations and future work
- What would improve accuracy? (e.g. more data, larger model, fine-tuning)
- What would make the deployment more production-ready?
```

---

## Step 8: Final check before submission

Go through this list before you submit:

- [ ] Training curves saved (accuracy and loss plots).
- [ ] Test accuracy reported (at least `model.evaluate()` output).
- [ ] Saved model in `models/` (`.keras`, `.h5`, or SavedModel folder).
- [ ] Deployment option works: API responds, or notebook runs end-to-end.
- [ ] Report in `docs/` with all 5 sections.
- [ ] Code has comments explaining what each block does (not every line — just the purpose of each major block).
- [ ] The project folder has a short `README.md` with: how to run training, how to run the demo or API.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| CUDA out of memory | GPU memory full | Reduce batch size: `batch_size=32` or `16`. Use a smaller model or fewer layers. |
| val_accuracy stays at ~10% (same as random) | Data not normalized, labels wrong, or model not learning | Check: print `x_train.min(), x_train.max()` (should be 0–1); print `y_train[:5]` (should be 0–9); try a smaller learning rate or more epochs. |
| Model overfits (train acc high, val acc low) | Model too complex or not enough regularization | Add `Dropout`, use data augmentation, reduce model size, use EarlyStopping. |
| TensorFlow import fails (charset_normalizer) | Broken dependency | Run: `pip install --upgrade charset-normalizer requests`, then restart kernel. See `DOCS/COLAB_SETUP.md`. |
| ModuleNotFoundError | Library not installed | Run: `pip install tensorflow pillow sklearn` (or `pip install -r requirements.txt` from the root). |
| Training very slow on CPU | No GPU | Enable GPU on Colab: Runtime → Change runtime type → GPU. |
| PIL / Pillow not found | Missing for image loading | `pip install Pillow` |
| model.save fails | Wrong path or format | Create the folder first: `import os; os.makedirs("models", exist_ok=True)`. |

---

## Quick reference: which unit notebooks to use

| Project step | Unit notebook to reference |
|--------------|---------------------------|
| Data loading + normalization | Unit 2 `02_image_processing_fundamentals_and_feature_extraction.ipynb` |
| CNN from scratch | Unit 2 `01_cnn_architecture.ipynb` |
| Transfer learning (MobileNet, ResNet) | Unit 2 `05_transfer_learning_cnns.ipynb`, `06_pretrained_cnn_architectures.ipynb` |
| Training loop + callbacks + curves | Unit 2 `07_training_cnn_image_datasets.ipynb` |
| Model optimization (ONNX, quantization) | Unit 5 `03_onnx_conversion.ipynb`, `07_model_optimization_quantization.ipynb` |
| FastAPI / Flask deployment | Unit 5 `06_flask_fastapi_deployment.ipynb` |

---

**For:** Course 08 – AIAT 122 - Deep Learning  
**Project:** 01 – Image Classification System  
**No solutions here** — your implementation and choices make the project uniquely yours.
