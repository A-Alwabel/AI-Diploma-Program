# Cumulative Retrieval Quiz — Week 28

**Programme week 28 of 35 · Course 10 — AIAT 124 (Generative AI), Units 1–4**
**Taken in the last session of the week (session 112), in the final 15 minutes.**

---

**How this works**

- **15 minutes, in class, at the END of the session.** 7 minutes to answer, then 8 minutes in which
  your instructor works the correct answers aloud. The worked correction is not optional extra —
  it is the part that makes this worth doing.
- **Not graded.** No mark from this paper reaches your course grade. Write what you actually think.
- **Ten items.** Three on what you were taught this week and last week, three on material from about
  a month ago, four from earlier in the programme. Every item has been taught already.
- Write the **letter only**. Closed book. One best answer per item.

---

## Part A — This week and last week (Course 10, Generative AI)

### Item 1
Unit 1 fits a generative model (Gaussian Naive Bayes) and a discriminative model (logistic
regression) to the same two-class dataset. The generative model scores **97.2%** test accuracy; the
discriminative model scores **96.1%**. Which conclusion do those two numbers support?

A) The 1.1-point gap shows generative models classify better, so prefer them whenever accuracy matters.
B) Logistic regression could generate new samples too, if its decision boundary were inverted into a data distribution.
C) Accuracy is not what separates the two families — what separates them is that the generative model learns p(x) and can draw new samples from it.
D) The generative model was bound to win here: p(x|y) turns into a classifier by Bayes' rule, so it carries more information than a bare decision boundary.

---

### Item 2
You are training the GAN from Unit 1. After a few hundred steps the **discriminator's loss has
fallen to nearly 0 and stays there**, while the generator's loss climbs. What is happening, and what
does it mean for the generator?

A) The discriminator has saturated — it wins batch after batch — so the gradient reaching G through D vanishes and G stops improving.
B) Training has converged — a discriminator loss near zero is the equilibrium the adversarial game aims for.
C) The generator has mode-collapsed onto a single output, and a collapsed generator is what drives the discriminator's loss to zero.
D) The discriminator has overfitted the real images; the standard fix is to lower the generator's learning rate until the two losses cross.

---

### Item 3
In the β-VAE experiment (identical data, architecture and epochs, β alone changed), **β = 1**
finished at reconstruction **104.6** and KL **20.5**; **β = 4** finished at reconstruction **137.8**
and KL **7.2**. You need a VAE for anomaly detection that flags defects by **reconstruction error**.
Which run do you ship, and why?

A) β = 4 — its much lower KL means a latent space closer to N(0, I), and a more regular latent space reconstructs normal inputs more accurately overall.
B) β = 4 — a higher β disentangles the latent axes, and disentangled axes make anomalies easier to separate.
C) Either one — the two runs differ just in a loss weighting, so their decoders produce equivalent reconstructions.
D) β = 1 — the detector's signal is reconstruction error, and β = 4 raised it by about 32%, lifting the error floor a small defect has to clear.

---

## Part B — About a month ago (Course 09, Reinforcement Learning)

### Item 4
In Reinforcement Learning, Unit 1's value iteration ran a 3×3 grid with **−1 for every ordinary
step, +10 for entering the goal, −10 for entering the pit, and gamma = 0.90**. In the converged
table the tile immediately **above the pit** holds **6.20** — positive, even though one of its four
actions steps straight into the −10 pit. The tile to its right holds **8.00**. Which explanation is
correct?

A) The pit's −10 is discounted once per sweep, so by convergence 0.90 raised to the sweep count has shrunk it below −1.
B) The sweep skips terminal states, so no pit transition is generated for that tile and the −10 stays out of its backup.
C) The backup keeps the maximum over the four actions, and the best of them moves right, not down: −1 + 0.90 × 8.00 = 6.20.
D) The backup averages the four action targets instead of maximising, and the three non-pit actions outweigh the single −10.

---

### Item 5
In Reinforcement Learning, Unit 2 trained **SARSA** and **Q-learning** on CliffWalking with the same
seed and identical settings (alpha 0.5, gamma 1.0, epsilon 0.1, 500 episodes); the TD target line is
the sole difference. Greedy path length: **SARSA 17 steps, Q-learning 13**. Average return over the
last 100 **training** episodes, with epsilon still 0.1: **SARSA −24.49, Q-learning −47.96**. Which
reading of those four numbers is correct?

A) SARSA's greedy path is the shorter one, and it earned more in training because a shorter route pays fewer −1 step penalties per episode.
B) Q-learning's greedy path is the shorter one, and SARSA still earned more in training because its target prices in the exploratory steps taken.
C) Q-learning earned less while training because gamma = 1.0 leaves its max-target undiscounted, so the values it bootstraps from grow without bound.
D) Both agents converged on the same greedy path, and the 23-point gap in training return is down to the different random seeds the two runs were given.

---

### Item 6
In Reinforcement Learning, every value update in that course had the form `r + gamma * V(s')`. A
grid-world agent trained with **gamma = 0.99** walks a long route to a large delayed reward;
retrained with **gamma = 0.10** it grabs the nearest small reward instead. What does gamma control?

A) The step size of each update, so a small gamma makes the agent change its estimates slowly.
B) The rate at which exploration is traded for exploitation as training proceeds.
C) The number of steps of experience collected before an update is applied.
D) How much weight a future reward carries against an immediate one, near 0 being myopic.

---

## Part C — Earlier in the programme

### Item 7 — Course 03, Mathematics and Probability for ML
Unit 4 ran one classifier on the 569-biopsy breast-cancer data, changing how many principal
components it may see, scored throughout by the same 5-fold cross-validation:

| components | variance kept | 5-fold accuracy |
|---|---|---|
| 1 | 44.3% | 0.9121 |
| 2 | 63.2% | 0.9578 |
| 3 | 72.6% | 0.9491 |
| 5 | 84.7% | 0.9736 |
| 10 | 95.2% | 0.9807 |
| 30 | 100.0% | 0.9789 |

The same classifier on all 30 raw features, with no PCA at all, scores **0.9789**. Which conclusion
do these numbers support?

A) Each component adds accuracy in proportion to the variance it carries, so keeping all 30 is the best choice.
B) Accuracy flattens long before variance does — k = 5 already reaches 0.9736 while keeping 84.7% of the variance.
C) PCA hurt this classifier: the reduced models score below the 0.9789 that the 30 raw features reach on their own.
D) The dip at k = 3 shows the third component carries no variance, so it should be dropped from the model.

---

### Item 8 — Course 02, Python for Artificial Intelligence
Unit 1 ran A\* with the heuristic `h(n) = |ord(n) - ord(goal)|` and checked it against the true
remaining cost `h*`:

```
   A: h=6, h*=3  ->  OVERESTIMATES by 3
   B: h=5, h*=2  ->  OVERESTIMATES by 3
   E: h=2, h*=1  ->  OVERESTIMATES by 1
   G: h=0, h*=0  ->  OK
```

A\* then returned `A -> B -> E -> G`, which is the shortest path on that graph, having opened 6 of
the 7 nodes (BFS opened 7). What does this run establish about the heuristic?

A) h overestimates, so the optimality guarantee did not apply — the shortest path came back anyway.
B) h is admissible, because the path A\* returned is in fact the shortest path available on this graph.
C) The overestimates are uniform across nodes, so they cancel and the guarantee holds.
D) h is inadmissible, and that is what made A\* open 6 nodes where BFS had to open 7.

---

### Item 9 — Course 07, Natural Language Processing
Unit 4 measured how much gradient signal survives travelling backwards through a plain RNN with
typical weights: about **5×10⁻¹ after 1 step**, **6×10⁻⁶ after 10 steps**, and **7×10⁻³⁰ after 50
steps**. Which conclusion does that measurement support?

A) The recurrent weights grow exponentially during training, and gradient clipping in transformers is the fix for that.
B) The hidden state vector is too short to hold a long sentence, which is why transformers use a much longer one.
C) The signal linking far-apart words dies exponentially with distance; attention links two positions in one step.
D) The network's accuracy falls as sentences get longer, which is why transformers truncate their inputs to 512 tokens.

---

### Item 10 — Course 06, Ethics of Artificial Intelligence
Northpointe showed that COMPAS was **calibrated** — a given risk score meant the same re-offence
probability for Black and for white defendants. ProPublica showed that the **false-positive rates
differed**: 44.9% for Black defendants against 23.5% for white defendants. Which statement best
describes this situation?

A) Both are correct: with different base rates, no classifier can be calibrated and hold equal error rates at once.
B) Northpointe is right and ProPublica is not: a score that means the same thing for both groups is the fairness that counts.
C) ProPublica measured demographic parity, which is the fairness definition a court would apply to a sentencing tool.
D) Calibrating the scores separately within each group would let both fairness criteria hold at the same time.

---

**End of quiz — put your pen down and follow the worked answers.**
