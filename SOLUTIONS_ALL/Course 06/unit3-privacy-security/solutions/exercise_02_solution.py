"""
Unit 3 - Exercise 2: Solution
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Task 1: k-anonymity
def check_k_anonymity(df, quasi_identifiers, k=3):
    grouped = df.groupby(quasi_identifiers).size()
    return all(grouped >= k)

def achieve_k_anonymity(df, quasi_identifiers, k=3):
    df_anon = df.copy()
    # Generalize age
    df_anon['age'] = (df_anon['age'] // 10) * 10
    # Generalize zipcode (first 3 digits)
    df_anon['zipcode'] = (df_anon['zipcode'] // 100) * 100
    return df_anon

# Task 2: Federated Learning
def simulate_federated_learning(X_train, y_train, n_clients=3):
    from sklearn.linear_model import LogisticRegression
    
    # Split data
    client_data = np.array_split(X_train, n_clients)
    client_labels = np.array_split(y_train, n_clients)
    
    # Train on each client
    models = []
    for X_client, y_client in zip(client_data, client_labels):
        model = LogisticRegression(random_state=42)
        model.fit(X_client, y_client)
        models.append(model)
    
    # Aggregate (simple average of coefficients)
    aggregated_coef = np.mean([m.coef_ for m in models], axis=0)
    aggregated_intercept = np.mean([m.intercept_ for m in models], axis=0)
    
    # Create aggregated model
    aggregated_model = LogisticRegression(random_state=42)
    aggregated_model.coef_ = aggregated_coef
    aggregated_model.intercept_ = aggregated_intercept
    aggregated_model.classes_ = models[0].classes_
    
    return aggregated_model

# Task 3: Security vulnerabilities
def detect_adversarial_vulnerability(model, X_test, y_test, epsilon=0.1):
    # Original accuracy
    y_pred_orig = model.predict(X_test)
    acc_orig = accuracy_score(y_test, y_pred_orig)
    
    # Add adversarial noise
    X_adv = X_test + np.random.normal(0, epsilon, X_test.shape)
    y_pred_adv = model.predict(X_adv)
    acc_adv = accuracy_score(y_test, y_pred_adv)
    
    vulnerability = acc_orig - acc_adv
    return vulnerability

def detect_membership_inference_risk(model, X_train, X_test):
    # Prediction confidence on training data
    train_probs = model.predict_proba(X_train)
    train_confidence = np.max(train_probs, axis=1).mean()
    
    # Prediction confidence on test data
    test_probs = model.predict_proba(X_test)
    test_confidence = np.max(test_probs, axis=1).mean()
    
    # Risk: higher confidence on training indicates vulnerability
    risk = train_confidence - test_confidence
    return risk

# Task 4: Privacy-Utility Trade-off
def analyze_privacy_utility_tradeoff(X, y, epsilon_values=[0.1, 0.5, 1.0, 2.0]):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    results = []
    for epsilon in epsilon_values:
        # Add Laplace noise
        sensitivity = 1.0
        noise_scale = sensitivity / epsilon
        X_train_noisy = X_train + np.random.laplace(0, noise_scale, X_train.shape)
        
        # Train model
        model = RandomForestClassifier(n_estimators=50, random_state=42)
        model.fit(X_train_noisy, y_train)
        
        # Evaluate
        acc = accuracy_score(y_test, model.predict(X_test))
        results.append({'epsilon': epsilon, 'accuracy': acc})
    
    return pd.DataFrame(results)

if __name__ == "__main__":
    print("="*80)
    print("Unit 3 - Exercise 2: Solution")
    print("="*80)
    
    # Sample data
    np.random.seed(42)
    n_samples = 1000
    data = {
        'age': np.random.randint(18, 80, n_samples),
        'zipcode': np.random.randint(10000, 99999, n_samples),
        'income': np.random.normal(50000, 15000, n_samples),
        'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_samples),
        'target': np.random.choice([0, 1], n_samples)
    }
    df = pd.DataFrame(data)
    
    # Task 1
    print("\nTask 1: k-anonymity")
    quasi_ids = ['age', 'zipcode']
    is_k_anon = check_k_anonymity(df, quasi_ids, k=3)
    print(f"k-anonymity (k=3): {is_k_anon}")
    
    df_anon = achieve_k_anonymity(df, quasi_ids, k=3)
    is_k_anon_after = check_k_anonymity(df_anon, quasi_ids, k=3)
    print(f"k-anonymity after generalization: {is_k_anon_after}")
    
    # Task 2
    print("\nTask 2: Federated Learning")
    X = df[['age', 'zipcode', 'income']].values
    y = df['target'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    federated_model = simulate_federated_learning(X_train, y_train, n_clients=3)
    federated_acc = accuracy_score(y_test, federated_model.predict(X_test))
    print(f"Federated model accuracy: {federated_acc:.4f}")
    
    # Task 3
    print("\nTask 3: Security Vulnerabilities")
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    
    vulnerability = detect_adversarial_vulnerability(model, X_test, y_test, epsilon=0.1)
    print(f"Adversarial vulnerability: {vulnerability:.4f}")
    
    risk = detect_membership_inference_risk(model, X_train, X_test)
    print(f"Membership inference risk: {risk:.4f}")
    
    # Task 4
    print("\nTask 4: Privacy-Utility Trade-off")
    tradeoff_results = analyze_privacy_utility_tradeoff(X, y)
    print(tradeoff_results)
    
    print("\n" + "="*80)
    print("Solution Complete!")
    print("="*80)

