# Cumulative Retrieval Quiz - Week 15

**Programme week 15 of 35 | Course 05 - AIAT 115 (Scalable Data Science)**

Taught this week: Unit 4 (machine learning, sessions 57-58) and Unit 5 (scaling, sessions 59-60).

---

## How this works

- **15 minutes, in class, at the END of session 60.** You answer for about 7 minutes; your instructor then works the correct answers aloud for about 8.
- **This is not graded.** No mark from this paper reaches your course grade, and it carries no weight in any of the six assessment lines.
- **The correct answers are worked immediately afterwards, in the room.** That worked correction is the part that does the teaching; a quiz that only returns a score is worth about a third less.
- Ten questions. Three are on material from this week or last, three on material from about a month ago, and four on material from earlier in the programme. Each earlier question carries the context it needs, so you are not being asked to recall a lesson cold.
- Write one letter per question. No calculator, no laptop, no notes - answering from memory is the whole point.

---

### Question 1
*taught this week or last | Course 05, Unit 5*

In Course 05 Unit 5 you measured pandas against Dask on the same 4.3 MB file. pandas ran the groupby in 0.0007 s against Dask's 0.0146 s, and pandas also won the whole job end to end: 0.01 s against 0.02 s. Given that measurement, what does a scaling tool such as Dask, PySpark or RAPIDS actually buy you?

A) Handling data that will not fit in one machine's memory, because the engine works over partitions rather than the whole file  
B) Reducing wall-clock time on a job whose data already fits in memory, because the partitions are scheduled in parallel across the cores  
C) Improving data quality, because an engine that partitions a file also validates and repairs the records as it reads them  
D) Lowering total cost, because a cluster of small commodity machines comes out cheaper than one machine with more memory  

---

### Question 2
*taught this week or last | Course 05, Unit 5*

In Course 05 Unit 5, dd.read_csv on the 4.3 MB sample returned in 0.003 s reporting 4 partitions of 1 MB each, and df['Flow Duration'].mean() then printed a dask_expr object instead of a number. It took a .compute() call to produce 15,409,254.17 - the same value pandas gave. What did Dask actually do?

A) The 0.003 s read the file into four partitions; mean() returned an object because each partition holds its own mean, which .compute() averages  
B) Almost nothing had happened yet: dd.read_csv inferred the schema and stopped there, and mean() added a node to a task graph that .compute() then ran  
C) mean() returned an object because 4.3 MB exceeds the memory Dask allows per partition, so .compute() spills the partitions to disk and reads them back  
D) The 0.003 s read the file into four partitions; mean() returned an object because Dask types results lazily, and .compute() casts it  

---

### Question 3
*taught this week or last | Course 05, Unit 4*

Course 05 Unit 4 called train_test_split before fitting each model. What is that call for?

A) It holds back rows the model does not train on, so the score on them estimates unseen-data performance  
B) It shortens training, because the model is fitted on a fraction of the rows instead of on all of them at once  
C) It removes rows whose values lie outside the usual range, which would otherwise distort the fit  
D) It balances the classes, so the training half and the testing half hold equal numbers of each label  

---

### Question 4
*taught about a month ago | Course 04, Unit 3*

Course 04 Unit 3's KNN lesson fits the same model twice on the same 313 real card transactions. Without scaling it scores accuracy 0.9048; with StandardScaler it scores 0.9683. The lesson also prints that the Time column alone contributes 99.9978% of the raw squared distance between two transactions (Time std 46,331.2, against a median feature std of 1.302). What does that 99.9978% figure explain?

A) Unscaled, 'nearest neighbour' means roughly 'happened at a similar moment', so what V1-V28 know is drowned out  
B) The V1-V28 columns barely vary across these rows, so they contribute almost nothing to the distances the model computes  
C) Time is the most predictive feature of fraud here, so scaling it down discards the best signal  
D) StandardScaler dropped Time from the feature set, and removing that one dominant column is what lifted accuracy by 6.35 points  

---

### Question 5
*taught about a month ago | Course 04, Unit 4*

Course 04 Unit 4 clusters 1,994 communities on 4 scaled crime features and prints:

```
K=2   Inertia=5347.86   Silhouette=0.3967       K=6    Inertia=2398.46   Silhouette=0.2954
K=3   Inertia=4041.38   Silhouette=0.3134       K=8    Inertia=1970.75   Silhouette=0.3007
K=4   Inertia=3124.93   Silhouette=0.3153       K=10   Inertia=1720.82   Silhouette=0.2941
```

The elbow falls at K = 4; the silhouette peaks at K = 2; the lesson itself clusters at K = 3. How should K be settled?

A) Take K = 10: it posts the lowest inertia anywhere in the table, and lower inertia means tighter clusters  
B) Take K = 2: the silhouette is the score that measures separation, so it settles the question  
C) The disagreement is a symptom of unscaled features; rescaling the four crime columns would make the criteria converge  
D) The two criteria measure different things and disagree, so K is settled by what the clusters are for  

---

### Question 6
*taught about a month ago | Course 04, Unit 3*

The same lesson refits the model with class_weight='balanced' and prints the change on the test set:

```
Fraud caught (TP):   3 -> 3       Fraud missed (FN):   3 -> 3
False alarms (FP):   3 -> 18      Legit cleared (TN):  3191 -> 3176
```

Precision 0.5000 -> 0.1429, recall 0.5000 -> 0.5000, accuracy 0.9981 -> 0.9934. What should the analyst conclude?

A) Recall did not move because the weighting was too weak; a larger manual weight on class 1 would lift it  
B) Precision falling from 0.50 to 0.14 is the signature of a model overfitting the minority class it was weighted towards  
C) The weighting bought 15 extra false alarms and no extra fraud: it moved the operating point, not the information  
D) Accuracy fell from 0.9981 to 0.9934, so the balanced model is the worse of the two and should be dropped  

---

### Question 7
*taught eight or more weeks ago | Course 01, Unit 1*

Course 01 sorted AI systems by how broad their competence is. Which kind is actually built and deployed today?

A) General AI - one system that transfers its competence across unrelated tasks the way a person does  
B) Self-aware AI - a system with an internal model of its own mental states and its own interests  
C) Narrow AI - a system built for one task, which performs at or above human level inside that task  
D) Superintelligent AI - a system exceeding the best human performance across essentially all domains  

---

### Question 8
*taught eight or more weeks ago | Course 01, Unit 5*

What distinguishes a generative AI system from the classifiers Course 01 built earlier?

A) It sorts each input into one of a fixed set of categories it was shown during training  
B) It produces new content - text, an image, audio - that was not present in its training set  
C) It forecasts a future value of a series from the values recorded before it  
D) It retrieves the stored training example closest to the input and returns that example unchanged  

---

### Question 9
*taught eight or more weeks ago | Course 03, Unit 1*

You want to compute A @ B where A has shape (64, 128). What has to be true of B's shape?

A) B has 64 rows, matching A's row count, and the resulting product then has as many columns as B has  
B) B has shape (64, 128) as well, since the two matrices are combined entry by entry  
C) B is square, because a non-square second matrix leaves the product's shape undefined  
D) B has 128 rows, matching A's column count, and the product then has shape (64, B's columns)  

---

### Question 10
*taught eight or more weeks ago | Course 02, Unit 4*

Course 02 ran simulated annealing with a cooling schedule. What does the temperature parameter do?

A) It counts the iterations that still remain, so the run halts at the moment the temperature reaches zero  
B) It sets how readily a move to a worse solution is accepted, and that willingness falls as it cools  
C) It scales the size of each proposed move, so a hot run jumps further across the search space  
D) It records the value of the best solution found so far, against which each proposal is compared  

---

**Answers: worked aloud by your instructor in the eight minutes after you hand this back. Nothing to submit, nothing to mark.**
