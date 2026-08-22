# START HERE

Welcome to AIAT 124 — Generative Artificial Intelligence (Semester 2 of the
AI Diploma).

Credit hours: 3 · Contact hours: 4/week · Total training hours: 64 (theory+practical)

## Prerequisites

- Semester 1 (AIAT 111–116)
- AIAT 122 — Deep Learning (Course 08): PyTorch, CNNs, training loops

## Setup

Use the repo root virtual environment and the **ai-diploma** Jupyter kernel:

```bash
cd "AI Diploma"                      # repo root
source .venv/bin/activate
jupyter lab                          # select the "ai-diploma" kernel in notebooks
```

Required packages:

```bash
pip install numpy pandas matplotlib scikit-learn
pip install torch torchvision
pip install nltk                     # BLEU metrics (Units 1-2 evaluation)
```

Optional: `pip install transformers` and `pip install openai` — only if you
want to run the clearly labeled *reference* workflows in the Unit 2
fine-tuning and prompt-engineering lessons (a model download or an API key is
required; every lesson runs fully without them).

Verify:

```python
import numpy, pandas, sklearn, torch, torchvision, nltk
print("PyTorch:", torch.__version__)
```

**GPU:** not required — every notebook trains classroom-sized models on CPU
in seconds to ~1 minute. A GPU (or Google Colab — see `DOCS/COLAB_SETUP.md`)
is only needed to try the full-size systems referenced in Unit 3
(Stable Diffusion, StyleGAN).

## Learning Path

1. Read `README.md` — course overview, units, and CLOs.
2. Work the units in order. In each unit:
   1. Read the unit `README.md`.
   2. Do the `examples/` notebooks in file order (01, 02, 03, ...).
   3. Do the `exercises/` notebook.
   4. Take the unit quiz in `QUIZZES/`.
3. Units, in order:
   - `unit1-generative-fundamentals/` — Introduction to Generative AI
   - `unit2-text-generation/` — Text and Language Generation
   - `unit3-image-generation/` — Image and Visual Generation
   - `unit4-ethics-regulations/` — Ethical and Regulatory Considerations
   - `unit5-future-trends/` — Future Trends and Research in Generative AI
4. Finish with the final exam in `ASSESSMENTS/`.

Track your progress in `STUDENT_PROGRESS_CHECKLIST.md`.
Solutions and answer keys are released by your instructor.
