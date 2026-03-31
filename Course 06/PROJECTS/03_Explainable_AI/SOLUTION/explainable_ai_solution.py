"""
Explainable AI - Complete Solution
SHAP and LIME implementations for model interpretability
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')

# Try to import SHAP and LIME, provide fallback if not available
try:
    import shap
    SHAP_AVAILABLE = True
except ImportError:
    SHAP_AVAILABLE = False
    print("⚠️  SHAP not installed. Install with: pip install shap")

try:
    from lime import lime_tabular
    LIME_AVAILABLE = True
except ImportError:
    LIME_AVAILABLE = False
    print("⚠️  LIME not installed. Install with: pip install lime")

def load_data():
    """Load and prepare data."""
    X, y = make_classification(n_samples=500, n_features=5, n_informative=3,
                              n_redundant=1, n_classes=2, random_state=42)
    
    feature_names = [f'Feature_{i+1}' for i in range(X.shape[1])]
    df = pd.DataFrame(X, columns=feature_names)
    
    return X, y, df, feature_names

def train_model(X_train, y_train):
    """Train a random forest model."""
    model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
    model.fit(X_train, y_train)
    return model

def shap_explanations(model, X_train, X_test, feature_names):
    """Generate SHAP explanations."""
    if not SHAP_AVAILABLE:
        print("SHAP not available. Skipping SHAP explanations.")
        return None
    
    print("\nGenerating SHAP explanations...")
    
    # Create SHAP explainer
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test[:10])  # Explain first 10 samples
    
    # Summary plot
    plt.figure(figsize=(10, 6))
    shap.summary_plot(shap_values, X_test[:10], feature_names=feature_names, 
                     show=False, plot_type="bar")
    plt.title("SHAP Summary Plot - Feature Importance", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    # Waterfall plot for first sample
    plt.figure(figsize=(10, 6))
    shap.waterfall_plot(shap.Explanation(values=shap_values[0], 
                                         base_values=explainer.expected_value[0],
                                         data=X_test[0], 
                                         feature_names=feature_names),
                      show=False)
    plt.title("SHAP Waterfall Plot - Sample 0", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    return shap_values

def lime_explanations(model, X_train, X_test, feature_names, class_names):
    """Generate LIME explanations."""
    if not LIME_AVAILABLE:
        print("LIME not available. Skipping LIME explanations.")
        return None
    
    print("\nGenerating LIME explanations...")
    
    # Create LIME explainer
    explainer = lime_tabular.LimeTabularExplainer(
        X_train, 
        feature_names=feature_names,
        class_names=class_names,
        mode='classification'
    )
    
    # Explain first few samples
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.flatten()
    
    for i in range(min(4, len(X_test))):
        explanation = explainer.explain_instance(
            X_test[i], 
            model.predict_proba, 
            num_features=5
        )
        
        # Get explanation data
        exp_list = explanation.as_list()
        features = [x[0] for x in exp_list]
        values = [x[1] for x in exp_list]
        
        # Create bar plot
        colors = ['red' if v < 0 else 'green' for v in values]
        axes[i].barh(features, values, color=colors)
        axes[i].set_title(f'LIME Explanation - Sample {i}')
        axes[i].set_xlabel('Feature Contribution')
        axes[i].axvline(x=0, color='black', linestyle='--', linewidth=0.5)
        axes[i].grid(True, alpha=0.3, axis='x')
    
    plt.suptitle('LIME Explanations for Multiple Samples', 
                fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    return explanation

def feature_importance_plot(model, feature_names):
    """Plot traditional feature importance."""
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(importances)), importances[indices])
    plt.xticks(range(len(importances)), 
              [feature_names[i] for i in indices], rotation=45)
    plt.xlabel('Feature')
    plt.ylabel('Importance')
    plt.title('Feature Importance (Random Forest)', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run explainable AI solution."""
    print("Explainable AI - Complete Solution")
    print("=" * 60)
    
    # Load data
    print("\n1. Loading data...")
    X, y, df, feature_names = load_data()
    print(f"   Data shape: {X.shape}")
    print(f"   Features: {feature_names}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    print("\n2. Training model...")
    model = train_model(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"   Model accuracy: {accuracy:.4f}")
    
    # Feature importance
    print("\n3. Feature importance...")
    feature_importance_plot(model, feature_names)
    
    # SHAP explanations
    if SHAP_AVAILABLE:
        print("\n4. SHAP explanations...")
        shap_explanations(model, X_train, X_test, feature_names)
    else:
        print("\n4. SHAP explanations skipped (not installed)")
    
    # LIME explanations
    if LIME_AVAILABLE:
        print("\n5. LIME explanations...")
        class_names = ['Class 0', 'Class 1']
        lime_explanations(model, X_train, X_test, feature_names, class_names)
    else:
        print("\n5. LIME explanations skipped (not installed)")
    
    print("\n" + "=" * 60)
    print("✅ Demo complete!")
    print("\nNote: Install SHAP and LIME for full functionality:")
    print("  pip install shap lime")

if __name__ == "__main__":
    main()
