# Recommended Order for Example Notebooks
## Aligned with institution slides (Content folder)

Use this order so **examples** match the **slide sequence** you use in class.

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

*Then (optional):* `06_gpt_text_generation.ipynb`, `07_sequence_to_sequence.ipynb`, `08_text_generation_rnn_lstm_gru.ipynb`, `09_transformer_models_bert_gpt_nlp.ipynb`, `10_sentiment_analysis_translation_speech.ipynb`

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

*Then (optional):* `regularization_techniques_dropout_batch_normalization.ipynb`, `optimizing_deep_learning_models_using_regularization.ipynb`, `model_compression_for_edge_devices.ipynb`, `cloud_deployment_of_deep_learning_models.ipynb`

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
