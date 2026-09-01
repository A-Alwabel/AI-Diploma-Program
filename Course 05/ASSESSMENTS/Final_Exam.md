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

A) Handling large datasets efficiently  
B) Reducing the wall-clock time of a job whose data already fits in one machine's memory  
C) Improving data quality, because distributed engines validate records as they partition them  
D) Lowering total cost, because a cluster of small machines is cheaper than one large machine

---

### Question 2 (4 points)
**CLO2:** Your pipeline's `groupby` is saturating a single CPU core, and the machine has an NVIDIA GPU. Which of these course tools runs the same pandas-style DataFrame operations on that GPU with essentially unchanged code?

A) Numba  
B) Dask  
C) PySpark  
D) cuDF (RAPIDS)

---

### Question 3 (4 points)
**CLO2:** What does Dask provide?

A) A just-in-time compiler that turns Python loops into machine code  
B) Distributed computing for large datasets  
C) GPU execution of the pandas API, using the same method names  
D) A columnar file format that stores typed columns so you can read only the ones you need

---

### Question 4 (4 points)
**CLO1:** A colleague's bar chart of 2018 quarterly 911 call volume shows Q2 as a collapse and Q4 as a full recovery. The counts behind it are Q1 1,478, Q2 1,352, Q3 1,402, Q4 1,478 — a change of **+0.00%** across the year. No number was altered between the data and the chart. What produced the misleading chart, and what is the fix?

A) The bars were sorted by value instead of chronologically; re-order them by quarter  
B) Counts were plotted where percentages were needed; convert each quarter to a percentage change from Q1  
C) The y-axis was truncated to start just below the smallest bar; start it at zero, or flag the zoom clearly  
D) Four categories are too few for bars; a pie chart would show the quarters' shares more fairly

---

### Question 5 (4 points)
**CLO3:** What is the purpose of data profiling?

A) Removing missing values, duplicates and outliers so the table is ready to model  
B) Understanding data structure, quality, and patterns  
C) Computing summary statistics thorough enough that plotting the data becomes unnecessary  
D) Choosing the model family that will fit the data best

---

### Question 6 (4 points)
**CLO2:** You must compute two figures from a 40 GB `sales.csv` on a laptop with 16 GB of RAM, using `pd.read_csv(..., chunksize=...)`: **(i)** the mean `amount` per `category`, and **(ii)** the median `amount` over the whole file. Which statement is correct?

A) (i) can be computed exactly by carrying a running sum and a running count per category; (ii) cannot be obtained from one chunked pass, because a median needs all the values together — it takes an approximation, several passes, or a different engine  
B) Both can be computed exactly, provided each chunk's own result is averaged across the chunks at the end — that is what makes chunking equivalent to a single pass  
C) Both can be computed exactly, because the median of the per-chunk medians equals the median of the whole file  
D) Neither can be computed by chunking, because any statistic over a whole file requires a distributed engine such as Dask or Spark

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
