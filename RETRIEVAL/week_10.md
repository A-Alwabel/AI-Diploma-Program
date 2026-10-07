# Retrieval Quiz — Week 10

**Week 10 of 35 · Course 04 — AIAT 114 (Machine Learning Algorithms and Applications)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Unit 2's 5-fold cross-validation of the murder-rate regression prints these fold scores:

```
Fold 1: R² = 0.1095
Fold 2: R² = 0.0616
Fold 3: R² = 0.0703
Fold 4: R² = 0.0999
Fold 5: R² = 0.0809

Mean R²: 0.0844
Std R²:  0.0179
```

A teammate wants the report to state **R² = 0.0616** - "the worst fold, so nobody can accuse us of picking a lucky split." Which response is right?

A) Quoting the worst fold is still quoting one draw; the honest figure is the pair 0.0844 ± 0.0179, which shows how far a single fold can land from the mean  
B) Agree: the lowest fold is the floor on what the model can do, so quoting it is the conservative choice and needs no spread beside it  
C) The spread comes from fold 5 holding out 398 rows instead of 399, so the fix is Leave-One-Out cross-validation, which gives each fold the same size before anything is reported  
D) A std of 0.0179 on a mean of 0.0844 means the model is too unstable to report; collect more features before quoting any R² to the client  

---

### Question 2

Unit 3's logistic-regression lesson sweeps the decision cut from 0.1 to 0.9 on its 3,200-row test set and prints:

```
Threshold    Accuracy     Precision    Recall       F1 Score
0.1          0.9975       0.4000       0.6667       0.5000
0.2          0.9984       0.5714       0.6667       0.6154
0.3          0.9981       0.5000       0.5000       0.5000
...
0.9          0.9981       0.5000       0.5000       0.5000
```

Precision and recall move by tens of points down the table; the accuracy column stays between 0.9975 and 0.9984. A student asks why accuracy looks "stuck". What is the correct explanation?

A) The model's predicted probabilities are nearly identical from row to row, so sliding the cut hardly changes any individual prediction  
B) Accuracy, like AUC, is defined over the whole range of thresholds at once, so a table that varies the cut is not something it is expected to respond to  
C) 3,194 of 3,200 rows are legitimate and cleared at almost any cut, so accuracy stays pinned near the baseline of calling each row legitimate, whatever the 6 fraud rows do  
D) A 3,200-row test set is simply too small for accuracy to resolve the differences between cuts; a larger test sample would separate the rows of the table cleanly and rank them  

---

### Question 3

Unit 1's regularization lesson predicts transaction `Amount` and prints a plain `LinearRegression` baseline of **MSE 4133.96**, then this part of the Lasso sweep:

```
Alpha   1.00: MSE = 4137.4229, R² = 0.8930, Features = 28/29
Alpha  10.00: MSE = 6043.0153, R² = 0.8437, Features = 14/29
Alpha 100.00: MSE = 36102.8517, R² = 0.0659, Features = 1/29
```

A teammate wants to report the α = 10 model: "it is the first setting where Lasso actually selects features, so the regularization is finally doing its job." Which reading of these rows is right?

A) Fourteen inputs at R² 0.8437 is the leaner model, and leaner is what regularization is for, so it should replace the 29-feature baseline in the report  
B) Each column Lasso switched off cost test error, which is what selection looks like when the baseline had no overfitting for a penalty to remove  
C) The grid is too coarse: an α between 1 and 10 would drop columns while holding the baseline's error, so refine the sweep before choosing  
D) Removing half the columns cures the multicollinearity among V1–V28, so the α = 10 coefficients are the trustworthy ones to publish  

---

### Question 4

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
B) The f(x) column read against a cut-off: 1.2884e-01 is below 1 and 2.2751e+05 is far above it, and a cost under 1 is the notebook's working test for having converged  
C) Which way |x| moved: 0.95 ends 0.3589 away, nearer than its start at 5.0, while 1.1 ends 476.9810 away — crossing while shrinking converges, crossing while growing diverges  
D) The 0.1 row: its 0.0189 is the one distance that has essentially reached zero, so a run still 0.3589 away after 25 steps has failed in the same way 1.1 did  

---

### Question 5

The Unit 3 diagnosis system was loaded with these printed symptom probabilities, among others:

```
  ➕ P(Fever|Flu) = 90.00%
  ➕ P(Cough|Flu) = 80.00%
  ➕ P(Fatigue|Flu) = 70.00%
  ➕ P(Fever|COVID-19) = 85.00%
  ➕ P(Cough|COVID-19) = 90.00%
  ➕ P(Fatigue|COVID-19) = 60.00%
```

For the patient with fever, cough and fatigue it printed `Flu: 58.91%` and `COVID-19: 21.46%`. Its slope-chart table shows the two likelihoods nearly tied — `P(symptoms|d)` of 50.4% for Flu against 45.9% for COVID-19 — with normalised priors of 22.7% and 9.1%. COVID-19 explains this patient almost as well as Flu does. Why does it end up with far less than half of Flu's posterior?

A) COVID-19's 2.0% prevalence is renormalised up to 9.1% over three diseases, and that renormalisation step is what costs it the ranking against Flu  
B) The likelihood gap does it: COVID-19's fatigue figure of 60.00% is the weakest entry, and 45.9% against 50.4% is what pulls its posterior down to 21.46%  
C) Normalising the three posteriors to sum to 100% hands the leader a share of the others' mass, which is what widens a near-tie into 58.91% against 21.46%  
D) With the likelihoods this close, the prior decides: Flu's normalised prior of 22.7% is more than twice COVID-19's 9.1%, and Bayes multiplies the two  

---

### Question 6

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

A) 0.30 — the highest cut-off whose misses stay within 5, bringing false alarms down to 12 at the price of 5 missed tumours rather than 1  
B) 0.10 — the one row that misses no malignant tumours, and a programme that fears misses should begin from zero of them and then work its way up  
C) 0.20 — it misses 1 and raises 21 false alarms, which satisfies the rule with a comfortable margin on the missed-tumour side  
D) 0.44 — the grid's best accuracy at 92.4%, and 8 misses is near enough to the rule for a figure the notebook itself singled out  

---

### Question 7

Unit 2 ran K-Means on 150 iris flowers with the species column hidden. The crosstab printed afterwards showed cluster 1 holding 50 setosa flowers and 0 of either other species. A classmate says: "a match that clean means K-Means obviously trained on the species labels." Which statement correctly describes what the clustering run was given?

A) It received the 4 measurements plus the species column, which is why cluster 1 lines up with setosa so exactly  
B) It received the 4 measurements per flower; the species column stayed hidden and was brought back afterwards to score the clusters  
C) It received the measurements and predicted a species category for each flower, so it was a classification model like the biopsy one  
D) It received the measurements and the labels but ignored them to finish faster, because fits without labels take fewer passes  

---

### Question 8

What are the components of a knowledge representation system, of the kind Course 01 built to answer questions about a family?

A) A relational database table with indexed columns holding the system's records  
B) A labelled training set and a loss function  
C) A priority queue ordered by a heuristic function estimating remaining cost  
D) Facts, rules, and an inference mechanism that derives new facts from them  

---

### Question 9

Course 01 ran BFS, DFS and A* on the same small graph. Which of these is guaranteed to return a shortest path on an unweighted graph, and why?

A) Depth-First Search, because it drives straight down one branch and reaches a goal without wandering over the frontier  
B) Breadth-First Search, because it expands the frontier one edge-layer at a time, so a goal is first met at its shallowest depth  
C) A* with a heuristic of your choosing, because ordering the frontier by estimated remaining cost settles path length  
D) Depth-First Search with a visited set, because marking visited nodes stops it from revisiting and so from lengthening the path it returns  

---

### Question 10

Before training anything, the single-neuron lesson printed this table:

```
     z |  sigmoid |    tanh |  relu
   1.0 |    0.731 |   0.762 |   1.0
   3.0 |    0.953 |   0.995 |   3.0
```

The training cell that followed compiled the neuron with `Adam(learning_rate=0.05)` and `loss="mse"`. A classmate files sigmoid, tanh and relu under "things that score the model". What job do the three functions in this table actually do inside a `Dense(1)` neuron?

A) They turn the weighted sum `z` into the neuron's output, which is why each column is a different reshaping of the same `z`  
B) They measure how far the neuron's output is from the 0/1 label, which is the scoring job that `mse` also performs in the compile line  
C) They decide how much each weight moves after a batch, which is why the learning rate 0.05 is set right beside them  
D) They switch random units off during training to limit overfitting, the way dropout does in a larger network  

---
