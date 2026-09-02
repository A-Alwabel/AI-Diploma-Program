# Cumulative Retrieval Quiz - Week 07

**Course 03 - AIAT 113 (Mathematics and Probability for ML), Units 1 and 2**

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

Unit 1 computes the same two-layer transformation of the same data two ways: Route A as `(X @ W1) @ W2`, using 8,510,592 scalar multiplications, and Route B as `X @ (W1 @ W2)`, using 1,191,040. The largest disagreement between the two outputs is 1.33e-14. What does this establish about a two-layer network with no activation function between the layers?

A) Route B is cheaper because it drops the hidden layer, so its output is an approximation  
B) The 1.33e-14 disagreement shows the two routes compute different functions, so the order the products are taken in matters  
C) The two layers can be replaced by one layer with weight matrix `W1 @ W2` without changing the function computed  
D) The second layer re-weights the first layer's outputs, so stacking the two adds expressive power a single layer lacks  

---

### Question 2

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

### Question 3

What is the main goal of artificial intelligence as a field?

A) To reproduce the biological structure of the human brain, neuron by neuron, in software  
B) To simulate human intelligence in machines  
C) To remove human judgement from decisions a machine can score numerically  
D) To automate repetitive clerical work  

---

### Question 4

Two Course 01 notebooks fit models on the same kind of table. One is given feature columns X together with a label column y; the other is given X alone. What separates supervised from unsupervised learning?

A) Supervised learning is faster  
B) Supervised learning predicts numbers, unsupervised learning predicts categories  
C) Supervised learning uses labelled data, unsupervised learning uses unlabelled data  
D) Supervised learning uses neural networks, unsupervised learning uses clustering algorithms  

---

### Question 5

A layer computes `X @ W`, with X of shape (3, 2). Which shapes of W make the product defined, and what shape does the result have?

A) W of shape (3, 2), giving a product of shape (3, 2)  
B) W of shape (2, p) for some p, giving a product of shape (3, p)  
C) W of whatever shape; NumPy broadcasts the smaller operand to fit  
D) W of shape (2, 2), since a square second matrix is what makes the product defined  

---

### Question 6

A* orders its frontier by a score f(n). What is that score built from?

A) f(n) = g(n) + h(n) — the cost already paid to reach n, plus the estimated cost remaining  
B) f(n) = h(n) — the estimated cost from n to the goal, which is what makes the search informed  
C) f(n) = g(n) — the cost already paid from the start  
D) f(n) = g(n) - h(n) — the cost paid, discounted by the estimate of what remains  

---

### Question 7

On the 50-state USArrests data (Murder, Assault), Unit 1 eigen-decomposes the covariance matrix twice.

- **Standardized:** eigenvalues 1.8019 and 0.1981; PC1 = +0.707 x Murder +0.707 x Assault; PC1 explains 90.09% of the variance.
- **Raw units:** feature variances Murder 18.97 and Assault 6945.17; PC1 = +0.042 x Murder +0.999 x Assault; PC1 explains 99.90% of the variance.

Why is the raw-units 99.90% the less informative of the two figures?

A) The raw-units run keeps one component while the standardized run keeps two, so the two percentages count different totals  
B) Standardizing increases the variance available to PC1, so 90.09% of standardized variance carries more information than the raw 99.90%  
C) A first component above 99% means the raw covariance matrix is singular  
D) On raw units PC1 follows Assault, whose variance is 6945 against Murder's 19, so it reports the measuring scale  

---

### Question 8

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

### Question 9

A single perceptron computes one weighted sum of its inputs and passes it through a step function. Which problems can it solve?

A) Problems whose two classes can be separated by a single straight boundary  
B) Problems with a curved decision boundary, which the step function bends to fit  
C) Problems of both kinds, provided it is trained for enough epochs  
D) Neither kind; a perceptron scores its inputs but does not assign a class  

---

### Question 10

Which kind of AI exists today, rather than in theory?

A) General AI — a system that transfers competence across the full range of tasks a person can do  
B) Self-aware AI — a system aware of its own internal states  
C) Superintelligent AI — a system that outperforms the best humans at science, strategy and persuasion  
D) Narrow AI — a system specialised for one task, such as a spam filter  

---

**End of quiz. Your instructor works the answers now.**
