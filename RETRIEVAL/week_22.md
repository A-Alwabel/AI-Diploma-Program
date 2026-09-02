# Cumulative Retrieval Quiz — Week 22

**Programme week 22 of 35 · Current course: Course 08 — AIAT 122 (Deep Learning), Unit 3 / Unit 4 / Unit 5**
**Placement: session 4 of the week (s88), in the closing block.**

- **15 minutes**, taken **in class at the END of the session**. Not homework.
- **Not graded.** No mark from this paper reaches your course grade.
- Write your answers, then your instructor **works every correct answer aloud immediately afterwards**. Stay for it.
- Ten items. Three from what you are studying now, seven from courses you finished earlier. The earlier items carry their own context.

---

### 1. [Course 08 · Unit 3]
On IMDB reviews padded to 100 tokens, a `SimpleRNN` reaches **0.544** best validation accuracy and an **LSTM** of the same width reaches **0.776**. Where does the LSTM's advantage come from?

A) Its gates and cell state add a path along which the gradient can be carried back many steps
B) It reads all 100 tokens in parallel instead of one at a time, so early words are not forgotten
C) It has fewer parameters than a `SimpleRNN` of the same width, so it needs less data to train
D) It reads each review backwards as well as forwards, so early words are seen last

---

### 2. [Course 08 · Unit 3]
Scaled dot-product self-attention computes `Attention(Q, K, V) = softmax(QKᵀ / √d_k) V`. What does the **softmax term** produce?

A) A probability distribution over the vocabulary, giving the model's next predicted token
B) The position of each token, which is why no positional encoding is needed
C) One weight per position, used to take a weighted average of the value vectors `V`
D) The model's confidence that its prediction is correct, which is why attention maps can be read as explanations

---

### 3. [Course 08 · Unit 2]
You load a pre-trained MobileNetV2, **freeze** the base, and attach a new 10-class head: **12,810 of 2,236,682 parameters (0.57%)** are trainable. You have 2,000 labelled images. Which statement about this setup is correct?

A) Because the base is frozen, no training is needed — the model can be used as it is
B) The frozen layers keep their ImageNet features; the new head is what learns your 10 classes
C) Freezing the base means the model can no longer overfit your 2,000 images
D) A frozen backbone pays off once the new dataset is at least as large as the one it was pre-trained on

---

### 4. [Course 06 · Unit 5]
Your company is placing a CV-screening model that ranks job applicants on the EU market. Under the EU AI Act risk tiers taught in Course 06 Unit 5, what follows?

A) Limited risk: the duty is a transparency notice telling applicants that an AI system is involved in the screening
B) Prohibited: the Act lists automated decision-making about employment among its Article 5 banned practices
C) Minimal risk: the system produces a ranking and a human recruiter still takes the final hiring decision
D) High risk: data governance, logging, human oversight and a conformity assessment apply before deployment

---

### 5. [Course 06 · Unit 1 / Unit 2]
Northpointe showed that COMPAS was **calibrated** — a given risk score meant the same re-offence probability for Black and for white defendants. ProPublica showed that the **false-positive rates differed**: 44.9% for Black defendants against 23.5% for white defendants. Which statement best describes this situation?

A) Both are correct: when base rates differ, calibration and equal error rates are mathematically incompatible
B) Northpointe is right and ProPublica is not: a score that means the same thing for both groups is the fairness that counts
C) ProPublica measured demographic parity, which is the fairness definition a court would apply to a sentencing tool
D) Calibrating the scores separately within each group would let both fairness criteria hold at the same time

---

### 6. [Course 07 · Unit 1]
What is the main goal of NLP?

A) Convert recorded speech into text so that audio can be archived and searched
B) Index documents by keyword so that a search box can retrieve them
C) Enable computers to understand, interpret and manipulate human language
D) Hand-write a complete grammar of a language, so that nothing needs to be learned from text

---

### 7. [Course 04 · Unit 3]
Course 04's KNN lesson fit the same model twice on the same 313 real card transactions. Without scaling it scored accuracy **0.9048**; with `StandardScaler` it scored **0.9683**. The lesson also printed that the `Time` column alone contributes **99.9978%** of the raw squared distance between two transactions (`Time` std 46,331.2, against a median feature std of 1.302). What does that 99.9978% figure explain?

A) Unscaled, "nearest neighbour" means roughly "happened at a similar moment", so what V1–V28 know about a transaction is drowned out
B) The V1–V28 columns barely vary across these rows, so they contribute almost nothing to the distances the model computes between transactions
C) `Time` is the single most predictive feature of fraud here, so scaling it down discards the best signal the model has
D) `StandardScaler` dropped `Time` from the feature set, and removing that column lifted accuracy by 6.35 points

---

### 8. [Course 04 · Unit 2]
A colleague evaluated the crime-rate regression on one 80/20 split and reported **R² = 0.1095**. Course 04 Unit 2 ran 5-fold cross-validation on the same data and printed **R² = 0.0844 ± 0.0358**; across ten different single splits the R² ran from **0.0402 to 0.1259** (the largest 3.1× the smallest). What is wrong with the colleague's report?

A) 0.1095 has to be wrong: the true value is 0.0844, so test rows leaked into training
B) Both procedures hold out 20% of the rows, so the difference comes down to the random seed and can be safely ignored
C) Cross-validation trains each fold on less of the data, which makes 0.0844 pessimistic and 0.1095 the more honest figure
D) 0.1095 sits near the top of what a single split produces, and the report gives no way to spot a lucky one

---

### 9. [Course 02 · Unit 4]
Course 02's Unit 4 notebook ran gradient descent on `f(x) = x²` from `x = 5.0`, changing only the learning rate:

```
learning rate     x @ step 0   x @ step 3   x @ step 6  x @ step 12  x @ step 25   verdict
0.01                  5.0000       4.7060       4.4292       3.9236       3.0173   too small
0.10                  5.0000       2.5600       1.3107       0.3436       0.0189   just right
0.95                  5.0000      -3.6450       2.6572       1.4121      -0.3589   too big
1.10                  5.0000      -8.6400      14.9299      44.5805    -476.9810   way too big
```

A student concludes: *"a learning rate that overshoots the minimum will diverge."* Which row refutes that, and how?

A) lr = 0.01: it stays on one side of the minimum, so overshoot is not required in order to converge
B) lr = 0.95: it lands beyond the minimum (x = −3.65 at step 3) and still closes in to |x| = 0.36
C) lr = 0.10: it reaches x = 0.019 without overshooting, so overshoot is what slows a run down
D) lr = 1.10: its sign alternates, showing that overshoot and divergence are the same behaviour

---

### 10. [Course 01 · Unit 2]
Course 01's Bayes lesson updated a 1% prior on a disease to P(disease | positive test) = **8.76%**, and a 30% prior on spam to P(spam | "free") = **77.42%**. What is Bayesian probability used for in AI?

A) Guaranteeing a correct diagnosis once a positive test result has been observed by the system
B) Computing the prior probability of a hypothesis before evidence has been observed at all
C) Updating a belief as evidence arrives, and reporting how strong the belief now is
D) Eliminating uncertainty, so predictions become deterministic

---

**End of paper. Hand nothing in. Stay for the worked answers.**
