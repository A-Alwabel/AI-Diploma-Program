# Unit 5: NLP Applications and Ethics Standards
## AIAT 121 — Natural Language Processing

Unit hours: 14 (theory+practical)

## What This Unit Teaches

Real-world NLP applications and the ethics of deploying them: detecting bias in NLP models and datasets, applying fairness metrics and qualitative analysis, and addressing bias during preprocessing and evaluation.

This unit currently has one example notebook; additional content is being authored.

## Examples (run in order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

1. **[CORE]** `examples/01_bias_detection.ipynb` — The logic of a bias audit walked through on simulated association scores (disclosed as simulated), plus mitigation strategies and a responsible-NLP checklist; measuring bias on real data is the exercise's design task.
2. **[ENRICHMENT]** `enrichment/E17_the_arabic_evaluation_gap.ipynb` — Non-examinable: measure the Arabic penalty in an English-first pipeline yourself — UTF-8 byte cost, BPE fertility on MSA and a Saudi dialect, what 32x more vocabulary buys each language, clitic segmentation, and the published Absher/QIMMA benchmark findings. Notebooks in `enrichment/` appear in no quiz or exam.

## Exercise

- `exercises/01_nlp_applications_ethics_exercise.ipynb` — Analyze NLP applications and their ethical implications.

## Quiz

- `../QUIZZES/quiz_05.md` — Unit 5 quiz (45 minutes, 110 points; 100 required).

Solutions and answer keys are released by your instructor.

## Related Materials

- Case study: `../CASE_STUDIES/01_nlp_application_case_study.md`
- Course project: `../PROJECTS/Sentiment_Analysis_System/`

## Prerequisites

- Units 1–4 of this course
- Notebooks run on the **ai-diploma** Jupyter kernel (repository root `.venv`)
