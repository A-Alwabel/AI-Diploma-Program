# Quiz 03: Classification Techniques

## Instructions
- **Time Limit**: 45 minutes
- **Total Points**: 95 points (19 questions x 5 points)
- **Format**: Multiple choice, short answer, code completion
- **Allowed Resources**: None (closed book)

---

## Part 1: Classification Algorithms (35 points)

### Question 1 (5 points)
What is the main difference between regression and classification?
- A) Regression predicts continuous values, classification predicts categories
- B) Classification predicts continuous values, regression predicts categories
- C) There is no difference
- D) Regression uses neural networks, classification uses trees

---

### Question 2 (5 points)
Which algorithm uses a sigmoid function to output probabilities?
- A) Decision Tree
- B) Logistic Regression
- C) K-Nearest Neighbors
- D) Support Vector Machine

---

### Question 3 (5 points)
An airport security team must be able to explain to a passenger exactly why the model flagged them. Which property of Decision Trees makes them suitable for such stakeholder-facing decisions?
- A) They are always the most accurate classifier
- B) They produce explicit if-then rules that can be read and visualized
- C) They train without requiring feature scaling
- D) They never overfit the training data

---

### Question 4 (5 points)
What does SVM (Support Vector Machine) try to find?
- A) The best decision boundary that maximizes the margin
- B) The most common class
- C) The average of all features
- D) The correlation between features

---

### Question 5 (5 points)
What is Random Forest?
- A) A single decision tree with many branches
- B) An ensemble method that combines multiple decision trees
- C) A type of neural network
- D) A clustering algorithm

---

### Question 6 (5 points)
What is the main advantage of Random Forest over a single Decision Tree?
- A) It's always faster
- B) It reduces overfitting by combining multiple trees
- C) It's easier to interpret
- D) It doesn't require any hyperparameters

---

### Question 7 (5 points)
How does K-Nearest Neighbors (KNN) classify a new data point?
- A) It uses a sigmoid function
- B) It finds the K nearest training examples and predicts the majority class
- C) It builds a decision tree
- D) It uses support vectors

---

## Part 2: Evaluation Metrics (20 points)

### Question 8 (5 points)
What does accuracy measure?
- A) The proportion of correctly classified instances
- B) The proportion of positive predictions that are correct
- C) The proportion of actual positives that are correctly identified
- D) The harmonic mean of precision and recall

---

### Question 9 (5 points)
What is precision?
- A) The proportion of correctly classified instances
- B) The proportion of positive predictions that are correct
- C) The proportion of actual positives that are correctly identified
- D) The harmonic mean of precision and recall

---

### Question 10 (5 points)
What is recall?
- A) The proportion of correctly classified instances
- B) The proportion of positive predictions that are correct
- C) The proportion of actual positives that are correctly identified
- D) The harmonic mean of precision and recall

---

### Question 11 (5 points)
What does F1-score represent?
- A) The proportion of correctly classified instances
- B) The proportion of positive predictions that are correct
- C) The proportion of actual positives that are correctly identified
- D) The harmonic mean of precision and recall

---

## Part 3: Confusion Matrix and ROC (20 points)

### Question 12 (5 points)
In a confusion matrix, what does True Positive (TP) represent?
- A) Correctly predicted negative cases
- B) Correctly predicted positive cases
- C) Incorrectly predicted negative cases
- D) Incorrectly predicted positive cases

---

### Question 13 (5 points)
What does False Positive (FP) represent in a confusion matrix?
- A) Model predicted Class 1, but actual is Class 0 (false alarm)
- B) Model predicted Class 0, but actual is Class 1 (missed detection)
- C) Model correctly predicted Class 1
- D) Model correctly predicted Class 0

---

### Question 14 (5 points)
What does False Negative (FN) represent in a confusion matrix?
- A) Model predicted Class 1, but actual is Class 0 (false alarm)
- B) Model predicted Class 0, but actual is Class 1 (missed detection)
- C) Model correctly predicted Class 1
- D) Model correctly predicted Class 0

---

### Question 15 (5 points)
What does AUC (Area Under Curve) measure in ROC analysis?
- A) The accuracy of the model
- B) The model's ability to distinguish between classes
- C) The precision of the model
- D) The recall of the model

---

## Part 4: Advanced Topics (20 points)

### Question 16 (5 points)
When are classification metrics (accuracy, precision, recall) calculated?
- A) Before training the model
- B) During training
- C) After training, on test data
- D) Before loading the data

---

### Question 17 (5 points)
What is the difference between `.predict()` and `.predict_proba()` in logistic regression?
- A) `.predict()` returns probabilities, `.predict_proba()` returns classes
- B) `.predict()` returns classes (0 or 1), `.predict_proba()` returns probabilities (0-1)
- C) They are the same
- D) `.predict()` is for training, `.predict_proba()` is for testing

---

### Question 18 (5 points)
What is class imbalance in classification?
- A) When classes have equal number of samples
- B) When one class has significantly more samples than another
- C) When features are imbalanced
- D) When the model is overfitting

---

### Question 19 (5 points)
How can you handle class imbalance in logistic regression?
- A) Use `class_weight='balanced'` parameter
- B) Remove the minority class
- C) Always use accuracy as the metric
- D) Increase the learning rate

---

**Good luck!** 🍀

---

> Answers and rubric: released by your instructor.
