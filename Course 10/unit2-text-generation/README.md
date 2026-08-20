# Unit 2: Text and Language Generation

## AIAT 124 - Generative Artificial Intelligence

Unit training hours: 12

## What This Unit Teaches

Generating text with language models: GPT-style autoregressive generation,
fine-tuning language models, prompt engineering, text-to-text systems,
creative text generation, and evaluating output quality with BLEU and
perplexity. Notebook 02 uses Hugging Face `transformers`; the
prompt-engineering notebook can optionally use the OpenAI API (the `openai`
package plus an API key), but also works without it.

## Prerequisites

- Unit 1 completed
- `transformers` installed (see `../START_HERE.md`)

## Examples (do in order)

1. `examples/01_text_generation_gpt_models.ipynb` — Implementing text
   generation with GPT-style models.
2. `examples/02_fine_tuning_language_models.ipynb` — Fine-tuning a language
   model for a specific task (uses Hugging Face `transformers`).
3. `examples/03_prompt_engineering_openai_huggingface.ipynb` — Prompt
   engineering with the OpenAI API or Hugging Face Transformers (`openai`
   package optional).
4. `examples/04_building_text_to_text_generation.ipynb` — Building a
   text-to-text generation system with Transformers.
5. `examples/05_generating_creative_text_stories_poems.ipynb` — Generating
   creative text: stories and poems.
6. `examples/06_evaluating_text_quality_bleu_perplexity.ipynb` — Evaluating
   text generation quality with BLEU and perplexity.

## Exercise

- `exercises/01_gan_exercise.ipynb` — GAN practice exercise (generating
  realistic faces), reinforcing Unit 1 skills.

## Quiz

- `../QUIZZES/quiz_02.md`

Solutions and answer keys are released by your instructor.
