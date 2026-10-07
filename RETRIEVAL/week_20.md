# Retrieval Quiz — Week 20

**Week 20 of 35 · Course 07 — AIAT 121 (Natural Language Processing)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Unit 4 then repeated the gradient measurement along an LSTM's memory lane and printed it beside the plain RNN:

```
distance k     plain RNN    LSTM b_f=1
        25      2.41e-15      1.84e-02
        50      7.33e-30      1.24e-04
```

At k = 50 the LSTM lane keeps about 2e+25 times more signal than the RNN, yet on the log plot its curve still slopes downward. Which conclusion does this table support?

A) Biasing the forget gate towards 1 has pushed the recurrent weights high enough for the gradient to explode instead — the mirror problem, which gradient clipping is there to handle  
B) A surviving signal of 1.24e-04 after 50 steps shows the long-range dependency is now learnable, so the vanishing gradient is a solved problem for LSTMs  
C) The lane slows the exponential decay of the backward signal but does not stop it; attention removes the distance, putting two far-apart words one step apart  
D) The LSTM's separate cell-state vector has room to store a 50-step sequence that the RNN's hidden state could not hold, which makes this a capacity fix  

---

### Question 2

The same Unit 4 probe scored *"The meeting is scheduled for Tuesday at 3pm"* **POSITIVE at 0.9301**, and the Arabic sentence glossed *"the meeting is Tuesday at 3"* at **P(POSITIVE) = 0.3695** after chopping it into **6.4** word-pieces per word. Same content, two very different scores — what explains the pair?

A) The model understood the English sentence as mildly positive and the Arabic one as close to neutral, so both numbers are fair readings of what the two sentences say  
B) The model is well calibrated: 0.9301 sits below the 0.9999 it gave a real opinion because a schedule is a weaker positive than praise  
C) The English fact had to leave through one of two exits, since there is no neutral class; the Arabic one was read letter by letter, so 0.3695 carries no information  
D) Both scores come from the lowercasing the `uncased` checkpoint applies; the `cased` checkpoint would read the capital letters and fix both  

---

### Question 3

In a Unit 5 bias audit you build pairs of test sentences that are identical except for one demographic word — *he* / *she*, or a male / female name — and compare the model's output on each pair. What does that test measure?

A) How large the model's vocabulary is, since each name has to be a known token already  
B) Whether the output moves when the demographic attribute alone is changed and the rest is held fixed  
C) How accurate the model is on the group each name belongs to, measured against held-out labels for that group  
D) How stable the model is under paraphrase, since the two sentences carry the same meaning  

---

### Question 4

The Unit 5 chunking lesson streamed the **14,015**-flow sample in **10 chunks of 1,500** rows (the last chunk held **515**) and printed a global mean of **6.84** forward packets per flow from a running total of **95,877** packets. A colleague wants two further figures from that same single pass: **(a)** the largest `Flow Duration` recorded for each `Label`, and **(b)** the quartiles of `Flow Duration` across the whole file. Which of the two can one chunked pass deliver exactly, and how?

A) (a) exactly, by keeping each label's largest value seen so far and updating it per chunk; (b) not from one pass, since quartiles are rank statistics that need the whole ordering, so use t-digest or a real engine  
B) (a) exactly, by keeping per-chunk maxima for each label; (b) exactly, by computing the quartiles of each chunk and weighting the ten results by chunk size so that the 515-row final chunk counts for less  
C) (a) approximately at best, because a rare label such as Heartbleed may fall inside a single chunk and its maximum is then compared against no other chunk; (b) exactly, by taking the quartiles of the per-chunk quartiles  
D) Neither exactly: an uneven final chunk of 515 rows breaks any statistic merged across chunks, so both need the file in memory at once, as the lesson's 1.3 MB measurement did  

---

### Question 5

Course 05 ends the data-science lifecycle with deployment and monitoring. What does deploying a model add, over and above having a trained model file on your laptop?

A) An assurance that the accuracy measured on the held-out split carries over to the incoming records  
B) A second training run on the full dataset, since the held-out split is no longer needed  
C) A record of the model's parameters, so the training run can be reproduced from the file alone  
D) A path by which new records reach the model and its predictions reach whatever consumes them  

---

### Question 6

The Unit 2 screening model was trained on `Pclass, Age, SibSp, Parch, Fare, Embarked`, with `Sex` deliberately left out. A reviewer writes: "since the model never received sex, its positive-prediction rates for women and men can differ only by chance." The lesson's threshold storyboard (same model, same test set, only the cut-off moves) prints:

```
 threshold   female rate     male rate   DP gap
      0.20         0.660         0.497    0.163
      0.65         0.309         0.222    0.087
```

How should you answer the reviewer?

A) The gaps are cut-off artefacts: moving the threshold from 0.20 to 0.65 shrinks the gap from 0.163 to 0.087, so with a sensible cut-off the model is gender-blind as the reviewer says  
B) The reviewer is right: on the same test set the TPR gap is 0.047 and the FPR gap 0.031, so a model that passes equalized odds cannot be carrying sex through proxies  
C) Unequal group sizes in the test set (97 women against 171 men) make different rates expected, so the gap is not evidence of proxies in the features  
D) The model's scores separate women from men through fare, class and family size, so the rates differ at any cut-off; dropping the column removed the label, not the information  

---

### Question 7

The statistical-measures lesson evaluates a linear model on held-out diabetes patients and prints MSE 2900.19, then notes in 'Where this breaks' that RMSE exceeds MAE by about 26%. Its diagnostic panel adds that 30 of the 89 patients are missed by more than 53.9 and that the worst single prediction is off by 154. A teammate proposes reporting MAE on its own because it 'looks better'. What does the 26% gap, read together with those two counts, tell you?

A) The model over-predicts by about a quarter on average, since RMSE exceeding MAE by 26% measures the direction of the typical miss  
B) RMSE has to be squared back to MSE 2900.19 before it can be set against MAE, because the 26% gap compares unlike units  
C) The 154 miss is one outlier; remove that patient and RMSE would fall back to MAE, because the whole gap comes from a single record  
D) Errors are unevenly spread: a minority of badly missed patients pulls RMSE up, so MAE alone would understate the worst cases  

---

### Question 8

Course 01's history lesson placed four landmarks on a timeline. Which one is normally taken as the birth of AI as a named research field?

A) Turing's 1950 paper, which proposed the imitation game as a test for machine thinking  
B) The 1956 Dartmouth summer workshop, where the term 'artificial intelligence' was adopted  
C) Deep Blue's 1997 match victory over the reigning world chess champion  
D) The 2022 public release of ChatGPT, which put a language model in front of the general public  

---

### Question 9

Course 03 Unit 5 works with both discrete and continuous distributions. What separates the two?

A) A discrete variable takes values that can be listed; a continuous one ranges over an interval  
B) A discrete variable is bounded above and below; a continuous one runs to infinity in both directions  
C) A discrete variable is one you counted from a sample; a continuous one is one you modelled  
D) A discrete variable comes from a finite dataset; a continuous one needs the whole population  

---

### Question 10

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
C) With the likelihoods this close, the prior decides: Flu's normalised prior of 22.7% is more than twice COVID-19's 9.1%, and Bayes multiplies the two  
D) Normalising the three posteriors to sum to 100% hands the leader a share of the others' mass, which is what widens a near-tie into 58.91% against 21.46%  

---
