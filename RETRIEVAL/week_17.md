# Retrieval Quiz — Week 17

**Week 17 of 35 · Course 06 — AIAT 116 (Artificial Intelligence Ethics)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The lesson's epsilon sweep prints the private count's error as a share of the true answer for the 212-patient cohort and the 29-patient subgroup:

```
 epsilon    cohort (212)   subgroup (29)    ratio
     0.5            0.9%            7.8%     8.2x
     5.0            0.1%            0.6%     6.2x
```

A colleague reads the ratio column and concludes that the subgroup must be receiving a noisier draw from the mechanism. What actually produces this pattern?

A) A count over 29 patients has higher sensitivity than one over 212, because one patient is a larger fraction of the group, so the mechanism deliberately draws wider noise to protect the subgroup  
B) The subgroup count is an estimate from fewer records, so its ordinary sampling error adds to the privacy noise and inflates its share of the answer  
C) Laplace noise is drawn in proportion to the true answer, so the subgroup gets smaller absolute noise and the larger share is a rounding effect in the printed table  
D) The Laplace scale is sensitivity divided by epsilon, with no term for group size, so both counts get noise of the same size and the smaller answer absorbs it as a larger share  

---

### Question 2

A colleague drafts one line for the model card: "mean |SHAP| for `is_female` is **2.2×** that of the next feature (`Fare`), so the model's reliance on sex is uniform across passengers." You recompute the same quantity *within* each ticket class on the **223** held-out passengers. Reliance ranks **2nd class > 1st class > 3rd class**, the highest class is **1.83×** the lowest, and the real women-minus-men survival gap in the manifest ranks the classes in the same order. What should the line say instead?

A) Keep the 2.2× line exactly as written: the class ranking matches the real survival gap, which shows the global figure tracks the historical data correctly and needs no caveat about subgroups  
B) Replace it with the figure for the class where reliance is strongest, since a model card should disclose the worst case the model exhibits rather than an average  
C) Drop the SHAP figures: with 223 test passengers split three ways the per-class means are too thin to report, and a local waterfall for one passenger belongs there instead  
D) Reliance on sex is heterogeneous, 1.83× between the most- and least-affected class, so each class gets its own figure and the 2.2× ratio is labelled an average, not a per-passenger fact  

---

### Question 3

The Unit 2 screening model was trained on `Pclass, Age, SibSp, Parch, Fare, Embarked`, with `Sex` deliberately left out. A reviewer writes: "since the model never received sex, its positive-prediction rates for women and men can differ only by chance." The lesson's threshold storyboard (same model, same test set, only the cut-off moves) prints:

```
 threshold   female rate     male rate   DP gap
      0.20         0.660         0.497    0.163
      0.65         0.309         0.222    0.087
```

How should you answer the reviewer?

A) The gaps are cut-off artefacts: moving the threshold from 0.20 to 0.65 shrinks the gap from 0.163 to 0.087, so with a sensible cut-off the model is gender-blind as the reviewer says  
B) The reviewer is right: on the same test set the TPR gap is 0.047 and the FPR gap 0.031, so a model that passes equalized odds cannot be carrying sex through proxies  
C) The model's scores separate women from men through fare, class and family size, so the rates differ at any cut-off; dropping the column removed the label, not the information  
D) Unequal group sizes in the test set (97 women against 171 men) make different rates expected, so the gap is not evidence of proxies in the features  

---

### Question 4

The Unit 2 outliers lesson profiled the cleaned **889**-row `Fare` column and printed mean **32.10**, median **14.45**, quartiles **7.90** to **31.00** and a maximum of **512.33**. Its IQR rule flagged **114** fares (12.8% of passengers), **102** of them first class. A colleague's slide carries one line: "average fare: 32.10 pounds". Which revision does that profiling support?

A) Keep 32.10 but recompute it after dropping the 114 IQR-flagged fares first, so the mean then describes the typical passenger rather than the first-class tail  
B) Replace it with the median 14.45 and the 7.90 to 31.00 quartile range, and say the column is right-skewed, since 32.10 sits above the third quartile  
C) Standardise `Fare` to mean 0 and standard deviation 1 before quoting the average, so the first-class tail no longer pulls the reported figure away from the centre of the column  
D) Keep 32.10 and add the standard deviation 49.70, so readers can see the spread around the average and judge the typical fare for themselves  

---

### Question 5

The Unit 1 cuDF lesson could not run its GPU cells; it printed `cuDF NOT available on this machine (no NVIDIA GPU / RAPIDS not installed)` and showed this reference code instead:

```
df_cudf = cudf.from_pandas(df_pandas)             # move the same real frame to the GPU
df_cudf.groupby('label')['flow_duration'].mean()  # same groupby syntax
```

On the CPU the groupby + sum + mean took **0.001 s** on **14,015** rows, while reading the file took **0.012 s**. A classmate on a Colab GPU runtime runs the two lines above and they work without edits. What makes the unchanged `groupby` line execute on the GPU?

A) A GPU runtime lets the ordinary pandas library execute on the GPU, so the `from_pandas` line is cosmetic and the unchanged pandas code would have been accelerated there anyway  
B) Dask's scheduler notices the attached GPU and sends the groupby's partitions to it; cuDF is simply the name those partitions take once on the device  
C) cuDF re-implements the pandas DataFrame API method for method on CUDA; `from_pandas` copies the frame into GPU memory and the familiar method names then execute there  
D) Numba's `@jit` is applied inside cuDF to compile each pandas method into a CUDA kernel at call time, so the method names stay put while each call is compiled first  

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
