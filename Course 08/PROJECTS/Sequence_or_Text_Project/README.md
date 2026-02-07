# Optional Project 02: Sequence or Text Model
## Course 08 – AIAT 122 - Deep Learning

**Type:** Optional capstone (in addition to Project 01)  
**Points:** See `RUBRIC.md` (if used by instructor)  
**Suggested duration:** 2–3 weeks

---

## Objective

Build a **sequence or text model** using RNNs, LSTMs, or Transformers. Choose one of:

- **Sentiment analysis** – Classify product reviews or social media text (binary or multi-class).
- **Text classification** – Topic classification, intent detection, or similar (use a public dataset).
- **Time series** – Simple forecasting or sequence prediction (e.g. with LSTM) on a public dataset.

Deliverables: **code** (notebooks or scripts), a **short report** (1–2 pages), and optional **demo or API**.

---

## Suggested steps

1. **Data** – Load a public dataset (e.g. IMDB, AG News, UCI, or a time series dataset); split train/val/test; tokenize or normalize.
2. **Model** – Build an RNN/LSTM or use a pre-trained Transformer (e.g. BERT); add a classification or regression head.
3. **Training** – Train with validation monitoring; save the best model.
4. **Evaluation** – Report accuracy/F1 or MSE; optionally show sample predictions or error analysis.
5. **Optional** – Deploy as a simple API (e.g. FastAPI) or Gradio/Streamlit demo.

---

## Rubric (if used)

See `RUBRIC.md` in this folder. If your instructor does not use Project 02, this project is for **extra practice only**.

---

**For:** Course 08 – Deep Learning. Aligns with CLO2 (RNNs, Transformers) and CLO3 (build and deploy).
