# Quiz 03 – Unit 3: Cloud Deployment and Infrastructure
## AIAT 125 - AI Model Deployment

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 3 (cloud platforms, AWS SageMaker, GCP Vertex AI, Azure ML, security, auto-scaling, monitoring and logging) plus the IaaS/CaaS/PaaS deployment tiers.
**Concepts from:** Unit 3 examples (cloud deployment, AWS SageMaker, security measures, monitoring and logging), the Unit 4 cloud-comparison example, and related slides.
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
**AWS SageMaker** provides which capability specifically for AI model deployment?

a) Only model training
b) Only data storage
c) End-to-end ML lifecycle: training, hosting endpoints, auto-scaling, A/B testing, and monitoring
d) Only containerization

---

### Question 2 (10 points)
**Serverless computing** (e.g., AWS Lambda, GCP Cloud Run) is preferred when:

a) The model requires a GPU for every request
b) Traffic is unpredictable or low-volume, and you want to pay only for actual usage without managing servers
c) Maximum performance is needed
d) Latency must be under 10ms

---

### Question 3 (10 points)
In cloud AI deployment, **auto-scaling** means:

a) The model automatically retrains when performance drops
b) The model's batch size is automatically adjusted
c) Gradients are automatically scaled during training
d) The infrastructure automatically adds or removes compute instances based on incoming traffic

---

### Question 4 (10 points)
Which security measure is most critical when deploying an AI model API on a cloud platform?

a) Authentication (API keys/OAuth), HTTPS, rate limiting, and input validation to prevent abuse
b) Using only HTTP (not HTTPS)
c) Making the API publicly open
d) Storing model weights in plaintext

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write Python pseudocode (boto3-style) to deploy a model on **AWS SageMaker**:
Given: model artifact at s3://my-bucket/model.tar.gz, execution_role_arn, container_image_uri.

Step 1: Create SageMaker model (specify container_image_uri, model_artifact, role).
Step 2: Create endpoint configuration (specify model name, instance_type="ml.t2.medium", initial_instance_count=1).
Step 3: Create endpoint from the configuration.
Step 4: Wait for endpoint to become InService.
Step 5: Invoke endpoint with sample input and print prediction.

Note: Structured pseudocode with correct step order is sufficient; exact boto3 syntax not required.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Compare the three tiers of cloud ML deployment taught in this course — **IaaS, CaaS, and PaaS**. For each, say what you provide, what you still have to manage, and give one platform example. Which tier is most commonly used for deploying custom AI models, and why?

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Once a model is serving live traffic you have to monitor it. (a) Explain the difference between **p50 and p99 latency**, and say which one you would alert on and why. (b) In production you usually have **no ground-truth labels**, so accuracy cannot be computed directly — name **two** proxy signals covered in this unit that indicate the model is degrading, and explain what each one tells you.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A startup deploys a fraud detection model on AWS. During peak hours, requests jump from 100/min to 10,000/min. Describe how you would architect this using **auto-scaling, load balancing**, and appropriate AWS services.

**Answer key:** released by your instructor.

---

**Mapping:** CLO4; notebooks: Unit 3 cloud deployment examples.

**For:** AIAT 125 - AI Model Deployment
