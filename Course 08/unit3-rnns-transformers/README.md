# Unit 3 — Recurrent Neural Networks (RNNs) and Transformers for Sequential Data
## AIAT 122 — Deep Learning

Unit training hours: 12 (of 64 total)

## Prerequisites

- Units 1–2 (neural network training; comfortable building models).
- Environment set up (see `../START_HERE.md`): "ai-diploma" kernel for PyTorch notebooks, "tfenv" kernel for TensorFlow notebooks.

## What this unit teaches

Sequential data (time series, text, audio) and why feedforward networks fall short; RNNs and their vanishing/exploding gradient challenges; LSTM and GRU; attention and the Transformer architecture; using pretrained models (BERT, GPT) for NLP tasks such as sentiment analysis, translation, and text generation.

## Examples (do in file order)

Run the notebooks in `examples/` in this order:

1. `01_understanding_sequential_data_and_time_series_prediction.ipynb` — what makes data sequential; a first time-series prediction.
2. `02_rnn_basics.ipynb` — how RNNs work; vanishing and exploding gradients.
3. `03_lstm_advanced.ipynb` — LSTM (and GRU) gates and why they help with long sequences.
4. `04_transformer_attention.ipynb` — attention from scratch: queries, keys, values; self-attention.
5. `05_bert_finetuning.ipynb` — the BERT fine-tuning pattern (encoder + classification head), demonstrated hands-on with a from-scratch LSTM stand-in; real pretrained BERT appears in `09`.
6. `06_gpt_text_generation.ipynb` — generate text with a pretrained GPT model.
7. `07_sequence_to_sequence.ipynb` — encoder–decoder (Seq2Seq) models for tasks like translation.
8. `08_text_generation_rnn_lstm_gru.ipynb` — character/word-level text generation with RNN/LSTM/GRU.
9. `09_transformer_models_bert_gpt_nlp.ipynb` — survey of Transformer models (BERT, GPT) across NLP tasks.
10. `10_sentiment_analysis_translation_speech.ipynb` — applied NLP: sentiment analysis, translation, and speech-related tasks.

Note: notebooks that load pretrained models (05, 06, 09, 10) download weights and can take several minutes; a GPU (e.g. Colab, see `../DOCS/COLAB_SETUP.md`) and small batch sizes help.

## Exercises

- `exercises/01_rnn_exercise.ipynb` — RNN/LSTM for a sequence or text task (pairs with examples 02–03).
- `exercises/02_transformer_exercise.ipynb` — attention/Transformer usage (pairs with examples 04–05).

Solutions are released by your instructor.

## Quiz

- `../QUIZZES/quiz_03.md`

## Next

Unit 4: `../unit4-advanced-dl/README.md`
