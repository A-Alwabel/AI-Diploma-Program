# Unit 2: Text Representation and Feature Engineering
## AIAT 121 — Natural Language Processing

Unit hours: 12 (theory+practical)

**Official unit title: Text Representation and Feature Engineering.** The folder keeps its original slug (`unit2-tokenization-morphology/`).

## What This Unit Teaches

How to turn text into features that models can use: advanced tokenization strategies (word, sentence, subword/BPE-style), handling morphologically rich languages, and dense word representations trained with Word2Vec.

## Examples (run in order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

1. **[CORE]** `examples/01_advanced_tokenization.ipynb` — Advanced tokenization (subword, BPE-style), handling morphologically rich languages, and choosing a tokenization strategy for a given model.
2. **[CORE]** `examples/02_word_embeddings_word2vec.ipynb` — Train Word2Vec-style skip-gram embeddings from scratch in NumPy, explore word similarity, and visualize the embedding space with PCA/t-SNE (the gensim API is shown as a reference recipe).

## Exercise

- `exercises/01_tokenization_exercise.ipynb` — Multi-language text processing with NLTK.

## Quiz

- `../QUIZZES/quiz_02.md` — Unit 2 quiz (45 minutes, 110 points; 100 required).

Solutions and answer keys are released by your instructor.

## Prerequisites

- Unit 1: Introduction to NLP
- Notebooks run on the **ai-diploma** Jupyter kernel (repository root `.venv`)
