# Retrieval Quiz — Week 21

**Week 21 of 35 · Course 08 — AIAT 122 (Deep Learning)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

In the per-digit error chart of the lesson, both models were fitted on the identical **5,000** MNIST training images. Logistic regression misreads **143** of the test threes; the network with **128** ReLU hidden units misreads **73** of them, and it makes fewer errors on 9 of the 10 digits — digit **4** is the exception (**81** errors for logistic regression against **89** for the network). Which account of *how each model uses a pixel* explains this pattern?

A) The network needs fewer labelled threes to fit well, because its hidden units share what they learn across the ten digit classes, while logistic regression has to fit each class on its own  
B) The network's loss surface is convex, so Adam reaches the global minimum, while the logistic-regression solver stopped short at `max_iter=500` on the harder digits  
C) The network trains on pixels divided by 255 while logistic regression sees `StandardScaler` output, and raw-scale pixels preserve more of the stroke information  
D) Logistic regression scores each pixel with one fixed weight, so a slanted or off-centre 3 misses its template; the hidden layer combines pixels non-linearly and recovers it  

---

### Question 2

The lesson's `model.summary()` lists `conv2d_1 (Conv2D)`, 64 filters, at **18,496** parameters, and the `dense (Dense)` layer of 64 units that follows `Flatten` at **102,464** — the largest line in a **121,930**-parameter model. The conv layer turns a 13×13×32 map into an 11×11×64 one; the Dense layer reads a **1,600**-long vector. Which statement correctly accounts for the gap between the two counts?

A) Each of the 64 filters is one 3×3×32 weight block reused at each position of the map, so a pattern is learned once; Dense buys a separate weight per input per unit  
B) Flattening throws away where each value sat in the 13×13 grid, so the Dense layer has to compensate for the lost position information with many more weights than a conv layer needs  
C) Weight sharing keeps the conv layer from memorising, which is why the lesson can train without holding out a validation split  
D) The convolution already includes its non-linearity, so it saves the parameters that a separate ReLU stage would otherwise add  

---

### Question 3

Course 07's Unit 5 bias-audit notebook disclosed that its association scores were **simulated** rather than measured; its skip-gram experiment shows where real ones come from. In a real audit, what produces those numbers?

A) A published audit of a comparable system, rescaled to this model's vocabulary size  
B) The share of each demographic group in the training corpus, counted from the raw text  
C) Cosine similarities in the model's own trained vectors, or its outputs on probe inputs  
D) The auditor's own judgement of how strongly each profession reads as male or as female, written into the table  

---

### Question 4

The lesson's epsilon sweep prints the private count's error as a share of the true answer for the 212-patient cohort and the 29-patient subgroup:

```
 epsilon    cohort (212)   subgroup (29)    ratio
     0.5            0.9%            7.8%     8.2x
     5.0            0.1%            0.6%     6.2x
```

A colleague reads the ratio column and concludes that the subgroup must be receiving a noisier draw from the mechanism. What actually produces this pattern?

A) A count over 29 patients has higher sensitivity than one over 212, because one patient is a larger fraction of the group, so the mechanism deliberately draws wider noise to protect the subgroup  
B) The Laplace scale is sensitivity divided by epsilon, with no term for group size, so both counts get noise of the same size and the smaller answer absorbs it as a larger share  
C) The subgroup count is an estimate from fewer records, so its ordinary sampling error adds to the privacy noise and inflates its share of the answer  
D) Laplace noise is drawn in proportion to the true answer, so the subgroup gets smaller absolute noise and the larger share is a rounding effect in the printed table  

---

### Question 5

A colleague drafts one line for the model card: "mean |SHAP| for `is_female` is **2.2×** that of the next feature (`Fare`), so the model's reliance on sex is uniform across passengers." You recompute the same quantity *within* each ticket class on the **223** held-out passengers. Reliance ranks **2nd class > 1st class > 3rd class**, the highest class is **1.83×** the lowest, and the real women-minus-men survival gap in the manifest ranks the classes in the same order. What should the line say instead?

A) Keep the 2.2× line exactly as written: the class ranking matches the real survival gap, which shows the global figure tracks the historical data correctly and needs no caveat about subgroups  
B) Replace it with the figure for the class where reliance is strongest, since a model card should disclose the worst case the model exhibits rather than an average  
C) Reliance on sex is heterogeneous, 1.83× between the most- and least-affected class, so each class gets its own figure and the 2.2× ratio is labelled an average, not a per-passenger fact  
D) Drop the SHAP figures: with 223 test passengers split three ways the per-class means are too thin to report, and a local waterfall for one passenger belongs there instead  

---

### Question 6

A passenger appeals a decision. The Case Officer pulls the record from the audit trail:

```
    model_version: screening-rf-v1.0
       input_hash: 798b3362838a
       prediction: predicted non-survivor
       confidence: 0.6733333333333333
      top_factors: ['is_female -', 'Fare +']
   human_reviewer: None
    subject_group: male
```

The ML Lead replies that, because the RACI matrix lists **The AI system** as *Responsible* for individual decisions, the appeal should be closed as "decided by the model". Under the framework, how is the appeal handled?

A) Close it as the ML Lead proposes: Responsible is the role that produced the decision, and a confidence of 0.6733 shows the system was operating inside its normal range, so there is nobody else to ask  
B) Reject it as moot: 0.6733 is above the deployed router's 0.60 threshold, so the decision was correctly automated and no accountability question arises  
C) Escalate it to the ML Lead: the record shows no human reviewer, and the role that trained the model is the one able to explain a 0.6733 output to the passenger  
D) A named role answers it: the Case Officer is Accountable for the decision, the Head of Operations owns redress, and the trail's version, hash and factors make the answer evidence  

---

### Question 7

From the same sample of 100 recorded Titanic ages, the confidence-interval lesson prints a 90% interval of [27.3582, 32.2468] (width 4.8886) and a 99% interval of [25.9361, 33.6689] (width 7.7327). When it redoes the whole study 2000 times, 92.5% of the 90% intervals and 99.6% of the 99% intervals capture the population mean, and in the panel that draws 100 of those repeats, 3 intervals are shown in crimson. A student writes: 'There is a 99% chance the true mean age is between 25.9361 and 33.6689.' Which statement about that sentence is right?

A) Wrong: the 99% is the capture rate of the procedure across repeats — measured here as 99.6% — not the odds for this one interval  
B) Acceptable: 99.6% of the 2000 repeated intervals held the mean, so roughly 99% is also the right probability for this one  
C) Wrong: the level counts recorded ages, so the sentence should say that 99% of the 714 ages lie between 25.9361 and 33.6689  
D) Acceptable, and understated: the wider 99% interval (7.7327 against 4.8886) carries more knowledge about the mean, which is why its coverage rose to 99.6%  

---

### Question 8

Unit 1's regularization lesson predicts transaction `Amount` and prints a plain `LinearRegression` baseline of **MSE 4133.96**, then this part of the Lasso sweep:

```
Alpha   1.00: MSE = 4137.4229, R² = 0.8930, Features = 28/29
Alpha  10.00: MSE = 6043.0153, R² = 0.8437, Features = 14/29
Alpha 100.00: MSE = 36102.8517, R² = 0.0659, Features = 1/29
```

A teammate wants to report the α = 10 model: "it is the first setting where Lasso actually selects features, so the regularization is finally doing its job." Which reading of these rows is right?

A) Fourteen inputs at R² 0.8437 is the leaner model, and leaner is what regularization is for, so it should replace the 29-feature baseline in the report  
B) Each column Lasso switched off cost test error, which is what selection looks like when the baseline had no overfitting for a penalty to remove  
C) The grid is too coarse: an α between 1 and 10 would drop columns while holding the baseline's error, so refine the sweep before choosing  
D) Removing half the columns cures the multicollinearity among V1–V28, so the α = 10 coefficients are the trustworthy ones to publish  

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

A) `Largest N (1,000,000): NumPy is 62x faster` — the compiled loop is the same code at any N, so the factor carries over to ten values  
B) `this run measured 15.5x` — one honest measurement on this machine, so that is the realistic gain for the helper to expect  
C) `Smallest N (10): NumPy is SLOWER (0.5x)` — on ten values the per-call setup cost is the whole job, so the plain list stays ahead  
D) The Part 2 text's `100x faster` — the 15.5x and 62x were pulled down by timing noise, so the tutorial figure is the safer planning estimate  

---

### Question 10

In the knowledge-representation lesson, `classify_animal` returned `is a fish` for the whale and the printout marked it `WRONG`. After the repair the same printout read `is a mammal`, and the heading said the function's code was untouched. Which part of the knowledge-based system was changed to get the right answer?

A) The inference loop: `classify_animal` was rewritten so that it tests `breathes air` before it tests `lives in water`  
B) The training data: the whale's row was relabelled `mammal` and the classifier was refitted on the four observed animals  
C) The fact table: an index on the fact `lives in water` was rebuilt so that a lookup for the whale returned mammal instead of fish  
D) The rule store: `breathes air -> is a mammal` was inserted at the front of `animal_kb.rules`, and the old loop reached it first  

---
