# Quiz 04 – Unit 4: Deep Learning for NLP
## AIAT 121 - Natural Language Processing

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 4 (attention and transformers, positional encodings, causal masking / BERT vs. GPT, RNNs and LSTMs, the vanishing gradient, pretrained models with Hugging Face, GPT-2 text generation).  
**Concepts from:** Unit 4 examples 01 (attention/transformers bridge), 02 (RNNs & LSTMs), 03 (BERT in practice), 05 (GPT text generation).  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
In **self-attention**, the output vector for a word is:

a) A copy of the word's own embedding  
b) A random vector that gets trained later  
c) The hidden state of an RNN at that position  
d) A weighted average of all the word vectors in the sentence, with weights computed by softmax over query–key similarity scores  

---

### Question 2 (10 points)
Why do transformers need **positional encodings**?

a) To make the vectors longer  
b) Because attention by itself is order-blind — it sees a bag of vectors, so "dog bites man" and "man bites dog" would look the same without position information  
c) To remove stop words automatically  
d) To reduce the memory used by attention  

---

### Question 3 (10 points)
What does the **causal mask** do, and which model family uses it?

a) It blocks attention to future positions so each word sees only itself and the past; used by GPT-style (decoder) models for generation  
b) It hides rare words; used by BERT  
c) It removes attention entirely; used by RNNs  
d) It doubles the attention weights; used by all transformers  

---

### Question 4 (10 points)
The Unit 4 notebook **measured** the vanishing-gradient problem: over 50 RNN steps, the surviving gradient signal shrank to about 10⁻²⁹. Why do **LSTMs** cope better with long-range dependencies?

a) They use bigger learning rates  
b) They process the sequence backwards  
c) Learned gates (forget/input/output) plus an additive cell-state "memory lane" let information flow across many steps without being repeatedly squashed  
d) They have more layers than RNNs  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write code that uses a **pretrained sentiment model** from Hugging Face (the modern workhorse pattern — no training needed):

1. Import `pipeline` from `transformers`.
2. Create a `"sentiment-analysis"` pipeline with the checkpoint `distilbert-base-uncased-finetuned-sst-2-english`.
3. Classify the sentences `"I love natural language processing!"` and `"This movie was terrible."`.
4. For each sentence, print the text, the predicted label, and the confidence score.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
In the toy sentence *"the animal crossed the street because it was tired"*, the word **"it"** puts most of its attention (≈43%) on **"animal"**. Explain the mechanism that produces this: where do the attention weights come from, and why does each row of the attention matrix sum to 1?

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Compare **greedy decoding** and **temperature sampling** for GPT-2 text generation, as demonstrated in Unit 4: how does each pick the next token, what failure mode does greedy decoding show, and what changes as temperature rises (e.g. 0.7 → 1.3)?

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
Your company needs (a) a classifier that routes incoming support tickets by topic, and (b) a system that drafts reply text for agents. For each need, choose **BERT-style (encoder)** or **GPT-style (decoder)** models, and justify both choices using the attention patterns each family uses.

**Answer key:** released by your instructor.

---

**Mapping:** CLO4, CLO5, CLO8; notebooks: `unit4-deep-learning-nlp/examples/01_attention_transformers_bridge`, `02_rnn_lstm_nlp`, `03_bert_advanced_usage`, `05_gpt_openai_text_generation`.

**For:** AIAT 121 - Natural Language Processing
