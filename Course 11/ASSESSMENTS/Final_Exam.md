# Final Exam: AI Model Deployment
## AIAT 125

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. In Parts 2–4, show your reasoning — partial credit is awarded for a correct mechanism even when the detail is incomplete. Part 1 is marked on the chosen letter only.

**Marking scheme:** Part 1 (Q1–Q6): 5 pts each = 30. Part 2 (Q7–Q9): 10 pts each = 30. Part 3 (Q10: 15 pts, Q11: 10 pts) = 25. Part 4 (Q12): 15 pts. **Total: 100.**

---

## Part 1: Multiple Choice (30 points)

Every option below is something a reasonable person might believe. Choose the one that is correct.

### Question 1 (5 points)
**CLO1:** What is model deployment?

A) Saving the trained model to a file so it can be reloaded later  
B) Making trained models available for use in production  
C) Retraining the model on the full dataset before release  
D) Measuring the model's accuracy on a held-out test set

---

### Question 2 (5 points)
**CLO2:** You have a trained scikit-learn model. It must be called from a Java backend service and must also run inside a mobile app that cannot host a Python interpreter. Which packaging choice makes that possible?

A) `pickle`, because Python runs on every major operating system  
B) `joblib` with `compress=3`, because it makes the smallest artifact  
C) ONNX, because the graph runs on any ONNX runtime without Python  
D) JSON of the learned parameters, because every language parses JSON

---

### Question 3 (5 points)
**CLO3:** What is the main advantage of REST APIs for model serving?

A) Standardized interface, language-agnostic, scalable  
B) Lower latency than an in-process `model.predict()` call  
C) Automatic validation of requests against the model's schema  
D) Automatic scaling of the service as request volume grows

---

### Question 4 (5 points)
**CLO4:** What does Docker provide for ML deployment?

A) Rescheduling a failed container onto a healthy node  
B) Identical images from two builds of the same Dockerfile  
C) Portability of the platform, not just the runtime  
D) Containerization for consistent environments

---

### Question 5 (5 points)
**CLO5:** Your GitHub Actions workflow has four jobs chained with `needs:` — run `pytest`, train the model, build and push the Docker image, then `kubectl set image`. Every job passes and the rollout completes, but the model now serving traffic is only 60% accurate. Which missing stage would have prevented it from reaching production?

A) A model-validation gate that fails the build when metrics miss threshold  
B) A smoke test that issues known-answer requests to the live endpoint  
C) A rollback step that reverts the Deployment when a later job fails  
D) Image tags carrying the commit SHA so every release stays traceable

---

### Question 6 (5 points)
**CLO6:** A deployed classifier's dashboards look healthy: error rate under 1%, p99 latency inside the SLO, mean prediction confidence 0.9, and a KS test on every input feature returns p > 0.05. Then the first ground-truth labels arrive and accuracy has fallen from 0.95 to 0.72. What is the most likely explanation?

A) The service has stopped receiving traffic, so the accuracy figure is unreliable  
B) Data drift in the inputs; retraining on recent data will restore accuracy  
C) CPU saturation on the serving pods is degrading the quality of predictions  
D) Concept drift: P(Y|X) has changed, which input-only tests cannot detect

---

## Part 2: Short Answer Questions (30 points)

### Question 7 (10 points)
**CLO1, CLO2:** Explain the complete model deployment pipeline. Include packaging, versioning, serving, and monitoring steps.

---

### Question 8 (10 points)
**CLO3, CLO4:** Compare different deployment approaches: REST API, Docker containers, and cloud platforms. When would you use each?

---

### Question 9 (10 points)
**CLO6:** Explain model drift and data drift. How would you detect and handle each?

---

## Part 3: Practical/Coding Questions (25 points)

### Question 10 (15 points)
**CLO3:** Create a complete Flask API for serving a machine learning model:
1. Load trained model
2. Create prediction endpoint
3. Add input validation
4. Handle errors
5. Include health check endpoint

---

### Question 11 (10 points)
**CLO4:** Write a Dockerfile for containerizing a Flask ML API. Include all necessary dependencies.

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
**CLO5, CLO6:** Design a production ML deployment system for a recommendation engine serving 1 million users:
1. Architecture design (API, containers, orchestration)
2. CI/CD pipeline
3. Monitoring and alerting strategy
4. Scalability considerations
5. Failure handling and rollback procedures

---

**End of Exam**

**Good Luck!**
