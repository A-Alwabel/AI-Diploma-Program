# Retrieval Quiz — Week 06

**Week 06 of 35 · Course 02 — AIAT 112 (Python for Artificial Intelligence)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Unit 5's threshold sweep — one logistic-regression model, its probability cut-off moved while nothing else changed, evaluated on 171 held-out biopsies — printed these rows (the four cut-offs above 0.50 miss 13 or more):

```
    threshold   missed malignant   false alarms   accuracy
         0.10                  0             38     77.8%
         0.20                  1             21     87.1%
         0.30                  5             12     90.1%
         0.40                  7              9     90.6%
         0.50                 11              5     90.6%

   Best accuracy on this grid: 92.4% at threshold 0.44 — which still misses 8 malignant tumours.
```

A regional programme builds its rule around the dangerous error instead: it will tolerate at most 5 missed malignant tumours among these 171, and inside that cap it wants the fewest false alarms it can get. Which row meets the rule at the lowest false-alarm count, and what is traded away to get there?

A) 0.10 — the one row that misses no malignant tumours, and a programme that fears misses should begin from zero of them and then work its way up  
B) 0.20 — it misses 1 and raises 21 false alarms, which satisfies the rule with a comfortable margin on the missed-tumour side  
C) 0.44 — the grid's best accuracy at 92.4%, and 8 misses is near enough to the rule for a figure the notebook itself singled out  
D) 0.30 — the highest cut-off whose misses stay within 5, bringing false alarms down to 12 at the price of 5 missed tumours rather than 1  

---

### Question 2

Which of these models can produce a new data point that was not in its training set?

A) Logistic regression, which fits a boundary and returns a class probability  
B) A generative adversarial network, whose generator is trained to produce samples  
C) A support vector machine, which places a boundary at the widest margin it can find  
D) A decision tree, which splits the feature space and labels each region  

---

### Question 3

On an unweighted graph — one in which each edge costs the same — which search is guaranteed to return a path with the fewest edges?

A) Breadth-first search, because it finishes depth level d before opening depth level d+1  
B) Depth-first search, because it commits to one branch and stops as soon as the goal appears  
C) Whichever visits fewer nodes here, since less searching means a shorter path  
D) Dijkstra's algorithm, since a fewest-edge result needs edge weights and a priority queue  

---

### Question 4

Five cross-validation folds of one Course 02 model on one dataset scored MSE 0.5230, 0.5746, 0.5755, 0.7748 and 0.8388 — the worst fold 60% worse than the best, with nothing changed but which rows were held out. What does that spread show cross-validation is for?

A) Reporting the fold with the lowest error as the model's performance  
B) Averaging away the luck of one train/test split, and showing how wide that luck runs  
C) Training the model on more data than a single split allows, which raises its accuracy  
D) Splitting the data once into a training set and a test set before the model is fitted  

---

### Question 5

What distinguishes a generative model from the classifiers studied earlier in Course 01?

A) It scores an input against a decision boundary it has fitted to labelled data  
B) It ranks training examples by how typical they are  
C) It draws new samples that resemble the data it was trained on  
D) It compresses the training set so that it can be stored and searched faster  

---

### Question 6

A discriminative classifier and a generative model are trained on the same labelled dataset. Which probability does the generative model learn?

A) P(Y | X) — the probability of the label given the features, which is what a fitted decision boundary encodes  
B) P(X) alone — how the features are distributed, with the labels discarded  
C) P(Y) alone — how often each label occurs in the training set  
D) P(X | Y) with P(Y) — how the features are distributed inside each class, and how common each class is  

---

### Question 7

The weather recommender in Course 01's first lesson printed two neighbouring cases:

```
26 °C, 59% humidity, morning -> Go for a jog in the park
26 °C, 61% humidity, morning -> Moderate weather, any outdoor activity is fine
```

A classmate concludes that the recommender "learned a humidity boundary near 60% from past weather data". Which statement describes where that boundary actually came from, and what it tells you about the system's family?

A) The 60% cut was fitted from the four printed test cases, which makes the recommender a small data-driven model of the kind Unit 2 trains  
B) The jump between 59% and 61% shows the system hides its reasoning, which is the mark of a modern learned model  
C) A person typed `humidity < 60` into an `if` statement, so the system is rule-based: the threshold was authored, not fitted to data  
D) The two answers differ because the hand-written rule evaluates faster than a fitted model would; speed is what separates the two families  

---

### Question 8

A bank wants two models: one that predicts whether an applicant will default, yes or no, and one that predicts the size of the loss in riyals. Which is which?

A) Default is classification because its target is a category; loss size is regression because its target is a number  
B) Default is regression because a probability is a number; loss size is classification because losses naturally fall into bands  
C) The two are classification, since the bank has to act on each prediction by approving or refusing  
D) The two are regression, since each model is fitted by minimising a squared error  

---

### Question 9

Before training anything, the single-neuron lesson printed this table:

```
     z |  sigmoid |    tanh |  relu
   1.0 |    0.731 |   0.762 |   1.0
   3.0 |    0.953 |   0.995 |   3.0
```

The training cell that followed compiled the neuron with `Adam(learning_rate=0.05)` and `loss="mse"`. A classmate files sigmoid, tanh and relu under "things that score the model". What job do the three functions in this table actually do inside a `Dense(1)` neuron?

A) They measure how far the neuron's output is from the 0/1 label, which is the scoring job that `mse` also performs in the compile line  
B) They decide how much each weight moves after a batch, which is why the learning rate 0.05 is set right beside them  
C) They switch random units off during training to limit overfitting, the way dropout does in a larger network  
D) They turn the weighted sum `z` into the neuron's output, which is why each column is a different reshaping of the same `z`  

---

### Question 10

Course 01 introduces the perceptron before the first multi-layer network. What is a perceptron?

A) A single neuron: a weighted sum of the inputs, plus a bias, through a step function  
B) A rule of the form IF condition THEN conclusion, applied to facts by an inference engine  
C) A node-and-edge structure over which a search algorithm looks for a path  
D) A method for choosing which features to keep before a model is fitted  

---
