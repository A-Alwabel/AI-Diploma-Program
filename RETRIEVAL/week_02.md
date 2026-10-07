# Retrieval Quiz — Week 02

**Week 02 of 35 · Course 01 — AIAT 111 (Introduction to Artificial Intelligence and Applications)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Why does a neural network put a non-linear activation function between its layers?

A) To keep the weights bounded so that training does not overflow  
B) So that stacked layers do not collapse into a single linear map  
C) To reduce the number of parameters the network has to store  
D) To speed up the matrix multiplications the forward pass performs  

---

### Question 2

Breadth-first search keeps a frontier of nodes it has discovered but not yet expanded. What container does it use for that frontier, and why?

A) A stack, so the most recently discovered node is expanded first  
B) A queue, so the earliest discovered node is expanded first  
C) The visited set that records which nodes have been expanded already  
D) A priority queue ordered by f(n) = g(n) + h(n)  

---

### Question 3

Two Course 01 notebooks fit models on the same kind of table. One is given feature columns X together with a label column y; the other is given X alone. What separates supervised from unsupervised learning?

A) Supervised learning is faster  
B) Supervised learning predicts numbers, unsupervised learning predicts categories  
C) Supervised learning uses labelled data, unsupervised learning uses unlabelled data  
D) Supervised learning uses neural networks, unsupervised learning uses clustering algorithms  

---

### Question 4

A single perceptron computes one weighted sum of its inputs and passes it through a step function. Which problems can it solve?

A) Problems whose two classes can be separated by a single straight boundary  
B) Problems with a curved decision boundary, which the step function bends to fit  
C) Problems of both kinds, provided it is trained for enough epochs  
D) Problems of neither kind, since a perceptron scores its inputs but does not assign a class  

---

### Question 5

A* orders its frontier by a score f(n). What is that score built from?

A) f(n) = g(n) + h(n) — the cost already paid to reach n, plus the estimated cost remaining  
B) f(n) = h(n) — the estimated cost from n to the goal, which is what makes the search informed  
C) f(n) = g(n) — the cost already paid from the start  
D) f(n) = g(n) - h(n) — the cost paid, discounted by the estimate of what remains  

---

### Question 6

Before training anything, the single-neuron lesson printed this table:

```
     z |  sigmoid |    tanh |  relu
   1.0 |    0.731 |   0.762 |   1.0
   3.0 |    0.953 |   0.995 |   3.0
```

The training cell that followed compiled the neuron with `Adam(learning_rate=0.05)` and `loss="mse"`. A classmate files sigmoid, tanh and relu under "things that score the model". What job do the three functions in this table actually do inside a `Dense(1)` neuron?

A) They measure how far the neuron's output is from the 0/1 label, which is the scoring job that `mse` also performs in the compile line  
B) They decide how much each weight moves after a batch, which is why the learning rate 0.05 is set right beside them  
C) They switch random units off during training to limit overfitting, the way dropout does in a larger network  
D) They turn the weighted sum `z` into the neuron's output, which is why each column is a different reshaping of the same `z`  

---

### Question 7

Which event is treated as the founding of AI as a named field of study?

A) The 1956 Dartmouth summer workshop, at which the term was coined  
B) Turing's 1950 paper proposing the imitation game as a test for machine thinking  
C) Deep Blue's 1997 defeat of the reigning world chess champion  
D) The 2022 public release of ChatGPT  

---

### Question 8

A Course 01 notebook starts from a 1% prior that a patient has a disease and, after a positive test, prints P(disease | positive) = 8.76%. What is Bayesian probability used for in AI?

A) Confirming a diagnosis once a test comes back positive  
B) Computing the prior probability of a hypothesis, before evidence is observed  
C) Eliminating uncertainty so that model predictions become deterministic  
D) Handling uncertainty and updating a belief as evidence arrives  

---

### Question 9

The weather recommender in Course 01's first lesson printed two neighbouring cases:

```
26 °C, 59% humidity, morning -> Go for a jog in the park
26 °C, 61% humidity, morning -> Moderate weather, any outdoor activity is fine
```

A classmate concludes that the recommender "learned a humidity boundary near 60% from past weather data". Which statement describes where that boundary actually came from, and what it tells you about the system's family?

A) The 60% cut was fitted from the four printed test cases, which makes the recommender a small data-driven model of the kind Unit 2 trains  
B) The jump between 59% and 61% shows the system hides its reasoning, which is the mark of a modern learned model  
C) The two answers differ because the hand-written rule evaluates faster than a fitted model would; speed is what separates the two families  
D) A person typed `humidity < 60` into an `if` statement, so the system is rule-based: the threshold was authored, not fitted to data  

---

### Question 10

What distinguishes a generative model from the classifiers studied earlier in Course 01?

A) It scores an input against a decision boundary it has fitted to labelled data  
B) It ranks training examples by how typical they are  
C) It draws new samples that resemble the data it was trained on  
D) It compresses the training set so that it can be stored and searched faster  

---
