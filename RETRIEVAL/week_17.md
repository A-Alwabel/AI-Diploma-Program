# Retrieval Quiz — Week 17

**Week 17 of 35 · Course 06 — AIAT 116 (Artificial Intelligence Ethics)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

In Course 06's differential privacy lesson, the Laplace mechanism at epsilon = 0.1 produced a mean absolute error of about 10 on a count of 212 patients (4.7% of the answer) and about 10 again on a count of 29 patients (34.2% of the answer). What does this tell you about deploying differential privacy?

A) The Laplace mechanism is unsuitable for small groups, which should be protected using k-anonymity instead of added noise  
B) Lowering epsilon further would shrink the error on the small subgroup, because epsilon is the mechanism's accuracy setting  
C) The small subgroup has fewer records to average over, so collecting more data there would close the gap  
D) Laplace noise scales with sensitivity and epsilon, not with the true answer, so one epsilon costs small groups more  

---

### Question 2

A global SHAP chart reports a mean |SHAP| of 0.204 for the feature is_female. Computed within ticket class, the same quantity is 0.300 in second class and 0.163 in third class. A regulator asks how much the model relies on sex when it decides about third-class passengers. What is the correct response?

A) Report 0.204, since it is computed on far more data and is therefore the more reliable estimate  
B) Report 0.163, and state that the global average of 0.204 in fact describes none of the three classes  
C) Report 0.300 from second class, since a regulator should be shown the largest reliance on sex the model has  
D) Report that SHAP explains single predictions, so a per-class average of SHAP values is not a usable figure  

---

### Question 3

A team removes the Sex column from a screening model's training data and reports that the system is now fair. On the held-out set the model's positive-prediction rate is 44.3% for women and 31.6% for men - a demographic parity difference of 0.128. What does this result show?

A) Removing Sex made the model blind to gender, so the remaining gap is not something the model itself produced  
B) Demographic parity is the wrong test here: on the same held-out set the equalized-odds gaps are small (TPR gap 0.047)  
C) The model rebuilt the group split from correlated features like fare and class, so deleting the column changed nothing  
D) The model satisfies demographic parity, since two applicants with identical inputs receive an identical decision from it  

---

### Question 4

In Course 05 Unit 2 you profiled two columns of the same 891-row Titanic manifest. Age printed a skew of 0.53 and a median near 26; Fare printed a skew of 4.79, with most passengers in the first histogram bin and a few tickets reaching 512 pounds. A colleague's report quotes one 'average' per column. What does the profiling step tell you to do, and why?

A) Report Fare by its median and quartiles and note that it is skewed, because one mean describes almost nobody in that shape  
B) Report the mean for both columns, because a mean is computed from the whole column while a median keeps just the middle value of it  
C) Drop the tickets near 512 pounds as outliers, because the mean of Fare becomes fair once that tail is gone  
D) Standardise both columns to mean 0 and standard deviation 1 first, because scaling removes the skew and makes the averages comparable  

---

### Question 5

Your pipeline's groupby is saturating a single CPU core, and the machine has an NVIDIA GPU. Which Course 05 tool runs the same pandas-style DataFrame operations on that GPU with essentially unchanged code, and by what mechanism?

A) Numba, because its @jit decorator compiles a pandas groupby call into a CUDA kernel  
B) Dask, because it dispatches its DataFrame partitions to the GPU whenever one is present  
C) PySpark, because its executors move DataFrame operations onto the GPU when the cluster has one  
D) cuDF, because it re-implements the pandas DataFrame API, method for method, on top of CUDA  

---

### Question 6

Course 05 Unit 2 flagged unusual Fare values on the Titanic manifest. Which rule is the IQR method?

A) Flag a value that appears fewer than five times in the column, since rare values are the unusual ones  
B) Flag a value lying more than 1.5 interquartile ranges below the first quartile or above the third  
C) Flag a value that differs from the column's mode, the column's most common entry  
D) Flag a value in the top or bottom 1% of the column, so 2% of rows are marked each time  

---

### Question 7

ReLU is the default activation in the networks Course 01 built. What does the name stand for, and what does the function do?

A) Random Linear Unit - it scales its input by a weight drawn fresh on each forward pass through the layer  
B) Rectified Linear Unit - it passes a positive input through unchanged and returns zero otherwise  
C) Recursive Linear Unit - it feeds its own previous output back in alongside the current input  
D) Regular Linear Unit - it returns the input unchanged, which keeps the layer's response linear  

---

### Question 8

How did Course 01 define the goal of artificial intelligence as a field?

A) To build machines that carry out tasks which would need intelligence if a person did them  
B) To remove human judgement from decisions, so that outcomes stop depending on which person decides  
C) To construct physical robots capable of moving through and acting on the world  
D) To replace human labour across the economy with systems that work without wages  

---

### Question 9

Course 03 decomposed the USArrests covariance matrix into eigenvalues and eigenvectors. What is an eigenvector of a matrix M?

A) A vector whose length M leaves unchanged, though it may turn the vector to point in a new direction  
B) A vector holding one row of M, which is why an n x n matrix has exactly n of them  
C) A vector M maps to a scalar multiple of itself, so its direction survives the transformation  
D) A vector of the variances of M's columns, ordered from the largest down to the smallest  

---

### Question 10

Course 02's logistic-regression model on the breast-tumour biopsies produced a score for each case that was then compared with a threshold. What does the sigmoid do in that model?

A) It squashes the unbounded weighted sum into the range 0 to 1, so the output reads as a probability  
B) It selects the threshold at which the two kinds of error are balanced against one another on the test set  
C) It measures the distance between the prediction and the label, which training then minimises  
D) It removes the non-linear terms from the weighted sum so the boundary comes out straight  

---
