# Retrieval Quiz — Week 24

**Week 24 of 35 · Course 09 — AIAT 123 (Reinforcement Learning)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The cliff-walking comparison in Unit 2 (a 4x12 grid, -1 per step and -100 for the cliff; alpha = 0.5, gamma = 1.0, epsilon = 0.1, 500 episodes, one shared seed) ends with a row statistic for the two greedy paths:

```
Mean grid row walked - SARSA: 0.67 | Q-learning: 2.14
(row 3 is the cliff row, row 2 runs right along its edge, row 0 is the far safe side)
```

A colleague glances at the line and decides the agent walking at row 2.14 must be the cautious one. Which statement correctly explains the two row figures?

A) SARSA's greedy path is the one hugging the cliff edge, since an on-policy learner settles wherever its exploratory steps happened to lead it most often while it was training.  
B) The agent averaging row 0.67 scored lower in training, because its long detour pays extra -1 step penalties on each episode that the edge route avoids.  
C) With gamma = 1.0 the undiscounted max target inflates the cliff-edge tiles, so Q-learning's 2.14 reflects value overestimation rather than a route it would actually walk.  
D) Q-learning hugs the cliff edge because its max target values the greedy policy; SARSA keeps to the far side because its target also prices the 10% of steps that are random.  

---

### Question 2

Unit 2 contrasts Monte Carlo control with the TD methods that follow it. How does a Monte Carlo method estimate the value of a state?

A) By bootstrapping: it replaces the rest of the episode with its current estimate of the next state  
B) By averaging the actual returns observed from that state over complete episodes  
C) By sweeping the Bellman equation across the state space, using the environment's transition table  
D) By fitting a neural network to the visited states, since tables do not scale  

---

### Question 3

Unit 3's monitoring lesson trains a well-tuned tabular Q-learning agent on slippery `FrozenLake-v1` (cautious learning rate, exploration decaying) for 4000 episodes. Across two cells it prints:

```
Success rate, first 200 eps : 0.010
Success rate, last 500 eps  : 0.498
Smoothed curve range        : 0.000 to 0.590

Well-tuned run  : final rolling std = 0.500
```

A student's dashboard raises an alert whenever the 200-episode rolling standard deviation of episode reward climbs during training, and it fires on this run: the spread ends at 0.500, five times the 0.099 of the badly-tuned run trained in the same notebook. How should the alert be read?

A) The rise is a symptom of learning: with a 0/1 reward the spread is sqrt(p(1-p)), so it has to grow as the success rate climbs from 0.010 toward 0.498, and the greedy evaluation of 0.726 confirms it.  
B) The alert is justified: a spread of 0.500 on a reward that can be 0 or 1 means the agent is winning and losing almost at random, so the learning rate should be lowered until the spread settles back down again.  
C) The alert should be recomputed from the 1000 greedy evaluation episodes, where exploration is off; a training-time spread describes just the epsilon-greedy behaviour policy.  
D) The spread climbed because the 200-episode window is too short for a slippery environment; a 500-episode window would smooth the figure back down.  

---

### Question 4

Unit 4 then repeated the gradient measurement along an LSTM's memory lane and printed it beside the plain RNN:

```
distance k     plain RNN    LSTM b_f=1
        25      2.41e-15      1.84e-02
        50      7.33e-30      1.24e-04
```

At k = 50 the LSTM lane keeps about 2e+25 times more signal than the RNN, yet on the log plot its curve still slopes downward. Which conclusion does this table support?

A) The lane slows the exponential decay of the backward signal but does not stop it; attention removes the distance, putting two far-apart words one step apart  
B) Biasing the forget gate towards 1 has pushed the recurrent weights high enough for the gradient to explode instead — the mirror problem, which gradient clipping is there to handle  
C) A surviving signal of 1.24e-04 after 50 steps shows the long-range dependency is now learnable, so the vanishing gradient is a solved problem for LSTMs  
D) The LSTM's separate cell-state vector has room to store a 50-step sequence that the RNN's hidden state could not hold, which makes this a capacity fix  

---

### Question 5

The same Unit 4 probe scored *"The meeting is scheduled for Tuesday at 3pm"* **POSITIVE at 0.9301**, and the Arabic sentence glossed *"the meeting is Tuesday at 3"* at **P(POSITIVE) = 0.3695** after chopping it into **6.4** word-pieces per word. Same content, two very different scores — what explains the pair?

A) The model understood the English sentence as mildly positive and the Arabic one as close to neutral, so both numbers are fair readings of what the two sentences say  
B) The model is well calibrated: 0.9301 sits below the 0.9999 it gave a real opinion because a schedule is a weaker positive than praise  
C) The English fact had to leave through one of two exits, since there is no neutral class; the Arabic one was read letter by letter, so 0.3695 carries no information  
D) Both scores come from the lowercasing the `uncased` checkpoint applies; the `cased` checkpoint would read the capital letters and fix both  

---

### Question 6

In a Course 07 Unit 5 bias audit you build pairs of test sentences that are identical except for one demographic word — *he* / *she*, or a male / female name — and compare the model's output on each pair. What does that test measure?

A) How large the model's vocabulary is, since each name has to be a known token already  
B) Whether the output moves when the demographic attribute alone is changed and the rest is held fixed  
C) How accurate the model is on the group each name belongs to, measured against held-out labels for that group  
D) How stable the model is under paraphrase, since the two sentences carry the same meaning  

---

### Question 7

Unit 4's K-Means sweep over the 1,994 scaled communities prints, among its rows:

```
K=7: Inertia=2145.23, Silhouette=0.2970
K=9: Inertia=1824.09, Silhouette=0.3008
```

A colleague picks K = 9: "it beats K = 7 on silhouette *and* on inertia - for once both criteria agree, so the data has decided." The lesson's own elbow landed on K = 4, and the lesson clustered at K = 3. What is the right response?

A) The colleague is right: when the inertia criterion and the silhouette criterion point the same way, the data has chosen K and no judgement is needed  
B) K = 2 should stand: its silhouette of 0.3967 is the highest in the sweep, and the global peak outranks any comparison between neighbouring rows  
C) K = 4 should stand: the elbow was located geometrically, from the chord between the first and last points of the curve, which makes it a measurement rather than a judgement  
D) Inertia falls with each added cluster by construction, and a third-decimal silhouette bump is no ranking, so K is still settled by what the clusters are for  

---

### Question 8

Course 04 Unit 5 tunes hyperparameters with grid search and with random search on the same model. What does random search buy, and at what cost?

A) It walks the whole grid, so whichever setting in the grid is best gets evaluated  
B) It narrows the search around the best setting found so far, so later draws beat earlier ones  
C) It draws a set number of settings at random, so you fix the budget rather than the grid  
D) It removes the need for cross-validation, since each draw is an independent estimate on its own  

---

### Question 9

Unit 5's threshold sweep — one logistic-regression model, its probability cut-off moved while nothing else changed, evaluated on 171 held-out biopsies — printed these rows (the four cut-offs above 0.50 miss 13 or more):

```
    threshold   missed malignant   false alarms   accuracy
         0.10                  0             38     77.8%
         0.20                  1             21     87.1%
         0.30                  5             12     90.1%
         0.40                  7              9     90.6%
         0.50                 11              5     90.6%

   Best accuracy on this grid: 92.4% at threshold 0.44 — which still misses 8 malignant tumours.
```

A regional programme builds its rule around the dangerous error instead: it will tolerate at most 5 missed malignant tumours among these 171, and inside that cap it wants the fewest false alarms it can get. Which row meets the rule at the lowest false-alarm count, and what is traded away to get there?

A) 0.10 — the one row that misses no malignant tumours, and a programme that fears misses should begin from zero of them and then work its way up  
B) 0.30 — the highest cut-off whose misses stay within 5, bringing false alarms down to 12 at the price of 5 missed tumours rather than 1  
C) 0.20 — it misses 1 and raises 21 false alarms, which satisfies the rule with a comfortable margin on the missed-tumour side  
D) 0.44 — the grid's best accuracy at 92.4%, and 8 misses is near enough to the rule for a figure the notebook itself singled out  

---

### Question 10

Unit 2 ran K-Means on 150 iris flowers with the species column hidden. The crosstab printed afterwards showed cluster 1 holding 50 setosa flowers and 0 of either other species. A classmate says: "a match that clean means K-Means obviously trained on the species labels." Which statement correctly describes what the clustering run was given?

A) It received the 4 measurements plus the species column, which is why cluster 1 lines up with setosa so exactly  
B) It received the measurements and predicted a species category for each flower, so it was a classification model like the biopsy one  
C) It received the 4 measurements per flower; the species column stayed hidden and was brought back afterwards to score the clusters  
D) It received the measurements and the labels but ignored them to finish faster, because fits without labels take fewer passes  

---
