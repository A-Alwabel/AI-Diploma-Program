# Project 02: Sequence or Text Model
## Course 08 – AIAT 122 - Deep Learning

**Type:** Optional capstone (in addition to Project 01, or as an alternative if specified by your instructor)  
**Points:** 100 (see `RUBRIC.md`)  
**Suggested duration:** 2–3 weeks

---

## Objective

Build a **sequence or text model** using RNNs, LSTMs, GRUs, or Transformers. You will go from raw data all the way to a trained model that makes real predictions, and optionally deploy it as a simple API or demo.

Choose **one** task:

- **Sentiment analysis** — Classify text as positive or negative (e.g. IMDB movie reviews, product reviews).
- **Text classification** — Classify text into categories (e.g. news topics, spam vs not spam, intent detection).
- **Time series forecasting** — Predict the next value(s) in a sequence (e.g. stock prices, temperature, energy usage).

Deliverables: **code** (notebooks or scripts), a **short report** (1–2 pages), and an optional **demo or API**.

---

## Project Structure

```
Sequence_or_Text_Project/
├── README.md           (this file)
├── RUBRIC.md           (grading criteria)
├── PROJECT_GUIDE.md    (step-by-step guide — read this first)
├── starter/            (optional starter code)
│   ├── README.md
│   ├── train_stub.py       ← training skeleton; fill in TODOs
│   └── predict_stub.py     ← inference skeleton; fill in TODOs
├── notebooks/          (your training and evaluation notebooks)
├── data/               (dataset or links)
├── models/             (saved model files)
└── docs/
    └── report.md       (your short report)
```

**Starter code:** Copy `starter/train_stub.py` and `starter/predict_stub.py` and fill in the `TODO` sections. Or start from scratch in a notebook — both are fine.

**Step-by-step guide:** See `PROJECT_GUIDE.md` for a complete walkthrough from data loading to deployment, with code snippets and troubleshooting tips.

**Recommended preparation:** Complete **Unit 3** examples (`02_rnn_basics.ipynb`, `03_lstm_advanced.ipynb`, `05_bert_finetuning.ipynb`) and optionally **Unit 5** (`06_flask_fastapi_deployment.ipynb`) for the deployment step.

---

## Steps (recommended order)

### 1. Dataset and preprocessing (≈20% of grade)

- Choose a **public dataset** (see suggestions below).
- Load and split into train / validation / test.
- **For text:** Tokenize (e.g. `tf.keras.preprocessing.text.Tokenizer`) and pad sequences to a fixed length.
- **For time series:** Normalize values and create sliding-window sequences.
- Show sample data (e.g. a decoded review, a plot of the time series).

### 2. Model design (≈25% of grade)

- Choose one of: **LSTM**, **GRU**, or **BERT fine-tuning** (for text); **LSTM/GRU** (for time series).
- Define your model architecture (layers, sizes, activation functions).
- Justify your choice briefly (1–2 sentences: why LSTM vs BERT, etc.).

### 3. Training and evaluation (≈25% of grade)

- Compile with an appropriate optimizer, loss, and metric.
- Train with validation monitoring; use callbacks (ModelCheckpoint, EarlyStopping).
- Plot training curves (accuracy/loss or MSE/MAE).
- Evaluate on the **test set**: report accuracy/F1 (text) or MSE/MAE (time series).
- Show sample predictions (e.g. true label → predicted label, true value → predicted value).

### 4. Deployment or demo (≈15% of grade)

- **Option A:** Simple FastAPI/Flask API that accepts text (or a sequence) and returns the prediction.
- **Option B:** Notebook inference — load the saved model, run on a few new examples, with clear output.
- **Option C:** Gradio/Streamlit demo that accepts user text and shows the prediction.

### 5. Report and clarity (≈15% of grade)

- **Short report (1–2 pages):** Problem, dataset, model choice, results, limitations.
- Code should be readable with brief comments.
- Short `README` in your project folder explaining how to run training and inference.

---

## Deliverables

1. **Code:** Notebooks or scripts (training, evaluation, optional API/demo).
2. **Saved model:** In `models/` (`.keras` or SavedModel folder).
3. **Saved tokenizer** (if LSTM/GRU, save `tokenizer.pkl`).
4. **Report:** 1–2 page PDF or Markdown in `docs/`.
5. **Optional:** Live demo or API test.

---

## Dataset suggestions (public — check licenses)

**For sentiment analysis / text classification:**

| Dataset | Where to get | Task | # classes |
|---------|-------------|------|-----------|
| IMDB Movie Reviews | `tf.keras.datasets.imdb.load_data()` | Sentiment | 2 |
| AG News | HuggingFace `datasets`: `load_dataset("ag_news")` | Topic | 4 |
| SMS Spam | Kaggle (UCI SMS Spam) | Spam detection | 2 |
| Twitter Sentiment | Kaggle sentiment140 | Sentiment | 2 |

**For time series:**

| Dataset | Where to get | Task |
|---------|-------------|------|
| Stock prices | `yfinance` (`pip install yfinance`) | Forecasting |
| Air quality (UCI) | UCI Machine Learning Repository | Forecasting |
| Energy consumption | Kaggle household power consumption | Forecasting |
| Sunspot data | `statsmodels.datasets.sunspots` | Forecasting |

---

## Submission

- Submit the whole **Sequence_or_Text_Project** folder (or a zip) including code, saved model, and report.
- **Due date:** [To be announced by instructor]

---

## Teaching notes (instructors)

- **Suggested timeline:** 2 weeks implementation; 1 week report + optional demo.
- **Common issues:** GPU for BERT (recommend Colab); tokenizer saved separately for inference; IMDB is the easiest dataset to start with.
- **Grading:** Use `RUBRIC.md` in this folder.
- **Alignment:** CLO2 (RNNs, Transformers), CLO3 (deploy), CLO4 (hyperparameter tuning).

---

**For:** Course 08 – AIAT 122 - Deep Learning
