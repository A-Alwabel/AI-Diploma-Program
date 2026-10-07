# Retrieval Quiz — Week 34

**Week 34 of 35 · Course 12 — AIAT 126 (Graduation Project)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The Unit 2 design primer says a capstone system design document answers **five questions**. Which of the following is **not** one of them?

A) What are the components of your system, and what does each of them do?  
B) In what order does data move between the components you have listed?  
C) What could block you — licences, APIs, compute, imbalanced data — and what do you depend on?  
D) What is the projected annual cloud hosting cost of the deployed system?  

---

### Question 2

The Unit 3 grid search ran over a grid of 3 × 4 × 3 × 3 = **108 parameter combinations** with `cv=5`. How many **model fits** did that require?

A) 108 fits — one per parameter combination  
B) 540 fits — each of the 108 combinations × 5 folds  
C) 216 fits — 108 combinations × 2, train and validate  
D) 5 fits — one per cross-validation fold  

---

### Question 3

In that same Unit 3 run the tuned model reached validation accuracy **0.7933** against the baseline's **0.8045**, while the cross-validated F1 that the search actually optimised rose from **0.7347 to 0.7629**. Which response does the notebook teach?

A) Report it as it stands, check the criterion the search optimised, keep the baseline  
B) Re-run the search with fresh random seeds until the tuned model comes out ahead of it  
C) Score both models on the held-out test set and let that comparison break the tie  
D) Drop the baseline from the report so that the results read consistently  

---

### Question 4

Unit 1 lesson 02 wrote the same Iris RandomForest to disk four ways and printed:

```
format                  size (KB)  load (ms)
pickle                      170.6       0.59
joblib                      182.5       5.28
joblib (compress=3)          25.4       5.35
ONNX                         78.3       0.59
```

A teammate reads the table and says: "pickle ties for the fastest load, so send `iris_rf.pkl` to the gateway team." The gateway is a C++ service on a factory device with no Python installed. Which reply is right?

A) Send `iris_rf.pkl` (170.6 KB): it loads in 0.59 ms and C++ can read the bytes like any other file  
B) Send `iris_rf_compressed.joblib` (25.4 KB): on a constrained device the smallest artifact is the one to ship  
C) Send `iris_rf.onnx` (78.3 KB): a C++ ONNX runtime executes the saved graph without importing scikit-learn  
D) Send the forest's learned thresholds as JSON: C++ parses numbers natively, so no model runtime is needed  

---

### Question 5

In Unit 1 lesson 01, `wdbc-baseline` was wrapped in a FastAPI app and the notebook printed a ready-to-paste `curl -X POST http://localhost:8000/predict` carrying 30 JSON fields. The dashboard team writes JavaScript and the billing team writes Go; both want predictions. A colleague asks why they should call this endpoint instead of each loading `model.joblib` themselves. Which answer gives the benefit the lesson actually claims for serving over HTTP?

A) HTTP makes each prediction faster than the in-process call the lesson timed at 0.060 ms per call  
B) Behind HTTP, Flask returns `400` for a missing field on its own, so nobody has to write any validation code  
C) Once the model sits behind one address, extra worker processes are started by the API layer as traffic grows  
D) Any program that can send JSON to one address can use the model, whatever language it was written in  

---

### Question 6

Unit 3 compared cloud hosting tiers for a model endpoint. When is **serverless** compute (AWS Lambda, GCP Cloud Run) the right choice?

A) When each request needs a GPU, since the platform attaches one for the call  
B) When the response budget is 10 ms, since scaling to zero removes queueing between requests  
C) When traffic is low or unpredictable and you would rather pay per request than run a server  
D) When peak throughput matters most, because a managed runtime outruns a container you built yourself  

---

### Question 7

Unit 2 ran K-Means on 150 iris flowers with the species column hidden. The crosstab printed afterwards showed cluster 1 holding 50 setosa flowers and 0 of either other species. A classmate says: "a match that clean means K-Means obviously trained on the species labels." Which statement correctly describes what the clustering run was given?

A) It received the 4 measurements plus the species column, which is why cluster 1 lines up with setosa so exactly  
B) It received the 4 measurements per flower; the species column stayed hidden and was brought back afterwards to score the clusters  
C) It received the measurements and predicted a species category for each flower, so it was a classification model like the biopsy one  
D) It received the measurements and the labels but ignored them to finish faster, because fits without labels take fewer passes  

---

### Question 8

In the Unit 2 expert-system cell, three recorded observations about `Patient1` and two rules went in, and the run printed:

```
   BEFORE Forward Chaining:
      Facts: 3

  ➕ Added: Fact(Patient1, likely_has, Flu)
   ✅ Applied rule: Flu Diagnosis Rule
  ➕ Added: Fact(Patient1, recommend, Rest)
   ✅ Applied rule: Flu Treatment Rule

✅ Forward chaining complete! (2 iterations)
   (Stopped because no more new facts can be derived)

   AFTER Forward Chaining:
      Facts: 5
```

A clinic now wants the system to run with no particular question in mind: *each time a nurse records a new observation, surface whatever recommendations now follow for that patient.* Which chaining direction suits that job, and what in the printout shows why?

A) Forward chaining: data-driven, firing whichever rules the recorded facts satisfy until a pass adds no new fact — the loop that stopped above after 2 iterations  
B) Forward chaining: the Flu Diagnosis Rule was entered before the Flu Treatment Rule, and firing rules in the order they were written is what keeps the chain valid  
C) Backward chaining: it would prove `recommend Rest` for one patient at a time, and a focused proof costs less than deriving facts even when no goal has been named  
D) Backward chaining: if a later observation contradicts `likely_has Flu`, it can take back the `Rest` recommendation, which a forward chainer has no way to do  

---

### Question 9

The Unit 5 chunking lesson streamed the **14,015**-flow sample in **10 chunks of 1,500** rows (the last chunk held **515**) and printed a global mean of **6.84** forward packets per flow from a running total of **95,877** packets. A colleague wants two further figures from that same single pass: **(a)** the largest `Flow Duration` recorded for each `Label`, and **(b)** the quartiles of `Flow Duration` across the whole file. Which of the two can one chunked pass deliver exactly, and how?

A) (a) exactly, by keeping per-chunk maxima for each label; (b) exactly, by computing the quartiles of each chunk and weighting the ten results by chunk size so that the 515-row final chunk counts for less  
B) (a) approximately at best, because a rare label such as Heartbleed may fall inside a single chunk and its maximum is then compared against no other chunk; (b) exactly, by taking the quartiles of the per-chunk quartiles  
C) Neither exactly: an uneven final chunk of 515 rows breaks any statistic merged across chunks, so both need the file in memory at once, as the lesson's 1.3 MB measurement did  
D) (a) exactly, by keeping each label's largest value seen so far and updating it per chunk; (b) not from one pass, since quartiles are rank statistics that need the whole ordering, so use t-digest or a real engine  

---

### Question 10

A colleague drafts one line for the model card: "mean |SHAP| for `is_female` is **2.2×** that of the next feature (`Fare`), so the model's reliance on sex is uniform across passengers." You recompute the same quantity *within* each ticket class on the **223** held-out passengers. Reliance ranks **2nd class > 1st class > 3rd class**, the highest class is **1.83×** the lowest, and the real women-minus-men survival gap in the manifest ranks the classes in the same order. What should the line say instead?

A) Reliance on sex is heterogeneous, 1.83× between the most- and least-affected class, so each class gets its own figure and the 2.2× ratio is labelled an average, not a per-passenger fact  
B) Keep the 2.2× line exactly as written: the class ranking matches the real survival gap, which shows the global figure tracks the historical data correctly and needs no caveat about subgroups  
C) Replace it with the figure for the class where reliance is strongest, since a model card should disclose the worst case the model exhibits rather than an average  
D) Drop the SHAP figures: with 223 test passengers split three ways the per-class means are too thin to report, and a local waterfall for one passenger belongs there instead  

---
