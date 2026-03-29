# START HERE! | ابدأ من هنا!

## 👋 Welcome! | مرحباً!

This course is part of Semester 2 of the AI Diploma Program.

**✅ Official Path:** Follow the unit folders in order (Unit 1 → Unit 5).  
**📚 Official unit structure:** See **README.md** (Unit ↔ Folder mapping) and `../DETAILED_UNIT_DESCRIPTIONS.md` for learning outcomes per unit.

---

## 🚀 Student Quick Start (3 steps)

1. **Read README.md** — Course overview, unit mapping, and what you'll learn.
2. **Set up your environment** — Install dependencies below. For free GPU: use **Google Colab**.
3. **Start Unit 1** — Open `unit1-rl-fundamentals/README.md` and do the example notebooks in file order (01, 02, 03, …).

### Required packages

```bash
pip install numpy matplotlib
pip install torch torchvision        # PyTorch (all notebooks)
pip install gymnasium                # OpenAI Gym environments (Unit 1)
pip install scikit-learn
```

### Verify setup

```python
import torch, gymnasium, numpy
print("PyTorch:", torch.__version__)
print("Gymnasium:", gymnasium.__version__)
```

---

## 📋 Prerequisites | المتطلبات الأساسية

**Before starting this course, you must have completed:**
- All Semester 1 courses (AIAT 111–116)
- Course 08 — Deep Learning Basics (especially neural networks and PyTorch)

---

## 📚 Learning Path | مسار التعلم

1. **Read README.md** — Understand course overview and goals.
2. **Review prerequisites** — Make sure you're comfortable with PyTorch basics.
3. **Start with Unit 1** — RL Fundamentals: MDPs, rewards, OpenAI Gym.
4. **Unit 2** — Classical RL Algorithms: Q-learning, SARSA, Dynamic Programming.
5. **Unit 3** — Deep RL: DQN, Policy Gradient, Actor-Critic, PPO.
6. **Unit 4** — Exploration and Exploitation Strategies: epsilon-greedy, UCB, Thompson Sampling.
7. **Unit 5** — Multi-Agent Systems and Advanced Topics.
8. **Complete exercises** — Practice what you learn in each unit.
9. **Take quizzes** — Test your understanding after each unit.

**📌 Notebook order:** In each unit, do the example notebooks in **file order** (01, 02, 03, …). Always use the order shown in each unit's README, not slide numbers.

**❓ If a notebook isn't clear:** Open `DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md` (if available) or ask your instructor.

---

## ✅ Progress Tracking | تتبع التقدم

Use `STUDENT_PROGRESS_CHECKLIST.md` to track your progress through all 5 units.

---

**Ready to begin?** Read the course README.md first!
