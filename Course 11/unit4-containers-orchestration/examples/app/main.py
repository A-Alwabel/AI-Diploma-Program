"""FastAPI inference server for the Iris RandomForest model."""
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
import subprocess
import sys

app = FastAPI(title="Iris Classifier API")

# The model file (model/iris_rf.joblib) is gitignored, so a fresh clone has
# no model yet. If it is missing, train it once before loading — this makes
# `uvicorn main:app` work locally with no separate setup step.
MODEL_PATH = "model/iris_rf.joblib"
if not os.path.exists(MODEL_PATH):
    subprocess.run([sys.executable, "model_train.py"], check=True)

# Load model once at startup — not on every request
model = joblib.load(MODEL_PATH)
CLASSES = ["setosa", "versicolor", "virginica"]


class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict")
def predict(req: IrisRequest):
    features = np.array([[req.sepal_length, req.sepal_width,
                           req.petal_length, req.petal_width]])
    label = CLASSES[model.predict(features)[0]]
    proba = model.predict_proba(features)[0].max()
    return {"prediction": label, "confidence": round(float(proba), 3)}


@app.get("/health")
def health():
    return {"status": "ok"}

# Run locally: uvicorn main:app --host 0.0.0.0 --port 8000
