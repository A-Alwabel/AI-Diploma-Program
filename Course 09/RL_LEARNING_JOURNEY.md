# RL Learning Journey (AIAT 123)

This page is a **single narrative map** for the whole course. The numbered notebooks in each unit are the real lessons; this file answers: *where am I, what did I just gain, and what comes next?*

## The through-line (one sentence per stage)

| Stage | You can now… |
| ----- | -------------- |
| **Formulation** | Say what the agent observes, what it can do, and what the reward is trying to optimize (before any “magic algorithm”). |
| **Tabular control** | Improve a policy from **experience** using updates to value or Q tables when the world is small enough to tabulate. |
| **Deep RL** | Use **function approximation** for the same ideas when observations or state structure are too large for a table. |
| **Exploration** | Control **where data comes from**—how much randomness or structure you inject while learning. |
| **Applications** | Place RL in **realistic stories**—multi-agent settings, safety, and extensions—and tie them back to Units 1–4. |

## Units 1–5 in order

| Unit | Folder | Carries forward… |
| ---- | ------ | ------------------ |
| **1** | [`unit1-rl-fundamentals/`](unit1-rl-fundamentals/README.md) | MDPs, Bellman-style thinking, Gym `reset`/`step`, ε-greedy intuition, **states / actions / rewards** as a design task. |
| **2** | [`unit2-policy-value/`](unit2-policy-value/README.md) | Monte Carlo, TD, **Q-learning**, SARSA—learning from samples without a full model of the environment. |
| **3** | [`unit3-deep-rl/`](unit3-deep-rl/README.md) | DQN-style targets, replay, policy gradients, actor–critic—**scale** and **stability** concerns. |
| **4** | [`unit4-exploration-exploitation/`](unit4-exploration-exploitation/README.md) | Bandits and schedules—**exploration design** as its own lever on sample efficiency. |
| **5** | [`unit5-applications/`](unit5-applications/README.md) | Case studies, MARL, ethics, hierarchical / goal-conditioned / model-based **threads** that reuse vocabulary from earlier units. |

## Reuse the same mental checklist everywhere

Whatever notebook you open, ask:

1. **State** — Is everything the agent needs represented (and nothing toxic or misleading)?
2. **Action** — Are the choices legal in the real system you have in mind?
3. **Reward** — Does it align with the true goal, or can it be gamed?
4. **Policy / value** — What is being updated, and from which data?
5. **Exploration** — How does the agent avoid getting stuck on a bad early habit?

If you can answer these for a toy environment, you are practicing the same skill you need for a project-scale problem—only the engineering gets heavier.

## Close the loop

- **Per unit:** `README.md` → numbered `examples/` → `exercises/` → `QUIZZES/quiz_0N.md`
- **Whole course:** [`START_HERE.md`](START_HERE.md) → Units 1–5 → [`PROJECTS/`](PROJECTS/) → [`ASSESSMENTS/Final_Exam.md`](ASSESSMENTS/Final_Exam.md)
- **Progress:** [`STUDENT_PROGRESS_CHECKLIST.md`](STUDENT_PROGRESS_CHECKLIST.md)

Skim this journey page **once at the start** and **once before the project** so the course feels like one story, not five disconnected folders.

## Automated check (optional, maintainers)

From the repository root:

```bash
python3 "Course 09/scripts/verify_student_notebooks.py"
```

This executes student-path notebooks under `Course 09/unit*/` (long run). Results land in `Course 09/scripts/_last_notebook_verify.log`.
