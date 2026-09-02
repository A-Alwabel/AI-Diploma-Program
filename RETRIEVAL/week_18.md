# Cumulative Retrieval Quiz - Week 18

**Programme week 18 of 35 | Course 06 - AIAT 116 closes (session 70) and Course 07 - AIAT 121 (NLP) opens**

Taught this week: Course 06 Unit 5 (session 69), the Course 06 wrap (session 70), Course 07 Unit 1 (session 71) and Course 07 Unit 2 (session 72).

---

## How this works

- **15 minutes, in class, at the END of session 72.** You answer for about 7 minutes; your instructor then works the correct answers aloud for about 8.
- **This is not graded.** No mark from this paper reaches your course grade, and it carries no weight in any of the six assessment lines.
- **The correct answers are worked immediately afterwards, in the room.** That worked correction is the part that does the teaching; a quiz that only returns a score is worth about a third less.
- Ten questions. Three are on material from this week or last, three on material from about a month ago, and four on material from earlier in the programme. Each earlier question carries the context it needs, so you are not being asked to recall a lesson cold.
- Write one letter per question. No calculator, no laptop, no notes - answering from memory is the whole point.

---

### Question 1
*taught this week or last | Course 06, Unit 5*

Your company is placing a CV-screening model that ranks job applicants on the EU market. Under the EU AI Act risk tiers taught in Course 06 Unit 5, what follows?

A) Limited risk: the duty is a transparency notice telling applicants that an AI system is involved in the screening  
B) Prohibited: the Act lists automated decision-making about employment among its Article 5 banned practices  
C) Minimal risk: the system produces a ranking and a human recruiter still takes the final hiring decision  
D) High risk: data governance, logging, human oversight and a conformity assessment apply before deployment  

---

### Question 2
*taught this week or last | Course 07, Unit 1*

In Course 07 Unit 1 a paragraph was split on whitespace and counted. The frequency table gave every word a count of 1 - even though language and nlp each occur twice in that paragraph. Which explanation is correct?

A) The stop-word list deleted one of the two occurrences of each of those words before they were counted  
B) 'language.' and '(nlp)' remained separate tokens from 'language' and 'nlp', splitting each count  
C) Counter records each distinct word just once per document, however often the word occurs  
D) Lowercasing merged the two occurrences of each word into one token before they were counted  

---

### Question 3
*taught this week or last | Course 07, Unit 2*

Course 07 Unit 2 split words into subword pieces rather than keeping a fixed word-level vocabulary. Why do BERT and GPT tokenizers work this way?

A) Subword pieces make the token sequence shorter, so a fixed context window can hold more of the document at once  
B) Subword pieces remove the need for training data, because the pieces carry their meaning on their own  
C) Subword pieces are language-independent, so one tokenizer costs the same number of tokens across languages  
D) A word missing from the vocabulary can still be spelled out of pieces the model knows, so new words survive  

---

### Question 4
*taught about a month ago | Course 05, Unit 3*

A colleague's bar chart of 2018 quarterly 911 call volume shows Q2 as a collapse and Q4 as a full recovery. The counts behind it are Q1 1,478, Q2 1,352, Q3 1,402, Q4 1,478 - a change of +0.00% across the year. No number was altered between the data and the chart. What produced the misleading chart, and what is the fix?

A) The bars were sorted by value rather than by quarter; re-order them chronologically so the trend reads correctly  
B) Counts were plotted where percentages were needed; convert each quarter to a percentage change from Q1  
C) The y-axis was truncated to start just below the smallest bar; start it at zero, or flag the zoom  
D) Four categories are too few for bars; a pie chart would show the quarters' shares more fairly  

---

### Question 5
*taught about a month ago | Course 05, Unit 3*

You want to show whether a community's assault rate moves with its urban population share - two numeric columns, one row per community. Which chart does that job?

A) A bar chart, with one bar for each of the communities and its height set by that community's assault rate  
B) A scatter plot with urban share on one axis and assault rate on the other, a point per community  
C) A histogram of the assault rate, with the communities grouped into bins along the axis  
D) A pie chart, with each community taking a slice sized by its share of the total assaults  

---

### Question 6
*taught about a month ago | Course 05, Unit 4*

Course 05 Unit 4 compared training and test scores for the same model. Which pattern is overfitting?

A) Training score low and test score low as well, because the model is too simple for the pattern in the data  
B) Training score high and test score much lower, because the model has learned the training rows themselves  
C) Training score low and test score high, because the test split happened to be the easier of the two  
D) Training score high and test score high, because the model has learned a pattern that generalises  

---

### Question 7
*taught eight or more weeks ago | Course 01, Unit 4*

Course 01 implemented a perceptron from scratch before moving to Keras. What is a perceptron?

A) A layer of neurons whose outputs feed into a second layer before a prediction is produced  
B) A rule base whose conditions are learned from data rather than written by a person  
C) A single unit that takes a weighted sum of its inputs and passes it through a threshold  
D) A graph traversal that follows the highest-weight edge out of each node it reaches  

---

### Question 8
*taught eight or more weeks ago | Course 01, Unit 5*

Course 01 closed by comparing the two families of model. What separates a generative model from a discriminative one?

A) A generative model learns how the data was produced and can emit a fresh sample; a discriminative model learns where the classes divide  
B) A generative model trains faster, because it is spared the work of separating the classes from one another  
C) A discriminative model reaches a higher score on held-out data whenever both are fitted well, which is why it is the default for a labelling task  
D) A generative model handles images while a discriminative model handles tables and text  

---

### Question 9
*taught eight or more weeks ago | Course 04, Unit 3*

Course 04's fraud classifier printed TN 3191, FP 3, FN 3, TP 3 on a test set holding 6 frauds. What are the 3 false positives?

A) Transactions the model called fraud that were in fact legitimate - three false alarms sent to the fraud team  
B) Transactions the model called legitimate that were in fact fraud - three frauds that went through the system unflagged  
C) Transactions the model called fraud that were in fact fraud, which is the count the fraud team acts on  
D) Transactions the model called legitimate that were in fact legitimate, which is the bulk of the traffic  

---

### Question 10
*taught eight or more weeks ago | Course 02, Unit 1*

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

**Answers: worked aloud by your instructor in the eight minutes after you hand this back. Nothing to submit, nothing to mark.**
