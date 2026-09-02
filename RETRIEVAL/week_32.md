# Cumulative Retrieval Quiz — Week 32

**Programme week 32 of 35 · Course 11 — AIAT 125 (AI Model Deployment), Units 4–5.**
**Taken in session 126, in the final 15 minutes.**

---

**How this works**

- **15 minutes, in class, at the END of the session.** 7 minutes to answer, then 8 minutes in which
  your instructor works the correct answers aloud.
- **Not graded.** No mark from this paper reaches your course grade.
- **Ten items.** Three on this week and last week, three from about a month ago, four from earlier in
  the programme.
- Write the **letter only**. Closed book. One best answer per item.

---

## Part A — This week and last week (Course 11, AI Model Deployment)

### Item 1
Your GitHub Actions workflow has four jobs chained with `needs:` — run `pytest`, train the model,
build and push the Docker image, then `kubectl set image`. Every job passes and the rollout completes,
but the model now serving traffic is only 60% accurate. Which missing stage would have prevented it
from reaching production?

A) A model-validation gate that fails the build when the metrics miss threshold
B) A smoke test that issues known-answer requests to the live endpoint after rollout
C) A rollback step that reverts the Deployment when one of the later jobs fails
D) Image tags carrying the commit SHA so each release stays traceable

---

### Item 2
A deployed classifier's dashboards look healthy: error rate under 1%, p99 latency inside the SLO, mean
prediction confidence 0.9, and a KS test on each input feature returns p > 0.05. Then the first
ground-truth labels arrive and accuracy has fallen from **0.95 to 0.72**. What is the most likely
explanation?

A) The service has stopped receiving traffic, so the accuracy figure is unreliable
B) Data drift in the inputs; retraining on recent data restores accuracy
C) CPU saturation on the serving pods is degrading the quality of predictions
D) Concept drift: P(Y|X) has changed, which input-side tests do not detect

---

### Item 3
Unit 5 walked a release through the stages 5% → 25% → 100% with an automatic rollback at each gate.
How does a **canary deployment** release a new model version?

A) It replaces the old version at once, then watches the dashboards for regressions
B) It runs both versions side by side and routes each user to whichever one answers first
C) It sends a small share of live traffic to the new version and widens on good metrics
D) It ships to the development environment first and promotes after manual sign-off

---

## Part B — About a month ago (Course 10, Generative AI)

### Item 4
Unit 1 fits a generative model (Gaussian Naive Bayes) and a discriminative model (logistic regression)
to the same two-class dataset. The generative model scores **97.2%** test accuracy; the discriminative
model scores **96.1%**. Which conclusion do those two numbers support?

A) The generative model was bound to win here: p(x|y) turns into a classifier by Bayes' rule, so it carries more information than a bare decision boundary.
B) Accuracy is not what separates the two families — what separates them is that the generative model learns p(x) and can draw new samples from it.
C) The 1.1-point gap shows generative models classify better, so prefer them whenever accuracy matters.
D) Logistic regression could generate new samples too, if its decision boundary were inverted into a data distribution.

---

### Item 5
You are training the GAN from Unit 1. After a few hundred steps the **discriminator's loss has fallen
to nearly 0 and stays there**, while the generator's loss climbs. What is happening, and what does it
mean for the generator?

A) The generator has mode-collapsed onto a single output, and a collapsed generator is what drives the discriminator's loss to zero.
B) Training has converged — a discriminator loss near zero is the equilibrium the adversarial game aims for.
C) The discriminator has saturated — it wins batch after batch — so the gradient reaching G through D vanishes and G stops improving.
D) The discriminator has overfitted the real images; the standard fix is to lower the generator's learning rate until the two losses cross.

---

### Item 6
In the β-VAE experiment (identical data, architecture and epochs, β alone changed), **β = 1** finished
at reconstruction **104.6** and KL **20.5**; **β = 4** finished at reconstruction **137.8** and KL
**7.2**. You need a VAE for anomaly detection that flags defects by **reconstruction error**. Which
run do you ship, and why?

A) β = 1 — the detector's signal is reconstruction error, and β = 4 raised it by about 32%, lifting the error floor a small defect has to clear.
B) β = 4 — a higher β disentangles the latent axes, and disentangled axes make anomalies easier to separate.
C) Either one — the two runs differ just in a loss weighting, so their decoders produce equivalent reconstructions.
D) β = 4 — its much lower KL means a latent space closer to N(0, I), and a more regular latent space reconstructs normal inputs more accurately overall.

---

## Part C — Earlier in the programme

### Item 7 — Course 01, Introduction to AI and Applications
Unit 1's expert-system lesson built a system that answered questions without being trained on data.
What is a key component of a knowledge representation system?

A) A relational database table with indexed columns
B) A labelled training dataset and a chosen loss function
C) A priority queue ordered by a heuristic function
D) Facts, rules, and a mechanism that infers from them

---

### Item 8 — Course 03, Mathematics and Probability for ML
On 89 held-out diabetes patients, Unit 3 prints **MAE 42.79**, **RMSE 53.85**, a mean signed error of
**−3.91**, and reports that the 10 worst-predicted patients carry **44.3%** of the total squared error.
What does the gap between MAE and RMSE tell you about this model?

A) A small group of large errors inflates RMSE, so the typical patient is missed by about 43 rather than 54.
B) The model over-predicts by roughly 11 units on each patient, which is what the gap between the two metrics measures.
C) The model accounts for 53.85% of the variation in the targets, which is the quantity a root-mean-squared error reports.
D) RMSE and MAE are on different scales, so RMSE has to be squared before the two numbers can be compared.

---

### Item 9 — Course 07, Natural Language Processing
Unit 1 split a paragraph on whitespace and counted the words. The frequency table gave each word a
count of 1 — although *language* and *nlp* both occur **twice** in that paragraph. Which explanation is
correct?

A) The stop-word list deleted one occurrence of each of those two words before they were counted up.
B) `language.` and `(nlp)` stayed separate tokens from `language` and `nlp`, splitting each count.
C) A `Counter` records each distinct word once per document, however often the word occurs.
D) Lowercasing merged the two occurrences of each word into a single token before counting.

---

### Item 10 — Course 06, Ethics of Artificial Intelligence
Your company is placing a CV-screening model that ranks job applicants on the EU market. Under the EU
AI Act risk tiers taught in Unit 5, what follows?

A) Limited risk: the duty is a notice telling applicants that an AI system is involved
B) Prohibited: the Act lists automated decisions about employment among its Article 5 banned practices
C) Minimal risk: the system produces a ranking and a human recruiter still takes the hiring decision
D) High risk: data governance, logging, human oversight and a conformity assessment apply first

---

**End of quiz — put your pen down and follow the worked answers.**
