# Unit 4: Introduction to Machine Learning

**Unit hours:** 20 (of 96 total training hours)

## Prerequisites

- Unit 3: Data Visualization (`../unit3-visualization/`)
- Comfortable with pandas data manipulation
- AIAT 114 - Machine Learning Algorithms and Applications (Course 04), where these algorithms were first taught

## What This Unit Covers

**ML at scale — a recap that reinforces AIAT 114.** Course 04 already taught these algorithms in depth; this unit deliberately revisits them from the data-science-workflow angle rather than re-teaching them from scratch. The focus here is: preparing real data for ML, running the scikit-learn workflow end to end (regression, classification, evaluation, hyperparameter tuning, K-means), applying it to a complete real-world problem, and — the part that is new — what happens to training and evaluation **cost** as data grows, leading into CPU-vs-GPU training and Unit 5's scaling tools. If an algorithm feels familiar, that is by design: treat it as reinforcement and focus on the workflow and cost measurements.

## Examples (run in order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

| # | Notebook | Description | Tier |
|---|----------|-------------|------|
| 01 | `examples/01_pandas_data_manipulation.ipynb` | Data manipulation with pandas for ML workflows | **HOMEWORK** |
| 02 | `examples/02_data_preparation_ml_tasks.ipynb` | Preparing data for ML: splits, scaling, encoding | **CORE** |
| 03 | `examples/03_implementing_ml_models_sklearn.ipynb` | Implementing regression and classification with scikit-learn | **CORE** |
| 04 | `examples/04_linear_regression.ipynb` | Linear regression in depth | **HOMEWORK** |
| 05 | `examples/05_supervised_learning_logistic_regression.ipynb` | Supervised learning with logistic regression | **HOMEWORK** |
| 06 | `examples/06_classification.ipynb` | Classification basics and common classifiers | **HOMEWORK** |
| 07 | `examples/07_model_evaluation.ipynb` | Evaluation metrics, confusion matrices, ROC curves | **CORE** |
| 08 | `examples/08_hyperparameter_tuning_grid_random_search.ipynb` | Hyperparameter tuning with grid search and random search | **CORE** |
| 09 | `examples/09_unsupervised_learning_kmeans.ipynb` | Unsupervised learning with K-means clustering | **HOMEWORK** |
| 10 | `examples/10_clustering_unsupervised.ipynb` | Clustering techniques and cluster evaluation | **HOMEWORK** |
| 11 | `examples/11_real_world_problem_solving.ipynb` | End-to-end problem solving with supervised and unsupervised learning | **CORE** |
| 12 | `examples/12_cpu_vs_gpu_ml.ipynb` | CPU vs GPU ML performance comparison (optional GPU) | **CORE** |

## Exercise

- `exercises/exercise_01.ipynb` - machine learning practice (a script version `exercise_01.py` is also provided)

## Quiz

- `../QUIZZES/Quiz_04_ML_Introduction.md`
- Answer keys are released by your instructor.

## Learning Path

1. Read this README
2. Run the examples in numeric order
3. Complete `exercises/exercise_01.ipynb`
4. Take Quiz 04

**Next unit:** `../unit5-scaling/`
