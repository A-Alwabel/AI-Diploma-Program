# Unit 1: Introduction to Generative AI

## AIAT 124 - Generative Artificial Intelligence

Unit training hours: 12

## What This Unit Teaches

Foundations of generative modeling: how generative models differ from
discriminative ones, probabilistic generative models, and the two core deep
generative architectures — VAEs and GANs — including training techniques,
evaluation metrics, and latent-space exploration. All notebooks use PyTorch;
several train on the MNIST data included in `examples/data/`.

## Prerequisites

- `Course 10/START_HERE.md` completed (environment set up, "ai-diploma" kernel)
- AIAT 122 — Deep Learning (Course 08): neural networks and training loops in
  PyTorch

## Examples (do in order)

1. `examples/01_generative_vs_discriminative.ipynb` — Generative vs
   discriminative models: what each learns and when to use which.
2. `examples/02_generative_model_comparison.ipynb` — Comparing families of
   generative models and their trade-offs.
3. `examples/03_probabilistic_generative_models.ipynb` — Probabilistic
   modeling: distributions, sampling, and likelihood.
4. `examples/04_implementing_vae_image_generation.ipynb` — Implementing a
   Variational Autoencoder for image generation.
5. `examples/05_building_training_simple_gan.ipynb` — Building and training a
   simple GAN in PyTorch.
6. `examples/06_conditional_gans.ipynb` — Conditional GANs: controlling what
   the generator produces.
7. `examples/07_stylegan_basics.ipynb` — StyleGAN basics: style-based
   generation concepts.
8. `examples/08_training_techniques_gradient_penalties.ipynb` — Stabilizing
   GAN training: gradient penalties and spectral normalization.
9. `examples/09_comparing_gan_vae_architectures.ipynb` — GANs vs VAEs:
   architecture and output comparison.
10. `examples/10_evaluating_generative_models_fid_bleu.ipynb` — Evaluating
    generative models with metrics such as FID and BLEU.
11. `examples/11_generating_samples_trained_models.ipynb` — Generating samples
    from trained generative models.
12. `examples/12_exploring_latent_spaces_interpolation.ipynb` — Exploring
    latent spaces and interpolation in VAEs.

## Exercise

- `exercises/01_generative_models_fundamentals_exercise.ipynb`

## Quiz

- `../QUIZZES/quiz_01.md`

Solutions and answer keys are released by your instructor.
