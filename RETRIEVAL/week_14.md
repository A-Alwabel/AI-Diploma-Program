# Retrieval Quiz — Week 14

**Week 14 of 35 · Course 05 — AIAT 115 (Scalable Data Science)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

A colleague's bar chart of 2018 quarterly 911 call volume shows Q2 as a collapse and Q4 as a full recovery. The counts behind it are Q1 1,478, Q2 1,352, Q3 1,402, Q4 1,478 - a change of +0.00% across the year. No number was altered between the data and the chart. What produced the misleading chart, and what is the fix?

A) The bars were sorted by value rather than by quarter; re-order them chronologically so the trend reads correctly  
B) Counts were plotted where percentages were needed; convert each quarter to a percentage change from Q1  
C) The y-axis was truncated to start just below the smallest bar; start it at zero, or flag the zoom  
D) Four categories are too few for bars; a pie chart would show the quarters' shares more fairly  

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

Course 04 Unit 2 compared one 80/20 split against 5-fold cross-validation on the same community crime data. A colleague evaluates the crime-rate regression on one 80/20 split and reports R2 = 0.1095. The 5-fold cross-validation prints R2 = 0.0844 +/- 0.0358, and across ten different single splits the R2 ran from 0.0402 to 0.1259 - the largest 3.1 times the smallest. What is wrong with the colleague's report?

A) 0.1095 sits near the top of the range a single split produces, and the report gives no way to spot a lucky split  
B) 0.1095 has to be wrong: the true value is 0.0844, so test rows have leaked into the colleague's training set and inflated it  
C) The two procedures hold out 20% of the rows, so the difference is down to the seed and can be ignored  
D) Cross-validation trains each fold on less data, which makes 0.0844 pessimistic and 0.1095 the honest figure  

---

### Question 5

Course 04 Unit 3's logistic-regression lesson tests on 3,200 real card transactions, 6 of them fraudulent, and prints a confusion matrix of TN 3191, FP 3, FN 3, TP 3 - test accuracy 0.9981. The same lesson prints that labelling every row 'legitimate' also scores 0.9981. What do those two identical accuracies establish?

A) The classifier learned nothing from the 30 features, since it scores exactly what a model with no features scores  
B) Accuracy is set by the 3,194 legitimate rows and has no room to register the 6 fraud rows either way  
C) At 3,200 rows the test set is too small for accuracy to be reliable for either model  
D) The two agree because the cut sits at 0.5; moving that cut down to 0.3 would separate the model from the baseline  

---

### Question 6

Course 04 Unit 1's regularization lesson predicts transaction Amount from 29 features using 8,000 training rows, and prints:

```
Model               Test MSE    Test R2
Linear Regression   4133.9568   0.8930
Ridge (a = 0.01)    4133.9591   0.8930
Lasso (a = 0.1)     4130.9723   0.8931
```

Alphas from 0.01 to 100 were tried for both. At its best alpha, Lasso kept 29 of 29 features. Which conclusion do these numbers support?

A) The penalties were not tuned far enough; the search should be extended past a = 100 until one of them clearly beats the baseline  
B) Lasso won, and its margin is L1 performing the feature selection that Ridge leaves undone here  
C) V1-V28 are uncorrelated PCA components, so a penalty on their coefficients has no well-defined effect here  
D) With 8,000 rows against 29 features the baseline is not overfitting, so shrinking coefficients adds bias and buys nothing  

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
