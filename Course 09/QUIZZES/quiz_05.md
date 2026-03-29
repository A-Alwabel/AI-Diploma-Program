# Quiz 05 – Unit 5: Advanced Topics and Applications
## AIAT 123 - Reinforcement Learning

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 5 (multi-agent RL, hierarchical RL, model-based RL, real-world applications).
**Concepts from:** Unit 5 examples and related slides.
**Answers and rubrics:** Instructor only — see `DOCS/SOLUTIONS/quizzes/`.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
In **multi-agent RL**, a **cooperative** setting means:

a) Agents compete against each other for maximum individual reward
b) Agents work together toward a shared goal and may share rewards or information
c) Agents ignore each other completely
d) Only one agent is active at a time

---

### Question 2 (10 points)
The key advantage of **model-based RL** over model-free RL is:

a) It never requires real environment interactions
b) It learns a model of the environment and can plan or generate simulated experience, improving sample efficiency
c) It always achieves higher rewards
d) It does not require function approximation

---

### Question 3 (10 points)
**Hierarchical RL** (options framework) addresses which challenge?

a) Lack of GPU memory
b) Long-horizon planning by decomposing tasks into sub-goals at different temporal abstraction levels
c) Continuous action spaces only
d) Multi-agent coordination only

---

### Question 4 (10 points)
Which is a real-world RL success in **robotics**?

a) Training robots to walk using policy gradient methods in simulation, then transferring to real hardware
b) Using RL only for board games
c) RL has never been applied to robotics
d) Robots use only supervised learning

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write Python pseudocode to set up a **multi-agent grid world** with two agents:
- 5x5 grid, both agents start at (0,0) and need to reach (4,4).
- Represent joint state as tuple (agent1_pos, agent2_pos).
- Write a step(actions) function that moves both agents, returns (observations, rewards, done).
- Shared reward: +10 when BOTH agents reach the goal; -1 per step.
- You do not need to implement full RL training.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_05_solution.md`.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain **goal-conditioned RL**: what it is, how it differs from standard RL, and one practical application.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_05_solution.md`.

---

### Question 7 (15 points)
What is **sim-to-real transfer** in robotics RL? Name **two** common techniques used to make policies trained in simulation work in the real world.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_05_solution.md`.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
Design a high-level RL system to **optimize ad placement** on a website. Define: state, action, reward, and suggest an algorithm. Mention one ethical consideration.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_05_solution.md`.

---

**Mapping:** CLO6; notebooks: Unit 5 advanced topics examples.

**For:** AIAT 123 - Reinforcement Learning
