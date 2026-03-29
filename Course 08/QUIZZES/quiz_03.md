# Quiz 03 – Unit 3: RNNs and Transformers
## AIAT 122 - Deep Learning

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 3 (RNNs, LSTM, attention, Transformers, BERT/GPT).  
**Concepts from:** Unit 3 examples 02 (RNN), 03 (LSTM), 04 (attention), 05 (BERT) and related slides.  
**Answers and rubrics:** Instructor only — see `DOCS/SOLUTIONS/quizzes/`.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What problem do **RNNs** address that feedforward networks do not?

a) They are faster  
b) They can handle **sequential data** by maintaining a hidden state that carries information across time steps  
c) They need less memory  
d) They only work for images  

---

### Question 2 (10 points)
Why do we use **LSTM** (or GRU) instead of a simple RNN in practice?

a) LSTMs are always smaller  
b) LSTMs mitigate the **vanishing gradient** problem and can capture long-range dependencies better  
c) LSTMs do not use gradients  
d) LSTMs only work for classification  

---

### Question 3 (10 points)
What does the **attention mechanism** in Transformers do?

a) It replaces all layers  
b) It lets the model **focus on relevant parts of the input** (e.g. different words) when producing each output  
c) It only runs once per sequence  
d) It is used only in CNNs  

---

### Question 4 (10 points)
**BERT** is primarily used for:

a) Only image classification  
b) **Understanding** text (e.g. classification, NER, QA) and is pre-trained with masked language modeling  
c) Only text generation  
d) Reinforcement learning  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write code to build a **simple LSTM** in **PyTorch** for sequence classification (e.g. binary sentiment). Use:
- `nn.Embedding(vocab_size=1000, embedding_dim=64)`, then `nn.LSTM(input_size=64, hidden_size=32, batch_first=True)`.
- Take the last hidden state and pass through `nn.Linear(32, 1)` with sigmoid for binary output.
- Show the full `nn.Module` class with `__init__` and `forward` methods. Input is integer sequences of shape `(batch, seq_len=100)`.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_03_solution.md`.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
What problem does **attention** solve that RNNs/LSTMs struggle with (e.g. long sequences), and how does it help?

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_03_solution.md`.

---

### Question 7 (15 points)
In one or two sentences, what is the main difference between **BERT** (encoder) and **GPT** (decoder) in terms of how they are typically used?

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_03_solution.md`.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A **sentiment model** performs well on short reviews but poorly on **long documents**. What might be the cause (e.g. architecture or sequence length), and how could **attention** or a different model choice help?

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_03_solution.md`.

---

**Mapping:** CLO2; notebooks: 02_rnn_basics, 03_lstm_advanced, 04_transformer_attention, 05_bert_finetuning.

**For:** AIAT 122 - Deep Learning
