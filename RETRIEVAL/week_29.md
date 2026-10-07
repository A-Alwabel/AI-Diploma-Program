# Retrieval Quiz — Week 29

**Week 29 of 35 · Course 10 — AIAT 124 (Generative Artificial Intelligence) and Course 11 — AIAT 125 (Deploying AI Models)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

A marketplace wants a fresh banner image for each of its listings every night, inside a fixed maintenance window on the GPUs it already owns. A colleague proposes the Unit 3 diffusion model and argues its sampling cost will shrink on its own: the training loss fell `0.2712 → 0.1229 → 0.0956` over three epochs, so a better-trained denoiser should need fewer denoising steps. In the notebook, the from-scratch sampler walked **t = 199 down to t = 0** for each image, while a GAN produces an image in one forward pass. Which reasoning should drive the family choice for this job?

A) The falling MSE is the right signal: a denoiser that predicts noise more accurately can skip steps safely, so diffusion's per-image cost converges on the GAN's as training continues and the maintenance window stops being a constraint.  
B) Step counts are beside the point for a batch job: how many images fit in the window is set by output resolution and batch size, so pick whichever family gives the sharper banners and tune the batching afterwards.  
C) The step count comes from the schedule, not the weights — the sampler walks t = 199 down to 0 whatever the loss reads — so diffusion's cost scales with its steps and the one-pass GAN is the throughput choice for this nightly job.  
D) A VAE decoder is the one-pass option to prefer here: it generates in a single decoder pass, and its pixel-wise reconstruction loss is what keeps each banner crisp enough for a product page, without the GAN's training instability.  

---

### Question 2

Unit 4's Titanic audit trained a survival model with `Sex` and again without it. The sex-aware model predicted survival for **90.7%** of women and **8.8%** of men; the blind model for **35.1%** and **21.6%**. Among passengers who actually survived, the aware model found **97.1%** of the women and **24.2%** of the men; the blind model **44.3%** and **48.5%**. A team lead wants to ship the blind model and stop collecting the attribute altogether, "so nobody can say we used it". What do these figures say about that plan?

A) The plan is sound: with no `Sex` column there is no route from sex to the prediction, so the 35.1% against 21.6% is sampling noise on a small test split that a larger manifest would wash out, and the audit has already done its job.  
B) The plan is sound on the second metric: 44.3% against 48.5% shows the blind model treats surviving women and surviving men nearly alike, so equal opportunity is satisfied and the attribute can safely be retired from the pipeline.  
C) The figures show the gap closed because the model degraded: a classifier that predicts 'died' for everyone would also show matching rates for the two groups, and the blind model's falling rates are drifting toward that.  
D) The blind model still predicts survival for women more often than for men, so the disparity came through correlated features — and without the attribute the team could no longer measure it: the audit it would be giving up.  

---

### Question 3

Course 11 opened this week by separating training from shipping. What is **model deployment**?

A) Saving the trained model to a file so that it can be reloaded later  
B) Measuring the model's accuracy on a held-out test set  
C) Retraining the model on the full dataset before release  
D) Making a trained model reachable by users or other services  

---

### Question 4

Unit 3 trained two tabular Q-learning agents on slippery FrozenLake — same algorithm, same environment, different hyperparameters — and printed:

```
Well-tuned run  : final rolling std = 0.500 | final rolling mean = 0.495
Badly-tuned run : final rolling std = 0.099 | final rolling mean = 0.010

Greedy evaluation on 1000 fresh episodes:
  Well-tuned agent  : 0.726 success rate
  Badly-tuned agent : 0.040 success rate
```

A dashboard that plots only the rolling standard deviation flags the **badly-tuned** run as the more stable of the two. What is the error?

A) The two standard deviations were computed over different rolling window lengths, so the two figures are not on a comparable scale  
B) With a 0/1 reward the spread is mechanically tied to the mean, so a run stuck at 0.010 has almost no spread; 0.099 signals failure  
C) Rolling standard deviation describes the exploring behaviour policy, so both runs would show the same spread once exploration is switched off  
D) The well-tuned run's 0.500 is an artefact of its greedy evaluation at 0.726; the training std should be recomputed from the evaluation episodes  

---

### Question 5

The Unit 4 notebook on tuning exploration parameters sweeps four epsilon settings on the same five-variant A/B test, **50 independent runs per epsilon**, then asks how often a lone run would have picked each setting. Three rows of its table, plus the tally from its closing cell:

```
   ε    |  mean ± std   |  min … max across runs
  0.05 |   599.6 ±  76.2 |   314 …   697
   0.1 |   623.7 ±  50.1 |   475 …   691
   0.3 |   610.8 ±  35.7 |   508 …   673

Single-run winners: ε=0.01: 6, ε=0.05: 15, ε=0.1: 23, ε=0.3: 6
The 50-run mean picks ε = 0.1; a single run agrees only 23/50 of the time.
```

A classmate insists: *'epsilon = 0.05 can beat epsilon = 0.1 — look, its top run hit 697 and 0.1 peaked at 691.'* Which reply refutes the claim most directly?

A) Top run against top run is a one-draw comparison: the 50-run means (599.6 vs 623.7) and the single-run win tally (15 vs 23) both put ε = 0.1 ahead, and 23/50 is the printed warning.  
B) A maximum of 697 does not belong in the ε = 0.05 row, whose mean is 599.6; a single run of that setting should stay within one standard deviation (±76.2) of it.  
C) Neither a top run nor a mean settles it, because total reward is the wrong statistic for exploration rates; the whole sweep would have to be redone in cumulative regret before any ranking is made.  
D) The spread column should decide it, and ε = 0.3 has the tightest band (±35.7) and the highest floor (508), so neither ε = 0.05 nor ε = 0.1 deserved to be crowned as the best setting in the first place.  

---

### Question 6

Unit 2 estimated state values two ways on the same environment: one method waited until an episode ended, the other updated after every step. How does the **Monte Carlo** method estimate a state's value?

A) By bootstrapping: it updates each estimate toward the reward plus the discounted value of the next state  
B) By sweeping the whole state space with the Bellman equation, using a known transition model  
C) By averaging the returns actually observed from complete episodes that passed through the state  
D) By fitting a neural network to the observed rewards and reading its prediction for that state  

---

### Question 7

From the same sample of 100 recorded Titanic ages, the confidence-interval lesson prints a 90% interval of [27.3582, 32.2468] (width 4.8886) and a 99% interval of [25.9361, 33.6689] (width 7.7327). When it redoes the whole study 2000 times, 92.5% of the 90% intervals and 99.6% of the 99% intervals capture the population mean, and in the panel that draws 100 of those repeats, 3 intervals are shown in crimson. A student writes: 'There is a 99% chance the true mean age is between 25.9361 and 33.6689.' Which statement about that sentence is right?

A) Acceptable: 99.6% of the 2000 repeated intervals held the mean, so roughly 99% is also the right probability for this one  
B) Wrong: the 99% is the capture rate of the procedure across repeats — measured here as 99.6% — not the odds for this one interval  
C) Wrong: the level counts recorded ages, so the sentence should say that 99% of the 714 ages lie between 25.9361 and 33.6689  
D) Acceptable, and understated: the wider 99% interval (7.7327 against 4.8886) carries more knowledge about the mean, which is why its coverage rose to 99.6%  

---

### Question 8

Unit 2 computed the probability of a disease given a positive test from the prior, the sensitivity and the false-positive rate. What role does Bayesian probability play in an AI system?

A) It updates a belief as evidence arrives, and reports the result as a probability  
B) It removes uncertainty from the model, so that its predictions become deterministic  
C) It confirms the diagnosis whenever the test result comes back positive  
D) It computes the probability of a hypothesis before evidence has been observed  

---

### Question 9

You are reviewing a slide built from the Unit 3 best-practices lesson. Its bar chart of 2018 quarterly 911 dispatches shows a visible plunge in Q2, yet the check printed under the very same data reads: *"the whole year sits within 8.8% of its own mean"*. The data is the bundled 1-in-27 sample of the call log. How do you reconcile the chart with the printout, and what should the slide do?

A) The 8.8% is measured against the mean while the bars show raw counts, so the chart is right and the printout understates the swing; keep the bars as drawn and delete the sentence  
B) The 1-in-27 sampling inflates quarter-to-quarter variation in the counts, so the chart exaggerates; multiply each quarter by 27 before plotting so the bars settle  
C) The axis made the plunge, not the data: `set_ylim` starts just under the lowest quarter, so a year within 8.8% of its mean fills the frame; redraw from zero or flag the zoom  
D) Quarters differ in length by a few days, which the raw counts do not correct for; convert each bar to calls per day and the plunge will shrink to its true size  

---

### Question 10

In the per-digit error chart of the lesson, both models were fitted on the identical **5,000** MNIST training images. Logistic regression misreads **143** of the test threes; the network with **128** ReLU hidden units misreads **73** of them, and it makes fewer errors on 9 of the 10 digits — digit **4** is the exception (**81** errors for logistic regression against **89** for the network). Which account of *how each model uses a pixel* explains this pattern?

A) The network needs fewer labelled threes to fit well, because its hidden units share what they learn across the ten digit classes, while logistic regression has to fit each class on its own  
B) The network's loss surface is convex, so Adam reaches the global minimum, while the logistic-regression solver stopped short at `max_iter=500` on the harder digits  
C) The network trains on pixels divided by 255 while logistic regression sees `StandardScaler` output, and raw-scale pixels preserve more of the stroke information  
D) Logistic regression scores each pixel with one fixed weight, so a slanted or off-centre 3 misses its template; the hidden layer combines pixels non-linearly and recovers it  

---
