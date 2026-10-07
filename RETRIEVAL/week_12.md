# Retrieval Quiz — Week 12

**Week 12 of 35 · Course 04 — AIAT 114 (Machine Learning Algorithms and Applications)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

In gradient boosting (XGBoost, LightGBM), what does the learning_rate hyperparameter control?

A) How many of the available features each individual tree in the ensemble is allowed to look at when it splits  
B) How much each newly added tree contributes to the ensemble's running prediction, round by round  
C) How many CPU cores the library is allowed to use while it fits the trees in the ensemble  
D) The proportion of the data held back for the test split before the boosting rounds begin  

---

### Question 2

A random forest and a gradient-boosted ensemble both combine many decision trees. What separates the way they are built?

A) Bagging is used for regression targets and boosting for classification targets  
B) Bagging averages trees of the same depth, while boosting averages trees of increasing depth  
C) Boosting fits its trees independently in parallel, while bagging fits each one after the last has finished  
D) Bagging fits its trees in parallel; boosting fits each tree to correct what the previous ones got wrong  

---

### Question 3

Course 04 Unit 5 tuned the same model with grid search and with random search. What is random search's main advantage over an exhaustive grid?

A) It reaches a higher test score than grid search on the same budget of fits  
B) It removes the need for cross-validation, since each draw is already independent  
C) It samples the space instead of enumerating it, so a good setting often turns up in fewer fits  
D) It settles on the best combination in the grid, and does so without repeating a combination twice  

---

### Question 4

The statistical-measures lesson evaluates a linear model on held-out diabetes patients and prints MSE 2900.19, then notes in 'Where this breaks' that RMSE exceeds MAE by about 26%. Its diagnostic panel adds that 30 of the 89 patients are missed by more than 53.9 and that the worst single prediction is off by 154. A teammate proposes reporting MAE on its own because it 'looks better'. What does the 26% gap, read together with those two counts, tell you?

A) Errors are unevenly spread: a minority of badly missed patients pulls RMSE up, so MAE alone would understate the worst cases  
B) The model over-predicts by about a quarter on average, since RMSE exceeding MAE by 26% measures the direction of the typical miss  
C) RMSE has to be squared back to MSE 2900.19 before it can be set against MAE, because the 26% gap compares unlike units  
D) The 154 miss is one outlier; remove that patient and RMSE would fall back to MAE, because the whole gap comes from a single record  

---

### Question 5

The PCA lesson's first cell prints the explained-variance ratios of the top three components of the standardized 569-biopsy data as 44.3%, 19.0% and 9.4%, and adds that keeping 80% of the variance needs 5 of the 30 components while keeping 95% needs 10. Its cross-validation figure then reports that the classifier's accuracy climbs from 91.2% at k = 1 to 97.4% by k = 5, dips at k = 3, and from k = 5 to k = 30 stays inside a band 0.7 percentage points tall, with its best point at k = 10 (98.07%) just above the 97.89% of the 30 raw features. A colleague applies the rule 'keep 95% of the variance' and so picks k = 10. Which assessment of that rule do the printed figures support?

A) It is the right rule because accuracy rises with variance kept, which is why the k that reaches 95% of the variance is also the k that scores highest  
B) It reached a good k for the wrong reason: the plateau from k = 5 shows the accuracy had flattened long before the variance reached its 95% line  
C) It is too generous: the dip at k = 3 shows the third component's 9.4% of variance is harming the classifier, so k should stop at 2  
D) It is too strict: a reduced model can at best match the 30 raw features, so the 5 components that already keep 80% of the variance are the honest ceiling  

---

### Question 6

From the same sample of 100 recorded Titanic ages, the confidence-interval lesson prints a 90% interval of [27.3582, 32.2468] (width 4.8886) and a 99% interval of [25.9361, 33.6689] (width 7.7327). When it redoes the whole study 2000 times, 92.5% of the 90% intervals and 99.6% of the 99% intervals capture the population mean, and in the panel that draws 100 of those repeats, 3 intervals are shown in crimson. A student writes: 'There is a 99% chance the true mean age is between 25.9361 and 33.6689.' Which statement about that sentence is right?

A) Acceptable: 99.6% of the 2000 repeated intervals held the mean, so roughly 99% is also the right probability for this one  
B) Wrong: the level counts recorded ages, so the sentence should say that 99% of the 714 ages lie between 25.9361 and 33.6689  
C) Acceptable, and understated: the wider 99% interval (7.7327 against 4.8886) carries more knowledge about the mean, which is why its coverage rose to 99.6%  
D) Wrong: the 99% is the capture rate of the procedure across repeats — measured here as 99.6% — not the odds for this one interval  

---

### Question 7

Course 01 used Bayes' theorem on a medical test whose positive result still left the patient probably healthy. What is Bayesian probability used for in AI?

A) Handling uncertainty and drawing probabilistic inferences from evidence  
B) Confirming a diagnosis whenever a test result comes back positive  
C) Computing the prior probability of a hypothesis before evidence is observed  
D) Removing uncertainty so predictions become deterministic  

---

### Question 8

In Course 01 you built a small knowledge graph over family relations and queried it. What is a knowledge graph?

A) A neural network whose neurons are arranged as nodes and edges rather than as layers  
B) A search algorithm that walks a graph outward from a start node until it first meets a goal node  
C) A structure that stores entities as nodes and the relations between them as labelled edges  
D) An activation function applied over a graph of inputs to produce one scalar output  

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
B) The detour is not the evidence; h is inadmissible because the node-by-node check finds h above h* at A, B and E, whichever route the search took first  
C) The detour shows h behaved admissibly: C was popped at f=5 ahead of B at f=6, which is just the lowest-f-first order the optimality proof relies on  
D) The detour is beside the point because C and F have h*=unreachable, which makes h <= h* hold on that branch and settles the question in h's favour  

---

### Question 10

In the Unit 2 expert-system cell, three recorded observations about `Patient1` and two rules went in, and the run printed:

```
   BEFORE Forward Chaining:
      Facts: 3

  ➕ Added: Fact(Patient1, likely_has, Flu)
   ✅ Applied rule: Flu Diagnosis Rule
  ➕ Added: Fact(Patient1, recommend, Rest)
   ✅ Applied rule: Flu Treatment Rule

✅ Forward chaining complete! (2 iterations)
   (Stopped because no more new facts can be derived)

   AFTER Forward Chaining:
      Facts: 5
```

A clinic now wants the system to run with no particular question in mind: *each time a nurse records a new observation, surface whatever recommendations now follow for that patient.* Which chaining direction suits that job, and what in the printout shows why?

A) Forward chaining: the Flu Diagnosis Rule was entered before the Flu Treatment Rule, and firing rules in the order they were written is what keeps the chain valid  
B) Backward chaining: it would prove `recommend Rest` for one patient at a time, and a focused proof costs less than deriving facts even when no goal has been named  
C) Forward chaining: data-driven, firing whichever rules the recorded facts satisfy until a pass adds no new fact — the loop that stopped above after 2 iterations  
D) Backward chaining: if a later observation contradicts `likely_has Flu`, it can take back the `Rest` recommendation, which a forward chainer has no way to do  

---
