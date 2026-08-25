# Final Exam: Introduction to Artificial Intelligence and Applications
## AIAT 111

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. Show your work for partial credit.

**Marking scheme:** Part 1 (Q1–Q6): 4 pts each = 24. Part 2 (Q7–Q9): 9 pts each = 27. Part 3 (Q10: 14 pts, Q11: 10 pts) = 24. Part 4 (Q12): 15 pts. Part 5 (Q13): 10 pts. **Total: 100.**

---

## Part 1: Multiple Choice (24 points)

### Question 1 (4 points)
What is the main difference between traditional AI (rule-based) and modern AI (data-driven)?

A) Traditional AI uses neural networks, modern AI uses rules  
B) Traditional AI cannot explain its decisions, modern AI is fully transparent  
C) Traditional AI uses explicit rules, modern AI learns from data  
D) Traditional AI is faster, modern AI is slower

---

### Question 2 (4 points)
Which search algorithm guarantees finding the shortest path?

A) Depth-First Search (DFS)  
B) Breadth-First Search (BFS)  
C) Random Search  
D) Both A and B

---

### Question 3 (4 points)
What is a key component of knowledge representation systems?

A) A relational database table with indexed columns  
B) A labeled training dataset and a loss function  
C) A priority queue ordered by a heuristic function  
D) Rules, facts, and inference mechanisms

---

### Question 4 (4 points)
Bayesian probability is used in AI for:

A) Handling uncertainty and making probabilistic inferences  
B) Guaranteeing a correct diagnosis whenever a test result is positive  
C) Computing the prior probability of a hypothesis before any evidence is observed  
D) Eliminating uncertainty so that model predictions become deterministic

---

### Question 5 (4 points)
What is the main difference between supervised and unsupervised learning?

A) Supervised is faster  
B) Supervised learning predicts numbers, unsupervised learning predicts categories  
C) Supervised uses labeled data, unsupervised uses unlabeled data  
D) Supervised learning uses neural networks, unsupervised learning uses clustering algorithms

---

### Question 6 (4 points)
Which activation function is commonly used in feedforward neural networks?

A) ReLU, Sigmoid, Tanh  
B) Adam, SGD, RMSprop  
C) MSE, Cross-Entropy, Hinge  
D) Dropout, Batch Normalization, Early Stopping

---

## Part 2: Short Answer Questions (27 points)

### Question 7 (9 points)
**CLO1:** Explain the difference between traditional AI (rule-based) and modern AI (data-driven). Provide a real-world example of each.

---

### Question 8 (9 points)
**CLO2:** Describe how the A* search algorithm works. What makes it more efficient than BFS or DFS?

---

### Question 9 (9 points)
**CLO3:** Explain knowledge representation and provide two methods used to represent knowledge in AI systems.

---

## Part 3: Practical/Coding Questions (24 points)

### Question 10 (14 points)
**CLO2:** Implement a simple BFS (Breadth-First Search) algorithm in Python to find a path in a graph. Use the following graph structure:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
```

Find the path from 'A' to 'F'.

---

### Question 11 (10 points)
**CLO6:** Write Python code to create a simple feedforward neural network with:
- Input layer: 3 neurons
- Hidden layer: 4 neurons with ReLU activation
- Output layer: 1 neuron with sigmoid activation

The network is for **binary classification** (predicting 0 or 1) from 3 numeric patient features. Build the model and compile it with an appropriate loss function and optimizer.

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
**CLO5, CLO7:** You are building an AI system for a hospital to help diagnose diseases. The system needs to:
1. Process patient symptoms (supervised learning)
2. Find patterns in patient data (unsupervised learning)
3. Use neural networks for complex pattern recognition

Explain how you would design this system using concepts from this course. Include:
- Which AI approach you'd use for each component
- Why you chose each approach
- How you would evaluate the system

---

## Part 5: Generative AI (10 points)

### Question 13 (10 points)
**CLO8:** Answer both parts.

**(a)** Explain the difference between a **discriminative** model and a **generative** model. Name one example of each from this course.

**(b)** A GAN is never shown the "correct" output for a sample it generates. Describe how a GAN trains its generator, and explain where the training signal comes from.

---

**End of Exam**

**Good Luck!**
