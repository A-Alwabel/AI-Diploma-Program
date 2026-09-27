# Retrieval Quiz — Week 20

**Week 20 of 35 · Course 07 — AIAT 121 (Natural Language Processing)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

Unit 4 measured how much gradient signal survives travelling backwards through a plain RNN with typical weights: about 5×10⁻¹ after 1 step, 6×10⁻⁶ after 10 steps, and 7×10⁻³⁰ after 50 steps. Which conclusion does that measurement support?

A) The signal that would link far-apart words dies exponentially with distance; attention links two distant positions in one step  
B) The recurrent weights grow exponentially during training, which is the problem that transformers solve by clipping the gradient  
C) The network's accuracy falls as sentences get longer, which is why transformers truncate their inputs to 512 tokens  
D) The hidden state vector is too short to hold a long sentence, which is why transformers use a much longer one  

---

### Question 2

In Unit 4 the pretrained English sentiment model labelled *"I have no opinion about this product"* **NEGATIVE at 0.9997**, and gave an Arabic sentence **P(POSITIVE) = 0.42** after splitting it into 5.5 word-pieces per word. What do these two results, read together, show?

A) The model has no neutral class, so it picks a side either way; and 0.42 on Arabic means "nothing readable", not "unsure"  
B) The model is well calibrated: it is confident where the sentiment is clear, and hesitant where the sentiment is genuinely ambiguous  
C) The Arabic sentence was correctly judged neutral, which shows the model handles other languages acceptably  
D) The two outputs are casing failures, and each disappears once the text is lowercased before it is scored  

---

### Question 3

In a Unit 5 bias audit you build pairs of test sentences that are identical except for one demographic word — *he* / *she*, or a male / female name — and compare the model's output on each pair. What does that test measure?

A) How large the model's vocabulary is, since each name has to be a known token already  
B) Whether the output moves when the demographic attribute alone is changed and the rest is held fixed  
C) How accurate the model is on the group each name belongs to, measured against held-out labels for that group  
D) How stable the model is under paraphrase, since the two sentences carry the same meaning  

---

### Question 4

You must compute two figures from a 40 GB `sales.csv` on a laptop with 16 GB of RAM, using `pd.read_csv(..., chunksize=...)`: **(i)** the mean `amount` per `category`, and **(ii)** the median `amount` over the whole file. Which statement correctly describes what one chunked pass can give you, and how?

A) (i) exactly, by carrying a running sum and a running count per category; (ii) exactly, by taking one median per chunk and averaging those medians in proportion to the number of rows in each chunk  
B) (i) exactly, by averaging the per-chunk category means at the end; (ii) exactly, because the median of the per-chunk medians is the median of the whole file  
C) (i) exactly, by carrying a running sum and a running count per category; (ii) not from one chunked pass — a median needs all the values at once, so it takes an approximation or another engine  
D) (i) and (ii) approximately at best: combining results across chunks assumes the chunks hold equal numbers of rows, and here the last chunk holds fewer rows than the ones before it  

---

### Question 5

Course 05 ends the data-science lifecycle with deployment and monitoring. What does deploying a model add, over and above having a trained model file on your laptop?

A) An assurance that the accuracy measured on the held-out split carries over to the incoming records  
B) A second training run on the full dataset, since the held-out split is no longer needed  
C) A record of the model's parameters, so the training run can be reproduced from the file alone  
D) A path by which new records reach the model and its predictions reach whatever consumes them  

---

### Question 6

A Course 06 team removed the `Sex` column from a screening model's training data and reported that the system was now fair. On the held-out set the model's positive-prediction rate was **44.3% for women and 31.6% for men** — a demographic parity difference of **0.128**. What does this result show?

A) Removing `Sex` made the model blind to gender, so the remaining gap is not something the model itself produced  
B) Demographic parity is the wrong test here: on the same held-out set the equalized-odds gaps are small (TPR gap 0.047)  
C) The model rebuilt the group split from correlated features like fare and class, so deleting the column changed nothing  
D) The model satisfies demographic parity, since two applicants with identical inputs receive an identical decision from it  

---

### Question 7

On 89 held-out diabetes patients, Course 03 Unit 3 printed MAE 42.79, RMSE 53.85, and a mean signed error of −3.91, and reported that the 10 worst-predicted patients carry 44.3% of the total squared error. What does the gap between MAE and RMSE tell you about this model?

A) The model over-predicts by roughly 11 units on each patient, which is what the gap between the two metrics measures  
B) The model accounts for 53.85% of the variation in the targets, which is the quantity a root-mean-squared error reports  
C) RMSE and MAE are on different scales, so RMSE has to be squared before the two numbers can be compared  
D) A small group of large errors inflates RMSE, so the typical patient is missed by about 43 rather than 54  

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

Course 02's Unit 3 diagnosis system was given a patient with fever, cough and fatigue, and printed:

```
disease         prevalence  prior (norm.)  P(symptoms|d)   posterior   rank move
Common Cold         15.0%          68.2%           5.6%       19.6%       1 → 3
Flu                  5.0%          22.7%          50.4%       58.9%       2 → 1
COVID-19             2.0%           9.1%          45.9%       21.5%       3 → 2
```

Common Cold is by far the most prevalent of the three diseases, yet it finishes last. Why?

A) Renormalising the three prevalences over one another pushes the largest of them below the rest  
B) Common Cold has no listed probability for fatigue, so the system skips it in the product  
C) Bayes multiplies prior by likelihood, and P(symptoms | Cold) = 5.6% is nine times below Flu's  
D) The posterior follows the highest single symptom probability, and Flu's fever figure is 90%  

---
