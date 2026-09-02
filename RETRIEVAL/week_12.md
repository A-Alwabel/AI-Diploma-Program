# Cumulative Retrieval Quiz - Week 12

**Programme week 12 of 35 | Course 04 - AIAT 114 (Machine Learning Algorithms and Applications)**

Taught this week: Unit 5 (model selection and boosting, sessions 45-47); session 48 is the course wrap.

---

## How this works

- **15 minutes, in class, at the END of session 46.** You answer for about 7 minutes; your instructor then works the correct answers aloud for about 8.
- **This is not graded.** No mark from this paper reaches your course grade, and it carries no weight in any of the six assessment lines.
- **The correct answers are worked immediately afterwards, in the room.** That worked correction is the part that does the teaching; a quiz that only returns a score is worth about a third less.
- Ten questions. Three are on material from this week or last, three on material from about a month ago, and four on material from earlier in the programme. Each earlier question carries the context it needs, so you are not being asked to recall a lesson cold.
- Write one letter per question. No calculator, no laptop, no notes - answering from memory is the whole point.

---

### Question 1
*taught this week or last | Course 04, Unit 5*

In gradient boosting (XGBoost, LightGBM), what does the learning_rate hyperparameter control?

A) How many of the available features each individual tree in the ensemble is allowed to look at when it splits  
B) How much each newly added tree contributes to the ensemble's running prediction, round by round  
C) How many CPU cores the library is allowed to use while it fits the trees in the ensemble  
D) The proportion of the data held back for the test split before the boosting rounds begin  

---

### Question 2
*taught this week or last | Course 04, Unit 5*

A random forest and a gradient-boosted ensemble both combine many decision trees. What separates the way they are built?

A) Bagging is used for regression targets and boosting for classification targets  
B) Bagging averages trees of the same depth, while boosting averages trees of increasing depth  
C) Boosting fits its trees independently in parallel, while bagging fits each one after the last has finished  
D) Bagging fits its trees in parallel; boosting fits each tree to correct what the previous ones got wrong  

---

### Question 3
*taught this week or last | Course 04, Unit 5*

Course 04 Unit 5 tuned the same model with grid search and with random search. What is random search's main advantage over an exhaustive grid?

A) It reaches a higher test score than grid search on the same budget of fits  
B) It removes the need for cross-validation, since each draw is already independent  
C) It samples the space instead of enumerating it, so a good setting often turns up in fewer fits  
D) It settles on the best combination in the grid, and does so without repeating a combination twice  

---

### Question 4
*taught about a month ago | Course 03, Unit 3*

On 89 held-out diabetes patients, Course 03 printed MAE 42.79, RMSE 53.85, and a mean signed error of -3.91, and reported that the 10 worst-predicted patients carry 44.3% of the total squared error. What does the gap between MAE and RMSE tell you about this model?

A) The model over-predicts by roughly 11 units on each patient, which is what the gap between the two metrics measures  
B) The model accounts for 53.85% of the variation in the targets, which is the quantity a root-mean-squared error reports  
C) RMSE and MAE are on different scales, so RMSE has to be squared before the two numbers can be compared  
D) A small group of large errors inflates RMSE, so the typical patient is missed by about 43 rather than 54  

---

### Question 5
*taught about a month ago | Course 03, Unit 4*

Course 03 ran the same classifier on the 569-biopsy breast-cancer data, changing only how many principal components it may see, scoring every row with the same 5-fold cross-validation:

```
components   variance kept   5-fold accuracy
    1            44.3%           0.9121
    2            63.2%           0.9578
    3            72.6%           0.9491
    5            84.7%           0.9736
   10            95.2%           0.9807
   30           100.0%           0.9789
```

The same classifier on all 30 raw features, with no PCA at all, scores 0.9789. Which conclusion do these numbers support?

A) Each component adds accuracy in proportion to the variance it carries, so keeping all 30 components is the best choice  
B) Accuracy flattens long before variance does - k = 5 already reaches 0.9736 while keeping only 84.7% of the variance  
C) PCA hurt this classifier: the reduced models score below the 0.9789 that the 30 raw features reach on their own  
D) The dip at k = 3 shows the third component carries no variance, so it should be dropped from the model  

---

### Question 6
*taught about a month ago | Course 03, Unit 5*

Course 03 drew a sample of n = 100 from the 714 recorded Titanic passenger ages and printed a 95% confidence interval of [26.8815, 32.7235] for the mean age. Repeating the whole study 2000 times, 96.4% of the intervals built this way contained the true population mean of 29.6991. Which statement do these results support?

A) There is a 95% probability that the true mean age of the 714 recorded passengers lies inside this interval [26.88, 32.72]  
B) The 95% is a hit rate of the procedure across repeated studies, not a probability attached to this interval  
C) About 95% of the 714 recorded passenger ages fall inside [26.88, 32.72], which is what the level counts  
D) Raising the level to 99% would narrow the interval, because greater confidence pins the true mean down more tightly  

---

### Question 7
*taught eight or more weeks ago | Course 01, Unit 2*

Course 01 used Bayes' theorem on a medical test whose positive result still left the patient probably healthy. What is Bayesian probability used for in AI?

A) Handling uncertainty and drawing probabilistic inferences from evidence  
B) Guaranteeing a correct diagnosis whenever a test result comes back positive  
C) Computing the prior probability of a hypothesis before evidence is observed  
D) Removing uncertainty so predictions become deterministic  

---

### Question 8
*taught eight or more weeks ago | Course 01, Unit 2*

In Course 01 you built a small knowledge graph over family relations and queried it. What is a knowledge graph?

A) A neural network whose neurons are arranged as nodes and edges rather than as layers  
B) A search algorithm that walks a graph outward from a start node until it first meets a goal node  
C) A structure that stores entities as nodes and the relations between them as labelled edges  
D) An activation function applied over a graph of inputs to produce one scalar output  

---

### Question 9
*taught eight or more weeks ago | Course 02, Unit 1*

Course 02 ran A* with the heuristic h(n) = |ord(n) - ord(goal)| and checked it against the true remaining cost h*:

```
   A: h=6, h*=3  ->  OVERESTIMATES by 3
   B: h=5, h*=2  ->  OVERESTIMATES by 3
   E: h=2, h*=1  ->  OVERESTIMATES by 1
   G: h=0, h*=0  ->  OK
```

A* then returned A -> B -> E -> G, which is the shortest path on that graph, having opened 6 of the 7 nodes (BFS opened 7). What does this run establish about the heuristic?

A) h is admissible, because the path A* returned is in fact the shortest one on this graph  
B) The overestimates are uniform across nodes, so they cancel and the guarantee holds  
C) h is inadmissible, and that is what made A* open 6 nodes where BFS had to open 7  
D) h overestimates, so the guarantee did not apply - the shortest path came back anyway  

---

### Question 10
*taught eight or more weeks ago | Course 02, Unit 2*

A triage knowledge base holds 4,000 recorded patient facts and 300 rules. A clinician needs one answer: should Patient 7 be flagged for sepsis? Which inference strategy fits this request, and why?

A) Backward chaining: it starts from this one goal and expands just the rules that bear on the case  
B) Forward chaining: firing the rules in the order they were written is what makes a conclusion sound  
C) Backward chaining: it can withdraw a conclusion when a later fact turns out to contradict it  
D) Forward chaining: it derives the consequences of the 4,000 facts, and this answer is among them  

---

**Answers: worked aloud by your instructor in the eight minutes after you hand this back. Nothing to submit, nothing to mark.**
