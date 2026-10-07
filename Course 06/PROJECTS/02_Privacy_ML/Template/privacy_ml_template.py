"""
Privacy-Preserving ML System Template
Project 02 Template

Fill in the functions marked with TODO comments.
Requires: pip install diffprivlib pandas scikit-learn
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Differential Privacy
try:
    from diffprivlib.models import LogisticRegression as DP_LogisticRegression
    DIFFPRIV_AVAILABLE = True
except ImportError:
    DIFFPRIV_AVAILABLE = False
    print("diffprivlib not installed. Install with: pip install diffprivlib")


class PrivacyTechniques:
    """Implements privacy-preserving techniques."""
    
    def anonymize_data(self, df, sensitive_columns):
        """
        Anonymize sensitive data.
        
        TODO: Implement data anonymization
        """
        # TODO: Remove or mask PII
        # TODO: Generalize quasi-identifiers
        # TODO: Apply k-anonymity if possible
        pass
    
    def apply_differential_privacy(self, epsilon=1.0):
        """
        Apply differential privacy to model training.
        
        TODO: Train model with differential privacy
        """
        if not DIFFPRIV_AVAILABLE:
            print("diffprivlib not available")
            return None
        
        # TODO: Create DP model
        # dp_model = DP_LogisticRegression(epsilon=epsilon)
        # return dp_model
        pass


class PrivateML:
    """Trains ML models with privacy constraints."""
    
    def train_private_model(self, X_train, y_train, epsilon=1.0):
        """
        Train model with differential privacy.
        
        TODO: Train model with privacy constraints
        """
        # TODO: Use diffprivlib models
        # TODO: Train with specified epsilon
        pass
    
    def evaluate_privacy_utility(self, private_model, non_private_model, 
                                 X_test, y_test):
        """
        Evaluate privacy-utility tradeoff.
        
        TODO: Compare private vs non-private model performance
        """
        # TODO: Evaluate both models
        # TODO: Calculate accuracy difference
        # TODO: Plot privacy-utility tradeoff
        pass


class ComplianceChecker:
    """Checks GDPR compliance."""
    
    def check_data_minimization(self, df):
        """
        Check if data minimization is followed.
        
        TODO: Verify only necessary data is collected
        """
        # TODO: Check if all columns are necessary
        pass
    
    def document_data_handling(self, data_operations):
        """
        Document all data handling operations.
        
        TODO: Create compliance documentation
        """
        # TODO: Document data sources
        # TODO: Document processing steps
        # TODO: Document retention policies
        pass


def main():
    """
    Main execution function.
    
    TODO: Implement complete privacy-preserving ML workflow
    """
    # TODO: Load data
    # TODO: Anonymize data
    # TODO: Train private model
    # TODO: Train non-private model (for comparison)
    # TODO: Evaluate privacy-utility tradeoff
    # TODO: Check compliance
    
    print("Privacy-preserving ML system complete!")


if __name__ == "__main__":
    main()

