# Quiz 03 – Unit 3: Implementation and Development of the Project Idea
## AIAT 126 - Graduation Project

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 3 (data collection strategies, the cleaning pipeline, feature engineering, the train/validation/test split, baseline models, grid search vs random search, and reading tuning results honestly).  
**Concepts from:** Unit 3 example 01 (data collection and preprocessing) and example 02 (model training and hyperparameter optimization), plus exercise 01 (implementation planning).  
**Note:** Questions 1, 3, 4, 6 and 7 refer to the numbers printed by the Unit 3 notebooks when you ran them.  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
In the Unit 3 cleaning pipeline, the sample DataFrame started at shape `(1000, 4)` and, after dropping rows with missing values, was `(957, 4)`. How many rows carried a missing value, and in which column?

a) 43 rows, all in `feature3`  
b) 43 rows, all in `feature1`  
c) 57 rows, all in `feature3`  
d) 100 rows, all in `target`  

---

### Question 2 (10 points)
The Unit 3 split divides 1000 samples into 600 / 200 / 200. Which set is used **only** for the final evaluation?

a) The training set  
b) The validation set  
c) The test set  
d) All three, in equal measure  

---

### Question 3 (10 points)
The grid search ran over a grid of 3 × 4 × 3 × 3 = 108 parameter combinations with `cv=5`. How many **model fits** did that require?

a) 5  
b) 108  
c) 216  
d) 540  

---

### Question 4 (10 points)
In that run the tuned model reached validation accuracy 0.8950 against the baseline's 0.9050. Which response does the notebook teach?

a) Re-run the search with new random seeds until the tuned model wins  
b) Report the result as it stands, check the criterion the search actually optimised (cross-validated F1), and keep the baseline if it holds up  
c) Evaluate both models on the test set to break the tie  
d) Drop the baseline from the report so that the results read consistently  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Given `X_train`, `y_train`, `X_val` and `y_val`, write code that:

1. trains a `RandomForestClassifier` **baseline** with default hyperparameters and prints accuracy, precision, recall and F1 on the validation set;
2. runs `GridSearchCV` with `cv=5` and an explicit `scoring` metric, fitted on the **training data only**;
3. prints the best parameters and the best cross-validated score;
4. prints the **signed** change in validation accuracy between the tuned model and the baseline.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Why must you establish a **baseline model** before doing any hyperparameter tuning? Support your answer with the numbers from the Unit 3 run: the baseline and tuned validation accuracies, and what happened to the cross-validated F1 score that the search actually optimised.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Compare **grid search** and **random search**. State the number of model fits each performed in the Unit 3 run and the best cross-validated F1 each reached, then say when you would choose each one for your own project.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
Your capstone dataset has 1000 rows: one numeric column with about 5% missing values, one categorical column, and a binary target. Using the Unit 3 pipeline, list the preprocessing steps in the order you would apply them. For the missing values, say which of the two options the notebook demonstrates you would choose and why. Then name the split you would use and give the argument for stratifying it.

**Answer key:** released by your instructor.

---

**Mapping:** CLO2, CLO3; notebooks: `unit3-model-development/examples/01_data_collection_preprocessing`, `unit3-model-development/examples/02_model_training_hyperparameter_optimization`, `unit3-model-development/exercises/exercise_01_implementation_planning`.

**For:** AIAT 126 - Graduation Project
