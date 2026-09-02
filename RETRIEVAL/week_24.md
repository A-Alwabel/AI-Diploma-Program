# Cumulative Retrieval Quiz — Week 24

**Programme week 24 of 35 · Current course: Course 09 — AIAT 123 (Reinforcement Learning), Unit 2 / Unit 3**
**Placement: session 4 of the week (s96), in the closing block.**

- **15 minutes**, taken **in class at the END of the session**. Not homework.
- **Not graded.** No mark from this paper reaches your course grade.
- Write your answers, then your instructor **works every correct answer aloud immediately afterwards**. Stay for it.
- Ten items. Three from what you are studying now, seven from courses you finished earlier. The earlier items carry their own context.

---

### 1. [Course 09 · Unit 2]
Unit 2's cliff-walking lesson trains **SARSA** and **Q-learning** on `CliffWalking-v1` with the same environment, the same seed and identical settings (alpha = 0.5, gamma = 1.0, epsilon = 0.1, 500 episodes). Only the TD target line differs. It prints:

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

### 2. [Course 09 · Unit 2]
Unit 2 contrasts Monte Carlo control with the TD methods that follow it. How does a Monte Carlo method estimate the value of a state?

A) By bootstrapping: it replaces the rest of the episode with its current estimate of the next state
B) By averaging the actual returns observed from that state over complete episodes
C) By sweeping the Bellman equation across the state space, using the environment's transition table
D) By fitting a neural network to the visited states, since tables do not scale

---

### 3. [Course 09 · Unit 3]
Unit 3's monitoring lesson trains two tabular Q-learning agents on slippery `FrozenLake-v1` — same algorithm, same environment, different hyperparameters — then evaluates both greedily on 1000 fresh episodes. It prints:

```
Well-tuned run  : final rolling std = 0.500 | final rolling mean = 0.495
Badly-tuned run : final rolling std = 0.099 | final rolling mean = 0.010

Evaluation on 1000 fresh episodes with exploration turned off (greedy policy):
  Well-tuned agent  : 0.726 success rate (training curve ended at 0.498)
  Badly-tuned agent : 0.040 success rate (training curve ended at 0.014)
```

A dashboard that plots only the rolling standard deviation flags the **badly-tuned** run as the more stable of the two. What is the error?

A) The two standard deviations were computed over different rolling window lengths, so 0.500 and 0.099 are not on a comparable scale.
B) With a 0/1 reward the spread is mechanically tied to the mean, so a run stuck at 0.010 has almost no spread; 0.099 signals failure.
C) Rolling standard deviation describes just the exploring behaviour policy, so both runs would show the same spread once exploration is switched off.
D) The well-tuned run's 0.500 is an artefact of its greedy evaluation at 0.726; the training std should be recomputed from the evaluation episodes.

---

### 4. [Course 07 · Unit 4]
Course 07 Unit 4 measured how much gradient signal survives travelling backwards through a plain RNN with typical weights: about 5×10⁻¹ after 1 step, 6×10⁻⁶ after 10 steps, and 7×10⁻³⁰ after 50 steps. Which conclusion does that measurement support?

A) The signal that would link far-apart words dies exponentially with distance; attention links two distant positions in one step
B) The recurrent weights grow exponentially during training, which is the problem that transformers solve by clipping the gradient
C) The network's accuracy falls as sentences get longer, which is why transformers truncate their inputs to 512 tokens
D) The hidden state vector is too short to hold a long sentence, which is why transformers use a much longer one

---

### 5. [Course 07 · Unit 4]
In Course 07 Unit 4 the pretrained English sentiment model labelled *"I have no opinion about this product"* **NEGATIVE at 0.9997**, and gave an Arabic sentence **P(POSITIVE) = 0.42** after splitting it into 5.5 word-pieces per word. What do these two results, read together, show?

A) The model has no neutral class, so it picks a side either way; and 0.42 on Arabic means "nothing readable", not "unsure"
B) The model is well calibrated: it is confident where the sentiment is clear, and hesitant where the sentiment is genuinely ambiguous
C) The Arabic sentence was correctly judged neutral, which shows the model handles other languages acceptably
D) Both outputs are casing failures, and both disappear once the text is lowercased before it is scored

---

### 6. [Course 07 · Unit 5]
In a Course 07 Unit 5 bias audit you build pairs of test sentences that are identical except for one demographic word — *he* / *she*, or a male / female name — and compare the model's output on each pair. What does that test measure?

A) How large the model's vocabulary is, since each name has to be a known token already
B) Whether the output moves when the demographic attribute alone is changed and the rest is held fixed
C) How accurate the model is on the group each name belongs to, measured against held-out labels for that group
D) How stable the model is under paraphrase, since the two sentences carry the same meaning

---

### 7. [Course 04 · Unit 4]
Course 04 clustered 1,994 communities on 4 scaled crime features and printed:

```
K=2   Inertia=5347.86   Silhouette=0.3967       K=6    Inertia=2398.46   Silhouette=0.2954
K=3   Inertia=4041.38   Silhouette=0.3134       K=8    Inertia=1970.75   Silhouette=0.3007
K=4   Inertia=3124.93   Silhouette=0.3153       K=10   Inertia=1720.82   Silhouette=0.2941
```

The elbow falls at K = 4; the silhouette peaks at K = 2; the lesson itself clusters at K = 3. How should K be settled?

A) Take K = 10: it posts the lowest inertia anywhere in the table, and lower inertia means tighter, better clusters
B) Take K = 2: the silhouette is the score that measures separation, so it settles the question
C) The disagreement is a symptom of unscaled features; rescaling the four crime columns would make the two criteria converge
D) The two criteria measure different things and disagree, so K is settled by what the clusters are for

---

### 8. [Course 04 · Unit 5]
Course 04 Unit 5 tunes hyperparameters with grid search and with random search on the same model. What does random search buy, and at what cost?

A) It walks the whole grid, so whichever setting in the grid is best gets evaluated
B) It narrows the search around the best setting found so far, so later draws beat earlier ones
C) It draws a set number of settings at random, so you fix the budget rather than the grid
D) It removes the need for cross-validation, since each draw is an independent estimate on its own

---

### 9. [Course 02 · Unit 5]
One trained logistic-regression model was scored on the same 171 held-out breast-tumour biopsies in Course 02; only the decision threshold changes:

```
    threshold   missed malignant   false alarms   accuracy
         0.10                  0             38     77.8%
         0.20                  1             21     87.1%
         0.30                  5             12     90.1%
         0.40                  7              9     90.6%
         0.50                 11              5     90.6%
         0.60                 13              4     90.1%
         0.70                 16              3     88.9%
         0.80                 20              0     88.3%
         0.90                 29              0     83.0%

   Best accuracy on this grid: 92.4% at threshold 0.44 — which still misses 8 malignant tumours.
```

A screening clinic can absorb at most 25 false alarms out of the 171, and within that limit wants to miss as few malignant tumours as it can. Which threshold does the table support, and at what cost?

A) 0.44 — it is the highest accuracy on the grid, 92.4%, and accuracy is the metric to maximise
B) 0.80 — it brings false alarms down to zero, and 88.3% accuracy is near the grid maximum
C) 0.50 — it is the library default, so it already balances the two kinds of error by construction
D) 0.20 — it misses 1 malignant tumour rather than 11, and its 21 false alarms fit the budget

---

### 10. [Course 01 · Unit 2]
Course 01 printed, for supervised learning, "Input: Features (X) and Labels (y)", and for unsupervised learning, "Input: Features (X) only"; it then fit `LinearRegression` and `LogisticRegression` on labelled data (R² 0.9287, accuracy 0.9500) and K-Means on unlabelled points (inertia 641.2076). What is the main difference between supervised and unsupervised learning?

A) Supervised learning is the faster of the two to train, which is the practical distinction
B) Supervised predicts numbers, unsupervised predicts categories
C) Supervised learning is fitted on labelled rows; unsupervised on features alone
D) Supervised learning uses neural networks, unsupervised learning uses clustering algorithms

---

**End of paper. Hand nothing in. Stay for the worked answers.**
