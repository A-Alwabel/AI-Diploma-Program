# Retrieval Quiz — Week 13

**Week 13 of 35 · Course 05 — AIAT 115 (Scalable Data Science)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The Unit 2 outliers lesson profiled the cleaned **889**-row `Fare` column and printed mean **32.10**, median **14.45**, quartiles **7.90** to **31.00** and a maximum of **512.33**. Its IQR rule flagged **114** fares (12.8% of passengers), **102** of them first class. A colleague's slide carries one line: "average fare: 32.10 pounds". Which revision does that profiling support?

A) Keep 32.10 but recompute it after dropping the 114 IQR-flagged fares first, so the mean then describes the typical passenger rather than the first-class tail  
B) Standardise `Fare` to mean 0 and standard deviation 1 before quoting the average, so the first-class tail no longer pulls the reported figure away from the centre of the column  
C) Keep 32.10 and add the standard deviation 49.70, so readers can see the spread around the average and judge the typical fare for themselves  
D) Replace it with the median 14.45 and the 7.90 to 31.00 quartile range, and say the column is right-skewed, since 32.10 sits above the third quartile  

---

### Question 2

The Unit 1 cuDF lesson could not run its GPU cells; it printed `cuDF NOT available on this machine (no NVIDIA GPU / RAPIDS not installed)` and showed this reference code instead:

```
df_cudf = cudf.from_pandas(df_pandas)             # move the same real frame to the GPU
df_cudf.groupby('label')['flow_duration'].mean()  # same groupby syntax
```

On the CPU the groupby + sum + mean took **0.001 s** on **14,015** rows, while reading the file took **0.012 s**. A classmate on a Colab GPU runtime runs the two lines above and they work without edits. What makes the unchanged `groupby` line execute on the GPU?

A) A GPU runtime lets the ordinary pandas library execute on the GPU, so the `from_pandas` line is cosmetic and the unchanged pandas code would have been accelerated there anyway  
B) Dask's scheduler notices the attached GPU and sends the groupby's partitions to it; cuDF is simply the name those partitions take once on the device  
C) Numba's `@jit` is applied inside cuDF to compile each pandas method into a CUDA kernel at call time, so the method names stay put while each call is compiled first  
D) cuDF re-implements the pandas DataFrame API method for method on CUDA; `from_pandas` copies the frame into GPU memory and the familiar method names then execute there  

---

### Question 3

Course 05 Unit 2 flagged unusual Fare values on the Titanic manifest. Which rule is the IQR method?

A) Flag a value that appears fewer than five times in the column, since rare values are the unusual ones  
B) Flag a value lying more than 1.5 interquartile ranges below the first quartile or above the third  
C) Flag a value that differs from the column's mode, the column's most common entry  
D) Flag a value in the top or bottom 1% of the column, so 2% of rows are marked each time  

---

### Question 4

Course 04's KNN lesson scored 0.9048 without scaling and 0.9683 with StandardScaler on the same rows. What does StandardScaler do to a column?

A) It replaces each category in the column with a separate 0/1 indicator column, one per distinct value observed  
B) It clips the values that lie beyond 1.5 interquartile ranges from the nearer quartile  
C) It subtracts the column's mean and divides by its standard deviation, giving mean 0 and standard deviation 1  
D) It fills the column's missing entries with the column's mean, so no row has to be dropped  

---

### Question 5

Course 03 compared loss functions on the same predictions. Which task calls for cross-entropy loss?

A) Predicting a patient's blood-glucose reading, where the error is the number of units the model missed by  
B) Grouping patients into clusters, where no target label exists to compare a prediction against  
C) Reducing 30 measurements to 2 components, where the aim is to keep as much variance as possible  
D) Predicting which of three diseases a patient has, where the model outputs a probability per class  

---

### Question 6

Course 03 compared SGD and Adam on the same loss surface. What does Adam do that plain SGD does not?

A) It maintains a per-parameter step size from running estimates of the gradient's mean and its square  
B) It computes the gradient over the whole training set at each step rather than over a mini-batch of it  
C) It searches for the learning rate before training starts and holds that value for the whole run  
D) It applies the update to the parameters in a random order, which keeps the run from stalling  

---

### Question 7

Course 01's history lesson placed four landmarks on a timeline. Which one is normally taken as the birth of AI as a named research field?

A) Turing's 1950 paper, which proposed the imitation game as a test for machine thinking  
B) The 1956 Dartmouth summer workshop, where the term 'artificial intelligence' was adopted  
C) Deep Blue's 1997 match victory over the reigning world chess champion  
D) The 2022 public release of ChatGPT, which put a language model in front of the general public  

---

### Question 8

Course 01's expert system held three recorded facts about a patient and two IF-THEN rules. What does forward chaining do with them?

A) It starts from the goal 'does this patient have flu' and works backwards through the rules that could establish it  
B) It scores each rule with a probability and keeps the single most likely conclusion  
C) It starts from the recorded facts and fires whatever rules they satisfy, adding the conclusions as new facts  
D) It searches the rule base breadth-first, expanding rules in the order they were written down  

---

### Question 9

Course 02's genetic algorithm cycled through selection, crossover and mutation. What does crossover do?

A) It builds a child solution by taking part of its representation from one parent and part from another  
B) It keeps the highest-scoring members of the population and discards the rest before breeding  
C) It flips a small number of positions in one solution at random, to keep the population from converging  
D) It scores each candidate against the objective, so the population can be ranked before the next round  

---

### Question 10

Course 01 ran a small GAN at the end of the course. Which of these models can produce a new sample rather than a label for an existing one?

A) A decision tree, which routes an input down a chain of tests to a leaf  
B) A support vector machine, which places a maximum-margin boundary between two classes  
C) A GAN, whose generator is trained to output samples a discriminator accepts as real  
D) A logistic regression, which maps a weighted sum through a sigmoid to a probability  

---
