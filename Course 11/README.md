# AIAT 125 - Deploying AI Models

## New Students: Start Here

Read [`START_HERE.md`](START_HERE.md) first.

## Course Overview

This course teaches how to deploy AI models to production: packaging artifacts, serving APIs, cloud hosting, containers, CI/CD, and monitoring of deployed models.

**Course Code:** AIAT 125
**Language:** English
**Credit hours:** 4 · **Contact hours:** 6/week · **Total training hours:** 96 (theory+practical)

## Prerequisites

- Semester 1 (AIAT 111–116)
- AIAT 122 — Deep Learning (Course 08): train and save models

## Units

| Unit | Official Title | Folder | Hours |
| ---- | -------------- | ------ | ----- |
| 1 | Introduction to AI Model Deployment | `unit1-deployment-basics/` | 18 |
| 2 | Model Packaging and Serving | `unit2-versioning-serving/` | 19 |
| 3 | Cloud Deployment and Infrastructure | `unit3-cloud-deployment/` | 19 |
| 4 | Containers and Orchestration | `unit4-containers-orchestration/` | 20 |
| 5 | Monitoring and Maintenance of Deployed AI Models | `unit5-pipelines-monitoring/` | 20 |

## Course Learning Outcomes

By the end of the course, students should be able to:

- Explain the AI model deployment lifecycle and key production challenges.
- Package models for different runtimes (pickle, ONNX, PyTorch artifacts).
- Build and manage REST APIs for model inference.
- Use Docker and Kubernetes for reproducible, scalable deployment.
- Set up CI/CD pipelines for model delivery.
- Monitor deployed models and respond to drift and degradation.

## Study Path

Follow this pattern in every unit:

1. Read the unit `README.md`
2. Complete the numbered example notebooks in file order (`01`, `02`, …)
3. Complete the unit exercise notebook
4. Take the unit quiz in `QUIZZES/`

For the whole course:

1. Start with [`START_HERE.md`](START_HERE.md)
2. Work through Units 1 to 5 in order
3. Complete [`final_exercise.ipynb`](final_exercise.ipynb) — the graded course practical (100 points, covers all six CLOs). Its solution is released by your instructor.
4. Finish with [`ASSESSMENTS/Final_Exam.md`](ASSESSMENTS/Final_Exam.md)

`PROJECTS/ML_Deployment_Pipeline/` is used only if your instructor assigns it.

## How the units fit together

Read [`DEPLOYMENT_LEARNING_JOURNEY.md`](DEPLOYMENT_LEARNING_JOURNEY.md) once at the start and again before the final exercise. It connects packaging → serving → cloud → containers → monitoring into one deployment story.

## Supporting Documents

- [`../docs/SETUP_GUIDE.md`](../docs/SETUP_GUIDE.md) — environment setup for the whole diploma
- [`DOCS/EXAMPLES_ORDER.md`](DOCS/EXAMPLES_ORDER.md) — notebook order for every unit
- [`DOCS/REQUIREMENTS_COURSE_11.md`](DOCS/REQUIREMENTS_COURSE_11.md) — packages needed per unit (see also [`requirements-course11.txt`](requirements-course11.txt))
- [`DOCS/CLOUD_CREDENTIALS_SETUP.md`](DOCS/CLOUD_CREDENTIALS_SETUP.md) — optional cloud accounts for Unit 3 live labs
- [`DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md`](DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md) — what to do when a notebook runs but is confusing

## Course Structure

```text
Course 11/
├── README.md
├── START_HERE.md
├── DEPLOYMENT_LEARNING_JOURNEY.md
├── STUDENT_PROGRESS_CHECKLIST.md
├── requirements-course11.txt
├── final_exercise.ipynb        # graded course practical
├── unit1-deployment-basics/
├── unit2-versioning-serving/
├── unit3-cloud-deployment/
├── unit4-containers-orchestration/
├── unit5-pipelines-monitoring/
├── PROJECTS/
├── QUIZZES/
├── ASSESSMENTS/
├── CASE_STUDIES/
└── DOCS/
```
