# Unit 4: Evaluation and Refinement

Unit hours: 17 total (3 theory + 14 practical)

You evaluate your project systematically and refine it: run experiments, compare against baselines, analyze failure cases, and iterate on models and data.

## Builds on (AIAT 111-125)

**Builds on:** AIAT 114 U2/U3 (bias-variance, learning curves, classification metrics) · AIAT 116 U2/U4 (per-subgroup metrics, SHAP) · AIAT 113 U5 (confidence intervals — is the improvement real?) · AIAT 125 U5 (A/B and canary comparison).

Every artifact you reuse goes in **section 6, the Prior Work Inventory**, of [`TEMPLATES/project_proposal_template.md`](../TEMPLATES/project_proposal_template.md) — scored at gate 1 and re-checked at the design review. It is this course's **CLO2** evidence: AIAT 126 integrates the diploma, it does not re-teach it.

## Prerequisites

- Unit 3: Implementation and Development of the Project Idea (a first working version of your project)

## Examples (work through in order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

1. **[CORE]** [examples/01_model_evaluation_optimization.ipynb](examples/01_model_evaluation_optimization.ipynb) - Running experiments and collecting metrics, comparing against baseline models, analyzing failure cases, visualizing results (confusion matrices, curves), and iterative improvement.
2. **[ENRICHMENT]** [enrichment/E2_one_success_isnt_reliability.ipynb](enrichment/E2_one_success_isnt_reliability.ipynb) - Non-examinable: why a single successful run measures almost nothing - pass@1 vs pass^k, Wilson vs Wald intervals, and how many repeated runs your project needs before it may claim an improvement.

## Exercise

This unit has no separate exercise notebook; the practical work is evaluating and refining your own project. Course exercises live in Units 1-3.

## Quiz

- [../QUIZZES/quiz_04.md](../QUIZZES/quiz_04.md)

## Next

[Unit 5: Project Documentation and Final Presentation](../unit5-documentation-presentation/README.md)
