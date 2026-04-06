# Practical Exam: Deep Learning
## Reference Solution

Use with `Practical_Exam_1Hour.md`.

---

## Question 1: Neural Network Basics (8 points)

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
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = SimpleNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)
```

One valid validation metric:
- accuracy
- F1-score
- precision / recall

---

## Question 2: CNN for Image Classification (10 points)

```python
import torch
import torch.nn as nn

class CNNClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 8 * 8, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x
```

One valid reason CNNs are better for images:
- they exploit spatial structure
- they learn local patterns such as edges and textures
- they use parameter sharing, so they are more efficient than dense layers on images

---

## Question 3: Sequence Model with LSTM (8 points)

```python
import torch
import torch.nn as nn

class TextClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        x = self.embedding(x)
        output, (hidden, cell) = self.lstm(x)
        last_hidden = hidden[-1]
        logits = self.fc(last_hidden)
        return logits
```

One valid advantage of LSTM over a basic RNN:
- it handles long-term dependencies better
- gating reduces vanishing-gradient problems

---

## Question 4: Advanced Deep Learning (6 points)

### Part A

```python
vae_loss = recon_loss + (-0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp()))
```

Equivalent answers that correctly combine reconstruction loss and
KL divergence should receive full credit.

### Part B

The reward signal tells the agent how good or bad an action was,
so it can learn a policy that maximizes cumulative reward.

---

## Question 5: Deployment and Responsible AI (8 points)

### Part A: ONNX Export

```python
model.eval()
torch.onnx.export(model, dummy_input, "model.onnx")
```

### Part B: Safety Check

One valid compression technique:
- quantization
- pruning
- distillation

One valid fairness or interpretability check:
- compare performance across demographic groups
- inspect confusion matrices by subgroup
- use Grad-CAM, SHAP, or attention visualization
- review false positives and false negatives before deployment

---

## Suggested Marking Guide

### Question 1 (8 pts)
- 2 pts: activation line
- 2 pts: loss function
- 2 pts: optimizer
- 2 pts: valid metric

### Question 2 (10 pts)
- 3 pts: first pooling layer
- 3 pts: second pooling layer
- 2 pts: final classification layer
- 2 pts: valid CNN justification

### Question 3 (8 pts)
- 2 pts: embedding layer
- 2 pts: LSTM layer
- 2 pts: last hidden state
- 2 pts: valid LSTM advantage

### Question 4 (6 pts)
- 4 pts: correct VAE loss idea
- 2 pts: correct reward explanation

### Question 5 (8 pts)
- 4 pts: correct ONNX export lines
- 2 pts: valid compression technique
- 2 pts: valid fairness or interpretability check
