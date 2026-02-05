# Unit 3: Recurrent Neural Networks (RNNs) and Transformers | الشبكات العصبية المتكررة والمحولات
## AIAT 122 - Deep Learning

**Maps to (DETAILED_UNIT_DESCRIPTIONS):** Unit 3 — Recurrent Neural Networks (RNNs) and Transformers for Sequential Data.

## ✅ Prerequisites Checklist | قائمة المتطلبات الأساسية

Before starting this unit, confirm:

- [ ] Completed Unit 2: Convolutional Neural Networks (CNNs) for Computer Vision
- [ ] Understand deep learning fundamentals (Unit 1)
- [ ] Comfortable with neural network architectures
- [ ] Installed required libraries (`pip check` passes)
- [ ] Reviewed related topics in `COURSE_MAP.md` if needed

### Learning Objectives | أهداف التعلم

By the end of this unit, students will be able to:
- Understand sequential data and time series prediction
- Implement RNN, LSTM, and GRU architectures
- Understand attention mechanisms and Transformer architecture
- Use pre-trained Transformer models (BERT, GPT)
- Apply RNNs and Transformers to NLP tasks
- Perform sentiment analysis, machine translation, and speech recognition

---

## Topics Covered | المواضيع المغطاة

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

## Recommended order (examples) | ترتيب الأمثلة الموصى به

Follow this order to align with slides **21 → 17 → 12 → 03 → 13**. Full table: `DOCS/EXAMPLES_ORDER.md`.

1. `01_understanding_sequential_data_and_time_series_prediction.ipynb`  
2. `02_rnn_basics.ipynb`  
3. `03_lstm_advanced.ipynb`  
4. `04_transformer_attention.ipynb`  
5. `05_bert_finetuning.ipynb`  

*Optional (do after the core 01–05; order among these doesn't matter):* `06_gpt_text_generation.ipynb`, `07_sequence_to_sequence.ipynb`, `08_text_generation_rnn_lstm_gru.ipynb`, `09_transformer_models_bert_gpt_nlp.ipynb`, `10_sentiment_analysis_translation_speech.ipynb`

---

## Unit Breakdown | تفصيل الوحدة

**Theoretical Hours:** 6  
**Practical Hours:** 6  
**Total Hours:** 12

### Theoretical Content | المحتوى النظري

- Understanding sequential data and time series prediction
- RNN structure and challenges (vanishing gradients problem)
- Advanced architectures: LSTM, GRU, Transformers, attention mechanism
- Applications in NLP

### Practical Content | المحتوى العملي

- Implementing RNN, LSTM, and GRU for text generation
- Using Transformer models like BERT and GPT for NLP tasks
- Performing sentiment analysis, machine translation, and speech recognition

---

**Unit Duration:** 2 weeks  
**Difficulty:** Advanced  
**Prerequisites:** Units 1-2 completion

**Created for:** AIAT 122 - Deep Learning  
**Last Updated:** 2025-01-24 (reorganized: Transformers merged from Unit 4 to match DETAILED_UNIT_DESCRIPTIONS)
