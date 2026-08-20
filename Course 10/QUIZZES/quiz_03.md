# Quiz 03 – Unit 3: Image and Visual Generation
## AIAT 124 - Generative AI

**Time Limit:** 45 minutes
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)
**Covers:** Unit 3 (diffusion models, StyleGAN, image-to-image translation, style transfer).
**Concepts from:** Unit 3 examples 02 (image generation advanced) and related slides.
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
**Denoising Diffusion Probabilistic Models (DDPM)** generate images by:

a) Directly mapping noise to images in one step
b) Learning to reverse a forward noising process — gradually denoising a random noise sample step-by-step to produce a clean image
c) Using a GAN discriminator
d) Only removing Gaussian noise from existing images

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
b) Diffusion happens in a compressed latent space (encoded by a VAE), making it far more computationally efficient than pixel-space diffusion
c) It uses GANs for generation
d) It does not support text conditioning

---

### Question 4 (10 points)
**Neural style transfer** works by:

a) Training a GAN to copy painting styles
b) Optimizing an input image to match the content of one image and the style (Gram matrix statistics) of another
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
Explain the difference between **Pix2Pix** (paired) and **CycleGAN** (unpaired) image-to-image translation. When would you use each?

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

**Mapping:** CLO3; notebooks: 02_image_generation_advanced.

**For:** AIAT 124 - Generative AI
