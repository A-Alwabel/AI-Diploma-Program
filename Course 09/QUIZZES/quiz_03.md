# Quiz 03 – Unit 3: Deep Reinforcement Learning
## AIAT 123 - Reinforcement Learning

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as
bonus or toward total)
**Covers:** Unit 3 DQN, policy-gradient intuition, actor-critic, replay,
target networks, and simplified PPO-style stability ideas.
**Concepts from:** Unit 3 numbered example notebooks and related slides.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What problem does **experience replay** solve in DQN?

a) It speeds up the GPU
b) It breaks the correlation between consecutive training samples by storing
   transitions and sampling randomly from a replay buffer
c) It replaces the need for a target network
d) It allows the agent to learn from a single episode

---

### Question 2 (10 points)
Why does DQN use a separate **target network** updated less frequently?

a) To increase the number of parameters
b) To replace experience replay
c) To stabilize training by providing a fixed target for Q-value updates,
   preventing oscillations
d) To process images faster

---

### Question 3 (10 points)
In **REINFORCE (policy gradient)**, the gradient update uses:

a) The gradient of the log probability of the action, weighted by the
   cumulative return
b) Only the reward from the last step
c) The Q-table values
d) A fixed supervised signal

---

### Question 4 (10 points)
The **Actor-Critic** method combines:

a) Supervised learning and unsupervised learning
b) DQN and SARSA
c) Q-learning and Monte Carlo
d) A policy (actor) that selects actions and a value function (critic)
   that evaluates those actions

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write a minimal **DQN setup** using PyTorch for CartPole:
- Define a neural network: 2 hidden layers (64 units each, ReLU), input=4
  (CartPole state), output=2 (actions).
- Write the select_action method (epsilon-greedy using network Q-values).
- Write the Bellman update target: target = r + gamma * max(Q(s', a')).
- Show how you compute the MSE loss between predicted Q[s,a] and the target.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain **reward shaping**: what it is, why it is used, and one risk of using
it poorly.

---

### Question 7 (15 points)
At a high level, what advantage is **Proximal Policy Optimization (PPO)**
trying to achieve over vanilla Policy Gradient (REINFORCE)? Describe the kind
of update constraint it enforces.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A DQN agent trained in a small Gym-style environment achieves near-zero reward
for many episodes before improving. What is the likely cause, and how do
**experience replay** and **epsilon decay** help?

---

**Mapping:** CLO3, CLO4; notebooks: Unit 3 numbered path, especially `01`,
`02`, `03`, and `05`.

**For:** AIAT 123 - Reinforcement Learning
