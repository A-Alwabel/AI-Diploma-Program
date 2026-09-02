# Cumulative Retrieval Quiz — Week 25

**Programme week 25 of 35 · Current course: Course 09 — AIAT 123 (Reinforcement Learning), Unit 3 / Unit 4**
**Placement: session 4 of the week (s100), in the closing block.**

- **15 minutes**, taken **in class at the END of the session**. Not homework.
- **Not graded.** No mark from this paper reaches your course grade.
- Write your answers, then your instructor **works every correct answer aloud immediately afterwards**. Stay for it.
- Ten items. Three from what you are studying now, seven from courses you finished earlier. The earlier items carry their own context.

---

### 1. [Course 09 · Unit 4]
Unit 4's tuning lesson runs epsilon-greedy on the same 5-variant A/B test at four values of epsilon, **50 runs of 2000 rounds each**, and prints:

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

A student reports: *"epsilon = 0.01 is the best setting — I ran it once and scored 704, the highest total anywhere in this table."* What is the strongest objection?

A) 704 is impossible for epsilon = 0.01, whose mean is 489.0; a single run of that setting stays within one standard deviation of its own printed mean.
B) Total reward is the wrong statistic for ranking exploration rates; cumulative regret is the one that orders these four settings.
C) Epsilon = 0.01 explores too little for its runs to be compared with the others, so that row should be dropped from the table entirely.
D) 704 is one draw from the widest-spread row (±120.3 on a mean of 489.0), and the printed 27-of-50 figure says one run is not enough to rank epsilon.

---

### 2. [Course 09 · Unit 3]
DQN stores each transition in a replay buffer and trains on a random minibatch drawn from it, rather than on the transition it just took. What does that buy?

A) Consecutive steps are correlated; sampling at random breaks that, and each transition can be reused
B) The buffer keeps a fixed target for the Q-update, which is what stops the estimates oscillating
C) Once the buffer is filled the agent can be trained with no further interaction with the environment
D) Random sampling lets one large minibatch replace many small ones, which is what shortens wall-clock training

---

### 3. [Course 09 · Unit 3]
DQN keeps a second copy of the network whose weights are refreshed at intervals of a few hundred steps, and computes its update target from that copy. Why?

A) Two copies double the parameter count, and the larger model fits the value function more closely
B) The frozen copy supplies the random sample that a replay buffer would otherwise have to store
C) The target moves whenever the network moves; freezing the copy stops the network chasing its own output
D) Refreshing weights rarely means fewer gradient steps, so the same policy is learned with less compute overall

---

### 4. [Course 08 · Unit 1]
A team replaces a logistic-regression classifier with a two-layer neural network on the **same raw pixels** and the **same 10,000 test images**. Test accuracy rises from **0.8879 to 0.9130** — 1,121 wrong images down to 870. Which statement best explains the advantage the network has here?

A) It needs fewer labelled training images, because its layers share information between the ten classes
B) It learns hierarchical features from the raw pixels instead of using each pixel as a fixed feature
C) It is guaranteed to reach the global minimum of its loss, which logistic regression is not
D) It removes the need to scale or normalise the inputs before training

---

### 5. [Course 08 · Unit 2]
Your first model for a 28×28 image task is a `Dense` network on flattened pixels. You replace it with a CNN and accuracy improves. What does the **convolutional layer** give you that the `Dense` layer did not?

A) It treats each image as one flat vector, so the position of a pixel no longer changes the result
B) Its weight sharing removes the risk of overfitting, so a held-out validation split is no longer needed
C) It supplies the non-linearity itself, so no ReLU is needed after the layer
D) The same small filter runs at each position, so a pattern learned once is found anywhere

---

### 6. [Course 07 · Unit 5]
Course 07's Unit 5 bias-audit notebook disclosed that its association scores were **simulated** rather than measured; its skip-gram experiment shows where real ones come from. In a real audit, what produces those numbers?

A) A published audit of a comparable system, rescaled to this model's vocabulary size
B) The share of each demographic group in the training corpus, counted from the raw text
C) Cosine similarities in the model's own trained vectors, or its outputs on probe inputs
D) The auditor's own judgement of how strongly each profession reads as male or as female, written into the table

---

### 7. [Course 05 · Unit 2]
In Course 05 Unit 2 you profiled two columns of the same 891-row Titanic manifest. `Age` printed a skew of **0.53** and a median near **26**; `Fare` printed a skew of **4.79**, with most passengers in the first histogram bin and a few tickets reaching **512** pounds. A colleague's report quotes one "average" per column. What does the profiling step tell you to do, and why?

A) Report `Fare` by its median and quartiles and say the column is skewed, because a single mean describes almost nobody in that shape
B) Report the mean for both columns, because the mean uses all the rows while the median throws away everything except the middle one
C) Drop the tickets near 512 pounds as outliers first, because the mean of `Fare` becomes a fair summary once that tail is gone
D) Standardise both columns to mean 0 and standard deviation 1 first, because scaling removes the skew and makes the two averages comparable

---

### 8. [Course 05 · Unit 2]
Course 05's cleaning lesson printed, on the 893-row Titanic manifest, `dropna(): 893 rows -> 184 rows (79.4% deleted)` and `76.8% of the people with a missing Age were 3rd class`. What do those two lines together say about dropping rows with missing values here?

A) It costs 709 rows, which is affordable because 184 rows are still enough to fit the model
B) It is the safe default, because an imputed age is invented data and invented data biases the fit
C) It is unnecessary once `Age` is imputed, since imputation fills the columns the manifest has
D) It costs 709 rows, and it takes third-class passengers out at a higher rate than everyone else

---

### 9. [Course 01 · Unit 4]
Course 01 Unit 4 plotted and trained three activation functions on the same single neuron (test accuracy sigmoid 0.860, tanh 0.850, relu 0.860). Which group below lists **activation functions** used in a feedforward neural network?

A) ReLU, Sigmoid, Tanh
B) Adam, SGD, RMSprop
C) MSE, Cross-Entropy, Hinge
D) Dropout, Batch Normalization, Early Stopping

---

### 10. [Course 01 · Unit 1]
On the same unweighted graph, Course 01's BFS returned `A -> C -> F` (2 edges) and its DFS returned `A -> B -> E -> F` (3 edges). Which search is guaranteed to return a path with the fewest edges, and why?

A) Depth-First Search, because the first goal it reaches is the one it returns
B) Breadth-First Search, because it finishes one depth level before starting the next
C) A\* search, because a heuristic that orders the frontier is what makes a path optimal
D) Either search, since both visit the same set of nodes on this graph before stopping

---

**End of paper. Hand nothing in. Stay for the worked answers.**
