# Retrieval Quiz — Week 22

**Week 22 of 35 · Course 08 — AIAT 122 (Deep Learning)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The lesson trains three recurrent layers of width 64 on the same `Embedding(2000, 64)`, the same **2,000** training reviews, the same **12** epochs and the same seed. Best validation accuracy: `GRU` **0.720** (final 0.692), `SimpleRNN` **0.544** (final 0.520). A classmate says the GRU beats the gateless layer for the same reason an LSTM does. Which reason is that?

A) It takes in the 100 padded positions at once rather than one word at a time, so the opening words are not overwritten by the ones that come later  
B) It carries fewer recurrent weights than the SimpleRNN's 8,256 — so with 2,000 reviews there is less for it to overfit  
C) It runs over each review forwards and then backwards, so the words from the start are the freshest when the verdict is made  
D) Its gates make each step a controlled, trainable update of the state, so a gradient can reach earlier words along a near-additive path  

---

### Question 2

For the first review in the IMDB test split (**68** real tokens), the lesson prints: one attention row sums to **1.000** over the real tokens; uniform attention would give each token **0.0147**; the most-attended word, `terrible`, receives **0.0156** (**1.06×** uniform); and the model's P(positive) for the review is **0.012**. In the `MultiHeadAttention` layer's returned scores, what are the entries of that row?

A) Weights for one query position: the coefficients that average the 68 value vectors `V` into that position's output vector  
B) The probability the model assigns to each of the 68 words as the next token, which is why the row sums to 1.000  
C) A learned code for where each of the 68 tokens sits, which the layer uses in place of a separate positional embedding  
D) Per-word contributions to P(positive) = 0.012, so the 0.0156 on `terrible` is the layer's stated reason for the negative verdict on this review  

---

### Question 3

After setting `requires_grad = False` on the MobileNetV2 base and attaching `Dropout(0.2)` + `Linear(1280, 10)`, the lesson prints **Frozen (reused): 2,223,872 parameters = 99.43%**. Training on **2,000** resized MNIST digits, the head reports train accuracy **0.569** after epoch 1 and **0.843** after epoch 2, then scores **0.854** on the **500** held-out images. Which reading of this run is correct?

A) The 99.43% already encodes digits well enough that the two epochs mostly confirm what the model could do before any training  
B) The 99.43% stays as ImageNet learned it; the climb from 0.569 to 0.843 is the fresh head learning what the ten digit classes look like  
C) With 99.43% frozen there is too little capacity left to memorise 2,000 images, so the 500-image hold-out is a formality  
D) A base frozen to 99.43% pays off once the new dataset is at least ImageNet-sized; at 2,000 digits the whole network should be unfrozen and retrained  

---

### Question 4

A bank is placing two systems on the EU market: a **customer-service chatbot** that answers account questions, and a **credit-scoring model** that decides loan eligibility. The lesson's `classify_eu_risk()` returned a tier for each, and the chart under it counts obligations per tier as **0 → 2 → 9** from minimal to high risk. What follows for the two systems?

A) Both fall in limited risk: each system faces customers directly, so an Article 50 notice that an AI is involved discharges the bank's duties for the pair  
B) The credit scorer is prohibited under Article 5, since algorithmic decisions on access to loans sit beside social scoring, while the chatbot is minimal risk with no new obligations  
C) The chatbot carries the 2 limited-risk duties (disclose the AI, label synthetic media); the credit scorer carries the 9 high-risk obligations, conformity assessment included  
D) Both are high risk: a bank counts as critical infrastructure under the Act, so the 9 obligations attach to any AI system it deploys, the account-questions chatbot included  

---

### Question 5

A student reruns the lesson's five-frame storyboard. Both groups are pinned to **PPV = 62%** and **FNR = 28%** in every frame; the white base rate stays at 39% while the Black base rate slides from 39% to 51%. Frame 1 prints a forced false-positive gap of **0.0 points**; frame 5 prints **17.7 points**. The gap ProPublica measured in Broward County was **21.4 points**. What does the storyboard establish?

A) ProPublica's 21.4-point finding is mostly an artefact: a tool pinned to equal PPV treats both groups correctly, so the error-rate critique of COMPAS does not stand  
B) The gap sits in the base-rate column, so lowering the cut-off for white defendants until their FPR also reads 45.9% would let calibration and equal error rates hold together  
C) Frame 5 shows a 17.7-point failure of demographic parity, which is the fairness test a court applies, so Northpointe's calibration defence is beside the point  
D) Both camps measured correctly: holding PPV equal while base rates differ forces an FPR gap by arithmetic, so the dispute is which criterion to hold, not who miscounted  

---

### Question 6

Four teams at the same company describe what they are building. Judged by how Unit 1's sample paragraph defines the field, which team is doing **NLP** rather than one of its neighbouring jobs?

A) A team teaching software to read complaint emails, work out what each one means and decide where to route it  
B) A team turning recorded support calls into written transcripts so the audio can be archived and searched  
C) A team matching the words typed into a search box against the documents that contain those same words  
D) A team writing out by hand a rule set for Arabic grammar so the rules come from a linguist rather than from data  

---

### Question 7

Unit 3's KNN lesson splits its card transactions into 250 training and 63 test rows and prints, before any scaling:

```
Std of first feature (Time): 46331.17
Std of Amount feature: 215.28
```

The figure caption adds that on a log axis `Time` stands about four orders of magnitude above the V1–V28 columns, and `Amount` about two. A classmate proposes a shortcut: delete `Time`, skip `StandardScaler`, and fit KNN on the remaining 29 raw columns, "since the one problem column is gone." What does the lesson's evidence say will happen to the distances KNN computes?

A) With `Time` removed the remaining columns sit on comparable scales, so the shortcut does the same job `StandardScaler` would have done  
B) `Amount` inherits the role `Time` played: its spread sits about two orders of magnitude above V1–V28, so it now decides who counts as a neighbour  
C) Dropping `Time` discards the column that dominated the distance, which is the model's strongest fraud signal, so the fit gets worse for a different reason  
D) KNN compares the ranking of distances rather than their raw size, so a column's standard deviation cannot change which rows come out nearest  

---

### Question 8

Unit 2's 5-fold cross-validation of the murder-rate regression prints these fold scores:

```
Fold 1: R² = 0.1095
Fold 2: R² = 0.0616
Fold 3: R² = 0.0703
Fold 4: R² = 0.0999
Fold 5: R² = 0.0809

Mean R²: 0.0844
Std R²:  0.0179
```

A teammate wants the report to state **R² = 0.0616** - "the worst fold, so nobody can accuse us of picking a lucky split." Which response is right?

A) Agree: the lowest fold is the floor on what the model can do, so quoting it is the conservative choice and needs no spread beside it  
B) The spread comes from fold 5 holding out 398 rows instead of 399, so the fix is Leave-One-Out cross-validation, which gives each fold the same size before anything is reported  
C) Quoting the worst fold is still quoting one draw; the honest figure is the pair 0.0844 ± 0.0179, which shows how far a single fold can land from the mean  
D) A std of 0.0179 on a mean of 0.0844 means the model is too unstable to report; collect more features before quoting any R² to the client  

---

### Question 9

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
B) The f(x) column read against a cut-off: 1.2884e-01 is below 1 and 2.2751e+05 is far above it, and a cost under 1 is the notebook's working test for having converged  
C) The 0.1 row: its 0.0189 is the one distance that has essentially reached zero, so a run still 0.3589 away after 25 steps has failed in the same way 1.1 did  
D) Which way |x| moved: 0.95 ends 0.3589 away, nearer than its start at 5.0, while 1.1 ends 476.9810 away — crossing while shrinking converges, crossing while growing diverges  

---

### Question 10

Course 01's Bayes lesson updated a 1% prior on a disease to P(disease | positive test) = **8.76%**, and a 30% prior on spam to P(spam | "free") = **77.42%**. What is Bayesian probability used for in AI?

A) Confirming a diagnosis once a positive test result has been observed by the system  
B) Computing the prior probability of a hypothesis before evidence has been observed at all  
C) Updating a belief as evidence arrives, and reporting how strong the belief now is  
D) Eliminating uncertainty, so predictions become deterministic  

---
