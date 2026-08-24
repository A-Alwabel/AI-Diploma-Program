# Unit 4: Deep Learning for NLP
## AIAT 121 — Natural Language Processing

Unit hours: 14 (theory+practical)

## What This Unit Teaches

Deep learning models for language, used as **pretrained building blocks**: what attention and transformers are (taught first, from scratch, in NumPy), recurrent networks (RNNs/LSTMs) and the bottleneck that motivated attention, sentiment classification with a pretrained BERT-family model, a sequence-to-sequence translation architecture with attention built in Keras, and text generation with a local GPT-2 model.

**Note on order:** this course runs *before* the Deep Learning course (AIAT 122), so unit 4 deliberately stays at the "understand the mechanism, use pretrained models" level. Training mechanics (backpropagation, optimizers, building transformers) arrive in AIAT 122.

## Examples (run in order)

1. `examples/01_attention_transformers_bridge.ipynb` — Attention and transformers from scratch: scaled dot-product attention computed by hand in NumPy, attention-map heatmaps, positional encodings, causal masking, and how BERT/GPT fit the map.
2. `examples/02_rnn_lstm_nlp.ipynb` — RNNs and LSTMs: a real NumPy forward pass, the vanishing-gradient problem measured numerically, and one hand-computed LSTM step.
3. `examples/03_bert_advanced_usage.ipynb` — Sentiment classification with a pretrained DistilBERT model via Hugging Face, plus the fine-tuning recipe as a code walkthrough (not executed). *(downloads ~250MB on first run)*
4. `examples/04_seq2seq_attention_translation.ipynb` — Build (and forward-pass, without training) a Keras seq2seq model with attention for machine translation. *(tfenv kernel)*
5. `examples/05_gpt_openai_text_generation.ipynb` — Real text generation with a local GPT-2 model (greedy vs. sampling, temperature), plus an OpenAI API walkthrough (not executed; no API key needed for this notebook). *(downloads ~500MB on first run)*

## Exercise

- `exercises/01_ner_exercise.ipynb` — Named entity recognition on provided sample news articles with spaCy.

## Quiz

- `../QUIZZES/quiz_04.md` — Unit 4 quiz (45 minutes, 110 points; 100 required).

Solutions and answer keys are released by your instructor.

## Prerequisites

- Units 1–3 of this course
- Neural network basics from Course 01 (AIAT 111), Unit 4 — notebook 01 and 02 include short refreshers and pointers
- Notebooks run on the **ai-diploma** Jupyter kernel (repository root `.venv`); the TensorFlow notebook (04) runs on the **tfenv** kernel
