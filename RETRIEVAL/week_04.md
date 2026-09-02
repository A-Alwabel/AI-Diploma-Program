# Cumulative Retrieval Quiz - Week 04

**Course 02 - AIAT 112, Units 2 and 3**

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

A triage knowledge base holds 4,000 recorded patient facts and 300 rules. A clinician needs one answer: should Patient 7 be flagged for sepsis? Which inference strategy fits this request, and why?

A) Backward chaining: it starts from this one goal and expands just the rules that bear on the case  
B) Forward chaining: firing the rules in the order they were written is what makes a conclusion sound  
C) Backward chaining: it can withdraw a conclusion when a later fact turns out to contradict it  
D) Forward chaining: it derives the consequences of the 4,000 facts, and this answer is among them  

---

### Question 2

A feedforward network's hidden layer needs an activation function. Which list contains three activation functions and nothing else?

A) Adam, SGD, RMSprop  
B) MSE, cross-entropy, hinge  
C) Dropout, batch normalization, early stopping  
D) ReLU, sigmoid, tanh  

---

### Question 3

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

### Question 4

What does depth-first search gain over breadth-first search on the same graph?

A) It reaches the goal in fewer edges when several paths exist  
B) It holds just the current path and its siblings, not a whole frontier level  
C) It visits each node once, where breadth-first search may expand the same node twice  
D) Its asymptotic running time is lower, O(V) against breadth-first search's O(V + E)  

---

### Question 5

An expert system is given three recorded facts about a patient and two rules. Run forward, what does the engine do?

A) It begins from a candidate conclusion and looks for facts that would support it  
B) It fires the rules in the order they were written, once each, and then stops  
C) It begins from the facts and fires the rules they satisfy, adding results as new facts  
D) It searches the rule set for the rule with the highest stated confidence and fires that one alone  

---

### Question 6

Why does a neural network put a non-linear activation function between its layers?

A) To keep the weights bounded so that training does not overflow  
B) So that stacked layers do not collapse into a single linear map  
C) To reduce the number of parameters the network has to store  
D) To speed up the matrix multiplications the forward pass performs  

---

### Question 7

A knowledge-based system stores what it knows separately from how it acts. What does its knowledge component consist of?

A) A relational database table with indexed columns and a query planner  
B) A labelled training dataset and a loss function  
C) A priority queue ordered by a heuristic function  
D) Rules, facts, and an inference mechanism that applies them  

---

### Question 8

A Bayesian calculation starts from a 1% chance that a patient has a disease and, after a positive test, prints 8.76%. Which number is the prior, and what does 'prior' mean?

A) 1% — the probability of the hypothesis before this evidence is taken into account  
B) 8.76% — the probability after the evidence has been taken into account  
C) Neither: the prior is the probability of the evidence itself, P(positive test)  
D) Neither: the prior is P(positive test | disease), the figure the test's manufacturer publishes  

---

### Question 9

What distinguishes a generative model from the classifiers studied earlier in Course 01?

A) It scores an input against a decision boundary it has fitted to labelled data  
B) It ranks training examples by how typical they are  
C) It draws new samples that resemble the data it was trained on  
D) It compresses the training set so that it can be stored and searched faster  

---

### Question 10

Which kind of AI exists today, rather than in theory?

A) General AI — a system that transfers competence across the full range of tasks a person can do  
B) Self-aware AI — a system aware of its own internal states  
C) Superintelligent AI — a system that outperforms the best humans at science, strategy and persuasion  
D) Narrow AI — a system specialised for one task, such as a spam filter  

---

**End of quiz. Your instructor works the answers now.**
