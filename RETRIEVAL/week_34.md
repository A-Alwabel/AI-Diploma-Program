# Cumulative Retrieval Quiz — Week 34

**Programme week 34 of 35 · Course 12 — AIAT 126 (Graduation Project), Units 2–4.**
**Taken in session 136, in the final 15 minutes.**

---

**How this works**

- **15 minutes, in class, at the END of the session.** 7 minutes to answer, then 8 minutes in which
  your instructor works the correct answers aloud.
- **Not graded.** No mark from this paper reaches your capstone milestone gates.
- **Ten items.** Three on this week and last week, three from about a month ago, four from earlier in
  the programme.
- Write the **letter only**. Closed book. One best answer per item.

---

## Part A — This week and last week (Course 12, Graduation Project)

### Item 1
The Unit 2 design primer says a capstone system design document answers **five questions**. Which of
the following is **not** one of them?

A) What are the components of your system, and what does each of them do?
B) In what order does data move between the components you have listed?
C) What could block you — licences, APIs, compute, imbalanced data — and what do you depend on?
D) What is the projected annual cloud hosting cost of the deployed system?

---

### Item 2
The Unit 3 grid search ran over a grid of 3 × 4 × 3 × 3 = **108 parameter combinations** with `cv=5`.
How many **model fits** did that require?

A) 108 fits — one per parameter combination
B) 540 fits — each of the 108 combinations × 5 folds
C) 216 fits — 108 combinations × 2, train and validate
D) 5 fits — one per cross-validation fold

---

### Item 3
In that same Unit 3 run the tuned model reached validation accuracy **0.8950** against the baseline's
**0.9050**, while the cross-validated F1 that the search actually optimised rose from **0.8888 to
0.8924**. Which response does the notebook teach?

A) Report it as it stands, check the criterion the search optimised, keep the baseline
B) Re-run the search with fresh random seeds until the tuned model comes out ahead of it
C) Score both models on the held-out test set and let that comparison break the tie
D) Drop the baseline from the report so that the results read consistently

---

## Part B — About a month ago (Course 11, AI Model Deployment)

### Item 4
You have a trained scikit-learn model. It must be called from a Java backend service and must also run
inside a mobile app that hosts no Python interpreter. Which packaging choice makes that possible?

A) ONNX, because the graph runs in an ONNX runtime with no Python present
B) `joblib` with `compress=3`, because it produces the smallest artifact of the four
C) `pickle`, because Python runs on all the major operating systems
D) JSON of the learned parameters, because most languages parse JSON

---

### Item 5
Unit 1 put a model behind an HTTP endpoint instead of importing it into the calling program. What is
the main advantage of a REST API for model serving?

A) Lower latency than an in-process `model.predict()` call
B) Automatic validation of requests against the model's schema
C) Automatic scaling of the service as request volume grows
D) A standardized, language-neutral interface that scales out

---

### Item 6
Unit 3 compared cloud hosting tiers for a model endpoint. When is **serverless** compute (AWS Lambda,
GCP Cloud Run) the right choice?

A) When each request needs a GPU, since the platform attaches one for the call
B) When the response budget is 10 ms, since scaling to zero removes queueing between requests
C) When traffic is low or unpredictable and you would rather pay per request than run a server
D) When peak throughput matters most, because a managed runtime outruns a container you built yourself

---

## Part C — Earlier in the programme

### Item 7 — Course 01, Introduction to AI and Applications
Unit 2 trained a classifier on labelled patient records and then clustered the same records with no
labels at all. What is the main difference between supervised and unsupervised learning?

A) Supervised learning trains on examples with a target; unsupervised learning has none
B) Supervised learning predicts numbers, while unsupervised learning predicts categories
C) Supervised learning runs faster, because a labelled dataset needs fewer passes
D) Supervised learning uses neural networks, and unsupervised learning uses clustering

---

### Item 8 — Course 02, Python for Artificial Intelligence
A triage knowledge base holds 4,000 recorded patient facts and 300 rules. A clinician needs one
answer: *should Patient 7 be flagged for sepsis?* Which inference strategy fits this request, and why?

A) Forward chaining: firing the rules in the order they were written is what makes a conclusion sound
B) Backward chaining: it starts from this one goal and expands just the rules that bear on the case
C) Backward chaining: it can withdraw a conclusion when a later fact turns out to contradict it
D) Forward chaining: it derives the consequences of the 4,000 facts, and this answer is among them

---

### Item 9 — Course 05, Scalable Data Science
You must compute two figures from a 40 GB `sales.csv` on a laptop with 16 GB of RAM, using
`pd.read_csv(..., chunksize=...)`: **(i)** the mean `amount` per `category`, and **(ii)** the median
`amount` over the whole file. Which statement describes what one chunked pass can give you?

A) (i) exactly, by carrying a running sum and count per category; (ii) exactly, by taking one median per chunk and weighting those by chunk size
B) (i) exactly, by averaging the per-chunk category means at the end; (ii) exactly, because the median of the per-chunk medians is the file's median
C) Neither exactly: combining across chunks assumes equal chunk sizes, and the last chunk holds fewer rows
D) (i) exactly, by carrying a running sum and count per category; (ii) not from one pass — a median needs all the values at once

---

### Item 10 — Course 06, Ethics of Artificial Intelligence
A global SHAP chart reports a mean |SHAP| of **0.204** for the feature `is_female`. Computed *within*
ticket class, the same quantity is **0.300** in second class and **0.163** in third class. A regulator
asks how much the model relies on sex when it decides about **third-class** passengers. What is the
correct response?

A) Report 0.204, since it rests on far more data and is the more reliable estimate
B) Report 0.300 from second class, since a regulator should see the largest reliance on sex
C) Report 0.163, and state that the global 0.204 in fact describes none of the classes
D) Report that SHAP explains single predictions, so a per-class average is not usable here

---

**End of quiz — put your pen down and follow the worked answers.**
