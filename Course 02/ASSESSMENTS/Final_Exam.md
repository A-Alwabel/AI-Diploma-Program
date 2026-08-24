# Final Exam: Python for Artificial Intelligence
## AIAT 112

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. Show your work for partial credit. Closed book; calculator allowed.

The exam covers all five units: search algorithms, knowledge representation, learning under uncertainty, optimization techniques, and AI-based learning models.

---

## Part 1: Multiple Choice (30 points)

### Question 1 (5 points)
Which Python library is used for numerical computations?

A) NumPy  
B) pandas  
C) matplotlib  
D) scikit-learn

---

### Question 2 (5 points)
Breadth-First Search (BFS) uses which data structure, and what does that guarantee in an unweighted graph?

A) A stack (LIFO); it guarantees the shortest path  
B) A queue (FIFO); it guarantees the fastest runtime  
C) A queue (FIFO); it guarantees the shortest path  
D) A priority queue; it guarantees the fewest explored nodes

---

### Question 3 (5 points)
A* search expands nodes in order of:

A) f(n) = g(n), the cost from the start  
B) f(n) = h(n), the estimated cost to the goal  
C) f(n) = g(n) − h(n)
D) f(n) = g(n) + h(n)  

---

### Question 4 (5 points)
In a rule-based system, forward chaining:

A) Starts from a goal and searches for rules that could prove it  
B) Starts from known facts and applies rules to derive new facts  
C) Removes facts that contradict the rules  
D) Orders the rules alphabetically before firing them

---

### Question 5 (5 points)
In Bayesian inference, the **prior** probability is:

A) The probability of the evidence  
B) The probability of a hypothesis after seeing the evidence  
C) Always equal to 0.5
D) The probability of a hypothesis before seeing the evidence  

---

### Question 6 (5 points)
In gradient descent, if the learning rate is too high, the algorithm:

A) Converges more slowly but always safely  
B) Stops after one iteration  
C) May overshoot the minimum and diverge  
D) Ignores the gradient

---

## Part 2: Short Answer Questions (30 points)

### Question 7 (10 points)
Explain the difference between NumPy arrays and Python lists. When would you use each?

---

### Question 8 (10 points)
A factory sensor raises an alarm when a product may be defective:

- P(defective) = 0.02
- P(alarm | defective) = 0.90
- P(alarm | not defective) = 0.10

Using Bayes' theorem, calculate **P(defective | alarm)**. Show your work. Then explain in one sentence why the result is much lower than 90%.

---

### Question 9 (10 points)
Explain the difference between **forward chaining** and **backward chaining** in a rule-based system. Give a small example of each using the rule "IF it is raining THEN the ground is wet."

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

Write a gradient descent loop that starts at `x = 0.0`, uses learning rate `0.2`, runs 50 iterations of `x ← x − lr · slope(error, x)`, and prints the final `x` and `error(x)`. State approximately what final value of `x` you expect and why.

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
A bank wants to predict whether a loan applicant will **default (yes/no)** from historical data with two features: monthly income and existing debt. Design a complete machine-learning solution in Python:

1. Which kind of ML problem is this (classification or regression), and why?
2. Name two suitable model families from this course and one strength of each.
3. Describe how you would evaluate the models fairly — name the data-splitting technique and the metrics you would report, and explain why training accuracy alone is not acceptable.
4. The bank says a missed defaulter costs far more than a false alarm. Name one change to your evaluation or decision threshold that respects this.

Write your answer as a short design document (bullet points allowed) with code sketches for the key steps (splitting, training, evaluating).

---

**End of Exam**

**Good Luck!**
