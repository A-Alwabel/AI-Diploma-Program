# Unit 5: Monitoring and Maintenance of Deployed AI Models

Folder: `unit5-pipelines-monitoring/` · **Unit hours:** 20

## Where this unit sits in the course

Deployment does not end at launch. This unit covers living models: monitoring, drift, retraining, experiments, and safe rollouts.

## Prerequisites

- Units 1–4 complete
- `mlflow` installed (see [`../START_HERE.md`](../START_HERE.md) and `../requirements-course11.txt`)

## Learning goals

- Track model performance and set alerts
- Detect drift and plan retraining
- Use experiment tracking (MLflow-style patterns)
- Run A/B tests and canary deployments
- Keep models reproducible across retrains

## Study order (required)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

1. **[CORE]** `examples/01_model_monitoring.ipynb` — performance monitoring of a deployed model
2. **[CORE]** `examples/02_retraining_pipeline.ipynb` — retraining workflows
3. **[HOMEWORK]** `examples/03_alerting_incident_management.ipynb` — alerts and incident handling
4. **[CORE]** `examples/04_drift_detection.ipynb` — data and concept drift detection
5. **[CORE]** `examples/05_experiment_tracking_mlflow_wandb.ipynb` — experiment tracking (MLflow, W&B patterns)
6. **[CORE]** `examples/06_model_versioning_reproducibility.ipynb` — reproducibility across model versions
7. **[CORE]** `examples/07_ab_testing_canary_deployment.ipynb` — A/B testing and canary rollout

## Exercise and quiz

1. `exercises/01_monitoring_exercise.ipynb` (solution released by your instructor)
2. `../QUIZZES/quiz_05.md`

After this unit, re-read [`../DEPLOYMENT_LEARNING_JOURNEY.md`](../DEPLOYMENT_LEARNING_JOURNEY.md), then complete the graded course practical [`../final_exercise.ipynb`](../final_exercise.ipynb) before the final exam.
