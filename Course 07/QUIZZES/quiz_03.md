# Quiz 03 – Unit 3: Machine Learning for NLP
## AIAT 121 - Natural Language Processing

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 3 (TF-IDF features, Naive Bayes and Logistic Regression text classifiers, evaluation and small-dataset pitfalls, spaCy NER and POS tagging).  
**Concepts from:** Unit 3 examples 01 (text classification) and 02 (named entity recognition), and exercise 01 (product-review sentiment analysis).  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
**TF-IDF** gives a word a high score in a document when the word is:

a) Frequent in every document  
b) Frequent in that document but rare across the whole collection of documents  
c) Rare everywhere, including that document  
d) A stop word  

---

### Question 2 (10 points)
Why do we evaluate a classifier on a **held-out test set** that it never saw during training?

a) To make training faster  
b) Because scikit-learn requires it  
c) So the reported accuracy measures generalization to new data, not memorization of the training data  
d) To increase the amount of training data  

---

### Question 3 (10 points)
In the Unit 3 experiment, the same pipeline trained on only **8 documents** (2 in the test set) produced accuracies of 100%, 100%, 100%, 0%, 0% across five random splits. What is the lesson?

a) With a tiny test set, a single accuracy number is mostly noise — prefer cross-validation and more data  
b) Accuracy above 50% is always meaningful  
c) The model was broken on splits 4 and 5  
d) Random seeds should always be set to 0  

---

### Question 4 (10 points)
In spaCy's NER output on the tech-companies paragraph, `Apple Inc.` is labeled **ORG** and `Cupertino` is labeled **GPE**. What does **GPE** stand for / denote?

a) General Purpose Entity — any noun  
b) Global Product Edition — a product name  
c) Grammatical Phrase Element — a syntax unit  
d) Geopolitical entity — countries, cities, states  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write a complete text-classification pipeline with scikit-learn:

1. Start from two lists: `docs` (strings) and `labels` (`"positive"`/`"negative"`).
2. Vectorize with `TfidfVectorizer` (fit on `docs`).
3. Split with `train_test_split` using `test_size=0.25`, `random_state=42`, and `stratify=labels` — say in a comment what `stratify` does.
4. Train a `MultinomialNB` classifier.
5. Print held-out accuracy, and predict the label of the new sentence `"An amazing, wonderful film"`.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Both Naive Bayes and Logistic Regression scored **100% accuracy** (held-out and 8-fold CV) on the 32-review dataset in Unit 3. Explain why this result should *not* impress you, and describe what a trustworthy evaluation of a sentiment classifier would look like.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Explain the difference between **Named Entity Recognition (NER)** and **Part-of-Speech (POS) tagging**: what does each one label, and give one practical application of each.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A client trained a sentiment model on **30 labeled reviews**, measured 100% accuracy on a held-out set of 8 reviews, and wants to deploy it to production tomorrow. Using what Unit 3 demonstrated (measured, not asserted), write your professional response: what is wrong with the evidence, and what evaluation plan do you propose before deployment?

**Answer key:** released by your instructor.

---

**Mapping:** CLO3, CLO5, CLO6; notebooks: `unit3-ml-for-nlp/examples/01_text_classification`, `unit3-ml-for-nlp/examples/02_named_entity_recognition`.

**For:** AIAT 121 - Natural Language Processing
