# Unit 5: Introduction to Generative AI and Course Summary

**Course:** AIAT 111 · **Unit hours:** 14 (7 theory + 7 practical)

Generative models and how they differ from discriminative ones (GANs, Transformers, LLMs), an applied binary-classification project — a feedforward neural network for diabetes prediction with EDA and preprocessing — a hands-on GAN training experiment, and a summary that ties the whole course together.

This unit is a first taste: the math behind these models arrives in Course 03 (AIAT 113), the deep-learning mechanics in Course 08 (AIAT 122), and generative AI gets its own full course in Course 10 (AIAT 124).

**Prerequisites:** Unit 4 (`../unit4-neural-networks-basics/README.md`).

**Kernels:** notebooks 01, 02, and 05 run on the `ai-diploma` kernel; notebooks 03 and 04 use TensorFlow/Keras and run on the `tfenv` kernel (see `../START_HERE.md`).

---

## Notebooks (run in order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

| # | Notebook | What it covers | Tier |
|---|----------|----------------|------|
| 01 | `examples/01_generative_ai_introduction.ipynb` | What generative AI is; overview of model families and applications | **CORE** |
| 02 | `examples/02_generative_vs_discriminative.ipynb` | Generative vs discriminative models | **HOMEWORK** |
| 03 | `examples/03_diabetes_classification_ffnn.ipynb` | Diabetes classification with a feedforward neural network: EDA, preprocessing, training, evaluation (`tfenv` kernel) | **CORE** |
| 04 | `examples/04_simple_gan_experiment.ipynb` | Training a simple GAN to generate the two-moons dataset (`tfenv` kernel) | **CORE** |
| 05 | `examples/05_course_summary.ipynb` | Course summary and integration of all units | **CORE** |

---

## After the Notebooks

1. **Exercise:** `exercises/01_generative_ai_exercise.ipynb` — generative AI concepts. Solutions are released by your instructor.
2. **Quiz:** `quizzes/quiz_05.md`

Then finish the course with the final exam: `../ASSESSMENTS/Final_Exam.md`.
