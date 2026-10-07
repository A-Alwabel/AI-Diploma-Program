# Retrieval Quiz — Week 15

**Week 15 of 35 · Course 05 — AIAT 115 (Scalable Data Science)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The Dask lesson's per-operation table on the 14,015-flow CIC-IDS2017 sample reads:

```
Filter   pandas 0.0005 s | Dask 0.0105 s -> faster here: pandas
Sort     pandas 0.0007 s | Dask 0.0094 s -> faster here: pandas
```

Its closing note adds that pandas was only in the race because the code read **5 of the file's 79 columns**, and that the 708 MB original is about **165x** this sample. A teammate reads the table as proof that Dask is simply a slower pandas. Which conclusion do the printed timings and the note together support?

A) Dask's case is size, not speed: once a file is too big to materialise, `dd.read_csv` still works partition by partition where `pd.read_csv` fails, and this sample cannot show that  
B) Dask lost because 14,015 rows are too few to spread across cores; with more cores on the same sample, parallel partitions would pull the 0.0105 s filter below pandas's 0.0005 s  
C) Dask lost on filter and sort but gains on operations that move rows between partitions, such as a merge or a high-cardinality groupby, so the ranking depends on which operation you time  
D) Dask lost because reading 5 columns is cheap; requesting the full 79 would let Dask parse the columns in parallel and overtake pandas even on this sample  

---

### Question 2

In the same Dask lesson two consecutive calls behaved differently. `df_dask.head()` printed five real BENIGN flows straight away, but `df_dask['Flow Duration'].mean()` printed

```
<dask_expr.expr.Scalar: expr=(...)['Flow Duration'].mean(), dtype=float64>
   ^ that is a task graph, not a number
```

For comparison, `pd.read_csv` had already returned in **0.01 s** with all **14,015** rows in memory. Why did `head()` hand back rows while `mean()` handed back an object?

A) `head()` is served from rows that `dd.read_csv` loaded during its 0.003 s open; `mean()` ignores those rows because a Scalar result is recomputed from disk on each `.compute()`  
B) `head()` is not a reduction, so it returns a pandas object; `mean()` is a reduction whose value has been computed but is stored as a Scalar until `.compute()` casts it to float64  
C) `head()` needs the first partition alone, so Dask reads just that one and returns real rows; `mean()` needs each of the four partitions, so it stays a graph node until `.compute()` runs it  
D) `head()` fits inside Dask's per-partition memory budget, so it runs at once; a mean across four 1 MB partitions would exceed that budget, so Dask defers it until it can spill partitions to disk  

---

### Question 3

Course 05 Unit 4 called train_test_split before fitting each model. What is that call for?

A) It holds back rows the model does not train on, so the score on them estimates unseen-data performance  
B) It shortens training, because the model is fitted on a fraction of the rows instead of on all of them at once  
C) It removes rows whose values lie outside the usual range, which would otherwise distort the fit  
D) It balances the classes, so the training half and the testing half hold equal numbers of each label  

---

### Question 4

Unit 3's KNN lesson splits its card transactions into 250 training and 63 test rows and prints, before any scaling:

```
Std of first feature (Time): 46331.17
Std of Amount feature: 215.28
```

The figure caption adds that on a log axis `Time` stands about four orders of magnitude above the V1–V28 columns, and `Amount` about two. A classmate proposes a shortcut: delete `Time`, skip `StandardScaler`, and fit KNN on the remaining 29 raw columns, "since the one problem column is gone." What does the lesson's evidence say will happen to the distances KNN computes?

A) With `Time` removed the remaining columns sit on comparable scales, so the shortcut does the same job `StandardScaler` would have done  
B) Dropping `Time` discards the column that dominated the distance, which is the model's strongest fraud signal, so the fit gets worse for a different reason  
C) KNN compares the ranking of distances rather than their raw size, so a column's standard deviation cannot change which rows come out nearest  
D) `Amount` inherits the role `Time` played: its spread sits about two orders of magnitude above V1–V28, so it now decides who counts as a neighbour  

---

### Question 5

Unit 4's K-Means sweep over the 1,994 scaled communities prints, among its rows:

```
K=7: Inertia=2145.23, Silhouette=0.2970
K=9: Inertia=1824.09, Silhouette=0.3008
```

A colleague picks K = 9: "it beats K = 7 on silhouette *and* on inertia - for once both criteria agree, so the data has decided." The lesson's own elbow landed on K = 4, and the lesson clustered at K = 3. What is the right response?

A) Inertia falls with each added cluster by construction, and a third-decimal silhouette bump is no ranking, so K is still settled by what the clusters are for  
B) The colleague is right: when the inertia criterion and the silhouette criterion point the same way, the data has chosen K and no judgement is needed  
C) K = 2 should stand: its silhouette of 0.3967 is the highest in the sweep, and the global peak outranks any comparison between neighbouring rows  
D) K = 4 should stand: the elbow was located geometrically, from the chord between the first and last points of the curve, which makes it a measurement rather than a judgement  

---

### Question 6

The same lesson prints two different ways of pushing the fraud model to flag more of the 3,200 test transactions - lowering the cut on the original model, and refitting with `class_weight='balanced'`:

```
cut 0.1 (original model):   caught 4   missed 2   false alarms 6    recall 0.6667   precision 0.4000
class_weight='balanced':    caught 3   missed 3   false alarms 18   recall 0.5000   precision 0.1429
```

A colleague reads the second line and concludes that the weighted refit is "the more aggressive model, so it must be the one catching more fraud." What do the two lines establish?

A) Recall sat at 0.5000 because 'balanced' is a mild preset; a hand-set weight on class 1 would carry recall past the 0.6667 the lower cut reached  
B) Flagging more is not finding more: 18 alarms bought 3 frauds where 6 alarms bought 4, so the weighting moved the operating point without adding signal  
C) The precision collapse to 0.1429 is the minority class being overfitted by the refit, which the threshold change avoids because the fitted model is left untouched  
D) Both rows fall below the 0.9981 that labelling each row legitimate scores, so the default 0.5 cut, which matches it, remains the model to keep  

---

### Question 7

Course 01 sorted AI systems by how broad their competence is. Which kind is actually built and deployed today?

A) General AI - one system that transfers its competence across unrelated tasks the way a person does  
B) Self-aware AI - a system with an internal model of its own mental states and its own interests  
C) Narrow AI - a system built for one task, which performs at or above human level inside that task  
D) Superintelligent AI - a system exceeding the best human performance across essentially all domains  

---

### Question 8

What distinguishes a generative AI system from the classifiers Course 01 built earlier?

A) It sorts each input into one of a fixed set of categories it was shown during training  
B) It produces new content - text, an image, audio - that was not present in its training set  
C) It forecasts a future value of a series from the values recorded before it  
D) It retrieves the stored training example closest to the input and returns that example unchanged  

---

### Question 9

You want to compute A @ B where A has shape (64, 128). What has to be true of B's shape?

A) B has 64 rows, matching A's row count, and the resulting product then has as many columns as B has  
B) B has shape (64, 128) as well, since the two matrices are combined entry by entry  
C) B is square, because a non-square second matrix leaves the product's shape undefined  
D) B has 128 rows, matching A's column count, and the product then has shape (64, B's columns)  

---

### Question 10

Course 02 ran simulated annealing with a cooling schedule. What does the temperature parameter do?

A) It counts the iterations that still remain, so the run halts at the moment the temperature reaches zero  
B) It sets how readily a move to a worse solution is accepted, and that willingness falls as it cools  
C) It scales the size of each proposed move, so a hot run jumps further across the search space  
D) It records the value of the best solution found so far, against which each proposal is compared  

---
