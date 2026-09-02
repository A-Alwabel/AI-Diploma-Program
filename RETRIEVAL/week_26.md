# Cumulative Retrieval Quiz — Week 26

**Programme week 26 of 35 · Current course: Course 09 — AIAT 123 (Reinforcement Learning), Unit 4 / Unit 5**
**Placement: session 2 of the week (s102), in the closing block. Session 4 (s104) is the course wrap and session 3 (s103) closes Unit 5 with its unit quiz, so the block moves back to s102.**

- **15 minutes**, taken **in class at the END of the session**. Not homework.
- **Not graded.** No mark from this paper reaches your course grade.
- Write your answers, then your instructor **works every correct answer aloud immediately afterwards**. Stay for it.
- Ten items. Three from what you are studying now, seven from courses you finished earlier. The earlier items carry their own context.

---

### 1. [Course 09 · Unit 5]
Unit 5's model-based vs model-free lesson runs both agents on `FrozenLake-v1` over **20 seeds x 300 episodes**, with the same learning rule, the same discount and the same epsilon = 0.2. The one difference: after each real environment step the model-based agent also replays 20 remembered transitions. It prints:

```
  Success rate after ...   | model-free | model-based
  -------------------------|------------|------------
  50 episodes              |      0.020 |      0.332
  100 episodes             |      0.217 |      0.584
  the last 50 episodes     |      0.747 |      0.746
```

and notes that the model-based agent did about **20x more Q-updates** for the same environment experience. What do these numbers support?

A) The model-based agent had 20x more experience of the environment, so its early lead at 50 and 100 episodes is what you would expect.
B) The model-based agent is the better choice whenever compute is the scarce resource, because it extracts more learning per unit of computation.
C) The model-based agent is more sample-efficient — it reaches a given success rate in fewer environment steps — but it does not end higher.
D) The 300-episode budget is too short to separate the two: with more episodes the model-based agent's early lead would reappear as a higher final rate.

---

### 2. [Course 09 · Unit 4]
Unit 4 compares four exploration rules on the same 5-variant A/B test. On what basis does **Upper Confidence Bound** pick its next action?

A) The estimated value of each action plus a bonus that grows the less often the action has been tried
B) The estimated value of each action, with ties broken by whichever action was tried least recently in the run
C) A sample drawn from a posterior distribution over each action's reward, taken fresh each round
D) A probability proportional to exp(Q/tau), so higher-valued actions are picked more often

---

### 3. [Course 09 · Unit 3 / Unit 4]
Unit 3's monitoring lesson sabotages one FrozenLake agent by setting `eps_decay = 1.0` and `eps_min = 0.50`; that agent ends at a 0.040 greedy success rate against the well-tuned agent's 0.726. What does an epsilon **decay** schedule do?

A) It lowers the learning rate as training proceeds, so late updates disturb the table less than early ones
B) It shrinks the exploration rate over training, so the agent explores early and commits later
C) It reduces the discount factor over training, so the agent stops valuing distant rewards
D) It drops the oldest transitions from the replay buffer, so stale experience is not replayed

---

### 4. [Course 08 · Unit 3]
On IMDB reviews padded to 100 tokens, a `SimpleRNN` reaches **0.544** best validation accuracy and an **LSTM** of the same width reaches **0.776**. Where does the LSTM's advantage come from?

A) Its gates and cell state add a path along which the gradient can be carried back many steps
B) It reads all 100 tokens in parallel instead of one at a time, so early words are not forgotten
C) It has fewer parameters than a `SimpleRNN` of the same width, so it needs less data to train
D) It reads each review backwards as well as forwards, so early words are seen last

---

### 5. [Course 08 · Unit 3]
Scaled dot-product self-attention computes `Attention(Q, K, V) = softmax(QKᵀ / √d_k) V`. What does the **softmax term** produce?

A) A probability distribution over the vocabulary, giving the model's next predicted token
B) The position of each token, which is why no positional encoding is needed
C) One weight per position, used to take a weighted average of the value vectors `V`
D) The model's confidence that its prediction is correct, which is why attention maps can be read as explanations

---

### 6. [Course 08 · Unit 2]
You load a pre-trained MobileNetV2, **freeze** the base, and attach a new 10-class head: **12,810 of 2,236,682 parameters (0.57%)** are trainable. You have 2,000 labelled images. Which statement about this setup is correct?

A) Because the base is frozen, no training is needed — the model can be used as it is
B) The frozen layers keep their ImageNet features; the new head is what learns your 10 classes
C) Freezing the base means the model can no longer overfit your 2,000 images
D) A frozen backbone pays off once the new dataset is at least as large as the one it was pre-trained on

---

### 7. [Course 05 · Unit 3]
A colleague's bar chart of 2018 quarterly 911 call volume shows Q2 as a collapse and Q4 as a full recovery. The counts behind it are Q1 1,478, Q2 1,352, Q3 1,402, Q4 1,478 — a change of **+0.00%** across the year. No number was altered between the data and the chart. What produced the misleading chart, and what is the fix?

A) The y-axis was truncated to start just below the smallest bar; start it at zero, or flag the zoom
B) The bars were sorted by value rather than by quarter; re-order them chronologically so the trend reads correctly
C) Counts were plotted where percentages were needed; convert each quarter to a percentage change from Q1
D) Four categories are too few for bars; a pie chart would show the quarters' shares more fairly

---

### 8. [Course 05 · Unit 4]
Course 05's introduction to machine learning holds out a test split before reporting any score. A model returns 0.99 accuracy on the rows it was trained on and 0.71 on the held-out rows. What is that pattern called, and what does it mean?

A) Underfitting — the model is too simple to capture the structure that is in the training rows
B) Data leakage — test rows were present during training, which is what lifts the training figure
C) Class imbalance — one class dominates, so accuracy is high on it and low on the smaller one
D) Overfitting — the model learned detail specific to the training rows that does not carry over

---

### 9. [Course 02 · Unit 1]
Course 02 Unit 1 ran A\* with the heuristic `h(n) = |ord(n) - ord(goal)|` and checked it against the true remaining cost `h*`:

```
   A: h=6, h*=3  ->  OVERESTIMATES by 3
   B: h=5, h*=2  ->  OVERESTIMATES by 3
   E: h=2, h*=1  ->  OVERESTIMATES by 1
   G: h=0, h*=0  ->  OK
```

A\* then returned `A -> B -> E -> G`, which is the shortest path on that graph, having opened 6 of the 7 nodes (BFS opened 7). What does this run establish about the heuristic?

A) h is admissible, because the path A\* returned is in fact the shortest one on this graph
B) The overestimates are uniform across nodes, so they cancel and the guarantee holds
C) h is inadmissible, and that is what made A\* open 6 nodes where BFS had to open 7
D) h overestimates, so the guarantee did not apply — the shortest path came back anyway

---

### 10. [Course 02 · Unit 3]
Course 02's Unit 3 diagnosis system was given a patient with fever, cough and fatigue, and printed:

```
disease         prevalence  prior (norm.)  P(symptoms|d)   posterior   rank move
Common Cold         15.0%          68.2%           5.6%       19.6%       1 → 3
Flu                  5.0%          22.7%          50.4%       58.9%       2 → 1
COVID-19             2.0%           9.1%          45.9%       21.5%       3 → 2
```

Common Cold is by far the most prevalent of the three diseases, yet it finishes last. Why?

A) Renormalising the three prevalences over one another pushes the largest of them below the rest
B) Common Cold has no listed probability for fatigue, so the system skips it in the product
C) Bayes multiplies prior by likelihood, and P(symptoms | Cold) = 5.6% is nine times below Flu's
D) The posterior follows the highest single symptom probability, and Flu's fever figure is 90%

---

**End of paper. Hand nothing in. Stay for the worked answers.**
