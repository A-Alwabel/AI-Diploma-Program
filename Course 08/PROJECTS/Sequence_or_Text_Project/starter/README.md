# Starter code – Project 02: Sequence or Text Model

These files are an **optional starting point**. You can use them as-is and fill in the TODOs, or start from scratch using a notebook.

## Files

| File | Purpose |
|------|---------|
| `train_stub.py` | Load data → build LSTM model → train → evaluate. Fill in your dataset and architecture. |
| `predict_stub.py` | Load saved model → run inference on new text. Fill in your tokenizer and labels. |

## How to use

1. Copy these files into your project folder (or the `starter/` folder itself).
2. Open `train_stub.py` and fill in the `TODO` blocks with your dataset, architecture choices, and hyperparameters.
3. Run training: `python train_stub.py`
4. Check that `models/best_model.keras` was saved.
5. Fill in `predict_stub.py` with your tokenizer path and test texts.
6. Test inference: `python predict_stub.py`

## Requirements

```bash
pip install tensorflow numpy scikit-learn
# For BERT (optional):
pip install transformers datasets
# For FastAPI deployment (Unit 5):
pip install fastapi uvicorn
```

## Reference notebooks

| Topic | Unit notebook |
|-------|--------------|
| LSTM/GRU training | Unit 3 `03_lstm_advanced.ipynb` |
| BERT fine-tuning | Unit 3 `05_bert_finetuning.ipynb` |
| FastAPI deployment | Unit 5 `06_flask_fastapi_deployment.ipynb` |

**Note:** These stubs do not include solutions — your implementation and choices are part of the grade.
