# Quiz 05 – Unit 5: Future Trends in Generative AI
## AIAT 124 - Generative AI

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 5 (multimodal AI, CLIP, advanced models, creative applications, future challenges).
**Concepts from:** Unit 5 examples (generative AI applications, music generation, future trends) and related slides.
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
**CLIP (Contrastive Language-Image Pre-Training)** enables:

a) Only image classification
b) Joint understanding of text and images — enabling zero-shot classification and text-to-image retrieval via aligned embeddings
c) Only text generation
d) Only object detection

---

### Question 2 (10 points)
**Multimodal generative AI** (e.g., DALL-E, Gemini) differs from unimodal models because:

a) It only processes images
b) It can accept and generate multiple data types (text, images, audio, video) and understands cross-modal relationships
c) It is faster to train
d) It requires less data

---

### Question 3 (10 points)
**WaveNet** is an example of generative AI applied to:

a) Music playlist recommendation
b) Raw audio synthesis — generating a waveform one sample at a time with an autoregressive model
c) Video generation
d) Text translation

---

### Question 4 (10 points)
A key **computational challenge** in scaling generative AI is:

a) Lack of algorithms
b) The enormous compute, energy, and data required for very large models, raising sustainability and access concerns
c) GPUs are becoming slower
d) There are no remaining challenges

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write Python code demonstrating a **simple multimodal similarity search**:
- Simulate text and image embeddings: text_emb = torch.randn(1, 512), img_embs = torch.randn(5, 512).
- Implement find_closest_image(text_emb, img_embs) using cosine similarity:
  cos_sim = (a @ b.T) / (||a|| * ||b||)
- Return the index of the most similar image embedding.
- Print the index and similarity score.
Use: torch.nn.functional.cosine_similarity or manual computation.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Unit example 02 maps **five research directions** shaping generative AI (the "Five Directions to Watch" table). Name at least four of the five directions and briefly explain two of them, giving one tool or model that each of those two directions already powers.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Name **three** industries being transformed by generative AI and give a **concrete application** for each (e.g., healthcare, entertainment, education).

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A company uses generative AI to create personalized educational exercises for each student. Identify: (1) the technique you would use, (2) one ethical concern, (3) how you would evaluate quality of generated content.

**Answer key:** released by your instructor.

---

**Mapping:** CLO7; notebooks: Unit 5 future trends examples.

**For:** AIAT 124 - Generative AI
