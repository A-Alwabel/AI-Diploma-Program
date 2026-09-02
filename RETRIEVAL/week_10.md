# Cumulative Retrieval Quiz - Week 10

**Programme week 10 of 35 | Course 04 - AIAT 114 (Machine Learning Algorithms and Applications)**

Taught this week: Unit 2 (model evaluation, sessions 37-38) and Unit 3 (classification, sessions 39-40).

---

## How this works

- **15 minutes, in class, at the END of session 40.** You answer for about 7 minutes; your instructor then works the correct answers aloud for about 8.
- **This is not graded.** No mark from this paper reaches your course grade, and it carries no weight in any of the six assessment lines.
- **The correct answers are worked immediately afterwards, in the room.** That worked correction is the part that does the teaching; a quiz that only returns a score is worth about a third less.
- Ten questions. Three are on material from this week or last, three on material from about a month ago, and four on material from earlier in the programme. Each earlier question carries the context it needs, so you are not being asked to recall a lesson cold.
- Write one letter per question. No calculator, no laptop, no notes - answering from memory is the whole point.

---

### Question 1
*taught this week or last | Course 04, Unit 2*

Course 04 Unit 2 compared one 80/20 split against 5-fold cross-validation on the same community crime data. A colleague evaluates the crime-rate regression on one 80/20 split and reports R2 = 0.1095. The 5-fold cross-validation prints R2 = 0.0844 +/- 0.0358, and across ten different single splits the R2 ran from 0.0402 to 0.1259 - the largest 3.1 times the smallest. What is wrong with the colleague's report?

A) 0.1095 sits near the top of the range a single split produces, and the report gives no way to spot a lucky split  
B) 0.1095 has to be wrong: the true value is 0.0844, so test rows have leaked into the colleague's training set and inflated it  
C) Both procedures hold out 20% of the rows, so the difference is down to the seed and can be ignored  
D) Cross-validation trains each fold on less data, which makes 0.0844 pessimistic and 0.1095 the honest figure  

---

### Question 2
*taught this week or last | Course 04, Unit 3*

Course 04 Unit 3's logistic-regression lesson tests on 3,200 real card transactions, 6 of them fraudulent, and prints a confusion matrix of TN 3191, FP 3, FN 3, TP 3 - test accuracy 0.9981. The same lesson prints that labelling every row 'legitimate' also scores 0.9981. What do those two identical accuracies establish?

A) The classifier learned nothing from the 30 features, since it scores exactly what a model with no features scores  
B) Accuracy is set by the 3,194 legitimate rows and has no room to register the 6 fraud rows either way  
C) At 3,200 rows the test set is too small for accuracy to be reliable for either model  
D) The two agree because the cut sits at 0.5; moving that cut down to 0.3 would separate the model from the baseline  

---

### Question 3
*taught this week or last | Course 04, Unit 1*

Course 04 Unit 1's regularization lesson predicts transaction Amount from 29 features using 8,000 training rows, and prints:

```
Model               Test MSE    Test R2
Linear Regression   4133.9568   0.8930
Ridge (a = 0.01)    4133.9591   0.8930
Lasso (a = 0.1)     4130.9723   0.8931
```

Alphas from 0.01 to 100 were tried for both. At its best alpha, Lasso kept 29 of 29 features. Which conclusion do these numbers support?

A) Neither penalty was tuned far enough; the search should be extended past a = 100 until one of them clearly beats the baseline  
B) Lasso won, and its margin is L1 performing the feature selection that Ridge leaves undone here  
C) V1-V28 are uncorrelated PCA components, so a penalty on their coefficients has no well-defined effect here  
D) With 8,000 rows against 29 features the baseline is not overfitting, so shrinking coefficients adds bias and buys nothing  

---

### Question 4
*taught about a month ago | Course 02, Unit 4*

Course 02's Unit 4 notebook ran gradient descent on f(x) = x^2 from x = 5.0, changing only the learning rate:

```
learning rate     x @ step 0   x @ step 3   x @ step 12  x @ step 25   verdict
0.01                  5.0000       4.7060       3.9236       3.0173   too small
0.10                  5.0000       2.5600       0.3436       0.0189   just right
0.95                  5.0000      -3.6450       1.4121      -0.3589   too big
1.10                  5.0000      -8.6400      44.5805    -476.9810   way too big
```

A student concludes: "a learning rate that overshoots the minimum will diverge." Which row refutes that, and how?

A) lr = 0.01: it stays on one side of the minimum, so overshoot is not required in order to converge  
B) lr = 0.95: it lands beyond the minimum (x = -3.65 at step 3) and still closes in to |x| = 0.36  
C) lr = 0.10: it reaches x = 0.019 without overshooting, so overshoot is what slows a run down  
D) lr = 1.10: its sign alternates, showing that overshoot and divergence are the same behaviour  

---

### Question 5
*taught about a month ago | Course 02, Unit 3*

Course 02's Unit 3 diagnosis system is given a patient with fever, cough and fatigue, and prints:

```
disease         prevalence  prior (norm.)  P(symptoms|d)   posterior   rank move
Common Cold         15.0%          68.2%           5.6%       19.6%       1 -> 3
Flu                  5.0%          22.7%          50.4%       58.9%       2 -> 1
COVID-19             2.0%           9.1%          45.9%       21.5%       3 -> 2
```

Common Cold is by far the most prevalent of the three diseases, yet it finishes last. Why?

A) Renormalising the three prevalences against one another pushes the largest of them below the rest  
B) Common Cold has no listed probability for fatigue, so the system skips it in the product  
C) Bayes multiplies prior by likelihood, and P(symptoms | Cold) = 5.6% is nine times below Flu's  
D) The posterior follows the highest single symptom probability, and Flu's fever figure is 90%  

---

### Question 6
*taught about a month ago | Course 02, Unit 5*

One trained logistic-regression model is scored on the same 171 held-out breast-tumour biopsies; only the decision threshold changes:

```
    threshold   missed malignant   false alarms   accuracy
         0.20                  1             21     87.1%
         0.40                  7              9     90.6%
         0.50                 11              5     90.6%
         0.80                 20              0     88.3%
   Best accuracy on this grid: 92.4% at threshold 0.44 - which still misses 8 malignant tumours.
```

A screening clinic can absorb at most 25 false alarms out of the 171, and within that limit wants to miss as few malignant tumours as it can. Which threshold does the table support, and at what cost?

A) 0.44 - it is the highest accuracy on the grid, 92.4%, and accuracy is the metric to maximise  
B) 0.80 - it brings false alarms down to zero, and 88.3% accuracy is near the grid maximum  
C) 0.50 - it is the library default, so it already balances the two kinds of error by construction  
D) 0.20 - it misses 1 malignant tumour rather than 11, and its 21 false alarms fit the budget  

---

### Question 7
*taught eight or more weeks ago | Course 01, Unit 2*

What is the main difference between supervised and unsupervised learning?

A) Supervised learning trains faster, because the labels shorten the search for a good model  
B) Supervised learning predicts numbers, unsupervised learning predicts categories  
C) Supervised learning uses labelled data, unsupervised learning uses unlabelled data  
D) Supervised learning uses neural networks, unsupervised learning uses clustering algorithms  

---

### Question 8
*taught eight or more weeks ago | Course 01, Unit 1*

What are the components of a knowledge representation system, of the kind Course 01 built to answer questions about a family?

A) A relational database table with indexed columns holding the system's records  
B) A labelled training set and a loss function  
C) A priority queue ordered by a heuristic function estimating remaining cost  
D) Facts, rules, and an inference mechanism that derives new facts from them  

---

### Question 9
*taught eight or more weeks ago | Course 01, Unit 1*

Course 01 ran BFS, DFS and A* on the same small graph. Which of these is guaranteed to return a shortest path on an unweighted graph, and why?

A) Depth-First Search, because it drives straight down one branch and reaches a goal without wandering over the frontier  
B) Breadth-First Search, because it expands the frontier one edge-layer at a time, so a goal is first met at its shallowest depth  
C) A* with a heuristic of your choosing, because ordering the frontier by estimated remaining cost settles path length  
D) Depth-First Search with a visited set, because marking visited nodes stops it from revisiting and so from lengthening the path it returns  

---

### Question 10
*taught eight or more weeks ago | Course 01, Unit 4*

Which of these groups lists three activation functions of the kind used inside a feedforward neural network?

A) ReLU, Sigmoid, Tanh  
B) Adam, SGD, RMSprop  
C) MSE, Cross-Entropy, Hinge  
D) Dropout, Batch Normalization, Early Stopping  

---

**Answers: worked aloud by your instructor in the eight minutes after you hand this back. Nothing to submit, nothing to mark.**
