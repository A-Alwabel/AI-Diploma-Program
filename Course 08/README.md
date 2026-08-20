# AIAT 122 — Deep Learning

**Course 08 · Semester 2 of the AI Diploma**

Credit hours: 3 · Contact hours: 4/week · Total training hours: 64 (theory+practical)

New students: read `START_HERE.md` first, then follow the units in order.

---

## What this course covers

Building, training, and deploying deep neural networks: fundamentals and backpropagation, CNNs for computer vision, RNNs and Transformers for sequential data, advanced techniques (GANs, VAEs, reinforcement learning, ethics), and model optimization and deployment.

**Frameworks:** Both **TensorFlow/Keras** and **PyTorch** are used. Many notebooks show a concept in one or both frameworks; Unit 3 transformer notebooks use Hugging Face (PyTorch).

The official TVTC training plan is the authority for course scope and hours; this README describes how the materials in this folder follow it.

---

## Units

| Unit | Folder | Official title | Hours |
|------|--------|----------------|-------|
| 1 | `unit1-deep-learning-basics/` | Introduction to Deep Learning and Neural Networks | 12 |
| 2 | `unit2-cnns/` | Convolutional Neural Networks (CNNs) for Computer Vision | 12 |
| 3 | `unit3-rnns-transformers/` | Recurrent Neural Networks (RNNs) and Transformers for Sequential Data | 12 |
| 4 | `unit4-advanced-dl/` | Advanced Deep Learning Techniques | 14 |
| 5 | `unit5-deployment/` | Model Optimization and Deployment | 14 |

---

## Learning path

One numbered path — do it in this order:

1. `START_HERE.md`
2. Units 1 → 5. In each unit: read the unit `README.md`, run the notebooks in `examples/` in file order (01, 02, 03, …), do the `exercises/` notebook(s), then take the unit quiz in `QUIZZES/`.
3. `ASSESSMENTS/` — theory exam, practical exam, and final exam (as scheduled by your instructor).

Projects (`PROJECTS/`) and the case study (`CASE_STUDIES/`) are assigned by your instructor.

**Notebook order:** always follow the file numbers (01 → 02 → 03 …) listed in each unit README. Slide numbers mentioned inside notebooks are topic references, not an order to follow — see `DOCS/EXAMPLES_ORDER.md` for the slide ↔ notebook map.

---

## Prerequisites

- Semester 1 (AIAT 111–116), including machine learning fundamentals.
- Comfortable with Python and NumPy.

---

## Setup

- Use the repo root `.venv` and the **"ai-diploma"** Jupyter kernel. Install dependencies from the root `requirements.txt`; course-specific notes: `DOCS/REQUIREMENTS_COURSE_08.md`.
- Notebooks that import TensorFlow run on the **"tfenv"** kernel; PyTorch notebooks use the "ai-diploma" kernel.
- A GPU speeds up training considerably. For free GPU access use Google Colab: `DOCS/COLAB_SETUP.md`.
- Datasets (e.g. MNIST, CIFAR-10, IMDB) download automatically when you run the notebooks.

---

## Course Learning Outcomes (CLOs)

- **CLO1:** Explain basic concepts of deep learning, including the structure and performance of neural networks, backpropagation, and optimization techniques.
- **CLO2:** Develop and implement deep learning architectures such as CNNs, RNNs, and Transformers.
- **CLO3:** Build and deploy deep learning models to solve real-world problems, including image recognition tasks such as classification and object detection.
- **CLO4:** Optimize deep learning models by applying techniques such as hyperparameter tuning and regularization (dropout, batch normalization).
- **CLO5:** Critically evaluate ethical issues related to deep learning, including dataset bias, fairness, and interpretability.

---

## Folder guide

```
Course 08/
├── README.md                        (this file)
├── START_HERE.md                    (first read for new students)
├── STUDENT_PROGRESS_CHECKLIST.md    (track your progress)
├── unit1-deep-learning-basics/      Unit 1 — examples/ + exercises/
├── unit2-cnns/                      Unit 2 — examples/ + exercises/
├── unit3-rnns-transformers/         Unit 3 — examples/ + exercises/
├── unit4-advanced-dl/               Unit 4 — examples/ + exercises/
├── unit5-deployment/                Unit 5 — examples/ + exercises/
├── QUIZZES/                         quiz_01 … quiz_05 (one per unit)
├── ASSESSMENTS/                     theory, practical, and final exams
├── PROJECTS/                        capstone projects with rubrics
├── CASE_STUDIES/                    deployment case study
├── PRESENTATIONS/SLIDES/            27 lecture decks (see its README)
├── DOCS/                            setup and study guides
└── TEMPLATES/                       instructor templates
```

**Slides:** the institution lecture decks live in `PRESENTATIONS/SLIDES/` (27 `.pptx` files, indexed in `PRESENTATIONS/SLIDES/README.md`). `DOCS/EXAMPLES_ORDER.md` maps slides to notebooks.

**If a notebook isn't clear:** see `DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md`. Common questions: `DOCS/COMMON_MISCONCEPTIONS_AND_FAQ.md`.

**Solutions and answer keys:** released by your instructor.
