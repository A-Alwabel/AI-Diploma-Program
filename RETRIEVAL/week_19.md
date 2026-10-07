# Retrieval Quiz — Week 19

**Week 19 of 35 · Course 07 — AIAT 121 (Natural Language Processing)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

An investigative newsroom has inherited an English-language document leak of the kind that opened Unit 3. No file has been annotated, the only machine is a laptop, and the editors want, for each file, the people, companies and dates it names. Which approach from this course gets there with the least work?

A) Vectorise the files with TF-IDF and fit `MultinomialNB`, treating each file as one document to be labelled  
B) Run `en_core_web_sm` over each file and read `doc.ents`, the pretrained NER that tagged 12 spans in the sample paragraph  
C) Prompt the local GPT-2 text-generation pipeline from Unit 4 to write out the names it notices in each file  
D) Fine-tune `AutoModelForSequenceClassification` from Hugging Face on the leaked files so that it learns the newsroom's own entity types  

---

### Question 2

Course 07 Unit 2 trained a small skip-gram model and then ranked words by cosine similarity between their vectors. Two word vectors score a cosine similarity close to **1.0**. What does that mean?

A) The two vectors point in nearly the same direction, so the model places the words in similar contexts  
B) The two vectors are close to orthogonal, which is what a similarity value near 1.0 records for a pair of words  
C) The two words appear side by side in the corpus, which is what cosine similarity counts  
D) One vector is about twice the length of the other, since cosine similarity compares magnitudes  

---

### Question 3

Unit 3's pipeline was `TfidfVectorizer(stop_words="english")` feeding `MultinomialNB()`. A teammate wants to replace the second stage and still get a *positive* or *negative* label for each of the 1,000 held-out reviews. Which replacement still does that job?

A) A Porter stemmer applied to each review before its text reaches the TF-IDF vectorizer  
B) A second `TfidfVectorizer` with a larger vocabulary, run on the output of the first one  
C) K-Means with two clusters, fitted on the same TF-IDF rows without ever looking at the review labels  
D) `LogisticRegression(max_iter=1000)`, fitted on the same 3,000 TF-IDF rows and their labels  

---

### Question 4

The Dask lesson's per-operation table on the 14,015-flow CIC-IDS2017 sample reads:

```
Filter   pandas 0.0005 s | Dask 0.0105 s -> faster here: pandas
Sort     pandas 0.0007 s | Dask 0.0094 s -> faster here: pandas
```

Its closing note adds that pandas was only in the race because the code read **5 of the file's 79 columns**, and that the 708 MB original is about **165x** this sample. A teammate reads the table as proof that Dask is simply a slower pandas. Which conclusion do the printed timings and the note together support?

A) Dask lost because 14,015 rows are too few to spread across cores; with more cores on the same sample, parallel partitions would pull the 0.0105 s filter below pandas's 0.0005 s  
B) Dask lost on filter and sort but gains on operations that move rows between partitions, such as a merge or a high-cardinality groupby, so the ranking depends on which operation you time  
C) Dask lost because reading 5 columns is cheap; requesting the full 79 would let Dask parse the columns in parallel and overtake pandas even on this sample  
D) Dask's case is size, not speed: once a file is too big to materialise, `dd.read_csv` still works partition by partition where `pd.read_csv` fails, and this sample cannot show that  

---

### Question 5

In the same Dask lesson two consecutive calls behaved differently. `df_dask.head()` printed five real BENIGN flows straight away, but `df_dask['Flow Duration'].mean()` printed

```
<dask_expr.expr.Scalar: expr=(...)['Flow Duration'].mean(), dtype=float64>
   ^ that is a task graph, not a number
```

For comparison, `pd.read_csv` had already returned in **0.01 s** with all **14,015** rows in memory. Why did `head()` hand back rows while `mean()` handed back an object?

A) `head()` needs the first partition alone, so Dask reads just that one and returns real rows; `mean()` needs each of the four partitions, so it stays a graph node until `.compute()` runs it  
B) `head()` is served from rows that `dd.read_csv` loaded during its 0.003 s open; `mean()` ignores those rows because a Scalar result is recomputed from disk on each `.compute()`  
C) `head()` is not a reduction, so it returns a pandas object; `mean()` is a reduction whose value has been computed but is stored as a Scalar until `.compute()` casts it to float64  
D) `head()` fits inside Dask's per-partition memory budget, so it runs at once; a mean across four 1 MB partitions would exceed that budget, so Dask defers it until it can spill partitions to disk  

---

### Question 6

The Unit 1 cuDF lesson could not run its GPU cells; it printed `cuDF NOT available on this machine (no NVIDIA GPU / RAPIDS not installed)` and showed this reference code instead:

```
df_cudf = cudf.from_pandas(df_pandas)             # move the same real frame to the GPU
df_cudf.groupby('label')['flow_duration'].mean()  # same groupby syntax
```

On the CPU the groupby + sum + mean took **0.001 s** on **14,015** rows, while reading the file took **0.012 s**. A classmate on a Colab GPU runtime runs the two lines above and they work without edits. What makes the unchanged `groupby` line execute on the GPU?

A) A GPU runtime lets the ordinary pandas library execute on the GPU, so the `from_pandas` line is cosmetic and the unchanged pandas code would have been accelerated there anyway  
B) cuDF re-implements the pandas DataFrame API method for method on CUDA; `from_pandas` copies the frame into GPU memory and the familiar method names then execute there  
C) Dask's scheduler notices the attached GPU and sends the groupby's partitions to it; cuDF is simply the name those partitions take once on the device  
D) Numba's `@jit` is applied inside cuDF to compile each pandas method into a CUDA kernel at call time, so the method names stay put while each call is compiled first  

---

### Question 7

The matrix-operations lesson redraws its fusion experiment on the 1,797 mean-centred digit images and adds a third route, `relu(X @ W1) @ W2`, with a ReLU between the two layers. The printed reading of the figure is:

```
Blue points (no activation): 2.0e-14 is the largest amount any of the 17,970 output numbers differs from the fused one-layer network.
Orange points (ReLU inserted): up to 11.8 away from the diagonal, on outputs that span roughly -19 to +18.
```

A classmate argues that the ReLU is a minor numerical detail and that the real lesson is which bracketing is cheaper. Which reading of these two printed gaps is correct?

A) Both gaps are rounding noise; the ReLU route sits further off because `max()` adds another rounded operation per entry  
B) The 2.0e-14 gap shows the layer-by-layer route drifts from the fused one, so even without a ReLU the two layers compute a slightly different function  
C) The 2.0e-14 gap says the two linear routes are one function; the 11.8 gap says the ReLU made a genuinely different model  
D) The orange points leave the diagonal because the digits were mean-centred, not because of the ReLU; on raw pixels the same ReLU would spread them as far  

---

### Question 8

The eigenvalues lesson notes that the raw USArrests features live on very different ranges — Murder spans 0.8–17.4 and Assault 45–337 arrests per 100,000 — and its figure note says that on raw units PC1 'points almost straight up: 99.8% of it is the Assault axis'. After standardizing, the printed feature variances are Murder = 1.02 and Assault = 1.02, and PC2 keeps 9.91% of the variance. A colleague wants to send the raw-units decomposition to a state governor because 'it explains far more of the variance'. Why is the standardized run the one to report?

A) Standardizing gives both features a variance of 1.02, which adds spread for PC1 to explain that the raw run lacked  
B) The 9.91% left to PC2 after standardizing shows the raw run had dropped its second component and summed over a single eigenvalue  
C) Because 99.8% of raw PC1 lies along Assault, the raw covariance matrix is close to singular and its eigenvalues cannot be trusted  
D) On raw units PC1 is nearly the Assault column renamed, so its variance figure describes the recording scale, not a crime pattern  

---

### Question 9

In Course 01 you built a small knowledge graph over family relations and queried it. What is a knowledge graph?

A) A neural network whose neurons are arranged as nodes and edges rather than as layers  
B) A search algorithm that walks a graph outward from a start node until it first meets a goal node  
C) A structure that stores entities as nodes and the relations between them as labelled edges  
D) An activation function applied over a graph of inputs to produce one scalar output  

---

### Question 10

The Unit 1 search notebook also printed the order in which A\* popped nodes on the same graph, with the `f = g + h` each one carried:

```
   #1  A   f=6  (g=0 + h=6)
   #2  C   f=5  (g=1 + h=4)
   #3  F   f=3  (g=2 + h=1)
   #4  B   f=6  (g=1 + h=5)
   #5  E   f=4  (g=2 + h=2)
   #6  G   f=3  (g=3 + h=0)
```

Its admissibility check also reported `C: h=4, h*=unreachable` and `F: h=1, h*=unreachable` — the branch A\* tried first cannot reach the goal at all, so two of the six expansions went to a dead end before the search came back to `B`. A student concludes: *"that wasted detour is what shows the heuristic is inadmissible."* How should the detour be read?

A) The detour is the evidence: an admissible heuristic steers A* straight toward the goal, so expanding a dead end means h must have overestimated somewhere  
B) The detour is not the evidence; h is inadmissible because the node-by-node check finds h above h* at A, B and E, whichever route the search took first  
C) The detour shows h behaved admissibly: C was popped at f=5 ahead of B at f=6, which is just the lowest-f-first order the optimality proof relies on  
D) The detour is beside the point because C and F have h*=unreachable, which makes h <= h* hold on that branch and settles the question in h's favour  

---
