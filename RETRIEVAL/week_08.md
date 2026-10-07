# Retrieval Quiz — Week 08

**Week 08 of 35 · Course 03 — AIAT 113 (Mathematics and Probability for Machine Learning)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The PCA lesson's first cell prints the explained-variance ratios of the top three components of the standardized 569-biopsy data as 44.3%, 19.0% and 9.4%, and adds that keeping 80% of the variance needs 5 of the 30 components while keeping 95% needs 10. Its cross-validation figure then reports that the classifier's accuracy climbs from 91.2% at k = 1 to 97.4% by k = 5, dips at k = 3, and from k = 5 to k = 30 stays inside a band 0.7 percentage points tall, with its best point at k = 10 (98.07%) just above the 97.89% of the 30 raw features. A colleague applies the rule 'keep 95% of the variance' and so picks k = 10. Which assessment of that rule do the printed figures support?

A) It reached a good k for the wrong reason: the plateau from k = 5 shows the accuracy had flattened long before the variance reached its 95% line  
B) It is the right rule because accuracy rises with variance kept, which is why the k that reaches 95% of the variance is also the k that scores highest  
C) It is too generous: the dip at k = 3 shows the third component's 9.4% of variance is harming the classifier, so k should stop at 2  
D) It is too strict: a reduced model can at best match the 30 raw features, so the 5 components that already keep 80% of the variance are the honest ceiling  

---

### Question 2

In the Unit 2 expert-system cell, three recorded observations about `Patient1` and two rules went in, and the run printed:

```
   BEFORE Forward Chaining:
      Facts: 3

  ➕ Added: Fact(Patient1, likely_has, Flu)
   ✅ Applied rule: Flu Diagnosis Rule
  ➕ Added: Fact(Patient1, recommend, Rest)
   ✅ Applied rule: Flu Treatment Rule

✅ Forward chaining complete! (2 iterations)
   (Stopped because no more new facts can be derived)

   AFTER Forward Chaining:
      Facts: 5
```

A clinic now wants the system to run with no particular question in mind: *each time a nurse records a new observation, surface whatever recommendations now follow for that patient.* Which chaining direction suits that job, and what in the printout shows why?

A) Forward chaining: the Flu Diagnosis Rule was entered before the Flu Treatment Rule, and firing rules in the order they were written is what keeps the chain valid  
B) Backward chaining: it would prove `recommend Rest` for one patient at a time, and a focused proof costs less than deriving facts even when no goal has been named  
C) Backward chaining: if a later observation contradicts `likely_has Flu`, it can take back the `Rest` recommendation, which a forward chainer has no way to do  
D) Forward chaining: data-driven, firing whichever rules the recorded facts satisfy until a pass adds no new fact — the loop that stopped above after 2 iterations  

---

### Question 3

The weather recommender in Course 01's first lesson printed two neighbouring cases:

```
26 °C, 59% humidity, morning -> Go for a jog in the park
26 °C, 61% humidity, morning -> Moderate weather, any outdoor activity is fine
```

A classmate concludes that the recommender "learned a humidity boundary near 60% from past weather data". Which statement describes where that boundary actually came from, and what it tells you about the system's family?

A) A person typed `humidity < 60` into an `if` statement, so the system is rule-based: the threshold was authored, not fitted to data  
B) The 60% cut was fitted from the four printed test cases, which makes the recommender a small data-driven model of the kind Unit 2 trains  
C) The jump between 59% and 61% shows the system hides its reasoning, which is the mark of a modern learned model  
D) The two answers differ because the hand-written rule evaluates faster than a fitted model would; speed is what separates the two families  

---

### Question 4

Course 03 Unit 3 runs the same model with SGD and with Adam and compares their curves. What is the structural difference between the two optimizers?

A) Adam computes the exact gradient over the full dataset at each step; SGD estimates it from a mini-batch  
B) Adam minimises a different loss function, which is why its curve can lie below SGD's  
C) Adam keeps a separate, adapted step size for each parameter; plain SGD applies one rate to them all  
D) Adam updates the parameters once per epoch; SGD updates them once per training example  

---

### Question 5

A discriminative classifier and a generative model are trained on the same labelled dataset. Which probability does the generative model learn?

A) P(Y | X) — the probability of the label given the features, which is what a fitted decision boundary encodes  
B) P(X) alone — how the features are distributed, with the labels discarded  
C) P(Y) alone — how often each label occurs in the training set  
D) P(X | Y) with P(Y) — how the features are distributed inside each class, and how common each class is  

---

### Question 6

The Unit 3 diagnosis system was loaded with these printed symptom probabilities, among others:

```
  ➕ P(Fever|Flu) = 90.00%
  ➕ P(Cough|Flu) = 80.00%
  ➕ P(Fatigue|Flu) = 70.00%
  ➕ P(Fever|COVID-19) = 85.00%
  ➕ P(Cough|COVID-19) = 90.00%
  ➕ P(Fatigue|COVID-19) = 60.00%
```

For the patient with fever, cough and fatigue it printed `Flu: 58.91%` and `COVID-19: 21.46%`. Its slope-chart table shows the two likelihoods nearly tied — `P(symptoms|d)` of 50.4% for Flu against 45.9% for COVID-19 — with normalised priors of 22.7% and 9.1%. COVID-19 explains this patient almost as well as Flu does. Why does it end up with far less than half of Flu's posterior?

A) COVID-19's 2.0% prevalence is renormalised up to 9.1% over three diseases, and that renormalisation step is what costs it the ranking against Flu  
B) The likelihood gap does it: COVID-19's fatigue figure of 60.00% is the weakest entry, and 45.9% against 50.4% is what pulls its posterior down to 21.46%  
C) With the likelihoods this close, the prior decides: Flu's normalised prior of 22.7% is more than twice COVID-19's 9.1%, and Bayes multiplies the two  
D) Normalising the three posteriors to sum to 100% hands the leader a share of the others' mass, which is what widens a near-tie into 58.91% against 21.46%  

---

### Question 7

What does depth-first search gain over breadth-first search on the same graph?

A) It reaches the goal in fewer edges when several paths exist  
B) It holds just the current path and its siblings, not a whole frontier level  
C) It visits each node once, where breadth-first search may expand the same node twice  
D) Its asymptotic running time is lower, O(V) against breadth-first search's O(V + E)  

---

### Question 8

The gradient-descent lesson prints, next to each learning rate, the factor |1 − 2·lr| that multiplies x at each step when minimising f(x) = x² from x = 5 for 30 steps: 0.98 for lr = 0.01, 0.80 for lr = 0.1, 0.80 for lr = 0.9, 1.00 for lr = 1.0 and 1.20 for lr = 1.1. The losses after 30 steps are 7.43883, 3.83124e-05, 3.83124e-05, 25 and 1.40869e+06 respectively. A colleague watching a training run sees a loss curve that is a straight line down on a log axis and concludes the step size is well chosen. Using the printed factors, which objection is justified?

A) A factor of 0.80 belongs to both lr = 0.1 and lr = 0.9, so the same straight line can come from a run that crosses zero at each step  
B) A factor of 0.80 means both runs move x by the same distance each step, so lr = 0.9 is a relabelled lr = 0.1 and no objection applies  
C) A straight line down shows the factor is below 1, so the rate can safely be raised toward the 1.00 row for a faster descent  
D) The 3.83124e-05 reached at lr = 0.9 beats the 7.43883 at lr = 0.01 because the larger rate found a second, deeper minimum of f  

---

### Question 9

Which of these models can produce a new data point that was not in its training set?

A) Logistic regression, which fits a boundary and returns a class probability  
B) A generative adversarial network, whose generator is trained to produce samples  
C) A support vector machine, which places a boundary at the widest margin it can find  
D) A decision tree, which splits the feature space and labels each region  

---

### Question 10

An expert system is given three recorded facts about a patient and two rules. Run forward, what does the engine do?

A) It begins from a candidate conclusion and looks for facts that would support it  
B) It fires the rules in the order they were written, once each, and then stops  
C) It begins from the facts and fires the rules they satisfy, adding results as new facts  
D) It searches the rule set for the rule with the highest stated confidence and fires that one alone  

---
