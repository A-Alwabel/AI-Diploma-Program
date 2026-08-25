# Unit 4 — Advanced Deep Learning Techniques
## AIAT 122 — Deep Learning

Unit training hours: 14 (of 64 total)

## Prerequisites

- Units 1–3 (training networks; CNNs; sequence models).
- Environment set up (see `../START_HERE.md`): "ai-diploma" kernel for PyTorch notebooks, "tfenv" kernel for TensorFlow notebooks.

## What this unit teaches

Generative models — GANs (generator vs discriminator) and autoencoders/VAEs (latent spaces, anomaly detection); reinforcement learning fundamentals (reward-based learning, Deep Q-Networks, policy gradients); and ethical concerns in deep learning: dataset bias, fairness metrics, and interpretability.

## Examples (do in file order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

Run the notebooks in `examples/` in this order:

1. **[CORE]** `01_gans_and_autoencoders_vaes.ipynb` — GANs and autoencoders/VAEs: how generative models learn to produce data.
2. **[CORE]** `02_implementing_a_vae_variational_autoencoder_for_anomaly_detection.ipynb` — build a VAE and use reconstruction error to flag anomalies.
3. **[CORE]** `03_reinforcement_learning_fundamentals_deep_q_networks_policy_gradients.ipynb` — rewards, DQN, and policy gradients (uses `gymnasium`).
4. **[CORE]** `04_ethical_concerns_in_ai_bias_fairness_interpretability.ipynb` — measure bias and fairness; interpret model decisions.

Note: GAN/VAE training in 01–02 can take several minutes; a GPU helps (see `../DOCS/COLAB_SETUP.md`). The ethics notebook audits a classifier trained on the real Titanic manifest (`Course 04/datasets/raw/titanic.csv`), where the group disparity is historical fact rather than injected by the code.

## Exercises

- `exercises/01_gans_vaes_exercise.ipynb` — build a simple GAN or VAE (pairs with examples 01–02).
- `exercises/02_reinforcement_learning_exercise.ipynb` — solve an environment with RL (pairs with example 03).

Solutions are released by your instructor.

## Quiz

- `../QUIZZES/quiz_04.md`

## Next

Unit 5: `../unit5-deployment/README.md`
