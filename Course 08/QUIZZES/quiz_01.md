# Quiz 01 – Unit 1: Deep Learning Basics
## AIAT 122 - Deep Learning

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 1 (neural networks, backpropagation, optimization, activation functions).  
**Concepts from:** Unit 1 examples 02 (simple NN), 05 (backprop), 06 (optimization) and related slides.  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What is the main advantage of deep neural networks over shallow (single hidden layer) networks?

a) Each extra layer lowers the training loss further, since more parameters mean a closer fit  
b) They require less data  
c) They can learn hierarchical representations and complex non-linear patterns  
d) They are easier to optimize, because the gradient has more layers to flow through  

---

### Question 2 (10 points)
What is the role of the loss function during training?

a) To measure how wrong the model’s predictions are and guide gradient updates  
b) To initialize the weights  
c) To choose the learning rate  
d) To report the percentage of predictions the model got right after each epoch  

---

### Question 3 (10 points)
Which statement about backpropagation is correct?

a) It computes the activations and the loss for each mini-batch, layer by layer from input to output  
b) It replaces the need for an optimizer  
c) It computes the gradient at the output layer and copies that same value back to each earlier layer  
d) It computes gradients of the loss with respect to the weights using the chain rule  

---

### Question 4 (10 points)
Why do we use activation functions (e.g. ReLU) in hidden layers?

a) To turn the hidden layer’s outputs into class probabilities that sum to 1  
b) To introduce non-linearity so the network can learn complex functions  
c) To squash each activation into the range 0 to 1 so that the gradients stay stable  
d) To normalize the inputs  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write code to build a **2-layer feedforward neural network** for **MNIST digit classification** (10 classes) in **either PyTorch or Keras/TensorFlow** (both are used in Unit 1; state which one you chose). Requirements:
- Input size 784 (flattened 28×28); one hidden layer with 128 units and ReLU activation; output layer with 10 units.
- PyTorch: define a class `SimpleNN` inheriting from `nn.Module` with `__init__` and `forward`; output logits (no softmax) and name the matching loss (`CrossEntropyLoss`).
- Keras/TensorFlow: build the equivalent `Sequential` model (`Flatten` → `Dense(128, relu)` → `Dense(10)`) and name the matching loss (`sparse_categorical_crossentropy`, with a softmax output or `from_logits=True`).

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain what **overfitting** is and name **one** technique to reduce it in deep learning.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Describe the **training loop** in one sentence each: what happens in the forward pass, and what happens after the loss is computed (backward pass and update).

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A model achieves **99% training accuracy** and **70% validation accuracy**. What is the likely problem, and **one** concrete step you would take to address it?

**Answer key:** released by your instructor.

---

**Mapping:** CLO1 (explain concepts); notebooks: 02_simple_neural_network, 05_backpropagation_detailed, 06_optimization_techniques.

**For:** AIAT 122 - Deep Learning
