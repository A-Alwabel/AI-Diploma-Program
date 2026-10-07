# Retrieval Quiz — Week 18

**Week 18 of 35 · Course 06 — AIAT 116 (Artificial Intelligence Ethics) and Course 07 — AIAT 121 (Natural Language Processing)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

A bank is placing two systems on the EU market: a **customer-service chatbot** that answers account questions, and a **credit-scoring model** that decides loan eligibility. The lesson's `classify_eu_risk()` returned a tier for each, and the chart under it counts obligations per tier as **0 → 2 → 9** from minimal to high risk. What follows for the two systems?

A) Both fall in limited risk: each system faces customers directly, so an Article 50 notice that an AI is involved discharges the bank's duties for the pair  
B) The credit scorer is prohibited under Article 5, since algorithmic decisions on access to loans sit beside social scoring, while the chatbot is minimal risk with no new obligations  
C) Both are high risk: a bank counts as critical infrastructure under the Act, so the 9 obligations attach to any AI system it deploys, the account-questions chatbot included  
D) The chatbot carries the 2 limited-risk duties (disclose the AI, label synthetic media); the credit scorer carries the 9 high-risk obligations, conformity assessment included  

---

### Question 2

Unit 1 also printed the pipeline as a step table:

```
stage                                   tokens  distinct types
3. stop-words removed                       21              21
4. punctuation stripped per token           21              19
```

Between steps 3 and 4 the token count holds at 21 while the number of distinct types drops by two. What happened at step 4?

A) Two tokens made of punctuation alone were deleted from the list, because stripping punctuation removes such tokens from a token sequence  
B) Two more words matched the nine-word stop list once their trailing punctuation no longer hid them from it  
C) Stripping the bracket and the full stop turned `(nlp)` and `language.` into `nlp` and `language`, which were already types  
D) Lowercasing merged `Natural` and `NLP` with their lower-case spellings, cutting the type count by two  

---

### Question 3

Course 07 Unit 2 split words into subword pieces rather than keeping a fixed word-level vocabulary. Why do BERT and GPT tokenizers work this way?

A) Subword pieces make the token sequence shorter, so a fixed context window can hold more of the document at once  
B) Subword pieces remove the need for training data, because the pieces carry their meaning on their own  
C) Subword pieces are language-independent, so one tokenizer costs the same number of tokens across languages  
D) A word missing from the vocabulary can still be spelled out of pieces the model knows, so new words survive  

---

### Question 4

You are reviewing a slide built from the Unit 3 best-practices lesson. Its bar chart of 2018 quarterly 911 dispatches shows a visible plunge in Q2, yet the check printed under the very same data reads: *"the whole year sits within 8.8% of its own mean"*. The data is the bundled 1-in-27 sample of the call log. How do you reconcile the chart with the printout, and what should the slide do?

A) The 8.8% is measured against the mean while the bars show raw counts, so the chart is right and the printout understates the swing; keep the bars as drawn and delete the sentence  
B) The 1-in-27 sampling inflates quarter-to-quarter variation in the counts, so the chart exaggerates; multiply each quarter by 27 before plotting so the bars settle  
C) The axis made the plunge, not the data: `set_ylim` starts just under the lowest quarter, so a year within 8.8% of its mean fills the frame; redraw from zero or flag the zoom  
D) Quarters differ in length by a few days, which the raw counts do not correct for; convert each bar to calls per day and the plunge will shrink to its true size  

---

### Question 5

You want to show whether a community's assault rate moves with its urban population share - two numeric columns, one row per community. Which chart does that job?

A) A bar chart, with one bar for each of the communities and its height set by that community's assault rate  
B) A scatter plot with urban share on one axis and assault rate on the other, a point per community  
C) A histogram of the assault rate, with the communities grouped into bins along the axis  
D) A pie chart, with each community taking a slice sized by its share of the total assaults  

---

### Question 6

Course 05 Unit 4 compared training and test scores for the same model. Which pattern is overfitting?

A) Training score low and test score low as well, because the model is too simple for the pattern in the data  
B) Training score high and test score much lower, because the model has learned the training rows themselves  
C) Training score low and test score high, because the test split happened to be the easier of the two  
D) Training score high and test score high, because the model has learned a pattern that generalises  

---

### Question 7

Course 01 implemented a perceptron from scratch before moving to Keras. What is a perceptron?

A) A layer of neurons whose outputs feed into a second layer before a prediction is produced  
B) A rule base whose conditions are learned from data rather than written by a person  
C) A single unit that takes a weighted sum of its inputs and passes it through a threshold  
D) A graph traversal that follows the highest-weight edge out of each node it reaches  

---

### Question 8

Course 01 closed by comparing the two families of model. What separates a generative model from a discriminative one?

A) A generative model learns how the data was produced and can emit a fresh sample; a discriminative model learns where the classes divide  
B) A generative model trains faster, because it is spared the work of separating the classes from one another  
C) A discriminative model reaches a higher score on held-out data whenever both are fitted well, which is why it is the default for a labelling task  
D) A generative model handles images while a discriminative model handles tables and text  

---

### Question 9

Course 04's fraud classifier printed TN 3191, FP 3, FN 3, TP 3 on a test set holding 6 frauds. What are the 3 false positives?

A) Transactions the model called fraud that were in fact legitimate - three false alarms sent to the fraud team  
B) Transactions the model called legitimate that were in fact fraud - three frauds that went through the system unflagged  
C) Transactions the model called fraud that were in fact fraud, which is the count the fraud team acts on  
D) Transactions the model called legitimate that were in fact legitimate, which is the bulk of the traffic  

---

### Question 10

Course 02 timed one removal from the front of a queue for two containers holding the same items:

```
 queue size    list.pop(0)   deque.popleft()   list costs
      1,000       0.0669 us          0.0236 us           3x
     32,000       1.7127 us          0.0246 us          69x
```

Why does BFS use `collections.deque` for its frontier rather than a plain list?

A) A list stores its items contiguously, so removing the front one shifts the rest, at a cost that grows with the queue  
B) A deque holds fewer bytes per item, so a long frontier stays inside cache while a list spills out of it  
C) A list would return the items in the wrong order, since popping index 0 takes the item added most recently  
D) A deque sorts its items as they arrive, so the shallowest node is already sitting at the front by the time BFS asks for it  

---
