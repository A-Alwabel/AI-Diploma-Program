# Unit 3: Applications of Generative AI

## AIAT 124 - Generative Artificial Intelligence

Unit training hours: 12

> The folder keeps its historical name `unit3-image-generation/`; the official unit
> title is **Applications of Generative AI**. In the delivered timetable this unit has
> one live 3-hour session, and that session is spent on lesson 06.

## What This Unit Teaches

Building a generative-AI application end to end, with your own hands: a
retrieval-augmented question answerer over a real corpus (this repository's own
markdown files), a labelled evaluation set scored against a no-retrieval baseline,
and a deliberate corpus-poisoning attack that is fixed structurally. That is lesson
06, and it is the unit's live session. It runs offline on CPU, with no API key.

Around it, as self-study: image generation in depth. Implementing and applying VAEs
for images, advanced VAE topics, diffusion-based generation (a full DDPM you train
and sample), and how modern generators (StyleGAN, DALL-E, Stable Diffusion) build on
those foundations. All notebooks use PyTorch and run on CPU at classroom scale; a
GPU (or Google Colab — see `../DOCS/COLAB_SETUP.md`) is only needed to try the
full-size systems referenced in examples 04–05.

## Prerequisites

- Units 1–2 completed (GAN and VAE fundamentals; Unit 2 lesson 04 for the
  retriever + generator pairing that lesson 06 builds)
- Course 07 Unit 2 (TF-IDF vectors; its enrichment E4 is the seed of lesson 06)
- Comfortable with CNNs and image data in PyTorch (examples 01–05)

## Examples

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

The live session is lesson 06. Do 01–05 as homework, in file order, around it.

1. **[HOMEWORK]** `examples/01_vae_implementation.ipynb` — Implementing a VAE for images,
   step by step.
2. **[HOMEWORK]** `examples/02_vae_applications.ipynb` — VAE applications: denoising and
   anomaly detection hands-on, plus face-generation and style-transfer
   recipes.
3. **[HOMEWORK]** `examples/03_vae_advanced_topics.ipynb` — Advanced VAE topics: conditional
   VAE, latent interpolation, and a β-VAE experiment.
4. **[HOMEWORK]** `examples/04_image_generation_advanced.ipynb` — Advanced image generation:
   train and sample a DDPM diffusion model (Stable Diffusion's core).
5. **[HOMEWORK]** `examples/05_generating_ai_images_stylegan_dalle.ipynb` — How StyleGAN,
   DALL-E, and Stable Diffusion work, mapped to the models you built.
6. **[CORE]** `examples/06_build_a_rag_question_answerer.ipynb` — Build a
   retrieval-augmented question answerer over this repository's own markdown,
   offline: chunk → TF-IDF retrieval → a composed answer with citations → an
   18-question evaluation set scored against a no-retrieval baseline → one
   poisoned document, cited, then blocked by a provenance gate. The unit's live
   session.

## Exercise

- `exercises/01_vae_exercise.ipynb`

## Quiz

- `../QUIZZES/quiz_03.md`

Solutions and answer keys are released by your instructor.
