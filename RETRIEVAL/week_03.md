# Cumulative Retrieval Quiz - Week 03

**Course 01 wrap-up and Course 02 - AIAT 112 (Python for AI), Unit 1**

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

The Unit 1 libraries notebook doubles the same numbers twice — once as a Python list comprehension, once as one NumPy whole-array operation — and prints:

```
         N    list (ms)   NumPy (ms)   speed-up
        10       0.0001       0.0003       0.5x
       100       0.0009       0.0003       3.0x
     1,000       0.0123       0.0006      21.5x
    10,000       0.1195       0.0032      37.1x
   100,000       1.2403       0.0254      48.8x
 1,000,000      15.1218       0.2454      61.6x
```

Which statement is supported by this table?

A) The list version scales better, because its cost per element falls as N grows  
B) NumPy's lead grows with N, and at N = 10 the list version is the faster of the two  
C) Both converge to the same speed at large N, since each loop is run by the interpreter  
D) NumPy runs about 100x faster here, the speed-up the notebook's own text quotes  

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
D) Dijkstra's algorithm; a fewest-edge guarantee needs edge weights and a priority queue  

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
D) Neither kind; a perceptron scores its inputs but does not assign a class  

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

A) Guaranteeing a correct diagnosis after a positive test  
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

**End of quiz. Your instructor works the answers now.**
