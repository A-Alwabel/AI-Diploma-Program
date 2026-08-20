# Project 03: Machine Learning Classifier

## Overview

Build a complete machine learning pipeline: load data, preprocess, train multiple models, evaluate, and compare performance.

**Learning Objectives:**
- Implement complete ML pipeline
- Train and compare multiple models
- Evaluate model performance
- Handle real-world data

---

## Requirements

### Functional Requirements
1. **Data Loading & Preprocessing**
   - Load dataset (CSV file or built-in dataset)
   - Handle missing values
   - Encode categorical variables
   - Split into train/test sets

2. **Model Training**
   - Train at least 3 different models:
     - Logistic Regression
     - Decision Tree
     - K-Nearest Neighbors (KNN)
   - Tune hyperparameters (optional)

3. **Model Evaluation**
   - Calculate accuracy
   - Create confusion matrix
   - Calculate precision, recall, F1-score
   - Visualize results

4. **Comparison & Reporting**
   - Compare all models
   - Visualize performance metrics
   - Recommend best model
   - Explain why

### Technical Requirements
- Use Python 3.9+
- Use Scikit-learn for ML
- Use Pandas for data manipulation
- Use Matplotlib/Seaborn for visualization
- Use NumPy for numerical operations
- Code should be well-commented
- Include error handling

---

## Deliverables

1. **Source Code**
   - `data_loader.py` - Data loading and preprocessing
   - `models.py` - Model definitions
   - `trainer.py` - Training functions
   - `evaluator.py` - Evaluation functions
   - `main.py` - Main pipeline
   - `visualizer.py` - Visualization functions

2. **Documentation**
   - README.md explaining dataset and approach
   - Code comments
   - Results report

3. **Results**
   - Performance metrics for all models
   - Visualizations (confusion matrices, ROC curves if applicable)
   - Comparison report

---

## Project Structure

```
project_03_ml_classifier/
├── data_loader.py
├── models.py
├── trainer.py
├── evaluator.py
├── visualizer.py
├── main.py
├── README.md
├── requirements.txt
└── data/
    └── dataset.csv (or use built-in dataset)
```

---

## Example: Iris Classification

**Dataset:** Iris (3 classes: setosa, versicolor, virginica)
**Features:** Sepal length, sepal width, petal length, petal width
**Task:** Classify iris species

**Expected Results:**
- All models should achieve >90% accuracy
- Compare which model performs best
- Visualize decision boundaries (if possible)

---

## Evaluation Criteria

See `../../ASSESSMENTS/Project_Rubric.md` for detailed rubric.

**Key Areas:**
- Data preprocessing (20%)
- Model implementation (30%)
- Evaluation quality (25%)
- Code quality (15%)
- Documentation (10%)

---

## Bonus Features

- [ ] Feature engineering
- [ ] Hyperparameter tuning
- [ ] Cross-validation
- [ ] ROC curves
- [ ] Feature importance visualization
- [ ] Deploy model (save/load)

---

## Resources

- Notebook 05: AI-based Learning Models
- Scikit-learn documentation
- Pandas documentation
- UCI Machine Learning Repository (for datasets)

---

## Submission

Submit:
1. All source code files
2. README.md with dataset description
3. Results report with visualizations
4. Trained models (optional)

**Due Date:** [Set by instructor]

---

**Created**: 2025  
**For**: Python for AI Course - 112 AIAT
