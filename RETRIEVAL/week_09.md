# Cumulative Retrieval Quiz - Week 09

**Course 03 wrap-up and Course 04 - AIAT 114 (ML Algorithms), Unit 1**

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

Unit 5 draws a sample of n = 100 from the 714 recorded Titanic passenger ages and prints a 95% confidence interval of [26.8815, 32.7235] for the mean age. Repeating the whole study 2000 times, 96.4% of the intervals built this way contained the true population mean of 29.6991. Which statement do these results support?

A) There is a 95% probability that the true mean age lies inside [26.88, 32.72]  
B) Raising the level to 99% would narrow the interval, because greater confidence pins the true mean down more tightly  
C) The 95% is a hit rate of the procedure across repeated studies, not a probability attached to this interval  
D) About 95% of the 714 recorded passenger ages fall inside [26.88, 32.72], which is the quantity the level counts  

---

### Question 2

Breadth-first search keeps a frontier of nodes it has discovered but not yet expanded. What container does it use for that frontier, and why?

A) A stack, so the most recently discovered node is expanded first  
B) A queue, so the earliest discovered node is expanded first  
C) The visited set that records which nodes have been expanded already  
D) A priority queue ordered by f(n) = g(n) + h(n)  

---

### Question 3

A Bayesian calculation starts from a 1% chance that a patient has a disease and, after a positive test, prints 8.76%. Which number is the prior, and what does 'prior' mean?

A) 1% — the probability of the hypothesis before this evidence is taken into account  
B) 8.76% — the probability after the evidence has been taken into account  
C) Neither: the prior is the probability of the evidence itself, P(positive test)  
D) Neither: the prior is P(positive test | disease), the figure the test's manufacturer publishes  

---

### Question 4

A colour column holds red, green and blue. One encoding turns it into three 0/1 columns; another turns it into a single column holding 0, 1 and 2. Which is which?

A) Both are one-hot encoding, with different encoder settings  
B) The three-column result is label encoding; the single-column result is one-hot encoding, packed into one column  
C) Both are label encoding, since each maps the same three categories to numbers  
D) The three-column result is one-hot encoding; the single-column result is label encoding  

---

### Question 5

On an unweighted graph — one in which each edge costs the same — which search is guaranteed to return a path with the fewest edges?

A) Breadth-first search, because it finishes depth level d before opening depth level d+1  
B) Depth-first search, because it commits to one branch and stops as soon as the goal appears  
C) Whichever visits fewer nodes here, since less searching means a shorter path  
D) Dijkstra's algorithm; a fewest-edge guarantee needs edge weights and a priority queue  

---

### Question 6

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

### Question 7

A knowledge-based system stores what it knows separately from how it acts. What does its knowledge component consist of?

A) A relational database table with indexed columns and a query planner  
B) A labelled training dataset and a loss function  
C) A priority queue ordered by a heuristic function  
D) Rules, facts, and an inference mechanism that applies them  

---

### Question 8

Which expression is Bayes' theorem, and what does each factor do?

A) P(A | B) = P(B | A) . P(A) / P(B) — likelihood times prior, over the probability of the evidence  
B) P(A | B) = P(B | A) . P(B) / P(A) — the same three terms, with the prior and the evidence swapped  
C) P(A | B) = P(A) . P(B) — which holds when the two events are independent  
D) P(A | B) = P(A and B) / P(A) — the joint probability divided by the probability of A  

---

### Question 9

In the update `x <- x - lr * gradient`, what does `lr` control?

A) The number of iterations the loop will run before it stops  
B) The point the loop starts from, which fixes how close it begins to the minimum  
C) The threshold below which the gradient counts as zero and the loop terminates  
D) How far along the negative gradient the parameter moves at each step  

---

### Question 10

Three of these tasks are AI applications of the kind this course studies. Which one is not?

A) Flagging a card transaction as fraudulent from the pattern of a customer's past spending  
B) Forecasting tomorrow's rainfall from decades of recorded weather records  
C) Sorting a spreadsheet column alphabetically with a fixed comparison rule  
D) Reading a tumour boundary out of an MRI scan  

---

**End of quiz. Your instructor works the answers now.**
