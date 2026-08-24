# Quiz 01 – Unit 1: Introduction to NLP
## AIAT 121 - Natural Language Processing

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 1 (what NLP is, text cleaning and normalization, tokenization, stop-word removal, word-frequency analysis).  
**Concepts from:** Unit 1 example 01 (text preprocessing) and exercise 01 (cleaning social-media posts, minimal vs. aggressive pipelines).  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What is **tokenization** in NLP?

a) Removing stop words from a document  
b) Splitting text into smaller units such as words or sentences  
c) Converting all text to lowercase  
d) Encrypting text before sending it to a model  

---

### Question 2 (10 points)
You lowercase a paragraph and split it on whitespace, and your frequency table counts `language.` and `language` as **two different words**. Which preprocessing step fixes this?

a) Removing punctuation (normalization) before tokenizing and counting  
b) Removing stop words  
c) Splitting the text into sentences first  
d) Counting a larger corpus  

---

### Question 3 (10 points)
What are **stop words**, and why are they often removed before frequency analysis?

a) Words that end a sentence; removed to shorten documents  
b) Misspelled words; removed because models cannot process them  
c) Rare technical terms; removed because they inflate the vocabulary  
d) Very frequent function words (e.g. "the", "is", "and") that carry little topical content; removing them reduces noise in counting tasks  

---

### Question 4 (10 points)
Why do we usually **lowercase** text before counting word frequencies?

a) Models can only read lowercase letters  
b) It removes punctuation automatically  
c) So that "The" and "the" are normalized to the same token and counted once  
d) It removes stop words automatically  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write a preprocessing pipeline in plain Python (`re` and `string` modules — no NLP libraries) for messy social-media posts. Your code must:

1. Define `clean_text(text)` that removes URLs (`http...`), removes `@mentions`, drops the `#` symbol but **keeps** the hashtag word, and collapses extra whitespace.
2. Lowercase the cleaned text and remove punctuation (hint: `str.maketrans` with `string.punctuation`).
3. Tokenize by splitting on whitespace.
4. Remove stop words using the set `stop_words = {"the", "is", "a", "and", "this", "that", "with", "or", "but"}`.
5. Apply the pipeline to the post `"Just tried @QuickBites and WOW the delivery was so fast!! #foodie https://qb.example.com"` and print the final token list.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Define the **minimal** and **aggressive** preprocessing pipelines from the Unit 1 exercise (what steps does each include?), and explain the trade-off: what does aggressive cleaning gain, and what kind of signal can it destroy? Give one concrete example of a destroyed signal.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
What does a **word-frequency analysis** (e.g. `collections.Counter` plus a bar chart) tell you about a corpus, and why must cleaning and normalization happen **before** counting? Illustrate with what happens to a token like `(nlp)` or `language.` if you skip normalization.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
You are building a **sentiment analysis** system for customer posts about a delivery app. Would you feed the classifier the output of the *minimal* or the *aggressive* pipeline? Justify your choice, including what you would do about URLs, @mentions, and negation words like "not".

**Answer key:** released by your instructor.

---

**Mapping:** CLO1, CLO2; notebooks: `unit1-nlp-fundamentals/examples/01_text_preprocessing`, `unit1-nlp-fundamentals/exercises/01_text_preprocessing_exercise`.

**For:** AIAT 121 - Natural Language Processing
