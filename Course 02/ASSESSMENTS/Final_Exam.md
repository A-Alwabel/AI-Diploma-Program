# Final Exam: Python for Artificial Intelligence
## AIAT 112

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. Show your work for partial credit. Closed book; calculator allowed.

**Marking scheme:** Part 1 (Q1–Q6): 5 pts each = 30. Part 2 (Q7–Q9): 10 pts each = 30. Part 3 (Q10: 15 pts, Q11: 10 pts) = 25. Part 4 (Q12): 15 pts. **Total: 100.**

The exam covers the Python libraries of Unit 1 and all five units: search algorithms, knowledge representation, learning under uncertainty, optimization techniques, and AI-based learning models. Every printed table quoted below is output from a notebook you ran in this course; read the numbers, do not recall them.

---

## Part 1: Multiple Choice (30 points)

Choose one option per question. No partial credit.

### Question 1 (5 points)
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
D) NumPy runs about 100× faster here, the speed-up the notebook's own text quotes

---

### Question 2 (5 points)
The Unit 1 search notebook runs A\* with the heuristic `h(n) = |ord(n) - ord(goal)|` and checks it against the true remaining cost `h*`:

```
   A: h=6, h*=3  ->  OVERESTIMATES by 3
   B: h=5, h*=2  ->  OVERESTIMATES by 3
   E: h=2, h*=1  ->  OVERESTIMATES by 1
   G: h=0, h*=0  ->  OK
```

A\* then returns `A -> B -> E -> G`, which is the shortest path on that graph, having opened 6 of the 7 nodes (BFS opened 7). What does this run establish about the heuristic?

A) h is admissible, because the path A\* returned is in fact the shortest one on this graph  
B) The overestimates are uniform across nodes, so they cancel and the guarantee holds  
C) h is inadmissible, and that is what made A\* open 6 nodes where BFS had to open 7  
D) h overestimates, so the guarantee did not apply — the shortest path came back anyway

---

### Question 3 (5 points)
A triage knowledge base holds 4,000 recorded patient facts and 300 rules. A clinician needs one answer: *should Patient 7 be flagged for sepsis?* Which inference strategy fits this request, and why?

A) Backward chaining: it starts from this one goal and expands just the rules that bear on the case  
B) Forward chaining: firing the rules in the order they were written is what makes a conclusion sound  
C) Backward chaining: it can withdraw a conclusion when a later fact turns out to contradict it  
D) Forward chaining: it derives the consequences of the 4,000 facts, and this answer is among them

---

### Question 4 (5 points)
The Unit 3 diagnosis system is given a patient with fever, cough and fatigue, and prints:

```
disease         prevalence  prior (norm.)  P(symptoms|d)   posterior   rank move
Common Cold         15.0%          68.2%           5.6%       19.6%       1 → 3
Flu                  5.0%          22.7%          50.4%       58.9%       2 → 1
COVID-19             2.0%           9.1%          45.9%       21.5%       3 → 2
```

Common Cold is by far the most prevalent of the three diseases, yet it finishes last. Why?

A) Renormalising the three prevalences over one another pushes the largest of them below the rest  
B) Common Cold has no listed probability for fatigue, so the system skips it in the product  
C) Bayes multiplies prior by likelihood, and P(symptoms | Cold) = 5.6% is nine times below Flu's  
D) The posterior follows the highest single symptom probability, and Flu's fever figure is 90%

---

### Question 5 (5 points)
The Unit 4 notebook runs gradient descent on `f(x) = x²` from `x = 5.0`, changing only the learning rate:

```
learning rate     x @ step 0   x @ step 3   x @ step 6  x @ step 12  x @ step 25   verdict
0.01                  5.0000       4.7060       4.4292       3.9236       3.0173   too small
0.10                  5.0000       2.5600       1.3107       0.3436       0.0189   just right
0.95                  5.0000      -3.6450       2.6572       1.4121      -0.3589   too big
1.10                  5.0000      -8.6400      14.9299      44.5805    -476.9810   way too big
```

A student concludes: *"a learning rate that overshoots the minimum will diverge."* Which row refutes that, and how?

A) lr = 0.01: it stays on one side of the minimum, so overshoot is not required in order to converge  
B) lr = 0.95: it lands beyond the minimum (x = −3.65 at step 3) and still closes in to |x| = 0.36  
C) lr = 0.10: it reaches x = 0.019 without overshooting, so overshoot is what slows a run down  
D) lr = 1.10: its sign alternates, showing that overshoot and divergence are the same behaviour

---

### Question 6 (5 points)
One trained logistic-regression model is scored on the same 171 held-out breast-tumour biopsies; only the decision threshold changes:

```
    threshold   missed malignant   false alarms   accuracy
   --------------------------------------------------------
         0.10                  0             38     77.8%
         0.20                  1             21     87.1%
         0.30                  5             12     90.1%
         0.40                  7              9     90.6%
         0.50                 11              5     90.6%
         0.60                 13              4     90.1%
         0.70                 16              3     88.9%
         0.80                 20              0     88.3%
         0.90                 29              0     83.0%

   Best accuracy on this grid: 92.4% at threshold 0.44 — which still misses 8 malignant tumours.
```

A screening clinic can absorb at most 25 false alarms out of the 171, and within that limit wants to miss as few malignant tumours as it can. Which threshold does the table support, and at what cost?

A) 0.44 — it is the highest accuracy on the grid, 92.4%, and accuracy is the metric to maximise  
B) 0.80 — it brings false alarms down to zero, and 88.3% accuracy is near the grid maximum  
C) 0.50 — it is the library default, so it already balances the two kinds of error by construction  
D) 0.20 — it misses 1 malignant tumour rather than 11, and its 21 false alarms fit the budget

---

## Part 2: Short Answer Questions (30 points)

### Question 7 (10 points)
The Unit 1 libraries notebook times one removal from the front of a queue, for two containers holding the same items:

```
 queue size    list.pop(0)   deque.popleft()   list costs
      1,000       0.0669 us          0.0236 us           3x
      4,000       0.1657 us          0.0246 us           7x
     16,000       0.6301 us          0.0241 us          26x
     32,000       1.7127 us          0.0246 us          69x
```

**(a)** Using these two columns, explain what "O(1) versus O(n)" means here, and say which container is which. *(4 pts)*

**(b)** BFS removes one item from the front of its frontier for every node it expands. Explain what happens to the running time of a BFS whose frontier is a plain Python list instead of a `deque`, and why `from collections import deque` is therefore a complexity decision rather than a style preference. *(4 pts)*

**(c)** The same notebook measured a NumPy speed-up of **0.5×** at N = 10 — that is, NumPy was slower. Name one situation in this course where a plain Python list is the right container and a NumPy array is not. *(2 pts)*

---

### Question 8 (10 points)
A factory sensor raises an alarm when a product may be defective:

- P(defective) = 0.02
- P(alarm | defective) = 0.90
- P(alarm | not defective) = 0.10

Using Bayes' theorem, calculate **P(defective | alarm)**. Show your work. Then explain in one sentence why the result is much lower than 90%.

---

### Question 9 (10 points)
The Unit 2 expert system starts from three recorded facts — `Patient1 has Fever`, `Patient1 has Cough`, `Patient1 has Fatigue` — and two rules:

```
R1: IF X has Fever AND X has Cough AND X has Fatigue  THEN  X likely_has Flu
R2: IF X likely_has Flu                               THEN  X recommend Rest
```

**(a)** Forward chaining ends holding 5 facts, not 4. Explain what lets R2 fire, and why the engine has to pass over the rule set more than once. *(5 pts)*

**(b)** The notebook re-runs the identical two rules against a knowledge base in which `Fatigue` was never recorded. It reports **2 facts, 0 derived** — and prints no warning. Name the assumption that makes *"fatigue was not recorded"* and *"the patient has no fatigue"* the same thing to this engine, and give one consequence of that assumption for a real clinic. *(5 pts)*

---

## Part 3: Practical/Coding Questions (25 points)

### Question 10 (15 points)
A graph is given as an adjacency dictionary, for example:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D'],
}
```

Write a function `bfs_path(graph, start, goal)` that uses **Breadth-First Search** (with `collections.deque`) to return a shortest path from `start` to `goal` as a list of nodes, or `None` if no path exists. Do not revisit already-seen nodes.

---

### Question 11 (10 points)
The production error of a machine setting `x` is `error(x) = (x - 3) ** 2`. The slope at any point can be *measured* numerically (no calculus needed):

```python
def slope(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)
```

**(a)** Write a gradient descent loop that starts at `x = 0.0`, uses learning rate `0.2`, runs 50 iterations of `x ← x − lr · slope(error, x)`, and prints the final `x` and `error(x)`. State approximately what final value of `x` you expect, and why. *(8 pts)*

**(b)** Unit 4 ran the same kind of loop on `f(x) = x²` and found that `lr = 0.95` converged while `lr = 1.10` diverged. State what your loop above would do at `lr = 1.2`, and justify it in one or two sentences. *(2 pts)*

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
A bank wants to predict whether a loan applicant will **default (yes/no)** from historical data with two features: monthly income and existing debt. Design a complete machine-learning solution in Python:

1. Which kind of ML problem is this (classification or regression), and why?
2. Name two suitable model families from this course and one strength of each.
3. Describe how you would evaluate the models fairly — name the data-splitting technique and the metrics you would report, and explain why training accuracy alone is not acceptable. In Unit 5, five cross-validation folds of one model on one dataset scored MSE **0.5230, 0.5746, 0.5755, 0.7748, 0.8388** — the worst fold 60% worse than the best, with nothing changed but which rows were held out. Use that measurement in your argument.
4. The bank says a missed defaulter costs far more than a false alarm. Name one change to your training, your decision threshold or your reported metric that respects this, and say what it costs you in the other direction.

Write your answer as a short design document (bullet points allowed) with code sketches for the key steps (splitting, training, evaluating).

---

**End of Exam**

**Good Luck!**
