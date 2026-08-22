# AIAT 121 — Natural Language Processing

**New students: read `START_HERE.md` first.**

Credit hours: 3 · Contact hours: 4/week · Total training hours: 64 (theory+practical)

## Course Overview

This course covers Natural Language Processing (NLP) with Python: text preprocessing and representation, classical machine learning for text, deep learning models (RNNs, LSTMs, Transformers), and the ethics of NLP systems. Hands-on work uses NLTK, spaCy, scikit-learn, and Hugging Face Transformers (the Word2Vec notebook implements skip-gram in NumPy and shows the gensim API as a reference).

Note: several units currently have only one or two example notebooks; additional content is being authored. Each unit README lists exactly what exists today.

## Units

| Unit | Official title | Folder | Hours |
|------|----------------|--------|-------|
| 1 | Introduction to NLP | `unit1-nlp-fundamentals/` | 12 |
| 2 | Text Representation and Feature Engineering | `unit2-tokenization-morphology/` | 12 |
| 3 | Machine Learning for NLP | `unit3-ml-for-nlp/` | 12 |
| 4 | Deep Learning for NLP | `unit4-deep-learning-nlp/` | 14 |
| 5 | NLP Applications and Ethics Standards | `unit5-applications-ethics/` | 14 |

The Unit 2 folder keeps its original slug (`unit2-tokenization-morphology/`); the official unit title is **Text Representation and Feature Engineering**.

## Prerequisites

- Semester 1 (AIAT 111–116)
- Python programming and basic machine learning concepts

## Setup

- Use the repository root `.venv` and select the **ai-diploma** Jupyter kernel for notebooks.
- Unit 4 notebook `04_seq2seq_attention_translation.ipynb` uses TensorFlow — run it on the **tfenv** kernel. The Hugging Face notebooks (BERT, GPT-2) run on the **ai-diploma** kernel via PyTorch.
- `unit4-deep-learning-nlp/examples/05_gpt_openai_text_generation.ipynb` generates text with a local GPT-2 model; its OpenAI API section is a non-executed walkthrough, so no API key is needed.

## Course Learning Outcomes (CLOs)

This course has 10 CLOs — the most of any course in the program. The trainee will be able to:

1. Understand NLP fundamentals and importance in real-world applications.
2. Apply text processing techniques such as tokenization, stemming, lemmatization, and vectorization.
3. Implement traditional machine learning models for NLP tasks such as classification, named entity recognition, and topic modeling.
4. Use deep learning techniques such as Recurrent Neural Networks (RNNs), Long Short-Term Memory networks (LSTMs), and Transformers.
5. Work with popular NLP frameworks such as NLTK, spaCy, and Hugging Face Transformers.
6. Develop and evaluate NLP applications such as sentiment analysis, text summarization, and chatbots.
7. Analyze ethical considerations and challenges in NLP, including bias and fairness in AI models.
8. Optimize and fine-tune pre-trained language models for custom NLP tasks.
9. Implement multilingual and cross-lingual NLP solutions.
10. Design and implement end-to-end NLP pipelines for real-world applications.

## Course Structure

```
Course 07/
├── README.md
├── START_HERE.md
├── STUDENT_PROGRESS_CHECKLIST.md
├── unit1-nlp-fundamentals/        Unit 1: Introduction to NLP
├── unit2-tokenization-morphology/ Unit 2: Text Representation and Feature Engineering
├── unit3-ml-for-nlp/              Unit 3: Machine Learning for NLP
├── unit4-deep-learning-nlp/       Unit 4: Deep Learning for NLP
├── unit5-applications-ethics/     Unit 5: NLP Applications and Ethics Standards
├── QUIZZES/                       Quiz 01 (Unit 1); quizzes 02-05 are placeholders being authored
├── ASSESSMENTS/                   Final exam
├── PROJECTS/                      Course project (Sentiment Analysis System) + template
├── CASE_STUDIES/                  NLP application case study
└── PRESENTATIONS/                 Presentation template
```

## Assessments

- Quizzes: `QUIZZES/` — `quiz_01.md` covers Unit 1; quizzes 02–05 are placeholders being authored.
- Final exam: `ASSESSMENTS/Final_Exam.md` (2 hours, 100 points, covers all 10 CLOs).
- Project: `PROJECTS/Sentiment_Analysis_System/`.
- Answer keys and solutions are released by your instructor.
