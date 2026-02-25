# Project 02: Sequence or Text Model — Step-by-Step Guide
## Course 08 – AIAT 122 - Deep Learning

This guide walks you through building a **sequence or text model end-to-end** — from data loading to training and optional deployment. Follow it in order. Each step points to the Unit 3 examples you already ran so you can reuse the patterns.

**Before starting:** Complete the recommended Unit 3 examples, especially `02_rnn_basics.ipynb`, `03_lstm_advanced.ipynb`, `04_transformer_attention.ipynb`, and `05_bert_finetuning.ipynb`.

**Total time estimate:** ~2–3 weeks working in lab sessions.

---

## How to use this guide

- Read each step fully before coding.
- Copy patterns directly from the unit examples — they already work.
- Run one cell, verify it works, then continue.
- Choose **one task type** (sentiment, text classification, or time series) and stick with it.
- **Troubleshooting** section is at the bottom if something breaks.

---

## Step 0: Choose your task (Day 1)

Pick **one** of the following:

| Task | Model type | Dataset (suggested) | Metric |
|------|-----------|---------------------|--------|
| **Sentiment analysis** | LSTM or BERT fine-tune | IMDB Movie Reviews, Twitter Sentiment | Accuracy / F1 |
| **Text classification** | LSTM or BERT fine-tune | AG News, 20 Newsgroups, SMS Spam | Accuracy / F1 |
| **Time series forecasting** | LSTM or GRU | Stock prices (Yahoo Finance), Air quality (UCI), Sunspot data | MSE / MAE |

**Recommended for beginners:** Start with **IMDB sentiment** — it loads with one line and is binary (positive/negative), which makes it simpler to debug. Reference: Unit 3 `03_lstm_advanced.ipynb`.

**Recommended if you want to use Transformers:** Try **BERT fine-tuning on IMDB or AG News**. Reference: Unit 3 `05_bert_finetuning.ipynb`.

**Write in your report (Section 1):** Task name, dataset, model type, and why you chose it.

---

## Set up your project folder

```
Sequence_or_Text_Project/
├── notebooks/
│   ├── 01_data_and_tokenization.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_evaluation_and_demo.ipynb
├── data/          ← dataset goes here (or a Colab path)
├── models/        ← saved model files go here
└── docs/
    └── report.md  ← fill in as you go
```

**Or** use `starter/train_stub.py` and `starter/predict_stub.py` if you prefer scripts.

---

## Step 1: Load and explore your dataset (Day 1–2)

**Open:** `notebooks/01_data_and_tokenization.ipynb`

### Option A — IMDB sentiment (easiest start)

```python
import tensorflow as tf

# Download and load IMDB — already split into train/test
(x_train_raw, y_train), (x_test_raw, y_test) = tf.keras.datasets.imdb.load_data(
    num_words=10000  # keep only the 10,000 most common words
)
print("Train samples:", len(x_train_raw))
print("Example review (token IDs):", x_train_raw[0][:20])
print("Label (0=neg, 1=pos):", y_train[0])

# Decode one review back to text (to understand what you're working with)
word_index = tf.keras.datasets.imdb.get_word_index()
reverse_index = {v+3: k for k, v in word_index.items()}
reverse_index.update({0: "<PAD>", 1: "<START>", 2: "<UNK>", 3: "<UNUSED>"})
decoded = " ".join(reverse_index.get(i, "?") for i in x_train_raw[0])
print("\nDecoded review:", decoded[:300])
```

### Option B — CSV text dataset (AG News, Spam, or custom)

```python
import pandas as pd

df = pd.read_csv("data/dataset.csv")   # your downloaded CSV
print(df.head())
print("Columns:", df.columns.tolist())
print("Label distribution:\n", df["label"].value_counts())

# Split into train / validation / test
from sklearn.model_selection import train_test_split
train_df, temp_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df["label"])
val_df, test_df   = train_test_split(temp_df, test_size=0.5, random_state=42)
print(f"Train: {len(train_df)} | Val: {len(val_df)} | Test: {len(test_df)}")
```

### Option C — Time series data

```python
import pandas as pd, numpy as np

# Example: load a CSV with a time-indexed numeric column
df = pd.read_csv("data/timeseries.csv", parse_dates=["date"], index_col="date")
print(df.head())
print("Shape:", df.shape)
df["value"].plot(title="Time series", figsize=(12, 3))

# Normalize (important for LSTMs)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
values = scaler.fit_transform(df[["value"]])

# Create sliding window sequences (SEQ_LEN steps → predict next 1 step)
SEQ_LEN = 30
X, y = [], []
for i in range(len(values) - SEQ_LEN):
    X.append(values[i:i+SEQ_LEN])
    y.append(values[i+SEQ_LEN])
X, y = np.array(X), np.array(y)
print("X shape:", X.shape, "y shape:", y.shape)  # (samples, SEQ_LEN, 1)
```

**Checkpoint:** Make sure you can print dataset shape, class distribution (or value range for time series), and see a sample.

---

## Step 2: Tokenization and padding (Day 2–3)

**Reference:** Unit 3 `02_rnn_basics.ipynb` and `03_lstm_advanced.ipynb` — reuse the tokenization / padding pattern.

*(Skip this step if you chose time series — sequences are already numeric.)*

### For IMDB (already tokenized — just pad)

```python
from tensorflow.keras.preprocessing.sequence import pad_sequences

MAX_LEN = 200   # truncate/pad all reviews to 200 tokens
x_train = pad_sequences(x_train_raw, maxlen=MAX_LEN, padding="post", truncating="post")
x_test  = pad_sequences(x_test_raw,  maxlen=MAX_LEN, padding="post", truncating="post")

# Create a validation split from training data
x_train, x_val = x_train[:20000], x_train[20000:]
y_train, y_val = y_train[:20000], y_train[20000:]
print(f"Train: {x_train.shape} | Val: {x_val.shape} | Test: {x_test.shape}")
```

### For your own text dataset (tokenize from scratch)

```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

VOCAB_SIZE = 20000
MAX_LEN    = 150

tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token="<OOV>")
tokenizer.fit_on_texts(train_df["text"])

x_train = pad_sequences(tokenizer.texts_to_sequences(train_df["text"]), maxlen=MAX_LEN, padding="post")
x_val   = pad_sequences(tokenizer.texts_to_sequences(val_df["text"]),   maxlen=MAX_LEN, padding="post")
x_test  = pad_sequences(tokenizer.texts_to_sequences(test_df["text"]),  maxlen=MAX_LEN, padding="post")

y_train = train_df["label"].values
y_val   = val_df["label"].values
y_test  = test_df["label"].values

print(f"Train: {x_train.shape} | Val: {x_val.shape}")
```

---

## Step 3: Build your model (Day 3–5)

**Open:** `notebooks/02_model_training.ipynb`

Choose **one** approach:

### Option A: LSTM (great for text and time series)

**Reference:** Unit 3 `03_lstm_advanced.ipynb`

```python
import tensorflow as tf

# For text classification (sentiment / multi-class)
VOCAB_SIZE = 10000   # adjust to your tokenizer
EMBED_DIM  = 64
NUM_CLASSES = 2      # 2 for binary; more for multi-class

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(VOCAB_SIZE, EMBED_DIM, input_length=MAX_LEN),
    tf.keras.layers.LSTM(64, return_sequences=True),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation="sigmoid"),   # binary: sigmoid + binary_crossentropy
    # For multi-class: Dense(NUM_CLASSES, activation="softmax")
])
model.summary()
```

```python
# For time series regression
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, return_sequences=True, input_shape=(SEQ_LEN, 1)),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(1),   # predict one value
])
model.summary()
```

### Option B: GRU (faster than LSTM, similar accuracy)

**Reference:** Unit 3 `08_text_generation_rnn_lstm_gru.ipynb`

```python
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(VOCAB_SIZE, EMBED_DIM, input_length=MAX_LEN),
    tf.keras.layers.GRU(64, return_sequences=True),
    tf.keras.layers.GRU(32),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])
model.summary()
```

### Option C: Fine-tune BERT (highest accuracy, more complex)

**Reference:** Unit 3 `05_bert_finetuning.ipynb` — copy the tokenizer and model setup.

```python
# pip install transformers datasets
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import tensorflow as tf

MODEL_NAME = "bert-base-uncased"    # or "distilbert-base-uncased" for speed
tokenizer  = AutoTokenizer.from_pretrained(MODEL_NAME)
model      = TFAutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

# Tokenize your texts
def tokenize_batch(texts, max_len=128):
    return tokenizer(texts, padding=True, truncation=True,
                     max_length=max_len, return_tensors="tf")

train_enc = tokenize_batch(train_df["text"].tolist())
val_enc   = tokenize_batch(val_df["text"].tolist())

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=2e-5),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"]
)
model.summary()
```

**Write in your report (Section 2):** Which model you chose and why (1–2 sentences).

---

## Step 4: Compile and train (Day 5–8)

**Reference:** Unit 3 `03_lstm_advanced.ipynb` — reuse the compile + fit pattern.

### For LSTM / GRU (binary text classification)

```python
import os
os.makedirs("models", exist_ok=True)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss="binary_crossentropy",       # binary: "binary_crossentropy"; multi-class: "sparse_categorical_crossentropy"
    metrics=["accuracy"]
)

callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        "models/best_model.keras", save_best_only=True,
        monitor="val_accuracy", verbose=1
    ),
    tf.keras.callbacks.EarlyStopping(
        monitor="val_accuracy", patience=3,
        restore_best_weights=True, verbose=1
    ),
]

history = model.fit(
    x_train, y_train,
    epochs=15,
    batch_size=64,
    validation_data=(x_val, y_val),
    callbacks=callbacks
)
```

### For time series (regression)

```python
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss="mse",
    metrics=["mae"]
)
history = model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=32,
    validation_split=0.1,
    callbacks=[tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)]
)
```

### Plot training curves

```python
import matplotlib.pyplot as plt

metric = "accuracy" if "accuracy" in history.history else "mae"
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(history.history[metric],         label=f"train {metric}")
ax1.plot(history.history[f"val_{metric}"],label=f"val {metric}")
ax1.set_title(metric.capitalize()); ax1.set_xlabel("Epoch"); ax1.legend()

ax2.plot(history.history["loss"],         label="train loss")
ax2.plot(history.history["val_loss"],     label="val loss")
ax2.set_title("Loss"); ax2.set_xlabel("Epoch"); ax2.legend()
plt.tight_layout(); plt.show()
```

---

## Step 5: Evaluate (Day 8–9)

**Open:** `notebooks/03_evaluation_and_demo.ipynb`

### Text classification evaluation

```python
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

model = tf.keras.models.load_model("models/best_model.keras")
loss, acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {acc:.4f}")

y_pred = (model.predict(x_test) > 0.5).astype(int).flatten()   # binary
print(classification_report(y_test, y_pred, target_names=["Negative", "Positive"]))

# Show sample predictions
print("\nSample predictions (first 5):")
for i in range(5):
    pred = "Positive" if y_pred[i] == 1 else "Negative"
    true = "Positive" if y_test[i] == 1  else "Negative"
    print(f"  True: {true:10s} | Predicted: {pred}")
```

### Time series evaluation

```python
import numpy as np, matplotlib.pyplot as plt

model = tf.keras.models.load_model("models/best_model.keras")
y_pred = model.predict(X_test).flatten()
y_true = y_test.flatten()

mse = np.mean((y_pred - y_true) ** 2)
mae = np.mean(np.abs(y_pred - y_true))
print(f"Test MSE: {mse:.4f} | MAE: {mae:.4f}")

plt.figure(figsize=(12, 4))
plt.plot(y_true[:100],  label="True")
plt.plot(y_pred[:100],  label="Predicted")
plt.title("True vs Predicted (first 100 steps)")
plt.xlabel("Time step"); plt.legend(); plt.show()
```

**Write in your report (Section 3):** Test accuracy (or MSE/MAE), 1–2 sample predictions, and one observation (e.g. "BERT achieved 90% accuracy; LSTM achieved 85% — BERT is better but takes longer to train").

---

## Step 6: Optional deployment (Day 10–12)

**Reference:** Unit 5 `06_flask_fastapi_deployment.ipynb`

```python
# File: serve.py — FastAPI endpoint for text classification
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

app = FastAPI(title="Text Classifier API")

# Load model once at startup
model = tf.keras.models.load_model("models/best_model.keras")

# Load the tokenizer you saved during training
import pickle
with open("models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAX_LEN = 200

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(req: TextRequest):
    """Accept a text string and return sentiment prediction."""
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    seq = tokenizer.texts_to_sequences([req.text])
    padded = pad_sequences(seq, maxlen=MAX_LEN, padding="post")
    prob = float(model.predict(padded)[0][0])
    label = "Positive" if prob > 0.5 else "Negative"
    return {"label": label, "confidence": prob if prob > 0.5 else 1 - prob}

# Run: uvicorn serve:app --reload
# Test: curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"text": "This movie was great!"}'
```

**Save your tokenizer during training:**

```python
import pickle
with open("models/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)
print("Tokenizer saved.")
```

---

## Step 7: Write your report (Day 12–14)

`docs/report.md` — **1–2 pages**:

```markdown
# Sequence / Text Model – Project Report

## 1. Problem and dataset
- What am I predicting?
- Dataset name, source, number of classes (or value range), number of samples.
- Why is this useful in real life?

## 2. Model architecture
- LSTM / GRU / BERT — which and why?
- Key hyperparameters: EMBED_DIM, hidden units, learning rate, epochs.

## 3. Results
- Final test accuracy (or MSE/MAE): XX%
- Training curves: (paste plot)
- Interesting observations.

## 4. Deployment (if done)
- API endpoint and how to test it.

## 5. Limitations and future work
- What would improve accuracy? (e.g. longer training, bigger BERT model, more data)
```

---

## Step 8: Final checklist before submission

- [ ] Training curves (loss and metric plots) saved.
- [ ] Test accuracy or MSE/MAE reported.
- [ ] Model saved in `models/`.
- [ ] Tokenizer saved (if LSTM/GRU) or BERT model saved (if Transformers).
- [ ] Report in `docs/` with all 5 sections filled.
- [ ] Code has comments explaining each major block.
- [ ] Short `README.md` in your project folder: how to run training, how to test the model.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| Training accuracy stuck at 50% | Binary labels not balanced or model not learning | Check `y_train` distribution; try smaller learning rate (e.g. `1e-4`); verify normalization. |
| CUDA out of memory (BERT) | BERT is large | Reduce `batch_size` to 8 or 4; use `distilbert-base-uncased` instead (faster, smaller). |
| Tokenizer vocabulary size mismatch | Model built with different VOCAB_SIZE than tokenizer | Match `VOCAB_SIZE` between tokenizer fit and model Embedding layer. |
| `ModuleNotFoundError: transformers` | HuggingFace not installed | `pip install transformers datasets` |
| LSTM val_accuracy stays at 50% | Sequences not padded correctly or embedding layer issue | Print `x_train[:3]` and check for all-zero rows; verify `MAX_LEN`. |
| Slow training (BERT on CPU) | BERT needs GPU | Enable Colab GPU: Runtime → Change runtime type → GPU. |
| `KeyError` or `AttributeError` on tokenizer load | Wrong pickle format | Re-save tokenizer in same session; ensure `tokenizer.pkl` matches the model. |

---

## Quick reference: which unit notebooks to use

| Project step | Unit notebook |
|--------------|---------------|
| Understanding sequential data | Unit 3 `01_understanding_sequential_data_and_time_series_prediction.ipynb` |
| RNN/LSTM basics, padding | Unit 3 `02_rnn_basics.ipynb`, `03_lstm_advanced.ipynb` |
| BERT / fine-tuning | Unit 3 `05_bert_finetuning.ipynb` |
| Text generation (for RNN context) | Unit 3 `08_text_generation_rnn_lstm_gru.ipynb` |
| Sentiment / classification (NLP end-to-end) | Unit 3 `10_sentiment_analysis_translation_speech.ipynb` |
| FastAPI deployment | Unit 5 `06_flask_fastapi_deployment.ipynb` |

---

**For:** Course 08 – AIAT 122 - Deep Learning  
**Project:** 02 – Sequence or Text Model  
**No solutions here** — your choices (dataset, model, task) make the project uniquely yours.
