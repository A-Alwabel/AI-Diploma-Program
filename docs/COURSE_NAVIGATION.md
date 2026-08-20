# Course Navigation Guide

How the 12 courses connect and build on each other.

**Last Updated:** 2026-08

---

## Official Order

The program is taken **sequentially, Course 01 through Course 12**. This is the
official order — there are no alternate tracks:

```
Semester 1
  Course 01  AIAT 111  Introduction to Artificial Intelligence and Applications
  Course 02  AIAT 112  Python for Artificial Intelligence
  Course 03  AIAT 113  Mathematics and Probability for Machine Learning
  Course 04  AIAT 114  Machine Learning Algorithms and Applications
  Course 05  AIAT 115  Scalable Data Science
  Course 06  AIAT 116  Artificial Intelligence Ethics

Semester 2
  Course 07  AIAT 121  Natural Language Processing
  Course 08  AIAT 122  Deep Learning
  Course 09  AIAT 123  Reinforcement Learning
  Course 10  AIAT 124  Generative Artificial Intelligence
  Course 11  AIAT 125  Deploying AI Models
  Course 12  AIAT 126  Graduation Project
```

**Course 02 (Python) comes before Course 03 (Mathematics).** Course 03 uses
Python (from Course 02) to compute and visualize the math — you do not need the
math course to start the Python course. Earlier versions of this guide
suggested taking the math first; the official sequential order above is the one
to follow.

---

## Prerequisites by Course

| Course | Code | Prerequisite courses | What it provides |
|--------|------|----------------------|------------------|
| 01 | AIAT 111 | None | AI concepts, search, agents, intro to neural nets and generative AI |
| 02 | AIAT 112 | AIAT 111 | Python programming, implementing AI algorithms |
| 03 | AIAT 113 | AIAT 112 | Linear algebra, calculus, probability, statistics |
| 04 | AIAT 114 | AIAT 111–113 | Regression, classification, clustering, model selection |
| 05 | AIAT 115 | AIAT 114 | Data cleaning, visualization, ML pipelines, big data |
| 06 | AIAT 116 | AIAT 111–115 | Bias, fairness, privacy, transparency, governance |
| 07 | AIAT 121 | AIAT 111–116 | Text processing, embeddings, deep learning NLP |
| 08 | AIAT 122 | AIAT 121 (esp. 114, 121) | Neural networks, CNNs, RNNs, transformers |
| 09 | AIAT 123 | AIAT 122 | MDPs, Q-learning, deep RL |
| 10 | AIAT 124 | AIAT 122 | GANs, VAEs, diffusion, LLMs |
| 11 | AIAT 125 | AIAT 111–124 | Packaging, APIs, containers, cloud, MLOps |
| 12 | AIAT 126 | AIAT 111–125 | Capstone project applying everything |

---

## Topic Map: Where Each Topic Lives

Topics deliberately appear in more than one course (spiral curriculum):
first as an **introduction**, later as a **deep dive**, and finally in
**application**. Do not skip a repeated topic — each pass adds depth.

| Topic | Introduction | Deep dive | Application |
|-------|--------------|-----------|-------------|
| Python programming | Course 01 (basics for AI) | Course 02 | Course 05 (data-science Python) |
| Search algorithms | Course 01 | Course 02 | — |
| Knowledge representation | Course 01 | Course 02 | — |
| Mathematics for ML | — | Course 03 | Used in all later courses |
| Machine learning | Course 01 | Course 04 | Course 05 |
| Optimization / gradient descent | Course 02 | Course 03 (the math) | Course 04 |
| Data science | — | Course 05 | Course 12 |
| Ethics and responsible AI | Course 06 | Course 06 | Courses 10–12 |
| NLP | Course 07 | Course 07 | Course 08 (deep learning NLP) |
| Neural networks / deep learning | Course 01 | Course 08 | Course 11 (deployment) |
| Reinforcement learning | — | Course 09 | Course 12 |
| Generative AI | Course 01 | Course 10 | Course 12 |
| Deployment / MLOps | Course 08 (intro) | Course 11 | Course 12 |

**How to use this table:** when a topic reappears, check which level you are
at. First encounter → study it fully. Reappearance → review quickly, then focus
on what is new at that level.

---

## Key Course-to-Course Connections

- **01 → 02:** AI concepts from Course 01 get implemented in Python in Course 02.
- **02 → 03:** Python skills from Course 02 are used to compute and plot the math in Course 03.
- **03 → 04:** Linear algebra, calculus, and probability underpin every ML algorithm in Course 04.
- **04 → 05:** Course 05 scales the ML workflow from Course 04 to real datasets and pipelines.
- **04, 07 → 08:** Deep learning extends classical ML; Course 08 also applies deep learning to the NLP tasks introduced in Course 07.
- **08 → 09:** Deep RL (DQN and beyond) builds directly on neural network training.
- **08 → 10:** GANs, VAEs, and diffusion models are neural networks — Course 08 first.
- **All → 11:** Course 11 deploys the models you built earlier (APIs, containers, cloud, monitoring).
- **All → 12:** The graduation project draws on the entire program.

---

## Rules of Thumb

1. **Follow the sequence.** Courses assume everything before them.
2. **Finish units in order** within a course (1 → 5); later units build on earlier ones.
3. **Review before big jumps:** revisit Course 03 before Course 04, and
   Course 08 before Courses 09 and 10.
4. **Track progress** with each course's `STUDENT_PROGRESS_CHECKLIST.md`.

---

## Related Documents

- [STUDENT_GUIDE.md](STUDENT_GUIDE.md) — how to work through the program
- [QUICK_REFERENCE_GUIDE.md](QUICK_REFERENCE_GUIDE.md) — courses, hours, CLOs at a glance
- [SETUP_GUIDE.md](SETUP_GUIDE.md) — environment setup
