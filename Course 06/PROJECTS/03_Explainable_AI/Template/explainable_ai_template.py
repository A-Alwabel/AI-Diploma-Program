"""
Explainable AI Tool Template
Project 03 Template

Fill in the functions marked with TODO comments.
Requires: pip install shap lime pandas scikit-learn matplotlib
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# SHAP for model explanations
try:
    import shap
    SHAP_AVAILABLE = True
except ImportError:
    SHAP_AVAILABLE = False
    print("SHAP not installed. Install with: pip install shap")

# LIME for local explanations
try:
    from lime import lime_tabular
    from lime.lime_tabular import LimeTabularExplainer
    LIME_AVAILABLE = True
except ImportError:
    LIME_AVAILABLE = False
    print("LIME not installed. Install with: pip install lime")


class ModelExplainer:
    """Explains ML model decisions."""
    
    def __init__(self, model, X_train, feature_names):
        self.model = model
        self.X_train = X_train
        self.feature_names = feature_names
    
    def explain_with_shap(self, X_test, plot_type='summary'):
        """
        Generate SHAP explanations.
        
        TODO: Implement SHAP explanations
        """
        if not SHAP_AVAILABLE:
            print("SHAP not available")
            return None
        
        # TODO: Create SHAP explainer
        # explainer = shap.TreeExplainer(self.model)
        # shap_values = explainer.shap_values(X_test)
        
        # TODO: Create plots
        # if plot_type == 'summary':
        #     shap.summary_plot(shap_values, X_test)
        # elif plot_type == 'waterfall':
        #     shap.waterfall_plot(...)
        
        pass
    
    def explain_with_lime(self, instance, num_features=10):
        """
        Generate LIME explanation for a single instance.
        
        TODO: Implement LIME local explanation
        """
        if not LIME_AVAILABLE:
            print("LIME not available")
            return None
        
        # TODO: Create LIME explainer
        # explainer = LimeTabularExplainer(
        #     self.X_train,
        #     feature_names=self.feature_names,
        #     mode='classification'
        # )
        
        # TODO: Explain instance
        # explanation = explainer.explain_instance(
        #     instance,
        #     self.model.predict_proba,
        #     num_features=num_features
        # )
        
        # TODO: Return explanation
        pass
    
    def feature_importance(self):
        """
        Get feature importance from model.
        
        TODO: Extract and visualize feature importance
        """
        # TODO: Get feature importance (if available)
        # TODO: Create bar plot
        pass


class ExplanationVisualizer:
    """Visualizes model explanations."""
    
    def plot_shap_summary(self, shap_values, X_test):
        """
        Plot SHAP summary.
        
        TODO: Create SHAP summary plot
        """
        # TODO: Use shap.summary_plot()
        pass
    
    def plot_lime_explanation(self, explanation):
        """
        Plot LIME explanation.
        
        TODO: Visualize LIME explanation
        """
        # TODO: Use explanation.show_in_notebook() or create custom plot
        pass


class ExplanationReporter:
    """Generates explanation reports."""
    
    def generate_report(self, explanations, model_name):
        """
        Generate explanation report.
        
        TODO: Create formatted explanation report
        """
        # TODO: Format explanations
        # TODO: Add model information
        # TODO: Save to file
        pass


def main():
    """
    Main execution function.
    
    TODO: Implement complete explainable AI workflow
    """
    # TODO: Load data and train model
    # TODO: Initialize ModelExplainer
    # TODO: Generate SHAP explanations
    # TODO: Generate LIME explanations
    # TODO: Create visualizations
    # TODO: Generate report
    
    print("Explainable AI tool complete!")


if __name__ == "__main__":
    main()

