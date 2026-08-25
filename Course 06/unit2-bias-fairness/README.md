# Unit 2: Bias, Fairness, and Discrimination in AI

Unit hours: 12 (theory+practical)

This unit covers how bias enters machine learning systems and how to measure and reduce it: fairness metrics (demographic parity, equalized odds), pre-/in-/post-processing mitigation techniques, fair representation learning, real-world bias case studies, and practices for developing fair AI systems.

## Prerequisites

- Unit 1: Foundations of AI Ethics ([../unit1-ethics-foundations/README.md](../unit1-ethics-foundations/README.md))
- Setup from [../START_HERE.md](../START_HERE.md) (root `.venv` + **ai-diploma** kernel)

## Learning Objectives

By the end of this unit, you will be able to:

- Detect bias in ML models using group fairness metrics
- Apply bias mitigation techniques and compare their trade-offs
- Analyze documented cases of biased AI systems (hiring, credit, facial recognition, policing)
- Apply fair-AI development practices such as human-in-the-loop review

## Examples (work in this order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

1. **[CORE]** [examples/01_bias_detection.ipynb](examples/01_bias_detection.ipynb) — Detecting bias in ML models with fairness metrics such as demographic parity and equalized odds.
2. **[CORE]** [examples/02_bias_mitigation.ipynb](examples/02_bias_mitigation.ipynb) — Bias mitigation techniques applied before, during, and after model training.
3. **[HOMEWORK]** [examples/03_fair_representation.ipynb](examples/03_fair_representation.ipynb) — Fair representation learning: transforming features to reduce encoded bias.
4. **[HOMEWORK]** [examples/04_bias_case_studies.ipynb](examples/04_bias_case_studies.ipynb) — Case studies of biased AI: hiring, credit scoring, facial recognition, predictive policing.
5. **[HOMEWORK]** [examples/05_fair_ai_development.ipynb](examples/05_fair_ai_development.ipynb) — Building fairness into the development workflow, including human-in-the-loop review.

## Exercise

- [exercises/exercise_01.ipynb](exercises/exercise_01.ipynb)

Solutions are released by your instructor.

## Quiz

- [../QUIZZES/Quiz_02_Bias_Justice.md](../QUIZZES/Quiz_02_Bias_Justice.md)

## Next

Continue to [Unit 3: Privacy, Security, and Data Protection](../unit3-privacy-security/README.md).
