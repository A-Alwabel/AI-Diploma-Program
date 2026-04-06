# Practical Exam: Deep Learning
## AIAT 122

**Time Limit:** 60 minutes  
**Total Points:** 40  
**Framework:** Python + PyTorch  
**Instructions:** Complete the missing code and answer the short
implementation questions. Minor syntax mistakes may receive partial
credit if the logic is correct.

---

## Question 1: Neural Network Basics (8 points)

Complete the missing parts in the following training setup for a simple classifier.

```python
import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(20, 32)
        self.fc2 = nn.Linear(32, 3)

    def forward(self, x):
        x = ____________
        x = self.fc2(x)
        return x

model = SimpleNet()
criterion = ____________
optimizer = ____________
```

Tasks:
1. Fill in the activation function line
2. Fill in the loss function
3. Fill in the optimizer
4. Name one metric you would track on validation data

---

## Question 2: CNN for Image Classification (10 points)

Complete the CNN below for a `32 x 32 x 3` image classification
problem with **10 classes**.

```python
import torch
import torch.nn as nn

class CNNClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            ____________,
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            ____________
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 8 * 8, 64),
            nn.ReLU(),
            ____________
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x
```

Tasks:
1. Fill in the two missing pooling layers
2. Fill in the final classification layer
3. State one reason CNNs are better than plain fully connected networks for images

---

## Question 3: Sequence Model with LSTM (8 points)

Complete the text classification model below.

```python
import torch
import torch.nn as nn

class TextClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
        super().__init__()
        self.embedding = ____________
        self.lstm = ____________
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        x = self.embedding(x)
        output, (hidden, cell) = self.lstm(x)
        last_hidden = ____________
        logits = self.fc(last_hidden)
        return logits
```

Tasks:
1. Fill in the embedding layer
2. Fill in the LSTM layer
3. Fill in `last_hidden`
4. State one advantage of LSTM over a basic RNN

---

## Question 4: Advanced Deep Learning (6 points)

### Part A
Write the standard VAE loss formula using:
- `recon_loss`
- `mu`
- `logvar`

You may write it as a single PyTorch expression.

### Part B
In reinforcement learning, what is the role of the **reward** signal?

---

## Question 5: Deployment and Responsible AI (8 points)

### Part A: ONNX Export
Write two lines of PyTorch code to export a trained model called
`model` with a sample input tensor called `dummy_input` to an
ONNX file named `model.onnx`.

### Part B: Safety Check
Name:
1. One compression technique you could apply before deployment
2. One fairness or interpretability check you should perform before
   using the model in a real application

---

## End of Exam
