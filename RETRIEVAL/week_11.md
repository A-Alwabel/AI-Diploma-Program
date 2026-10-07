# Retrieval Quiz — Week 11

**Week 11 of 35 · Course 04 — AIAT 114 (Machine Learning Algorithms and Applications)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Unit 3's KNN lesson splits its card transactions into 250 training and 63 test rows and prints, before any scaling:

```
Std of first feature (Time): 46331.17
Std of Amount feature: 215.28
```

The figure caption adds that on a log axis `Time` stands about four orders of magnitude above the V1–V28 columns, and `Amount` about two. A classmate proposes a shortcut: delete `Time`, skip `StandardScaler`, and fit KNN on the remaining 29 raw columns, "since the one problem column is gone." What does the lesson's evidence say will happen to the distances KNN computes?

A) With `Time` removed the remaining columns sit on comparable scales, so the shortcut does the same job `StandardScaler` would have done  
B) Dropping `Time` discards the column that dominated the distance, which is the model's strongest fraud signal, so the fit gets worse for a different reason  
C) `Amount` inherits the role `Time` played: its spread sits about two orders of magnitude above V1–V28, so it now decides who counts as a neighbour  
D) KNN compares the ranking of distances rather than their raw size, so a column's standard deviation cannot change which rows come out nearest  

---

### Question 2

Unit 4's K-Means sweep over the 1,994 scaled communities prints, among its rows:

```
K=7: Inertia=2145.23, Silhouette=0.2970
K=9: Inertia=1824.09, Silhouette=0.3008
```

A colleague picks K = 9: "it beats K = 7 on silhouette *and* on inertia - for once both criteria agree, so the data has decided." The lesson's own elbow landed on K = 4, and the lesson clustered at K = 3. What is the right response?

A) The colleague is right: when the inertia criterion and the silhouette criterion point the same way, the data has chosen K and no judgement is needed  
B) Inertia falls with each added cluster by construction, and a third-decimal silhouette bump is no ranking, so K is still settled by what the clusters are for  
C) K = 2 should stand: its silhouette of 0.3967 is the highest in the sweep, and the global peak outranks any comparison between neighbouring rows  
D) K = 4 should stand: the elbow was located geometrically, from the chord between the first and last points of the curve, which makes it a measurement rather than a judgement  

---

### Question 3

The same lesson prints two different ways of pushing the fraud model to flag more of the 3,200 test transactions - lowering the cut on the original model, and refitting with `class_weight='balanced'`:

```
cut 0.1 (original model):   caught 4   missed 2   false alarms 6    recall 0.6667   precision 0.4000
class_weight='balanced':    caught 3   missed 3   false alarms 18   recall 0.5000   precision 0.1429
```

A colleague reads the second line and concludes that the weighted refit is "the more aggressive model, so it must be the one catching more fraud." What do the two lines establish?

A) Recall sat at 0.5000 because 'balanced' is a mild preset; a hand-set weight on class 1 would carry recall past the 0.6667 the lower cut reached  
B) The precision collapse to 0.1429 is the minority class being overfitted by the refit, which the threshold change avoids because the fitted model is left untouched  
C) Flagging more is not finding more: 18 alarms bought 3 frauds where 6 alarms bought 4, so the weighting moved the operating point without adding signal  
D) Both rows fall below the 0.9981 that labelling each row legitimate scores, so the default 0.5 cut, which matches it, remains the model to keep  

---

### Question 4

The matrix-operations lesson redraws its fusion experiment on the 1,797 mean-centred digit images and adds a third route, `relu(X @ W1) @ W2`, with a ReLU between the two layers. The printed reading of the figure is:

```
Blue points (no activation): 2.0e-14 is the largest amount any of the 17,970 output numbers differs from the fused one-layer network.
Orange points (ReLU inserted): up to 11.8 away from the diagonal, on outputs that span roughly -19 to +18.
```

A classmate argues that the ReLU is a minor numerical detail and that the real lesson is which bracketing is cheaper. Which reading of these two printed gaps is correct?

A) Both gaps are rounding noise; the ReLU route sits further off because `max()` adds another rounded operation per entry  
B) The 2.0e-14 gap shows the layer-by-layer route drifts from the fused one, so even without a ReLU the two layers compute a slightly different function  
C) The orange points leave the diagonal because the digits were mean-centred, not because of the ReLU; on raw pixels the same ReLU would spread them as far  
D) The 2.0e-14 gap says the two linear routes are one function; the 11.8 gap says the ReLU made a genuinely different model  

---

### Question 5

The gradient-descent lesson prints, next to each learning rate, the factor |1 − 2·lr| that multiplies x at each step when minimising f(x) = x² from x = 5 for 30 steps: 0.98 for lr = 0.01, 0.80 for lr = 0.1, 0.80 for lr = 0.9, 1.00 for lr = 1.0 and 1.20 for lr = 1.1. The losses after 30 steps are 7.43883, 3.83124e-05, 3.83124e-05, 25 and 1.40869e+06 respectively. A colleague watching a training run sees a loss curve that is a straight line down on a log axis and concludes the step size is well chosen. Using the printed factors, which objection is justified?

A) A factor of 0.80 belongs to both lr = 0.1 and lr = 0.9, so the same straight line can come from a run that crosses zero at each step  
B) A factor of 0.80 means both runs move x by the same distance each step, so lr = 0.9 is a relabelled lr = 0.1 and no objection applies  
C) A straight line down shows the factor is below 1, so the rate can safely be raised toward the 1.00 row for a faster descent  
D) The 3.83124e-05 reached at lr = 0.9 beats the 7.43883 at lr = 0.01 because the larger rate found a second, deeper minimum of f  

---

### Question 6

Course 02 classified points with k-nearest neighbours and varied k. What goes wrong when k is set too small - say k = 1?

A) The prediction rests on one neighbour, so a single mislabelled or unusual training point decides the answer  
B) The decision boundary is smoothed so heavily that the two classes stop being distinguishable  
C) Training slows down, because the model has to sort the full distance table before it reads off a label  
D) The model becomes more robust to noise, since consulting fewer neighbours means fewer chances to pick up a stray point  

---

### Question 7

The weather recommender in Course 01's first lesson printed two neighbouring cases:

```
26 °C, 59% humidity, morning -> Go for a jog in the park
26 °C, 61% humidity, morning -> Moderate weather, any outdoor activity is fine
```

A classmate concludes that the recommender "learned a humidity boundary near 60% from past weather data". Which statement describes where that boundary actually came from, and what it tells you about the system's family?

A) The 60% cut was fitted from the four printed test cases, which makes the recommender a small data-driven model of the kind Unit 2 trains  
B) The jump between 59% and 61% shows the system hides its reasoning, which is the mark of a modern learned model  
C) A person typed `humidity < 60` into an `if` statement, so the system is rule-based: the threshold was authored, not fitted to data  
D) The two answers differ because the hand-written rule evaluates faster than a fitted model would; speed is what separates the two families  

---

### Question 8

A discriminative model learns P(Y | X) - the label given the input. What does a generative model learn instead?

A) P(Y) alone - the base rate of each class in the training set  
B) P(Y | X) as well, but estimated with a different optimiser and a larger training budget  
C) P(X) alone - the distribution of the inputs, with the class labels left out of the model  
D) P(X | Y) and P(Y) - the joint distribution over inputs and labels  

---

### Question 9

The Unit 1 libraries notebook timed the doubling of 1,000,000 numbers twice. A one-shot timing cell printed:

```
   Python list comprehension :    11.05 ms
   NumPy, whole array at once:     0.71 ms
   Speed-up measured here    :     15.5x

Against the "100x faster" line in the Part 2 text above:
   this run measured 15.5x - well short of 100x.
```

The next cell re-timed six array sizes, keeping the best of three trials after a warm-up, and closed with:

```
Smallest N (10):        NumPy is SLOWER (0.5x)
Largest N (1,000,000): NumPy is 62x faster
```

A teammate wants to vectorise a helper that is called thousands of times per second on arrays of about ten values, and quotes the 62x as the gain to expect. Which printed line actually bears on that helper, and what does it say?

A) `Smallest N (10): NumPy is SLOWER (0.5x)` — on ten values the per-call setup cost is the whole job, so the plain list stays ahead  
B) `Largest N (1,000,000): NumPy is 62x faster` — the compiled loop is the same code at any N, so the factor carries over to ten values  
C) `this run measured 15.5x` — one honest measurement on this machine, so that is the realistic gain for the helper to expect  
D) The Part 2 text's `100x faster` — the 15.5x and 62x were pulled down by timing noise, so the tutorial figure is the safer planning estimate  

---

### Question 10

Why does a feedforward network put an activation function between two dense layers?

A) To add a controlled amount of randomness, which keeps the network from settling too early  
B) To introduce non-linearity, without which stacked layers collapse into a single linear map  
C) To reduce memory use, because the activation discards values that the next layer will not read  
D) To speed up computation, since the activation replaces the layer's matrix product with a lookup  

---
