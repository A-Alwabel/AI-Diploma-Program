# Final Exam: Deep Learning
## AIAT 122

**Time Limit:** 2 hours  
**Total Points:** 110 points (100 required; Q13 may be bonus or count toward total)  
**Instructions:** Answer all questions. Show your work for partial credit.

**Marking scheme:** Part 1 (Q1–Q6): 5 pts each = 30. Part 2 (Q7–Q9): 10 pts each = 30. Part 3 (Q10: 15 pts, Q11: 10 pts) = 25. Part 4 (Q12): 15 pts. Part 5 (Q13): 10 pts. **Total: 110** (100 required; Q13 may be bonus or count toward total). See `Final_Exam_Rubric.md` for detailed criteria.

---

## Part 1: Multiple Choice (30 points)

Every option below is a statement someone in this field has actually believed. Exactly one is
correct. Read all four before you answer.

### Question 1 (5 points)
A team replaces a logistic-regression classifier with a deep neural network on the **same raw
pixels**, and test accuracy rises. Which statement best explains the advantage the deep
network has here?

A) It needs fewer labelled training images, because its layers share information between classes  
B) It learns hierarchical features from the raw pixels instead of using each pixel as a fixed feature  
C) It is guaranteed to reach the global minimum of its loss, which logistic regression is not  
D) It removes the need to scale or normalise the inputs before training

---

### Question 2 (5 points)
Your first model for a 28×28 image task is a `Dense` network on flattened pixels. You replace
it with a CNN and accuracy improves. What does the **convolutional layer** give you that the
`Dense` layer did not?

A) It treats each image as one flat vector, so where a pixel sits no longer changes the result  
B) Its weight sharing removes the risk of overfitting, so a held-out validation split is no longer needed  
C) It supplies the non-linearity itself, so no ReLU or other activation is needed after it  
D) The same small filter is applied at every position, so a pattern learned once is detected anywhere in the image

---

### Question 3 (5 points)
A `SimpleRNN` trained on 100-token movie reviews barely uses the words near the **start** of
each review. You replace it with an **LSTM** and results improve. Why does the LSTM help?

A) Its gates and cell state stop the gradient from shrinking away over many time steps  
B) It reads all 100 tokens in parallel instead of one at a time  
C) It has fewer parameters than a `SimpleRNN`, so it needs less data to train  
D) It reads each review backwards as well as forwards, so the early words are seen last

---

### Question 4 (5 points)
Scaled dot-product self-attention computes `Attention(Q, K, V) = softmax(QKᵀ / √d_k) V`.
What does the **softmax term** produce?

A) A probability distribution over the vocabulary, giving the model's next predicted token  
B) The position of each token in the sequence, which is why no positional encoding is needed  
C) One weight per position, used to take a weighted average of the value vectors `V`  
D) The model's confidence that its prediction is correct, which is why attention maps can be read as explanations

---

### Question 5 (5 points)
You load a pre-trained MobileNetV2, **freeze** the base, and attach a new 10-class head:
**12,810 of 2,236,682 parameters (0.57%)** are trainable. You have 2,000 labelled images.
Which statement about this setup is correct?

A) Because the base is frozen, no training is needed — the model can be used as it is  
B) The frozen layers keep their ImageNet features; the new head is what learns your 10 classes  
C) Freezing the base means the model can no longer overfit your 2,000 images  
D) A frozen backbone pays off only when the new dataset is at least as large as the one it was pre-trained on

---

### Question 6 (5 points)
A trained FP32 model is converted to INT8. The stored file gets smaller and validation
accuracy barely moves. Which optimization technique is this, and what did it change?

A) Quantization — the number of **bits** used to store each weight value  
B) Pruning — the number of **weights**, by zeroing out the smallest ones  
C) Distillation — the **architecture**, by training a smaller model to copy a larger one  
D) ONNX export — the **file format**, so the model runs outside the framework that trained it

---

## Part 2: Short Answer Questions (30 points)

### Question 7 (10 points)
**CLO2:** Explain the architecture of a CNN. Describe convolution, pooling, and fully connected layers.

---

### Question 8 (10 points)
**CLO2:** Compare RNNs, LSTMs, and Transformers. What are the advantages and disadvantages of each?

---

### Question 9 (10 points)
**CLO2:** Explain the Transformer architecture. How does self-attention work?

---

## Part 3: Practical/Coding Questions (25 points)

### Question 10 (15 points)
**CLO2, CLO3:** Implement a CNN for image classification:
1. Define CNN architecture (conv, pooling, FC layers)
2. Define training loop
3. Include data loading and preprocessing
4. Show evaluation

---

### Question 11 (10 points)
**CLO2:** Write a **PyTorch** text classification model for sequence data using an LSTM. Define:
1. A model class with `nn.Embedding`, `nn.LSTM`, and `nn.Linear` layers.
2. Show the `forward` method that takes token IDs and returns a class logit.
3. Briefly describe how you would train this model (loss function and optimizer choice).

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
**CLO3, CLO4, CLO5:** Design a deep learning system for medical image diagnosis:
1. Choose an appropriate architecture (CNN, Transformer, …) and justify the choice
2. Explain the data preprocessing the chosen model requires
3. Choose your evaluation: explain why one overall accuracy number is not enough for this
   system, and state what you would report instead
4. Optimize the model for deployment on the clinic's hardware
5. Consider ethical implications (bias, explainability)

---

## Part 5: Debug / Critique (10 points, optional toward total)

### Question 13 (10 points)
**CLO1, CLO4:** The following training setup is given: a CNN is trained for 50 epochs with no
validation split, no early stopping, and a fixed learning rate of 0.1. The final training
accuracy is 99% but the instructor reports poor performance on unseen images.
**Identify at least two problems** in this setup and **suggest one fix** for each.

---

**End of Exam**

**Good Luck!**
