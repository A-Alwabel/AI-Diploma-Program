# Unit 5: AI-Based Learning Models

**Course:** AIAT 112 - Python for Artificial Intelligence
**Unit hours:** 20 (7 theory + 13 practical)

## What This Unit Teaches

Building and evaluating common machine learning models in Python, and
comparing model families and their trade-offs, including deployment
considerations.

This unit is a first pass over classic ML: Course 04 (AIAT 114) re-teaches
each of these model families in depth, so treat this as the preview that the
machine-learning course deepens.

Lesson 03 delivers the unit's official "model deployment and maintenance"
bullet: the model from lesson 01 saved, served over HTTP and defended against
malformed input.

Lesson 02 is a bridge, not an official bullet of this unit. Transfer learning
belongs officially to AIAT 122 (Deep Learning), where you will meet it again.
It sits here because it is the single idea that makes the rest of this diploma
comprehensible: four ways to use a pretrained network, put on one axis of cost,
so that by the time AIAT 122 arrives you already know why nobody trains from
scratch. Treat it as enrichment if the unit's time is short.

## Prerequisites

- Unit 4: Optimization Techniques
- Comfortable with NumPy and the ML workflow introduced in Unit 1

## Notebooks

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

**Kernels:** notebooks 01 and 03 run on the `ai-diploma` kernel; notebook 02 uses
PyTorch and Keras and runs on the `tfenv` kernel (see `../START_HERE.md`).

1. **[CORE]** `examples/01_ai_learning_models.ipynb` - Build and evaluate common AI/ML
   models; compare model families and deployment considerations.
2. **[ENRICHMENT — bridge to AIAT 122]** `examples/02_transfer_learning_the_ladder.ipynb` - Four ways to use a
   pretrained ResNet-18 on the same 1,000 CIFAR-10 photographs (as-is, frozen backbone
   + new head, partial fine-tune, full fine-tune), with trainable parameters, wall-clock
   and held-out accuracy printed for each. The lesson is the table: where accuracy
   stops paying for cost. All four rungs run in about a minute on a laptop CPU
   (`tfenv` kernel).
3. **[CORE]** `examples/03_serving_the_model.ipynb` - Save lesson 01's biopsy model with
   `joblib`, serve it with FastAPI, POST one row and get a prediction back, then send
   five malformed rows and watch each one rejected before it reaches the model. Ends
   with a demonstration of why a model file from a stranger is executable code.

## Exercise

- `exercises/exercise_05_machine_learning_models.ipynb` - practice problems
  on machine learning models.

## Quiz

- `../QUIZZES/Quiz_05_ML_Models.md`

Solutions and answer keys are released by your instructor.

**Next:** complete a project from `../PROJECTS/` and review `../ASSESSMENTS/`
for the final exam.
