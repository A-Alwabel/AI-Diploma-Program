# Diploma Glossary — one meaning per word, across all twelve courses

**Last updated:** 2026-08

This diploma is taught in order, 01 → 12, by one instructor. A word introduced in
Course 01 has to still mean the same thing in Course 11, and where it honestly
*cannot*, you deserve to be told why rather than left to notice the clash yourself.

This file is the authority. **If a notebook and this file disagree, this file is
right and the notebook is a bug** — report it.

Three things you will find in each entry:

- **The definition the whole diploma uses.**
- **Where it is taught** — by course number and AIAT code, so you can go back.
- **Other technical senses**, where the same word genuinely means something else
  in a different subfield. These are *homonyms*, not contradictions. AI grew out
  of statistics, logic, control theory, linguistics and law at the same time, and
  those fields reused each other's words without coordinating. We keep each field's
  own convention rather than inventing private ones, and we tell you when the
  meaning switches.
- **What settles it** — the paper, textbook or official documentation the
  definition comes from. Nothing here rests on anyone's memory.

**Quick index:** [Accuracy](#accuracy) · [Agent](#agent) · [Bias](#bias) ·
[Confidence interval](#confidence-interval) · [Cross-validation](#cross-validation) ·
[Drift](#drift) · [Epoch / iteration / batch](#epoch-iteration-batch) ·
[Inference](#inference) · [Loss](#loss-function) · [Normalization vs standardization](#normalization-vs-standardization) ·
[Overfitting](#overfitting-and-underfitting) · [Parameter vs hyperparameter](#parameter-vs-hyperparameter) ·
[Policy](#policy) · [Precision, recall, F1](#precision-recall-and-f1) ·
[p-value](#p-value) · [Regularization strength](#regularization-strength) ·
[Significance level](#significance-level-α) · [Temperature](#temperature) · [Token](#token) ·
[Train / validation / test](#training-set-validation-set-test-set) ·
[Symbols](#symbols-that-mean-more-than-one-thing)

---

## Accuracy

**The diploma's definition.** The fraction of predictions that were correct:
`(TP + TN) / (TP + TN + FP + FN)`.

**Where it is taught.** Course 01 (AIAT 111) Unit 5 · Course 04 (AIAT 114) Unit 3 ·
Course 05 (AIAT 115) Unit 4 · used for group-by-group fairness auditing in
Course 06 (AIAT 116) Unit 2 and Course 08 (AIAT 122) Unit 4.

**Health warning the diploma repeats deliberately.** On imbalanced data accuracy is
close to meaningless — a model that predicts "not fraud" every time scores 99.8% on
the credit-card data in Course 04. That is not a contradiction between lessons; it is
the same lesson taught again because it is the mistake students actually make.

**What settles it.** scikit-learn, `sklearn.metrics.accuracy_score` documentation.

---

## Agent

**The diploma's definition.** An **agent** is anything that can be viewed as perceiving
its environment through **sensors** and acting upon that environment through
**actuators**. A **rational** agent selects the action expected to maximise its
performance measure, given what it has perceived and what it knows.

**Where it is taught.** Course 01 (AIAT 111) Unit 1, lesson 04 "Intelligent Agents and
Rationality" — this is the definition, and every later course inherits it.

**The later uses are specialisations, not redefinitions.** This matters, because it is
the single most common place a student thinks two courses disagree:

| Course | What the agent is | What is added |
|---|---|---|
| Course 01 (AIAT 111) Unit 1 | perceive → think → act loop | the abstraction itself |
| Course 09 (AIAT 123), all units | an RL agent in an MDP | the *think* step is **learned**, by maximising expected cumulative reward |
| Course 10 (AIAT 124) Unit 5, Course 01 Unit 1 "State of the field" | a 2026 tool-using LLM agent | the *think* step is a language model; actions are tool calls |

One abstraction, three implementations. Nothing was redefined between Course 01 and
Course 09 — reinforcement learning simply fixes *how* the agent chooses.

**A genuinely unrelated sense.** In **Course 06 (AIAT 116) Unit 5, lesson 04**, "agent"
is the **legal** term: one party acting on another's behalf, so that the principal
answers for what the agent does (this is the holding in *Mobley v. Workday*). That has
nothing to do with sensors and actuators. Same spelling, different discipline.

**What settles it.** Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern
Approach*, 4th ed., Ch. 2 · Sutton, R. & Barto, A. (2018). *Reinforcement Learning: An
Introduction*, 2nd ed., Ch. 3.

---

## Bias

This word does the most damage of any word in the diploma, because it has **five**
established technical meanings and two of them sound moral. They are homonyms. Read the
sentence, never the word alone.

| Sense | What it means | Where you meet it |
|---|---|---|
| **1. Bias term** | the constant `b` in `w·x + b`; one more learnable number | Course 01 (AIAT 111) Unit 4 · Course 03 (AIAT 113) projects |
| **2. Bias–variance bias** | error caused by a model too simple to represent the pattern (underfitting) | Course 03 (AIAT 113) Unit 3 · Course 04 (AIAT 114) Unit 2, lesson 02 |
| **3. Estimator bias** | the expected difference between an estimate and the true value | Course 03 (AIAT 113) Unit 5, lesson 05 |
| **4. Inductive bias** | the assumptions an architecture builds in (locality in a CNN, recurrence in an RNN) | Course 01 (AIAT 111) Unit 4, lesson 02 · Course 08 (AIAT 122) Unit 2 |
| **5. Fairness bias** | systematically worse outcomes for a group of people | Course 06 (AIAT 116) Units 1–2 · Course 08 (AIAT 122) Unit 4 · Course 10 (AIAT 124) Unit 4 |

**Senses 1–4 carry no moral content at all.** A "high-bias model" is an underfitting
model, not an unfair one. You can drive bias–variance bias to zero and still ship a
system that discriminates, and you can have a large bias term in a perfectly fair model.

**House rule.** Where context does not settle it, this diploma writes **"model bias"**
for senses 1–4 and **"fairness bias"** for sense 5.

**What settles it.** NIST (2022). *Towards a Standard for Identifying and Managing Bias
in Artificial Intelligence*, SP 1270, §2.1.1 — which separates the **statistical
context** ("bias is an effect that deprives a statistical result of representativeness
by systematically distorting it"), the **legal context**, and the **cognitive and
societal context**, and warns that the statistical view alone "does not sufficiently
encompass or communicate the full spectrum of risks posed by bias in AI systems."
Senses 1–2 additionally: Hastie, Tibshirani & Friedman, *The Elements of Statistical
Learning*, Ch. 7.

---

## Confidence interval

**The diploma's definition.** A range of plausible values for a population parameter,
built by a procedure with a stated success rate. "95%" is a property of the
**procedure**: repeat the experiment many times and 95% of the intervals built this way
would contain the true value.

**It is not** "a 95% chance the true value is in *this* interval". The true value is a
fixed number; it is either inside your one interval or it is not. Both "there is a 95%
probability the true mean lies between these numbers" and "we can be 95% confident the
true mean is in this interval" are false statements about a frequentist interval.

**Where it is taught.** Course 03 (AIAT 113) Unit 5, lesson 08 — including the Hoekstra
et al. study in which 120 researchers and 442 students were given six statements about a
95% interval, all six false, and both groups endorsed more than three on average.

**Used later in.** Course 04 (AIAT 114) Unit 2 (reporting CV spread) · Course 09
(AIAT 123) Unit 4 (UCB's bonus term *is* a confidence bound) · Course 11 (AIAT 125)
Unit 5 (A/B tests).

**What settles it.** Hoekstra, R., Morey, R. D., Rouder, J. N., & Wagenmakers, E.-J.
(2014). *Robust misinterpretation of confidence intervals*. Psychonomic Bulletin &
Review, 21(5), 1157–1164.

---

## Cross-validation

**The diploma's definition.** Repeatedly splitting the training data into fit/score
folds so that the performance estimate does not depend on one arbitrary split. K-fold
cross-validation gives you a **spread**, not a certificate.

**Where it is taught.** Course 04 (AIAT 114) Unit 2, lesson 01 · Course 05 (AIAT 115)
Unit 4, lesson 07.

**The rule the whole diploma follows.** Cross-validation is a *validation* technique.
Selecting a model on CV scores is itself a form of overfitting, one level up — so the
final number still comes from a test set that no selection step ever touched. See
[Training set, validation set, test set](#training-set-validation-set-test-set).

**What settles it.** scikit-learn, *Cross-validation: evaluating estimator performance*.

---

## Drift

**The diploma's definition.**

- **Data drift** (covariate shift): the input distribution `P(X)` changes while the
  relationship `P(Y|X)` stays the same.
- **Concept drift**: `P(Y|X)` itself changes — the same inputs now imply a different
  answer.

**Where it is taught.** Course 11 (AIAT 125) Unit 5, lesson 04 · triggers for retraining
in lesson 02.

**The honest limit the diploma states.** Distribution tests (KS, PSI, JS) see `P(X)`
only. **Concept drift cannot be detected without labels.**

**What settles it.** Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., & Bouchachia,
A. (2014). *A survey on concept drift adaptation*. ACM Computing Surveys, 46(4).

---

## Epoch, iteration, batch

These three are **not** synonyms, and the diploma keeps them apart in every course.

| Term | Definition |
|---|---|
| **Batch** (mini-batch) | the group of samples used for **one** weight update |
| **Iteration** (also **step**) | **one** weight update, on one batch |
| **Epoch** | **one full pass over the entire training set** |

So one epoch contains `n_samples / batch_size` iterations. "Trained for 100 epochs" and
"trained for 100 iterations" describe wildly different amounts of training.

**Where it is taught.** Course 01 (AIAT 111) Unit 3, lesson 02 (first definition) and
Unit 4, lesson 01 · Course 08 (AIAT 122) Unit 1, lesson 02 · used throughout Courses 08
and 10.

**What settles it.** Keras `Model.fit` documentation: "**epochs**: … An epoch is an
iteration over the entire `x` and `y` data provided", and "**steps_per_epoch**: Total
number of steps (batches of samples) before declaring one epoch finished."

---

## Inference

Three established meanings, one spelling. The field never tidied this up, so the
diploma names the sense whenever context does not.

| Sense | What it means | Where |
|---|---|---|
| **Logical inference** | deriving new facts from rules and existing facts | Course 02 (AIAT 112) Unit 2 |
| **Statistical inference** | drawing conclusions about a population from a sample | Course 03 (AIAT 113) Unit 5 |
| **Bayesian inference** | updating a prior into a posterior given evidence | Course 02 (AIAT 112) Unit 3 · Course 03 (AIAT 113) Unit 5, lesson 03 |
| **Inference (serving)** | running a trained model forward on new input to get a prediction — what happens inside `/predict`, measured in milliseconds | Course 05 (AIAT 115) · Course 08 (AIAT 122) Unit 5 · Course 11 (AIAT 125), all units |

"Inference latency" in Course 11 has nothing to do with "statistical inference" in
Course 03. They are unrelated words that happen to be spelled the same.

**What settles it.** Russell & Norvig, *AIMA* 4e, Ch. 7–8 (logical inference) · James,
Witten, Hastie & Tibshirani, *An Introduction to Statistical Learning*, 2nd ed., Ch. 3
and 5 (statistical inference) · Wasserstein & Lazar (2016), ASA Statement (the p-value
machinery of statistical inference) · PyTorch `torch.no_grad` / TorchServe documentation,
which uses "inference" exclusively in the forward-pass sense.

---

## Loss function

**The diploma's definition.** The single number a training procedure tries to make
small. The diploma uses **"loss function"** as the standard name.

**"Cost function" and "objective function" mean the same thing here.** You will see all
three in the wild and occasionally in older notebooks in this repository (the
Course 03 gradient-descent project says "cost function"). Some courses elsewhere reserve
"loss" for one example and "cost" for the average over the set; **this diploma does not
make that distinction**, and when the difference matters we say "per-sample loss" or
"mean loss" explicitly.

**Where it is taught.** Course 01 (AIAT 111) Unit 3, lesson 04 · Course 03 (AIAT 113)
Units 2–3 · Course 08 (AIAT 122) Unit 1.

**What settles it.** Goodfellow, Bengio & Courville (2016). *Deep Learning*, §4.3: the
function to be minimised or maximised is the objective function or criterion, and when
minimising it may equally be called the cost function, loss function, or error function.

---

## Normalization vs standardization

**The diploma's definition.**

- **Normalization** (min–max scaling): rescale to a fixed range, usually `[0, 1]`.
  scikit-learn's `MinMaxScaler`.
- **Standardization** (z-score): subtract the mean, divide by the standard deviation, so
  the feature has mean 0 and standard deviation 1. scikit-learn's `StandardScaler`.

**Where it is taught.** Course 04 (AIAT 114) Unit 1, lesson 03 · Course 05 (AIAT 115)
Unit 2, lesson 03.

**Other uses of the word "normalization" that are unrelated to feature scaling.**
**Batch normalization** and **layer normalization** (Course 08, AIAT 122) are *layers
inside a network* that renormalise activations during training — not a preprocessing
step you apply to a dataframe. **Text normalization** (Course 07, AIAT 121, Unit 1) means
lowercasing, stripping punctuation and unifying orthography before tokenizing. Same word, three jobs.

**The rule that never changes.** Fit any scaler on the training split only, then apply
it to validation and test. Fitting on the whole dataset is leakage, and Course 05
Unit 4 lesson 02 shows what it costs.

**What settles it.** scikit-learn, *Preprocessing data* — `MinMaxScaler` and
`StandardScaler`.

---

## Overfitting and underfitting

**The diploma's definition.** **Overfitting**: the model performs well on the training
data and materially worse on held-out data — it has fitted noise as if it were pattern.
**Underfitting**: the model is too simple to capture the pattern, and performs poorly on
both.

**Where it is taught.** Course 03 (AIAT 113) Unit 3 · Course 04 (AIAT 114) Unit 1
lesson 05 and Unit 2 lesson 02 · Course 05 (AIAT 115) Unit 4.

**Connected term.** Underfitting is the high-**bias** end of the bias–variance
trade-off, overfitting the high-**variance** end — sense **2** in the
[Bias](#bias) table, not sense 5.

**What settles it.** Hastie, Tibshirani & Friedman, *The Elements of Statistical
Learning*, 2nd ed., Ch. 7.

---

## Parameter vs hyperparameter

**The diploma's definition.** **Parameters are learned** from the training data by the
fitting procedure (weights, the bias term, split points in a tree). **Hyperparameters
are set before training** and are not learned from the training data (learning rate,
`alpha` in Ridge, `max_depth`, `n_estimators`, `k` in k-NN).

**Where it is taught.** Course 04 (AIAT 114) Unit 5, lesson 01 · Course 05 (AIAT 115)
Unit 4, lesson 08 · Course 12 (AIAT 126) Unit 3, lesson 02.

**Consequence used throughout the diploma.** Because hyperparameters are *chosen*, they
must be chosen on validation data. See
[Training set, validation set, test set](#training-set-validation-set-test-set).

**What settles it.** scikit-learn, *Tuning the hyper-parameters of an estimator*.

---

## Policy

**The diploma's definition (technical).** A **policy** π is a rule mapping each state to
an action, or to a probability distribution over actions. A *deterministic* policy gives
one action per state; a *stochastic* policy gives probabilities.

**Where it is taught.** Course 02 (AIAT 112) Unit 3, lesson 04 (MDPs and value
iteration — the first appearance) · Course 09 (AIAT 123), all units · the RL-specific
glossary at `Course 09/DOCS/GLOSSARY.md` expands the surrounding vocabulary.

**A genuinely unrelated sense.** "Policy" in ordinary and governance English — an
organisation's rules, a regulation, a company's data-retention policy — appears in
Course 06 (AIAT 116) Unit 5 and, as Kubernetes "restart policy" / "auto-scaling policy",
in Course 11 (AIAT 125) Unit 4. None of these is a mapping from states to actions. Same
spelling, unrelated concepts.

**What settles it.** Sutton & Barto (2018), *Reinforcement Learning: An Introduction*,
2nd ed., §3.5.

---

## Precision, recall, and F1

**The diploma's definition.** For a chosen positive class:

- **Precision** = `TP / (TP + FP)` — *of what I predicted positive, how much was
  actually positive?* It is the ability of the classifier not to label as positive a
  sample that is negative.
- **Recall** = `TP / (TP + FN)` — *of all the actual positives, how many did I catch?*
  It is the ability of the classifier to find all the positive samples. Also called
  **sensitivity**, and in a fairness audit the **true positive rate (TPR)**.
- **F1** = the harmonic mean of precision and recall. F1 weights the two equally, which
  is a claim that a false alarm and a miss cost the same. They almost never do — say so
  out loud with `fbeta_score` when they do not.

**Where it is taught.** Course 01 (AIAT 111) Unit 5, lesson 03 · Course 04 (AIAT 114)
Unit 3, lesson 01 (the full treatment) · Course 05 (AIAT 115) Unit 4, lesson 07 ·
per-group in Course 06 (AIAT 116) Unit 2 and Course 08 (AIAT 122) Unit 4 · production
monitoring in Course 11 (AIAT 125) Unit 5 · Course 12 (AIAT 126) Unit 3.

**This one is not overloaded.** Every course in the diploma uses these two formulas and
these two sentences. If a lesson ever seems to swap them, that lesson is wrong.

**What settles it.** scikit-learn, *Metrics and scoring*: "Intuitively, precision is the
ability of the classifier not to label as positive a sample that is negative, and recall
is the ability of the classifier to find all the positive samples", with
`precision = tp / (tp + fp)` and `recall = tp / (tp + fn)`.

---

## p-value

**The diploma's definition.** A **p-value** is the probability, computed in a world where
the null hypothesis is true, of getting a test statistic **at least as extreme as the one
actually observed**.

**Read carefully what it is not.** A p-value is **not**:

- the probability that the null hypothesis is true;
- the probability that the result arose by chance alone;
- a measure of how large or how important the effect is;
- on its own, good evidence about a model or a hypothesis.

**And `p < 0.05` is a threshold you chose, not a verdict the test handed you.**
Crossing it means "the observed result would be unlikely if nothing were going on", which
is a reason to *investigate*, not proof that something changed.

**Where it is taught.** Course 03 (AIAT 113) Unit 5, lesson 07 (hypothesis testing) and
lesson 08 (p-values and confidence intervals) — this is the definition of record.

**Used later in.** Course 05 (AIAT 115) Unit 3 (correlation) · Course 08 (AIAT 122) Unit 3
(comparing forecasters) · Course 09 (AIAT 123) Unit 4 (bandits vs fixed-horizon A/B
tests) · **Course 11 (AIAT 125) Unit 5**, where the Kolmogorov–Smirnov drift detector and
the A/B canary test both use it. Course 11 uses exactly this definition: a small KS
p-value means a gap this large would be unlikely if nothing had changed, which is why the
feature is **flagged**, not why it is **known** to have drifted.

**The operational warning Course 11 adds.** With enough production traffic, a KS test
reports `p < 0.05` on almost any feature every day, because it detects *any* difference,
not a difference that matters. Threshold on **effect size** (the KS statistic, the PSI
value) instead.

**What settles it.** Wasserstein, R. L., & Lazar, N. A. (2016). *The ASA Statement on
p-Values: Context, Process, and Purpose*. The American Statistician, 70(2), 129–133 —
whose Principle 2 reads: "P-values do not measure the probability that the studied
hypothesis is true, or the probability that the data were produced by random chance
alone", and Principle 5: "A p-value, or statistical significance, does not measure the
size of an effect or the importance of a result."

---

## Regularization strength

**The diploma's definition.** The dial `α` that controls how hard a penalty on large
coefficients pulls against the fit: `Cost = MSE + α × penalty`. `α = 0` is no
regularization; large `α` shrinks coefficients towards zero (and in Lasso, to exactly
zero). It is a **hyperparameter**, tuned on validation data — never on the test set.

**Where it is taught.** Course 03 (AIAT 113) Unit 1, lesson 08 and Unit 3, lesson 04 ·
Course 04 (AIAT 114) Unit 1, lesson 06 (Ridge and Lasso).

**On the symbol.** We write `α` because that is what scikit-learn calls the argument
(`Ridge(alpha=…)`). Much of the statistics literature writes the same quantity as `λ`.
Same quantity, two letters, no disagreement. Do **not** confuse it with the `α` of
[significance level](#significance-level-α) or the `α` of RL step size.

**What settles it.** scikit-learn, `sklearn.linear_model.Ridge` / `Lasso` documentation ·
Hastie, Tibshirani & Friedman, *ESL*, Ch. 3.

---

## Significance level (α)

**The diploma's definition.** The false-positive rate you commit to *before* looking at
the data — the p-value threshold at which you will reject the null hypothesis.
Conventionally 0.05, but it is a choice with consequences, not a law.

**Where it is taught.** Course 03 (AIAT 113) Unit 5, lesson 07.

**Used later in.** Course 11 (AIAT 125) Unit 5, as the 0.05 drift-flag threshold and the
A/B-test significance level.

**Symbol collision.** See [Symbols](#symbols-that-mean-more-than-one-thing) — `α` also
means regularization strength, a Beta-distribution shape parameter, and (in Course 09)
the RL step size.

**What settles it.** Wasserstein & Lazar (2016), ASA Statement, Principle 3: "Scientific
conclusions and business or policy decisions should not be based only on whether a
p-value passes a specific threshold."

---

## Temperature

**The diploma's definition.** A single positive number `T` that you divide a score by
before exponentiating and normalising. **Low `T` sharpens** a distribution towards its
peak; **high `T` flattens** it towards uniform; `T = 1` leaves it unchanged. That is the
whole idea, and it is the same idea every time you meet it.

**Where you meet it — four appearances, one mechanism.**

| Appearance | What is divided by `T` | Course |
|---|---|---|
| **Simulated annealing** | an energy difference, in the acceptance probability | Course 02 (AIAT 112) Unit 4 |
| **Temperature scaling** (calibration) | the logits of a trained classifier, to make its confidence honest | Course 03 (AIAT 113) Unit 5, lesson 09 |
| **Distillation temperature** | the teacher's logits, to expose the "soft labels" the student learns from | Course 08 (AIAT 122) Unit 5, lesson 05 |
| **Sampling temperature** | the next-token logits, to trade safe text against surprising text | Course 08 (AIAT 122) Unit 3 · Course 10 (AIAT 124) Unit 2 |

These are **not** four unrelated meanings — that is why the word is the same. If you can
explain the softmax with a temperature in it, you can explain all four.

**One thing temperature is not.** It is not a creativity dial. Above the corpus's own
entropy, higher `T` produces non-words, not better writing — Course 10 Unit 2, lesson 05
demonstrates this on real text.

**What settles it.** Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). *On
Calibration of Modern Neural Networks*, ICML — the source Course 03 Unit 5 lesson 09 uses
for temperature scaling · Hinton, G., Vinyals, O., & Dean, J. (2015). *Distilling the
Knowledge in a Neural Network*, arXiv:1503.02531 — the source for distillation with soft
targets · Goodfellow, Bengio & Courville (2016), *Deep Learning*, Ch. 17 (Monte Carlo
methods, where the same tempering idea appears for sampling).

---

## Token

**The diploma's definition.** The unit a language model actually reads and emits. A token
is **not** a character and **not** always a whole word — modern models use sub-word
tokens, so one long word may be several tokens and a common word exactly one. The
tokenizer defines the vocabulary; change it and the token boundaries change with it.

**Where it is taught.** Course 07 (AIAT 121) Units 1–2 (tokenization, sub-word units) ·
used throughout Course 08 (AIAT 122) Unit 3 and Course 10 (AIAT 124) Unit 2.

**Consequence the diploma repeats.** Perplexity is a *per-token* number, so changing the
tokenizer changes the denominator and changes the score. Perplexities are not comparable
across models with different tokenizers (Course 10, Unit 2, lesson 06).

**A genuinely unrelated sense.** In Course 11 (AIAT 125) Unit 3, lesson 05 a **token** is
a **security credential** — a JWT carried in a request header. It has nothing to do with
text units. Same spelling, different field.

**What settles it.** Jurafsky, D., & Martin, J. H. *Speech and Language Processing*, 3rd
ed., Ch. 2 (tokenization and sub-word units).

---

## Training set, validation set, test set

**The diploma's definition — three roles, and they never swap.**

| Split | What it is for | How often you may look |
|---|---|---|
| **Training set** | fitting the model's **parameters** | constantly |
| **Validation set** (or the CV folds) | **choosing** — hyperparameters, thresholds, which model wins | as often as you like |
| **Test set** | reporting an honest number | **once**, at the very end |

**The single rule that follows from it:** *if a step **chooses** something, it belongs on
validation data.* The first time the test set influences a decision, it stops being a
test set and becomes another validation set — and the number it produces becomes
optimistic.

**Where it is taught.** Course 04 (AIAT 114) Unit 1, lesson 03 (the split) · Unit 3,
lesson 01 (the three-way diagram) · Unit 5, lesson 01 (grid search) · Course 05
(AIAT 115) Unit 4, lessons 02, 07 and 08 · applied as a promotion gate in Course 11
(AIAT 125) Units 2 and 5.

**Common confusion, resolved.** Keras's `validation_split=0.1` (Course 08) carves the
validation set out of the training data automatically — it is the same role, done for
you. It is not a test set, and a `val_accuracy` number is not a test number.

**What settles it.** scikit-learn, *Cross-validation: evaluating estimator performance*:
"there is still a risk of overfitting *on the test set* because the parameters can be
tweaked until the estimator performs optimally … To solve this problem, yet another part
of the dataset can be held out as a so-called validation set: training proceeds on the
training set, after which evaluation is done on the validation set, and when the
experiment seems to be successful, final evaluation can be done on the test set."

---

## Symbols that mean more than one thing

Mathematics in AI is not standardised, and different subfields settled on different
letters long before anyone taught them in one diploma. We use each field's own
convention rather than inventing private notation — which means you must read a symbol
from its sentence, never from the symbol alone.

| Symbol | Meaning | Where |
|---|---|---|
| **α** | regularization strength (Ridge / Lasso `alpha`) | Course 03 (AIAT 113) Units 1, 3 · Course 04 (AIAT 114) Unit 1 |
| **α** | significance level of a hypothesis test | Course 03 (AIAT 113) Unit 5 |
| **α** | shape parameter of a Beta distribution | Course 03 (AIAT 113) Unit 5, lesson 03 |
| **α** | learning rate / step size | Course 09 (AIAT 123), following Sutton & Barto |
| **η** | learning rate / step size — *the same quantity as RL's α* | Course 08 (AIAT 122) Unit 1, lessons 05–06, following the deep-learning convention |
| `learning_rate`, `lr` | learning rate / step size, spelled out | Course 03 (AIAT 113) Units 2–3 · all scikit-learn and Keras code |
| **λ** | regularization strength in most statistics texts — *the same quantity as sklearn's `alpha`* | referenced, not used, in this diploma |
| **π** | a policy (states → actions) | Course 02 (AIAT 112) Unit 3 · Course 09 (AIAT 123) |
| **γ** | discount factor for future reward | Course 02 (AIAT 112) Unit 3 · Course 09 (AIAT 123) |
| **θ** | the vector of model parameters | Course 03 (AIAT 113) Units 1–3 |

Where two letters name **one** quantity (α and η for the learning rate; α and λ for
regularization strength), there is no disagreement about the mathematics — only about
which literature you happened to read first.

---

## How to use this file when something looks wrong

1. **Find the term here.** This file's definition is the diploma's definition.
2. **Check whether the clash is one of the listed homonyms.** If the two uses appear in
   the "other senses" section of an entry, the courses do not disagree — the English
   language does.
3. **If a notebook genuinely contradicts this file, it is the notebook that is wrong.**
   Note the course, unit, lesson and cell, and raise it. Terminology bugs are treated
   the same as code bugs here.

**Related reading:** [STUDENT_GUIDE.md](STUDENT_GUIDE.md) ·
[COURSE_NAVIGATION.md](COURSE_NAVIGATION.md) ·
`Course 09/DOCS/GLOSSARY.md` (reinforcement-learning vocabulary in depth) ·
`Course 08/DOCS/COMMON_MISCONCEPTIONS_AND_FAQ.md` (deep-learning misconceptions).
