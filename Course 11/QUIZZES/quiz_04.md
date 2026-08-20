# Quiz 04 – Unit 4: Containers and Orchestration
## AIAT 125 - AI Model Deployment

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 4 (Docker images, Dockerfile, Kubernetes, CI/CD for ML deployment).
**Concepts from:** Unit 4 examples (Docker, Kubernetes) and related slides.
**Answers and rubrics:** Instructor only — see `DOCS/SOLUTIONS/quizzes/`.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What is the main difference between a **Docker image** and a **Docker container**?

a) They are the same thing
b) A Docker image is a read-only template (blueprint); a container is a running instance of that image
c) Containers are stored on disk; images run in memory
d) Images can only run locally

---

### Question 2 (10 points)
A **Kubernetes Pod** is:

a) A node in the cluster
b) The smallest deployable unit in Kubernetes, containing one or more containers that share networking and storage
c) A virtual machine
d) A Docker registry

---

### Question 3 (10 points)
**Horizontal scaling** in Kubernetes means:

a) Making each node faster (bigger CPU/RAM)
b) Adding more replica Pods (container instances) to distribute load
c) Increasing the model's hidden layer size
d) Adding more storage

---

### Question 4 (10 points)
In a **CI/CD pipeline for ML**, "CD" (Continuous Deployment) automates:

a) Collecting training data
b) Testing, building the Docker image, pushing to registry, and deploying the model when code passes all tests
c) Only model training
d) Only monitoring

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write a complete **Dockerfile** to containerize a FastAPI model-serving application:
- FROM python:3.11-slim
- WORKDIR /app
- COPY requirements.txt . and RUN pip install -r requirements.txt
- COPY . .
- EXPOSE 8000
- CMD to start the app: uvicorn app:app --host 0.0.0.0 --port 8000

Write all Dockerfile instructions in the correct order. Then write the docker build and docker run commands to build the image and start the container.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain the Kubernetes **Deployment** resource. What does it manage, and how does it ensure model-serving Pods are always running?

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
What is a **GitHub Actions CI/CD workflow** for ML deployment? Describe the key steps: trigger, test, build image, push to registry, deploy.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
Your team needs to update a Kubernetes-deployed model **without downtime**. Describe two deployment strategies (rolling update, blue-green, or canary) and recommend one for a critical production model.

**Answer key:** released by your instructor.

---

**Mapping:** CLO5; notebooks: Unit 4 container/orchestration examples.

**For:** AIAT 125 - AI Model Deployment
