# Quiz 02 – Unit 2: Classical RL Algorithms
## AIAT 123 - Reinforcement Learning

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 2 (Dynamic Programming, Monte Carlo, TD-learning, Q-learning, SARSA).
**Concepts from:** Unit 2 examples (policy/value iteration, Q-learning, SARSA) and related slides.
**Answers and rubrics:** Instructor only — see `DOCS/SOLUTIONS/quizzes/`.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What is the key difference between **Q-learning** (off-policy) and **SARSA** (on-policy)?

a) Q-learning uses neural networks; SARSA does not
b) Q-learning updates using the max Q-value of the next state; SARSA uses the Q-value of the action actually taken
c) SARSA is always faster
d) Q-learning requires a model of the environment

---

### Question 2 (10 points)
**Monte Carlo methods** estimate value functions by:

a) Using neural networks to approximate values
b) Averaging returns from complete episodes of experience
c) Using the Bellman equation at every time step
d) Bootstrapping from the next state's estimate

---

### Question 3 (10 points)
Which statement about **Temporal Difference (TD) learning** is correct?

a) It requires complete episodes before updating
b) It updates value estimates after every step using a bootstrapped target (reward + discounted next value)
c) It cannot be used in environments with long episodes
d) It is only used in continuous action spaces

---

### Question 4 (10 points)
**Policy iteration** alternates between two steps. What are they?

a) Exploration and exploitation
b) Policy evaluation (compute value of current policy) and policy improvement (make policy greedy w.r.t. value)
c) Forward pass and backward pass
d) Reward shaping and discount

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write Python code implementing a **Q-learning agent** for a 5x5 grid world:
- Q-table: shape (25, 4) initialized to zero.
- Parameters: alpha=0.1, gamma=0.95, epsilon=0.1.
- Write the epsilon-greedy action selection function.
- Write the Q-update function.
- Apply one Q-update: current state=5, action=2, reward=-1, next_state=6.
- Print Q[5, 2] before and after the update.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_02_solution.md`.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain the main limitation of **Dynamic Programming** for RL, and why **model-free methods** (like Q-learning) are preferred in practice.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_02_solution.md`.

---

### Question 7 (15 points)
Compare **first-visit Monte Carlo** and **every-visit Monte Carlo** for estimating state values. When would one be preferred over the other?

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_02_solution.md`.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
You apply Q-learning to FrozenLake and the agent converges to a poor policy. You suspect alpha (learning rate) is too high. Explain why a high alpha causes instability and suggest a concrete fix.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_02_solution.md`.

---

**Mapping:** CLO2; notebooks: Q-learning/SARSA examples, value/policy iteration examples.

**For:** AIAT 123 - Reinforcement Learning
