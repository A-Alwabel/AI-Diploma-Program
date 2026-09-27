# Retrieval Quiz — Week 19

**Week 19 of 35 · Course 07 — AIAT 121 (Natural Language Processing)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

You must extract PERSON, ORG and DATE mentions from 50,000 English news articles, on a CPU-only server, with **no labelled data**. Which tool from Course 07 does the job with the least work?

A) `TfidfVectorizer` with `MultinomialNB`, trained on the 50,000 articles  
B) spaCy's `en_core_web_sm` pipeline, whose NER already tags these entity types  
C) A local GPT-2 text-generation pipeline, prompted to list the entities in each article  
D) `AutoModelForSequenceClassification` from Hugging Face, fine-tuned on the articles  

---

### Question 2

Course 07 Unit 2 trained a small skip-gram model and then ranked words by cosine similarity between their vectors. Two word vectors score a cosine similarity close to **1.0**. What does that mean?

A) The two vectors point in nearly the same direction, so the model places the words in similar contexts  
B) The two vectors are close to orthogonal, which is what a similarity value near 1.0 records for a pair of words  
C) The two words appear side by side in the corpus, which is what cosine similarity counts  
D) One vector is about twice the length of the other, since cosine similarity compares magnitudes  

---

### Question 3

Which group lists three methods that can serve as the **classifier** in a text-classification pipeline?

A) TF-IDF, bag-of-words, Word2Vec  
B) Tokenization, stemming and lemmatization  
C) K-Means clustering, PCA, t-SNE  
D) Naive Bayes, Logistic Regression, SVM  

---

### Question 4

In Course 05 Unit 5 you measured pandas against Dask on the same 4.3 MB file. pandas ran the groupby in 0.0007 s against Dask's 0.0146 s, and pandas also won the whole job end to end: 0.01 s against 0.02 s. Given that measurement, what does a scaling tool such as Dask, PySpark or RAPIDS actually buy you?

A) Handling data that will not fit in one machine's memory, because the engine works over partitions instead of materialising the whole file  
B) Reducing wall-clock time on a job whose data already fits in memory, because the partitions are scheduled in parallel across the available cores  
C) Improving data quality, because an engine that partitions a file also validates and repairs the records as it reads them  
D) Lowering total cost, because a cluster of small commodity machines comes out cheaper than one machine with more memory  

---

### Question 5

In Course 05 Unit 5, `dd.read_csv` on the 4.3 MB sample returned in 0.003 s reporting 4 partitions of 1 MB each, and `df['Flow Duration'].mean()` then printed a `dask_expr` object instead of a number. It took a `.compute()` call to produce 15,409,254.17 — the same value pandas gave. What did Dask actually do?

A) The 0.003 s read the file into four partitions; `mean()` returned an object because each of those partitions holds its own mean, and `.compute()` averages the four into the value shown  
B) Almost nothing had happened yet: `dd.read_csv` inferred the schema and stopped there, and `mean()` added a node to a task graph that `.compute()` then ran over the four partitions  
C) `mean()` returned an object because 4.3 MB exceeds the memory Dask allows per partition, so `.compute()` spills the partitions to disk and reads them back in order  
D) The 0.003 s read the file into four partitions; `mean()` returned an object because Dask types its results lazily, and `.compute()` casts that object to float64  

---

### Question 6

Your pipeline's `groupby` is saturating a single CPU core, and the machine has an NVIDIA GPU. Which Course 05 tool runs the same pandas-style DataFrame operations on that GPU with essentially unchanged code, and by what mechanism?

A) Numba, because its `@jit` decorator compiles a pandas `groupby` call into a CUDA kernel  
B) Dask, because it dispatches its DataFrame partitions to the GPU whenever one is present  
C) PySpark, because its executors move DataFrame operations onto the GPU when the cluster has one  
D) cuDF, because it re-implements the pandas DataFrame API, method for method, on top of CUDA  

---

### Question 7

Course 03 Unit 1 computed the same two-layer transformation of the same data two ways: Route A as `(X @ W1) @ W2`, using 8,510,592 scalar multiplications, and Route B as `X @ (W1 @ W2)`, using 1,191,040. The largest disagreement between the two outputs was 1.33e-14. What does this establish about a two-layer network with no activation function between the layers?

A) Route B is cheaper because it drops the hidden layer, so it returns an approximation  
B) The 1.33e-14 disagreement shows the two routes compute different functions, so the order the products are taken in matters  
C) The two layers can be replaced by one layer with weight matrix `W1 @ W2` without changing the function computed  
D) The second layer re-weights the first layer's outputs, so stacking the two adds expressive power a single layer lacks  

---

### Question 8

On the 50-state USArrests data (Murder, Assault), Course 03 Unit 1 eigen-decomposed the covariance matrix twice.

- **Standardized:** eigenvalues 1.8019 and 0.1981; PC1 = +0.707×Murder +0.707×Assault; PC1 explains 90.09% of the variance.
- **Raw units:** feature variances Murder 18.97 and Assault 6945.17; PC1 = +0.042×Murder +0.999×Assault; PC1 explains 99.90% of the variance.

Why is the raw-units 99.90% the less informative of the two figures?

A) On raw units PC1 follows Assault, whose variance is 6945 against Murder's 19, so it reports the measuring scale  
B) The raw-units run keeps one component while the standardized run keeps two, so the totals differ  
C) Standardizing increases the variance available to PC1, so 90.09% of standardized variance carries more information than the raw 99.90%  
D) A first component above 99% means the raw covariance matrix is singular, which makes its second eigenvalue unreliable  

---

### Question 9

In Course 01 you built a small knowledge graph over family relations and queried it. What is a knowledge graph?

A) A neural network whose neurons are arranged as nodes and edges rather than as layers  
B) A search algorithm that walks a graph outward from a start node until it first meets a goal node  
C) A structure that stores entities as nodes and the relations between them as labelled edges  
D) An activation function applied over a graph of inputs to produce one scalar output  

---

### Question 10

Course 02 Unit 1 ran A\* with the heuristic `h(n) = |ord(n) - ord(goal)|` and checked it against the true remaining cost `h*`:

```
   A: h=6, h*=3  ->  OVERESTIMATES by 3
   B: h=5, h*=2  ->  OVERESTIMATES by 3
   E: h=2, h*=1  ->  OVERESTIMATES by 1
   G: h=0, h*=0  ->  OK
```

A\* then returned `A -> B -> E -> G`, which is the shortest path on that graph, having opened 6 of the 7 nodes (BFS opened 7). What does this run establish about the heuristic?

A) h is admissible, because the path A\* returned is in fact the shortest one available on this graph  
B) The overestimates are uniform across nodes, so they cancel and optimality still holds  
C) h is inadmissible, and that is what made A\* open 6 nodes where BFS had to open 7  
D) h overestimates, so the optimality proof did not apply — the shortest path came back anyway  

---
