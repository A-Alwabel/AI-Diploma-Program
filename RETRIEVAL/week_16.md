# Cumulative Retrieval Quiz - Week 16

**Programme week 16 of 35 | Course 05 - AIAT 115 closes (session 62) and Course 06 - AIAT 116 (Ethics of AI) opens**

Taught this week: Course 05 Unit 5 (session 61), the Course 05 wrap (session 62), and Course 06 Unit 1 (session 63).

---

## How this works

- **15 minutes, in class, at the END of session 63.** You answer for about 7 minutes; your instructor then works the correct answers aloud for about 8.
- **This is not graded.** No mark from this paper reaches your course grade, and it carries no weight in any of the six assessment lines.
- **The correct answers are worked immediately afterwards, in the room.** That worked correction is the part that does the teaching; a quiz that only returns a score is worth about a third less.
- Ten questions. Three are on material from this week or last, three on material from about a month ago, and four on material from earlier in the programme. Each earlier question carries the context it needs, so you are not being asked to recall a lesson cold.
- Write one letter per question. No calculator, no laptop, no notes - answering from memory is the whole point.

---

### Question 1
*taught this week or last | Course 05, Unit 5*

You must compute two figures from a 40 GB sales.csv on a laptop with 16 GB of RAM, using pd.read_csv(..., chunksize=...): (i) the mean amount per category, and (ii) the median amount over the whole file. Which statement correctly describes what one chunked pass can give you, and how?

A) (i) exactly, by carrying a running sum and count per category; (ii) exactly, by taking one median per chunk and averaging those in proportion to chunk size  
B) (i) exactly, by averaging the per-chunk category means at the end; (ii) exactly, because the median of the per-chunk medians is the median of the file  
C) (i) exactly, by carrying a running sum and a running count per category; (ii) not from one chunked pass - a median needs all the values at once  
D) Neither exactly: combining results across chunks assumes the chunks hold equal numbers of rows, and here the last chunk holds fewer  

---

### Question 2
*taught this week or last | Course 06, Unit 1*

A triage model raises average survival across all patients while systematically deprioritising one group. What does a utilitarian analysis of that trade say?

A) The deprioritisation is wrong in itself, because it treats those patients as a means to a total rather than as ends in themselves  
B) The right question is what a person of good character would do, and a good clinician would not accept the trade  
C) The trade is justified if the aggregate gain in survival outweighs the harm, since the total welfare is what counts  
D) The trade is acceptable when the affected group consented to it, because consent is what makes a burden legitimate  

---

### Question 3
*taught this week or last | Course 06, Unit 1*

Course 06 Unit 1 used the COMPAS recidivism tool as its worked case. ProPublica reported that among defendants who did NOT go on to reoffend, the tool's false-positive rate was 44.9% for Black defendants against 23.5% for white defendants. Which ethical problem do those two numbers identify?

A) The tool's overall accuracy was too low for it to be used in a courtroom at all, for defendants of either group  
B) Among defendants who did not reoffend, one racial group was wrongly flagged far more often than the other  
C) The risk scores meant different things for the two groups, so the same score was not comparable across them  
D) The tool's scores were kept secret, so a defendant could not see the number used against them  

---

### Question 4
*taught about a month ago | Course 04, Unit 5*

In gradient boosting (XGBoost, LightGBM), what does the learning_rate hyperparameter control?

A) How many of the available features each individual tree in the ensemble is allowed to look at when it splits  
B) How much each newly added tree contributes to the ensemble's running prediction, round by round  
C) How many CPU cores the library is allowed to use while it fits the trees in the ensemble  
D) The proportion of the data held back for the test split before the boosting rounds begin  

---

### Question 5
*taught about a month ago | Course 04, Unit 5*

A random forest and a gradient-boosted ensemble both combine many decision trees. What separates the way they are built?

A) Bagging is used for regression targets and boosting for classification targets  
B) Bagging averages trees of the same depth, while boosting averages trees of increasing depth  
C) Boosting fits its trees independently in parallel, while bagging fits each one after the last has finished  
D) Bagging fits its trees in parallel; boosting fits each tree to correct what the previous ones got wrong  

---

### Question 6
*taught about a month ago | Course 04, Unit 5*

Course 04 Unit 5 tuned the same model with grid search and with random search. What is random search's main advantage over an exhaustive grid?

A) It reaches a higher test score than grid search on the same budget of fits  
B) It removes the need for cross-validation, since each draw is already independent  
C) It samples the space instead of enumerating it, so a good setting often turns up in fewer fits  
D) It settles on the best combination in the grid, and does so without repeating a combination twice  

---

### Question 7
*taught eight or more weeks ago | Course 01, Unit 1*

On a deep graph, what does Depth-First Search have over Breadth-First Search?

A) It stores one branch at a time, so its frontier stays small where BFS holds a whole layer  
B) It reaches the goal along a shorter path, since it does not spread out sideways  
C) It visits fewer nodes in total, because it does not re-open a node it has already seen  
D) It returns a more accurate answer, because it explores each branch to its full depth first  

---

### Question 8
*taught eight or more weeks ago | Course 01, Unit 2*

A rule in Course 01's expert system reads: IF X has Fever AND X has Cough THEN X likely_has Flu. What is that IF-THEN construct?

A) A loop that repeats the test over the fact base until the fact base stops changing  
B) A production rule: a condition on the facts, plus the conclusion to add when it holds  
C) An indexing structure that lets the engine look a symptom up without scanning the facts  
D) A search procedure that expands the fact base outward from the patient node  

---

### Question 9
*taught eight or more weeks ago | Course 03, Unit 1*

Course 03 eigen-decomposed the covariance matrix of the 50-state USArrests data (Murder, Assault) twice:

- Standardized: eigenvalues 1.8019 and 0.1981; PC1 = +0.707 x Murder + 0.707 x Assault; PC1 explains 90.09% of the variance.
- Raw units: feature variances Murder 18.97 and Assault 6945.17; PC1 = +0.042 x Murder + 0.999 x Assault; PC1 explains 99.90% of the variance.

Why is the raw-units 99.90% the less informative of the two figures?

A) On raw units PC1 follows Assault, whose variance is 6945 against Murder's 19, so the component reports the measuring scale  
B) The raw-units run keeps one component while the standardized run keeps two, so the two percentages count different totals  
C) Standardizing increases the variance available to PC1, so 90.09% of standardized variance carries more information than the raw 99.90%  
D) A first component above 99% means the raw covariance matrix is singular, which makes its second eigenvalue unreliable  

---

### Question 10
*taught eight or more weeks ago | Course 02, Unit 3*

In Course 02's diagnosis system, Common Cold entered with a prevalence of 15% and left with a posterior of 19.6%. Which of these is the prior?

A) The 19.6% figure, since that is the probability the system reports at the end of the whole calculation  
B) The 5.6% likelihood, which is the probability of seeing these symptoms if the patient has a cold  
C) The ratio of the two, which measures how far the evidence moved the system's belief  
D) The 15% prevalence, which is what the system believed about Common Cold before the symptoms arrived  

---

**Answers: worked aloud by your instructor in the eight minutes after you hand this back. Nothing to submit, nothing to mark.**
