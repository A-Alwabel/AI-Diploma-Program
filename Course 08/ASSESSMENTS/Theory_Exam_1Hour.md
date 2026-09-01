# Theory Exam: Deep Learning
## AIAT 122

**Time Limit:** 60 minutes  
**Total Points:** 40  
**Instructions:** Answer all questions. Keep answers clear and concise.

---

## Part A: Multiple Choice (20 points)

Choose the best answer. Each question is worth **2 points**. Every option is a statement
someone could believe, and in several questions more than one option names a real technique —
read all four before choosing.

### Question 1
What is a key advantage of deep learning compared with many
traditional machine learning methods?

A) It reaches higher accuracy than traditional ML on any dataset, including small tabular ones  
B) It needs fewer labelled examples, because its layers share information between classes  
C) It automatically learns hierarchical features from raw data, with no hand-designed features  
D) It does not require choosing hyperparameters such as the learning rate or the number of layers

### Question 2
What is the main purpose of backpropagation?

A) To compute the gradients of the loss with respect to each weight  
B) To choose a separate learning rate for each weight automatically  
C) To pass the input forward through the layers and produce the prediction  
D) To decide how many hidden layers the network should have

### Question 3
Which of the following is a technique used to **reduce** overfitting in neural networks?

A) Adding more layers and more units to the network  
B) Training for more epochs on the same data  
C) Raising the learning rate so that training converges faster  
D) Randomly switching off units during training (dropout)

### Question 4
Why are CNNs effective for image tasks?

A) They flatten the image first, so that every pixel is compared with every other pixel  
B) They use convolutions to detect local visual patterns, and pooling to tolerate small shifts  
C) They need no activation function after them, because convolution is already non-linear  
D) They have more parameters than a fully connected network of the same depth

### Question 5
What is transfer learning?

A) Reusing a model pre-trained on a large dataset for a related task  
B) Training one model on two datasets at the same time so it learns both tasks  
C) Using a large model's outputs as targets to train a smaller model  
D) Copying a trained model to another machine so that it can serve predictions

### Question 6
Why are LSTMs usually better than basic RNNs for longer sequences?

A) They process all of the time steps in parallel instead of one at a time  
B) They have far fewer parameters, so they can be trained on much less data  
C) They use gates and a cell state to carry information across many time steps  
D) They read the whole sequence backwards as well as forwards

### Question 7
What does self-attention allow a Transformer to do?

A) Encode each token's position, which is why no positional encoding is needed  
B) Guarantee that the highest-weighted token is the reason for the prediction  
C) Process the sequence one token at a time while carrying a hidden state  
D) Let every token weigh every other token when computing its own representation

### Question 8
Which model learns a **compressed latent representation**, then treats that latent as a
**probability distribution** (a mean and a variance) that it samples from to reconstruct or
generate data?

A) Generative adversarial network (GAN)  
B) Variational autoencoder (VAE)  
C) Plain (deterministic) autoencoder  
D) Deep Q-network (DQN)

### Question 9
In reinforcement learning, what is the training signal that guides the agent toward better
actions?

A) Reward signals returned by the environment after each action  
B) Labelled (state, correct action) pairs collected in advance  
C) The reconstruction error between the agent's output and its input  
D) A discriminator's judgement of whether the action looks real

### Question 10
A team audits a model and finds its accuracy is 0.750 for one group and 0.783 for another.
Which statement about responsible AI is correct?

A) If the training data is a faithful record of what really happened, a model trained on it cannot be biased  
B) Deleting the protected attribute from the feature set removes the disparity between groups  
C) Accuracy can be near-equal across groups while the *kinds* of error differ sharply, so one metric is not enough  
D) A measured difference in outcomes between two groups is by itself proof that the model is unjust

---

## Part B: Short Answer (20 points)

Answer each question in **3 to 6 lines**. Each question is worth **5 points**.

### Question 11
Explain the roles of:
1. Convolution
2. Pooling
3. Fully connected layers

in a CNN used for image classification.

### Question 12
Compare **RNNs**, **LSTMs**, and **Transformers**. Give:
1. One strength of each
2. One limitation of each

### Question 13
You need to deploy an image classification model to a small clinic
computer with limited memory and low-latency requirements.

Answer the following:
1. Name **two** model optimization techniques that can help
2. State **one** trade-off you may face after optimization
3. Name **one** deployment option covered in the course

### Question 14
A medical AI system performs worse on one demographic group than another.

Answer the following:
1. What ethical problem does this indicate?
2. Give **two** actions to reduce this problem
3. Name **one** interpretability method or idea that can help build trust

---

## End of Exam
