# Final Exam: Reinforcement Learning
## AIAT 123

**Time Limit:** 2 hours  
**Total Points:** 100  
**Coverage:** Units 1-5  
**Instructions:** Answer all questions. Show reasoning for partial credit.  
**Instructor key:** `../DOCS/SOLUTIONS/final_exam_solution.md`

---

## Part 1: Multiple Choice (20 points)

### Question 1 (5 points)
Which statement best describes a **Markov Decision Process (MDP)**?

A) A system with labels but no actions  
B) A framework with states, actions, rewards, and transitions  
C) A neural network architecture  
D) A dataset used for supervised learning

---

### Question 2 (5 points)
Why is **Q-learning** called an off-policy method?

A) It cannot use exploration  
B) It updates toward the greedy next action value, even if the behavior
policy explored differently  
C) It always needs a model of the environment  
D) It is only used for continuous action spaces

---

### Question 3 (5 points)
What is the main purpose of **experience replay** in DQN?

A) To reduce the number of actions  
B) To break correlations between consecutive samples and reuse experience  
C) To remove the need for epsilon-greedy  
D) To replace the target network

---

### Question 4 (5 points)
Which statement about **model-based RL** is most accurate?

A) It never uses planning  
B) It learns or uses a model of the environment and can plan with it  
C) It always outperforms model-free RL  
D) It is the same as Monte Carlo learning

---

## Part 2: Short Answer (30 points)

### Question 5 (10 points)
Explain the difference between:

- **state**
- **action**
- **reward**
- **policy**

Use one simple environment such as FrozenLake, CartPole, or a recommendation system.

---

### Question 6 (10 points)
Compare **Q-learning**, **SARSA**, and **Policy Gradient** at a high level.

Your answer should mention:

- what each method learns
- when each method is a reasonable choice
- one limitation of each

---

### Question 7 (10 points)
Explain the **exploration-exploitation dilemma** and compare
**epsilon-greedy** with **UCB** or **Thompson Sampling**.

---

## Part 3: Practical / Coding (30 points)

### Question 8 (15 points)
Write Python code for one **value iteration** sweep on a small grid-world MDP.

Requirements:

- assume a small discrete state space
- compute the Bellman optimality update for each non-terminal state
- store the updated state values
- explain in one sentence why terminal states are handled differently

---

### Question 9 (15 points)
Write Python or pseudocode for a minimal **Q-learning** training loop.

Requirements:

- initialize a Q-table
- use epsilon-greedy action selection
- take one environment step
- apply the Q-update
- repeat across episodes

You do not need to implement a full environment.

---

## Part 4: Application and Judgment (20 points)

### Question 10 (10 points)
Design an RL formulation for **product recommendation** or **resource optimization**.

Define:

1. state
2. action
3. reward
4. one challenge with delayed or misleading rewards

---

### Question 11 (10 points)
You are deploying an RL system in a real-world setting.

Answer both:

1. What is one **ethical or safety risk** such as reward hacking,
   unsafe exploration, manipulation, or unfair exposure?
2. What is one **evaluation metric or testing strategy** you would use before deployment?

---

## Grading Note

Strong answers should connect algorithms to the actual course flow:

- Unit 1: RL foundations and MDPs
- Unit 2: classical prediction and control
- Unit 3: deep RL
- Unit 4: exploration strategies
- Unit 5: applications, advanced topics, and deployment thinking

## End of Exam
