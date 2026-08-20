# Quiz 05 – Unit 5: Model Optimization and Deployment
## AIAT 122 - Deep Learning

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 5 (quantization, pruning, distillation, ONNX, serving, Flask/FastAPI).  
**Concepts from:** Unit 5 examples 01 (optimization), 03 (ONNX), 06 (Flask/FastAPI), 07 (quantization). Unit 5 has no slides; concepts are from the notebooks.  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
**Model quantization** (e.g. converting weights from float32 to int8) is used to:

a) Increase model size  
b) **Reduce model size and speed up inference** with often minimal accuracy loss when done carefully  
c) Only improve accuracy  
d) Replace the need for a GPU  

---

### Question 2 (10 points)
What is **knowledge distillation**?

a) Removing layers from the model  
b) **Training a smaller “student” model to mimic the outputs of a larger “teacher” model** to get similar performance with less compute  
c) Converting to ONNX only  
d) Only used in training  

---

### Question 3 (10 points)
**ONNX** (Open Neural Network Exchange) is useful because:

a) It is the only way to train models  
b) It provides a **standard format** to export models so they can run across frameworks (e.g. TensorFlow, PyTorch) and runtimes  
c) It replaces TensorFlow  
d) It is only for reinforcement learning  

---

### Question 4 (10 points)
Why do we expose a model via a **REST API** (e.g. Flask or FastAPI) in production?

a) To train the model  
b) So **other services or applications can send requests and get predictions** over the network (HTTP)  
c) Only to reduce latency  
d) To replace the need for a database  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write a **minimal FastAPI** application that: (1) defines a POST endpoint `/predict` that accepts a JSON body with a list of numbers (e.g. `{"features": [0.1, 0.2, 0.3]}`), (2) uses a dummy predictor (e.g. return the sum of the list or a fixed class) and returns a JSON response (e.g. `{"prediction": 0}`). No need to load a real model file.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Give **two** trade-offs when deploying a model (e.g. latency vs accuracy, model size vs performance, batch vs real-time).

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
What is **model pruning**, and what is one benefit and one risk?

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A team deploys a model with **2 s latency** but the product requirement is **200 ms**. Name **two** concrete optimization strategies (e.g. quantization, smaller model, batching) and **one** trade-off to consider.

**Answer key:** released by your instructor.

---

**Mapping:** CLO3, CLO4; notebooks: 01_model_optimization, 06_flask_fastapi_deployment, 07_model_optimization_quantization.

**For:** AIAT 122 - Deep Learning
