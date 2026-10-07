# Retrieval Quiz — Week 03

**Week 03 of 35 · Course 01 — AIAT 111 (Introduction to Artificial Intelligence and Applications) and Course 02 — AIAT 112 (Python for Artificial Intelligence)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The Unit 1 libraries notebook timed the doubling of 1,000,000 numbers twice. A one-shot timing cell printed:

```
   Python list comprehension :    11.05 ms
   NumPy, whole array at once:     0.71 ms
   Speed-up measured here    :     15.5x

Against the "100x faster" line in the Part 2 text above:
   this run measured 15.5x - well short of 100x.
```

The next cell re-timed six array sizes, keeping the best of three trials after a warm-up, and closed with:

```
Smallest N (10):        NumPy is SLOWER (0.5x)
Largest N (1,000,000): NumPy is 62x faster
```

A teammate wants to vectorise a helper that is called thousands of times per second on arrays of about ten values, and quotes the 62x as the gain to expect. Which printed line actually bears on that helper, and what does it say?

A) `Largest N (1,000,000): NumPy is 62x faster` — the compiled loop is the same code at any N, so the factor carries over to ten values  
B) `Smallest N (10): NumPy is SLOWER (0.5x)` — on ten values the per-call setup cost is the whole job, so the plain list stays ahead  
C) `this run measured 15.5x` — one honest measurement on this machine, so that is the realistic gain for the helper to expect  
D) The Part 2 text's `100x faster` — the 15.5x and 62x were pulled down by timing noise, so the tutorial figure is the safer planning estimate  

---

### Question 2

Two Course 01 notebooks fit models on the same kind of table. One is given feature columns X together with a label column y; the other is given X alone. What separates supervised from unsupervised learning?

A) Supervised learning is faster  
B) Supervised learning predicts numbers, unsupervised learning predicts categories  
C) Supervised learning uses labelled data, unsupervised learning uses unlabelled data  
D) Supervised learning uses neural networks, unsupervised learning uses clustering algorithms  

---

### Question 3

Which of these models can produce a new data point that was not in its training set?

A) Logistic regression, which fits a boundary and returns a class probability  
B) A generative adversarial network, whose generator is trained to produce samples  
C) A support vector machine, which places a boundary at the widest margin it can find  
D) A decision tree, which splits the feature space and labels each region  

---

### Question 4

On an unweighted graph — one in which each edge costs the same — which search is guaranteed to return a path with the fewest edges?

A) Breadth-first search, because it finishes depth level d before opening depth level d+1  
B) Depth-first search, because it commits to one branch and stops as soon as the goal appears  
C) Whichever visits fewer nodes here, since less searching means a shorter path  
D) Dijkstra's algorithm, since a fewest-edge result needs edge weights and a priority queue  

---

### Question 5

The Unit 1 libraries notebook times one removal from the front of a queue, for two containers holding the same items:

```
 queue size    list.pop(0)   deque.popleft()   list costs
      1,000       0.0669 us          0.0236 us           3x
      4,000       0.1657 us          0.0246 us           7x
     16,000       0.6301 us          0.0241 us          26x
     32,000       1.7127 us          0.0246 us          69x
```

What does this table show about `collections.deque`?

A) It uses less memory per element, which is what makes the removal cheaper  
B) It is faster at each operation a list supports, so it should replace lists generally  
C) Its removal cost stays flat as the queue grows, where the list's rises with size  
D) The gap closes at large sizes, because both containers end up copying the same underlying data  

---

### Question 6

A single perceptron computes one weighted sum of its inputs and passes it through a step function. Which problems can it solve?

A) Problems whose two classes can be separated by a single straight boundary  
B) Problems with a curved decision boundary, which the step function bends to fit  
C) Problems of both kinds, provided it is trained for enough epochs  
D) Problems of neither kind, since a perceptron scores its inputs but does not assign a class  

---

### Question 7

A discriminative classifier and a generative model are trained on the same labelled dataset. Which probability does the generative model learn?

A) P(Y | X) — the probability of the label given the features, which is what a fitted decision boundary encodes  
B) P(X) alone — how the features are distributed, with the labels discarded  
C) P(Y) alone — how often each label occurs in the training set  
D) P(X | Y) with P(Y) — how the features are distributed inside each class, and how common each class is  

---

### Question 8

What is the main goal of artificial intelligence as a field?

A) To reproduce the biological structure of the human brain, neuron by neuron, in software  
B) To simulate human intelligence in machines  
C) To remove human judgement from decisions a machine can score numerically  
D) To automate repetitive clerical work  

---

### Question 9

A Course 01 notebook starts from a 1% prior that a patient has a disease and, after a positive test, prints P(disease | positive) = 8.76%. What is Bayesian probability used for in AI?

A) Confirming a diagnosis once a test comes back positive  
B) Computing the prior probability of a hypothesis, before evidence is observed  
C) Eliminating uncertainty so that model predictions become deterministic  
D) Handling uncertainty and updating a belief as evidence arrives  

---

### Question 10

Course 01 introduces the perceptron before the first multi-layer network. What is a perceptron?

A) A single neuron: a weighted sum of the inputs, plus a bias, through a step function  
B) A rule of the form IF condition THEN conclusion, applied to facts by an inference engine  
C) A node-and-edge structure over which a search algorithm looks for a path  
D) A method for choosing which features to keep before a model is fitted  

---
