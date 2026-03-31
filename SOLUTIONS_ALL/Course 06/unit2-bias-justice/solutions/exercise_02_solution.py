"""
Unit 2: Bias, Justice, and Discrimination in AI
Exercise 2 Solution: Bias Mitigation Techniques

Complete solution for the bias mitigation exercise.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from fairlearn.metrics import demographic_parity_difference, equalized_odds_difference

# ============================================================================
# SOLUTION 1: Generate Biased Dataset
# ============================================================================

def generate_biased_dataset(n_samples=2000):
    """
    Generate a synthetic dataset with bias.
    """
    np.random.seed(42)
    
    # Sensitive attribute (e.g., gender: 0 = group A, 1 = group B)
    sensitive = np.random.binomial(1, 0.5, n_samples)
    
    # Features
    X1 = np.random.normal(0, 1, n_samples)
    X2 = np.random.normal(0, 1, n_samples)
    
    # Introduce bias: group B has lower probability of positive outcome
    true_prob = 0.3 + 0.4 * X1 + 0.3 * X2
    bias_penalty = 0.3 * (1 - sensitive)  # Group B (0) gets penalty
    prob = true_prob - bias_penalty + np.random.normal(0, 0.1, n_samples)
    prob = np.clip(prob, 0, 1)
    
    # Target variable
    y = (prob > 0.5).astype(int)
    
    # Create DataFrame
    df = pd.DataFrame({
        'feature1': X1,
        'feature2': X2,
        'sensitive': sensitive,
        'target': y
    })
    
    return df

# ============================================================================
# SOLUTION 2: Implement Pre-processing Bias Mitigation
# ============================================================================

def preprocess_reweighing(X_train, y_train, sensitive_train):
    """
    Implement reweighing technique.
    """
    # Calculate weights to balance groups
    group_counts = pd.Series(sensitive_train).value_counts()
    total = len(sensitive_train)
    
    weights = np.ones(len(sensitive_train))
    for group in group_counts.index:
        group_size = group_counts[group]
        # Weight inversely proportional to group size
        weights[sensitive_train == group] = total / (len(group_counts) * group_size)
    
    return weights

# ============================================================================
# SOLUTION 3: Train Models with Different Mitigation Techniques
# ============================================================================

def train_baseline_model(X_train, y_train):
    """
    Train a baseline model without any bias mitigation.
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    return model, scaler

def train_reweighed_model(X_train, y_train, sensitive_train):
    """
    Train a model using reweighing technique.
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    # Get weights from reweighing
    weights = preprocess_reweighing(X_train_scaled, y_train, sensitive_train)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train, sample_weight=weights)
    
    return model, scaler

# ============================================================================
# SOLUTION 4: Evaluate Fairness Metrics
# ============================================================================

def evaluate_fairness(y_true, y_pred, sensitive):
    """
    Evaluate fairness metrics.
    """
    metrics = {
        'demographic_parity_diff': demographic_parity_difference(
            y_true, y_pred, sensitive_features=sensitive
        ),
        'equalized_odds_diff': equalized_odds_difference(
            y_true, y_pred, sensitive_features=sensitive
        ),
        'accuracy': accuracy_score(y_true, y_pred)
    }
    
    return metrics

# ============================================================================
# SOLUTION 5: Compare Techniques
# ============================================================================

def compare_mitigation_techniques(df):
    """
    Compare baseline vs reweighing techniques.
    """
    # Prepare data
    X = df[['feature1', 'feature2']].values
    y = df['target'].values
    sensitive = df['sensitive'].values
    
    # Split data
    X_train, X_test, y_train, y_test, sensitive_train, sensitive_test = train_test_split(
        X, y, sensitive, test_size=0.3, random_state=42, stratify=y
    )
    
    print("\n" + "="*80)
    print("BASELINE MODEL (No Mitigation)")
    print("="*80)
    
    # Train baseline model
    baseline_model, baseline_scaler = train_baseline_model(X_train, y_train)
    X_test_scaled = baseline_scaler.transform(X_test)
    y_pred_baseline = baseline_model.predict(X_test_scaled)
    
    # Evaluate baseline
    baseline_metrics = evaluate_fairness(y_test, y_pred_baseline, sensitive_test)
    print(f"Accuracy: {baseline_metrics['accuracy']:.4f}")
    print(f"Demographic Parity Difference: {baseline_metrics['demographic_parity_diff']:.4f}")
    print(f"Equalized Odds Difference: {baseline_metrics['equalized_odds_diff']:.4f}")
    
    print("\n" + "="*80)
    print("REWEIGHING MODEL")
    print("="*80)
    
    # Train reweighed model
    reweigh_model, reweigh_scaler = train_reweighed_model(X_train, y_train, sensitive_train)
    X_test_reweigh = reweigh_scaler.transform(X_test)
    y_pred_reweigh = reweigh_model.predict(X_test_reweigh)
    
    # Evaluate reweighing
    reweigh_metrics = evaluate_fairness(y_test, y_pred_reweigh, sensitive_test)
    print(f"Accuracy: {reweigh_metrics['accuracy']:.4f}")
    print(f"Demographic Parity Difference: {reweigh_metrics['demographic_parity_diff']:.4f}")
    print(f"Equalized Odds Difference: {reweigh_metrics['equalized_odds_diff']:.4f}")
    
    # Comparison
    print("\n" + "="*80)
    print("COMPARISON")
    print("="*80)
    print(f"Demographic Parity Improvement: "
          f"{abs(baseline_metrics['demographic_parity_diff']) - abs(reweigh_metrics['demographic_parity_diff']):.4f}")
    print(f"Equalized Odds Improvement: "
          f"{abs(baseline_metrics['equalized_odds_diff']) - abs(reweigh_metrics['equalized_odds_diff']):.4f}")
    print(f"Accuracy Change: {reweigh_metrics['accuracy'] - baseline_metrics['accuracy']:.4f}")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 2 - Exercise 2 Solution: Bias Mitigation Techniques")
    print("="*80)
    
    # Generate dataset
    print("\nGenerating biased dataset...")
    df = generate_biased_dataset()
    print(f"Dataset shape: {df.shape}")
    print(f"\nSensitive attribute distribution:")
    print(df['sensitive'].value_counts())
    print(f"\nTarget distribution:")
    print(df['target'].value_counts())
    
    # Compare techniques
    compare_mitigation_techniques(df)
    
    print("\n" + "="*80)
    print("Solution completed!")
    print("="*80)

