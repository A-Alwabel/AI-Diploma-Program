# Retrieval Quiz — Week 25

**Week 25 of 35 · Course 09 — AIAT 123 (Reinforcement Learning)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The Unit 4 notebook on tuning exploration parameters sweeps four epsilon settings on the same five-variant A/B test, **50 independent runs per epsilon**, then asks how often a lone run would have picked each setting. Three rows of its table, plus the tally from its closing cell:

```
   ε    |  mean ± std   |  min … max across runs
  0.05 |   599.6 ±  76.2 |   314 …   697
   0.1 |   623.7 ±  50.1 |   475 …   691
   0.3 |   610.8 ±  35.7 |   508 …   673

Single-run winners: ε=0.01: 6, ε=0.05: 15, ε=0.1: 23, ε=0.3: 6
The 50-run mean picks ε = 0.1; a single run agrees only 23/50 of the time.
```

A classmate insists: *'epsilon = 0.05 can beat epsilon = 0.1 — look, its top run hit 697 and 0.1 peaked at 691.'* Which reply refutes the claim most directly?

A) A maximum of 697 does not belong in the ε = 0.05 row, whose mean is 599.6; a single run of that setting should stay within one standard deviation (±76.2) of it.  
B) Neither a top run nor a mean settles it, because total reward is the wrong statistic for exploration rates; the whole sweep would have to be redone in cumulative regret before any ranking is made.  
C) The spread column should decide it, and ε = 0.3 has the tightest band (±35.7) and the highest floor (508), so neither ε = 0.05 nor ε = 0.1 deserved to be crowned as the best setting in the first place.  
D) Top run against top run is a one-draw comparison: the 50-run means (599.6 vs 623.7) and the single-run win tally (15 vs 23) both put ε = 0.1 ahead, and 23/50 is the printed warning.  

---

### Question 2

DQN stores each transition in a replay buffer and trains on a random minibatch drawn from it, rather than on the transition it just took. What does that buy?

A) Consecutive steps are correlated; sampling at random breaks that, and each transition can be reused  
B) The buffer keeps a fixed target for the Q-update, which is what stops the estimates oscillating  
C) Once the buffer is filled the agent can be trained with no further interaction with the environment  
D) Random sampling lets one large minibatch replace many small ones, which is what shortens wall-clock training  

---

### Question 3

DQN keeps a second copy of the network whose weights are refreshed at intervals of a few hundred steps, and computes its update target from that copy. Why?

A) Two copies double the parameter count, and the larger model fits the value function more closely  
B) The frozen copy supplies the random sample that a replay buffer would otherwise have to store  
C) The target moves whenever the network moves; freezing the copy stops the network chasing its own output  
D) Refreshing weights rarely means fewer gradient steps, so the same policy is learned with less compute overall  

---

### Question 4

In the per-digit error chart of the lesson, both models were fitted on the identical **5,000** MNIST training images. Logistic regression misreads **143** of the test threes; the network with **128** ReLU hidden units misreads **73** of them, and it makes fewer errors on 9 of the 10 digits — digit **4** is the exception (**81** errors for logistic regression against **89** for the network). Which account of *how each model uses a pixel* explains this pattern?

A) The network needs fewer labelled threes to fit well, because its hidden units share what they learn across the ten digit classes, while logistic regression has to fit each class on its own  
B) Logistic regression scores each pixel with one fixed weight, so a slanted or off-centre 3 misses its template; the hidden layer combines pixels non-linearly and recovers it  
C) The network's loss surface is convex, so Adam reaches the global minimum, while the logistic-regression solver stopped short at `max_iter=500` on the harder digits  
D) The network trains on pixels divided by 255 while logistic regression sees `StandardScaler` output, and raw-scale pixels preserve more of the stroke information  

---

### Question 5

The lesson's `model.summary()` lists `conv2d_1 (Conv2D)`, 64 filters, at **18,496** parameters, and the `dense (Dense)` layer of 64 units that follows `Flatten` at **102,464** — the largest line in a **121,930**-parameter model. The conv layer turns a 13×13×32 map into an 11×11×64 one; the Dense layer reads a **1,600**-long vector. Which statement correctly accounts for the gap between the two counts?

A) Each of the 64 filters is one 3×3×32 weight block reused at each position of the map, so a pattern is learned once; Dense buys a separate weight per input per unit  
B) Flattening throws away where each value sat in the 13×13 grid, so the Dense layer has to compensate for the lost position information with many more weights than a conv layer needs  
C) Weight sharing keeps the conv layer from memorising, which is why the lesson can train without holding out a validation split  
D) The convolution already includes its non-linearity, so it saves the parameters that a separate ReLU stage would otherwise add  

---

### Question 6

Course 07's Unit 5 bias-audit notebook disclosed that its association scores were **simulated** rather than measured; its skip-gram experiment shows where real ones come from. In a real audit, what produces those numbers?

A) A published audit of a comparable system, rescaled to this model's vocabulary size  
B) The share of each demographic group in the training corpus, counted from the raw text  
C) Cosine similarities in the model's own trained vectors, or its outputs on probe inputs  
D) The auditor's own judgement of how strongly each profession reads as male or as female, written into the table  

---

### Question 7

The Unit 2 outliers lesson profiled the cleaned **889**-row `Fare` column and printed mean **32.10**, median **14.45**, quartiles **7.90** to **31.00** and a maximum of **512.33**. Its IQR rule flagged **114** fares (12.8% of passengers), **102** of them first class. A colleague's slide carries one line: "average fare: 32.10 pounds". Which revision does that profiling support?

A) Replace it with the median 14.45 and the 7.90 to 31.00 quartile range, and say the column is right-skewed, since 32.10 sits above the third quartile  
B) Keep 32.10 but recompute it after dropping the 114 IQR-flagged fares first, so the mean then describes the typical passenger rather than the first-class tail  
C) Standardise `Fare` to mean 0 and standard deviation 1 before quoting the average, so the first-class tail no longer pulls the reported figure away from the centre of the column  
D) Keep 32.10 and add the standard deviation 49.70, so readers can see the spread around the average and judge the typical fare for themselves  

---

### Question 8

Course 05's cleaning lesson printed, on the 891-row Titanic manifest, `Original: 891 rows → After dropping: 183 rows (79% of the data thrown away)`, and that the share of passengers with no cabin recorded is 18.5% in first class, 91.3% in second and 97.6% in third. What do those lines together say about dropping rows with missing values here?

A) It costs 708 rows, which is affordable because 183 rows are still enough to fit the model  
B) It is the safe default, because an imputed age is invented data and invented data biases whatever is fitted on it  
C) It is unnecessary once `Age` is imputed, since imputation fills the columns the manifest has  
D) It costs 708 rows, and it removes second- and third-class passengers at a far higher rate than first-class  

---

### Question 9

Before training anything, the single-neuron lesson printed this table:

```
     z |  sigmoid |    tanh |  relu
   1.0 |    0.731 |   0.762 |   1.0
   3.0 |    0.953 |   0.995 |   3.0
```

The training cell that followed compiled the neuron with `Adam(learning_rate=0.05)` and `loss="mse"`. A classmate files sigmoid, tanh and relu under "things that score the model". What job do the three functions in this table actually do inside a `Dense(1)` neuron?

A) They measure how far the neuron's output is from the 0/1 label, which is the scoring job that `mse` also performs in the compile line  
B) They decide how much each weight moves after a batch, which is why the learning rate 0.05 is set right beside them  
C) They turn the weighted sum `z` into the neuron's output, which is why each column is a different reshaping of the same `z`  
D) They switch random units off during training to limit overfitting, the way dropout does in a larger network  

---

### Question 10

On the same unweighted graph, Course 01's BFS returned `A -> C -> F` (2 edges) and its DFS returned `A -> B -> E -> F` (3 edges). Which search is guaranteed to return a path with the fewest edges, and why?

A) Depth-First Search, because the first goal it reaches is the one it returns  
B) Breadth-First Search, because it finishes one depth level before starting the next  
C) A\* search, because a heuristic that orders the frontier is what makes a path optimal  
D) The two searches equally, since each visits the same set of nodes on this graph before stopping  

---
