# Cumulative Retrieval Quiz - Week 11

**Programme week 11 of 35 | Course 04 - AIAT 114 (Machine Learning Algorithms and Applications)**

Taught this week: Unit 3 (classification, session 41) and Unit 4 (clustering and PCA, sessions 42-44).

---

## How this works

- **15 minutes, in class, at the END of session 43.** You answer for about 7 minutes; your instructor then works the correct answers aloud for about 8.
- **This is not graded.** No mark from this paper reaches your course grade, and it carries no weight in any of the six assessment lines.
- **The correct answers are worked immediately afterwards, in the room.** That worked correction is the part that does the teaching; a quiz that only returns a score is worth about a third less.
- Ten questions. Three are on material from this week or last, three on material from about a month ago, and four on material from earlier in the programme. Each earlier question carries the context it needs, so you are not being asked to recall a lesson cold.
- Write one letter per question. No calculator, no laptop, no notes - answering from memory is the whole point.

---

### Question 1
*taught this week or last | Course 04, Unit 3*

Course 04 Unit 3's KNN lesson fits the same model twice on the same 313 real card transactions. Without scaling it scores accuracy 0.9048; with StandardScaler it scores 0.9683. The lesson also prints that the Time column alone contributes 99.9978% of the raw squared distance between two transactions (Time std 46,331.2, against a median feature std of 1.302). What does that 99.9978% figure explain?

A) Unscaled, 'nearest neighbour' means roughly 'happened at a similar moment', so what V1-V28 know is drowned out  
B) The V1-V28 columns barely vary across these rows, so they contribute almost nothing to the distances the model computes  
C) Time is the most predictive feature of fraud here, so scaling it down discards the best signal  
D) StandardScaler dropped Time from the feature set, and removing that one dominant column is what lifted accuracy by 6.35 points  

---

### Question 2
*taught this week or last | Course 04, Unit 4*

Course 04 Unit 4 clusters 1,994 communities on 4 scaled crime features and prints:

```
K=2   Inertia=5347.86   Silhouette=0.3967       K=6    Inertia=2398.46   Silhouette=0.2954
K=3   Inertia=4041.38   Silhouette=0.3134       K=8    Inertia=1970.75   Silhouette=0.3007
K=4   Inertia=3124.93   Silhouette=0.3153       K=10   Inertia=1720.82   Silhouette=0.2941
```

The elbow falls at K = 4; the silhouette peaks at K = 2; the lesson itself clusters at K = 3. How should K be settled?

A) Take K = 10: it posts the lowest inertia anywhere in the table, and lower inertia means tighter clusters  
B) Take K = 2: the silhouette is the score that measures separation, so it settles the question  
C) The disagreement is a symptom of unscaled features; rescaling the four crime columns would make the criteria converge  
D) The two criteria measure different things and disagree, so K is settled by what the clusters are for  

---

### Question 3
*taught this week or last | Course 04, Unit 3*

The same lesson refits the model with class_weight='balanced' and prints the change on the test set:

```
Fraud caught (TP):   3 -> 3       Fraud missed (FN):   3 -> 3
False alarms (FP):   3 -> 18      Legit cleared (TN):  3191 -> 3176
```

Precision 0.5000 -> 0.1429, recall 0.5000 -> 0.5000, accuracy 0.9981 -> 0.9934. What should the analyst conclude?

A) Recall did not move because the weighting was too weak; a larger manual weight on class 1 would lift it  
B) Precision falling from 0.50 to 0.14 is the signature of a model overfitting the minority class it was weighted towards  
C) The weighting bought 15 extra false alarms and no extra fraud: it moved the operating point, not the information  
D) Accuracy fell from 0.9981 to 0.9934, so the balanced model is the worse of the two and should be dropped  

---

### Question 4
*taught about a month ago | Course 03, Unit 1*

Course 03 computed the same two-layer transformation of the same data two ways: Route A as (X @ W1) @ W2, using 8,510,592 scalar multiplications, and Route B as X @ (W1 @ W2), using 1,191,040. The largest disagreement between the two outputs was 1.33e-14. What does this establish about a two-layer network with no activation function between the layers?

A) Route B is cheaper because it drops the hidden layer, so it returns an approximation rather than the exact output  
B) The 1.33e-14 disagreement shows the two routes compute different functions  
C) The two layers can be replaced by one layer with weight matrix W1 @ W2 without changing the function computed  
D) The second layer re-weights the first layer's outputs, so stacking the two adds expressive power a single layer lacks  

---

### Question 5
*taught about a month ago | Course 03, Unit 2*

Minimising f(x) = x^2 from x = 5 for 30 steps, Course 03 changed only the learning rate and printed: lr = 0.01 -> x = 2.72742; lr = 0.1 -> x = 0.0061897; lr = 0.9 -> x = 0.0061897; lr = 1.0 -> x = 5 with loss 25; lr = 1.1 -> x = 1186.88. On a log axis the lr = 0.9 loss curve lies exactly on top of the lr = 0.1 curve. What does that coincidence tell you?

A) lr = 0.9 takes smaller steps than lr = 0.1, which is why the two runs finish at the same value of x  
B) The loss depends only on |x|, so a smoothly falling curve can still hide a run that crosses the minimum each step  
C) A smoothly falling loss curve rules out instability, so the rate could safely be raised from 0.9 up to 1.0 for speed  
D) lr = 0.9 has settled into a second minimum of f that happens to sit at the same height as the first one  

---

### Question 6
*taught about a month ago | Course 02, Unit 5*

Course 02 classified points with k-nearest neighbours and varied k. What goes wrong when k is set too small - say k = 1?

A) The prediction rests on one neighbour, so a single mislabelled or unusual training point decides the answer  
B) The decision boundary is smoothed so heavily that the two classes stop being distinguishable  
C) Training slows down, because the model has to sort the full distance table before it reads off a label  
D) The model becomes more robust to noise, since consulting fewer neighbours means fewer chances to pick up a stray point  

---

### Question 7
*taught eight or more weeks ago | Course 01, Unit 1*

Course 01 opened by contrasting two ways of building an AI system. What is the main difference between traditional, rule-based AI and modern, data-driven AI?

A) Traditional AI uses neural networks, while modern AI works from hand-written rules  
B) Traditional AI hides its reasoning, while modern AI is transparent by construction  
C) Traditional AI applies rules written by a person; modern AI learns its rules from data  
D) Traditional AI runs faster, while modern AI is slower because it has to process far more data  

---

### Question 8
*taught eight or more weeks ago | Course 01, Unit 5*

A discriminative model learns P(Y | X) - the label given the input. What does a generative model learn instead?

A) P(Y) alone - the base rate of each class in the training set  
B) P(Y | X) as well, but estimated with a different optimiser and a larger training budget  
C) P(X) alone - the distribution of the inputs, with the class labels left out of the model  
D) P(X | Y) and P(Y) - the joint distribution over inputs and labels  

---

### Question 9
*taught eight or more weeks ago | Course 02, Unit 1*

Course 02 Unit 1 doubled the same numbers twice - once as a Python list comprehension, once as one NumPy whole-array operation - and printed:

```
         N    list (ms)   NumPy (ms)   speed-up
        10       0.0001       0.0003       0.5x
     1,000       0.0123       0.0006      21.5x
   100,000       1.2403       0.0254      48.8x
 1,000,000      15.1218       0.2454      61.6x
```

Which statement is supported by this table?

A) The list version scales better, because its cost per element falls as N grows  
B) NumPy's lead grows with N, and at N = 10 the list version is the faster of the two  
C) Both converge to the same speed at large N, since each loop is run by the interpreter  
D) NumPy runs about 100x faster here, the speed-up the notebook's own text quotes  

---

### Question 10
*taught eight or more weeks ago | Course 01, Unit 4*

Why does a feedforward network put an activation function between two dense layers?

A) To add a controlled amount of randomness, which keeps the network from settling too early  
B) To introduce non-linearity, without which stacked layers collapse into a single linear map  
C) To reduce memory use, because the activation discards values that the next layer will not read  
D) To speed up computation, since the activation replaces the layer's matrix product with a lookup  

---

**Answers: worked aloud by your instructor in the eight minutes after you hand this back. Nothing to submit, nothing to mark.**
