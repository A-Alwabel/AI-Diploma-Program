# Quiz 02 – Unit 2: CNNs
## AIAT 122 - Deep Learning

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 2 (CNN architecture, convolution, pooling, transfer learning, image processing).  
**Concepts from:** Unit 2 examples 01 (CNN architecture), 02 (image processing), 05–07 (transfer learning, training) and related slides.  
**Answers and rubrics:** Instructor only — see `DOCS/SOLUTIONS/quizzes/`.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What does a **convolutional layer** do in a CNN?

a) Flattens the image to a vector  
b) Applies learnable filters that slide over the image to detect local patterns (e.g. edges)  
c) Reduces the number of parameters by removing layers  
d) Only works on 1D data  

---

### Question 2 (10 points)
What is the main purpose of **max pooling**?

a) To increase the spatial dimensions of the feature map  
b) To reduce spatial size, retain strong activations, and add translation invariance  
c) To add more parameters  
d) To replace convolution  

---

### Question 3 (10 points)
Why is **transfer learning** useful for image classification?

a) It makes models smaller  
b) We can use features learned on large datasets (e.g. ImageNet) and adapt them to our task with less data and training time  
c) It removes the need for a GPU  
d) It only works for text  

---

### Question 4 (10 points)
**Data augmentation** (e.g. random rotation, flip) for images is used to:

a) Speed up training  
b) Increase effective dataset size and improve generalization by adding variation  
c) Reduce model size  
d) Replace the need for a validation set  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write code to build a **small CNN** in **PyTorch** for image classification with:
- One `nn.Conv2d` layer (1 input channel, 32 filters, 3×3, ReLU), then `nn.MaxPool2d(2)`.
- `Flatten`, then one `nn.Linear(32*13*13, 64)` with ReLU, then `nn.Linear(64, 10)` (logits).
- Input shape suitable for 28×28 grayscale images (e.g. MNIST).
- Show the full `nn.Module` class with `__init__` and `forward` methods.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_02_solution.md`.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Why do we use **convolutional layers** instead of only **fully connected (dense) layers** for images? Give two reasons.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_02_solution.md`.

---

### Question 7 (15 points)
What is **fine-tuning** in transfer learning, and when would you freeze some layers instead of training all of them?

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_02_solution.md`.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
You train a CNN on **500 images** and get high training accuracy, but the model fails on new images with **different lighting or background**. What is likely going on, and what would you add or change (e.g. data, augmentation, or regularization)?

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_02_solution.md`.

---

**Mapping:** CLO2, CLO3; notebooks: 01_cnn_architecture, 05_transfer_learning_cnns, 06_pretrained_cnn_architectures.

**For:** AIAT 122 - Deep Learning
