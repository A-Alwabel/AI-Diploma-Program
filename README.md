# AI Diploma Program

A hands-on, notebook-based curriculum for the Artificial Intelligence Technology diploma
(AIAT track): 12 courses, 944 training hours, delivered over 2 official semesters.

---

## Courses

### Semester 1 (AIAT 111–116)

| # | Code | Course | Hours |
|---|------|--------|-------|
| 01 | AIAT 111 | Introduction to Artificial Intelligence and Applications | 64 |
| 02 | AIAT 112 | Python for Artificial Intelligence | 96 |
| 03 | AIAT 113 | Mathematics and Probability for Machine Learning | 64 |
| 04 | AIAT 114 | Machine Learning Algorithms and Applications | 96 |
| 05 | AIAT 115 | Scalable Data Science | 96 |
| 06 | AIAT 116 | Artificial Intelligence Ethics | 64 |

### Semester 2 (AIAT 121–126)

| # | Code | Course | Hours |
|---|------|--------|-------|
| 07 | AIAT 121 | Natural Language Processing | 64 |
| 08 | AIAT 122 | Deep Learning | 64 |
| 09 | AIAT 123 | Reinforcement Learning | 96 |
| 10 | AIAT 124 | Generative Artificial Intelligence | 64 |
| 11 | AIAT 125 | Deploying AI Models | 96 |
| 12 | AIAT 126 | Graduation Project | 80 |

**Total: 944 training hours** across 2 semesters. Courses are taken in order, 01 through 12.

---

## Quick Start

### 1. Set up the environment

```bash
cd "AI Diploma"
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Register the Jupyter kernel

```bash
python -m ipykernel install --user --name ai-diploma --display-name "AI Diploma"
```

Most notebooks in this repository use the `ai-diploma` kernel.

> **TensorFlow note:** TensorFlow does not ship a wheel for this venv's Python.
> The TensorFlow/Keras notebooks in **Course 01** and **Course 08** run on a separate
> kernel named `tfenv` (a Python 3.13 environment with TensorFlow installed).
> See [docs/SETUP_GUIDE.md](docs/SETUP_GUIDE.md) for how to create it.

### 3. Launch Jupyter and open the first course

```bash
jupyter lab
```

Open `Course 01/START_HERE.md` and follow it.

---

## Repository Structure

```
AI Diploma/
├── Course 01/ … Course 12/       # One folder per course (AIAT 111–126)
│   ├── START_HERE.md             # Read this first in every course
│   ├── README.md                 # Course overview and unit map
│   ├── unit1-…/ … unit5-…/       # Units, each with:
│   │   ├── examples/             #   numbered notebooks (01_…, 02_…, …)
│   │   └── exercises/            #   practice exercises
│   ├── QUIZZES/                  # Unit quizzes
│   ├── ASSESSMENTS/              # Final exam / course assessment
│   ├── PROJECTS/                 # Course projects
│   ├── CASE_STUDIES/             # Applied case studies
│   ├── PRESENTATIONS/            # Unit slide decks
│   ├── DOCS/                     # Extra docs (Colab setup, FAQ) — some courses
│   └── STUDENT_PROGRESS_CHECKLIST.md
├── docs/                         # Program-level guides (setup, navigation, troubleshooting)
├── tools/                        # Maintenance and verification scripts
├── requirements.txt              # Student environment baseline
└── README.md                     # This file
```

---

## Learning Path

Every course follows the same numbered path:

```
START_HERE.md → numbered examples (01 → NN) → exercise → quiz → assessment
```

1. **START_HERE.md** — course setup and the exact order to follow.
2. **Examples** — study and run the numbered notebooks in each unit, in order.
3. **Exercises** — complete the practice notebooks in each unit's `exercises/` folder.
4. **Quizzes** — take the unit quiz before moving to the next unit.
5. **Assessment** — finish with the course assessment in `ASSESSMENTS/`.

Solutions and answer keys are **released by your instructor** — they are not part of
this repository.

---

## Tech Stack

| Area | Tools | Where |
|---|---|---|
| Core (all courses) | NumPy, pandas, Matplotlib, Seaborn, scikit-learn | Courses 01–12 |
| Deep learning | TensorFlow + Keras **and** PyTorch | Course 08 (TF also in Course 01 intros) |
| NLP | NLTK, spaCy, Hugging Face Transformers | Course 07 |
| Reinforcement learning | Gymnasium | Course 09 |
| Scalable data science | Dask, Plotly | Course 05 |
| Generative AI | PyTorch | Course 10 |
| Deployment / MLOps | MLflow, FastAPI, Docker, PyTorch, ONNX | Course 11 |

---

## Prerequisites

- A computer running Windows, macOS, or Linux (8 GB RAM minimum)
- Python 3 (see [docs/SETUP_GUIDE.md](docs/SETUP_GUIDE.md) for versions)
- No prior AI experience required — Course 01 starts from the beginning

GPU is optional: the courses that benefit from one (05, 08, 10) include Google Colab
instructions. See [docs/GPU_REQUIREMENTS_SUMMARY.md](docs/GPU_REQUIREMENTS_SUMMARY.md).

---

## Documentation

| Document | Description |
|---|---|
| [Student Guide](docs/STUDENT_GUIDE.md) | How to work through the program |
| [Student Handbook](docs/STUDENT_HANDBOOK.md) | Study habits, notebooks, progress tracking |
| [Setup Guide](docs/SETUP_GUIDE.md) | Environment installation, kernels, smoke test |
| [Course Navigation](docs/COURSE_NAVIGATION.md) | How courses connect; prerequisites by AIAT code |
| [Quick Reference](docs/QUICK_REFERENCE_GUIDE.md) | Courses, hours, and CLOs at a glance |
| [Troubleshooting](docs/TROUBLESHOOTING_GUIDE.md) | Common errors and fixes |
| [Cross-Platform Guide](docs/CROSS_PLATFORM_GUIDE.md) | Windows / macOS / Linux notes |
| [GPU Requirements](docs/GPU_REQUIREMENTS_SUMMARY.md) | Which courses use a GPU, Colab options |
| [Community Resources](docs/COMMUNITY_RESOURCES.md) | Study groups, forums, external resources |

---

*Last updated: 2026-08*
