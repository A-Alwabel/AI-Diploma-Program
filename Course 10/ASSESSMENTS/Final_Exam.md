# Final Exam: Generative AI
## AIAT 124

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. Show your work for partial credit.

---

## Part 1: Multiple Choice (30 points)

### Question 1 (5 points)
**CLO1:** What is the main difference between generative and discriminative models?

A) Discriminative generate data
B) No difference  
C) Generative are always better  
D) Generative models learn P(X|Y), discriminative learn P(Y|X)  

---

### Question 2 (5 points)
**CLO2:** What does GAN stand for?

A) General Adversarial Network  
B) Generative Adversarial Network  
C) Gradient Adversarial Network  
D) Global Adversarial Network

---

### Question 3 (5 points)
**CLO3:** What is the key component of VAEs that enables generation?

A) Only encoder  
B) Only decoder  
C) Latent space with probabilistic sampling  
D) Only loss function

---

### Question 4 (5 points)
**CLO4:** Which metric is commonly used to evaluate generative models?

A) FID, IS, reconstruction error  
B) Only accuracy  
C) Only precision  
D) Only recall

---

### Question 5 (5 points)
**CLO5:** What is a real-world application of generative AI?

A) Image generation, text generation, music generation, data augmentation  
B) Only image generation  
C) Only text generation  
D) Only music generation

---

### Question 6 (5 points)
**CLO6:** What is a major ethical concern with generative AI?

A) Only bias  
B) Only privacy  
C) Deepfakes, misinformation, bias, intellectual property  
D) No concerns

---

## Part 2: Short Answer Questions (30 points)

### Question 7 (10 points)
**CLO1, CLO2:** Explain how GANs work. Describe the adversarial training process between generator and discriminator.

---

### Question 8 (10 points)
**CLO3:** Explain the VAE architecture and loss function. What is the role of the KL divergence term?

---

### Question 9 (10 points)
**CLO6:** Discuss ethical implications of generative AI. Provide examples and mitigation strategies.

---

## Part 3: Practical/Coding Questions (25 points)

### Question 10 (15 points)
**CLO2, CLO3:** Implement a simple VAE for image generation:
1. Define encoder and decoder networks
2. Implement reparameterization trick
3. Define VAE loss (reconstruction + KL divergence)
4. Show training loop structure

---

### Question 11 (10 points)
**CLO5:** Write a PyTorch function that performs **temperature-controlled text sampling** from a character-level language model. Given a model that outputs logits of shape `(vocab_size,)`, write code to:
1. Apply temperature scaling (`logits / temperature`).
2. Convert to probabilities with softmax.
3. Sample the next token using `torch.multinomial`.
4. Explain what happens to diversity when temperature → 0 vs temperature → ∞.

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
**CLO5, CLO7:** Design a generative AI system for a fashion design company:
1. Choose appropriate generative model (GAN/VAE/Diffusion)
2. Explain model architecture
3. Training strategy
4. Evaluation methods
5. Address ethical considerations (bias, authenticity)
6. Future trends and improvements

---

**End of Exam**

**Good Luck!**
