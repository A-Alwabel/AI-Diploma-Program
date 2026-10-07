"""
Multi-Class Classification System Template
Project 02 Template

Fill in the functions marked with TODO comments.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, auc
)
import matplotlib.pyplot as plt
import seaborn as sns

class DataPreparator:
    """Handles data loading and preprocessing."""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
    
    def load_data(self, filepath):
        """
        Load dataset from file.
        
        TODO: Load data from CSV/JSON file
        """
        # TODO: Load data using pandas
        # df = pd.read_csv(filepath)
        # return df
        pass
    
    def explore_data(self, df):
        """
        Perform exploratory data analysis.
        
        TODO: Display data info, statistics, check for missing values
        """
        # TODO: Print df.info()
        # TODO: Print df.describe()
        # TODO: Check for missing values
        # TODO: Check class distribution
        pass
    
    def preprocess(self, df, target_column):
        """
        Preprocess data for classification.
        
        TODO: Handle missing values, encode categorical, scale features
        """
        # TODO: Handle missing values
        # TODO: Encode categorical variables
        # TODO: Separate features and target
        # TODO: Scale features
        # return X, y
        pass
    
    def split_data(self, X, y, test_size=0.2, val_size=0.2):
        """
        Split data into train/validation/test sets.
        
        TODO: Split data appropriately
        """
        # TODO: First split: train+val / test
        # TODO: Second split: train / val
        # return X_train, X_val, X_test, y_train, y_val, y_test
        pass


class ClassificationSystem:
    """Implements multiple classification algorithms."""
    
    def __init__(self):
        self.models = {}
        self.best_params = {}
    
    def train_logistic_regression(self, X_train, y_train, X_val, y_val):
        """
        Train Logistic Regression with hyperparameter tuning.
        
        TODO: Implement GridSearchCV for hyperparameter tuning
        """
        # TODO: Define parameter grid
        # param_grid = {'C': [0.1, 1, 10], 'penalty': ['l1', 'l2']}
        
        # TODO: Create GridSearchCV
        # grid_search = GridSearchCV(...)
        
        # TODO: Fit on training data
        # grid_search.fit(X_train, y_train)
        
        # TODO: Store best model
        # self.models['logistic_regression'] = grid_search.best_estimator_
        pass
    
    def train_decision_tree(self, X_train, y_train, X_val, y_val):
        """
        Train Decision Tree Classifier.
        
        TODO: Implement with hyperparameter tuning
        """
        # TODO: Define parameter grid (max_depth, min_samples_split, etc.)
        # TODO: Create GridSearchCV
        # TODO: Fit and store best model
        pass
    
    def train_svm(self, X_train, y_train, X_val, y_val):
        """
        Train Support Vector Machine.
        
        TODO: Implement with hyperparameter tuning
        """
        # TODO: Define parameter grid (C, kernel, gamma)
        # TODO: Create GridSearchCV
        # TODO: Fit and store best model
        pass


class ModelEvaluator:
    """Evaluates classification models."""
    
    def evaluate(self, model, X_test, y_test, model_name):
        """
        Evaluate a single model.
        
        TODO: Calculate all metrics and return results
        """
        # TODO: Make predictions
        # y_pred = model.predict(X_test)
        
        # TODO: Calculate metrics
        # accuracy = accuracy_score(y_test, y_pred)
        # precision = precision_score(y_test, y_pred, average='weighted')
        # recall = recall_score(y_test, y_pred, average='weighted')
        # f1 = f1_score(y_test, y_pred, average='weighted')
        
        # TODO: Return dictionary with all metrics
        pass
    
    def compare_models(self, models, X_test, y_test):
        """
        Compare all models and return comparison table.
        
        TODO: Evaluate all models and create comparison DataFrame
        """
        # TODO: Evaluate each model
        # TODO: Create comparison DataFrame
        # TODO: Return sorted by accuracy
        pass
    
    def plot_confusion_matrix(self, y_true, y_pred, model_name):
        """
        Plot confusion matrix.
        
        TODO: Create confusion matrix visualization
        """
        # TODO: Calculate confusion matrix
        # TODO: Plot using seaborn heatmap
        pass
    
    def plot_roc_curves(self, models, X_test, y_test):
        """
        Plot ROC curves for all models (binary classification only).
        
        TODO: Create ROC curve plot
        """
        # TODO: For each model, calculate ROC curve
        # TODO: Plot all curves on same graph
        pass


def main():
    """
    Main execution function.
    
    TODO: Implement complete workflow
    """
    # TODO: Initialize DataPreparator
    # TODO: Load and explore data
    # TODO: Preprocess data
    # TODO: Split data
    
    # TODO: Initialize ClassificationSystem
    # TODO: Train all models
    
    # TODO: Initialize ModelEvaluator
    # TODO: Evaluate all models
    # TODO: Compare models
    # TODO: Create visualizations
    
    print("Classification system complete!")


if __name__ == "__main__":
    main()

