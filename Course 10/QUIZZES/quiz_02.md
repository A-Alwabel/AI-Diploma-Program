# Quiz 02 – Unit 2: Text and Language Generation
## AIAT 124 - Generative AI

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 2 (language models, GPT, text generation, fine-tuning, BLEU/perplexity).
**Concepts from:** Unit 2 examples 01 (GPT-style text generation), 02 (fine-tuning), 04 (text-to-text), 05 (creative text), 06 (BLEU/perplexity) and related slides.
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What is **autoregressive text generation**?

a) Generating all tokens simultaneously
b) Generating text one token at a time, where each new token is conditioned on all previously generated tokens
c) A technique specific to BERT
d) Generating text using only CNNs

---

### Question 2 (10 points)
**Perplexity** as an evaluation metric measures:

a) The speed of text generation
b) How uncertain the model is about the test data — lower perplexity means the model predicts the text more confidently
c) The length of generated text
d) The BLEU score

---

### Question 3 (10 points)
The key architectural difference between **GPT (decoder-only)** and **BERT (encoder-only)** is:

a) GPT uses convolutions; BERT uses attention
b) GPT generates text autoregressively using causal (left-to-right) attention; BERT reads full context bidirectionally for understanding
c) BERT can generate text; GPT cannot
d) There is no architectural difference

---

### Question 4 (10 points)
**BLEU score** evaluates text quality by:

a) Measuring perplexity
b) Comparing n-gram overlaps between generated text and reference text — higher BLEU = closer to reference
c) Using a discriminator neural network
d) Measuring number of unique words

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write PyTorch code to define a **character-level LSTM language model**:
- Use: nn.Embedding(vocab_size=50, embedding_dim=32), nn.LSTM(32, hidden_size=64, num_layers=2, batch_first=True), nn.Linear(64, 50).
- Write a generate(seed_text, max_length=50) function that produces characters one at a time using argmax selection.
- Show the CrossEntropyLoss used for training (input: logits of shape [batch, seq, vocab]; target: next character indices).

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain **greedy (argmax) decoding** versus **temperature sampling** for text generation. How does each method choose the next token, and what trade-off does the temperature value control?

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
What is **few-shot prompting** in LLMs? Give one concrete example showing a few-shot prompt for sentiment classification.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A text generation model produces coherent but very repetitive outputs for different prompts. What would you change in the generation strategy (e.g., temperature, top-k, top-p sampling) to increase diversity?

**Answer key:** released by your instructor.

---

**Mapping:** CLO2, CLO6; notebooks: 01_text_generation_gpt_models, 04_building_text_to_text_generation, 06_evaluating_text_quality_bleu_perplexity.

**For:** AIAT 124 - Generative AI
