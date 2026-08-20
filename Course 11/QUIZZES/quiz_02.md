# Quiz 02 – Unit 2: Model Packaging and Serving
## AIAT 125 - AI Model Deployment

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 2 (serialization: Pickle, ONNX, Docker, TorchServe, batch vs real-time inference).
**Concepts from:** Unit 2 examples (saving/loading models, ONNX, serving) and related slides.
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
A key **advantage of ONNX** over Pickle for model deployment:

a) ONNX files are always smaller
b) ONNX provides a standard cross-framework format that runs in optimized runtimes (ONNX Runtime) on various hardware
c) ONNX only works with PyTorch
d) Pickle is faster for inference

---

### Question 2 (10 points)
**TorchServe** is primarily used for:

a) Training PyTorch models
b) Serving PyTorch models in production via REST/gRPC APIs with multi-model support, logging, and metrics
c) Visualizing model training
d) Converting models to ONNX

---

### Question 3 (10 points)
In a Dockerfile, the instruction `COPY model.pkl /app/model.pkl` is used to:

a) Download the model from the internet
b) Copy the model file from the host into the container image at build time
c) Run the model
d) Install Python dependencies

---

### Question 4 (10 points)
**Batch inference** is preferred over real-time inference when:

a) Latency must be under 100ms
b) Processing large volumes of data at scheduled intervals where latency is not critical (e.g., overnight batch scoring)
c) Only one request arrives at a time
d) The model is very small

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write Python code to **export a PyTorch model to ONNX** and run inference:
- Define model: nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 3)).
- Export to ONNX using torch.onnx.export: input shape (1, 4), opset_version=11, output_names=["output"].
- Load with onnxruntime.InferenceSession("model.onnx").
- Run inference with np.random.randn(1, 4).astype(np.float32) and print the output.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain the difference between **REST** and **gRPC** for model serving. When would you choose gRPC over REST?

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
What is **load balancing** in model serving, and why is it needed when serving a model to many concurrent users?

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A deployed model API has 3-second response time, but the business requirement is 200ms. Name **three** concrete optimizations (e.g., quantization, caching, batching, async inference) and the trade-off for each.

**Answer key:** released by your instructor.

---

**Mapping:** CLO2, CLO3; notebooks: Unit 2 packaging/serving examples.

**For:** AIAT 125 - AI Model Deployment
