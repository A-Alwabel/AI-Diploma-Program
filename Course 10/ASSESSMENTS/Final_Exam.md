# Final Exam: Generative AI
## AIAT 124

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. Show your work for partial credit.

**Marking scheme:** Part 1 (Q1–Q6): 5 pts each = 30. Part 2 (Q7–Q9): 10 pts each = 30. Part 3 (Q10: 15 pts, Q11: 10 pts) = 25. Part 4 (Q12): 15 pts. **Total: 100.**

---

## Part 1: Multiple Choice (30 points)

Each question has exactly one best answer. Every option is a position somebody
actually holds — read all four before choosing.

### Question 1 (5 points)
**CLO1:** Unit 1 fits a generative model (Gaussian Naive Bayes) and a discriminative model (logistic regression) to the same two-class dataset. The generative model scores **97.2%** test accuracy; the discriminative model scores **96.1%**. Which conclusion do those two numbers support?

A) The 1.1-point gap shows generative models classify better, so prefer them whenever accuracy matters.  
B) Logistic regression could generate new samples too, if its decision boundary were inverted into a data distribution.  
C) Accuracy is not what separates the two families here — what separates them is that the generative model learns p(x) and can draw new samples from it.  
D) The generative model was bound to win here: p(x|y) turns into a classifier by Bayes' rule, so it carries more information than a bare decision boundary.

---

### Question 2 (5 points)
**CLO2:** You are training the GAN from Unit 1. After a few hundred steps the **discriminator's loss has fallen to nearly 0 and stays there**, while the generator's loss climbs. What is happening, and what does it mean for the generator?

A) The discriminator has saturated — it wins on every batch — so the gradient that reaches G through D vanishes and the generator stops improving.  
B) Training has converged — a discriminator loss near zero is the equilibrium the adversarial game aims for.  
C) The generator has mode-collapsed onto a single output, and a collapsed generator is what drives the discriminator's loss to zero.  
D) The discriminator has overfitted the real images; the standard fix is to lower the generator's learning rate until the two losses cross.

---

### Question 3 (5 points)
**CLO3:** In the β-VAE experiment (identical data, architecture and epochs, only β changed), **β = 1** finished at reconstruction **104.6** and KL **20.5**; **β = 4** finished at reconstruction **137.8** and KL **7.2**. You need a VAE for anomaly detection that flags defects by **reconstruction error**. Which run do you ship, and why?

A) β = 4 — its much lower KL means a latent space closer to N(0, I), and a more regular latent space reconstructs normal inputs more accurately.  
B) β = 4 — a higher β disentangles the latent axes, and disentangled axes make anomalies easier to separate.  
C) Either one — the two runs differ only in a loss weighting, so their decoders produce equivalent reconstructions.  
D) β = 1 — the detector's signal *is* reconstruction error, and β = 4 raised it by about 32%, lifting the error floor a small defect has to clear.

---

### Question 4 (5 points)
**CLO4:** Two image generators are scored with FID inside one fixed, documented pipeline. Model A scores 8.0 and Model B scores 12.0. Which reading of that result is correct?

A) Model A is both better and more diverse than B, since FID's covariance term is exactly what penalises a generator that has lost diversity.  
B) Model A fits this pipeline's feature distribution better — but FID also scores well a model that memorised the training set, or dropped a rare class.  
C) The 4-point gap can be compared directly against FID values published in papers, since FID is a standardised metric on a fixed scale.  
D) Model A's individual images are sharper, since FID computes a per-image sharpness score and averages it over the whole generated set.

---

### Question 5 (5 points)
**CLO5, CLO7:** A product team must generate a million catalogue images a day at interactive latency on a fixed GPU budget. The diffusion model you built needs roughly **200 sequential network passes per image**; a GAN needs **one**. Which trade-off should drive the family choice?

A) Diffusion — its sample quality is higher, and its sampling cost falls as the model is trained longer, so throughput improves with training.  
B) A VAE — its encoder makes generation a single pass, and its reconstruction loss is what guarantees sharp catalogue images.  
C) A GAN generates in one forward pass, so it is the throughput answer; diffusion buys quality at a cost that scales with the step count.  
D) The choice is immaterial at this scale: latency is set by output resolution and batch size, not by which generator family you pick.

---

### Question 6 (5 points)
**CLO6:** A team removes the protected attribute from its training data and reports that the model is now fair. Unit 4 ran exactly that experiment: dropping `Sex` cut the predicted-rate gap from **81.9% to 13.4%**, cost **9.7 points of accuracy**, and `Sex` was still predictable from the remaining features at **66.0%** against a **63.8%** majority-class baseline. What is the correct conclusion?

A) Removing the column removed the team's ability to *audit*, not the model's ability to discriminate — the attribute survives in correlated features.  
B) Fairness through unawareness worked here: a residual gap of 13.4% is small enough that the model can be reported to the client as unbiased.  
C) The gap fell only because accuracy fell: a model that predicts one class for everyone shows no gap at all, and has no value either.  
D) The result transfers: a mitigation of this kind leaves a residual gap of roughly this size, so about 13% is the floor any team should expect.

---

## Part 2: Short Answer Questions (30 points)

### Question 7 (10 points)
**CLO1, CLO2:** Explain how GANs work. Describe the adversarial training process between generator and discriminator.

---

### Question 8 (10 points)
**CLO3:** Explain the VAE architecture and loss function. What is the role of the KL divergence term?

---

### Question 9 (10 points)
**CLO6:** Discuss ethical implications of generative AI. Provide examples and mitigation strategies.

---

## Part 3: Practical/Coding Questions (25 points)

### Question 10 (15 points)
**CLO2, CLO3:** Implement a simple VAE for image generation:
1. Define encoder and decoder networks
2. Implement reparameterization trick
3. Define VAE loss (reconstruction + KL divergence)
4. Show training loop structure

---

### Question 11 (10 points)
**CLO5:** Write a PyTorch function that performs **temperature-controlled text sampling** from a character-level language model. Given a model that outputs logits of shape `(vocab_size,)`, write code to:
1. Apply temperature scaling (`logits / temperature`).
2. Convert to probabilities with softmax.
3. Sample the next token id from those probabilities (`torch.multinomial`, or `np.random.choice(..., p=probs)` as the unit notebooks do — either is accepted).
4. Explain what happens to diversity when temperature → 0 vs temperature → ∞.

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
**CLO5, CLO7:** Design a generative AI system for a fashion design company:
1. Choose appropriate generative model (GAN/VAE/Diffusion)
2. Explain model architecture
3. Training strategy
4. Evaluation methods
5. Address ethical considerations (bias, authenticity)
6. Future trends and improvements

---

**End of Exam**

**Good Luck!**
