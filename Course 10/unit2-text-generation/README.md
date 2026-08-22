# Unit 2: Text and Language Generation

## AIAT 124 - Generative Artificial Intelligence

Unit training hours: 12

## What This Unit Teaches

Generating text with language models: GPT-style autoregressive generation,
fine-tuning language models, prompt engineering, text-to-text systems,
creative text generation, and evaluating output quality with BLEU and
perplexity. All notebooks run fully offline on small PyTorch models; the
fine-tuning and prompt-engineering notebooks additionally show the Hugging
Face `transformers` / OpenAI API workflows as clearly labeled reference code
(running those requires a model download or an API key).

## Prerequisites

- Unit 1 completed
- `transformers` optional (see `../START_HERE.md`) — only needed to run the
  reference workflows shown in notebooks 02 and 03

## Examples (do in order)

1. `examples/01_text_generation_gpt_models.ipynb` — Implementing text
   generation with GPT-style models.
2. `examples/02_fine_tuning_language_models.ipynb` — Fine-tuning: pretrain a
   small LM, fine-tune it on a new domain, and measure the improvement (plus
   the Hugging Face `Trainer` workflow as reference).
3. `examples/03_prompt_engineering_openai_huggingface.ipynb` — Prompt
   engineering strategies with a hands-on steering demo (OpenAI API and
   Hugging Face examples included as reference code).
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
