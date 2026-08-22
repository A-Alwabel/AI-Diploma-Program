# AIAT 124 - Generative Artificial Intelligence

New students: read `START_HERE.md` first.

Credit hours: 3 · Contact hours: 4/week · Total training hours: 64 (theory+practical)

## Course Overview

This course covers generative AI: probabilistic generative models, Variational
Autoencoders (VAEs), Generative Adversarial Networks (GANs), Transformer-based
text generation, image generation (including a diffusion model you train),
ethics and regulation, and current research directions. Most notebooks use
PyTorch; a few use NumPy/scikit-learn only.

## Units

| Unit | Folder | Official title | Training hours |
|------|--------|----------------|----------------|
| 1 | `unit1-generative-fundamentals/` | Introduction to Generative AI | 12 |
| 2 | `unit2-text-generation/` | Text and Language Generation | 12 |
| 3 | `unit3-image-generation/` | Image and Visual Generation | 12 |
| 4 | `unit4-ethics-regulations/` | Ethical and Regulatory Considerations | 14 |
| 5 | `unit5-future-trends/` | Future Trends and Research in Generative AI | 14 |

## Learning Path

1. `START_HERE.md` — setup and orientation.
2. Units 1 to 5, in order. In each unit: read the unit `README.md`, work the
   `examples/` notebooks in file order (01, 02, ...), do the `exercises/`
   notebook, then take the unit quiz in `QUIZZES/`.
3. `ASSESSMENTS/` — final exam.

Track your progress with `STUDENT_PROGRESS_CHECKLIST.md`.

## Prerequisites

- Semester 1 (AIAT 111–116)
- AIAT 122 — Deep Learning (Course 08): neural networks, CNNs, PyTorch training loops
- AIAT 123 — Reinforcement Learning (Course 09) is taken in the same semester
  and is not required for this course

**Hardware:** no GPU needed — the notebooks train classroom-sized GAN/VAE/
diffusion models on CPU in seconds to about a minute. A GPU (free via Colab —
see `DOCS/COLAB_SETUP.md`) is only needed to try the full-size systems
referenced in Unit 3.

## Course Learning Outcomes (CLOs)

1. Explain basic principles of generative AI, including probabilistic modeling,
   neural network structures, and key concepts.
2. Apply generative modeling techniques such as VAEs, GANs, and
   Transformer-based models.
3. Implement and optimize generative models for tasks such as text generation,
   image synthesis, and audio creation.
4. Evaluate generative model performance using quantitative metrics (FID, BLEU,
   perplexity) and qualitative assessment, addressing challenges such as mode
   collapse.
5. Design and develop generative AI solutions for practical applications,
   including content generation, data augmentation, and creative applications.
6. Analyze ethical, legal, and social implications of generative AI, including
   bias, misinformation, intellectual property, and transparency.
7. Explore emerging trends in generative AI, such as multimodal generation and
   diffusion models.

## Folder Structure

```
Course 10/
├── README.md
├── START_HERE.md
├── STUDENT_PROGRESS_CHECKLIST.md
├── unit1-generative-fundamentals/
├── unit2-text-generation/
├── unit3-image-generation/
├── unit4-ethics-regulations/
├── unit5-future-trends/
├── QUIZZES/          # one quiz per unit
├── ASSESSMENTS/      # final exam
├── PROJECTS/         # course project
├── CASE_STUDIES/     # ethics case study (used in Unit 4)
├── PRESENTATIONS/    # presentation template for the course project
└── DOCS/             # Colab/GPU setup guide
```

Solutions and answer keys are released by your instructor.
