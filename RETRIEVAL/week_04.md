# Retrieval Quiz — Week 04

**Week 04 of 35 · Course 02 — AIAT 112 (Python for Artificial Intelligence)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

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

A) Forward chaining: data-driven, firing whichever rules the recorded facts satisfy until a pass adds no new fact — the loop that stopped above after 2 iterations  
B) Forward chaining: the Flu Diagnosis Rule was entered before the Flu Treatment Rule, and firing rules in the order they were written is what keeps the chain valid  
C) Backward chaining: it would prove `recommend Rest` for one patient at a time, and a focused proof costs less than deriving facts even when no goal has been named  
D) Backward chaining: if a later observation contradicts `likely_has Flu`, it can take back the `Rest` recommendation, which a forward chainer has no way to do  

---

### Question 2

Before training anything, the single-neuron lesson printed this table:

```
     z |  sigmoid |    tanh |  relu
   1.0 |    0.731 |   0.762 |   1.0
   3.0 |    0.953 |   0.995 |   3.0
```

The training cell that followed compiled the neuron with `Adam(learning_rate=0.05)` and `loss="mse"`. A classmate files sigmoid, tanh and relu under "things that score the model". What job do the three functions in this table actually do inside a `Dense(1)` neuron?

A) They measure how far the neuron's output is from the 0/1 label, which is the scoring job that `mse` also performs in the compile line  
B) They decide how much each weight moves after a batch, which is why the learning rate 0.05 is set right beside them  
C) They turn the weighted sum `z` into the neuron's output, which is why each column is a different reshaping of the same `z`  
D) They switch random units off during training to limit overfitting, the way dropout does in a larger network  

---

### Question 3

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
C) Normalising the three posteriors to sum to 100% hands the leader a share of the others' mass, which is what widens a near-tie into 58.91% against 21.46%  
D) With the likelihoods this close, the prior decides: Flu's normalised prior of 22.7% is more than twice COVID-19's 9.1%, and Bayes multiplies the two  

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
C) A third number: the prior is the probability of the evidence itself, P(positive test)  
D) A third number: the prior is P(positive test | disease), the figure the test's manufacturer publishes  

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
