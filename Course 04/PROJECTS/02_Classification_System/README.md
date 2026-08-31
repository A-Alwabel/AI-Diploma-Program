# Project 02: Multi-Class Classification System

## Overview

Build a comprehensive classification system that implements and compares multiple classification algorithms on a real-world dataset.

**Learning Objectives:**
- Implement multiple classification algorithms
- Compare algorithm performance
- Apply proper evaluation metrics
- Perform hyperparameter tuning
- Create classification visualizations

---

## Requirements

### Functional Requirements
1. **Data Preparation**
   - Load classification dataset
   - Perform EDA
   - Handle class imbalance (if present)
   - Split into train/validation/test sets

2. **Algorithm Implementation**
   - Logistic Regression
   - Decision Tree Classifier
   - Support Vector Machine (SVM)
   - (Optional) Random Forest, Naive Bayes

3. **Model Training**
   - Train all algorithms
   - Implement cross-validation
   - Perform hyperparameter tuning (GridSearchCV)
   - Handle class imbalance (SMOTE, class weights)

4. **Model Evaluation**
   - Calculate accuracy, precision, recall, F1-score
   - Generate confusion matrices
   - Create ROC curves and AUC scores
   - Generate classification reports

5. **Comparison and Visualization**
   - Compare all models side-by-side
   - Create performance comparison charts
   - Visualize decision boundaries (for 2D data)
   - Generate feature importance plots

### Technical Requirements
- Use Python 3.8+
- Use scikit-learn for algorithms
- Use imbalanced-learn for handling imbalance
- Use matplotlib/seaborn for visualization
- Implement proper error handling
- Add comprehensive logging

---

## Deliverables

1. **Source Code**
   - `data_preparation.py` - Data loading and preprocessing
   - `classifiers.py` - Classification algorithms
   - `evaluator.py` - Model evaluation
   - `comparison.py` - Model comparison
   - `visualizer.py` - Visualization functions
   - `main.py` - Main program

2. **Documentation**
   - README.md
   - Code comments
   - Results analysis

3. **Results**
   - Performance metrics table
   - Confusion matrices
   - ROC curves
   - Comparison charts

---

## Dataset Suggestions

- `load("montgomery_911_calls")` (multi-class: EMS/Fire/Traffic from `title`) — Emergency Response
- `load("unsw_nb15")` (multi-class `attack_cat`, or collapse to the binary `label`) — Cyber/Communication
- `load("cicids2017")` (multi-class ` Label`: 15 attack classes) — Cyber/Communication
- `load("creditcard_fraud")` (binary `Class`, heavily imbalanced; set class weights) — Financial/Terrorism Financing

**No file paths.** Load any of these with the shared loader, which finds the data from any
working directory and on Google Colab, and prints whether it gave you the full file or the
bundled sample:

```python
import sys, pathlib
_here = pathlib.Path.cwd().resolve()
sys.path.insert(0, str(next(p for p in [_here, *_here.parents] if (p / "tools" / "data.py").exists())))
from tools.data import load

df = load("creditcard_fraud", prefer="sample")   # prefer="sample" = same rows for everyone
```

See `Course 04/datasets/DATA.md` for what ships in the repository, what each sample changes,
and how to fetch the full files if you want them.

Use `random_state=73` for all splits/models to keep results reproducible.

---

## Evaluation Criteria

- Algorithm implementation (30%)
- Model performance (25%)
- Code quality (20%)
- Visualization quality (15%)
- Documentation (10%)

---

**Created**: 2025  
**For**: Machine Learning Algorithms and Applications - AIAT 114
