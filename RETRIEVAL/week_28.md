# Retrieval Quiz — Week 28

**Week 28 of 35 · Course 10 — AIAT 124 (Generative Artificial Intelligence)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

A teammate reruns Unit 1's side-by-side experiment with a new random seed, and this time **logistic regression edges out Gaussian Naive Bayes** on the held-out split. The team is choosing a model for a spam filter that must also flag mail unlike anything it has seen before, and the teammate says the rerun settles it in favour of logistic regression. Which piece of lesson evidence decides the question?

A) The accuracy printout: the model that scores higher on the held-out split has learned the data better, so a rerun that puts logistic regression ahead settles the choice in its favour for this filter as well.  
B) The right-hand panel: far from its boundary, logistic regression still answers confidently — it stored no picture of where data lives — so an accuracy swing does not make it a model that can flag unfamiliar mail.  
C) The left-hand panel: the Gaussian model's invented points land on top of the real ones, which shows that a generative model will also be the more accurate classifier once the random seed is held fixed across reruns.  
D) The probability field in the right-hand panel: an uncertain p(y|x) carries the same information as a low p(x), so logistic regression already flags unfamiliar mail without modelling the data distribution.  

---

### Question 2

Two loss readouts printed by Unit 1's GAN notebook:

```
2-D toy run   — Final G loss: 0.6610   D loss: 1.3927
MNIST run     — Epoch 1/5 — D_loss=0.8774  G_loss=1.4142
                Epoch 5/5 — D_loss=0.5101  G_loss=2.8917
```

A classmate says the 2-D run is the one in trouble, because its discriminator posts the larger loss. Which reading of the two logs is right?

A) The 2-D run is the one in trouble: a discriminator posting a larger loss than its generator has lost the game and stopped teaching it anything, and the repair is extra D updates per G step until D's loss falls back below G's.  
B) Both runs are healthy: the MNIST discriminator's falling loss shows it is learning the digits, and a generator loss that climbs to 2.8917 simply means G is now being graded by a stricter judge, which is how it improves.  
C) The 2-D run sits at the balance point — a D loss near 1.39 means D cannot tell real from fake — while the MNIST trend is the one to watch: D's loss falls as G's rises, and a D that wins outright starves G of gradient.  
D) The MNIST run has mode-collapsed: a generator loss that climbs while D's falls is the signature of G producing one output over and over, which the discriminator then learns to reject with growing confidence.  

---

### Question 3

The β-VAE experiment's per-epoch table (same data, same architecture, same epoch count; β is the one thing that changed):

```
epoch |  recon b=1   KL b=1 |  recon b=4   KL b=4
    1 |      202.7     10.8 |      219.3      2.7
    3 |      113.6     19.2 |      146.9      6.3
```

A product team wants a **design tool with latent sliders** — a user drags latent coordinates and watches the output change. Which run do they take, and on what grounds?

A) β = 1 — its reconstruction is lower at both epochs, and a slider tool is judged on how faithfully each decoded image matches a real digit, so the run with the sharper decoder is clearly the one to put behind the sliders.  
B) β = 4 — a KL of 6.3 against 19.2 shows that each latent axis now encodes one human-readable factor, so the sliders can be labelled thickness, slant and so on straight from the training run.  
C) Either run — the sliders act on the decoder, and both decoders saw the same images for the same number of epochs, so dragging a coordinate produces much the same change in each model.  
D) β = 4 — its KL sits far below β = 1's from the first epoch, so its latent is pressed closer to N(0, I); that regularity is what sliders need, and whether the axes are disentangled is a separate claim to measure.  

---

### Question 4

In Reinforcement Learning, Unit 1's value iteration ran a 3×3 grid with **−1 for every ordinary step, +10 for entering the goal, −10 for entering the pit, and gamma = 0.90**. In the converged table the tile immediately **above the pit** holds **6.20** — positive, even though one of its four actions steps straight into the −10 pit. The tile to its right holds **8.00**. Which explanation is correct?

A) The pit's −10 is discounted once per sweep, so by convergence 0.90 raised to the sweep count has shrunk it below −1  
B) The sweep skips terminal states, so no pit transition is generated for that tile and the −10 stays out of its backup  
C) The backup keeps the maximum over the four actions, and the best of them moves right, not down: −1 + 0.90 × 8.00 = 6.20  
D) The backup averages the four action targets instead of maximising, and the three non-pit actions outweigh the single −10  

---

### Question 5

In Reinforcement Learning, Unit 2 trained **SARSA** and **Q-learning** on CliffWalking with the same seed and identical settings (alpha 0.5, gamma 1.0, epsilon 0.1, 500 episodes); the TD target line is the sole difference. Greedy path length: **SARSA 17 steps, Q-learning 13**. Average return over the last 100 **training** episodes, with epsilon still 0.1: **SARSA −24.49, Q-learning −47.96**. Which reading of those four numbers is correct?

A) SARSA's greedy path is the shorter one, and it earned more in training because a shorter route pays fewer −1 step penalties per episode  
B) Q-learning's greedy path is the shorter one, and SARSA still earned more in training because its target prices in the exploratory steps taken  
C) Q-learning earned less while training because gamma = 1.0 leaves its max-target undiscounted, so the values it bootstraps from grow without bound  
D) The two agents converged on the same greedy path, and the 23-point gap in training return is down to the different random seeds the two runs were given  

---

### Question 6

In Reinforcement Learning, every value update in that course had the form `r + gamma * V(s')`. A grid-world agent trained with **gamma = 0.99** walks a long route to a large delayed reward; retrained with **gamma = 0.10** it grabs the nearest small reward instead. What does gamma control?

A) The step size of each update, so a small gamma makes the agent change its estimates slowly  
B) The rate at which exploration is traded for exploitation as training proceeds  
C) The number of steps of experience collected before an update is applied  
D) How much weight a future reward carries against an immediate one, near 0 being myopic  

---

### Question 7

The PCA lesson's first cell prints the explained-variance ratios of the top three components of the standardized 569-biopsy data as 44.3%, 19.0% and 9.4%, and adds that keeping 80% of the variance needs 5 of the 30 components while keeping 95% needs 10. Its cross-validation figure then reports that the classifier's accuracy climbs from 91.2% at k = 1 to 97.4% by k = 5, dips at k = 3, and from k = 5 to k = 30 stays inside a band 0.7 percentage points tall, with its best point at k = 10 (98.07%) just above the 97.89% of the 30 raw features. A colleague applies the rule 'keep 95% of the variance' and so picks k = 10. Which assessment of that rule do the printed figures support?

A) It reached a good k for the wrong reason: the plateau from k = 5 shows the accuracy had flattened long before the variance reached its 95% line  
B) It is the right rule because accuracy rises with variance kept, which is why the k that reaches 95% of the variance is also the k that scores highest  
C) It is too generous: the dip at k = 3 shows the third component's 9.4% of variance is harming the classifier, so k should stop at 2  
D) It is too strict: a reduced model can at best match the 30 raw features, so the 5 components that already keep 80% of the variance are the honest ceiling  

---

### Question 8

ReLU is the default activation in the networks Course 01 built. What does the name stand for, and what does the function do?

A) Rectified Linear Unit - it passes a positive input through unchanged and returns zero otherwise  
B) Random Linear Unit - it scales its input by a weight drawn fresh on each forward pass through the layer  
C) Recursive Linear Unit - it feeds its own previous output back in alongside the current input  
D) Regular Linear Unit - it returns the input unchanged, which keeps the layer's response linear  

---

### Question 9

Unit 4 then repeated the gradient measurement along an LSTM's memory lane and printed it beside the plain RNN:

```
distance k     plain RNN    LSTM b_f=1
        25      2.41e-15      1.84e-02
        50      7.33e-30      1.24e-04
```

At k = 50 the LSTM lane keeps about 2e+25 times more signal than the RNN, yet on the log plot its curve still slopes downward. Which conclusion does this table support?

A) Biasing the forget gate towards 1 has pushed the recurrent weights high enough for the gradient to explode instead — the mirror problem, which gradient clipping is there to handle  
B) The lane slows the exponential decay of the backward signal but does not stop it; attention removes the distance, putting two far-apart words one step apart  
C) A surviving signal of 1.24e-04 after 50 steps shows the long-range dependency is now learnable, so the vanishing gradient is a solved problem for LSTMs  
D) The LSTM's separate cell-state vector has room to store a 50-step sequence that the RNN's hidden state could not hold, which makes this a capacity fix  

---

### Question 10

A student reruns the lesson's five-frame storyboard. Both groups are pinned to **PPV = 62%** and **FNR = 28%** in every frame; the white base rate stays at 39% while the Black base rate slides from 39% to 51%. Frame 1 prints a forced false-positive gap of **0.0 points**; frame 5 prints **17.7 points**. The gap ProPublica measured in Broward County was **21.4 points**. What does the storyboard establish?

A) ProPublica's 21.4-point finding is mostly an artefact: a tool pinned to equal PPV treats both groups correctly, so the error-rate critique of COMPAS does not stand  
B) The gap sits in the base-rate column, so lowering the cut-off for white defendants until their FPR also reads 45.9% would let calibration and equal error rates hold together  
C) Both camps measured correctly: holding PPV equal while base rates differ forces an FPR gap by arithmetic, so the dispute is which criterion to hold, not who miscounted  
D) Frame 5 shows a 17.7-point failure of demographic parity, which is the fairness test a court applies, so Northpointe's calibration defence is beside the point  

---
