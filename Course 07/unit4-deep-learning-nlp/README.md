# Unit 4: Deep Learning for NLP
## AIAT 121 — Natural Language Processing

Unit hours: 14 (theory+practical)

## What This Unit Teaches

Deep learning models for language: recurrent networks (RNNs, LSTMs) for sequence modeling, Transformer-based models (fine-tuning BERT), sequence-to-sequence models with attention for machine translation, and text generation with GPT models via the OpenAI API.

## Examples (run in order)

1. `examples/01_rnn_lstm_nlp.ipynb` — RNNs and LSTMs for sequence modeling, built with NumPy to show the mechanics.
2. `examples/02_bert_advanced_usage.ipynb` — Fine-tune a BERT model for text classification with Hugging Face Transformers and TensorFlow. *(tfenv kernel)*
3. `examples/03_seq2seq_attention_translation.ipynb` — Sequence-to-sequence models with attention for machine translation in TensorFlow. *(tfenv kernel)*
4. `examples/04_gpt_openai_text_generation.ipynb` — Text generation with GPT models through the OpenAI API. *(requires an OpenAI API key)*

## Exercise

- `exercises/01_ner_exercise.ipynb` — Named entity recognition for news articles with spaCy.

## Quiz

- `../QUIZZES/quiz_04.md` — placeholder being authored.

Solutions and answer keys are released by your instructor.

## Prerequisites

- Units 1–3 of this course
- Neural network basics from Semester 1 (AIAT 111–116)
- Notebooks run on the **ai-diploma** Jupyter kernel (repository root `.venv`); the TensorFlow notebooks (02, 03) run on the **tfenv** kernel
