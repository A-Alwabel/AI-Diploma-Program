# Curriculum traceability: Courses 08–11 vs `DETAILED_UNIT_DESCRIPTIONS.md`

**Generated:** 2026-03-29  
**Source of requirements:** `/DETAILED_UNIT_DESCRIPTIONS.md` (official PDF extract), sections **COURSE 8** through **COURSE 11**.  
**Repo paths:** `Course 08/` … `Course 11/`.

## How to read this document

| Status | Meaning |
|--------|---------|
| **Full** | Clear primary artifact(s): example or exercise notebook(s) implement or teach the item. |
| **Partial** | Covered in passing (markdown/theory cell), split across notebooks, or only named without hands-on depth. |
| **Gap** | No substantive `.ipynb` / exercise match found in systematic search; may still appear in slides or quizzes only. |

**Artifacts counted:** `**/examples/*.ipynb`, `**/exercises/*.ipynb`, unit `README.md`, `QUIZZES/*.md`, `ASSESSMENTS/Final_Exam.md`, `PROJECTS/`.  
**Not audited line-by-line:** every cell of every notebook; this is **keyword + path + spot-check** traceability.

**Repeatable scan:** Run `python3 DOCS/curriculum_traceability_scan.py` from the repo root for a short keyword report on common gap terms.

---

## Inventory (all four courses)

| Course | Units | Example `.ipynb` (approx.) | Exercise `.ipynb` / unit | Quizzes | Final exam | Projects folder |
|--------|-------|----------------------------|----------------------------|---------|------------|-----------------|
| 08 | 5 | U1:8, U2:7, U3:10, U4:4, U5:7 | 1–2 per unit (8 total) | 5 | Yes | 2 + template |
| 09 | 5 | U1:11, U2:11, U3:10, U4:7, U5:13 | 1 per unit | 5 | Yes | Yes |
| 10 | 5 | U1:18, U2:15, U3:12, U4:2+root, U5:4 | U1,U2,U3,U5: `exercises/`; U4: mixed | 5 | Yes | Yes |
| 11 | 5 | U1:17, U2:12, U3:6, U4:5, U5:14+ | 1 per unit | 5 | Yes | Yes |

---

## Course 08 (AIAT 122 – Deep Learning)

### CLOs → evidence

| CLO | Summary | Primary artifacts |
|-----|---------|-------------------|
| CLO1 | NN architectures, components | `unit1-deep-learning-basics/examples/01–08*.ipynb`, `03_perceptron_mlp…` |
| CLO2 | CNNs, vision | `unit2-cnns/examples/01–07*.ipynb`, `PROJECTS/Image_Classification_System/` |
| CLO3 | RNN/LSTM/GRU, sequential & NLP | `unit3-rnns-transformers/examples/01–10*.ipynb`, `PROJECTS/Sequence_or_Text_Project/` |
| CLO4 | Transfer learning | `unit2-cnns/examples/05_transfer_learning…`, `06_pretrained…`, `unit3/05_bert_finetuning.ipynb` |
| CLO5 | Regularization, optimization, deploy | `unit1/04,06`, `unit5/examples/*`, `unit5-deployment/exercises/01_*.ipynb` |

### Unit-by-unit (PDF bullets → status)

#### Unit 1 — Introduction to DL / ANNs

| PDF topic (abbrev.) | Status | Evidence |
|---------------------|--------|----------|
| DL vs ML, applications | Full | `01_deep_learning_fundamentals_compared_to_traditional_ml.ipynb` |
| Perceptron, MLP, activations | Full | `03_perceptron_mlp…`, `04_activation_functions…` |
| Forward/backprop, SGD/Adam/RMSprop | Full | `05_backpropagation_detailed.ipynb`, `06_optimization_techniques.ipynb` (RMSprop in “Try it”) |
| TensorFlow & PyTorch setup | Full | Notebooks use Keras/TF and/or PyTorch patterns across units |
| Practical: MNIST-style training | Full | `02_simple_neural_network.ipynb` |

#### Unit 2 — CNNs

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Image fundamentals, augmentation | Full | `02_image_processing_fundamentals…` |
| Conv / pool / FC | Full | `01_cnn_architecture.ipynb` |
| LeNet–Inception, pretrained | Full | `03_cnn_advanced_architectures.ipynb`, `06_pretrained_cnn_architectures.ipynb` |
| Object detection (YOLO, SSD, Faster R-CNN) | Partial | `04_transfer_learning_object_detection.ipynb` (concepts + pipeline; not full YOLO training) |
| Segmentation (U-Net, Mask R-CNN) | Partial | `07_training_cnn_image_datasets.ipynb` references segmentation slide; **no** dedicated U-Net / Mask R-CNN notebook (keyword scan: no “U-Net” / “Mask R-CNN” in sources) |
| Confusion matrix, ROC, AUC | Partial | Confusion matrix: e.g. `02_image_processing…` — **ROC/AUC:** no `roc_curve` / `roc_auc` in Course 08 notebooks (gap for *hands-on ROC*) |
| CIFAR / ImageNet-scale practice | Partial | **CIFAR-10:** `07_training_cnn_image_datasets.ipynb`; ImageNet discussed via pretrained weights, not full training |
| Transfer learning for detection | Partial | `04_transfer_learning_object_detection.ipynb`, `05_transfer_learning_cnns.ipynb` |

#### Unit 3 — RNNs & Transformers

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Sequential data, time series | Full | `01_understanding_sequential_data…` |
| RNN, vanishing gradients | Full | `02_rnn_basics.ipynb` |
| LSTM, GRU, text generation | Full | `03_lstm_advanced.ipynb`, `08_text_generation_rnn_lstm_gru.ipynb` |
| Attention, Transformers, BERT, GPT | Full | `04_transformer_attention.ipynb`, `09_transformer_models_bert_gpt_nlp.ipynb`, `05_bert_finetuning.ipynb`, `06_gpt_text_generation.ipynb` |
| Sentiment, translation, seq2seq | Full | `10_sentiment_analysis_translation_speech.ipynb`, `07_sequence_to_sequence.ipynb` |
| Speech recognition (hands-on) | Partial | `10_sentiment…` documents ASR pipeline API; **focus is sentiment** for runtime |

#### Unit 4 — Advanced DL

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| GANs | Full | `01_gans_and_autoencoders_vaes.ipynb` |
| VAEs, anomaly detection | Full | `02_implementing_a_vae…` |
| RL fundamentals, DQN, policy gradients | Partial | `03_reinforcement_learning_fundamentals…` — **Course-level** intro; **deep RL** is Course 09 |
| Transfer learning, ethics | Full | BERT/finetuning in U3; `04_ethical_concerns_in_ai…` |

#### Unit 5 — Optimization & deployment

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Regularization, hyperparameters | Full | `02_regularization_hyperparameter_tuning.ipynb`, `03_dropout_batchnorm.ipynb` |
| Pruning, quantization | Full | `04_model_pruning.ipynb`, `01_model_optimization.ipynb`, `07_model_optimization_quantization.ipynb` |
| ONNX, SavedModel, serving | Full | `05_onnx_conversion.ipynb`, `06_flask_fastapi_deployment.ipynb`, `03_tensorflow_serving_basic.ipynb` |
| Cloud (AWS/GCP/Azure) | Partial | Notebooks may reference cloud; **hands-on** is lighter than dedicated cloud course (see Course 11) |
| TensorFlow Lite, mobile | Full | `unit5-deployment/examples/07_model_optimization_quantization.ipynb` (Keras → TFLite, FP16 sample inference) |
| End-to-end project | Full | `PROJECTS/*`, `unit5-deployment/exercises/01_deep_learning_model_deployment_exercise.ipynb` |

---

## Course 09 (AIAT 123 – Reinforcement Learning)

### CLOs → evidence

| CLO | Summary | Primary artifacts |
|-----|---------|-------------------|
| CLO1 | MDPs, fundamentals | `unit1-rl-fundamentals/examples/*`, exercise `01_rl_fundamentals_and_mdps_exercise.ipynb` |
| CLO2 | Q-learning, SARSA | `unit2-policy-value/examples/01_q_learning.ipynb`, `02_sarsa_algorithm.ipynb`, exercises |
| CLO3 | Policy gradients | `unit2-policy-value/examples/03_policy_gradient_basics.ipynb` |
| CLO4 | DQN, A2C, PPO | `unit3-deep-rl/examples/01_dqn_implementation.ipynb`, `02_actor_critic.ipynb`, `03_ppo_algorithm.ipynb` |
| CLO5 | Exploration–exploitation | `unit4-exploration-exploitation/examples/*`, exercise `02_exploration_exercise.ipynb` |
| CLO6 | Applications | `unit5-applications/examples/*`, `PROJECTS/RL_Game_Agent/` |

### Unit-by-unit

#### Unit 1

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Gymnasium/Gym setup, MDPs, Bellman, value iteration | Full | `04_openai_gym_setup.ipynb`, `01_mdp_example.ipynb`, `02_mdp_solving.ipynb`, `03_value_iteration.ipynb` |
| ε-greedy, UCB, Thompson | Partial | ε-greedy: U1 examples; **Thompson:** `unit4/02_balancing_exploration.ipynb`, `04_comparing_exploration_methods.ipynb` (PDF lists Thompson in **U1 theory**; hands-on is **U4**) |
| CartPole, FrozenLake, Q-learning, DQN “mini projects” | Partial | CartPole/FrozenLake + Q-learning: **Full** in U1/U2; **DQN** primarily **Unit 3** notebooks |

#### Unit 2

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| DP, Monte Carlo, TD(0), n-step | Full | `04_monte_carlo_value_estimation.ipynb`, `05_td_algorithms_td0_nstep.ipynb`, policy/value iteration comparison `06_policy_vs_value_iteration_comparison.ipynb` |
| Q-learning, SARSA, Gym | Full | `01_q_learning.ipynb`, `applying_q_learning_and_sarsa…`, `02_sarsa_algorithm.ipynb` |

#### Unit 3

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| DQN, replay, target nets | Full | `01_dqn_implementation.ipynb`, `05_optimization_experience_replay_reward_shaping.ipynb` |
| Policy gradient, REINFORCE | Partial | **REINFORCE** not matched as a literal lesson title; **policy gradient** via `unit2/03_policy_gradient_basics.ipynb` + actor–critic in U3 |
| A2C, PPO | Full | `02_actor_critic.ipynb`, `03_ppo_algorithm.ipynb` |
| **DDPG** | **Gap** | No `DDPG` string in Course 09 `.ipynb` sources (full-tree keyword scan) |
| Applications, challenges | Partial | Multiple overview notebooks; **intrinsic motivation / curriculum learning** not found by keyword scan |

#### Unit 4

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| ε-greedy, Boltzmann, Thompson, UCB | Full | `01_exploration_strategies.ipynb`, `02_balancing_exploration.ipynb`, `03_adaptive_exploration_ucb.ipynb`, `04_comparing_exploration_methods.ipynb`, `05_tuning_exploration_parameters.ipynb` |
| Intrinsic motivation, RND, Bayesian optimization | Gap / Partial | Not found as dedicated hands-on notebooks in keyword pass |

#### Unit 5

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Multi-agent, hierarchical, model-based, goal-conditioned | Full | Multiple `unit5-applications/examples/*` (e.g. `04_multi_agent_rl.ipynb`, `05_hierarchical_rl_options.ipynb`, `06_model_based_rl_world_models.ipynb`, `08_goal_conditioned_rl.ipynb`) |

---

## Course 10 (AIAT 124 – Generative AI)

### CLOs → evidence

| CLO | Summary | Primary artifacts |
|-----|---------|-------------------|
| CLO1 | GANs, VAEs, diffusion | `unit1/*`, `unit3/01_vae…`, `02_image_generation_advanced.ipynb` (Stable Diffusion) |
| CLO2 | Text / Transformers | `unit2-text-generation/examples/*` |
| CLO3 | Image generation | `unit3-image-generation/examples/*` |
| CLO4 | Audio / music | `unit5-future-trends/examples/03_music_generation.ipynb`, `05_audio_voice_synthesis_wavenet_jukebox.ipynb` (**PDF Unit 3 practical** lists audio; **repo places much of this in Unit 5**) |
| CLO5 | Ethics | `unit4-ethics-regulations/*` |
| CLO6 | Metrics FID, BLEU, perplexity | `unit1/08_evaluating_generative_models_fid_bleu.ipynb`, `unit2/09_evaluating_text_quality_bleu_perplexity.ipynb` |
| CLO7 | Applications / project | `PROJECTS/Generative_AI_Application/` |

### Structural note (PDF vs folders)

- **Unit 4** ethics: several notebooks live under `unit4-ethics-regulations/` **root** (e.g. `01_generative_ai_ethics_exercise.ipynb`), not only under `exercises/`. Students should read **`unit4-ethics-regulations/README.md`** for order.

### Unit-by-unit

#### Unit 1

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Discriminative vs generative, VAE, GAN variants, FID/BLEU, training stability | Full | Multiple `unit1-generative-fundamentals/examples/*` including `08_evaluating_generative_models_fid_bleu.ipynb`, StyleGAN/WGAN topics |

#### Unit 2

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| GPT, beam search, T5, prompting, OpenAI / HF | Full | `06_prompt_engineering_openai_huggingface.ipynb`, `07_building_text_to_text_generation.ipynb` (T5), etc. |

#### Unit 3 (PDF includes image + audio + code-gen bullets)

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| StyleGAN, Stable Diffusion, DALL-E | Full | `04_generating_ai_images_stylegan_dalle.ipynb`, `02_image_generation_advanced.ipynb`, related notebooks |
| Deepfakes | Partial | `unit4/02_deepfake_detection.ipynb` (ethics unit) |
| **Pix2Pix / CycleGAN** (explicit) | **Gap** | No keyword hit in `.ipynb` sources for “Pix2Pix” / “CycleGAN” (style transfer appears in VAE context in `02_vae_applications.ipynb`, not full CycleGAN) |
| Audio, WaveNet, Jukebox, music | Partial | Strong in **Unit 5** (`05_audio_voice_synthesis_wavenet_jukebox.ipynb`, `03_music_generation.ipynb`) — **unit placement ≠ PDF Unit 3 only** |
| Codex / Copilot | Full | `06_code_generation_openai_codex_copilot.ipynb`, `applying_models_like_openai_codex…` |

#### Unit 4 — Ethics & regulation

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Bias, deepfakes, IP, GDPR, governance | Full | `01_generative_ai_ethics.ipynb`, `02_deepfake_detection.ipynb`, `examples/building_ethical_ai…`, `applying_ai_regulatory_guidelines…` |

#### Unit 5 — Future trends

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Multimodal, CLIP-level, AlphaFold | Partial | Multimodal / creative apps: several notebooks — **CLIP / AlphaFold** no keyword hits in notebook sources |
| Advanced diffusion, creative applications | Full | `05_experimenting_advanced_generative_models.ipynb`, music/image notebooks |

---

## Course 11 (AIAT 125 – Deploying AI Models)

### CLOs → evidence

| CLO | Summary | Primary artifacts |
|-----|---------|-------------------|
| CLO1 | Deployment lifecycle | `unit1-deployment-basics/examples/*`, README |
| CLO2 | Package / serialize | `02_model_packaging.ipynb`, `04_saving_loading_models_pickle_onnx.ipynb`, Pickle/ONNX exercises |
| CLO3 | APIs | `02_fastapi_deployment.ipynb`, `01_flask_api_deployment.ipynb`, exercises |
| CLO4 | Cloud | `unit3-cloud-deployment/examples/*` (AWS, Azure, GCP notebooks) |
| CLO5 | Docker, Kubernetes | `unit4-containers-orchestration/examples/*` |
| CLO6 | Monitoring, MLOps | `unit5-pipelines-monitoring/examples/*`, MLflow / drift / canary notebooks |

### Unit-by-unit

#### Units 1–2

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Pickle, ONNX, SavedModel, PMML | Full / Partial | Pickle, ONNX, SavedModel: **Full** — `04_saving_loading_models_pickle_onnx.ipynb` (mentions PMML), packaging exercises |
| REST, gRPC | Partial | REST: **Full** — Flask/FastAPI notebooks; **gRPC:** mentioned in `unit2-versioning-serving/examples/05_tensorflow_serving_torchserve.ipynb` — typically **not** a full gRPC lab |
| TensorFlow Serving, TorchServe, MLflow | Full | `05_tensorflow_serving_torchserve.ipynb`, `03_model_versioning.ipynb` (MLflow) |
| **Kafka / RabbitMQ streaming inference** | **Gap** | No matches in Course 11 `.ipynb` sources for Kafka or RabbitMQ |

#### Unit 3

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| AWS SageMaker, GCP Vertex, Azure ML | Full | `02_aws_sagemaker.ipynb`, `04_gcp_vertex_ai.ipynb`, `03_azure_ml_deployment.ipynb`, security/monitoring companions |

#### Unit 4

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Docker, Kubernetes | Full | `01_docker_deployment.ipynb`, `02_kubernetes_deployment.ipynb` |
| CI/CD, GitHub Actions, Jenkins | Partial | `04_cicd_pipelines.ipynb` — **conceptual / print-based** walkthrough; not a full working Actions/Jenkins lab in-repo |

#### Unit 5

| PDF topic | Status | Evidence |
|-----------|--------|----------|
| Monitoring, drift, MLflow, W&B, retraining, A/B, canary | Full | `01_model_monitoring.ipynb`, `04_drift_detection.ipynb`, `05_experiment_tracking_mlflow_wandb.ipynb`, `07_ab_testing_canary_deployment.ipynb`, `02_retraining_pipeline.ipynb`, plus parallel long-title notebooks |

---

## Cross-cutting: PDF metadata vs course README

| Item | `DETAILED_UNIT_DESCRIPTIONS.md` | Course README (09 / 11) |
|------|----------------------------------|-------------------------|
| Course 9 total hours | **80** (32 + 48) | States **96** — **discrepancy** |
| Course 11 total hours | **80** (32 + 48) | States **96** — **discrepancy** |

Align README tables with the official PDF extract **or** update the extract if the institution changed hours.

---

## Summary: gap list (actionable)

| ID | Course | Item | Suggested fix |
|----|--------|------|----------------|
| G1 | 08 | Hands-on ROC/AUC | Add short notebook section or notebook using `sklearn.metrics.roc_curve` / `RocCurveDisplay` on CNN or tabular logits |
| G2 | 08 | U-Net / Mask R-CNN practical | Optional notebook or link out + exercise stub |
| G3 | 09 | DDPG | Add `examples/04_ddpg.ipynb` (e.g. Pendulum/BipedalWalker with stable-baselines3 or raw PyTorch) |
| G4 | 09 | Intrinsic motivation / RND / curriculum | Optional advanced notebook or reading + quiz items |
| G5 | 10 | Pix2Pix / CycleGAN explicit lab | Add notebook or clarify in README that VAE style transfer substitutes partial coverage |
| G6 | 10 | CLIP / AlphaFold | Add short “concepts + links” notebook or expand Unit 5 multimodal notebook |
| G7 | 11 | Kafka/RabbitMQ streaming | Add conceptual notebook or integrate one messaging demo |
| G8 | 11 | CI/CD hands-on | Extend `04_cicd_pipelines.ipynb` with minimal GitHub Actions YAML example |
| G9 | 09/11 | Hour totals | Reconcile README vs `DETAILED_UNIT_DESCRIPTIONS.md` |
| G10 | 10 | Unit 4 exercise layout | Move root `*_exercise.ipynb` into `exercises/` or document clearly in README |

---

## Maintenance

1. After adding notebooks, re-run `python3 DOCS/curriculum_traceability_scan.py`.  
2. Update this file’s **Generated** date and any rows whose status changed.  
3. Treat **Full** as the bar for “PDF practical line fully mirrored”; **Partial** is acceptable for breadth-first curricula if documented.

---

*End of traceability matrix.*
