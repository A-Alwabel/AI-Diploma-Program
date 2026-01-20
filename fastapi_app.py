
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="ML Model API", version="1.0.0")

# Load model
with open('deployment_model.pkl', 'rb') as f:
    model = pickle.load(f)

class PredictionRequest(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: int
    probabilities: list[float]
    status: str

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Predict endpoint with automatic API documentation"""
    try:
        features = np.array(request.features).reshape(1, -1)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0].tolist()
        
        return PredictionResponse(
            prediction=int(prediction), probabilities=probability,
            status='success'
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}

# Run with: uvicorn fastapi_app:app --reload
