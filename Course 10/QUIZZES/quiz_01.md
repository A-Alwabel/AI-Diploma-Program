# Quiz 01 – Unit 1: Generative AI Fundamentals
## AIAT 124 - Generative AI

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 1 (GANs, VAEs, latent spaces, evaluation metrics: FID, BLEU).
**Concepts from:** Unit 1 examples 04 (implementing a VAE), 05 (building a GAN), 08 (training techniques), 10 (evaluating models: FID/BLEU), 12 (latent spaces) and related slides.
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What is the fundamental difference between **generative** and **discriminative** models?

a) Generative models are always larger
b) Generative models learn the joint distribution P(X) and can generate new samples; discriminative models learn P(Y|X) for classification
c) Discriminative models can generate data
d) There is no difference

---

### Question 2 (10 points)
In a GAN, what happens during **adversarial training**?

a) Only the generator is trained
b) The generator tries to produce realistic samples to fool the discriminator; the discriminator tries to tell real from fake — both improve through competition
c) The discriminator generates samples
d) Both networks use the same loss

---

### Question 3 (10 points)
The **reparameterization trick** in VAEs allows:

a) Improving image resolution
b) Gradients to flow through the sampling operation by writing z = mu + eps * sigma (eps ~ N(0,1)), enabling backpropagation through the latent variable
c) Reducing model size
d) Replacing the KL divergence term

---

### Question 4 (10 points)
**FID (Frechet Inception Distance)** measures:

a) Training speed of a GAN
b) The distance between feature distributions of real and generated images — lower FID means more realistic and diverse generated images
c) Only sharpness of generated images
d) Number of parameters

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write PyTorch code to define a **simple GAN** for MNIST-like images (28x28 = 784 dims):
- Generator: takes noise vector (z_dim=100), outputs 784-dim. Use Linear, ReLU, Tanh at output.
- Discriminator: takes 784-dim, outputs probability (sigmoid). Use Linear, LeakyReLU.
- Write the generator loss expression: binary cross-entropy with all-ones labels (generator wants discriminator to output 1).
- Write the discriminator loss expression: real samples target 1, fake samples target 0.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain **mode collapse** in GANs: what it is, why it happens, and one technique to mitigate it.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Describe the **VAE loss function (ELBO)**. What are its two components, and what does each one enforce?

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A GAN trained on medical images produces sharp images but has a high FID score. What does this suggest, and what would you investigate?

**Answer key:** released by your instructor.

---

**Mapping:** CLO1, CLO6; notebooks: 04_building_training_simple_gan, 05_implementing_vae_image_generation, 08_evaluating_generative_models_fid_bleu.

**For:** AIAT 124 - Generative AI
