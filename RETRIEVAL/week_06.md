# Cumulative Retrieval Quiz - Week 06

**Course 02 - AIAT 112, Unit 5**

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

   Best accuracy on this grid: 92.4% at threshold 0.44 - which still misses 8 malignant tumours.
```

A screening clinic can absorb at most 25 false alarms out of the 171, and within that limit wants to miss as few malignant tumours as it can. Which threshold does the table support, and at what cost?

A) 0.44 — it is the highest accuracy anywhere on the grid, 92.4%, and accuracy is the metric to maximise  
B) 0.50 — it is the library default, so it already balances the two kinds of error by construction  
C) 0.80 — it brings false alarms to zero, and 88.3% is near the grid maximum  
D) 0.20 — it misses 1 malignant tumour rather than 11, and its 21 false alarms fit the budget  

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
D) Dijkstra's algorithm; a fewest-edge guarantee needs edge weights and a priority queue  

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

What is the main difference between traditional rule-based AI and modern data-driven AI?

A) Traditional AI uses neural networks, modern AI uses rules  
B) Traditional AI hides its reasoning, while modern AI can be audited line by line  
C) Traditional AI uses explicit rules, modern AI learns from data  
D) Traditional AI is faster, modern AI is slower  

---

### Question 8

A bank wants two models: one that predicts whether an applicant will default, yes or no, and one that predicts the size of the loss in riyals. Which is which?

A) Default is classification because its target is a category; loss size is regression because its target is a number  
B) Default is regression because a probability is a number; loss size is classification because losses naturally fall into bands  
C) Both are classification, since the bank has to act on each prediction by approving or refusing  
D) Both are regression, since each model is fitted by minimising a squared error  

---

### Question 9

A feedforward network's hidden layer needs an activation function. Which list contains three activation functions and nothing else?

A) Adam, SGD, RMSprop  
B) MSE, cross-entropy, hinge  
C) Dropout, batch normalization, early stopping  
D) ReLU, sigmoid, tanh  

---

### Question 10

Course 01 introduces the perceptron before the first multi-layer network. What is a perceptron?

A) A single neuron: a weighted sum of the inputs, plus a bias, through a step function  
B) A rule of the form IF condition THEN conclusion, applied to facts by an inference engine  
C) A node-and-edge structure over which a search algorithm looks for a path  
D) A method for choosing which features to keep before a model is fitted  

---

**End of quiz. Your instructor works the answers now.**
