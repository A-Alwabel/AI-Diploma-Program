# Quiz 02 – Unit 2: Text Representation and Feature Engineering
## AIAT 121 - Natural Language Processing

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 2 (word/sentence/subword tokenization, morphology and stemming, Word2Vec skip-gram embeddings, cosine similarity, embedding visualization).  
**Concepts from:** Unit 2 examples 01 (advanced tokenization) and 02 (Word2Vec from scratch), and exercise 01 (multi-language text processing).  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
Why do modern models (BERT, GPT) use **subword tokenization** instead of a pure word-level vocabulary?

a) Subwords make the text shorter  
b) Words the model never saw can still be represented as known pieces (e.g. character n-grams or BPE units), so rare and new words are not lost  
c) Subwords remove the need for training data  
d) Word-level vocabularies are illegal in production systems  

---

### Question 2 (10 points)
The **distributional hypothesis** behind Word2Vec states that:

a) Words that appear in similar contexts tend to have similar meanings  
b) Longer documents contain more information  
c) Words are distributed uniformly across documents  
d) Every word must appear at least 5 times to be learned  

---

### Question 3 (10 points)
In the **skip-gram** architecture, what does the model learn to predict?

a) The sentiment of the sentence  
b) The next sentence in the document  
c) The part-of-speech tag of the center word  
d) The context words that appear near a given center word (within a small window)  

---

### Question 4 (10 points)
Two word vectors have **cosine similarity ≈ 1.0**. What does this mean?

a) The vectors are orthogonal (unrelated)  
b) The words never co-occur in the corpus  
c) The vectors point in nearly the same direction — the model treats the words as very similar  
d) One vector is exactly twice as long as the other  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
You are given a trained embedding matrix `embeddings` (NumPy array, shape `(V, 16)`: one 16-dimensional vector per word), a dict `word_to_id`, and a list `id_to_word`. Write a function `most_similar(word, k=3)` that:

1. Normalizes every embedding row to unit length (so dot products become cosine similarities).
2. Computes the cosine similarity between `word`'s vector and every other word's vector.
3. Returns the `k` most similar words (excluding the query word itself) with their similarity scores.

Use NumPy only (`np.linalg.norm`, matrix multiplication, `np.argsort`) — this is the same query the Unit 2 notebook implements and gensim provides as `most_similar`.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Compare **skip-gram** and **CBOW**: what does each one predict from what, and — per the Unit 2 material — which one is generally preferred for rare words / smaller corpora, and which is faster to train?

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
In the Unit 2 notebook, the model trained on the toy animal/technology corpus ends up with `cat`'s nearest neighbors being `bird`, `dog`, and `horse` (cosine ≈ 0.94–0.98) — yet **nobody ever labeled which words are animals**. Explain what training signal produced these clusters.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
Your team is building a support chatbot for a product with many **new technical terms and product names** that will not exist in any fixed word-level vocabulary. Which tokenization strategy do you choose and why? Illustrate your answer with the character 3-gram split of the word `processing` from the Unit 2 example.

**Answer key:** released by your instructor.

---

**Mapping:** CLO2, CLO5; notebooks: `unit2-tokenization-morphology/examples/01_advanced_tokenization`, `unit2-tokenization-morphology/examples/02_word_embeddings_word2vec`.

**For:** AIAT 121 - Natural Language Processing
