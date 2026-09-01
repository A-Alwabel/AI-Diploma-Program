# Final Exam: Mathematics and Probability for Machine Learning
## AIAT 113

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. Show your work for partial credit.

**Marking scheme:** Part 1 (Q1–Q6): 5 pts each = 30. Part 2 (Q7–Q9): 10 pts each = 30. Part 3 (Q10: 15 pts, Q11: 10 pts) = 25. Part 4 (Q12): 15 pts. **Total: 100.** Multiple-choice items are marked on the chosen letter alone and carry no partial credit; every other question carries partial credit for correct working.

Several questions quote figures printed by the course notebooks. The figures are given to you — you are being asked what they mean, not to reproduce them from memory.

---

## Part 1: Multiple Choice (30 points)

### Question 1 (5 points)
**CLO1, CLO2:** Unit 1 computes the same two-layer transformation of the same data two ways: Route A as `(X @ W1) @ W2`, using 8,510,592 scalar multiplications, and Route B as `X @ (W1 @ W2)`, using 1,191,040. The largest disagreement between the two outputs is 1.33e-14. What does this establish about a two-layer network with no activation function between the layers?

A) Route B is cheaper because it drops the hidden layer, so it returns an approximation rather than the exact output  
B) The 1.33e-14 disagreement shows the two routes compute different functions, so the order the products are taken in matters  
C) The two layers can be replaced by one layer with weight matrix `W1 @ W2` without changing the function computed  
D) The second layer re-weights the first layer's outputs, so stacking the two adds expressive power a single layer lacks

---

### Question 2 (5 points)
**CLO2, CLO4:** On the 50-state USArrests data (Murder, Assault), Unit 1 eigen-decomposes the covariance matrix twice.

- **Standardized:** eigenvalues 1.8019 and 0.1981; PC1 = +0.707×Murder +0.707×Assault; PC1 explains 90.09% of the variance.
- **Raw units:** feature variances Murder 18.97 and Assault 6945.17; PC1 = +0.042×Murder +0.999×Assault; PC1 explains 99.90% of the variance.

Why is the raw-units 99.90% the less informative of the two figures?

A) On raw units PC1 follows Assault, whose variance is 6945 against Murder's 19, so it reports the measuring scale  
B) The raw-units run keeps one component while the standardized run keeps two, so the two percentages count different totals  
C) Standardizing increases the variance available to PC1, so 90.09% of standardized variance carries more information than the raw 99.90%  
D) A first component above 99% means the raw covariance matrix is singular, which makes its second eigenvalue unreliable

---

### Question 3 (5 points)
**CLO3:** On 89 held-out diabetes patients, Unit 3 prints MAE 42.79, RMSE 53.85, and a mean signed error of −3.91, and reports that the 10 worst-predicted patients carry 44.3% of the total squared error. What does the gap between MAE and RMSE tell you about this model?

A) The model over-predicts by roughly 11 units on each patient, which is what the gap between the two metrics measures  
B) The model accounts for 53.85% of the variation in the targets, which is the quantity a root-mean-squared error reports  
C) RMSE and MAE are on different scales, so RMSE has to be squared before the two numbers can be compared  
D) A small group of large errors inflates RMSE, so the typical patient is missed by about 43 rather than 54

---

### Question 4 (5 points)
**CLO4:** Unit 4 runs the same classifier on the 569-biopsy breast-cancer data, changing only how many principal components the classifier may see, and scores every row with the same 5-fold cross-validation:

| components | variance kept | 5-fold accuracy |
|---|---|---|
| 1 | 44.3% | 0.9121 |
| 2 | 63.2% | 0.9578 |
| 3 | 72.6% | 0.9491 |
| 5 | 84.7% | 0.9736 |
| 10 | 95.2% | 0.9807 |
| 20 | 99.6% | 0.9772 |
| 30 | 100.0% | 0.9789 |

The same classifier on all 30 raw features, with no PCA at all, scores 0.9789. Which conclusion do these numbers support?

A) Each component adds accuracy in proportion to the variance it carries, so keeping all 30 is the best choice  
B) Accuracy flattens long before variance does — k = 5 already reaches 0.9736 while keeping only 84.7% of the variance  
C) PCA hurt this classifier: the reduced models score below the 0.9789 that the 30 raw features reach on their own  
D) The dip at k = 3 shows the third component carries no variance, so it should be dropped from the model

---

### Question 5 (5 points)
**CLO5:** Minimising f(x) = x² from x = 5 for 30 steps, Unit 2 changes only the learning rate and prints: lr = 0.01 → x = 2.72742; lr = 0.1 → x = 0.0061897; lr = 0.9 → x = 0.0061897; lr = 1.0 → x = 5 with loss 25; lr = 1.1 → x = 1186.88. On a log axis the lr = 0.9 loss curve lies exactly on top of the lr = 0.1 curve. What does that coincidence tell you?

A) lr = 0.9 takes smaller steps than lr = 0.1, which is why the two runs finish at the same value of x  
B) A smoothly falling loss curve rules out instability, so the rate could be raised from 0.9 to 1.0 for speed  
C) The loss depends only on |x|, so a smoothly falling curve can still hide a run that crosses the minimum each step  
D) lr = 0.9 has settled into a second minimum of f that happens to sit at the same height as the first one

---

### Question 6 (5 points)
**CLO3:** Unit 5 draws a sample of n = 100 from the 714 recorded Titanic passenger ages and prints a 95% confidence interval of [26.8815, 32.7235] for the mean age. Repeating the whole study 2000 times, 96.4% of the intervals built this way contained the true population mean of 29.6991. Which statement do these results support?

A) There is a 95% probability that the true mean age of the 714 recorded passengers lies inside [26.88, 32.72]  
B) The 95% is a hit rate of the procedure across repeated studies, not a probability attached to this interval  
C) About 95% of the 714 recorded passenger ages fall inside [26.88, 32.72], which is the quantity the level counts  
D) Raising the level to 99% would narrow the interval, because greater confidence pins the true mean down more tightly

---

## Part 2: Short Answer Questions (30 points)

### Question 7 (10 points)
**CLO1, CLO2:** State the shape rule for multiplying an m×n matrix by an n×p matrix and explain how entry (i, j) of the product is formed. Then compute A × B, showing your working, for:

A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]]

---

### Question 8 (10 points)
**CLO3:** Answer both parts.

**(a)** Unit 3 fits a linear model to the diabetes data and, on 89 held-out patients, prints:

- mean of targets = 145.7753
- variance of targets = 5298.1517
- MSE = 2900.1936

Compute R² from these three numbers, showing the arithmetic, and state in one sentence what your R² says about this model compared with predicting every patient's target with the mean 145.78.

**(b)** Unit 5 draws n = 100 of the 714 recorded Titanic ages and prints a 95% confidence interval for the mean age of [26.8815, 32.7235]. Testing H₀: μ = 27 on the same sample gives p = 0.0599; testing H₀: μ = 33 gives p = 0.0322. State the decision at α = 0.05 for each hypothesis, and explain why the confidence interval and the two p-values are guaranteed to agree.

---

### Question 9 (10 points)
**CLO4:** Describe the steps of PCA, and explain the relationship between the eigenvalues of the covariance matrix and the principal components.

Unit 1's decomposition of the **standardized** USArrests covariance matrix prints eigenvalues 1.8019 and 0.1981. State the explained-variance ratio of the first principal component and show the arithmetic that produces it.

---

## Part 3: Practical/Coding Questions (25 points)

### Question 10 (15 points)
**CLO5:** Implement gradient descent to find the minimum of the function f(x) = x² + 2x + 1. Start with x = 5, learning rate = 0.1, and run for 10 iterations. Print the value of x at each iteration, and state where the iteration is heading relative to the true minimum of f.

---

### Question 11 (10 points)
**CLO4, CLO6:** Write Python code that reduces a feature matrix `X` (rows = samples, columns = features, on mixed measurement scales) to 2 dimensions with PCA. Your code must:

1. put the features on a common scale before the decomposition, and say in a comment why this step is not optional here;
2. fit PCA with 2 components and produce the transformed matrix;
3. report how much of the original variance the 2 components retain, and state the shape of the transformed matrix.

A from-scratch NumPy implementation and a scikit-learn implementation are both acceptable.

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
**CLO6:** You have a dataset with 100 features and want to reduce dimensionality for a machine learning model. Explain:

1. Which dimensionality reduction technique you would use and why
2. How you would determine the optimal number of dimensions
3. The trade-offs involved

---

**End of Exam**

**Good Luck!**
