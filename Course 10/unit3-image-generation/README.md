# Unit 3: Image and Visual Generation

## AIAT 124 - Generative Artificial Intelligence

Unit training hours: 12

## What This Unit Teaches

Image generation in depth: implementing and applying VAEs for images, advanced
VAE topics, diffusion-based generation (a full DDPM you train and sample), and
how modern generators (StyleGAN, DALL-E, Stable Diffusion) build on those
foundations. All notebooks use PyTorch and run on CPU at classroom scale; a
GPU (or Google Colab — see `../DOCS/COLAB_SETUP.md`) is only needed to try the
full-size systems referenced in examples 04–05.

## Prerequisites

- Units 1–2 completed (GAN and VAE fundamentals)
- Comfortable with CNNs and image data in PyTorch

## Examples (do in order)

1. `examples/01_vae_implementation.ipynb` — Implementing a VAE for images,
   step by step.
2. `examples/02_vae_applications.ipynb` — VAE applications: denoising and
   anomaly detection hands-on, plus face-generation and style-transfer
   recipes.
3. `examples/03_vae_advanced_topics.ipynb` — Advanced VAE topics: conditional
   VAE, latent interpolation, and a β-VAE experiment.
4. `examples/04_image_generation_advanced.ipynb` — Advanced image generation:
   train and sample a DDPM diffusion model (Stable Diffusion's core).
5. `examples/05_generating_ai_images_stylegan_dalle.ipynb` — How StyleGAN,
   DALL-E, and Stable Diffusion work, mapped to the models you built.

## Exercise

- `exercises/01_vae_exercise.ipynb`

## Quiz

- `../QUIZZES/quiz_03.md`

Solutions and answer keys are released by your instructor.
