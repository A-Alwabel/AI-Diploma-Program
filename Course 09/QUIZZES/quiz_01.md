# Quiz 01 – Unit 1: Reinforcement Learning Fundamentals
## AIAT 123 - Reinforcement Learning

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as
bonus or toward total)
**Covers:** Unit 1 RL basics, MDPs, value intuition, discounting, and
introductory exploration concepts.
**Concepts from:** Unit 1 numbered notebooks `01` to `07` and related slides.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
Which best describes the difference between **supervised learning** and
**reinforcement learning**?

a) Supervised learning uses rewards; RL uses labeled data
b) RL learns from interaction and feedback (rewards), while supervised
   learning learns from labeled input-output pairs
c) RL always requires more data
d) There is no difference

---

### Question 2 (10 points)
In a **Markov Decision Process (MDP)**, the Markov property states that:

a) Future states depend on all past states
b) The next state depends only on the current state and action, not on history
c) The reward depends only on the initial state
d) Actions have no effect on future states

---

### Question 3 (10 points)
What is the role of the **discount factor (gamma)** in RL?

a) It speeds up training
b) It balances the importance of immediate vs future rewards
   (`0` = only immediate, `1` = equal future weight)
c) It determines the number of training episodes
d) It controls the learning rate

---

### Question 4 (10 points)
In the **epsilon-greedy** exploration strategy:

a) The agent always picks the action with the highest known reward
b) With probability epsilon the agent picks a random action (explore);
   otherwise it picks the greedy best action (exploit)
c) Epsilon controls the learning rate
d) The agent never explores once training begins

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write Python code to implement a **simple Q-learning update** for a grid world:
- Initialize a Q-table of shape (5, 4) with zeros (5 states, 4 actions).
- Given: state=2, action=1, reward=10, next_state=3, alpha=0.1, gamma=0.9.
- Write the Q-learning update rule:
  `Q[s, a] += alpha * (r + gamma * max(Q[s', :]) - Q[s, a])`
- Print the updated Q[2, 1] value.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain what a **policy** is in RL, and describe the difference between a
**deterministic policy** and a **stochastic policy**.

---

### Question 7 (15 points)
Describe the **exploration-exploitation dilemma**. Why is it a challenge, and
give **one practical way** to reduce poor exploration behavior, such as
epsilon decay or a clearer exploration schedule.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
An RL agent trained in CartPole achieves high rewards during training but fails
at evaluation. What might be the cause, and what would you change
(`e.g.`, more episodes, a better exploration schedule, or reward design)?

---

**Mapping:** CLO1; notebooks: Unit 1 numbered path, with strongest links to
`02`, `03`, `05`, `06`, and `07`.

**For:** AIAT 123 - Reinforcement Learning
