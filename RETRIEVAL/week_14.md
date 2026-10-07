# Retrieval Quiz — Week 14

**Week 14 of 35 · Course 05 — AIAT 115 (Scalable Data Science)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

You are reviewing a slide built from the Unit 3 best-practices lesson. Its bar chart of 2018 quarterly 911 dispatches shows a visible plunge in Q2, yet the check printed under the very same data reads: *"the whole year sits within 8.8% of its own mean"*. The data is the bundled 1-in-27 sample of the call log. How do you reconcile the chart with the printout, and what should the slide do?

A) The 8.8% is measured against the mean while the bars show raw counts, so the chart is right and the printout understates the swing; keep the bars as drawn and delete the sentence  
B) The 1-in-27 sampling inflates quarter-to-quarter variation in the counts, so the chart exaggerates; multiply each quarter by 27 before plotting so the bars settle  
C) Quarters differ in length by a few days, which the raw counts do not correct for; convert each bar to calls per day and the plunge will shrink to its true size  
D) The axis made the plunge, not the data: `set_ylim` starts just under the lowest quarter, so a year within 8.8% of its mean fills the frame; redraw from zero or flag the zoom  

---

### Question 2

You want to show whether a community's assault rate moves with its urban population share - two numeric columns, one row per community. Which chart does that job?

A) A bar chart, with one bar for each of the communities and its height set by that community's assault rate  
B) A scatter plot with urban share on one axis and assault rate on the other, a point per community  
C) A histogram of the assault rate, with the communities grouped into bins along the axis  
D) A pie chart, with each community taking a slice sized by its share of the total assaults  

---

### Question 3

Course 05 Unit 4 compared training and test scores for the same model. Which pattern is overfitting?

A) Training score low and test score low as well, because the model is too simple for the pattern in the data  
B) Training score high and test score much lower, because the model has learned the training rows themselves  
C) Training score low and test score high, because the test split happened to be the easier of the two  
D) Training score high and test score high, because the model has learned a pattern that generalises  

---

### Question 4

Unit 2's 5-fold cross-validation of the murder-rate regression prints these fold scores:

```
Fold 1: R² = 0.1095
Fold 2: R² = 0.0616
Fold 3: R² = 0.0703
Fold 4: R² = 0.0999
Fold 5: R² = 0.0809

Mean R²: 0.0844
Std R²:  0.0179
```

A teammate wants the report to state **R² = 0.0616** - "the worst fold, so nobody can accuse us of picking a lucky split." Which response is right?

A) Agree: the lowest fold is the floor on what the model can do, so quoting it is the conservative choice and needs no spread beside it  
B) The spread comes from fold 5 holding out 398 rows instead of 399, so the fix is Leave-One-Out cross-validation, which gives each fold the same size before anything is reported  
C) Quoting the worst fold is still quoting one draw; the honest figure is the pair 0.0844 ± 0.0179, which shows how far a single fold can land from the mean  
D) A std of 0.0179 on a mean of 0.0844 means the model is too unstable to report; collect more features before quoting any R² to the client  

---

### Question 5

Unit 3's logistic-regression lesson sweeps the decision cut from 0.1 to 0.9 on its 3,200-row test set and prints:

```
Threshold    Accuracy     Precision    Recall       F1 Score
0.1          0.9975       0.4000       0.6667       0.5000
0.2          0.9984       0.5714       0.6667       0.6154
0.3          0.9981       0.5000       0.5000       0.5000
...
0.9          0.9981       0.5000       0.5000       0.5000
```

Precision and recall move by tens of points down the table; the accuracy column stays between 0.9975 and 0.9984. A student asks why accuracy looks "stuck". What is the correct explanation?

A) The model's predicted probabilities are nearly identical from row to row, so sliding the cut hardly changes any individual prediction  
B) Accuracy, like AUC, is defined over the whole range of thresholds at once, so a table that varies the cut is not something it is expected to respond to  
C) A 3,200-row test set is simply too small for accuracy to resolve the differences between cuts; a larger test sample would separate the rows of the table cleanly and rank them  
D) 3,194 of 3,200 rows are legitimate and cleared at almost any cut, so accuracy stays pinned near the baseline of calling each row legitimate, whatever the 6 fraud rows do  

---

### Question 6

Unit 1's regularization lesson predicts transaction `Amount` and prints a plain `LinearRegression` baseline of **MSE 4133.96**, then this part of the Lasso sweep:

```
Alpha   1.00: MSE = 4137.4229, R² = 0.8930, Features = 28/29
Alpha  10.00: MSE = 6043.0153, R² = 0.8437, Features = 14/29
Alpha 100.00: MSE = 36102.8517, R² = 0.0659, Features = 1/29
```

A teammate wants to report the α = 10 model: "it is the first setting where Lasso actually selects features, so the regularization is finally doing its job." Which reading of these rows is right?

A) Each column Lasso switched off cost test error, which is what selection looks like when the baseline had no overfitting for a penalty to remove  
B) Fourteen inputs at R² 0.8437 is the leaner model, and leaner is what regularization is for, so it should replace the 29-feature baseline in the report  
C) The grid is too coarse: an α between 1 and 10 would drop columns while holding the baseline's error, so refine the sweep before choosing  
D) Removing half the columns cures the multicollinearity among V1–V28, so the α = 10 coefficients are the trustworthy ones to publish  

---

### Question 7

Breadth-First Search keeps a frontier of nodes waiting to be expanded. Which container does it use, and what does that container enforce?

A) A stack, so the node added most recently is the next one expanded  
B) A hash table, so a node can be looked up in constant time when it is needed  
C) A priority queue, so the node with the lowest estimated total cost is expanded next  
D) A queue, so the node that has waited longest is the next one expanded  

---

### Question 8

Course 01 trained a single perceptron on AND, then on XOR, and it failed on XOR. Which problems can one perceptron solve?

A) Problems whose two classes can be separated by a single straight line in the space of inputs  
B) Problems where the classes interleave, which is what one weighted sum is built to untangle  
C) Problems of either kind, provided the perceptron is given enough training epochs to converge on them  
D) It fails on AND as well as on XOR, since a perceptron has no hidden layer at all  

---

### Question 9

Gradient descent updates a parameter with x <- x - learning_rate * gradient. What does the gradient itself point along, and why is there a minus sign?

A) Along the direction in which the function rises fastest, so the step is taken the opposite way  
B) Along the direction in which the function falls fastest, so the minus sign reverses a correct step  
C) Along the axis of the parameter with the largest current value, which the minus sign then shrinks  
D) Along the straight line from the current point to the minimum, scaled by the learning rate  

---

### Question 10

Course 02 compared two gambles: Option A pays 100 with probability 0.8, Option B pays 200 with probability 0.5. What quantity decides between them, and what is it?

A) The most likely single outcome, which is 100 for A and 0 for B, so A is preferred  
B) The largest possible payout, which is 200 for B, so B is preferred whatever the odds  
C) The expected value - each outcome weighted by its probability - which is 80 for A and 100 for B  
D) The probability of a payout at all, which is 0.8 for A against 0.5 for B, so A is clearly preferred  

---
