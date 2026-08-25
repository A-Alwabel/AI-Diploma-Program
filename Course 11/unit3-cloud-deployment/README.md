# Unit 3: Cloud Deployment and Infrastructure

Folder: `unit3-cloud-deployment/` · **Unit hours:** 19

## Where this unit sits in the course

You move from your machine to managed cloud endpoints — same model artifact, different ops concerns (IAM, logging, cost).

## Prerequisites

- Units 1–2 complete
- Optional: cloud sandbox or instructor-provided credentials for AWS/Azure/GCP demos (see [`../DOCS/CLOUD_CREDENTIALS_SETUP.md`](../DOCS/CLOUD_CREDENTIALS_SETUP.md))

**Note for students:** Many cloud cells run **locally simulated** workflows (no billing account required). Cells that need live cloud keys are called out in the notebook — ask your instructor before running those.

## Learning goals

- Compare major cloud ML platforms (SageMaker, Azure ML, Vertex AI)
- Describe deployment strategies on cloud (batch vs online)
- Apply security basics (auth, encryption, access control)
- Configure monitoring and logging for cloud-hosted models

## Study order (required)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

1. **[CORE]** `examples/01_cloud_deployment.ipynb` — cloud deployment overview
2. **[CORE]** `examples/02_aws_sagemaker.ipynb` — AWS SageMaker patterns
3. **[CORE]** `examples/03_azure_ml_deployment.ipynb` — Azure ML deployment
4. **[CORE]** `examples/04_gcp_vertex_ai.ipynb` — GCP Vertex AI deployment
5. **[CORE]** `examples/05_security_measures.ipynb` — auth, encryption, access control
6. **[CORE]** `examples/06_monitoring_logging_cloud.ipynb` — cloud logging and monitoring

## Exercise and quiz

1. `exercises/01_cloud_deployment_exercise.ipynb` (solution released by your instructor)
2. `../QUIZZES/quiz_03.md`
