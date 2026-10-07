# Retrieval Quiz — Week 30

**Week 30 of 35 · Course 11 — AIAT 125 (Deploying AI Models)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

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

### Question 2

In Unit 1 lesson 01, `wdbc-baseline` was wrapped in a FastAPI app and the notebook printed a ready-to-paste `curl -X POST http://localhost:8000/predict` carrying 30 JSON fields. The dashboard team writes JavaScript and the billing team writes Go; both want predictions. A colleague asks why they should call this endpoint instead of each loading `model.joblib` themselves. Which answer gives the benefit the lesson actually claims for serving over HTTP?

A) Any program that can send JSON to one address can use the model, whatever language it was written in  
B) HTTP makes each prediction faster than the in-process call the lesson timed at 0.060 ms per call  
C) Behind HTTP, Flask returns `400` for a missing field on its own, so nobody has to write any validation code  
D) Once the model sits behind one address, extra worker processes are started by the API layer as traffic grows  

---

### Question 3

Unit 3 compared cloud hosting tiers for a model endpoint. When is **serverless** compute (AWS Lambda, GCP Cloud Run) the right choice?

A) When each request needs a GPU, since the platform attaches one for the call  
B) When traffic is low or unpredictable and you would rather pay per request than run a server  
C) When the response budget is 10 ms, since scaling to zero removes queueing between requests  
D) When peak throughput matters most, because a managed runtime outruns a container you built yourself  

---

### Question 4

Unit 5's comparison notebook runs Dyna-style planning (20 replayed transitions after each real step) against plain Q-learning on `FrozenLake-v1`, averaged over **20 seeds × 300 episodes** with epsilon = 0.2 for both. It summarises its own table in two lines:

```
- EARLY: the model-based agent is ahead by +0.312 success rate over the first
  50 episodes. Same number of environment steps, more learning squeezed out of them.
- LATE: the gap has closed to -0.001. Both reach roughly the same level.
```

and adds that the planning agent performed about **20x more Q-updates** for the same environment experience. A team is choosing an agent for a warehouse robot: each real step costs time and wear, while a desktop CPU sits idle between steps. Which recommendation follows from those two gaps?

A) Choose the model-free agent: the -0.001 late gap shows both end level, so the 20x extra Q-updates are compute spent for no advantage that survives to the end of the 300 episodes.  
B) Choose the planning agent because the +0.312 gap shows it extracted 20x more environment experience from the same 300 episodes, which is exactly what a costly robot needs.  
C) Choose the planning agent: the +0.312 early gap means it reaches a usable success rate on far fewer costly real steps, and the -0.001 late gap says no final performance is lost.  
D) Run both past 300 episodes before deciding; a -0.001 gap averaged over 20 seeds is too narrow to show which agent would end higher, and that is what the choice turns on.  

---

### Question 5

Unit 3's DQN stored each transition in a buffer and trained on random minibatches drawn from it, rather than on the transitions in the order they arrived. What problem does **experience replay** solve?

A) It removes the need for a separate target network, since sampled targets are already stable  
B) It lets the agent learn a useful policy from a single episode of experience  
C) It shortens each training step, because a buffered batch is read faster than a live one  
D) Consecutive transitions are highly correlated, and random sampling breaks that correlation  

---

### Question 6

Unit 4 trained one agent with epsilon fixed at 0.3 and another with epsilon starting at 1.0 and decaying toward 0.05. What does **epsilon decay** change about training?

A) Exploration is broad early and mostly gives way to exploitation as epsilon falls  
B) The update step shrinks over time, so late episodes disturb the learned values less  
C) The discount factor is reduced, so the agent gradually stops valuing distant rewards  
D) The replay buffer is trimmed as training proceeds, so stale transitions go  

---

### Question 7

Under its learning-rate table, the Unit 4 notebook printed where each gradient-descent run on `f(x) = x²` stood after 25 steps from `x = 5.0`:

```
Distance from the optimum after 25 steps:
   lr = 0.01  |x| =     3.0173   f(x) =   9.1042e+00   (too small)
   lr = 0.1   |x| =     0.0189   f(x) =   3.5681e-04   (just right)
   lr = 0.95  |x| =     0.3589   f(x) =   1.2884e-01   (too big)
   lr = 1.1   |x| =   476.9810   f(x) =   2.2751e+05   (way too big)
```

A student disputes the two bottom verdicts: *"0.95 and 1.1 both jump across the minimum on every step, so they are the same failure and both deserve 'way too big'."* What in this printout separates the two rows?

A) The labels alone: both |x| values belong to runs that crossed the minimum on each step, so the printout gives the student no numerical ground for keeping the two verdicts apart  
B) Which way |x| moved: 0.95 ends 0.3589 away, nearer than its start at 5.0, while 1.1 ends 476.9810 away — crossing while shrinking converges, crossing while growing diverges  
C) The f(x) column read against a cut-off: 1.2884e-01 is below 1 and 2.2751e+05 is far above it, and a cost under 1 is the notebook's working test for having converged  
D) The 0.1 row: its 0.0189 is the one distance that has essentially reached zero, so a run still 0.3589 away after 25 steps has failed in the same way 1.1 did  

---

### Question 8

The weather recommender in Course 01's first lesson printed two neighbouring cases:

```
26 °C, 59% humidity, morning -> Go for a jog in the park
26 °C, 61% humidity, morning -> Moderate weather, any outdoor activity is fine
```

A classmate concludes that the recommender "learned a humidity boundary near 60% from past weather data". Which statement describes where that boundary actually came from, and what it tells you about the system's family?

A) The 60% cut was fitted from the four printed test cases, which makes the recommender a small data-driven model of the kind Unit 2 trains  
B) The jump between 59% and 61% shows the system hides its reasoning, which is the mark of a modern learned model  
C) The two answers differ because the hand-written rule evaluates faster than a fitted model would; speed is what separates the two families  
D) A person typed `humidity < 60` into an `if` statement, so the system is rule-based: the threshold was authored, not fitted to data  

---

### Question 9

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

### Question 10

The lesson's epsilon sweep prints the private count's error as a share of the true answer for the 212-patient cohort and the 29-patient subgroup:

```
 epsilon    cohort (212)   subgroup (29)    ratio
     0.5            0.9%            7.8%     8.2x
     5.0            0.1%            0.6%     6.2x
```

A colleague reads the ratio column and concludes that the subgroup must be receiving a noisier draw from the mechanism. What actually produces this pattern?

A) The Laplace scale is sensitivity divided by epsilon, with no term for group size, so both counts get noise of the same size and the smaller answer absorbs it as a larger share  
B) A count over 29 patients has higher sensitivity than one over 212, because one patient is a larger fraction of the group, so the mechanism deliberately draws wider noise to protect the subgroup  
C) The subgroup count is an estimate from fewer records, so its ordinary sampling error adds to the privacy noise and inflates its share of the answer  
D) Laplace noise is drawn in proportion to the true answer, so the subgroup gets smaller absolute noise and the larger share is a rounding effect in the printed table  

---
