# Unit 4: Interpretability, Transparency, and Accountability

Unit hours: 14 (theory+practical)

This unit covers explaining and auditing AI decisions: SHAP and LIME explanations, counterfactual analysis, accountability frameworks and audit trails, human-in-the-loop approaches, and transparency tooling.

## Prerequisites

- Unit 3: Privacy, Security, and Data Protection ([../unit3-privacy-security/README.md](../unit3-privacy-security/README.md))
- Setup from [../START_HERE.md](../START_HERE.md) (root `.venv` + **ai-diploma** kernel)

## Learning Objectives

By the end of this unit, you will be able to:

- Explain model predictions with SHAP and LIME
- Generate counterfactual explanations for individual decisions
- Apply accountability frameworks, audit trails, and stakeholder mapping
- Design human-in-the-loop oversight and choose appropriate transparency tools

## Examples (work in this order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

1. **[CORE]** [examples/01_shap_explanations.ipynb](examples/01_shap_explanations.ipynb) — SHAP values: global and local explanations with summary, waterfall, and dependence plots.
2. **[CORE]** [examples/02_lime_explanations.ipynb](examples/02_lime_explanations.ipynb) — LIME: local surrogate explanations for individual predictions.
3. **[CORE]** [examples/03_counterfactual_analysis.ipynb](examples/03_counterfactual_analysis.ipynb) — Counterfactual ("what-if") analysis of model decisions.
4. **[CORE]** [examples/04_accountability_frameworks.ipynb](examples/04_accountability_frameworks.ipynb) — Accountability frameworks, audit timelines, and stakeholder responsibilities.
5. **[HOMEWORK]** [examples/05_hitl_approaches.ipynb](examples/05_hitl_approaches.ipynb) — Human-in-the-loop approaches and when to use each.
6. **[HOMEWORK]** [examples/06_transparency_tools.ipynb](examples/06_transparency_tools.ipynb) — Comparing transparency tools for model reporting and disclosure.
7. **[HOMEWORK]** [examples/07_explainable_ai_techniques.ipynb](examples/07_explainable_ai_techniques.ipynb) — Implementing explainable-AI techniques (SHAP, LIME) end to end.

## Exercises

- [exercises/exercise_01.ipynb](exercises/exercise_01.ipynb)
- [exercises/exercise_02.ipynb](exercises/exercise_02.ipynb) — Explainable AI in practice

Solutions are released by your instructor.

## Quiz

- [../QUIZZES/Quiz_04_Transparency_Accountability.md](../QUIZZES/Quiz_04_Transparency_Accountability.md)

## Next

Continue to [Unit 5: AI Governance, Regulations, and Future Challenges](../unit5-governance-regulations/README.md).
