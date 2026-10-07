# Quiz 02 – Unit 2: CNNs
## AIAT 122 - Deep Learning

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 2 (CNN architecture, convolution, pooling, transfer learning, image processing).  
**Concepts from:** Unit 2 examples 01 (CNN architecture), 02 (image processing), 05–07 (transfer learning, training) and related slides.  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What does a **convolutional layer** do in a CNN?

a) Applies learnable filters that slide over the image to detect local patterns (e.g. edges)  
b) Flattens the image to a vector  
c) Connects each pixel to each neuron in the next layer so that no spatial information is lost  
d) Shrinks the feature map by summarizing each window with a single value  

---

### Question 2 (10 points)
What is the main purpose of **max pooling**?

a) To increase the spatial dimensions of the feature map  
b) To learn a set of weights that selects the most informative pixels in each window  
c) To average the activations in each window so that the feature map is smoother  
d) To reduce spatial size, retain strong activations, and add translation invariance  

---

### Question 3 (10 points)
Why is **transfer learning** useful for image classification?

a) It makes models smaller  
b) We can use features learned on large datasets (e.g. ImageNet) and adapt them to our task with less data and training time  
c) The pre-trained weights can be reused as long as the new images belong to the same classes as the original dataset  
d) Re-training the pre-trained architecture from scratch on the new data converges faster because the design is already proven  

---

### Question 4 (10 points)
**Data augmentation** (e.g. random rotation, flip) for images is used to:

a) Make each epoch faster, since the network sees more images per pass  
b) Let the model fit the training set more closely by showing each image in several versions  
c) Increase effective dataset size and improve generalization by adding variation  
d) Replace the need for a validation set  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write code to build a **small CNN** for classifying 28×28 grayscale images (e.g. MNIST, 10 classes) in **either PyTorch or Keras/TensorFlow** (both are used in Unit 2; state which one you chose). Architecture:
- One convolutional layer (1 input channel, 32 filters, 3×3, ReLU), then 2×2 max pooling; flatten; a dense layer with 64 units and ReLU; an output layer with 10 units.
- PyTorch: `nn.Conv2d(1, 32, 3)` → `nn.MaxPool2d(2)` → `Flatten` → `nn.Linear(32*13*13, 64)` → `nn.Linear(64, 10)` (logits); show the full `nn.Module` class with `__init__` and `forward`.
- Keras/TensorFlow: `Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1))` → `MaxPooling2D((2, 2))` → `Flatten` → `Dense(64, relu)` → `Dense(10)` with a softmax output or `from_logits=True`.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Why do we use **convolutional layers** instead of only **fully connected (dense) layers** for images? Give two reasons.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
What is **fine-tuning** in transfer learning, and when would you freeze some layers instead of training all of them?

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
You train a CNN on **500 images** and get high training accuracy, but the model fails on new images with **different lighting or background**. What is likely going on, and what would you add or change (e.g. data, augmentation, or regularization)?

**Answer key:** released by your instructor.

---

**Mapping:** CLO2, CLO3; notebooks: 01_cnn_architecture, 05_transfer_learning_cnns, 06_pretrained_cnn_architectures.

**For:** AIAT 122 - Deep Learning
