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

a) Speed up training by storing the weights and gradients in int8 from the first epoch onwards  
b) Replace the need for a GPU  
c) Reduce model size and speed up inference with often minimal accuracy loss when done carefully  
d) Improve accuracy, because rounding the weights removes small noise that the model learned from the data  

---

### Question 2 (10 points)
What is **knowledge distillation**?

a) Removing layers from the model  
b) Training a smaller “student” model to mimic the outputs of a larger “teacher” model to get similar performance with less compute  
c) Copying the teacher’s weights into a student with the same architecture, so that the student needs no training of its own  
d) Rounding the teacher’s weights to a lower precision (e.g. int8) so that the same model runs on smaller hardware  

---

### Question 3 (10 points)
**ONNX** (Open Neural Network Exchange) is useful because:

a) It speeds up training by running the training loop on an optimized computation graph instead of eager Python code  
b) It replaces TensorFlow and PyTorch with its own training framework, so models are written once in ONNX  
c) It shrinks the exported model to int8 as part of the export step, so no separate quantization pass is needed  
d) It provides a standard format to export models so they can run across frameworks (e.g. TensorFlow, PyTorch) and runtimes  

---

### Question 4 (10 points)
Why do we expose a model via a **REST API** (e.g. Flask or FastAPI) in production?

a) So other services or applications can send requests and get predictions over the network (HTTP)  
b) So the model keeps learning from each request it receives in production, without a separate training job  
c) Because an HTTP call to the model is faster than calling it in-process from the same Python program  
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
