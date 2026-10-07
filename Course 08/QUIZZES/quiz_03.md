# Quiz 03 – Unit 3: RNNs and Transformers
## AIAT 122 - Deep Learning

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 3 (RNNs, LSTM, attention, Transformers, BERT/GPT).  
**Concepts from:** Unit 3 examples 02 (RNN), 03 (LSTM), 04 (attention), 05 (BERT) and related slides.  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What problem do **RNNs** address that feedforward networks do not?

a) They are faster  
b) They learn a separate set of weights for each time step, so longer sequences need a bigger model  
c) They read the whole sequence at once and weight the most relevant positions  
d) They can handle sequential data by maintaining a hidden state that carries information across time steps  

---

### Question 2 (10 points)
Why do we use **LSTM** (or GRU) instead of a simple RNN in practice?

a) The gates let an LSTM skip time steps that carry no new information, so long sequences take fewer steps  
b) LSTMs remove the need to pad or truncate sequences to a common length  
c) LSTMs mitigate the vanishing gradient problem and can capture long-range dependencies better  
d) LSTMs copy the complete input history into the cell state instead of a compressed summary  

---

### Question 3 (10 points)
What does the **attention mechanism** in Transformers do?

a) It lets the model focus on relevant parts of the input (e.g. different words) when producing each output  
b) It processes the tokens one at a time, passing a hidden state from each token to the next  
c) It gives each vocabulary word a fixed importance score that is learned during training and reused at inference  
d) It compresses the whole input sequence into a single fixed-size context vector  

---

### Question 4 (10 points)
**BERT** is primarily used for:

a) Generating long passages of text one token at a time from a left-to-right prompt, as GPT-style decoders do  
b) Understanding text (e.g. classification, NER, QA) and is pre-trained with masked language modeling  
c) Translating between languages with an encoder–decoder trained on paired sentences  
d) Predicting the next word in a sentence, which is the objective it is pre-trained on before fine-tuning  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write code to build a **simple LSTM** for sequence classification (e.g. binary sentiment) in **either PyTorch or Keras/TensorFlow** (both are used in Unit 3; state which one you chose). Input is integer token sequences of shape `(batch, seq_len=100)` from a vocabulary of 1000. Architecture:
- Embedding layer (1000 tokens → 64 dimensions), then an LSTM with 32 hidden units, then a single sigmoid output for the binary label.
- PyTorch: `nn.Embedding(1000, 64)` → `nn.LSTM(input_size=64, hidden_size=32, batch_first=True)` → take the last time step (`out[:, -1, :]` or the final hidden state) → `nn.Linear(32, 1)` → sigmoid; show the full `nn.Module` class with `__init__` and `forward`.
- Keras/TensorFlow: `Embedding(1000, 64)` → `LSTM(32)` → `Dense(1, activation='sigmoid')`; name the matching loss (`binary_crossentropy`).

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
What problem does **attention** solve that RNNs/LSTMs struggle with (e.g. long sequences), and how does it help?

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
In one or two sentences, what is the main difference between **BERT** (encoder) and **GPT** (decoder) in terms of how they are typically used?

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A **sentiment model** performs well on short reviews but poorly on **long documents**. What might be the cause (e.g. architecture or sequence length), and how could **attention** or a different model choice help?

**Answer key:** released by your instructor.

---

**Mapping:** CLO2; notebooks: 02_rnn_basics, 03_lstm_advanced, 04_transformer_attention, 05_bert_finetuning.

**For:** AIAT 122 - Deep Learning
