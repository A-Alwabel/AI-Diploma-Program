# Retrieval Quiz — Week 05

**Week 05 of 35 · Course 02 — AIAT 112 (Python for Artificial Intelligence)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Under its learning-rate table, the Unit 4 notebook printed where each gradient-descent run on `f(x) = x²` stood after 25 steps from `x = 5.0`:

```
Distance from the optimum after 25 steps:
   lr = 0.01  |x| =     3.0173   f(x) =   9.1042e+00   (too small)
   lr = 0.1   |x| =     0.0189   f(x) =   3.5681e-04   (just right)
   lr = 0.95  |x| =     0.3589   f(x) =   1.2884e-01   (too big)
   lr = 1.1   |x| =   476.9810   f(x) =   2.2751e+05   (way too big)
```

A student disputes the two bottom verdicts: *"0.95 and 1.1 both jump across the minimum on every step, so they are the same failure and both deserve 'way too big'."* What in this printout separates the two rows?

A) The labels alone: both |x| values belong to runs that crossed the minimum on each step, so the printout gives the student no numerical ground for keeping the two verdicts apart  
B) The f(x) column read against a cut-off: 1.2884e-01 is below 1 and 2.2751e+05 is far above it, and a cost under 1 is the notebook's working test for having converged  
C) The 0.1 row: its 0.0189 is the one distance that has essentially reached zero, so a run still 0.3589 away after 25 steps has failed in the same way 1.1 did  
D) Which way |x| moved: 0.95 ends 0.3589 away, nearer than its start at 5.0, while 1.1 ends 476.9810 away — crossing while shrinking converges, crossing while growing diverges  

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

A) Confirming a diagnosis once a test comes back positive  
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
