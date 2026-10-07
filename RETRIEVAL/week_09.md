# Retrieval Quiz — Week 09

**Week 09 of 35 · Course 03 — AIAT 113 (Mathematics and Probability for Machine Learning) and Course 04 — AIAT 114 (Machine Learning Algorithms and Applications)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

From the same sample of 100 recorded Titanic ages, the confidence-interval lesson prints a 90% interval of [27.3582, 32.2468] (width 4.8886) and a 99% interval of [25.9361, 33.6689] (width 7.7327). When it redoes the whole study 2000 times, 92.5% of the 90% intervals and 99.6% of the 99% intervals capture the population mean, and in the panel that draws 100 of those repeats, 3 intervals are shown in crimson. A student writes: 'There is a 99% chance the true mean age is between 25.9361 and 33.6689.' Which statement about that sentence is right?

A) Acceptable: 99.6% of the 2000 repeated intervals held the mean, so roughly 99% is also the right probability for this one  
B) Wrong: the level counts recorded ages, so the sentence should say that 99% of the 714 ages lie between 25.9361 and 33.6689  
C) Wrong: the 99% is the capture rate of the procedure across repeats — measured here as 99.6% — not the odds for this one interval  
D) Acceptable, and understated: the wider 99% interval (7.7327 against 4.8886) carries more knowledge about the mean, which is why its coverage rose to 99.6%  

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
C) A third number: the prior is the probability of the evidence itself, P(positive test)  
D) A third number: the prior is P(positive test | disease), the figure the test's manufacturer publishes  

---

### Question 4

A colour column holds red, green and blue. One encoding turns it into three 0/1 columns; another turns it into a single column holding 0, 1 and 2. Which is which?

A) The two are one-hot encoding, produced with different encoder settings  
B) The three-column result is label encoding; the single-column result is one-hot encoding, packed into one column  
C) The two are label encoding, since each maps the same three categories to numbers  
D) The three-column result is one-hot encoding; the single-column result is label encoding  

---

### Question 5

On an unweighted graph — one in which each edge costs the same — which search is guaranteed to return a path with the fewest edges?

A) Breadth-first search, because it finishes depth level d before opening depth level d+1  
B) Depth-first search, because it commits to one branch and stops as soon as the goal appears  
C) Whichever visits fewer nodes here, since less searching means a shorter path  
D) Dijkstra's algorithm, since a fewest-edge result needs edge weights and a priority queue  

---

### Question 6

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
B) Which way |x| moved: 0.95 ends 0.3589 away, nearer than its start at 5.0, while 1.1 ends 476.9810 away — crossing while shrinking converges, crossing while growing diverges  
C) The f(x) column read against a cut-off: 1.2884e-01 is below 1 and 2.2751e+05 is far above it, and a cost under 1 is the notebook's working test for having converged  
D) The 0.1 row: its 0.0189 is the one distance that has essentially reached zero, so a run still 0.3589 away after 25 steps has failed in the same way 1.1 did  

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
