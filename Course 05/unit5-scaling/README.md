# Unit 5: Extending the Scope of Data Science

**Unit hours:** 20 (of 96 total training hours)

## Prerequisites

- Units 1-4 of this course
- Comfortable with pandas, visualization, and basic scikit-learn ML

## What This Unit Covers

Scaling data science beyond a single machine and into production: big data concepts, distributed computing with Dask and PySpark, GPU workflows with RAPIDS, production pipelines, performance optimization, large dataset handling, deployment, model monitoring, and pipeline automation.

## Examples (run in order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

| # | Notebook | Description | Tier |
|---|----------|-------------|------|
| 01 | `examples/01_big_data_theory.ipynb` | Big data characteristics and distributed computing theory | **CORE** |
| 02 | `examples/02_dask_distributed.ipynb` | Distributed computing with Dask | **CORE** |
| 03 | `examples/03_pyspark_distributed.ipynb` | Distributed data processing with PySpark (optional dependency) | **CORE** |
| 04 | `examples/04_rapids_workflows.ipynb` | GPU workflows with RAPIDS (optional GPU) | **CORE** |
| 05 | `examples/05_production_pipelines.ipynb` | Building production data pipelines | **ENRICHMENT** |
| 06 | `examples/06_performance_optimization.ipynb` | Profiling and optimizing data processing performance | **HOMEWORK** |
| 07 | `examples/07_large_datasets.ipynb` | Techniques for handling large datasets | **HOMEWORK** |
| 08 | `examples/08_deployment.ipynb` | Deploying models and pipelines | **CORE** |
| 09 | `examples/09_model_monitoring.ipynb` | Model monitoring and performance tracking | **CORE** |
| 10 | `examples/10_data_pipeline_automation.ipynb` | Automating data pipelines | **ENRICHMENT** |
| E15 | `enrichment/E15_zero_shot_forecasting_honestly.ipynb` | Seasonal-naive, Holt-Winters and Theta forecasts written from their formulas, backtested on rolling origins before and across the March-2020 break — then what a fair comparison against a zero-shot foundation model would require | **ENRICHMENT** |

Notebooks in `enrichment/` are **not examinable** - they connect this unit to current practice and appear in no quiz or exam.

PySpark and RAPIDS are optional - see `../DOCS/OPTIONAL_DEPENDENCIES.md`. The other files in `examples/` (`large_dataset.csv`, `deployed_model.pkl`, logs, metadata) are inputs/outputs of these notebooks.

## Exercise

- `exercises/exercise_01.ipynb` - scaling and production practice (a script version `exercise_01.py` is also provided)

## Quiz

- `../QUIZZES/Quiz_05_Scaling_Production.md`
- Answer keys are released by your instructor.

## Learning Path

1. Read this README
2. Run the examples in numeric order
3. Complete `exercises/exercise_01.ipynb`
4. Take Quiz 05

**Next:** final exam (`../ASSESSMENTS/Final_Exam.md`) and the capstone project (`../PROJECTS/01_Data_Pipeline/`)
