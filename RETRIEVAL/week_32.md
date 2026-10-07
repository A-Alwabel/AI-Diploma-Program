# Retrieval Quiz — Week 32

**Week 32 of 35 · Course 11 — AIAT 125 (Deploying AI Models)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Your `ml-deploy.yml` has the four jobs from Unit 4 lesson 04 — `test`, `train-and-validate`, `build-and-push`, `deploy` — chained with `needs:`. On today's push the `train-and-validate` log ends with:

```
[FAIL] Accuracy: 0.5333 (threshold: 0.95)
Validation FAILED. In CI/CD, the pipeline would stop here.
```

Yesterday's image is still serving traffic. Which statement describes what the workflow did with this push?

A) `validate_model.py` exited 1, but `build-and-push` still ran because an image build needs just `test` to pass  
B) `validate_model.py` exited 1, so `build-and-push` and `deploy` were skipped and no image was built for this commit  
C) The image was built and pushed, then `smoke_test.py` failed its three known-answer requests and rolled the deployment back  
D) `kubectl rollout status` saw the new pods fail readiness, so Kubernetes kept yesterday's ReplicaSet and marked the job red  

---

### Question 2

Unit 5 lesson 04 put three input-side detectors on the iris classifier. Two of its panels printed:

```
Class distribution PSI: 0.0082
Interpretation: No significant drift
```
```
Windows significant at p<0.05: 0 of 32.
```

Imagine both panels stay exactly like this for a month, and then that month's ground-truth labels arrive showing the classifier wrong on far more rows than it was at training time. A colleague says: "Both monitors are green, so the labels must be mislabelled." Which reading does the lesson's data-drift versus concept-drift distinction support?

A) Green KS windows mean P(X) has not moved, and an input distribution that has not moved keeps the model's accuracy where it was  
B) PSI at 0.0082 sits far below the 0.2 action band, so retraining on the latest inputs is the fix for the accuracy drop  
C) Flat input panels together with falling accuracy point to CPU-starved serving pods returning degraded predictions  
D) P(Y|X) can change while P(X) and the predicted-class mix hold still; neither panel sees that, so the labels may be right  

---

### Question 3

Unit 5 walked a release through the stages 5% → 25% → 100% with an automatic rollback at each gate. How does a **canary deployment** release a new model version?

A) It replaces the old version at once, then watches the dashboards for regressions  
B) It runs both versions side by side and routes each user to whichever one answers first  
C) It sends a small share of live traffic to the new version and widens on good metrics  
D) It ships to the development environment first and promotes after manual sign-off  

---

### Question 4

A teammate reruns Unit 1's side-by-side experiment with a new random seed, and this time **logistic regression edges out Gaussian Naive Bayes** on the held-out split. The team is choosing a model for a spam filter that must also flag mail unlike anything it has seen before, and the teammate says the rerun settles it in favour of logistic regression. Which piece of lesson evidence decides the question?

A) The right-hand panel: far from its boundary, logistic regression still answers confidently — it stored no picture of where data lives — so an accuracy swing does not make it a model that can flag unfamiliar mail.  
B) The accuracy printout: the model that scores higher on the held-out split has learned the data better, so a rerun that puts logistic regression ahead settles the choice in its favour for this filter as well.  
C) The left-hand panel: the Gaussian model's invented points land on top of the real ones, which shows that a generative model will also be the more accurate classifier once the random seed is held fixed across reruns.  
D) The probability field in the right-hand panel: an uncertain p(y|x) carries the same information as a low p(x), so logistic regression already flags unfamiliar mail without modelling the data distribution.  

---

### Question 5

Two loss readouts printed by Unit 1's GAN notebook:

```
2-D toy run   — Final G loss: 0.6610   D loss: 1.3927
MNIST run     — Epoch 1/5 — D_loss=0.8774  G_loss=1.4142
                Epoch 5/5 — D_loss=0.5101  G_loss=2.8917
```

A classmate says the 2-D run is the one in trouble, because its discriminator posts the larger loss. Which reading of the two logs is right?

A) The 2-D run is the one in trouble: a discriminator posting a larger loss than its generator has lost the game and stopped teaching it anything, and the repair is extra D updates per G step until D's loss falls back below G's.  
B) The 2-D run sits at the balance point — a D loss near 1.39 means D cannot tell real from fake — while the MNIST trend is the one to watch: D's loss falls as G's rises, and a D that wins outright starves G of gradient.  
C) Both runs are healthy: the MNIST discriminator's falling loss shows it is learning the digits, and a generator loss that climbs to 2.8917 simply means G is now being graded by a stricter judge, which is how it improves.  
D) The MNIST run has mode-collapsed: a generator loss that climbs while D's falls is the signature of G producing one output over and over, which the discriminator then learns to reject with growing confidence.  

---

### Question 6

The β-VAE experiment's per-epoch table (same data, same architecture, same epoch count; β is the one thing that changed):

```
epoch |  recon b=1   KL b=1 |  recon b=4   KL b=4
    1 |      202.7     10.8 |      219.3      2.7
    3 |      113.6     19.2 |      146.9      6.3
```

A product team wants a **design tool with latent sliders** — a user drags latent coordinates and watches the output change. Which run do they take, and on what grounds?

A) β = 1 — its reconstruction is lower at both epochs, and a slider tool is judged on how faithfully each decoded image matches a real digit, so the run with the sharper decoder is clearly the one to put behind the sliders.  
B) β = 4 — a KL of 6.3 against 19.2 shows that each latent axis now encodes one human-readable factor, so the sliders can be labelled thickness, slant and so on straight from the training run.  
C) β = 4 — its KL sits far below β = 1's from the first epoch, so its latent is pressed closer to N(0, I); that regularity is what sliders need, and whether the axes are disentangled is a separate claim to measure.  
D) Either run — the sliders act on the decoder, and both decoders saw the same images for the same number of epochs, so dragging a coordinate produces much the same change in each model.  

---

### Question 7

In the knowledge-representation lesson, `classify_animal` returned `is a fish` for the whale and the printout marked it `WRONG`. After the repair the same printout read `is a mammal`, and the heading said the function's code was untouched. Which part of the knowledge-based system was changed to get the right answer?

A) The inference loop: `classify_animal` was rewritten so that it tests `breathes air` before it tests `lives in water`  
B) The training data: the whale's row was relabelled `mammal` and the classifier was refitted on the four observed animals  
C) The fact table: an index on the fact `lives in water` was rebuilt so that a lookup for the whale returned mammal instead of fish  
D) The rule store: `breathes air -> is a mammal` was inserted at the front of `animal_kb.rules`, and the old loop reached it first  

---

### Question 8

The statistical-measures lesson evaluates a linear model on held-out diabetes patients and prints MSE 2900.19, then notes in 'Where this breaks' that RMSE exceeds MAE by about 26%. Its diagnostic panel adds that 30 of the 89 patients are missed by more than 53.9 and that the worst single prediction is off by 154. A teammate proposes reporting MAE on its own because it 'looks better'. What does the 26% gap, read together with those two counts, tell you?

A) Errors are unevenly spread: a minority of badly missed patients pulls RMSE up, so MAE alone would understate the worst cases  
B) The model over-predicts by about a quarter on average, since RMSE exceeding MAE by 26% measures the direction of the typical miss  
C) RMSE has to be squared back to MSE 2900.19 before it can be set against MAE, because the 26% gap compares unlike units  
D) The 154 miss is one outlier; remove that patient and RMSE would fall back to MAE, because the whole gap comes from a single record  

---

### Question 9

Unit 1 also printed the pipeline as a step table:

```
stage                                   tokens  distinct types
3. stop-words removed                       21              21
4. punctuation stripped per token           21              19
```

Between steps 3 and 4 the token count holds at 21 while the number of distinct types drops by two. What happened at step 4?

A) Two tokens made of punctuation alone were deleted from the list, because stripping punctuation removes such tokens from a token sequence  
B) Stripping the bracket and the full stop turned `(nlp)` and `language.` into `nlp` and `language`, which were already types  
C) Two more words matched the nine-word stop list once their trailing punctuation no longer hid them from it  
D) Lowercasing merged `Natural` and `NLP` with their lower-case spellings, cutting the type count by two  

---

### Question 10

A bank is placing two systems on the EU market: a **customer-service chatbot** that answers account questions, and a **credit-scoring model** that decides loan eligibility. The lesson's `classify_eu_risk()` returned a tier for each, and the chart under it counts obligations per tier as **0 → 2 → 9** from minimal to high risk. What follows for the two systems?

A) Both fall in limited risk: each system faces customers directly, so an Article 50 notice that an AI is involved discharges the bank's duties for the pair  
B) The credit scorer is prohibited under Article 5, since algorithmic decisions on access to loans sit beside social scoring, while the chatbot is minimal risk with no new obligations  
C) The chatbot carries the 2 limited-risk duties (disclose the AI, label synthetic media); the credit scorer carries the 9 high-risk obligations, conformity assessment included  
D) Both are high risk: a bank counts as critical infrastructure under the Act, so the 9 obligations attach to any AI system it deploys, the account-questions chatbot included  

---
