# Quiz 04 – Unit 4: Exploration and Exploitation Strategies
## AIAT 123 - Reinforcement Learning

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as
bonus or toward total)
**Covers:** Unit 4 (exploration strategies: epsilon-greedy, epsilon decay,
UCB, Boltzmann, Thompson Sampling, and high-level curiosity-driven
exploration).
**Concepts from:** Unit 4 numbered examples 01 to 05.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
**Upper Confidence Bound (UCB)** selects actions based on:

a) The highest average reward only
b) A combination of estimated value AND an exploration bonus proportional to
uncertainty (less-tried actions get higher bonus)
c) A random temperature parameter
d) The Bayesian posterior over rewards

---

### Question 2 (10 points)
**Boltzmann (softmax) exploration** selects actions by:

a) Choosing the action with the highest Q-value deterministically
b) Sampling actions with probabilities proportional to exp(Q/tau), where tau
(temperature) controls exploration breadth
c) Adding Gaussian noise to actions
d) Using the UCB formula

---

### Question 3 (10 points)
**Epsilon decay** means:

a) The learning rate decreases over time
b) Epsilon starts high (more exploration) and decreases during training (more
exploitation), balancing exploration early and convergence later
c) The discount factor is reduced
d) The replay buffer shrinks

---

### Question 4 (10 points)
At a **high level**, intrinsic motivation / curiosity-driven exploration
encourages an agent to:

a) Only exploit known high-reward states
b) Visit novel or surprising states by giving an intrinsic reward bonus for
states where prediction error is high
c) Reduce the number of actions
d) Ignore external rewards entirely

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Implement **epsilon-greedy with decay** in Python:
- Parameters: n_actions=4, epsilon_start=1.0, epsilon_end=0.05, epsilon_decay=0.995.
- Write `select_action(q_values, epsilon)`: returns random action with prob
  epsilon, greedy action otherwise.
- Write `update_epsilon(epsilon)`: applies
  `epsilon = max(epsilon_end, epsilon * epsilon_decay)`.
- Print epsilon values after 0, 100, and 500 decay steps (compute manually
  using the formula).

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Compare **epsilon-greedy** and **UCB** exploration strategies. In what
scenario would UCB be preferred, and why?

---

### Question 7 (15 points)
What is the **exploration-exploitation dilemma** in the multi-armed bandit
problem? Explain how **Thompson Sampling** addresses it.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
You are running a multi-armed bandit style online experiment with several
uncertain actions and limited data. What exploration strategy would you
recommend, and why? Choose one of the methods taught in Unit 4
(for example: epsilon-greedy with decay, UCB, or Thompson Sampling).

---

**Mapping:** CLO5; notebooks: `01_exploration_strategies`,
`02_balancing_exploration`, `03_adaptive_exploration_ucb`,
`04_comparing_exploration_methods`, `05_tuning_exploration_parameters`.

**For:** AIAT 123 - Reinforcement Learning
