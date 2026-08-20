# Project 01: Complete ML Pipeline

## 🎯 Real-World Application

**GDI Example: Financial Transaction Risk Scoring**

Build a pipeline that ingests transactions and flags risky behavior to support:
- **Financial/Terrorism Financing Investigations**: high-risk transaction scoring
- **Border Cargo Screening**: shipments flagged for secondary inspection
- **Cyber/Communication Threats**: login/session risk scoring

**Impact for GDI:**
- ✅ Faster triage of suspicious activity
- ✅ Consistent, auditable decisions
- ✅ Reusable pipeline for new data sources

**📖 New to machine learning?** Check out **[PROJECT_GUIDE.md](PROJECT_GUIDE.md)** for step-by-step instructions!

---

## Overview

Build a complete end-to-end machine learning pipeline that takes raw data through preprocessing, feature engineering, model training, evaluation, and deployment preparation.

**Learning Objectives:**
- Implement a complete ML workflow
- Apply data preprocessing techniques
- Perform feature engineering
- Train and evaluate multiple models
- Create a reusable pipeline framework

---

## Requirements

### Functional Requirements
1. **Data Loading and Exploration**
   - Load data from CSV/JSON files
   - Perform exploratory data analysis (EDA)
   - Generate summary statistics
   - Visualize data distributions

2. **Data Preprocessing**
   - Handle missing values
   - Remove duplicates
   - Detect and handle outliers
   - Encode categorical variables
   - Scale/normalize features

3. **Feature Engineering**
   - Create new features from existing ones
   - Select important features
   - Handle feature interactions
   - Apply dimensionality reduction (optional)

4. **Model Training**
   - Split data into train/validation/test sets
   - Train at least 3 different models
   - Implement cross-validation
   - Tune hyperparameters

5. **Model Evaluation**
   - Calculate appropriate metrics (accuracy, precision, recall, F1, etc.)
   - Generate confusion matrices
   - Create ROC curves (for classification)
   - Compare model performance

6. **Pipeline Framework**
   - Create reusable pipeline class
   - Save/load trained models
   - Make predictions on new data
   - Generate prediction reports

### Technical Requirements
- Use Python 3.8+
- Use scikit-learn for ML algorithms
- Use pandas and NumPy for data processing
- Use matplotlib/seaborn for visualization
- Code should be modular and well-organized
- Include comprehensive error handling
- Add logging for pipeline steps

---

## Deliverables

1. **Source Code**
   - `data_loader.py` - Data loading and exploration
   - `preprocessor.py` - Data preprocessing
   - `feature_engineer.py` - Feature engineering
   - `model_trainer.py` - Model training and evaluation
   - `pipeline.py` - Main pipeline class
   - `main.py` - Main program
   - `requirements.txt` - Dependencies

2. **Documentation**
   - README.md explaining how to run
   - Code comments explaining each step
   - User guide
   - Architecture diagram

3. **Results**
   - Model performance metrics
   - Visualizations (plots, charts)
   - Comparison report
   - Saved model files

---

## Project Structure

```
project_01_ml_pipeline/
├── data_loader.py
├── preprocessor.py
├── feature_engineer.py
├── model_trainer.py
├── pipeline.py
├── main.py
├── README.md
├── requirements.txt
├── models/          # Saved models
├── results/         # Output visualizations
└── data/            # Input data files
```

---

## Dataset Suggestions

Use provided GDI datasets (under `Course 04/datasets/raw/`):

1. **creditcard_fraud.csv** (default) — Financial/Terrorism Financing (binary target: `Class`)
2. **border_crossing_data.csv** — Border Cargo/Entry flows (pick a binary target you define)
3. **unsw_nb15.csv** — Cyber intrusion (multi-class or binary threat flag)
4. **crime_statistics.csv** — Internal intelligence pattern scoring

Set `random_state=73` everywhere for reproducibility.

---

## Evaluation Criteria

Grading weights below; the detailed rubric is released by your instructor.

**Key Areas:**
- Pipeline completeness (30%)
- Code quality and organization (25%)
- Model performance (20%)
- Documentation (15%)
- Creativity and extra features (10%)

---

## Bonus Features

- [ ] Implement automated feature selection
- [ ] Add model interpretability (SHAP, LIME)
- [ ] Create web interface for predictions
- [ ] Implement model versioning
- [ ] Add automated hyperparameter tuning
- [ ] Create deployment script
- [ ] Add unit tests
- [ ] Implement data validation

---

## Resources

- Unit 1: Data Processing & Regression
- Unit 2: Advanced Regression
- Unit 3: Classification Techniques
- Unit 5: Model Selection & Boosting
- scikit-learn Pipeline documentation
- pandas documentation

---

## Submission

Submit:
1. All source code files
2. README.md
3. Results and visualizations
4. Brief report explaining your implementation and findings

**Due Date:** [Set by instructor]

---

**Created**: 2025  
**For**: Machine Learning Algorithms and Applications - AIAT 114
