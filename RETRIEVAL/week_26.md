# Retrieval Quiz — Week 26

**Week 26 of 35 · Course 09 — AIAT 123 (Reinforcement Learning)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Unit 5's comparison notebook runs Dyna-style planning (20 replayed transitions after each real step) against plain Q-learning on `FrozenLake-v1`, averaged over **20 seeds × 300 episodes** with epsilon = 0.2 for both. It summarises its own table in two lines:

```
- EARLY: the model-based agent is ahead by +0.312 success rate over the first
  50 episodes. Same number of environment steps, more learning squeezed out of them.
- LATE: the gap has closed to -0.001. Both reach roughly the same level.
```

and adds that the planning agent performed about **20x more Q-updates** for the same environment experience. A team is choosing an agent for a warehouse robot: each real step costs time and wear, while a desktop CPU sits idle between steps. Which recommendation follows from those two gaps?

A) Choose the model-free agent: the -0.001 late gap shows both end level, so the 20x extra Q-updates are compute spent for no advantage that survives to the end of the 300 episodes.  
B) Choose the planning agent because the +0.312 gap shows it extracted 20x more environment experience from the same 300 episodes, which is exactly what a costly robot needs.  
C) Choose the planning agent: the +0.312 early gap means it reaches a usable success rate on far fewer costly real steps, and the -0.001 late gap says no final performance is lost.  
D) Run both past 300 episodes before deciding; a -0.001 gap averaged over 20 seeds is too narrow to show which agent would end higher, and that is what the choice turns on.  

---

### Question 2

Unit 4 compares four exploration rules on the same 5-variant A/B test. On what basis does **Upper Confidence Bound** pick its next action?

A) The estimated value of each action plus a bonus that grows the less often the action has been tried  
B) The estimated value of each action, with ties broken by whichever action was tried least recently in the run  
C) A sample drawn from a posterior distribution over each action's reward, taken fresh each round  
D) A probability proportional to exp(Q/tau), so higher-valued actions are picked more often  

---

### Question 3

Unit 3's monitoring lesson sabotages one FrozenLake agent by setting `eps_decay = 1.0` and `eps_min = 0.50`; that agent ends at a 0.040 greedy success rate against the well-tuned agent's 0.726. What does an epsilon **decay** schedule do?

A) It lowers the learning rate as training proceeds, so late updates disturb the table less than early ones  
B) It shrinks the exploration rate over training, so the agent explores early and commits later  
C) It reduces the discount factor over training, so the agent stops valuing distant rewards  
D) It drops the oldest transitions from the replay buffer, so stale experience is not replayed  

---

### Question 4

The lesson trains three recurrent layers of width 64 on the same `Embedding(2000, 64)`, the same **2,000** training reviews, the same **12** epochs and the same seed. Best validation accuracy: `GRU` **0.720** (final 0.692), `SimpleRNN` **0.544** (final 0.520). A classmate says the GRU beats the gateless layer for the same reason an LSTM does. Which reason is that?

A) It takes in the 100 padded positions at once rather than one word at a time, so the opening words are not overwritten by the ones that come later  
B) It carries fewer recurrent weights than the SimpleRNN's 8,256 — so with 2,000 reviews there is less for it to overfit  
C) Its gates make each step a controlled, trainable update of the state, so a gradient can reach earlier words along a near-additive path  
D) It runs over each review forwards and then backwards, so the words from the start are the freshest when the verdict is made  

---

### Question 5

For the first review in the IMDB test split (**68** real tokens), the lesson prints: one attention row sums to **1.000** over the real tokens; uniform attention would give each token **0.0147**; the most-attended word, `terrible`, receives **0.0156** (**1.06×** uniform); and the model's P(positive) for the review is **0.012**. In the `MultiHeadAttention` layer's returned scores, what are the entries of that row?

A) The probability the model assigns to each of the 68 words as the next token, which is why the row sums to 1.000  
B) A learned code for where each of the 68 tokens sits, which the layer uses in place of a separate positional embedding  
C) Per-word contributions to P(positive) = 0.012, so the 0.0156 on `terrible` is the layer's stated reason for the negative verdict on this review  
D) Weights for one query position: the coefficients that average the 68 value vectors `V` into that position's output vector  

---

### Question 6

After setting `requires_grad = False` on the MobileNetV2 base and attaching `Dropout(0.2)` + `Linear(1280, 10)`, the lesson prints **Frozen (reused): 2,223,872 parameters = 99.43%**. Training on **2,000** resized MNIST digits, the head reports train accuracy **0.569** after epoch 1 and **0.843** after epoch 2, then scores **0.854** on the **500** held-out images. Which reading of this run is correct?

A) The 99.43% already encodes digits well enough that the two epochs mostly confirm what the model could do before any training  
B) The 99.43% stays as ImageNet learned it; the climb from 0.569 to 0.843 is the fresh head learning what the ten digit classes look like  
C) With 99.43% frozen there is too little capacity left to memorise 2,000 images, so the 500-image hold-out is a formality  
D) A base frozen to 99.43% pays off once the new dataset is at least ImageNet-sized; at 2,000 digits the whole network should be unfrozen and retrained  

---

### Question 7

Course 01's knowledge base stores each rule as `{'if': condition, 'then': conclusion}` and adds one with `add_rule("has feathers", "is a bird")`. What is that IF-THEN construct?

A) A production rule: a condition on the facts, plus the conclusion to add when it holds  
B) A loop that repeats the test over the fact base until the fact base stops changing  
C) An indexing structure that lets the engine look a feature up without scanning the facts  
D) A search procedure that expands the fact base outward from the start node  

---

### Question 8

Course 05's introduction to machine learning holds out a test split before reporting any score. A model returns 0.99 accuracy on the rows it was trained on and 0.71 on the held-out rows. What is that pattern called, and what does it mean?

A) Underfitting — the model is too simple to capture the structure that is in the training rows  
B) Data leakage — test rows were present during training, which is what lifts the training figure  
C) Class imbalance — one class dominates, so accuracy is high on it and low on the smaller one  
D) Overfitting — the model learned detail specific to the training rows that does not carry over  

---

### Question 9

The Unit 1 search notebook also printed the order in which A\* popped nodes on the same graph, with the `f = g + h` each one carried:

```
   #1  A   f=6  (g=0 + h=6)
   #2  C   f=5  (g=1 + h=4)
   #3  F   f=3  (g=2 + h=1)
   #4  B   f=6  (g=1 + h=5)
   #5  E   f=4  (g=2 + h=2)
   #6  G   f=3  (g=3 + h=0)
```

Its admissibility check also reported `C: h=4, h*=unreachable` and `F: h=1, h*=unreachable` — the branch A\* tried first cannot reach the goal at all, so two of the six expansions went to a dead end before the search came back to `B`. A student concludes: *"that wasted detour is what shows the heuristic is inadmissible."* How should the detour be read?

A) The detour is the evidence: an admissible heuristic steers A* straight toward the goal, so expanding a dead end means h must have overestimated somewhere  
B) The detour shows h behaved admissibly: C was popped at f=5 ahead of B at f=6, which is just the lowest-f-first order the optimality proof relies on  
C) The detour is beside the point because C and F have h*=unreachable, which makes h <= h* hold on that branch and settles the question in h's favour  
D) The detour is not the evidence; h is inadmissible because the node-by-node check finds h above h* at A, B and E, whichever route the search took first  

---

### Question 10

The Unit 3 diagnosis system was loaded with these printed symptom probabilities, among others:

```
  ➕ P(Fever|Flu) = 90.00%
  ➕ P(Cough|Flu) = 80.00%
  ➕ P(Fatigue|Flu) = 70.00%
  ➕ P(Fever|COVID-19) = 85.00%
  ➕ P(Cough|COVID-19) = 90.00%
  ➕ P(Fatigue|COVID-19) = 60.00%
```

For the patient with fever, cough and fatigue it printed `Flu: 58.91%` and `COVID-19: 21.46%`. Its slope-chart table shows the two likelihoods nearly tied — `P(symptoms|d)` of 50.4% for Flu against 45.9% for COVID-19 — with normalised priors of 22.7% and 9.1%. COVID-19 explains this patient almost as well as Flu does. Why does it end up with far less than half of Flu's posterior?

A) With the likelihoods this close, the prior decides: Flu's normalised prior of 22.7% is more than twice COVID-19's 9.1%, and Bayes multiplies the two  
B) COVID-19's 2.0% prevalence is renormalised up to 9.1% over three diseases, and that renormalisation step is what costs it the ranking against Flu  
C) The likelihood gap does it: COVID-19's fatigue figure of 60.00% is the weakest entry, and 45.9% against 50.4% is what pulls its posterior down to 21.46%  
D) Normalising the three posteriors to sum to 100% hands the leader a share of the others' mass, which is what widens a near-tie into 58.91% against 21.46%  

---
