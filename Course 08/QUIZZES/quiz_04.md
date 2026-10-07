# Quiz 04 – Unit 4: Advanced Deep Learning
## AIAT 122 - Deep Learning

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 4 (GANs, VAEs, reinforcement learning, ethics: bias, fairness, interpretability).  
**Concepts from:** Unit 4 examples 01 (GANs/VAEs), 02 (VAE anomaly), 03 (RL), 04 (ethics) and related slides.  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
In a **GAN**, what is the role of the **discriminator**?

a) To generate new samples  
b) To distinguish real data from generator outputs and provide a signal to train the generator  
c) To be trained to high accuracy first and then frozen while the generator catches up  
d) To encode each real image into a latent vector that the generator later decodes  

---

### Question 2 (10 points)
A **Variational Autoencoder (VAE)** differs from a standard autoencoder because:

a) It learns a latent distribution (e.g. Gaussian) and uses reparameterization; we can sample from it to generate new data  
b) Its decoder is trained adversarially against a discriminator network that tries to tell reconstructions from real images  
c) It maps each input to a single fixed point in latent space rather than a distribution, so reconstructions are more exact  
d) It adds random noise to the input image so that the decoder learns to remove it  

---

### Question 3 (10 points)
In **reinforcement learning**, the agent learns by:

a) Imitating the correct action for each state, which it reads from a labeled dataset  
b) Choosing the action with the highest immediate reward at each step  
c) Maximizing cumulative reward through interaction with an environment (trial and error)  
d) Exploring at random for the whole run, since trying new actions is what produces the learning  

---

### Question 4 (10 points)
Why do we evaluate **fairness** (e.g. accuracy by demographic group) in addition to overall accuracy?

a) Because per-group accuracy gives a more precise estimate of the overall accuracy when the groups differ in size  
b) To replace the need for a test set  
c) To confirm that the model generalizes from the training split to the test split  
d) Because a model can have high overall accuracy but be unfair to some groups; we need to measure and mitigate this  

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
