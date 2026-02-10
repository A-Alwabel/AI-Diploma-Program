# Unit 3: Recurrent Neural Networks (RNNs) and Transformers
## AIAT 122 - Deep Learning

**Unit content** aligns with curriculum (see course README and DOCS/EXAMPLES_ORDER.md; DETAILED_UNIT_DESCRIPTIONS if available in your repo). Topic: RNNs and Transformers for Sequential Data.

## ✅ Prerequisites Checklist

Before starting this unit, confirm:

- [ ] Completed Unit 2: Convolutional Neural Networks (CNNs) for Computer Vision
- [ ] Understand deep learning fundamentals (Unit 1)
- [ ] Comfortable with neural network architectures
- [ ] Installed required libraries (`pip check` passes)
- [ ] Reviewed related topics (see course README and DOCS/EXAMPLES_ORDER.md; COURSE_MAP if available in your repo)

### Learning Objectives

By the end of this unit, students will be able to:
- Understand sequential data and time series prediction
- Implement RNN, LSTM, and GRU architectures
- Understand attention mechanisms and Transformer architecture
- Use pre-trained Transformer models (BERT, GPT)
- Apply RNNs and Transformers to NLP tasks
- Perform sentiment analysis, machine translation, and speech recognition

---

## Topics Covered

Based on official curriculum (AIAT 122), this unit covers:

1. **Understanding Sequential Data**
   - Temporal, audio, and textual data
   - Difference between feedforward networks and recurrent networks

2. **Recurrent Neural Networks (RNNs)**
   - How RNNs work
   - Challenges: vanishing and exploding gradients

3. **LSTM and GRU Networks**
   - Structure and benefits of LSTM and GRU
   - Applications in text generation and speech recognition

4. **Attention Mechanism and Transformers**
   - Introduction to attention mechanism
   - Transformer architecture (self-attention, multi-head attention)
   - BERT and GPT and their applications in NLP

5. **NLP Models**
   - Sentiment analysis and text classification
   - Machine translation using Seq2Seq models

---

## Recommended order (examples)

Follow this order to align with slides **21 → 17 → 12 → 03 → 13**. Full table: `DOCS/EXAMPLES_ORDER.md`.

1. `01_understanding_sequential_data_and_time_series_prediction.ipynb`  
2. `02_rnn_basics.ipynb`  
3. `03_lstm_advanced.ipynb`  
4. `04_transformer_attention.ipynb`  
5. `05_bert_finetuning.ipynb`  

*Optional (do after the core 01–05; order among these doesn't matter):* `06_gpt_text_generation.ipynb`, `07_sequence_to_sequence.ipynb`, `08_text_generation_rnn_lstm_gru.ipynb`, `09_transformer_models_bert_gpt_nlp.ipynb`, `10_sentiment_analysis_translation_speech.ipynb`

**⏱ Long run:** Notebooks **05** (BERT fine-tuning), **06** (GPT), and **09–10** can take **5–15+ minutes** (downloads, model load, training). Use Colab GPU and a small batch/subset for quicker runs.

---

## Exercises

Complete the exercises in `unit3-rnns-transformers/exercises/`:

1. **`01_rnn_exercise.ipynb`** – RNN/LSTM for sequence or text. Aligns with `02_rnn_basics.ipynb`, `03_lstm_advanced.ipynb`.
2. **`01_transformer_exercise.ipynb`** – Transformer/BERT usage. Aligns with `04_transformer_attention.ipynb`, `05_bert_finetuning.ipynb`.

**Solutions:** See `DOCS/SOLUTIONS/exercises/` (instructor-only; do not distribute before deadline).

---

## Teaching note (instructors)

- **Suggested time:** Core examples 01–05: ~2 hours; optional 06–10: +1–1.5 hours. Theory (slides): ~6 hours.
- **Demo notebook:** `04_transformer_attention.ipynb` or `05_bert_finetuning.ipynb` – show attention or BERT fine-tuning.
- **Common stumbling block:** GPU for BERT/GPT; long runtimes on CPU; recommend Colab GPU and small batch size (see `DOCS/COLAB_SETUP.md`).
- **Exercise alignment:** RNN exercise with 02, 03; Transformer exercise with 04, 05.

---

## Unit Breakdown

**Theoretical Hours:** 6  
**Practical Hours:** 13  
**Total Hours:** 19

### Theoretical Content

- Understanding sequential data and time series prediction
- RNN structure and challenges (vanishing gradients problem)
- Advanced architectures: LSTM, GRU, Transformers, attention mechanism
- Applications in NLP

### Practical Content

- Implementing RNN, LSTM, and GRU for text generation
- Using Transformer models like BERT and GPT for NLP tasks
- Performing sentiment analysis, machine translation, and speech recognition

---

**Unit Duration:** 2 weeks  
**Difficulty:** Advanced  
**Prerequisites:** Units 1-2 completion

**Created for:** AIAT 122 - Deep Learning  
**Last Updated:** 2025-01-24 (reorganized: Transformers merged from Unit 4 to match DETAILED_UNIT_DESCRIPTIONS)
