# Recommended Order for Example Notebooks
## Aligned with institution slides (Content folder)

Use this order so **examples** match the **slide sequence** you use in class.

---

## How do I know what topics each notebook covers?

- **In each notebook:** Open any example notebook and look at the **first cell**. You will see a line **📌 Covers slide(s):** that lists which lecture slide(s) it goes with (e.g. *"**08** — Fundamentals of Deep Learning"*). Do that notebook after watching those slides so you don’t get confused.
- **In this document:** Use the tables below. Each row shows **Slide** (number), **Topic** (what the slide is about), and **Example notebook** (which file to run). So you can see at a glance which notebook has which topics without opening every file.

**Summary:** Every notebook states its topics/slides at the top; this doc gives you the full map in one place.

---

## Why 23 slides but a different number of examples?

- **The 23 slides** are lecture slides (theory/topics). They are numbered 01–23 but **presented in a different order** in class (e.g. Unit 1: 08 → 01 → 02 → 06 → 19 → 23). Slide numbers are IDs, not sequence.
- **One slide can cover more than one topic** (e.g. Slide 01: "Anatomy of NN, TensorFlow, layers, fit(), loss"). We often use **one notebook per slide** (or per main topic), but not always 1:1.
- **Sometimes one notebook is used for two slides** (e.g. Slide 04 AutoEncoders + Slide 09 GANs → same notebook `01_gans_and_autoencoders_vaes`; Slide 14 + 15 both Object Detection → `04_transfer_learning_object_detection`). So we can have **fewer** notebooks than slides for that unit.
- **Sometimes one slide maps to two notebooks** (e.g. Slide 20 Transfer Learning → `05_transfer_learning_cnns` and `06_pretrained_cnn_architectures`). So we can have **more** notebooks than slides.
- **Unit 5 has no slides** (0 of the 23). All Unit 5 examples (01–07) are for deployment/optimization with **no** slide counterpart. So the total number of **examples** (36 across units) is **not** 23: the 23 slides cover only Units 1–4; Unit 5 adds 7 more notebooks.

**Summary:** Slides = theory; examples = hands-on. The mapping is by **topic**, not by "one example per slide." Some slides share a notebook; some slides need two notebooks; Unit 5 has only notebooks.

---

## Unit 1: Deep Learning Basics  
**Slide order:** 08 → 01 → 02 → 06 → 19 → 23

| Step | Slide | Topic | Example notebook |
|------|-------|--------|-------------------|
| 1 | 08 | Fundamentals of Deep Learning (vs traditional ML) | `01_deep_learning_fundamentals_compared_to_traditional_ml.ipynb` |
| 2 | 01 | Anatomy of NN, TensorFlow, layers, fit(), loss | `02_simple_neural_network.ipynb` |
| 3 | 02 | ANNs, perceptron, MLP, activation functions, Keras | `03_perceptron_mlp_tensorflow_pytorch_setup.ipynb` |
| 4 | 06 | TensorFlow vs PyTorch, Colab, Jupyter | `03_perceptron_mlp_tensorflow_pytorch_setup.ipynb` *(same: setup/Colab)* |
| 5 | 19 | Perceptron, MLP, activation (revisit) | `04_activation_functions_and_optimization_algorithms.ipynb` |
| 6 | 23 | Keras: Sequential, Functional API, callbacks, TensorBoard | `02_simple_neural_network.ipynb` *(Keras Sequential)* or `05_backpropagation_detailed.ipynb` *(training flow)* |

**Recommended notebook sequence (filenames = order):**  
1. `01_deep_learning_fundamentals_compared_to_traditional_ml.ipynb`  
2. `02_simple_neural_network.ipynb`  
3. `03_perceptron_mlp_tensorflow_pytorch_setup.ipynb`  
4. `04_activation_functions_and_optimization_algorithms.ipynb`  
5. `05_backpropagation_detailed.ipynb`  
6. `06_optimization_techniques.ipynb`  

*Then (optional):* `07_image_processing_feature_extraction.ipynb`, `08_forward_and_backward_propagation.ipynb`

---

## Unit 2: CNNs  
**Slide order:** 05 → 10 → 16 → 14 → 15 → 11 → 20

| Step | Slide | Topic | Example notebook |
|------|-------|--------|-------------------|
| 1 | 05 | CNN Architecture (conv, pooling, fully connected) | `01_cnn_architecture.ipynb` |
| 2 | 10 | Image Processing Basics (pixels, CIFAR-10, augmentation) | `02_image_processing_fundamentals_and_feature_extraction.ipynb` |
| 3 | 16 | CNN Architectures (LeNet, AlexNet) | `03_cnn_advanced_architectures.ipynb` |
| 4 | 14 | Object Detection (Faster R-CNN, SSD) | `04_transfer_learning_object_detection.ipynb` |
| 5 | 15 | Object Detection (YOLO) | `04_transfer_learning_object_detection.ipynb` *(same notebook)* |
| 6 | 11 | Image Segmentation (Mask R-CNN, UNet) | `07_training_cnn_image_datasets.ipynb` *(image pipelines)* or *see README* |
| 7 | 20 | Transfer Learning (VGG, ResNet, fine-tuning) | `05_transfer_learning_cnns.ipynb`, then `06_pretrained_cnn_architectures.ipynb` |

**Recommended notebook sequence (filenames = order):**  
1. `01_cnn_architecture.ipynb`  
2. `02_image_processing_fundamentals_and_feature_extraction.ipynb`  
3. `03_cnn_advanced_architectures.ipynb`  
4. `04_transfer_learning_object_detection.ipynb`  
5. `05_transfer_learning_cnns.ipynb`  
6. `06_pretrained_cnn_architectures.ipynb`  
7. `07_training_cnn_image_datasets.ipynb`  

*Why 07 last?* Transfer learning (05, 06) comes before the full training pipeline (07) so you see pretrained reuse first; 07 then trains a CNN from scratch on CIFAR-10.

---

## Unit 3: RNNs & Transformers  
**Slide order:** 21 → 17 → 12 → 03 → 13

| Step | Slide | Topic | Example notebook |
|------|-------|--------|-------------------|
| 1 | 21 | Understanding Sequential Data | `01_understanding_sequential_data_and_time_series_prediction.ipynb` |
| 2 | 17 | RNNs, vanishing/exploding gradients | `02_rnn_basics.ipynb` |
| 3 | 12 | LSTM & GRU | `03_lstm_advanced.ipynb` |
| 4 | 03 | Attention Mechanism | `04_transformer_attention.ipynb` |
| 5 | 13 | Multi-Head Attention, BERT | `05_bert_finetuning.ipynb` |

**Recommended notebook sequence (filenames = order):**  
1. `01_understanding_sequential_data_and_time_series_prediction.ipynb`  
2. `02_rnn_basics.ipynb`  
3. `03_lstm_advanced.ipynb`  
4. `04_transformer_attention.ipynb`  
5. `05_bert_finetuning.ipynb`  

*Then (optional; do after 01–05; order among these doesn't matter):* `06_gpt_text_generation.ipynb`, `07_sequence_to_sequence.ipynb`, `08_text_generation_rnn_lstm_gru.ipynb`, `09_transformer_models_bert_gpt_nlp.ipynb`, `10_sentiment_analysis_translation_speech.ipynb`

---

## Unit 4: Advanced Deep Learning  
**Slide order:** 04 → 09 → 22 → 18 → 07

| Step | Slide | Topic | Example notebook |
|------|-------|--------|-------------------|
| 1 | 04 | AutoEncoders | `01_gans_and_autoencoders_vaes.ipynb` |
| 2 | 09 | GANs | `01_gans_and_autoencoders_vaes.ipynb` *(same notebook: GANs + AEs)* |
| 3 | 22 | Variational Autoencoders (VAE) | `02_implementing_a_vae_variational_autoencoder_for_anomaly_detection.ipynb` |
| 4 | 18 | Reinforcement Learning (DQN, policy gradients) | `03_reinforcement_learning_fundamentals_deep_q_networks_policy_gradients.ipynb` |
| 5 | 07 | Ethical Considerations (bias, fairness, XAI) | `04_ethical_concerns_in_ai_bias_fairness_interpretability.ipynb` |

**Recommended notebook sequence (filenames = order):**  
1. `01_gans_and_autoencoders_vaes.ipynb`  
2. `02_implementing_a_vae_variational_autoencoder_for_anomaly_detection.ipynb`  
3. `03_reinforcement_learning_fundamentals_deep_q_networks_policy_gradients.ipynb`  
4. `04_ethical_concerns_in_ai_bias_fairness_interpretability.ipynb`  

---

## Unit 5: Deployment  
**No institution slides.** Use the examples in numerical order:

**Recommended notebook sequence:**  
1. `01_model_optimization.ipynb`  
2. `02_tensorflow_serving.ipynb`  
3. `03_onnx_conversion.ipynb`  
4. `04_model_pruning.ipynb`  
5. `05_model_distillation.ipynb`  
6. `06_flask_fastapi_deployment.ipynb`  
7. `07_model_optimization_quantization.ipynb`  

---

## Summary

| Unit | Slide order | Example order (01_, 02_, … = file order) |
|------|-------------|--------------------------------------------|
| 1 | 08→01→02→06→19→23 | 01_deep_learning_fundamentals → 02_simple_nn → 03_perceptron_mlp → 04_activation_functions → 05_backprop → 06_optimization |
| 2 | 05→10→16→14→15→11→20 | 01_cnn → 02_image_processing → 03_cnn_advanced → 04_object_detection → 05_transfer → 06_pretrained → 07_training |
| 3 | 21→17→12→03→13 | 01_understanding_sequential → 02_rnn → 03_lstm → 04_transformer_attention → 05_bert |
| 4 | 04→09→22→18→07 | 01_gans_vaes → 02_vae_anomaly → 03_reinforcement_learning → 04_ethical_concerns |
| 5 | *(no slides)* | 01 → 02 → 03 → 04 → 05 → 06 → 07 (by file number) |

See also: `INSTITUTION_SLIDES_COMPATIBILITY.md` for full slide ↔ unit mapping.
