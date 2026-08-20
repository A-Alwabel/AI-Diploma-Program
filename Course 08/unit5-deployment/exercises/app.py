
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch, torchvision.models as models, numpy as np
from torchvision import transforms

app = FastAPI(title="DL Model API")
model = models.mobilenet_v2(weights="DEFAULT").eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

class PredictRequest(BaseModel):
    # TODO: Define your input schema (e.g. base64 image string or pixel array)
    pixels: list   # flat list of floats, shape (3,224,224)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: PredictRequest):
    try:
        # TODO: Parse input, run model, return class index + top-5 scores
        tensor = torch.tensor(req.pixels).reshape(1, 3, 224, 224)
        with torch.no_grad():
            logits = model(tensor)
        top5 = logits.topk(5).indices.tolist()[0]
        return {"predicted_class": top5[0], "top5": top5}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
