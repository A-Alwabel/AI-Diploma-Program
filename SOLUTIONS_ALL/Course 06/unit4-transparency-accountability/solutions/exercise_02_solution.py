"""
Unit 4 - Exercise 2: Solution
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Task 1: Feature Importance
def analyze_feature_importance(model, feature_names, top_n=5):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1][:top_n]
    
    results = pd.DataFrame({
        'feature': [feature_names[i] for i in indices],
        'importance': importances[indices]
    })
    return results

def compare_model_interpretability(models_dict, X_test, y_test):
    results = []
    for name, model in models_dict.items():
        acc = accuracy_score(y_test, model.predict(X_test))
        interpretability = 'High' if hasattr(model, 'coef_') else 'Medium'
        results.append({
            'model': name,
            'accuracy': acc,
            'interpretability': interpretability
        })
    return pd.DataFrame(results)

# Task 2: Global vs Local
def global_interpretability_analysis(model, X_train, feature_names):
    importances = model.feature_importances_
    global_insights = {
        'top_features': [feature_names[i] for i in np.argsort(importances)[::-1][:3]],
        'feature_importance': dict(zip(feature_names, importances))
    }
    return global_insights

def local_interpretability_analysis(model, X_sample, X_train, feature_names):
    # Simple local explanation using feature contributions
    prediction = model.predict(X_sample.reshape(1, -1))[0]
    proba = model.predict_proba(X_sample.reshape(1, -1))[0]
    
    # Feature contributions (simplified)
    importances = model.feature_importances_
    contributions = X_sample * importances
    
    local_explanation = {
        'prediction': prediction,
        'confidence': max(proba),
        'feature_contributions': dict(zip(feature_names, contributions))
    }
    return local_explanation

# Task 3: Accountability Framework
def design_accountability_framework(model, X_test, y_test, threshold=0.8):
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)
    confidences = np.max(probabilities, axis=1)
    
    # Flag low-confidence predictions
    low_confidence = confidences < threshold
    high_confidence = confidences >= threshold
    
    report = {
        'total_predictions': len(predictions),
        'high_confidence': np.sum(high_confidence),
        'low_confidence': np.sum(low_confidence),
        'requires_review': np.sum(low_confidence),
        'high_confidence_accuracy': accuracy_score(
            y_test[high_confidence], 
            predictions[high_confidence]
        ) if np.sum(high_confidence) > 0 else 0
    }
    return report

def create_decision_log(model, X_test, predictions, metadata=None):
    probabilities = model.predict_proba(X_test)
    confidences = np.max(probabilities, axis=1)
    
    log_data = {
        'prediction': predictions,
        'confidence': confidences,
        'predicted_class_0_prob': probabilities[:, 0],
        'predicted_class_1_prob': probabilities[:, 1]
    }
    
    # Add feature values
    for i in range(X_test.shape[1]):
        log_data[f'feature_{i}'] = X_test[:, i]
    
    # Add metadata
    if metadata:
        for key, value in metadata.items():
            log_data[key] = value
    
    return pd.DataFrame(log_data)

# Task 4: Transparency Metrics
def calculate_transparency_metrics(model, X_train, X_test, feature_names):
    # Feature importance consistency
    importances = model.feature_importances_
    importance_std = np.std(importances)
    
    # Prediction stability (variance in predictions)
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    stability = 1 - (np.var(train_pred) + np.var(test_pred)) / 2
    
    # Explainability score (based on model type)
    explainability = 1.0 if hasattr(model, 'coef_') else 0.7
    
    metrics = {
        'feature_importance_consistency': 1 / (1 + importance_std),
        'prediction_stability': stability,
        'explainability_score': explainability,
        'overall_transparency': (1 / (1 + importance_std) + stability + explainability) / 3
    }
    return metrics

if __name__ == "__main__":
    print("="*80)
    print("Unit 4 - Exercise 2: Solution")
    print("="*80)
    
    # Generate data
    np.random.seed(42)
    n_samples = 1000
    X = np.random.randn(n_samples, 5)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    
    feature_names = [f'feature_{i}' for i in range(5)]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train models
    rf_model = RandomForestClassifier(n_estimators=50, random_state=42)
    rf_model.fit(X_train, y_train)
    
    lr_model = LogisticRegression(random_state=42)
    lr_model.fit(X_train, y_train)
    
    # Task 1
    print("\nTask 1: Feature Importance")
    top_features = analyze_feature_importance(rf_model, feature_names, top_n=3)
    print(top_features)
    
    models_dict = {'Random Forest': rf_model, 'Logistic Regression': lr_model}
    comparison = compare_model_interpretability(models_dict, X_test, y_test)
    print("\nModel Comparison:")
    print(comparison)
    
    # Task 2
    print("\nTask 2: Global vs Local Interpretability")
    global_insights = global_interpretability_analysis(rf_model, X_train, feature_names)
    print(f"Top features globally: {global_insights['top_features']}")
    
    sample_idx = 0
    local_explanation = local_interpretability_analysis(
        rf_model, X_test[sample_idx], X_train, feature_names
    )
    print(f"\nLocal explanation for sample {sample_idx}:")
    print(f"Prediction: {local_explanation['prediction']}")
    print(f"Confidence: {local_explanation['confidence']:.4f}")
    
    # Task 3
    print("\nTask 3: Accountability Framework")
    accountability_report = design_accountability_framework(
        rf_model, X_test, y_test, threshold=0.8
    )
    print(accountability_report)
    
    decision_log = create_decision_log(
        rf_model, X_test[:10], rf_model.predict(X_test[:10]),
        metadata={'model_version': '1.0', 'timestamp': '2025-12-01'}
    )
    print("\nDecision Log (first 10):")
    print(decision_log.head())
    
    # Task 4
    print("\nTask 4: Transparency Metrics")
    transparency_metrics = calculate_transparency_metrics(
        rf_model, X_train, X_test, feature_names
    )
    print(transparency_metrics)
    
    print("\n" + "="*80)
    print("Solution Complete!")
    print("="*80)

