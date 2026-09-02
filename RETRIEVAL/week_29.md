# Cumulative Retrieval Quiz — Week 29

**Programme week 29 of 35 · Course 10 — AIAT 124 (Generative AI) closing, and Course 11 — AIAT 125
(AI Model Deployment) opening.**
**Taken in session 115, in the final 15 minutes.**

---

**How this works**

- **15 minutes, in class, at the END of the session.** 7 minutes to answer, then 8 minutes in which
  your instructor works the correct answers aloud. The worked correction is the part that makes this
  worth doing.
- **Not graded.** No mark from this paper reaches your course grade.
- **Ten items.** Three on this week and last week, three on material from about a month ago, four
  from earlier in the programme. Everything here has already been taught.
- Write the **letter only**. Closed book. One best answer per item.

---

## Part A — This week and last week (Courses 10 and 11)

### Item 1
A product team must generate a million catalogue images a day at interactive latency on a fixed GPU
budget. The diffusion model you built needs roughly **200 sequential network passes per image**; a
GAN needs **one**. Which trade-off should drive the family choice?

A) Diffusion — its sample quality is higher, and its sampling cost falls as the model is trained longer, so throughput improves with training.
B) A VAE — its encoder makes generation a single pass, and its reconstruction loss is what guarantees sharp catalogue images.
C) A GAN generates in one forward pass, so it is the throughput answer; diffusion buys quality at a cost that scales with the step count.
D) The choice is immaterial at this scale: latency is set by output resolution and batch size, not by which generator family you pick.

---

### Item 2
A team removes the protected attribute from its training data and reports that the model is now
fair. Unit 4 ran exactly that experiment: dropping `Sex` cut the predicted-rate gap from **81.9% to
13.4%**, cost **9.7 points of accuracy**, and `Sex` was still predictable from the remaining
features at **66.0%** against a **63.8%** majority-class baseline. What is the correct conclusion?

A) Removing the column removed the ability to audit, not the ability to discriminate — the attribute survives in correlated features.
B) Fairness through unawareness worked here: a residual gap of 13.4% is small enough to report the model to the client as unbiased.
C) The gap fell because accuracy fell: a model that predicts one class for everyone shows no gap at all, and has no value either.
D) The result transfers: a mitigation of this kind leaves a residual gap of roughly this size, so about 13% is the floor a team should expect.

---

### Item 3
Course 11 opened this week by separating training from shipping. What is **model deployment**?

A) Saving the trained model to a file so that it can be reloaded later
B) Measuring the model's accuracy on a held-out test set
C) Retraining the model on the full dataset before release
D) Making a trained model reachable by users or other services

---

## Part B — About a month ago (Course 09, Reinforcement Learning)

### Item 4
Unit 3 trained two tabular Q-learning agents on slippery FrozenLake — same algorithm, same
environment, different hyperparameters — and printed:

```
Well-tuned run  : final rolling std = 0.500 | final rolling mean = 0.495
Badly-tuned run : final rolling std = 0.099 | final rolling mean = 0.010

Greedy evaluation on 1000 fresh episodes:
  Well-tuned agent  : 0.726 success rate
  Badly-tuned agent : 0.040 success rate
```

A dashboard that plots only the rolling standard deviation flags the **badly-tuned** run as the more
stable of the two. What is the error?

A) The two standard deviations were computed over different rolling window lengths, so the two figures are not on a comparable scale.
B) With a 0/1 reward the spread is mechanically tied to the mean, so a run stuck at 0.010 has almost no spread; 0.099 signals failure.
C) Rolling standard deviation describes the exploring behaviour policy, so both runs would show the same spread once exploration is switched off.
D) The well-tuned run's 0.500 is an artefact of its greedy evaluation at 0.726; the training std should be recomputed from the evaluation episodes.

---

### Item 5
Unit 4 ran epsilon-greedy on the same 5-variant A/B test at four values of epsilon, **50 runs of
2000 rounds each**:

```
   ε    |  mean ± std    |  min … max across runs
  0.01  |  489.0 ± 120.3 |  292 … 704
  0.05  |  599.6 ±  76.2 |  314 … 697
  0.1   |  623.7 ±  50.1 |  475 … 691
  0.3   |  610.8 ±  35.7 |  508 … 673
Best epsilon by MEAN total reward: ε = 0.1
27 of 50 single runs would have crowned a DIFFERENT epsilon than the 50-run average does.
```

A student reports: *"epsilon = 0.01 is the best setting — I ran it once and scored 704, the highest
total anywhere in this table."* What is the strongest objection?

A) 704 is one draw from the widest-spread row (±120.3 on a mean of 489.0), and 27 of 50 single runs disagree with the average.
B) Total reward is the wrong statistic for ranking exploration rates; cumulative regret is what orders these four settings correctly.
C) 704 is impossible for ε = 0.01, whose mean is 489.0; a single run does not exceed its own mean by more than one standard deviation.
D) ε = 0.01 explores too little for its runs to be compared with the others, so drop that row.

---

### Item 6
Unit 2 estimated state values two ways on the same environment: one method waited until an episode
ended, the other updated after every step. How does the **Monte Carlo** method estimate a state's
value?

A) By bootstrapping: it updates each estimate toward the reward plus the discounted value of the next state
B) By sweeping the whole state space with the Bellman equation, using a known transition model
C) By averaging the returns actually observed from complete episodes that passed through the state
D) By fitting a neural network to the observed rewards and reading its prediction for that state

---

## Part C — Earlier in the programme

### Item 7 — Course 03, Mathematics and Probability for ML
Unit 5 drew a sample of n = 100 from the 714 recorded Titanic passenger ages and printed a 95%
confidence interval of **[26.8815, 32.7235]** for the mean age. Repeating the whole study 2000
times, **96.4%** of the intervals built this way contained the true population mean of **29.6991**.
Which statement do these results support?

A) There is a 95% probability that the true mean age of the 714 recorded passengers lies inside [26.88, 32.72].
B) About 95% of the 714 recorded passenger ages fall inside [26.88, 32.72], which is the quantity the level counts.
C) Raising the level to 99% would narrow the interval, because greater confidence pins the true mean down more tightly.
D) The 95% is a hit rate of the procedure across repeated studies, not a probability attached to this one interval.

---

### Item 8 — Course 01, Introduction to AI and Applications
Unit 2 computed the probability of a disease given a positive test from the prior, the sensitivity
and the false-positive rate. What role does Bayesian probability play in an AI system?

A) It updates a belief as evidence arrives, and reports the result as a probability
B) It removes uncertainty from the model, so that its predictions become deterministic
C) It guarantees a correct diagnosis whenever the test result comes back positive
D) It computes the probability of a hypothesis before evidence has been observed

---

### Item 9 — Course 05, Scalable Data Science
A colleague's bar chart of 2018 quarterly 911-call volume shows Q2 as a collapse and Q4 as a full
recovery. The counts behind it are **Q1 1,478, Q2 1,352, Q3 1,402, Q4 1,478** — a change of
**+0.00%** across the year, and no number was altered between the data and the chart. What produced
the misleading chart, and what is the fix?

A) The bars were sorted by value rather than by quarter; re-order them chronologically so the trend reads correctly.
B) Counts were plotted where percentages were needed; convert each quarter to a percentage change from Q1.
C) The y-axis was truncated to start just below the smallest bar; start it at zero, or flag the zoom.
D) Four categories are too few for bars; a pie chart would show the quarters' shares more fairly.

---

### Item 10 — Course 08, Deep Learning
A team replaced a logistic-regression classifier with a two-layer neural network on the **same raw
pixels** and the **same 10,000 test images**. Test accuracy rose from **0.8879 to 0.9130** — 1,121
wrong images down to 870. Which statement best explains the advantage the network has here?

A) It needs fewer labelled training images, because its hidden layers share information between the classes.
B) It learns hierarchical features from the raw pixels instead of using each pixel as a fixed feature.
C) It is guaranteed to reach the global minimum of its loss, which logistic regression is not.
D) It removes the need to scale or normalise the inputs before training.

---

**End of quiz — put your pen down and follow the worked answers.**
