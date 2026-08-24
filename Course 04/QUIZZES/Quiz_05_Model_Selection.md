# Quiz 05: Model Selection and Boosting

## Instructions
- **Time Limit**: 30 minutes
- **Total Points**: 50 points
- **Format**: Multiple choice, short answer, code completion
- **Allowed Resources**: None (closed book)

---

## Part 1: Hyperparameter Tuning (20 points)

### Question 1 (5 points)
What is the main purpose of Grid Search?
- A) To find the best hyperparameters by trying all combinations
- B) To find the best features
- C) To find the best model architecture
- D) To find the best dataset

---

### Question 2 (5 points)
What is the main advantage of Random Search over Grid Search?
- A) It's always more accurate
- B) It's faster and can find good solutions with fewer iterations
- C) It always finds the best solution
- D) It doesn't require cross-validation

---

### Question 3 (5 points)
What is cross-validation used for in hyperparameter tuning?
- A) To speed up training
- B) To get a more reliable estimate of model performance for each hyperparameter set
- C) To reduce overfitting
- D) To handle missing values

---

### Question 4 (5 points)
What is a learning curve used for?
- A) To visualize model performance over training iterations
- B) To diagnose overfitting and underfitting
- C) To choose the best learning rate
- D) All of the above

---

## Part 2: Boosting Algorithms (20 points)

### Question 5 (5 points)
What is the main idea behind boosting?
- A) To combine multiple weak learners into a strong learner
- B) To use only the best single model
- C) To reduce the number of features
- D) To increase the number of samples

---

### Question 6 (5 points)
What is the difference between bagging and boosting?
- A) Bagging trains models in parallel, boosting trains sequentially
- B) Boosting trains models in parallel, bagging trains sequentially
- C) There is no difference
- D) Bagging is for regression, boosting is for classification

---

### Question 7 (5 points)
What is Gradient Boosting?
- A) A method that combines models by averaging predictions
- B) A method that trains models sequentially, each correcting the previous one's errors
- C) A method that uses only decision trees
- D) A method that doesn't use cross-validation

---

### Question 8 (5 points)
What is XGBoost?
- A) An optimized implementation of gradient boosting
- B) A type of neural network
- C) A clustering algorithm
- D) A dimensionality reduction technique

---

## Part 3: Tuning and Comparing Boosting Models (10 points)

### Question 9 (5 points)
In gradient boosting (XGBoost, LightGBM), what does the `learning_rate` hyperparameter control?
- A) How many features each tree is allowed to use
- B) How much each newly added tree contributes to the ensemble's prediction
- C) How many CPU cores are used during training
- D) The size of the train/test split

---

### Question 10 (5 points)
Compared with XGBoost, what is LightGBM's distinguishing characteristic?
- A) It grows trees leaf-wise, which makes it faster - especially on large datasets
- B) It trains all of its trees in parallel instead of sequentially
- C) It does not use decision trees at all
- D) It always achieves higher test accuracy than XGBoost

---

> Answers and rubric: released by your instructor.