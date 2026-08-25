# Unit 4: Containers and Orchestration

Folder: `unit4-containers-orchestration/` · **Unit hours:** 20

## Where this unit sits in the course

Cloud platforms often run containers. This unit makes environments reproducible (Docker) and scalable (Kubernetes, CI/CD).

## Prerequisites

- Units 1–3 complete
- Docker Desktop or compatible runtime (for hands-on cells)

## Learning goals

- Build Docker images that bundle model + dependencies
- Deploy containerized models with Kubernetes concepts
- Compare cloud deployment options in practice
- Wire CI/CD steps for automated model delivery

## Study order (required)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

1. **[CORE]** `examples/01_docker_deployment.ipynb` — Docker images for model services
2. **[CORE]** `examples/02_kubernetes_deployment.ipynb` — Kubernetes rollout of a model service
3. **[CORE]** `examples/03_cloud_deployment_comparison.ipynb` — comparing container deployment options across clouds
4. **[CORE]** `examples/04_cicd_pipelines.ipynb` — CI/CD steps for model delivery

### Supporting files (used by the notebooks)

- `examples/app/` — sample FastAPI service with `Dockerfile`, `Dockerfile.multistage`, training script, and saved model
- `examples/k8s/` — Kubernetes manifests (`deployment.yaml`, `service.yaml`, `hpa.yaml`)
- `examples/tests/`, `examples/smoke_test.py`, `examples/validate_model.py` — CI/CD test scripts

## Exercise and quiz

1. `exercises/01_docker_and_containerization_exercise.ipynb` (solution released by your instructor)
2. `../QUIZZES/quiz_04.md`
