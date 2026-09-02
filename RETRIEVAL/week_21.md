# Cumulative Retrieval Quiz — Week 21

**Programme week 21 of 35 · Current course: Course 08 — AIAT 122 (Deep Learning), Unit 1 / Unit 2**
**Placement: session 3 of the week (s83), in the closing block. Session 4 (s84) closes Unit 2 with its unit quiz, so the block moves back to s83.**

- **15 minutes**, taken **in class at the END of the session**. Not homework.
- **Not graded.** No mark from this paper reaches your course grade.
- Write your answers, then your instructor **works every correct answer aloud immediately afterwards**. Stay for it.
- Ten items. Three from what you are studying now, seven from courses you finished earlier. The earlier items carry their own context.

---

### 1. [Course 08 · Unit 1]
A team replaces a logistic-regression classifier with a two-layer neural network on the **same raw pixels** and the **same 10,000 test images**. Test accuracy rises from **0.8879 to 0.9130** — 1,121 wrong images down to 870. Which statement best explains the advantage the network has here?

A) It needs fewer labelled training images, because its layers share information between the ten classes
B) It learns hierarchical features from the raw pixels instead of using each pixel as a fixed feature
C) It is guaranteed to reach the global minimum of its loss, which logistic regression is not
D) It removes the need to scale or normalise the inputs before training

---

### 2. [Course 08 · Unit 2]
Your first model for a 28×28 image task is a `Dense` network on flattened pixels. You replace it with a CNN and accuracy improves. What does the **convolutional layer** give you that the `Dense` layer did not?

A) It treats each image as one flat vector, so the position of a pixel no longer changes the result
B) Its weight sharing removes the risk of overfitting, so a held-out validation split is no longer needed
C) It supplies the non-linearity itself, so no ReLU is needed after the layer
D) The same small filter runs at each position, so a pattern learned once is found anywhere

---

### 3. [Course 07 · Unit 5]
Course 07's Unit 5 bias-audit notebook disclosed that its association scores were **simulated** rather than measured; its skip-gram experiment shows where real ones come from. In a real audit, what produces those numbers?

A) A published audit of a comparable system, rescaled to this model's vocabulary size
B) The share of each demographic group in the training corpus, counted from the raw text
C) Cosine similarities in the model's own trained vectors, or its outputs on probe inputs
D) The auditor's own judgement of how strongly each profession reads as male or as female, written into the table

---

### 4. [Course 06 · Unit 3]
In Course 06's differential privacy lesson, the Laplace mechanism at **ε = 0.1** produced a mean absolute error of about **10** on a count of **212** patients (4.7% of the answer) and about **10** again on a count of **29** patients (34.2% of the answer). What does this tell you about deploying differential privacy?

A) The Laplace mechanism is unsuitable for small groups, which should be protected using k-anonymity instead of added noise
B) Lowering ε further would shrink the error on the small subgroup, because ε is the mechanism's accuracy setting
C) The small subgroup has fewer records to average over, so collecting more data there would close the gap
D) Laplace noise scales with sensitivity and ε, not with the size of the true answer, so one ε costs small groups more

---

### 5. [Course 06 · Unit 4]
A global SHAP chart reports a mean |SHAP| of **0.204** for the feature `is_female`. Computed *within* ticket class, the same quantity is **0.300** in second class and **0.163** in third class. A regulator asks how much the model relies on sex when it decides about **third-class** passengers. What is the correct response?

A) Report 0.204, since it is computed on far more data and is therefore the more reliable estimate
B) Report 0.300 from second class, since a regulator should be shown the largest reliance on sex the model has
C) Report 0.163, and state that the global average of 0.204 in fact describes none of the three classes
D) Report that SHAP explains single predictions, so a per-class average of SHAP values is not a usable figure

---

### 6. [Course 06 · Unit 4]
An audit trail shows **29 decisions** that were automated although written policy required human review below a confidence of 0.70 (the deployed router was configured at 0.60). On those 29 decisions the model was right **62.1%** of the time — its worst band, against **78.9%** overall. Under the accountability framework taught in Course 06 Unit 4, what does this finding require?

A) A named human role is accountable for the gap, and the audit trail is what made it measurable months later
B) Accountability rests with the routing algorithm, since it issued all those decisions with no human involved
C) The band's 62.1% is normal variation around the 78.9% overall accuracy, so the trail shows no problem to fix
D) Retraining the model on those 29 cases resolves it, because the problem is model accuracy, not process

---

### 7. [Course 03 · Unit 5]
Course 03 Unit 5 drew a sample of n = 100 from the 714 recorded Titanic passenger ages and printed a 95% confidence interval of [26.8815, 32.7235] for the mean age. Repeating the whole study 2000 times, 96.4% of the intervals built this way contained the true population mean of 29.6991. Which statement do these results support?

A) There is a 95% probability that the true mean age of the 714 passengers lies inside [26.88, 32.72]
B) The 95% is a hit rate of the procedure across repeated studies, not a probability attached to this interval
C) About 95% of the 714 recorded passenger ages fall inside [26.88, 32.72], which is the quantity the level counts
D) Raising the level to 99% would narrow the interval, because greater confidence pins the true mean down more tightly

---

### 8. [Course 04 · Unit 1]
Course 04's Unit 1 regularization lesson predicted transaction `Amount` from 29 features using 8,000 training rows, and printed:

| Model | Test MSE | Test R² |
|---|---|---|
| Linear Regression | 4133.9568 | 0.8930 |
| Ridge (α = 0.01) | 4133.9591 | 0.8930 |
| Lasso (α = 0.1) | 4130.9723 | 0.8931 |

Alphas from 0.01 to 100 were tried for both. At its best alpha, Lasso kept **29 of 29** features. Which conclusion do these numbers support?

A) Neither penalty was tuned far enough; the search should be extended past α = 100 until one of the two beats the plain baseline
B) Lasso won, and its margin is L1 performing the feature selection that Ridge leaves undone here
C) V1–V28 are uncorrelated PCA components, so a penalty on their coefficients has no well-defined effect here
D) With 8,000 rows against 29 features the baseline is not overfitting, so shrinking coefficients adds bias and buys nothing

---

### 9. [Course 02 · Unit 1]
Course 02's Unit 1 libraries notebook doubled the same numbers twice — once as a Python list comprehension, once as one NumPy whole-array operation — and printed:

```
         N    list (ms)   NumPy (ms)   speed-up
        10       0.0001       0.0003       0.5x
       100       0.0009       0.0003       3.0x
     1,000       0.0123       0.0006      21.5x
    10,000       0.1195       0.0032      37.1x
   100,000       1.2403       0.0254      48.8x
 1,000,000      15.1218       0.2454      61.6x
```

Which statement is supported by this table?

A) NumPy's lead grows with N, and at N = 10 the list version is the faster of the two
B) The list version scales better, because its cost per element falls as N grows
C) Both converge to the same speed at large N, since each loop is run by the interpreter
D) NumPy runs about 100× faster here, the speed-up the notebook's own text quotes

---

### 10. [Course 01 · Unit 1 / Unit 2]
Course 01's `KnowledgeBase` stored facts and rules, and its agent applied the rules to derive new conclusions. What is a key component of a knowledge representation system?

A) A relational database table with indexed columns, plus a query language to search them
B) A labeled training dataset and a loss function
C) A priority queue of nodes ordered by a heuristic estimate of the cost that remains
D) A store of facts, a set of rules over them, and an inference mechanism

---

**End of paper. Hand nothing in. Stay for the worked answers.**
