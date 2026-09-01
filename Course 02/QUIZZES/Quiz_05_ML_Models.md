# Quiz 05: AI-based Learning Models

## Instructions
- **Time Limit**: 50 minutes
- **Total Points**: 100 points
- **Format**: Multiple choice, short answer, code completion
- **Allowed Resources**: None (closed book)

---

## Part 1: Machine Learning Basics (20 points)

### Question 1 (5 points)
What is supervised learning?
- A) Learning without labels
- B) Learning from rewards
- C) Learning with labeled data
- D) Learning randomly

### Question 2 (5 points)
What is the difference between classification and regression?
- A) Classification predicts categories, regression predicts numbers
- B) Classification predicts numbers, regression predicts categories
- C) They're the same
- D) Classification is faster

### Question 3 (10 points)
What is the purpose of splitting data into training and testing sets?

**Answer key:** released by your instructor.

---

## Part 2: Linear Regression (20 points)

### Question 4 (5 points)
Linear regression is used for:
- A) Classification
- B) Visualization
- C) Clustering
- D) Regression (predicting continuous values)

### Question 5 (10 points)
Complete the code to train a linear regression model:

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.______(X_train, y_train)
predictions = model.______(X_test)
```

### Question 6 (5 points)
What does the coefficient in linear regression represent?
- A) The intercept
- B) The slope (how much y changes for each unit change in x)
- C) The error
- D) The prediction

---

## Part 3: Logistic Regression (15 points)

### Question 7 (5 points)
Logistic regression is used for:
- A) Binary classification
- B) Regression
- C) Clustering
- D) Visualization

### Question 8 (5 points)
What is the output range of logistic regression?
- A) -∞ to +∞
- B) 0 to 1 (probabilities)
- C) 0 to 100
- D) -1 to 1

### Question 9 (5 points)
What is the sigmoid function used for in logistic regression?
- A) To make predictions linear
- B) To calculate errors
- C) To convert outputs to probabilities between 0 and 1
- D) To visualize data

---

## Part 4: Decision Trees (15 points)

### Question 10 (5 points)
Decision trees split data based on:
- A) Random selection
- B) The last feature
- C) The first feature
- D) Features that best separate classes

### Question 11 (5 points)
What is a leaf node in a decision tree?
- A) The root
- B) A final decision/classification
- C) A split point
- D) A feature

### Question 12 (5 points)
What is overfitting in decision trees?
- A) Model is too simple
- B) Model is too slow
- C) Model memorizes training data and doesn't generalize
- D) Model doesn't work

---

## Part 5: K-Nearest Neighbors (KNN) (15 points)

### Question 13 (5 points)
KNN classifies based on:
- A) The most common class among k nearest neighbors
- B) The farthest neighbors
- C) Random neighbors
- D) All neighbors equally

### Question 14 (5 points)
What does k represent in KNN?
- A) The number of features
- B) The number of samples
- C) The number of classes
- D) The number of nearest neighbors to consider

### Question 15 (5 points)
If k is too small in KNN, what happens?
- A) Model is more robust
- B) Model is slower
- C) Model is sensitive to noise
- D) Nothing changes

---

## Part 6: Model Evaluation (15 points)

### Question 16 (5 points)
What is accuracy?
- A) Training time
- B) Average error
- C) Number of predictions
- D) Percentage of correct predictions

### Question 17 (5 points)
What is the purpose of a confusion matrix?
- A) To visualize classification performance
- B) To calculate accuracy
- C) To train models
- D) To split data

### Question 18 (5 points)
What is cross-validation used for?
- A) To train models
- B) To better estimate model performance
- C) To visualize data
- D) To split data once

---

---

## Grading Rubric

- **90-100 points**: Excellent understanding
- **80-89 points**: Good understanding
- **70-79 points**: Satisfactory understanding
- **60-69 points**: Needs improvement
- **Below 60**: Review required

---

**Created**: 2025  
**For**: Python for AI Course - 112 AIAT
