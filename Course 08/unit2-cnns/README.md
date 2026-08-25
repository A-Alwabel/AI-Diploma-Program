# Unit 2 — Convolutional Neural Networks (CNNs) for Computer Vision
## AIAT 122 — Deep Learning

Unit training hours: 12 (of 64 total)

## Prerequisites

- Unit 1 (neural networks, activation functions, training basics).
- Environment set up (see `../START_HERE.md`): "ai-diploma" kernel for PyTorch notebooks, "tfenv" kernel for TensorFlow notebooks.

## What this unit teaches

How CNNs process images: convolution, pooling, and feature maps; classic and advanced architectures (LeNet, AlexNet, ResNet); transfer learning with pretrained models; object detection basics; training CNNs on real image datasets with augmentation.

## Examples (do in file order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

Run the notebooks in `examples/` in this order:

1. **[CORE]** `01_cnn_architecture.ipynb` — convolution, pooling, and fully connected layers; a first CNN.
2. **[HOMEWORK]** `02_image_processing_fundamentals_and_feature_extraction.ipynb` — pixels, channels, normalization, and augmentation.
3. **[HOMEWORK]** `03_cnn_advanced_architectures.ipynb` — classic architectures (LeNet, AlexNet) and what changed between them.
4. **[HOMEWORK]** `04_transfer_learning_object_detection.ipynb` — object detection concepts (Faster R-CNN, SSD, YOLO) with pretrained backbones.
5. **[CORE]** `05_transfer_learning_cnns.ipynb` — reuse a pretrained CNN: freeze layers and fine-tune.
6. **[HOMEWORK]** `06_pretrained_cnn_architectures.ipynb` — compare pretrained architectures (VGG, ResNet, MobileNet).
7. **[HOMEWORK]** `07_training_cnn_image_datasets.ipynb` — train a CNN from scratch on CIFAR-10; full pipeline.

Note: notebooks 04, 05, and 07 involve downloads and training runs that can take tens of minutes on CPU — use a GPU (e.g. Colab, see `../DOCS/COLAB_SETUP.md`) or reduce epochs/data for a quicker pass.

## Exercise

- `exercises/01_cnn_exercise.ipynb` — build a CNN image classifier (from scratch or via transfer learning). Solutions are released by your instructor.

## Quiz

- `../QUIZZES/quiz_02.md`

## Next

Unit 3: `../unit3-rnns-transformers/README.md`
