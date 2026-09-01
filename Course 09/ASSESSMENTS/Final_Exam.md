# Final Exam: Reinforcement Learning
## AIAT 123

**Time Limit:** 2 hours  
**Total Points:** 100  
**Coverage:** Required numbered path across Units 1-5  
**Instructions:** Answer all questions. Show reasoning for partial credit.
Keep answers within the scope of the numbered student path.  

**Marking scheme:** Part 1 (Q1–Q5): 4 pts each = 20. Part 2 (Q6–Q8): 10 pts each = 30.
Part 3 (Q9–Q10): 15 pts each = 30. Part 4 (Q11–Q12): 10 pts each = 20. **Total: 100.**

Part 1 is scored on the correct option only, with no partial credit. Everywhere else,
correct reasoning earns partial credit even when a number or a line of code is wrong.

---

## Part 1: Multiple Choice (20 points)

Each question quotes output that a Unit 1–5 notebook actually printed. Read the numbers
before you read the options.

### Question 1 (4 points)
Unit 1's value-iteration lesson runs a 3x3 grid world with **-1 for every ordinary step,
+10 for entering the goal, -10 for entering the pit, and gamma = 0.90**. It prints this
converged value table and the greedy policy read off it:

```
State values:              Greedy policy:
  4.58   6.20   8.00         →   →   ↓
  6.20   8.00  10.00         →   →   ↓
  P     10.00   G            P   →   G
```

The tile immediately **above the pit** holds **6.20** — a positive value, even though one of
its four actions steps straight into the -10 pit. Which explanation is correct?

A) The pit's -10 is discounted once per sweep, so by the time the table converges 0.90 raised to the sweep count has shrunk it below -1.  
B) The sweep skips terminal states, so `transition(3, "down")` returns no pit transition, leaving the -10 out of that tile's backup.  
C) The backup keeps the maximum over four actions, and the best moves right: -1 + 0.90 x 8.00 = 6.20, so the pit shows in the arrow.  
D) The backup averages the four action targets instead of maximising, and the three non-pit actions outweigh the single -10.  

---

### Question 2 (4 points)
Unit 2's cliff-walking lesson trains **SARSA** and **Q-learning** on `CliffWalking-v1` with
the same environment, the same seed and identical settings (alpha = 0.5, gamma = 1.0,
epsilon = 0.1, 500 episodes). Only the TD target line differs. It prints:

```
Greedy path length  - SARSA: 17 steps | Q-learning: 13 steps
Average return over the last 100 TRAINING episodes (epsilon still 0.1):
   SARSA      :  -24.49
   Q-learning :  -47.96
```

Which reading of those four numbers is correct?

A) Q-learning's greedy path is the shorter one, and SARSA still earned more in training because its target prices in the exploratory steps taken.  
B) SARSA's greedy path is the shorter one, and it earned more in training because a shorter route pays fewer -1 step penalties per episode.  
C) Q-learning earned less while training because gamma = 1.0 leaves its max-target undiscounted, so the values it bootstraps from grow without bound.  
D) Both agents converged on the same greedy path, and the 23-point gap in training return is down to the different random seeds the two runs were given.  

---

### Question 3 (4 points)
Unit 3's monitoring lesson trains two tabular Q-learning agents on slippery
`FrozenLake-v1` — same algorithm, same environment, different hyperparameters — then
evaluates both greedily on 1000 fresh episodes. It prints:

```
Well-tuned run  : final rolling std = 0.500 | final rolling mean = 0.495
Badly-tuned run : final rolling std = 0.099 | final rolling mean = 0.010

Evaluation on 1000 fresh episodes with exploration turned off (greedy policy):
  Well-tuned agent  : 0.726 success rate (training curve ended at 0.498)
  Badly-tuned agent : 0.040 success rate (training curve ended at 0.014)
```

A dashboard that plots only the rolling standard deviation flags the **badly-tuned** run as
the more stable of the two. What is the error?

A) The two standard deviations were computed over different rolling window lengths, so 0.500 and 0.099 are not on a comparable scale.  
B) With a 0/1 reward the spread is mechanically tied to the mean, so a run stuck at 0.010 has almost no spread; 0.099 signals failure.  
C) Rolling standard deviation only describes the exploring behaviour policy, so both runs would show the same spread once exploration is switched off.  
D) The well-tuned run's 0.500 is an artefact of its greedy evaluation at 0.726; the training std should be recomputed from the evaluation episodes.  

---

### Question 4 (4 points)
Unit 4's tuning lesson runs epsilon-greedy on the same 5-variant A/B test at four values of
epsilon, **50 runs of 2000 rounds each**, and prints:

```
Total reward per epsilon (50 runs of 2000 rounds each):
   ε    |  mean ± std   |  min … max across runs
  0.01 |   489.0 ± 120.3 |   292 …   704
  0.05 |   599.6 ±  76.2 |   314 …   697
   0.1 |   623.7 ±  50.1 |   475 …   691
   0.3 |   610.8 ±  35.7 |   508 …   673

Best epsilon by MEAN total reward: ε=0.1
The single-run trap: judging by one run alone, 27 of 50 runs
would have crowned a DIFFERENT epsilon than the 50-run average does.
```

A student reports: *"epsilon = 0.01 is the best setting — I ran it once and scored 704, the
highest total anywhere in this table."* What is the strongest objection?

A) 704 is impossible for epsilon = 0.01, whose mean is only 489.0; a single run cannot exceed its own setting's mean by more than one standard deviation.  
B) Total reward is the wrong statistic for ranking exploration rates; only cumulative regret can order these four settings correctly.  
C) Epsilon = 0.01 explores too little for its runs to be compared with the others, so that row should be dropped from the table entirely.  
D) 704 is one draw from the widest-spread row (±120.3 on a mean of 489.0), and the printed 27-of-50 figure says one run cannot rank epsilon at all.  

---

### Question 5 (4 points)
Unit 5's model-based vs model-free lesson runs both agents on `FrozenLake-v1` over
**20 seeds x 300 episodes**, with the same learning rule, the same discount and the same
epsilon = 0.2. The only difference: after each real environment step the model-based agent
also replays 20 remembered transitions. It prints:

```
  Success rate after ...   | model-free | model-based
  -------------------------|------------|------------
  50 episodes              |      0.020 |      0.332
  100 episodes             |      0.217 |      0.584
  the last 50 episodes     |      0.747 |      0.746
```

and notes that the model-based agent did about **20x more Q-updates** for the same
environment experience. What do these numbers support?

A) The model-based agent had 20x more experience of the environment, so its early lead at 50 and 100 episodes is what you would expect.  
B) The model-based agent is the better choice whenever compute is the scarce resource, because it extracts more learning per unit of computation.  
C) The model-based agent is more sample-efficient — it reaches a given success rate in fewer environment steps — but it does not end higher.  
D) The 300-episode budget is too short to separate the two: with more episodes the model-based agent's early lead would reappear as a higher final rate.  

---

## Part 2: Short Answer (30 points)

### Question 6 (10 points)
Explain the difference between:

- **state**
- **action**
- **reward**
- **policy**

Ground all four in **one** environment the course actually ran (FrozenLake, CartPole, Taxi,
CliffWalking or the recommendation setting). For that environment, also state **the reward
rule as the course used it** and **what one episode's return means** there.

---

### Question 7 (10 points)
Compare **Q-learning**, **SARSA**, and **Policy Gradient** at a high level.

Your answer should mention:

- what each method learns
- when each method is a reasonable choice
- one limitation of each

---

### Question 8 (10 points)
Explain the **exploration-exploitation dilemma** and compare
**epsilon-greedy** with **UCB** or **Thompson Sampling** at a high level.

---

## Part 3: Practical / Coding (30 points)

### Question 9 (15 points)
Write Python code for one **value iteration** sweep on a small grid-world MDP.

Requirements:

- assume a small discrete state space
- compute the Bellman optimality update for each non-terminal state
- store the updated state values
- explain in one sentence why terminal states are handled differently

---

### Question 10 (15 points)
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

### Question 11 (10 points)
Design an RL formulation for **product recommendation** or **resource optimization**.

Define:

1. state
2. action
3. reward
4. one challenge with delayed or misleading rewards

---

### Question 12 (10 points)
You are deploying an RL system in a real-world setting.

Answer both:

1. What is one **ethical or safety risk** such as reward hacking,
   unsafe exploration, manipulation, or unfair exposure?
2. What is one **evaluation metric or testing strategy** you would use before deployment?

---

## Grading Note

Strong answers should connect algorithms to the actual course flow and should
not depend on supplemental-only topics:

- Unit 1: RL foundations and MDPs
- Unit 2: classical prediction and control
- Unit 3: deep RL
- Unit 4: exploration strategies
- Unit 5: applications, advanced topics, and deployment thinking

Ethics, safety, and fairness are assessed here at a high-level judgment level,
not as a separate deep technical specialization block.

## End of Exam
