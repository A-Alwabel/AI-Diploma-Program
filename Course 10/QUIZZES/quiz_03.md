# Quiz 03 – Unit 3: Image and Visual Generation
## AIAT 124 - Generative AI

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 3 (diffusion models, StyleGAN, latent diffusion, style transfer via latent blending).
**Concepts from:** Unit 3 examples 04 (advanced image generation: diffusion) and 05 (StyleGAN, DALL-E, Stable Diffusion) and related slides.
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
**Denoising Diffusion Probabilistic Models (DDPM)** generate images by:

a) Directly mapping noise to images in one step
b) Only removing Gaussian noise from existing images
c) Using a GAN discriminator
d) Learning to reverse a forward noising process — gradually denoising a random noise sample step-by-step to produce a clean image

---

### Question 2 (10 points)
**StyleGAN** is notable for:

a) Generating text descriptions of images
b) Separating high-level style (pose) from fine-level detail, enabling controllable style mixing and interpolation in latent space
c) Working only on face generation
d) Requiring no training data

---

### Question 3 (10 points)
**Stable Diffusion** is a **latent diffusion model**, meaning:

a) Diffusion happens in pixel space
b) It uses GANs for generation
c) Diffusion happens in a compressed latent space (encoded by a VAE), making it far more computationally efficient than pixel-space diffusion
d) It does not support text conditioning

---

### Question 4 (10 points)
**Style transfer via latent blending** with a VAE (unit example 02) works by:

a) Encoding two images into latent vectors, interpolating (blending) between the two codes, and decoding the blend into an image with mixed attributes
b) Training a GAN to copy painting styles
c) Using a classifier to identify art styles
d) Fine-tuning a ResNet

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write PyTorch code to implement the **DDPM forward noising process**:
- Given clean image x0 of shape (1,1,28,28).
- Define: betas = torch.linspace(0.0001, 0.02, 1000), alphas = 1 - betas, alphas_cumprod = torch.cumprod(alphas, 0).
- Write q_sample(x0, t): returns x_t = sqrt(alphas_cumprod[t]) * x0 + sqrt(1 - alphas_cumprod[t]) * noise.
- Apply q_sample at t=0, t=500, t=999 and describe what you expect to see.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Unit example 04 builds a **DDPM**. Explain (a) the **reverse (denoising) process** the trained network performs at sampling time, (b) why the network is trained to **predict the added noise** rather than the clean image directly, and (c) what the fixed **forward noising process** contributes to that training.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
What is a **U-Net** architecture, and why is it well-suited as the denoiser in diffusion models?

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A team wants to generate realistic medical scan images to augment a small dataset. Compare **GAN vs diffusion model** for this task: quality, training stability, and control trade-offs.

**Answer key:** released by your instructor.

---

**Mapping:** CLO3; notebooks: 04_image_generation_advanced.

**For:** AIAT 124 - Generative AI
