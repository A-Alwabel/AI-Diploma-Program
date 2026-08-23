# WHAT: write the FastAPI inference server that the container will run.
# WHY: note the relative model path — it works because the Dockerfile sets
# WORKDIR /app, the same directory this file lives in.
"""FastAPI inference server for the Iris RandomForest model."""
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Iris Classifier API")

# Load model once at startup — not on every request
model = joblib.load("model/iris_rf.joblib")
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
