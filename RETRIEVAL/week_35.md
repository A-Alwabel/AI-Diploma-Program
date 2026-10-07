# Retrieval Quiz — Week 35

**Week 35 of 35 · Course 12 — AIAT 126 (Graduation Project)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Unit 4 compared three algorithms and printed validation F1: Logistic Regression **0.7176**, Random Forest **0.7612**, SVM **0.7903**. Which model was selected, on which split, and by which metric?

A) Logistic Regression, on the test set, by overall accuracy  
B) SVM, on the validation set, by F1 (0.7903)  
C) Random Forest, on the training set, by precision on the positive class  
D) SVM, on the test set, by ROC-AUC  

---

### Question 2

Unit 4's final test evaluation gave F1 **0.7302** against a validation F1 of **0.8125** at the same tuned threshold — a gap of **−0.0823**. What is the correct action?

A) Re-tune the threshold on the test set until the gap between the two numbers closes up  
B) Report the validation number, since it is the higher of the two figures  
C) Re-split the data and repeat until the gap comes out positive  
D) Report the test number, note that the validation figure was tuned on, and stop there  

---

### Question 3

Unit 4's threshold tuning found **0.461** on the validation set, raising validation F1 from **0.8000** at the default 0.50 to **0.8125**. The **decision threshold** is best described as:

A) A parameter of the decision, tuned on validation after the model is trained  
B) A hyperparameter of the SVM itself, learned from the data while the model is fitted  
C) A property of the test set, fixed once that split has been drawn  
D) A constant of 0.5 that the library sets and the analyst leaves alone  

---

### Question 4

Unit 4 opened on the "works on my machine" problem. What does **Docker** provide for ML deployment?

A) Portability of the platform, not just the runtime  
B) Identical images from two builds of the same Dockerfile  
C) Containerization for a consistent runtime environment  
D) Rescheduling a failed container onto a healthy node  

---

### Question 5

Unit 4's analogy ran: Dockerfile = recipe, image = the baked cake, container = serving a slice. What is the difference between a Docker **image** and a Docker **container**?

A) They are two names for the same artifact at two points in the build  
B) An image runs on the build host; a container is what runs on a remote host  
C) The container is the stored artifact; the image is the copy loaded into memory  
D) The image is a fixed template; a container is one running instance of it  

---

### Question 6

Unit 3 attached a target-tracking policy to a hosted endpoint: minimum 1 instance, maximum 10, scale when invocations per instance pass 1000 per minute. What does **auto-scaling** do?

A) It retrains the served model when monitored accuracy drops  
B) It adds or removes compute instances as the incoming traffic rises and falls  
C) It adjusts the batch size the endpoint uses, to keep each response inside the budget  
D) It rescales gradients during training so that large updates do not destabilise it  

---

### Question 7

The gradient-descent lesson prints, next to each learning rate, the factor |1 − 2·lr| that multiplies x at each step when minimising f(x) = x² from x = 5 for 30 steps: 0.98 for lr = 0.01, 0.80 for lr = 0.1, 0.80 for lr = 0.9, 1.00 for lr = 1.0 and 1.20 for lr = 1.1. The losses after 30 steps are 7.43883, 3.83124e-05, 3.83124e-05, 25 and 1.40869e+06 respectively. A colleague watching a training run sees a loss curve that is a straight line down on a log axis and concludes the step size is well chosen. Using the printed factors, which objection is justified?

A) A factor of 0.80 means both runs move x by the same distance each step, so lr = 0.9 is a relabelled lr = 0.1 and no objection applies  
B) A straight line down shows the factor is below 1, so the rate can safely be raised toward the 1.00 row for a faster descent  
C) A factor of 0.80 belongs to both lr = 0.1 and lr = 0.9, so the same straight line can come from a run that crosses zero at each step  
D) The 3.83124e-05 reached at lr = 0.9 beats the 7.43883 at lr = 0.01 because the larger rate found a second, deeper minimum of f  

---

### Question 8

Unit 4's neuron lesson placed a non-linearity between a layer's weighted sum and the next layer. Which group lists three functions used in that role?

A) ReLU, Sigmoid and Tanh  
B) Adam, SGD and RMSprop  
C) MSE, Cross-Entropy and Hinge  
D) Dropout, Batch Norm and Early Stopping  

---

### Question 9

The same Unit 4 probe scored *"The meeting is scheduled for Tuesday at 3pm"* **POSITIVE at 0.9301**, and the Arabic sentence glossed *"the meeting is Tuesday at 3"* at **P(POSITIVE) = 0.3695** after chopping it into **6.4** word-pieces per word. Same content, two very different scores — what explains the pair?

A) The English fact had to leave through one of two exits, since there is no neutral class; the Arabic one was read letter by letter, so 0.3695 carries no information  
B) The model understood the English sentence as mildly positive and the Arabic one as close to neutral, so both numbers are fair readings of what the two sentences say  
C) The model is well calibrated: 0.9301 sits below the 0.9999 it gave a real opinion because a schedule is a weaker positive than praise  
D) Both scores come from the lowercasing the `uncased` checkpoint applies; the `cased` checkpoint would read the capital letters and fix both  

---

### Question 10

In the lesson's worked example, a trained digits classifier is converted with a single library call and no retraining. Measured on the same laptop CPU: stored size **70.2 KB → 22.2 KB** (**3.2×** smaller), accuracy **96.7%** before and after, and latency **0.228 → 0.360 ms/batch** — the converted model runs **1.6×** slower. Name the technique and the property of the model it modified.

A) Pruning — the number of surviving weights, with the smallest ones zeroed out so the file has fewer values to hold  
B) Quantization — the precision each weight is stored at, FP32 down to INT8, with a scale and zero-point kept per layer  
C) Distillation — the architecture, with a smaller student trained to match the 96.7% teacher's soft outputs  
D) ONNX export — the file format, so the model runs outside PyTorch, which is also why inference got slower in the new runtime  

---
