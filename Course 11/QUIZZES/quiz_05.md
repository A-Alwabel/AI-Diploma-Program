# Quiz 05 – Unit 5: Monitoring, Maintenance, and MLOps
## AIAT 125 - AI Model Deployment

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 5 (model monitoring, drift detection, MLflow, experiment tracking, retraining strategies).
**Concepts from:** Unit 5 examples (monitoring, MLflow, pipelines) and related slides.
**Answers and rubrics:** Instructor only — see `DOCS/SOLUTIONS/quizzes/`.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
**Model drift** in production occurs when:

a) The model is too large
b) The statistical properties of input data or the input-output relationship change over time, causing performance degradation
c) The model is updated too frequently
d) The server runs out of memory

---

### Question 2 (10 points)
**MLflow** is used primarily for:

a) Deploying Docker containers
b) Experiment tracking — logging parameters, metrics, and artifacts for each run, enabling comparison and reproducibility
c) Data preprocessing
d) Writing Kubernetes manifests

---

### Question 3 (10 points)
In **A/B testing for model deployment**, you:

a) Train two models and pick the better one before deployment
b) Route a percentage of real production traffic to both current model (A) and new model (B), measure metrics, and decide which performs better
c) Test models only offline
d) A/B testing is only for web UI design

---

### Question 4 (10 points)
**Canary deployment** releases a new model version by:

a) Immediately replacing the old model
b) Gradually routing a small percentage (e.g., 5-10%) of traffic to the new version, monitoring for issues before full rollout
c) Running both models simultaneously for all users
d) Only deploying to development environments

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write Python code using **MLflow** to track a model training experiment:
- import mlflow and relevant modules.
- Start a run with mlflow.start_run().
- Log parameters: learning_rate=0.01, epochs=50, batch_size=32.
- Log metrics: train_accuracy=0.92, val_accuracy=0.89.
- Log a model artifact using mlflow.sklearn.log_model or mlflow.pytorch.log_model.
- End the run and print the run_id.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
What is **data drift** vs **concept drift**? Give a concrete example of each in a real-world AI system (e.g., fraud detection, recommendation).

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Describe a **model retraining strategy** for a production system. What triggers retraining (performance threshold, scheduled), and how do you ensure the new model is safe before replacing the old one?

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A production recommendation model's click-through rate dropped from 8% to 4% over 6 months. Describe a **systematic diagnosis**: what monitoring data to check first, how to determine if it's data drift or model degradation, and what retraining strategy to apply.

**Answer key:** released by your instructor.

---

**Mapping:** CLO6; notebooks: Unit 5 monitoring/MLOps examples.

**For:** AIAT 125 - AI Model Deployment
