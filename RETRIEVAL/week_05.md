# Cumulative Retrieval Quiz - Week 05

**Course 02 - AIAT 112, Units 3 and 4**

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

The Unit 4 notebook runs gradient descent on `f(x) = x**2` from `x = 5.0`, changing only the learning rate:

```
learning rate     x @ step 0   x @ step 3   x @ step 6  x @ step 12  x @ step 25   verdict
0.01                  5.0000       4.7060       4.4292       3.9236       3.0173   too small
0.10                  5.0000       2.5600       1.3107       0.3436       0.0189   just right
0.95                  5.0000      -3.6450       2.6572       1.4121      -0.3589   too big
1.10                  5.0000      -8.6400      14.9299      44.5805    -476.9810   way too big
```

A student concludes: "a learning rate that overshoots the minimum will diverge." Which row refutes that, and how?

A) lr = 0.01: it stays on one side of the minimum, so overshoot is not required in order to converge  
B) lr = 0.95: it lands beyond the minimum (x = -3.65 at step 3) and still closes in to |x| = 0.36  
C) lr = 1.10: its sign alternates, showing that overshoot and divergence are the same behaviour  
D) lr = 0.10: it reaches x = 0.019 without overshooting, so overshoot is what slows a run down  

---

### Question 2

A* orders its frontier by a score f(n). What is that score built from?

A) f(n) = g(n) + h(n) — the cost already paid to reach n, plus the estimated cost remaining  
B) f(n) = h(n) — the estimated cost from n to the goal, which is what makes the search informed  
C) f(n) = g(n) — the cost already paid from the start  
D) f(n) = g(n) - h(n) — the cost paid, discounted by the estimate of what remains  

---

### Question 3

A Course 01 notebook starts from a 1% prior that a patient has a disease and, after a positive test, prints P(disease | positive) = 8.76%. What is Bayesian probability used for in AI?

A) Guaranteeing a correct diagnosis after a positive test  
B) Computing the prior probability of a hypothesis, before evidence is observed  
C) Eliminating uncertainty so that model predictions become deterministic  
D) Handling uncertainty and updating a belief as evidence arrives  

---

### Question 4

Gradient descent updates a parameter with a minus sign: `x <- x - lr * gradient`. Why the minus?

A) The gradient is negative wherever the function is decreasing, and the minus sign restores its sign  
B) The minus sign keeps the parameter positive, which most loss functions require  
C) The gradient points in the direction in which the function rises fastest, so we step against it  
D) The gradient gives the distance to the minimum, and the minus sign subtracts that distance  

---

### Question 5

Three of these tasks are AI applications of the kind this course studies. Which one is not?

A) Flagging a card transaction as fraudulent from the pattern of a customer's past spending  
B) Forecasting tomorrow's rainfall from decades of recorded weather records  
C) Sorting a spreadsheet column alphabetically with a fixed comparison rule  
D) Reading a tumour boundary out of an MRI scan  

---

### Question 6

Why does a neural network put a non-linear activation function between its layers?

A) To keep the weights bounded so that training does not overflow  
B) So that stacked layers do not collapse into a single linear map  
C) To reduce the number of parameters the network has to store  
D) To speed up the matrix multiplications the forward pass performs  

---

### Question 7

In the update `x <- x - lr * gradient`, what does `lr` control?

A) The number of iterations the loop will run before it stops  
B) The point the loop starts from, which fixes how close it begins to the minimum  
C) The threshold below which the gradient counts as zero and the loop terminates  
D) How far along the negative gradient the parameter moves at each step  

---

### Question 8

Which event is treated as the founding of AI as a named field of study?

A) The 1956 Dartmouth summer workshop, at which the term was coined  
B) Turing's 1950 paper proposing the imitation game as a test for machine thinking  
C) Deep Blue's 1997 defeat of the reigning world chess champion  
D) The 2022 public release of ChatGPT  

---

### Question 9

Two Course 01 notebooks fit models on the same kind of table. One is given feature columns X together with a label column y; the other is given X alone. What separates supervised from unsupervised learning?

A) Supervised learning is faster  
B) Supervised learning predicts numbers, unsupervised learning predicts categories  
C) Supervised learning uses labelled data, unsupervised learning uses unlabelled data  
D) Supervised learning uses neural networks, unsupervised learning uses clustering algorithms  

---

### Question 10

Breadth-first search keeps a frontier of nodes it has discovered but not yet expanded. What container does it use for that frontier, and why?

A) A stack, so the most recently discovered node is expanded first  
B) A queue, so the earliest discovered node is expanded first  
C) The visited set that records which nodes have been expanded already  
D) A priority queue ordered by f(n) = g(n) + h(n)  

---

**End of quiz. Your instructor works the answers now.**
