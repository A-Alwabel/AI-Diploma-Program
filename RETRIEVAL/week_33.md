# Cumulative Retrieval Quiz — Week 33

**Programme week 33 of 35 · Course 12 — AIAT 126 (Graduation Project), Units 1–2, with Course 11
still fresh.**
**Taken in session 131, in the final 15 minutes.**

---

**How this works**

- **15 minutes, in class, at the END of the session.** 7 minutes to answer, then 8 minutes in which
  your instructor works the correct answers aloud.
- **Not graded.** No mark from this paper reaches your capstone milestone gates.
- **Ten items.** Three on this week and last week, three from about a month ago, four from earlier in
  the programme.
- Write the **letter only**. Closed book. One best answer per item.

---

## Part A — This week and last week (Courses 12 and 11)

### Item 1 — Course 12, Unit 1
The `success_criteria` block taught in Unit 1 pairs a **named metric** with a **numeric threshold**
and the reason that threshold was chosen. Which of these is a properly stated success criterion in
that form?

A) The model will use a deep neural network trained on the collected image set
B) The model will be state of the art for this task by the end of the project
C) Recall above 85% on the validation set, since false negatives are the costly error
D) The model will perform well on the medical images the partner supplied for the project

---

### Item 2 — Course 12, Unit 1
The `scope` block taught in Unit 1 requires an **`out_of_scope`** list beside the `in_scope` list. Why?

A) Because the out-of-scope items become the starting point of the literature review section
B) Because naming what you will not build is what keeps the project finishable in 14 weeks
C) Because reviewers ask for a longer proposal document before the design review
D) Because the success criteria are recorded inside the out-of-scope list

---

### Item 3 — Course 11, Unit 5
Unit 5 motivated one tool with three questions an untracked team cannot answer: which run produced the
production model, which hyperparameters were already tried, and which data the model saw. What is
**MLflow** used for?

A) Logging parameters, metrics and artifacts per run, so runs can be compared later
B) Building and deploying the Docker containers that serve a trained model
C) Writing the Kubernetes manifests that a served model is rolled out with each release
D) Cleaning and transforming the raw data before a training run begins

---

## Part B — About a month ago (Courses 10 and 11)

### Item 4 — Course 10, Generative AI
A product team must generate a million catalogue images a day at interactive latency on a fixed GPU
budget. The diffusion model you built needs roughly **200 sequential network passes per image**; a GAN
needs **one**. Which trade-off should drive the family choice?

A) A GAN generates in one forward pass, so it is the throughput answer; diffusion buys quality at a cost that scales with the step count.
B) A VAE — its encoder makes generation a single pass, and its reconstruction loss is what guarantees sharp catalogue images.
C) The choice is immaterial at this scale: latency is set by output resolution and batch size, not by which generator family you pick.
D) Diffusion — its sample quality is higher, and its sampling cost falls as the model is trained longer, so throughput improves with training.

---

### Item 5 — Course 10, Generative AI
A team removes the protected attribute from its training data and reports that the model is now fair.
Unit 4 ran exactly that experiment: dropping `Sex` cut the predicted-rate gap from **81.9% to 13.4%**,
cost **9.7 points of accuracy**, and `Sex` was still predictable from the remaining features at
**66.0%** against a **63.8%** majority-class baseline. What is the correct conclusion?

A) The gap fell because accuracy fell: a model that predicts one class for everyone shows no gap at all, and has no value either.
B) Fairness through unawareness worked here: a residual gap of 13.4% is small enough to report the model to the client as unbiased.
C) The result transfers: a mitigation of this kind leaves a residual gap of roughly this size, so about 13% is the floor a team should expect.
D) Removing the column removed the ability to audit, not the ability to discriminate — the attribute survives in correlated features.

---

### Item 6 — Course 11, AI Model Deployment
What is **model deployment**?

A) Retraining the model on the full dataset before release
B) Making a trained model reachable by users or other services
C) Measuring the model's accuracy on a held-out test set
D) Saving the trained model to a file so that it can be reloaded later

---

## Part C — Earlier in the programme

### Item 7 — Course 02, Python for Artificial Intelligence
One trained logistic-regression model is scored on the same 171 held-out breast-tumour biopsies; only
the decision threshold changes:

```
   threshold   missed malignant   false alarms   accuracy
        0.20                  1             21     87.1%
        0.30                  5             12     90.1%
        0.50                 11              5     90.6%
        0.80                 20              0     88.3%
Best accuracy on this grid: 92.4% at threshold 0.44 — which still misses 8 malignant tumours.
```

A screening clinic can absorb at most **25 false alarms** out of the 171 and, within that limit, wants
to miss as few malignant tumours as it can. Which threshold does the table support?

A) 0.44 — it is the highest accuracy on the grid, 92.4%, and accuracy is the metric to maximise.
B) 0.80 — it brings false alarms down to zero, and 88.3% accuracy is near the grid maximum.
C) 0.50 — it is the library default, so it already balances the two kinds of error by construction.
D) 0.20 — it misses 1 malignant tumour rather than 11, and its 21 false alarms fit the budget.

---

### Item 8 — Course 03, Mathematics and Probability for ML
On the 50-state USArrests data (Murder, Assault), Unit 1 eigen-decomposed the covariance matrix twice.

- **Standardized:** eigenvalues 1.8019 and 0.1981; PC1 = +0.707×Murder +0.707×Assault; PC1 explains 90.09%.
- **Raw units:** feature variances Murder 18.97 and Assault 6945.17; PC1 = +0.042×Murder +0.999×Assault; PC1 explains 99.90%.

Why is the raw-units **99.90%** the less informative of the two figures?

A) The raw-units run keeps one component while the standardized run keeps two, so the percentages count different totals.
B) Standardizing increases the variance available to PC1, so 90.09% of standardized variance carries more information.
C) On raw units PC1 follows Assault, whose variance is 6945 against Murder's 19, so it reports the measuring scale used.
D) A first component above 99% means the raw covariance matrix is singular, which makes its second eigenvalue unreliable.

---

### Item 9 — Course 08, Deep Learning
You load a pre-trained MobileNetV2, **freeze** the base, and attach a new 10-class head: **12,810 of
2,236,682 parameters (0.57%)** are trainable. You have 2,000 labelled images. Which statement about
this setup is correct?

A) Because the base is frozen, no training is needed — the model can be used as it stands.
B) The frozen layers keep their ImageNet features; the new head is what learns your 10 classes.
C) Freezing the base means the model is no longer able to overfit your 2,000 images.
D) A frozen backbone pays off when the new dataset is at least as large as the pre-training one.

---

### Item 10 — Course 04, Machine Learning Algorithms and Applications
Unit 3's logistic-regression lesson tests on 3,200 real transactions, 6 of them fraudulent, and prints
TN 3191, FP 3, FN 3, TP 3, with test accuracy **0.9981**. The same lesson prints that labelling every
row "legitimate" also scores **0.9981**. What do those two identical accuracies establish?

A) The classifier learned nothing from the 30 features, since it scores what a model with no features scores.
B) At 3,200 rows the test set is too small for accuracy to be a reliable estimate of either model.
C) The two agree because the cut sits at 0.5; moving that cut down to 0.3 would separate the two.
D) Accuracy is set by the 3,194 legitimate rows and has no room to register the 6 fraud rows either way.

---

**End of quiz — put your pen down and follow the worked answers.**
