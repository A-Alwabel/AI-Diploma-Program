# Retrieval Quiz — Week 23

**Week 23 of 35 · Course 08 — AIAT 122 (Deep Learning) and Course 09 — AIAT 123 (Reinforcement Learning)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

In the lesson's worked example, a trained digits classifier is converted with a single library call and no retraining. Measured on the same laptop CPU: stored size **70.2 KB → 22.2 KB** (**3.2×** smaller), accuracy **96.7%** before and after, and latency **0.228 → 0.360 ms/batch** — the converted model runs **1.6×** slower. Name the technique and the property of the model it modified.

A) Pruning — the number of surviving weights, with the smallest ones zeroed out so the file has fewer values to hold  
B) Quantization — the precision each weight is stored at, FP32 down to INT8, with a scale and zero-point kept per layer  
C) Distillation — the architecture, with a smaller student trained to match the 96.7% teacher's soft outputs  
D) ONNX export — the file format, so the model runs outside PyTorch, which is also why inference got slower in the new runtime  

---

### Question 2

Course 08 Unit 4 trains a standard autoencoder and a variational autoencoder (VAE) on the same images. What does the VAE do that the plain autoencoder does not?

A) It compresses each input to a shorter code, which is what lets the decoder rebuild the image  
B) It trains encoder and decoder as two networks competing against each other  
C) It scores each input by how far its reconstruction sits from the original, and flags the gap  
D) It encodes each input to a distribution and samples from that, so new points can be drawn  

---

### Question 3

Unit 1's value-iteration notebook reports that its 3x3 grid world (gamma = 0.90; -1 for an ordinary step, +10 for entering the goal, -10 for entering the pit) **converged in 5 sweeps**, printing:

```
State values:              Greedy policy:
  4.58   6.20   8.00         →   →   ↓
  6.20   8.00  10.00         →   →   ↓
  P     10.00   G            P   →   G
```

Look at the **bottom-row tile between the pit and the goal**. It reads **10.00** — as much as the goal reward itself, and more than the 8.00 in the top-right corner — although stepping left from it lands in the -10 pit. A classmate concludes the pit must have been left out of that tile's backup. What actually happened in the code?

A) The -10 is multiplied by gamma = 0.90 once per sweep, so by the time the 5 sweeps are over it has shrunk too far to pull the tile below the 10.00 that the goal side offers.  
B) The pit is in `TERMINAL_STATES`, so the sweep's `continue` skips it and `transition(7, 'left')` therefore returns no -10 for this tile's backup.  
C) Four targets were computed and the largest kept: stepping right enters the goal for +10 with no future to discount, so 10.00 wins and the -10 target loses the comparison.  
D) The four targets are averaged rather than maximised, and the right-hand move into the goal lifts the mean far enough to cancel the single -10 that the pit contributes.  

---

### Question 4

An investigative newsroom has inherited an English-language document leak of the kind that opened Unit 3. No file has been annotated, the only machine is a laptop, and the editors want, for each file, the people, companies and dates it names. Which approach from this course gets there with the least work?

A) Vectorise the files with TF-IDF and fit `MultinomialNB`, treating each file as one document to be labelled  
B) Prompt the local GPT-2 text-generation pipeline from Unit 4 to write out the names it notices in each file  
C) Fine-tune `AutoModelForSequenceClassification` from Hugging Face on the leaked files so that it learns the newsroom's own entity types  
D) Run `en_core_web_sm` over each file and read `doc.ents`, the pretrained NER that tagged 12 spans in the sample paragraph  

---

### Question 5

Course 07 Unit 2 trained a small skip-gram model and then ranked words by cosine similarity between their vectors. Two word vectors score a cosine similarity close to **1.0**. What does that mean?

A) The two vectors point in nearly the same direction, so the model places the words in similar contexts  
B) The two vectors are close to orthogonal, which is what a similarity value near 1.0 records for a pair of words  
C) The two words appear side by side in the corpus, which is what cosine similarity counts  
D) One vector is about twice the length of the other, since cosine similarity compares magnitudes  

---

### Question 6

Unit 3's pipeline was `TfidfVectorizer(stop_words="english")` feeding `MultinomialNB()`. A teammate wants to replace the second stage and still get a *positive* or *negative* label for each of the 1,000 held-out reviews. Which replacement still does that job?

A) A Porter stemmer applied to each review before its text reaches the TF-IDF vectorizer  
B) `LogisticRegression(max_iter=1000)`, fitted on the same 3,000 TF-IDF rows and their labels  
C) A second `TfidfVectorizer` with a larger vocabulary, run on the output of the first one  
D) K-Means with two clusters, fitted on the same TF-IDF rows without ever looking at the review labels  

---

### Question 7

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

### Question 8

The same lesson prints two different ways of pushing the fraud model to flag more of the 3,200 test transactions - lowering the cut on the original model, and refitting with `class_weight='balanced'`:

```
cut 0.1 (original model):   caught 4   missed 2   false alarms 6    recall 0.6667   precision 0.4000
class_weight='balanced':    caught 3   missed 3   false alarms 18   recall 0.5000   precision 0.1429
```

A colleague reads the second line and concludes that the weighted refit is "the more aggressive model, so it must be the one catching more fraud." What do the two lines establish?

A) Flagging more is not finding more: 18 alarms bought 3 frauds where 6 alarms bought 4, so the weighting moved the operating point without adding signal  
B) Recall sat at 0.5000 because 'balanced' is a mild preset; a hand-set weight on class 1 would carry recall past the 0.6667 the lower cut reached  
C) The precision collapse to 0.1429 is the minority class being overfitted by the refit, which the threshold change avoids because the fitted model is left untouched  
D) Both rows fall below the 0.9981 that labelling each row legitimate scores, so the default 0.5 cut, which matches it, remains the model to keep  

---

### Question 9

In the Unit 2 expert-system cell, three recorded observations about `Patient1` and two rules went in, and the run printed:

```
   BEFORE Forward Chaining:
      Facts: 3

  ➕ Added: Fact(Patient1, likely_has, Flu)
   ✅ Applied rule: Flu Diagnosis Rule
  ➕ Added: Fact(Patient1, recommend, Rest)
   ✅ Applied rule: Flu Treatment Rule

✅ Forward chaining complete! (2 iterations)
   (Stopped because no more new facts can be derived)

   AFTER Forward Chaining:
      Facts: 5
```

A clinic now wants the system to run with no particular question in mind: *each time a nurse records a new observation, surface whatever recommendations now follow for that patient.* Which chaining direction suits that job, and what in the printout shows why?

A) Forward chaining: data-driven, firing whichever rules the recorded facts satisfy until a pass adds no new fact — the loop that stopped above after 2 iterations  
B) Forward chaining: the Flu Diagnosis Rule was entered before the Flu Treatment Rule, and firing rules in the order they were written is what keeps the chain valid  
C) Backward chaining: it would prove `recommend Rest` for one patient at a time, and a focused proof costs less than deriving facts even when no goal has been named  
D) Backward chaining: if a later observation contradicts `likely_has Flu`, it can take back the `Rest` recommendation, which a forward chainer has no way to do  

---

### Question 10

The weather recommender in Course 01's first lesson printed two neighbouring cases:

```
26 °C, 59% humidity, morning -> Go for a jog in the park
26 °C, 61% humidity, morning -> Moderate weather, any outdoor activity is fine
```

A classmate concludes that the recommender "learned a humidity boundary near 60% from past weather data". Which statement describes where that boundary actually came from, and what it tells you about the system's family?

A) The 60% cut was fitted from the four printed test cases, which makes the recommender a small data-driven model of the kind Unit 2 trains  
B) A person typed `humidity < 60` into an `if` statement, so the system is rule-based: the threshold was authored, not fitted to data  
C) The jump between 59% and 61% shows the system hides its reasoning, which is the mark of a modern learned model  
D) The two answers differ because the hand-written rule evaluates faster than a fitted model would; speed is what separates the two families  

---
