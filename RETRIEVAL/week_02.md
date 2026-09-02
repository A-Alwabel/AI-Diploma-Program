# Cumulative Retrieval Quiz - Week 02

**Course 01 - AIAT 111, Units 3, 4 and the opening of Unit 5**

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
D) Neither kind; a perceptron scores its inputs but does not assign a class  

---

### Question 5

A* orders its frontier by a score f(n). What is that score built from?

A) f(n) = g(n) + h(n) — the cost already paid to reach n, plus the estimated cost remaining  
B) f(n) = h(n) — the estimated cost from n to the goal, which is what makes the search informed  
C) f(n) = g(n) — the cost already paid from the start  
D) f(n) = g(n) - h(n) — the cost paid, discounted by the estimate of what remains  

---

### Question 6

A feedforward network's hidden layer needs an activation function. Which list contains three activation functions and nothing else?

A) Adam, SGD, RMSprop  
B) MSE, cross-entropy, hinge  
C) Dropout, batch normalization, early stopping  
D) ReLU, sigmoid, tanh  

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

A) Guaranteeing a correct diagnosis after a positive test  
B) Computing the prior probability of a hypothesis, before evidence is observed  
C) Eliminating uncertainty so that model predictions become deterministic  
D) Handling uncertainty and updating a belief as evidence arrives  

---

### Question 9

What is the main difference between traditional rule-based AI and modern data-driven AI?

A) Traditional AI uses neural networks, modern AI uses rules  
B) Traditional AI hides its reasoning, while modern AI can be audited line by line  
C) Traditional AI uses explicit rules, modern AI learns from data  
D) Traditional AI is faster, modern AI is slower  

---

### Question 10

What distinguishes a generative model from the classifiers studied earlier in Course 01?

A) It scores an input against a decision boundary it has fitted to labelled data  
B) It ranks training examples by how typical they are  
C) It draws new samples that resemble the data it was trained on  
D) It compresses the training set so that it can be stored and searched faster  

---

**End of quiz. Your instructor works the answers now.**
