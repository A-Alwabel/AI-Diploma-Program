# Cumulative Retrieval Quiz — Week 23

**Programme week 23 of 35 · Current courses: Course 08 — AIAT 122 (Deep Learning), Unit 5 + wrap, and Course 09 — AIAT 123 (Reinforcement Learning), Unit 1**
**Placement: session 3 of the week (s91), in the closing block. Session 4 (s92) closes Course 09 Unit 1 with its unit quiz, so the block moves back to s91.**

- **15 minutes**, taken **in class at the END of the session**. Not homework.
- **Not graded.** No mark from this paper reaches your course grade.
- Write your answers, then your instructor **works every correct answer aloud immediately afterwards**. Stay for it.
- Ten items. Three from what you are studying now, seven from courses you finished earlier. The earlier items carry their own context.

---

### 1. [Course 08 · Unit 5]
A trained FP32 model is converted to INT8. The stored file falls from **5,597 to 4,557 bytes** and validation accuracy is unchanged at **0.840**. Which optimization technique is this, and what did it change?

A) Quantization — the number of **bits** used to store each weight value
B) Pruning — the number of **weights**, by zeroing the smallest
C) Distillation — the **architecture**, by training a smaller model to copy a larger one
D) ONNX export — the **file format**, so the model runs outside the framework that trained it

---

### 2. [Course 08 · Unit 4]
Course 08 Unit 4 trains a standard autoencoder and a variational autoencoder (VAE) on the same images. What does the VAE do that the plain autoencoder does not?

A) It compresses each input to a shorter code, which is what lets the decoder rebuild the image
B) It trains encoder and decoder as two networks competing against each other
C) It scores each input by how far its reconstruction sits from the original, and flags the gap
D) It encodes each input to a distribution and samples from that, so new points can be drawn

---

### 3. [Course 09 · Unit 1]
Unit 1's value-iteration lesson runs a 3x3 grid world with **-1 for every ordinary step, +10 for entering the goal, -10 for entering the pit, and gamma = 0.90**. It prints this converged value table and the greedy policy read off it:

```
State values:              Greedy policy:
  4.58   6.20   8.00         →   →   ↓
  6.20   8.00  10.00         →   →   ↓
  P     10.00   G            P   →   G
```

The tile immediately **above the pit** holds **6.20** — a positive value, even though one of its four actions steps straight into the -10 pit. Which explanation is correct?

A) The pit's -10 is discounted once per sweep, so by the time the table converges 0.90 raised to the sweep count has shrunk it below -1.
B) The sweep skips terminal states, so `transition(3, "down")` returns no pit transition, leaving the -10 out of that tile's backup.
C) The backup keeps the maximum over four actions, and the best moves right: -1 + 0.90 x 8.00 = 6.20, so the pit shows in the arrow.
D) The backup averages the four action targets instead of maximising, and the three non-pit actions outweigh the single -10.

---

### 4. [Course 07 · Unit 3]
You must extract PERSON, ORG and DATE mentions from 50,000 English news articles, on a CPU-only server, with **no labelled data**. Which tool from Course 07 does the job with the least work?

A) `TfidfVectorizer` with `MultinomialNB`, trained on the 50,000 articles
B) spaCy's `en_core_web_sm` pipeline, whose NER already tags these entity types
C) A local GPT-2 text-generation pipeline, prompted to list the entities in each article
D) `AutoModelForSequenceClassification` from Hugging Face, fine-tuned on the articles

---

### 5. [Course 07 · Unit 2]
Course 07 Unit 2 trained a small skip-gram model and then ranked words by cosine similarity between their vectors. Two word vectors score a cosine similarity close to **1.0**. What does that mean?

A) The two vectors point in nearly the same direction, so the model places the words in similar contexts
B) The two vectors are close to orthogonal, which is what a similarity value near 1.0 records for a pair of words
C) The two words appear side by side in the corpus, which is what cosine similarity counts
D) One vector is about twice the length of the other, since cosine similarity compares magnitudes

---

### 6. [Course 07 · Unit 3]
Which group lists three methods that can serve as the **classifier** in a text-classification pipeline?

A) TF-IDF, bag-of-words, Word2Vec
B) Tokenization, stemming and lemmatization
C) K-Means clustering, PCA, t-SNE
D) Naive Bayes, Logistic Regression, SVM

---

### 7. [Course 04 · Unit 3]
Course 04's logistic-regression lesson tested on 3,200 real transactions, 6 of them fraudulent, and printed:

```
[[3191    3]      TN = 3191    FP = 3
 [   3    3]]     FN = 3       TP = 3
```

Test accuracy **0.9981**. The same lesson printed that labelling every row "legitimate" scores **0.9981**. What do those two identical accuracies establish?

A) The classifier learned nothing from the 30 features, since it scores exactly what a model with no features scores
B) Accuracy is set by the 3,194 legitimate rows and has no room to register the 6 fraud rows either way
C) At 3,200 rows the test set is too small for accuracy to be reliable
D) The two agree because the cut sits at 0.5; moving that cut down to 0.3 would separate the model from the baseline

---

### 8. [Course 04 · Unit 3]
The same lesson refit the model with `class_weight='balanced'` and printed the change on the test set:

```
Fraud caught (TP):   3 -> 3       Fraud missed (FN):   3 -> 3
False alarms (FP):   3 -> 18      Legit cleared (TN):  3191 -> 3176
```

Precision 0.5000 → 0.1429, recall 0.5000 → 0.5000, accuracy 0.9981 → 0.9934. What should the analyst conclude?

A) Recall did not move because the weighting was too weak; a larger manual weight on class 1 would lift it above 0.50
B) Precision falling from 0.50 to 0.14 is the signature of a model overfitting the minority class
C) The weighting bought 15 extra false alarms and no extra fraud: it moved the operating point, not the information
D) Accuracy fell from 0.9981 to 0.9934, so the balanced model is the worse of the two and should be dropped

---

### 9. [Course 02 · Unit 2]
A triage knowledge base holds 4,000 recorded patient facts and 300 rules. A clinician needs one answer: *should Patient 7 be flagged for sepsis?* Which inference strategy fits this request, and why?

A) Backward chaining: it starts from this one goal and expands just the rules that bear on the case
B) Forward chaining: firing the rules in the order they were written is what makes a conclusion sound
C) Backward chaining: it can withdraw a conclusion when a later fact turns out to contradict it
D) Forward chaining: it derives the consequences of the 4,000 facts, and this answer is among them

---

### 10. [Course 01 · Unit 1]
Course 01 hand-wrote a weather agent as `if temperature > 25 and humidity < 60: ...`, which does no learning at all; a later lesson fitted a model from features `X` and labels `y`. What is the main difference between traditional (rule-based) AI and modern (data-driven) AI?

A) Traditional AI uses neural networks, modern AI uses rules
B) Traditional AI is opaque about its decisions, while modern AI is transparent by construction
C) Traditional AI uses explicit rules, modern AI learns from data
D) Traditional AI is faster, modern AI is slower

---

**End of paper. Hand nothing in. Stay for the worked answers.**
