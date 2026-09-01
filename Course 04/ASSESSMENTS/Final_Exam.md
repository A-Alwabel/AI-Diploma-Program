# Final Exam: Machine Learning Algorithms and Applications
## AIAT 114

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. Show your work for partial credit.

**Marking scheme:** Part 1 (Q1–Q6): 5 pts each = 30. Part 2 (Q7–Q9): 10 pts each = 30. Part 3 (Q10: 15 pts, Q11: 10 pts) = 25. Part 4 (Q12): 15 pts. **Total: 100.**

Every table and figure quoted in this paper is a value printed by a lesson you ran in this course, on the real datasets you ran it on. Where a question asks you to *derive* a number, show the arithmetic.

---

## Part 1: Multiple Choice (30 points)

### Question 1 (5 points)
**CLO1:** Unit 3's KNN lesson fits the same model twice on the same 313 real card transactions. Without scaling it scores accuracy **0.9048**; with `StandardScaler` it scores **0.9683**. The lesson also prints that the `Time` column alone contributes **99.9978%** of the raw squared distance between two transactions (`Time` std 46,331.2, against a median feature std of 1.302).

What does that 99.9978% figure explain?

A) Unscaled, "nearest neighbour" means roughly "happened at a similar moment", so what V1–V28 know about a transaction is drowned out  
B) The V1–V28 columns barely vary across these rows, so they contribute almost nothing to the distances the model computes  
C) `Time` is the single most predictive feature of fraud here, so scaling it down discards the best signal the model has  
D) `StandardScaler` dropped `Time` from the feature set, and removing that one dominant column is what lifted accuracy by 6.35 points

---

### Question 2 (5 points)
**CLO2, CLO3:** Unit 1's regularization lesson predicts transaction `Amount` from 29 features using 8,000 training rows, and prints:

| Model | Test MSE | Test R² |
|---|---|---|
| Linear Regression | 4133.9568 | 0.8930 |
| Ridge (α = 0.01) | 4133.9591 | 0.8930 |
| Lasso (α = 0.1) | 4130.9723 | 0.8931 |

Alphas from 0.01 to 100 were tried for both. At its best alpha, Lasso kept **29 of 29** features.

Which conclusion do these numbers support?

A) Neither penalty was tuned far enough; the search should be extended past α = 100 until one of them beats the baseline  
B) Lasso won, and its margin is L1 performing the feature selection that Ridge leaves undone here  
C) V1–V28 are uncorrelated PCA components, so a penalty on their coefficients has no well-defined effect here  
D) With 8,000 rows against 29 features the baseline is not overfitting, so shrinking coefficients adds bias and buys nothing

---

### Question 3 (5 points)
**CLO4:** Unit 3's logistic-regression lesson tests on 3,200 real transactions, 6 of them fraudulent, and prints:

```
[[3191    3]      TN = 3191    FP = 3
 [   3    3]]     FN = 3       TP = 3
```

Test accuracy **0.9981**. The same lesson prints that labelling every row "legitimate" scores **0.9981**.

What do those two identical accuracies establish?

A) The classifier learned nothing from the 30 features, since it scores exactly what a model with no features scores  
B) Accuracy is set by the 3,194 legitimate rows and has no room to register the 6 fraud rows either way  
C) At 3,200 rows the test set is still too small for accuracy to be a reliable estimate of either model  
D) The two agree because the cut sits at 0.5; moving that cut down to 0.3 would separate the model from the baseline

---

### Question 4 (5 points)
**CLO4:** The same lesson refits the model with `class_weight='balanced'` and prints the change on the test set:

```
Fraud caught (TP):   3 -> 3       Fraud missed (FN):   3 -> 3
False alarms (FP):   3 -> 18      Legit cleared (TN):  3191 -> 3176
```

Precision 0.5000 → 0.1429, recall 0.5000 → 0.5000, accuracy 0.9981 → 0.9934.

What should the analyst conclude?

A) Recall did not move because the weighting was too weak; a larger manual weight on class 1 would lift it  
B) Precision falling from 0.50 to 0.14 is the signature of a model overfitting the minority class  
C) The weighting bought 15 extra false alarms and no extra fraud: it moved the operating point, not the information  
D) Accuracy fell from 0.9981 to 0.9934, so the balanced model is the worse of the two and should be dropped

---

### Question 5 (5 points)
**CLO5:** Unit 4 clusters 1,994 communities on 4 scaled crime features and prints:

```
K=2   Inertia=5347.86   Silhouette=0.3967       K=6    Inertia=2398.46   Silhouette=0.2954
K=3   Inertia=4041.38   Silhouette=0.3134       K=8    Inertia=1970.75   Silhouette=0.3007
K=4   Inertia=3124.93   Silhouette=0.3153       K=10   Inertia=1720.82   Silhouette=0.2941
```

The elbow falls at K = 4; the silhouette peaks at K = 2; the lesson itself clusters at K = 3.

How should K be settled?

A) Take K = 10: it posts the lowest inertia anywhere in the table, and lower inertia means tighter, better clusters  
B) Take K = 2: the silhouette is the score that measures separation, so it settles the question  
C) The disagreement is a symptom of unscaled features; rescaling the four crime columns would make the two criteria converge  
D) The two criteria measure different things and disagree, so K is settled by what the clusters are for

---

### Question 6 (5 points)
**CLO2, CLO6:** A colleague evaluates the crime-rate regression on one 80/20 split and reports **R² = 0.1095**. Unit 2 runs 5-fold cross-validation on the same data and prints **R² = 0.0844 ± 0.0358**; across ten different single splits the R² ran from **0.0402 to 0.1259** (the largest 3.1× the smallest).

What is wrong with the colleague's report?

A) 0.1095 sits near the top of what a single split produces, and the report gives no way to spot a lucky one  
B) 0.1095 has to be wrong: the true value is 0.0844, so test rows have leaked into the colleague's training set  
C) Both procedures hold out 20% of the rows, so the difference comes down to the random seed and can be safely ignored  
D) Cross-validation trains each fold on less of the data, which makes 0.0844 pessimistic and 0.1095 the more honest figure

---

## Part 2: Short Answer Questions (30 points)

### Question 7 (10 points)
**CLO1:** Unit 1's cleaning lesson works on the 891-row Titanic manifest (with 2 duplicate rows added for the demonstration, so 893). It prints:

```
dropna(): 893 rows -> 184 rows (79.4% deleted)
76.8% of the people with a missing Age were 3rd class
```

**(a)** State what `dropna()` costs on this dataset *beyond* the 709 deleted rows, and name the printed figure that establishes it. **(3 pts)**

**(b)** Name the imputation you would use for `Age` instead. Justify it against one alternative you considered and rejected. **(3 pts)**

**(c)** Name one preprocessing step that must be fitted on the training split only. State exactly what leaks if it is fitted on all rows, and name the `train_test_split` argument that keeps a 0.175% positive rate in both halves. **(4 pts)**

---

### Question 8 (10 points)
**CLO2, CLO3:** The regularization lesson fits the baseline on **standardized** features and prints its first five coefficients as `[-2.78, -45.54, -114.73, -45.04, 17.47]`, predicting `Amount` in dollars. Its alpha sweep prints:

```
Ridge:  a=0.01  MSE 4133.9591   |  a=1  MSE 4134.1823   |  a=10  MSE 4136.2722   |  a=100  MSE 4162.9477
Lasso:  a=0.01  MSE 4133.6218, 29/29 features   |  a=0.1  MSE 4130.9723, 29/29
        a=1     MSE 4137.4229, 28/29            |  a=10   MSE 6043.0153, 14/29
        a=100   MSE 36102.8517,  1/29  (R2 = 0.0659)
Linear Regression baseline: MSE 4133.9568
```

**(a)** State what a coefficient of **−114.73** means here, and why standardizing the features first is what makes that statement possible. **(3 pts)**

**(b)** State what the L2 and the L1 penalty each do to a coefficient, and which of the two can set one to exactly zero. **(3 pts)**

**(c)** Explain from the numbers why the best Lasso kept 29 of 29 features, and what went wrong at α = 100. Then name the condition a dataset must have for L1 feature selection to pay, and the Unit 2 procedure you would use to check it — not the test set. **(4 pts)**

---

### Question 9 (10 points)
**CLO4, CLO7:** On the fraud test set (3,200 transactions, **6** of them fraud), the threshold sweep prints:

```
  cut   caught (TP)   missed (FN)   false alarms (FP)    recall   precision
  0.1             4             2                   6     0.667       0.400
  0.2             ?             ?                   ?     0.667       0.571
  0.5             3             3                   3     0.500       0.500
```

**(a)** Derive TP, FN and FP at the 0.2 cut from the printed recall and precision. Show the arithmetic. **(3 pts)**

**(b)** A missed fraud costs the bank **1,000 SAR**; a false alarm costs **20 SAR** of support time. Compute the total error cost at each of the three cuts and recommend one. **(4 pts)**

**(c)** The bank now says a false alarm costs **200 SAR**, not 20. Recompute, and state whether your recommendation changes. Then state whether *any* pair of costs would change it, and why. Finish with one sentence on what a test set holding 6 frauds can and cannot support. **(3 pts)**

---

## Part 3: Practical/Coding Questions (25 points)

### Question 10 (15 points)
**CLO1, CLO4:** Write a complete Python script that builds and evaluates a fraud classifier on the course's credit-card extract (16,000 transactions, 28 of them fraud — a 0.175% positive rate). Your script must:

1. Load the data and separate `X` (30 features) from `y` (`Class`)
2. Split 80/20 **so that both halves keep the 0.175% fraud rate**
3. Scale the features, fitted so that no test-set information reaches the training transform
4. Train a `LogisticRegression` classifier
5. Print the **confusion matrix**, and precision, recall and F1 **for the fraud class specifically**
6. Print the **ROC-AUC**
7. Print, on the same screen, the accuracy a model that labels every transaction "legitimate" would score — and one line of your own saying what that comparison means for the accuracy of your model

Step 7 is worth marks. A script that stops at step 6 is incomplete.

---

### Question 11 (10 points)
**CLO5:** Write a complete Python script that clusters the 1,994 communities on their 4 crime features (`Murder`, `Assault`, `UrbanPop`, `Rape`). Your script must:

1. Scale the four features, and state in a comment why this is not optional for K-Means
2. Fit K-Means for **K = 2 through 10**, recording inertia and silhouette score for each
3. Print the resulting table
4. Choose a K and print a one-line justification for the choice
5. Plot the clustered communities, with the centroids marked

Then, in one or two sentences below your code: if you needed to put these four-dimensional clusters on a 2-D chart, what would you use, and what would you have to check before trusting that chart?

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
**CLO6, CLO7:** Two models from this course are candidates for deployment at a bank.

**Model A** — logistic regression, Unit 3 lesson 01. Tested on 3,200 transactions at the real 0.175% fraud rate: accuracy **0.9981**, fraud-class precision **0.50**, recall **0.50**, ROC-AUC **0.8787**. A model that flags nothing scores **0.9981** on the same split.

**Model B** — random forest, Unit 3 lesson 05. Tested on 353 transactions from a 2.38% extract: accuracy **0.9972**, fraud-class precision **1.0000**, recall **0.8750**, ROC-AUC **0.9875**. A model that flags nothing scores **0.9773** on that split. The test split holds **8** frauds; the confusion matrix is TN 345, FP **0**, FN 1, TP 7.

Write a recommendation for the bank. It must contain:

1. **Why the two accuracy figures cannot be compared** — use both do-nothing baselines to make the argument, and say which numbers *can* be compared instead. **(4 pts)**
2. **The model-selection procedure you would run** before committing: name the technique, state what you would tune, and state which metric you would tune *on* and why not accuracy. **(4 pts)**
3. **The honest reading of Model B's FP = 0** on 345 legitimate test rows. State what that zero does and does not establish about the false-alarm rate the bank would see on 284,807 transactions. **(3 pts)**
4. **Two deployment risks**, each with the specific quantity you would monitor in production to detect it. **(4 pts)**

A generic essay about machine learning that does not use the numbers above cannot score above 6.

---

**End of Exam**

**Good Luck!**
