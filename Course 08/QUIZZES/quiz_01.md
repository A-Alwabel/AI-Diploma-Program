# Quiz 01 – Unit 1: Deep Learning Basics
## AIAT 122 - Deep Learning

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 1 (neural networks, backpropagation, optimization, activation functions).  
**Concepts from:** Unit 1 examples 02 (simple NN), 05 (backprop), 06 (optimization) and related slides.  
**Answers and rubrics:** Instructor only — see `DOCS/SOLUTIONS/quizzes/`.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
What is the main advantage of deep neural networks over shallow (single hidden layer) networks?

a) They are always faster to train  
b) They can learn hierarchical representations and complex non-linear patterns  
c) They require less data  
d) They never overfit  

---

### Question 2 (10 points)
What is the role of the loss function during training?

a) To initialize the weights  
b) To measure how wrong the model’s predictions are and guide gradient updates  
c) To choose the learning rate  
d) To select the number of layers  

---

### Question 3 (10 points)
Which statement about backpropagation is correct?

a) It runs only once at the end of training  
b) It computes gradients of the loss with respect to the weights using the chain rule  
c) It is used only in CNNs  
d) It replaces the need for an optimizer  

---

### Question 4 (10 points)
Why do we use activation functions (e.g. ReLU) in hidden layers?

a) To reduce memory usage  
b) To introduce non-linearity so the network can learn complex functions  
c) To speed up training only  
d) To normalize the inputs  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write code to build a **2-layer feedforward neural network** in Keras/TensorFlow for **MNIST digit classification** (10 classes). Requirements:
- One hidden layer with 128 units and ReLU activation.
- Output layer with 10 units and softmax activation.
- Use appropriate input shape and compile with `sparse_categorical_crossentropy` and `adam` optimizer.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_01_solution.md`.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain what **overfitting** is and name **one** technique to reduce it in deep learning.

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_01_solution.md`.

---

### Question 7 (15 points)
Describe the **training loop** in one sentence each: what happens in the forward pass, and what happens after the loss is computed (backward pass and update).

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_01_solution.md`.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A model achieves **99% training accuracy** and **70% validation accuracy**. What is the likely problem, and **one** concrete step you would take to address it?

**Answer Key:** See `DOCS/SOLUTIONS/quizzes/quiz_01_solution.md`.

---

**Mapping:** CLO1 (explain concepts); notebooks: 02_simple_neural_network, 05_backpropagation_detailed, 06_optimization_techniques.

**For:** AIAT 122 - Deep Learning
