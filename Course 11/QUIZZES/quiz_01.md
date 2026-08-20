# Quiz 01 – Unit 1: AI Model Deployment Basics
## AIAT 125 - AI Model Deployment

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 1 (deployment lifecycle, model serialization, REST APIs, Docker basics).
**Concepts from:** Unit 1 examples (local deployment testing) and related slides.
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What is the main purpose of **model deployment** in the AI lifecycle?

a) To train the model
b) To make a trained model available to users or other systems so it can produce predictions on new data
c) To evaluate model accuracy offline
d) To visualize model performance

---

### Question 2 (10 points)
Which serialization format is **cross-framework** and allows AI models to run across runtimes (TF, PyTorch, etc.)?

a) Pickle
b) ONNX (Open Neural Network Exchange)
c) JSON
d) CSV

---

### Question 3 (10 points)
In a **REST API** for model serving, the client sends data and receives predictions via:

a) Direct database access
b) HTTP requests (typically POST with JSON body) and receives JSON responses
c) File transfer only
d) WebSocket only

---

### Question 4 (10 points)
**Docker** is used in AI deployment to:

a) Train models faster
b) Package the model, code, and all dependencies into a portable container that runs consistently across environments
c) Monitor model performance
d) Replace cloud services

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write a minimal **FastAPI** application to serve an ML model:
- Import FastAPI and BaseModel from pydantic.
- Define PredictInput(BaseModel) with field features: list[float].
- Create POST endpoint /predict that accepts PredictInput and returns {"prediction": sum(features)}.
- Include app = FastAPI() and the correct uvicorn run command.
- Show how you would test this with a requests.post() call.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Describe the **AI model deployment lifecycle**. Name the four key stages and explain what happens at each.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
What is **model drift**, and why is it a concern? Give one example of data drift and one example of concept drift.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A data scientist trains a model locally (95% accuracy) but when deployed to a colleague's machine it fails with ModuleNotFoundError. What is the root cause, and how does Docker solve this problem?

**Answer key:** released by your instructor.

---

**Mapping:** CLO1, CLO2, CLO3; notebooks: Unit 1 deployment examples.

**For:** AIAT 125 - AI Model Deployment
