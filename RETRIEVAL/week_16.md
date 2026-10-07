# Retrieval Quiz — Week 16

**Week 16 of 35 · Course 05 — AIAT 115 (Scalable Data Science) and Course 06 — AIAT 116 (Artificial Intelligence Ethics)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The Unit 5 chunking lesson streamed the **14,015**-flow sample in **10 chunks of 1,500** rows (the last chunk held **515**) and printed a global mean of **6.84** forward packets per flow from a running total of **95,877** packets. A colleague wants two further figures from that same single pass: **(a)** the largest `Flow Duration` recorded for each `Label`, and **(b)** the quartiles of `Flow Duration` across the whole file. Which of the two can one chunked pass deliver exactly, and how?

A) (a) exactly, by keeping each label's largest value seen so far and updating it per chunk; (b) not from one pass, since quartiles are rank statistics that need the whole ordering, so use t-digest or a real engine  
B) (a) exactly, by keeping per-chunk maxima for each label; (b) exactly, by computing the quartiles of each chunk and weighting the ten results by chunk size so that the 515-row final chunk counts for less  
C) (a) approximately at best, because a rare label such as Heartbleed may fall inside a single chunk and its maximum is then compared against no other chunk; (b) exactly, by taking the quartiles of the per-chunk quartiles  
D) Neither exactly: an uneven final chunk of 515 rows breaks any statistic merged across chunks, so both need the file in memory at once, as the lesson's 1.3 MB measurement did  

---

### Question 2

A triage model raises average survival across all patients while systematically deprioritising one group. What does a utilitarian analysis of that trade say?

A) The deprioritisation is wrong in itself, because it treats those patients as a means to a total rather than as ends in themselves  
B) The right question is what a person of good character would do, and a good clinician would not accept the trade  
C) The trade is justified if the aggregate gain in survival outweighs the harm, since the total welfare is what counts  
D) The trade is acceptable when the affected group consented to it, because consent is what makes a burden legitimate  

---

### Question 3

Course 06 Unit 1 used the COMPAS recidivism tool as its worked case. ProPublica reported that among defendants who did NOT go on to reoffend, the tool's false-positive rate was 44.9% for Black defendants against 23.5% for white defendants. Which ethical problem do those two numbers identify?

A) The tool's overall accuracy was too low for it to be used in a courtroom at all, for defendants of either group  
B) Among defendants who did not reoffend, one racial group was wrongly flagged far more often than the other  
C) The risk scores meant different things for the two groups, so the same score was not comparable across them  
D) The tool's scores were kept secret, so a defendant could not see the number used against them  

---

### Question 4

In gradient boosting (XGBoost, LightGBM), what does the learning_rate hyperparameter control?

A) How many of the available features each individual tree in the ensemble is allowed to look at when it splits  
B) How much each newly added tree contributes to the ensemble's running prediction, round by round  
C) How many CPU cores the library is allowed to use while it fits the trees in the ensemble  
D) The proportion of the data held back for the test split before the boosting rounds begin  

---

### Question 5

A random forest and a gradient-boosted ensemble both combine many decision trees. What separates the way they are built?

A) Bagging is used for regression targets and boosting for classification targets  
B) Bagging averages trees of the same depth, while boosting averages trees of increasing depth  
C) Boosting fits its trees independently in parallel, while bagging fits each one after the last has finished  
D) Bagging fits its trees in parallel; boosting fits each tree to correct what the previous ones got wrong  

---

### Question 6

Course 04 Unit 5 tuned the same model with grid search and with random search. What is random search's main advantage over an exhaustive grid?

A) It reaches a higher test score than grid search on the same budget of fits  
B) It removes the need for cross-validation, since each draw is already independent  
C) It samples the space instead of enumerating it, so a good setting often turns up in fewer fits  
D) It settles on the best combination in the grid, and does so without repeating a combination twice  

---

### Question 7

On a deep graph, what does Depth-First Search have over Breadth-First Search?

A) It stores one branch at a time, so its frontier stays small where BFS holds a whole layer  
B) It reaches the goal along a shorter path, since it does not spread out sideways  
C) It visits fewer nodes in total, because it does not re-open a node it has already seen  
D) It returns a more accurate answer, because it explores each branch to its full depth first  

---

### Question 8

Course 01's knowledge base stores each rule as `{'if': condition, 'then': conclusion}` and adds one with `add_rule("has feathers", "is a bird")`. What is that IF-THEN construct?

A) A loop that repeats the test over the fact base until the fact base stops changing  
B) A production rule: a condition on the facts, plus the conclusion to add when it holds  
C) An indexing structure that lets the engine look a feature up without scanning the facts  
D) A search procedure that expands the fact base outward from the start node  

---

### Question 9

The eigenvalues lesson notes that the raw USArrests features live on very different ranges — Murder spans 0.8–17.4 and Assault 45–337 arrests per 100,000 — and its figure note says that on raw units PC1 'points almost straight up: 99.8% of it is the Assault axis'. After standardizing, the printed feature variances are Murder = 1.02 and Assault = 1.02, and PC2 keeps 9.91% of the variance. A colleague wants to send the raw-units decomposition to a state governor because 'it explains far more of the variance'. Why is the standardized run the one to report?

A) Standardizing gives both features a variance of 1.02, which adds spread for PC1 to explain that the raw run lacked  
B) The 9.91% left to PC2 after standardizing shows the raw run had dropped its second component and summed over a single eigenvalue  
C) On raw units PC1 is nearly the Assault column renamed, so its variance figure describes the recording scale, not a crime pattern  
D) Because 99.8% of raw PC1 lies along Assault, the raw covariance matrix is close to singular and its eigenvalues cannot be trusted  

---

### Question 10

In Course 02's diagnosis system, Common Cold entered with a prevalence of 15% and left with a posterior of 19.6%. Which of these is the prior?

A) The 19.6% figure, since that is the probability the system reports at the end of the whole calculation  
B) The 5.6% likelihood, which is the probability of seeing these symptoms if the patient has a cold  
C) The ratio of the two, which measures how far the evidence moved the system's belief  
D) The 15% prevalence, which is what the system believed about Common Cold before the symptoms arrived  

---
