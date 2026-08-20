# Quiz 04 – Unit 4: Advanced Deep Learning
## AIAT 122 - Deep Learning

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 4 (GANs, VAEs, reinforcement learning, ethics: bias, fairness, interpretability).  
**Concepts from:** Unit 4 examples 01 (GANs/VAEs), 02 (VAE anomaly), 03 (RL), 04 (ethics) and related slides.  
**Answers and rubrics:** Instructor only — see `DOCS/SOLUTIONS/quizzes/`.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
In a **GAN**, what is the role of the **discriminator**?

a) To generate new samples  
b) To **distinguish real data from generator outputs** and provide a signal to train the generator  
c) To compress data  
d) To tune the learning rate  

---

### Question 2 (10 points)
A **Variational Autoencoder (VAE)** differs from a standard autoencoder because:

a) It has no encoder  
b) It learns a **latent distribution** (e.g. Gaussian) and uses reparameterization; we can sample from it to generate new data  
c) It does not use backpropagation  
d) It is only for classification  

---

### Question 3 (10 points)
In **reinforcement learning**, the agent learns by:

a) Using only labeled data  
b) **Maximizing cumulative reward** through interaction with an environment (trial and error)  
c) Minimizing classification loss only  
d) Using only supervised learning  

---

### Question 4 (10 points)
Why do we evaluate **fairness** (e.g. accuracy by demographic group) in addition to overall accuracy?

a) To make models larger  
b) Because a model can have **high overall accuracy but be unfair** to some groups; we need to measure and mitigate this  
c) To replace the need for a test set  
d) Only for image models  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Outline or write the key steps (in code or pseudocode) to **fine-tune a pre-trained model** for a new classification task: load a pre-trained model (e.g. ResNet or BERT), add or replace the head for your number of classes, and run training for a few epochs. You may use Keras/TF or PyTorch.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain **one** ethical concern when deploying a deep learning model (e.g. bias, fairness, or interpretability) and why it matters.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
What is **interpretability** in the context of deep learning, and name one reason we might need it (e.g. regulation, debugging, user trust).

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A hospital deploys a **skin lesion classifier** that works well overall but has **much lower recall for one skin type**. What ethical and technical steps would you recommend (e.g. evaluation, data, or fairness metrics)?

**Answer key:** released by your instructor.

---

**Mapping:** CLO4, CLO5; notebooks: 01_gans_and_autoencoders_vaes, 03_reinforcement_learning_*, 04_ethical_concerns_*.

**For:** AIAT 122 - Deep Learning
