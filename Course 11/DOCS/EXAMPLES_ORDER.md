# Recommended Order for Example Notebooks (Course 11)

Use this order so examples build from **local packaging** → **serving** → **cloud** → **containers** → **MLOps**.

## Order rule

**Always do notebooks in file number order: 01 → 02 → 03 → …** in each unit.  
Follow the list in each unit `README.md`, not alphabetical sorting in your file browser.

---

## Unit 1: Introduction to AI Model Deployment (`unit1-deployment-basics/examples/`)

| Step | Notebook | Focus |
| ---- | -------- | ----- |
| 1 | `01_model_serving_api.ipynb` | REST API concepts, local serving |
| 2 | `02_model_packaging.ipynb` | Pickle, joblib, packaging |
| 3 | `03_local_deployment_testing.ipynb` | Local test harness |
| 4 | `04_model_preparation_saving.ipynb` | Prepare artifacts for deploy |
| 5 | `05_model_validation_testing.ipynb` | Pre-deploy validation |
| 6 | `06_monitoring_updating_models.ipynb` | Logs, feedback, updates |

**Exercise:** `exercises/01_packaging_exercise.ipynb` → **Quiz:** `QUIZZES/quiz_01.md`

---

## Unit 2: Model Packaging and Serving (`unit2-versioning-serving/examples/`)

| Step | Notebook | Focus |
| ---- | -------- | ----- |
| 1 | `01_flask_api_deployment.ipynb` | Flask serving |
| 2 | `02_fastapi_deployment.ipynb` | FastAPI serving |
| 3 | `03_model_versioning.ipynb` | Versioning and metadata |
| 4 | `04_saving_loading_models_pickle_onnx.ipynb` | Serialization formats |
| 5 | `05_tensorflow_serving_torchserve.ipynb` | Serving frameworks |
| 6 | `06_batch_vs_realtime_inference.ipynb` | Batch vs streaming |
| 7 | `07_kubernetes_scaling.ipynb` | Scaling served models |

**Exercise:** `exercises/01_api_deployment_exercise.ipynb` → **Quiz:** `QUIZZES/quiz_02.md`

---

## Unit 3: Cloud Deployment and Infrastructure (`unit3-cloud-deployment/examples/`)

| Step | Notebook | Focus |
| ---- | -------- | ----- |
| 1 | `01_cloud_deployment.ipynb` | Cloud deployment overview |
| 2 | `02_aws_sagemaker.ipynb` | AWS SageMaker patterns |
| 3 | `03_azure_ml_deployment.ipynb` | Azure ML |
| 4 | `04_gcp_vertex_ai.ipynb` | GCP Vertex AI |
| 5 | `05_security_measures.ipynb` | Auth, encryption, access |
| 6 | `06_monitoring_logging_cloud.ipynb` | Cloud logging and monitoring |

**Exercise:** `exercises/01_cloud_deployment_exercise.ipynb` → **Quiz:** `QUIZZES/quiz_03.md`

---

## Unit 4: Containers and Orchestration (`unit4-containers-orchestration/examples/`)

| Step | Notebook | Focus |
| ---- | -------- | ----- |
| 1 | `01_docker_deployment.ipynb` | Docker images for models |
| 2 | `02_kubernetes_deployment.ipynb` | Kubernetes rollout |
| 3 | `03_cloud_deployment_comparison.ipynb` | Compare cloud options |
| 4 | `04_cicd_pipelines.ipynb` | CI/CD for model delivery |

**Exercise:** `exercises/01_docker_and_containerization_exercise.ipynb` → **Quiz:** `QUIZZES/quiz_04.md`

---

## Unit 5: Monitoring and Maintenance of Deployed AI Models (`unit5-pipelines-monitoring/examples/`)

| Step | Notebook | Focus |
| ---- | -------- | ----- |
| 1 | `01_model_monitoring.ipynb` | Performance monitoring |
| 2 | `02_retraining_pipeline.ipynb` | Retraining workflows |
| 3 | `03_alerting_incident_management.ipynb` | Alerts and incidents |
| 4 | `04_drift_detection.ipynb` | Data / concept drift |
| 5 | `05_experiment_tracking_mlflow_wandb.ipynb` | Experiment tracking |
| 6 | `06_model_versioning_reproducibility.ipynb` | Reproducibility |
| 7 | `07_ab_testing_canary_deployment.ipynb` | A/B and canary deploy |

**Exercise:** `exercises/01_monitoring_exercise.ipynb` → **Quiz:** `QUIZZES/quiz_05.md`

---

## After Unit 5

Complete the graded course practical `final_exercise.ipynb` (course root), then `ASSESSMENTS/Final_Exam.md`.
