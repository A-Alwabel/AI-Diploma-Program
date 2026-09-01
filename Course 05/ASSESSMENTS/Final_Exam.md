# Final Exam: Scalable Data Science
## AIAT 115

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. Show your work for partial credit in Parts 2–5; Part 1 is marked right or wrong with no partial credit.

**Marking scheme:** Part 1 (Q1–Q6): 4 pts each = 24. Part 2 (Q7–Q9): 9 pts each = 27. Part 3 (Q10: 14 pts, Q11: 10 pts) = 24. Part 4 (Q12): 15 pts. Part 5 (Q13): 10 pts. **Total: 100.**

---

## Part 1: Multiple Choice (24 points)

### Question 1 (4 points)
**CLO2:** In Unit 5 you measured pandas against Dask on the same 4.3 MB file. pandas ran the groupby in 0.0007 s against Dask's 0.0146 s, and pandas also won the whole job end to end: 0.01 s against 0.02 s. Given that measurement, what does a scaling tool such as Dask, PySpark or RAPIDS actually buy you?

A) Handling data that will not fit in one machine's memory, because the engine works over partitions instead of materialising the whole file  
B) Reducing wall-clock time on a job whose data already fits in memory, because the partitions are scheduled in parallel across the available cores  
C) Improving data quality, because an engine that partitions a file also validates and repairs the records as it reads them  
D) Lowering total cost, because a cluster of small commodity machines comes out cheaper than one machine with more memory

---

### Question 2 (4 points)
**CLO2:** Your pipeline's `groupby` is saturating a single CPU core, and the machine has an NVIDIA GPU. Which of these course tools runs the same pandas-style DataFrame operations on that GPU with essentially unchanged code, and by what mechanism?

A) Numba, because its `@jit` decorator compiles a pandas `groupby` call into a CUDA kernel  
B) Dask, because it dispatches its DataFrame partitions to the GPU whenever one is present  
C) PySpark, because its executors move DataFrame operations onto the GPU when the cluster has one  
D) cuDF, because it re-implements the pandas DataFrame API, method for method, on top of CUDA

---

### Question 3 (4 points)
**CLO2:** In Unit 5, `dd.read_csv` on the 4.3 MB sample returned in 0.003 s reporting 4 partitions of 1 MB each, and `df['Flow Duration'].mean()` then printed a `dask_expr` object instead of a number. It took a `.compute()` call to produce 15,409,254.17 — the same value pandas gave. What did Dask actually do?

A) The 0.003 s read the file into four partitions; `mean()` returned an object because each of those partitions holds its own mean, and `.compute()` averages the four into the value shown  
B) Almost nothing had happened yet: `dd.read_csv` inferred the schema and stopped there, and `mean()` added a node to a task graph that `.compute()` then ran over the four partitions  
C) `mean()` returned an object because 4.3 MB exceeds the memory Dask allows per partition, so `.compute()` spills the partitions to disk and reads them back in order  
D) The 0.003 s read the file into four partitions; `mean()` returned an object because Dask types its results lazily, and `.compute()` casts that object to float64

---

### Question 4 (4 points)
**CLO1:** A colleague's bar chart of 2018 quarterly 911 call volume shows Q2 as a collapse and Q4 as a full recovery. The counts behind it are Q1 1,478, Q2 1,352, Q3 1,402, Q4 1,478 — a change of **+0.00%** across the year. No number was altered between the data and the chart. What produced the misleading chart, and what is the fix?

A) The bars were sorted by value rather than by quarter; re-order them chronologically so the trend reads correctly  
B) Counts were plotted where percentages were needed; convert each quarter to a percentage change from Q1  
C) The y-axis was truncated to start just below the smallest bar; start it at zero, or flag the zoom  
D) Four categories are too few for bars; a pie chart would show the quarters' shares more fairly

---

### Question 5 (4 points)
**CLO3:** In Unit 2 you profiled two columns of the same 891-row Titanic manifest. `Age` printed a skew of **0.53** and a median near **26**; `Fare` printed a skew of **4.79**, with most passengers in the first histogram bin and a few tickets reaching **512** pounds. A colleague's report quotes one "average" per column. What does the profiling step tell you to do, and why?

A) Report `Fare` by its median and quartiles and say the column is skewed, because a single mean describes almost nobody in that shape  
B) Report the mean for both columns, because the mean uses every row while the median throws away everything except the middle one  
C) Drop the tickets near 512 pounds as outliers first, because the mean of `Fare` becomes a fair summary once that tail is gone  
D) Standardise both columns to mean 0 and standard deviation 1 first, because scaling removes the skew and makes the two averages comparable

---

### Question 6 (4 points)
**CLO2:** You must compute two figures from a 40 GB `sales.csv` on a laptop with 16 GB of RAM, using `pd.read_csv(..., chunksize=...)`: **(i)** the mean `amount` per `category`, and **(ii)** the median `amount` over the whole file. Which statement correctly describes what one chunked pass can give you, and how?

A) (i) exactly, by carrying a running sum and a running count per category; (ii) exactly, by taking one median per chunk and averaging those medians in proportion to the number of rows in each chunk  
B) (i) exactly, by averaging the per-chunk category means at the end; (ii) exactly, because the median of the per-chunk medians is the median of the whole file  
C) (i) exactly, by carrying a running sum and a running count per category; (ii) not from one chunked pass — a median needs all the values at once, so it takes an approximation or another engine  
D) Neither exactly: combining results across chunks assumes the chunks hold equal numbers of rows, and here the last chunk holds fewer rows than all the ones before it

---

## Part 2: Short Answer Questions (27 points)

### Question 7 (9 points)
**CLO5:** Explain the data science lifecycle, from problem definition through deployment and monitoring. Name each major step and say in one line what it does.

---

### Question 8 (9 points)
**CLO2:** Compare pandas, Dask, and cuDF: where each one runs, what data size it suits, and when you would choose it for data processing. Then cite **one measured result from this course** where the "bigger" tool lost, and say what that result changes about how you choose.

---

### Question 9 (9 points)
**CLO1:** Answer both parts.

**(a)** State four data visualization best practices, and for each one say what it protects the reader from.

**(b)** In Unit 3 you saw a chart that drew one township in red and pushed the other four into grey. That is a deliberate decision about what the reader is allowed to notice. Give one situation where that decision is right and one where it is not, and say what distinguishes them.

---

## Part 3: Practical/Coding Questions (24 points)

### Question 10 (14 points)
**CLO2:** A 40 GB `sales.csv` with columns including `category` and `amount` will not fit in your machine's memory. Write Python that computes the **mean `amount` per `category`** by:
1. Reading the file in chunks
2. Processing each chunk
3. Combining the partial results correctly
4. Keeping memory bounded

Add a comment stating **why your combination step is correct** — that is, why it gives the same answer as running the calculation over the whole file at once.

---

### Question 11 (10 points)
**CLO1:** Build a 2×2 dashboard with matplotlib/seaborn for one dataset of your choice (state the dataset and the columns you use). Use four **different** plot types, covering:
- a distribution of one numeric column
- a comparison between categories
- a relationship between two numeric columns
- a correlation summary

Label every axis, title every panel, give the figure one overall title, and write one sentence per panel naming the question that panel answers.

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
**CLO2, CLO5:** Design a scalable data science solution for processing 10TB of customer data:
1. Data loading strategy
2. Processing approach (distributed vs GPU)
3. Visualization strategy
4. Performance optimization
5. Cost considerations

---

## Part 5: Evaluation, Deployment and Monitoring (10 points)

### Question 13 (10 points)
**CLO4:** Answer both parts.

**(a)** In Unit 4 you met a credit-card dataset in which **0.175%** of transactions are fraud (28 in the 16,000-row sample). A model that answers "legitimate" for every transaction is **99.83% accurate** on that sample. A trained classifier scores **93.13% accuracy** on the held-out test split. Which model would you ship, and why? Name two metrics you would report **instead of** accuracy, and say what each one tells you that accuracy does not.

**(b)** In Unit 5 a classifier frozen on 2016 data was scored month by month for 43 months. During the March–May 2020 lockdown its **accuracy rose** while its **F1 on the traffic class fell**. Explain how both can be true of the same unchanged model, and name two things you would monitor on a deployed model so that a failure like this is visible instead of hidden.

---

**End of Exam**

**Good Luck!**
