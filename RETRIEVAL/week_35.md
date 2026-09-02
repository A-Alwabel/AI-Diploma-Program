# Cumulative Retrieval Quiz — Week 35

**Programme week 35 of 35 · Course 12 — AIAT 126 (Graduation Project), Units 4–5.**
**Taken in session 138, in the final 15 minutes.**
**Optional — your instructor may drop this one.** Week 35 is the last teaching week and the defense
follows immediately, so nothing comes after this quiz for it to consolidate. If it is run, it is run
for the same reason as the other thirty-four: to make you retrieve, and to hear the worked answer.

---

**How this works**

- **15 minutes, in class, at the END of the session.** 7 minutes to answer, then 8 minutes in which
  your instructor works the correct answers aloud.
- **Not graded.** No mark from this paper reaches your capstone milestone gates or your defense.
- **Ten items.** Three on this week and last week, three from about a month ago, four from earlier in
  the programme.
- Write the **letter only**. Closed book. One best answer per item.

---

## Part A — This week and last week (Course 12, Graduation Project)

### Item 1
Unit 4 compared three algorithms and printed validation F1: Logistic Regression **0.8958**, Random
Forest **0.9175**, SVM **0.8830**. Which model was selected, on which split, and by which metric?

A) Logistic Regression, on the test set, by overall accuracy
B) Random Forest, on the validation set, by F1 (0.9175)
C) SVM, on the training set, by precision on the positive class
D) Random Forest, on the test set, by ROC-AUC

---

### Item 2
Unit 4's final test evaluation gave F1 **0.9020** against a validation F1 of **0.9246** at the same
threshold — a gap of **−0.0227**. What is the correct action?

A) Re-tune the threshold on the test set until the gap between the two closes
B) Report the validation number, since it is the higher of the two figures
C) Re-split the data and repeat until the gap comes out positive
D) Report the test number, note that the gap is small, and stop there

---

### Item 3
Unit 4's threshold tuning found **0.410** on the validation set, raising validation F1 from **0.9175 to
0.9246**. The **decision threshold** is best described as:

A) A parameter of the decision, tuned on validation after the model is trained
B) A hyperparameter of the random forest itself, learned while the trees are grown
C) A property of the test set, fixed once that split has been drawn
D) A constant of 0.5 that the library sets and the analyst leaves alone

---

## Part B — About a month ago (Course 11, AI Model Deployment)

### Item 4
Unit 4 opened on the "works on my machine" problem. What does **Docker** provide for ML deployment?

A) Portability of the platform, not just the runtime
B) Identical images from two builds of the same Dockerfile
C) Containerization for a consistent runtime environment
D) Rescheduling a failed container onto a healthy node

---

### Item 5
Unit 4's analogy ran: Dockerfile = recipe, image = the baked cake, container = serving a slice. What is
the difference between a Docker **image** and a Docker **container**?

A) They are two names for the same artifact at two points in the build
B) An image runs on the build host; a container is what runs on a remote host
C) The container is the stored artifact; the image is the copy loaded into memory
D) The image is a fixed template; a container is one running instance of it

---

### Item 6
Unit 3 attached a target-tracking policy to a hosted endpoint: minimum 1 instance, maximum 10, scale
when invocations per instance pass 1000 per minute. What does **auto-scaling** do?

A) It retrains the served model when monitored accuracy drops
B) It adds or removes compute instances as the incoming traffic rises and falls
C) It adjusts the batch size the endpoint uses, to keep each response inside the budget
D) It rescales gradients during training so that large updates do not destabilise it

---

## Part C — Earlier in the programme

### Item 7 — Course 03, Mathematics and Probability for ML
Minimising `f(x) = x²` from `x = 5` for 30 steps, Unit 2 changed only the learning rate and printed:
lr = 0.01 → x = 2.72742; lr = 0.1 → x = 0.0061897; lr = 0.9 → x = 0.0061897; lr = 1.0 → x = 5 with loss
25; lr = 1.1 → x = 1186.88. On a log axis the **lr = 0.9** loss curve lies exactly on top of the
**lr = 0.1** curve. What does that coincidence tell you?

A) lr = 0.9 takes smaller steps than lr = 0.1, which is why the two runs finish at the same value of x.
B) A smoothly falling loss curve rules out instability, so the rate could be raised from 0.9 to 1.0 for speed.
C) The loss depends on |x| alone, so a falling curve can still hide a run that crosses the minimum each step.
D) lr = 0.9 has settled into a second minimum of f that happens to sit at the same height as the first one.

---

### Item 8 — Course 01, Introduction to AI and Applications
Unit 4's neuron lesson placed a non-linearity between a layer's weighted sum and the next layer. Which
group lists three functions used in that role?

A) ReLU, Sigmoid and Tanh
B) Adam, SGD and RMSprop
C) MSE, Cross-Entropy and Hinge
D) Dropout, Batch Norm and Early Stopping

---

### Item 9 — Course 07, Natural Language Processing
In Unit 4 the pretrained English sentiment model labelled *"I have no opinion about this product"*
**NEGATIVE at 0.9997**, and gave an Arabic sentence **P(POSITIVE) = 0.42** after splitting it into 5.5
word-pieces per word. What do these two results, read together, show?

A) The model is well calibrated: confident where the sentiment is clear, and hesitant where it is genuinely ambiguous.
B) The Arabic sentence was correctly judged neutral, which shows the model handles other languages acceptably.
C) Both outputs are casing failures, and both disappear once the text is lowercased before it is scored.
D) The model has no neutral class, so it picks a side; and 0.42 on Arabic means "nothing readable", not "unsure".

---

### Item 10 — Course 08, Deep Learning
A trained FP32 model is converted to INT8. The stored file falls from **5,597 to 4,557 bytes** and
validation accuracy is unchanged at **0.840**. Which optimization technique is this, and what did it
change?

A) Pruning — the number of weights, by zeroing the smallest
B) ONNX export — the file format, so the model runs outside its framework
C) Quantization — the number of bits used to store each weight value
D) Distillation — the architecture, by training a smaller model to copy a larger

---

**End of quiz — put your pen down and follow the worked answers.**
