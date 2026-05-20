# AIAT 125 - AI Model Deployment

## New Students: Start Here

Read [`START_HERE.md`](START_HERE.md) first.

## Course Overview

This course teaches how to deploy AI models to production: packaging artifacts, serving APIs, cloud hosting, containers, CI/CD, and MLOps monitoring.

**Course Code:** AIAT 125  
**Language:** English  
**Credit Hours:** 4  
**Lecture Hours:** 2  
**Practical Hours:** 4  
**Total Hours:** 96 (32 theoretical + 64 practical)

## Supporting Documents

Students may use these when needed:

- [`../docs/COURSE_MAP.md`](../docs/COURSE_MAP.md)
- [`../docs/SETUP_GUIDE.md`](../docs/SETUP_GUIDE.md)
- [`DOCS/EXAMPLES_ORDER.md`](DOCS/EXAMPLES_ORDER.md)
- [`DOCS/REQUIREMENTS_COURSE_11.md`](DOCS/REQUIREMENTS_COURSE_11.md)
- [`DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md`](DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md)
- [`DEPLOYMENT_LEARNING_JOURNEY.md`](DEPLOYMENT_LEARNING_JOURNEY.md) (course narrative across units)

## Course Learning Outcomes

By the end of the course, students should be able to:

- Explain the AI model deployment lifecycle and key production challenges.
- Package models for different runtimes (pickle, ONNX, PyTorch artifacts).
- Build and manage REST APIs for model inference.
- Use Docker and Kubernetes for reproducible, scalable deployment.
- Set up CI/CD pipelines for model delivery.
- Monitor deployed models and respond to drift, bias, and degradation.

## Unit Map

| Unit | Folder | Main Focus |
| ---- | ------ | ---------- |
| Unit 1 | `unit1-deployment-basics/` | Serialization, APIs, local deploy, validation |
| Unit 2 | `unit2-versioning-serving/` | Serving frameworks, versioning, batch vs real-time |
| Unit 3 | `unit3-cloud-deployment/` | AWS, Azure, GCP, cloud security and logging |
| Unit 4 | `unit4-containers-orchestration/` | Docker, Kubernetes, CI/CD |
| Unit 5 | `unit5-pipelines-monitoring/` | Monitoring, drift, retraining, MLOps tooling |

## How the units fit together

Read **[`DEPLOYMENT_LEARNING_JOURNEY.md`](DEPLOYMENT_LEARNING_JOURNEY.md)** once at the start and again before the final project. It connects packaging → serving → cloud → containers → MLOps into one deployment story.

## Student Workflow

Follow this pattern in every unit:

1. Read the unit `README.md`
2. Complete the numbered example notebooks in order (`01`, `02`, `03`, …)
3. Complete the unit exercise notebook
4. Take the unit quiz

For the whole course:

1. Start with `START_HERE.md`
2. Work through Units 1 to 5 in order
3. Complete the project in `PROJECTS/`
4. Finish with `ASSESSMENTS/Final_Exam.md`

## Important Note on Notebook Naming

Some units previously contained long descriptive notebook filenames alongside numbered lessons.

**Student rule:**

- Only the **numbered notebooks** (`01`, `02`, `03`, …) are the required study path.
- Long descriptive notebooks are **reference material** under `DOCS/REFERENCE_NOTEBOOKS/` unless your instructor assigns one.

## Course Structure

```text
Course 11/
├── README.md
├── START_HERE.md
├── DEPLOYMENT_LEARNING_JOURNEY.md
├── STUDENT_PROGRESS_CHECKLIST.md
├── unit1-deployment-basics/
├── unit2-versioning-serving/
├── unit3-cloud-deployment/
├── unit4-containers-orchestration/
├── unit5-pipelines-monitoring/
├── PROJECTS/
├── QUIZZES/
├── ASSESSMENTS/
└── DOCS/
```

**Created for:** AIAT 125 - AI Model Deployment  
**Last Updated:** 2026-05-17
