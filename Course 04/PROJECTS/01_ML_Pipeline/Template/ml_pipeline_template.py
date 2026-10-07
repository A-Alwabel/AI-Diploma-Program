"""
Complete ML Pipeline Template
Project 01 Template

Fill in the functions marked with TODO comments.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataLoader:
    """Handles data loading and exploration."""
    
    def load_csv(self, filepath):
        """
        Load data from CSV file.
        
        TODO: Load CSV and return DataFrame
        """
        # TODO: Load CSV using pandas
        # df = pd.read_csv(filepath)
        # logger.info(f"Loaded {len(df)} rows from {filepath}")
        # return df
        pass
    
    def explore(self, df):
        """
        Perform exploratory data analysis.
        
        TODO: Display data info, statistics, missing values
        """
        # TODO: Print df.info()
        # TODO: Print df.describe()
        # TODO: Print missing values count
        # TODO: Print data shape
        pass


class Preprocessor:
    """Handles data preprocessing."""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
    
    def handle_missing_values(self, df, strategy='mean'):
        """
        Handle missing values.
        
        TODO: Fill missing values based on strategy
        """
        # TODO: Check for missing values
        # TODO: Fill numeric columns with mean/median
        # TODO: Fill categorical columns with mode
        # return df
        pass
    
    def remove_duplicates(self, df):
        """
        Remove duplicate rows.
        
        TODO: Remove duplicates
        """
        # TODO: Remove duplicates
        # return df.drop_duplicates()
        pass
    
    def encode_categorical(self, df, columns):
        """
        Encode categorical variables.
        
        TODO: Encode categorical columns
        """
        # TODO: Use LabelEncoder or OneHotEncoder
        # return df
        pass
    
    def scale_features(self, X_train, X_test):
        """
        Scale features.
        
        TODO: Scale features using StandardScaler
        """
        # TODO: Fit scaler on training data
        # TODO: Transform both train and test
        # return X_train_scaled, X_test_scaled
        pass


class FeatureEngineer:
    """Handles feature engineering."""
    
    def create_features(self, df):
        """
        Create new features from existing ones.
        
        TODO: Create new features (e.g., interactions, transformations)
        """
        # TODO: Create feature interactions
        # TODO: Create polynomial features
        # TODO: Create derived features
        # return df
        pass
    
    def select_features(self, X, y, method='correlation'):
        """
        Select important features.
        
        TODO: Implement feature selection
        """
        # TODO: Select features based on correlation with target
        # TODO: Or use feature importance from a model
        # return selected_features
        pass


class ModelTrainer:
    """Handles model training and evaluation."""
    
    def __init__(self):
        self.models = {}
    
    def train_models(self, X_train, y_train):
        """
        Train multiple models.
        
        TODO: Train at least 3 different models
        """
        # TODO: Train RandomForest
        # TODO: Train other models (e.g., LogisticRegression, SVM)
        # TODO: Store models in self.models dictionary
        pass
    
    def evaluate_models(self, models, X_test, y_test):
        """
        Evaluate all models.
        
        TODO: Evaluate each model and return results
        """
        # TODO: For each model, calculate accuracy
        # TODO: Generate classification report
        # TODO: Return comparison results
        pass
    
    def save_model(self, model, filepath):
        """
        Save trained model.
        
        TODO: Save model using joblib
        """
        # TODO: Save model using joblib.dump()
        pass


class MLPipeline:
    """Complete ML pipeline class."""
    
    def __init__(self):
        self.data_loader = DataLoader()
        self.preprocessor = Preprocessor()
        self.feature_engineer = FeatureEngineer()
        self.model_trainer = ModelTrainer()
        self.is_fitted = False
    
    def fit(self, X, y):
        """
        Fit the complete pipeline.
        
        TODO: Implement complete pipeline fitting
        """
        # TODO: Preprocess data
        # TODO: Engineer features
        # TODO: Split data
        # TODO: Train models
        # TODO: Set is_fitted = True
        pass
    
    def predict(self, X):
        """
        Make predictions using fitted pipeline.
        
        TODO: Implement prediction
        """
        # TODO: Check if pipeline is fitted
        # TODO: Preprocess new data
        # TODO: Engineer features
        # TODO: Make predictions using best model
        # return predictions
        pass
    
    def save_pipeline(self, filepath):
        """
        Save the complete pipeline.
        
        TODO: Save all components
        """
        # TODO: Save models and preprocessors
        pass


def main():
    """
    Main execution function.
    
    TODO: Implement complete workflow
    """
    # TODO: Initialize pipeline
    # TODO: Load data
    # TODO: Fit pipeline
    # TODO: Make predictions
    # TODO: Evaluate results
    
    logger.info("ML Pipeline execution complete!")


if __name__ == "__main__":
    main()

