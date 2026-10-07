"""
Machine Learning Classifier Template
Project 03 Template

Fill in the functions marked with TODO comments.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filename=None):
    """
    Load dataset.
    
    TODO: Load data from file or use built-in dataset
    - If filename provided, load from CSV
    - Otherwise, use built-in dataset (e.g., Iris)
    - Return X (features) and y (target)
    """
    # TODO: Load data
    # Option 1: From CSV file
    # df = pd.read_csv(filename)
    # X = df.drop('target', axis=1)
    # y = df['target']
    
    # Option 2: Built-in dataset
    # from sklearn.datasets import load_iris
    # iris = load_iris()
    # X, y = iris.data, iris.target
    
    # TODO: Return X and y
    return None, None


def preprocess_data(X, y):
    """
    Preprocess data.
    
    TODO: Preprocess data
    - Handle missing values
    - Encode categorical variables (if any)
    - Scale/normalize features (if needed)
    - Return processed X and y
    """
    # TODO: Handle missing values
    # X = X.fillna(X.mean())  # or other strategy
    
    # TODO: Encode categorical variables if needed
    # from sklearn.preprocessing import LabelEncoder
    # le = LabelEncoder()
    # y = le.fit_transform(y)
    
    # TODO: Scale features if needed
    # from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler()
    # X = scaler.fit_transform(X)
    
    # TODO: Return processed X and y
    return X, y


def split_data(X, y, test_size=0.2):
    """
    Split data into train and test sets.
    
    TODO: Split data
    - Use train_test_split
    - Return X_train, X_test, y_train, y_test
    """
    # TODO: Split data
    # X_train, X_test, y_train, y_test = train_test_split(
    #     X, y, test_size=test_size, random_state=42, stratify=y
    # )
    
    # TODO: Return splits
    return None, None, None, None


def create_models():
    """
    Create model instances.
    
    TODO: Create and return dictionary of models
    """
    models = {
        'Logistic Regression': None,  # Replace with LogisticRegression()
        'Decision Tree': None,  # Replace with DecisionTreeClassifier()
        'KNN': None  # Replace with KNeighborsClassifier(n_neighbors=3)
    }
    
    # TODO: Create model instances
    # models['Logistic Regression'] = LogisticRegression(max_iter=200)
    # models['Decision Tree'] = DecisionTreeClassifier()
    # models['KNN'] = KNeighborsClassifier(n_neighbors=3)
    
    return models


def train_models(models, X_train, y_train):
    """
    Train all models.
    
    TODO: Train each model on training data
    """
    # TODO: For each model, fit on training data
    # for name, model in models.items():
    #     model.fit(X_train, y_train)
    #     print(f"{name} trained successfully")
    pass


def evaluate_model(model, X_test, y_test, model_name):
    """
    Evaluate a single model.
    
    TODO: Evaluate model and return metrics
    - Make predictions
    - Calculate accuracy
    - Create confusion matrix
    - Return metrics dictionary
    """
    # TODO: Make predictions
    # y_pred = model.predict(X_test)
    
    # TODO: Calculate metrics
    # accuracy = accuracy_score(y_test, y_pred)
    # report = classification_report(y_test, y_pred)
    # cm = confusion_matrix(y_test, y_pred)
    
    # TODO: Return metrics
    return {
        'accuracy': 0.0,
        'predictions': None,
        'confusion_matrix': None
    }


def visualize_results(results):
    """
    Visualize model comparison.
    
    TODO: Create visualizations
    - Bar chart comparing accuracies
    - Confusion matrices for each model
    """
    # TODO: Extract accuracies
    # accuracies = [r['accuracy'] for r in results.values()]
    # model_names = list(results.keys())
    
    # TODO: Create bar chart
    # plt.figure(figsize=(10, 6))
    # plt.bar(model_names, accuracies)
    # plt.title('Model Comparison')
    # plt.ylabel('Accuracy')
    # plt.show()
    
    # TODO: Create confusion matrices
    # for name, result in results.items():
    #     cm = result['confusion_matrix']
    #     sns.heatmap(cm, annot=True, fmt='d')
    #     plt.title(f'Confusion Matrix - {name}')
    #     plt.show()
    pass


def main():
    """Main function to run ML pipeline."""
    print("=" * 70)
    print("Machine Learning Classifier Pipeline")
    print("=" * 70)
    
    # Step 1: Load data
    print("\n1. Loading data...")
    X, y = load_data()  # TODO: Provide filename if using CSV
    print(f"   Data shape: {X.shape if X is not None else 'Not loaded'}")
    
    # Step 2: Preprocess
    print("\n2. Preprocessing data...")
    X, y = preprocess_data(X, y)
    
    # Step 3: Split data
    print("\n3. Splitting data...")
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Step 4: Create models
    print("\n4. Creating models...")
    models = create_models()
    
    # Step 5: Train models
    print("\n5. Training models...")
    train_models(models, X_train, y_train)
    
    # Step 6: Evaluate models
    print("\n6. Evaluating models...")
    results = {}
    for name, model in models.items():
        results[name] = evaluate_model(model, X_test, y_test, name)
        print(f"   {name} accuracy: {results[name]['accuracy']:.2f}")
    
    # Step 7: Visualize
    print("\n7. Visualizing results...")
    visualize_results(results)
    
    # Step 8: Compare and recommend
    print("\n8. Model Comparison:")
    best_model = max(results.items(), key=lambda x: x[1]['accuracy'])
    print(f"   Best model: {best_model[0]} (Accuracy: {best_model[1]['accuracy']:.2f})")


if __name__ == "__main__":
    main()

