# Cumulative Retrieval Quiz - Week 08

**Course 03 - AIAT 113, Units 2, 3 and 4**

- **15 minutes, in class, at the very end of the session.** It replaces the session's
  self-check block: about 7 minutes to answer, about 8 minutes for your instructor to work
  the correct answers aloud.
- **This quiz is not graded.** It carries no marks and does not appear in your course grade.
  Nothing you write here is collected.
- **The correct answers are worked immediately afterwards**, in the same session, before you
  leave. Being wrong now and corrected now is the point of the exercise - it is what makes
  the material stick.
- Ten questions, one answer each. Some are from this week; some are from earlier in the
  programme, on purpose.

---

### Question 1

Unit 4 runs the same classifier on the 569-biopsy breast-cancer data, changing only how many principal components the classifier may see, and scores each row with the same 5-fold cross-validation:

| components | variance kept | 5-fold accuracy |
|---|---|---|
| 1 | 44.3% | 0.9121 |
| 2 | 63.2% | 0.9578 |
| 3 | 72.6% | 0.9491 |
| 5 | 84.7% | 0.9736 |
| 10 | 95.2% | 0.9807 |
| 20 | 99.6% | 0.9772 |
| 30 | 100.0% | 0.9789 |

The same classifier on all 30 raw features, with no PCA at all, scores 0.9789. Which conclusion do these numbers support?

A) Each component adds accuracy in proportion to the variance it carries, so keeping all 30 is the best choice  
B) PCA hurt this classifier here: the reduced models score below the 0.9789 that the 30 raw features reach with no reduction at all  
C) The dip at k = 3 shows the third component carries no variance, so it should be dropped from the model  
D) Accuracy flattens long before variance does — k = 5 already reaches 0.9736 while keeping only 84.7% of the variance  

---

### Question 2

A triage knowledge base holds 4,000 recorded patient facts and 300 rules. A clinician needs one answer: should Patient 7 be flagged for sepsis? Which inference strategy fits this request, and why?

A) Backward chaining: it starts from this one goal and expands just the rules that bear on the case  
B) Forward chaining: firing the rules in the order they were written is what makes a conclusion sound  
C) Backward chaining: it can withdraw a conclusion when a later fact turns out to contradict it  
D) Forward chaining: it derives the consequences of the 4,000 facts, and this answer is among them  

---

### Question 3

What is the main difference between traditional rule-based AI and modern data-driven AI?

A) Traditional AI uses neural networks, modern AI uses rules  
B) Traditional AI hides its reasoning, while modern AI can be audited line by line  
C) Traditional AI uses explicit rules, modern AI learns from data  
D) Traditional AI is faster, modern AI is slower  

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

The Unit 3 diagnosis system is given a patient with fever, cough and fatigue, and prints:

```
disease         prevalence  prior (norm.)  P(symptoms|d)   posterior   rank move
Common Cold         15.0%          68.2%           5.6%       19.6%       1 -> 3
Flu                  5.0%          22.7%          50.4%       58.9%       2 -> 1
COVID-19             2.0%           9.1%          45.9%       21.5%       3 -> 2
```

Common Cold is by far the most prevalent of the three diseases, yet it finishes last. Why?

A) Renormalising the three prevalences over one another pushes the largest of them below the other two  
B) Bayes multiplies prior by likelihood, and P(symptoms | Cold) = 5.6% is nine times below Flu's  
C) Common Cold has no listed probability for fatigue, so the system skips it in the product  
D) The posterior follows the highest single symptom probability, and Flu's fever figure is 90%  

---

### Question 7

What does depth-first search gain over breadth-first search on the same graph?

A) It reaches the goal in fewer edges when several paths exist  
B) It holds just the current path and its siblings, not a whole frontier level  
C) It visits each node once, where breadth-first search may expand the same node twice  
D) Its asymptotic running time is lower, O(V) against breadth-first search's O(V + E)  

---

### Question 8

Minimising `f(x) = x**2` from x = 5 for 30 steps, Unit 2 changes only the learning rate and prints: lr = 0.01 -> x = 2.72742; lr = 0.1 -> x = 0.0061897; lr = 0.9 -> x = 0.0061897; lr = 1.0 -> x = 5 with loss 25; lr = 1.1 -> x = 1186.88. On a log axis the lr = 0.9 loss curve lies exactly on top of the lr = 0.1 curve. What does that coincidence tell you?

A) The loss depends on |x| alone, so a smoothly falling curve can still hide a run that crosses the minimum each step  
B) A smoothly falling loss curve rules out instability, so the learning rate could safely be raised from 0.9 to 1.0 for speed  
C) lr = 0.9 takes smaller steps than lr = 0.1, which is why the two runs finish at the same value of x  
D) lr = 0.9 has settled into a second minimum of f that happens to sit at the same height as the first one  

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

**End of quiz. Your instructor works the answers now.**
