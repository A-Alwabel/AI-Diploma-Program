# Quiz 01: NLP Fundamentals | اختبار 1: أساسيات معالجة اللغة الطبيعية
## AIAT 121 - Unit 1

**Time Limit:** 45 minutes  
**Total Points:** 100 points

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What is the purpose of tokenization in NLP?

أ) Remove stop words  
ب) Split text into words or sentences  
ج) Convert to lowercase  
د) Remove punctuation

**Answer:** ب

---

### Question 2 (10 points)
Stemming and lemmatization both:

أ) Remove stop words  
ب) Reduce words to their root form  
ج) Remove punctuation  
د) Convert to lowercase

**Answer:** ب

---

## Part 2: Code Writing (30 points)

### Question 3 (30 points)
Write code to preprocess text: lowercase, remove punctuation, tokenize, and remove stop words.

**Answer Key:**
```python
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in tokens if w not in stop_words]
    return filtered
```

---

## Part 3: Short Answer (30 points)

### Question 4 (15 points)
Explain the difference between stemming and lemmatization.

**Answer Key:**
- Stemming: Removes suffixes/prefixes, may not result in valid words (faster, less accurate)
- Lemmatization: Returns root form that is a valid word (slower, more accurate)

---

**For:** AIAT 121 - Natural Language Processing

