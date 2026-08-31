# Project 03: Advanced Regression Analysis

## Overview

Implement and compare different regression techniques with proper hyperparameter tuning, cross-validation, and performance evaluation.

**Learning Objectives:**
- Implement multiple regression algorithms
- Apply regularization techniques
- Perform hyperparameter tuning
- Evaluate regression models properly
- Handle overfitting and underfitting

---

## Requirements

### Functional Requirements
1. **Data Preparation**
   - Load regression dataset
   - Perform EDA and feature analysis
   - Handle multicollinearity
   - Split into train/validation/test sets

2. **Regression Implementation**
   - Linear Regression
   - Ridge Regression
   - Lasso Regression
   - Polynomial Regression
   - (Optional) Elastic Net, XGBoost

3. **Model Training**
   - Train all regression models
   - Implement k-fold cross-validation
   - Perform hyperparameter tuning
   - Handle feature scaling

4. **Model Evaluation**
   - Calculate MSE, RMSE, MAE, R²
   - Generate residual plots
   - Create prediction vs actual plots
   - Analyze model coefficients

5. **Comparison and Analysis**
   - Compare all models
   - Analyze bias-variance tradeoff
   - Visualize model performance
   - Generate comprehensive report

### Technical Requirements
- Use Python 3.8+
- Use scikit-learn
- Use matplotlib/seaborn
- Implement proper validation strategies

---

## Deliverables

1. **Source Code**
   - `regression_models.py` - All regression implementations
   - `evaluator.py` - Evaluation functions
   - `visualizer.py` - Visualization functions
   - `main.py` - Main program

2. **Documentation**
   - README.md
   - Analysis report
   - Code comments

3. **Results**
   - Performance metrics
   - Residual plots
   - Comparison charts
   - Model analysis

---

## Dataset Suggestions

- `load("montgomery_911_calls")` — Emergency Response (predict call volume per hour or per day)
- `load("border_crossing_data")` — Border throughput forecasting (predict `Value` per port and month)
- `load("crime_statistics")` — Internal intelligence metrics (predict `Murder` from the other columns)
- `load("creditcard_fraud")` — Financial risk scoring (regress `Amount`; the `Class` column makes it a
  classification file, so state clearly which problem you chose)

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

Use `random_state=73` for all splits/models to keep runs reproducible.

---

## Evaluation Criteria

- Model implementation (30%)
- Performance metrics (25%)
- Hyperparameter tuning (20%)
- Visualization quality (15%)
- Documentation (10%)

---

**Created**: 2025  
**For**: Machine Learning Algorithms and Applications - AIAT 114
