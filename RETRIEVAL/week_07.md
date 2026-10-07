# Retrieval Quiz — Week 07

**Week 07 of 35 · Course 03 — AIAT 113 (Mathematics and Probability for Machine Learning)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The matrix-operations lesson redraws its fusion experiment on the 1,797 mean-centred digit images and adds a third route, `relu(X @ W1) @ W2`, with a ReLU between the two layers. The printed reading of the figure is:

```
Blue points (no activation): 2.0e-14 is the largest amount any of the 17,970 output numbers differs from the fused one-layer network.
Orange points (ReLU inserted): up to 11.8 away from the diagonal, on outputs that span roughly -19 to +18.
```

A classmate argues that the ReLU is a minor numerical detail and that the real lesson is which bracketing is cheaper. Which reading of these two printed gaps is correct?

A) Both gaps are rounding noise; the ReLU route sits further off because `max()` adds another rounded operation per entry  
B) The 2.0e-14 gap shows the layer-by-layer route drifts from the fused one, so even without a ReLU the two layers compute a slightly different function  
C) The orange points leave the diagonal because the digits were mean-centred, not because of the ReLU; on raw pixels the same ReLU would spread them as far  
D) The 2.0e-14 gap says the two linear routes are one function; the 11.8 gap says the ReLU made a genuinely different model  

---

### Question 2

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

The eigenvalues lesson notes that the raw USArrests features live on very different ranges — Murder spans 0.8–17.4 and Assault 45–337 arrests per 100,000 — and its figure note says that on raw units PC1 'points almost straight up: 99.8% of it is the Assault axis'. After standardizing, the printed feature variances are Murder = 1.02 and Assault = 1.02, and PC2 keeps 9.91% of the variance. A colleague wants to send the raw-units decomposition to a state governor because 'it explains far more of the variance'. Why is the standardized run the one to report?

A) Standardizing gives both features a variance of 1.02, which adds spread for PC1 to explain that the raw run lacked  
B) The 9.91% left to PC2 after standardizing shows the raw run had dropped its second component and summed over a single eigenvalue  
C) On raw units PC1 is nearly the Assault column renamed, so its variance figure describes the recording scale, not a crime pattern  
D) Because 99.8% of raw PC1 lies along Assault, the raw covariance matrix is close to singular and its eigenvalues cannot be trusted  

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
D) Problems of neither kind, since a perceptron scores its inputs but does not assign a class  

---

### Question 10

Which kind of AI exists today, rather than in theory?

A) General AI — a system that transfers competence across the full range of tasks a person can do  
B) Self-aware AI — a system aware of its own internal states  
C) Superintelligent AI — a system that outperforms the best humans at science, strategy and persuasion  
D) Narrow AI — a system specialised for one task, such as a spam filter  

---
