# Unit 2: CNNs for Images
## AIAT 122 - Deep Learning

## ✅ Prerequisites Checklist

Before starting this unit, confirm:

- [ ] Completed Unit 1: Introduction to Deep Learning and Neural Networks
- [ ] Comfortable with tensors and activation functions
- [ ] Understand basic image data formats
- [ ] Installed required libraries (`pip check` passes)
- [ ] Reviewed related topics (see course README and DOCS/EXAMPLES_ORDER.md; COURSE_MAP if available in your repo)

### Learning Objectives

By the end of this unit, students will be able to:
- Understand Convolutional Neural Networks
- Build CNNs for image classification
- Apply transfer learning
- Understand CNN architectures (LeNet, AlexNet, ResNet)
- Deploy CNN models

---

## Topics Covered

1. **CNN Fundamentals**
   - Convolution operation
   - Pooling layers
   - Feature maps
   - CNN architecture

2. **Image Classification**
   - Building CNN models
   - Training on image datasets
   - Data augmentation
   - Model evaluation

3. **Transfer Learning**
   - Using pre-trained models
   - Fine-tuning
   - Feature extraction
   - Popular architectures (VGG, ResNet, MobileNet)

4. **Advanced CNN Topics**
   - Object detection basics
   - Semantic segmentation introduction
   - CNN visualization

---

## Recommended order (examples)

**Do notebooks in this number order: 01 → 02 → 03 → … → 07.** (Slide numbers are topic IDs only—do **not** use them to decide order.) Full table: `DOCS/EXAMPLES_ORDER.md`.

1. `01_cnn_architecture.ipynb`  
2. `02_image_processing_fundamentals_and_feature_extraction.ipynb`  
3. `03_cnn_advanced_architectures.ipynb`  
4. `04_transfer_learning_object_detection.ipynb`  
5. `05_transfer_learning_cnns.ipynb`  
6. `06_pretrained_cnn_architectures.ipynb`  
7. `07_training_cnn_image_datasets.ipynb`  

**Why is 07 last?** We do transfer learning (05, 06) before the full "train from scratch" pipeline (07) so you see how to reuse pretrained models first; 07 then shows training a CNN from scratch on CIFAR-10.

**⏱ Long run:** Notebooks **04**, **05**, and **07** can take **10–40+ minutes** to run (downloads, transfer learning, or full training). Use a GPU (e.g. Colab) and a smaller subset or fewer epochs if you need a quicker demo.

---

## Exercises

Complete the exercise in `unit2-cnns/exercises/`:

1. **`01_cnn_exercise.ipynb`** – CNN for image classification. Aligns with `01_cnn_architecture.ipynb`, `05_transfer_learning_cnns.ipynb`, `07_training_cnn_image_datasets.ipynb`.

**Solutions:** See `DOCS/SOLUTIONS/exercises/` (instructor-only; do not distribute before deadline).

---

## Teaching note (instructors)

- **Suggested time:** Examples 01–07: ~2.5–3 hours in lab. Theory (slides): ~6 hours.
- **Demo notebook:** `01_cnn_architecture.ipynb` or `05_transfer_learning_cnns.ipynb` – show conv/pool structure or transfer learning flow.
- **Common stumbling block:** GPU memory on full CIFAR-10/ImageNet; use subset or smaller batch size; recommend Colab GPU (see `DOCS/COLAB_SETUP.md`).
- **Exercise alignment:** `01_cnn_exercise` builds on 01_cnn_architecture and transfer learning examples.

---

**Unit Duration:** 3 weeks  
**Difficulty:** Advanced  
**Prerequisites:** Unit 1 completion, understanding of neural networks

