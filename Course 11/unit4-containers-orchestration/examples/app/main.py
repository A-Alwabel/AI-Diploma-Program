# WHAT: the inference server that runs INSIDE the container.
# WHY: note where the artifact comes from. Unit 1 and Unit 2 read the portfolio
# directory in your home folder; a container has no home folder to read. The
# model is baked in at "model/", relative to WORKDIR /app - the image IS the
# artifact store, which is exactly what makes it reproducible.
"""FastAPI inference server for the staged portfolio model."""
import json
import os
import re
from pathlib import Path

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field, create_model

MODEL_DIR = Path(os.environ.get("MODEL_DIR", "model"))
CARD = json.loads((MODEL_DIR / "model_card.json").read_text())
ARTIFACT = MODEL_DIR / CARD["artifact"]

if CARD["framework"] == "sklearn":
    import joblib
    _model = joblib.load(ARTIFACT)

    def probabilities(rows):
        return np.asarray(_model.predict_proba(rows))

elif CARD["framework"] == "onnx":
    import onnxruntime as ort
    _session = ort.InferenceSession(str(ARTIFACT), providers=["CPUExecutionProvider"])
    _input = _session.get_inputs()[0].name

    def probabilities(rows):
        logits = np.asarray(_session.run(None, {_input: np.asarray(rows, dtype=np.float32)})[0])
        exp = np.exp(logits - logits.max(axis=1, keepdims=True))
        return exp / exp.sum(axis=1, keepdims=True)

else:
    raise RuntimeError(f"This image serves 'sklearn' or 'onnx' artifacts, not {CARD['framework']!r}.")


def api_field(name):
    slug = re.sub(r"\W+", "_", str(name).strip().lower()).strip("_")
    return f"f_{slug}" if not slug or slug[0].isdigit() else slug

FIELD_ORDER = [api_field(n) for n in CARD["feature_names"]]

PredictRequest = create_model(
    "PredictRequest",
    **{field: (float, Field(..., description=f"training column: {original}"))
       for field, original in zip(FIELD_ORDER, CARD["feature_names"])},
)


class PredictResponse(BaseModel):
    prediction: str
    class_id: int
    confidence: float


app = FastAPI(title=f"{CARD['name']} API", version="1.0")


@app.get("/health")
def health():
    return {"status": "ok", "model": CARD["name"], "source": CARD["source_course"]}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    row = [getattr(req, field) for field in FIELD_ORDER]
    proba = probabilities([row])[0]
    idx = int(np.argmax(proba))
    return PredictResponse(prediction=CARD["class_names"][idx],
                           class_id=idx,
                           confidence=round(float(proba[idx]), 4))

# Run locally: uvicorn main:app --host 0.0.0.0 --port 8000
