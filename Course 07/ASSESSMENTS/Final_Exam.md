# Final Exam: Natural Language Processing
## AIAT 121

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. Show your work for partial credit.

**Marking scheme:** Part 1 (Q1–Q6): 5 pts each = 30. Part 2 (Q7–Q9): 10 pts each = 30. Part 3 (Q10: 15 pts, Q11: 10 pts) = 25. Part 4 (Q12): 15 pts. **Total: 100.**

---

## Part 1: Multiple Choice (30 points)

Every option below is a claim someone could genuinely hold. Read all four before answering.

### Question 1 (5 points)
**CLO1:** What is the main goal of NLP?

A) Convert recorded speech into text so that audio can be archived and searched  
B) Index documents by keyword so that a search box can retrieve them  
C) Enable computers to understand, interpret and manipulate human language  
D) Hand-write a complete grammar of a language so nothing must be learned from text

---

### Question 2 (5 points)
**CLO2:** In Unit 1 a paragraph was split on whitespace and counted. The frequency table gave **every** word a count of 1 — even though *language* and *nlp* each occur **twice** in that paragraph. Which explanation is correct?

A) The stop-word list deleted one occurrence of each of those two words before they were counted  
B) `language.` and `(nlp)` remained separate tokens from `language` and `nlp`, splitting each count  
C) `Counter` records each distinct word just once per document, however often the word occurs  
D) Lowercasing merged the two occurrences of each word into one token before they were counted

---

### Question 3 (5 points)
**CLO3:** Which group lists three methods that can serve as the **classifier** in a text-classification pipeline?

A) TF-IDF, bag-of-words, Word2Vec  
B) Tokenization, stemming, lemmatization  
C) K-Means clustering, PCA, t-SNE  
D) Naive Bayes, Logistic Regression, SVM

---

### Question 4 (5 points)
**CLO4:** Unit 4 measured how much gradient signal survives travelling backwards through a plain RNN with typical weights: about 5×10⁻¹ after 1 step, 6×10⁻⁶ after 10 steps, and 7×10⁻³⁰ after 50 steps. Which conclusion does that measurement support?

A) The signal that would link far-apart words dies exponentially with distance; attention links any two positions in one step  
B) The recurrent weights grow exponentially during training, which is the problem transformers solve with gradient clipping  
C) The network's accuracy falls as sentences get longer, which is why transformers truncate their inputs to 512 tokens  
D) The hidden state vector is too short to hold a long sentence, which is why transformers use a much longer one

---

### Question 5 (5 points)
**CLO5:** You must extract PERSON, ORG and DATE mentions from 50,000 English news articles, on a CPU-only server, with **no labelled data**. Which tool from this course does the job with the least work?

A) `TfidfVectorizer` with `MultinomialNB`, trained on the 50,000 articles  
B) A local GPT-2 text-generation pipeline, prompted to list the entities in each article  
C) spaCy's `en_core_web_sm` pipeline, whose NER already tags these entity types  
D) `AutoModelForSequenceClassification` from Hugging Face, fine-tuned on the articles

---

### Question 6 (5 points)
**CLO6, CLO9:** In Unit 4 the pretrained English sentiment model labelled *"I have no opinion about this product"* **NEGATIVE at 0.9997**, and gave an Arabic sentence **P(POSITIVE) = 0.42** after splitting it into 5.5 word-pieces per word. What do these two results, read together, show?

A) The model has no neutral class, so it must pick a side; and 0.42 on Arabic means "nothing readable", not "unsure"  
B) The model is well calibrated: confident where the sentiment is clear, hesitant where it is genuinely ambiguous  
C) The Arabic sentence was correctly judged neutral, which shows the model handles other languages acceptably  
D) Both outputs are casing failures, and both disappear once the text is lowercased before it is scored

---

## Part 2: Short Answer Questions (30 points)

### Question 7 (10 points)
**CLO1, CLO2:** Unit 1 ran a four-step pipeline on one paragraph — whitespace tokenization, lowercasing, stop-word removal, punctuation stripping. Unit 2 then added a naive suffix-stripping stemmer that produced `jumped → jump` but also `running → runn`.

**(a) (4 pts)** State what each of the four Unit 1 steps does, and why it is in the pipeline.

**(b) (3 pts)** A **lemmatizer** uses a dictionary and returns a real word (`running → run`, `better → good`); the stemmer above only chops suffixes. Give one task where `runn` is harmless and one where it is damaging, and justify both.

**(c) (3 pts)** Name one step in this pipeline you would switch **off** before training a sentiment classifier, and state exactly what it would have destroyed.

---

### Question 8 (10 points)
**CLO4:** In Unit 4's worked example the pronoun *it* placed **43.3%** of its attention on *animal*, with no rule about pronouns anywhere in the code.

**(a) (6 pts)** Explain, step by step, how that 43.3% is produced — from the word vectors to the final output vector for *it*.

**(b) (2 pts)** During left-to-right generation the same pronoun gave *animal* **52.2%** at step 7, but **43.3%** in the finished 9-token sentence. Explain why the number moved, although nothing about the words changed.

**(c) (2 pts)** A stakeholder reads "43.3%" as proof that the model *decided* **it** means the animal. Give the strongest reason to be careful with that reading.

---

### Question 9 (10 points)
**CLO7:** Unit 5 trained a toy skip-gram on a corpus with a **known** gender skew, and the association measured back out of the vectors matched the skew written in (r = 0.99). Subtracting the gender direction from every profession vector then drove the audit score to exactly **0.000** for all five professions — yet k-means on those "neutralised" vectors still separated the male-skewed professions from the female-skewed ones.

**(a) (3 pts)** The training loop was never shown a gender label, a profession list, or the word "gender". Explain how the association got into the vectors.

**(b) (4 pts)** The audit score now reads 0.000. Explain why that is not evidence the bias is gone, and why a model that passes this test can be **worse** to deploy than one that fails it.

**(c) (3 pts)** Name three mitigation strategies from this course and say, for each, whether it would have caught this particular failure.

---

## Part 3: Practical/Coding Questions (25 points)

### Question 10 (15 points)
**CLO2, CLO3:** Write a complete sentiment-analysis pipeline in Python using this labelled dataset:

```python
docs = [
    "I love this product", "Excellent quality, amazing",
    "Wonderful, works great", "Best purchase ever",
    "Terrible quality", "Awful, broke immediately",
    "Very disappointing, bad", "Worst product, horrible",
]
labels = ["positive"] * 4 + ["negative"] * 4
```

Your code must:
1. Preprocess the text (lowercase, strip punctuation, tokenize, remove stop words)
2. Vectorize with **TF-IDF**
3. Train a classifier (Naive Bayes **or** Logistic Regression) on a training split
4. Evaluate on a held-out test split
5. Predict sentiment for these three new texts: `["I love this product!", "Terrible quality", "It's okay"]`

Then, in **two sentences**, state what the accuracy you printed is and is not evidence for.

---

### Question 11 (10 points)
**CLO5, CLO8:** Write code that loads a pre-trained BERT-family checkpoint from Hugging Face and **fine-tunes** it for binary sentiment classification (positive / negative) on a labelled dataset you already have as `dataset["train"]` and `dataset["test"]`.

Your answer must include: the checkpoint and its classification head, tokenization of the dataset, the training step, and evaluation. Then state **one** thing you would check before trusting the accuracy your fine-tuned model reports.

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
**CLO6, CLO9, CLO10:** Design an end-to-end NLP system for a customer-service chatbot serving a Saudi company. The chatbot must:

1. Process customer queries in **Arabic and English**
2. Classify intent (question, complaint, request)
3. Generate appropriate responses
4. Handle ethical considerations (bias, privacy)

Include:
- **Complete pipeline design**, from raw message to answer
- **Technology choices**, named from this course, with a reason for each
- **Evaluation strategy** — say what you would measure and on which data
- **Ethical safeguards**
- **Cost:** the vendor bills per token. Unit 2 measured the same sentence costing about 1.2 tokens per word in English and 5.5–6.1 tokens per word in Arabic with English-trained tokenizers. Say what that does to your budget and what you would do about it.

---

**End of Exam**

**Good Luck!**
