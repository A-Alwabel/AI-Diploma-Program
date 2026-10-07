# Retrieval Quiz — Week 31

**Week 31 of 35 · Course 11 — AIAT 125 (Deploying AI Models)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Unit 4 opened on the "works on my machine" problem. What does **Docker** provide for ML deployment?

A) Rescheduling a failed container onto a healthy node  
B) Identical images from two builds of the same Dockerfile  
C) Portability of the platform, not just the runtime  
D) Containerization for a consistent runtime environment  

---

### Question 2

Unit 4's analogy ran: Dockerfile = recipe, image = the baked cake, container = serving a slice. What is the difference between a Docker **image** and a Docker **container**?

A) The image is a fixed template; a container is one running instance of it  
B) The container is the stored artifact; the image is the copy loaded into memory  
C) They are two names for the same artifact at two points in the build  
D) An image runs on the build host; a container is what runs on a remote host  

---

### Question 3

Unit 3 attached a target-tracking policy to a hosted endpoint: minimum 1 instance, maximum 10, scale when invocations per instance pass 1000 per minute. What does **auto-scaling** do?

A) It retrains the served model when monitored accuracy drops  
B) It adjusts the batch size the endpoint uses, to keep each response inside the budget  
C) It adds or removes compute instances as the incoming traffic rises and falls  
D) It rescales gradients during training so that large updates do not destabilise it  

---

### Question 4

The lesson's Fréchet-distance check, run inside one fixed PCA-feature pipeline, printed:

```
candidate set      Frechet distance (PCA features) — lower is better
real (held-out)          0.06
blurred                  2.29
noisy                    0.26
pure noise               3.82
```

A teammate's new digit generator scores **0.06** on that same pipeline, and they want to sign it off as a faithful generator on the strength of that number. What does the score establish?

A) It scores below both corrupted sets, so the generator has been shown to cover the ten digit classes as evenly as the real data does — a distribution-level metric penalises any lost diversity by construction.  
B) Its feature distribution sits as close to the reference as a second sample of real digits does — the floor of this measurement — which leaves a memorised training set or a dropped rare class undetected.  
C) A 0.06 can be quoted directly against the FID figures reported in GAN papers, since the formula is the same one and lower is better on the same scale no matter which feature extractor produced the vectors.  
D) Each generated digit is individually as crisp as a real one, since the distance averages a per-image quality score over the set, and a value of 0.06 leaves very little room for blur.  

---

### Question 5

Unit 2 contrasted a decoder-only model with an encoder-only one. What is the key architectural difference between **GPT** and **BERT**?

A) GPT is built from convolutions, while BERT is built from stacked attention layers  
B) BERT generates text one token at a time; GPT scores a finished sentence  
C) They share one architecture and differ in the corpus each was trained on  
D) GPT attends left-to-right for generation; BERT reads context in both directions  

---

### Question 6

Unit 5 compared a model-free agent with one that learns a model of the environment. What is the key advantage of **model-based RL**?

A) A learned model lets the agent plan or replay simulated steps, so fewer real ones are needed  
B) It removes the need to interact with the real environment, since the model supplies all of the data  
C) It reaches a higher final reward than a model-free agent given the same training budget  
D) It works without function approximation, so a table suffices for large state spaces  

---

### Question 7

The matrix-operations lesson redraws its fusion experiment on the 1,797 mean-centred digit images and adds a third route, `relu(X @ W1) @ W2`, with a ReLU between the two layers. The printed reading of the figure is:

```
Blue points (no activation): 2.0e-14 is the largest amount any of the 17,970 output numbers differs from the fused one-layer network.
Orange points (ReLU inserted): up to 11.8 away from the diagonal, on outputs that span roughly -19 to +18.
```

A classmate argues that the ReLU is a minor numerical detail and that the real lesson is which bracketing is cheaper. Which reading of these two printed gaps is correct?

A) Both gaps are rounding noise; the ReLU route sits further off because `max()` adds another rounded operation per entry  
B) The 2.0e-14 gap shows the layer-by-layer route drifts from the fused one, so even without a ReLU the two layers compute a slightly different function  
C) The 2.0e-14 gap says the two linear routes are one function; the 11.8 gap says the ReLU made a genuinely different model  
D) The orange points leave the diagonal because the digits were mean-centred, not because of the ReLU; on raw pixels the same ReLU would spread them as far  

---

### Question 8

Course 01 implemented a perceptron from scratch before moving to Keras. What is a perceptron?

A) A layer of neurons whose outputs feed into a second layer before a prediction is produced  
B) A rule base whose conditions are learned from data rather than written by a person  
C) A graph traversal that follows the highest-weight edge out of each node it reaches  
D) A single unit that takes a weighted sum of its inputs and passes it through a threshold  

---

### Question 9

The lesson trains three recurrent layers of width 64 on the same `Embedding(2000, 64)`, the same **2,000** training reviews, the same **12** epochs and the same seed. Best validation accuracy: `GRU` **0.720** (final 0.692), `SimpleRNN` **0.544** (final 0.520). A classmate says the GRU beats the gateless layer for the same reason an LSTM does. Which reason is that?

A) It takes in the 100 padded positions at once rather than one word at a time, so the opening words are not overwritten by the ones that come later  
B) Its gates make each step a controlled, trainable update of the state, so a gradient can reach earlier words along a near-additive path  
C) It carries fewer recurrent weights than the SimpleRNN's 8,256 — so with 2,000 reviews there is less for it to overfit  
D) It runs over each review forwards and then backwards, so the words from the start are the freshest when the verdict is made  

---

### Question 10

The Unit 2 outliers lesson profiled the cleaned **889**-row `Fare` column and printed mean **32.10**, median **14.45**, quartiles **7.90** to **31.00** and a maximum of **512.33**. Its IQR rule flagged **114** fares (12.8% of passengers), **102** of them first class. A colleague's slide carries one line: "average fare: 32.10 pounds". Which revision does that profiling support?

A) Keep 32.10 but recompute it after dropping the 114 IQR-flagged fares first, so the mean then describes the typical passenger rather than the first-class tail  
B) Replace it with the median 14.45 and the 7.90 to 31.00 quartile range, and say the column is right-skewed, since 32.10 sits above the third quartile  
C) Standardise `Fare` to mean 0 and standard deviation 1 before quoting the average, so the first-class tail no longer pulls the reported figure away from the centre of the column  
D) Keep 32.10 and add the standard deviation 49.70, so readers can see the spread around the average and judge the typical fare for themselves  

---
