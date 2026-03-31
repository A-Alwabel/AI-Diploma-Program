"""
ML Classifier - Complete Solution
Multiple classification algorithms with evaluation and visualization
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix, 
                            classification_report, roc_curve, auc)
from sklearn.preprocessing import label_binarize
import seaborn as sns

def load_data():
    """Load and prepare classification data."""
    # Generate synthetic dataset
    X, y = make_classification(n_samples=1000, n_features=4, n_informative=3,
                              n_redundant=1, n_classes=3, n_clusters_per_class=1,
                              random_state=42)
    
    # Convert to DataFrame for better visualization
    feature_names = [f'Feature_{i+1}' for i in range(X.shape[1])]
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y
    
    return X, y, df

def train_classifiers(X_train, y_train):
    """Train multiple classifiers."""
    classifiers = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=5),
        'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5)
    }
    
    trained_models = {}
    for name, clf in classifiers.items():
        print(f"Training {name}...")
        clf.fit(X_train, y_train)
        trained_models[name] = clf
    
    return trained_models

def evaluate_classifiers(models, X_test, y_test):
    """Evaluate all classifiers."""
    results = {}
    
    for name, model in models.items():
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        
        results[name] = {
            'model': model,
            'accuracy': accuracy,
            'confusion_matrix': cm,
            'predictions': y_pred
        }
        
        print(f"\n{name}:")
        print(f"  Accuracy: {accuracy:.4f}")
        print(f"  Confusion Matrix:\n{cm}")
    
    return results

def visualize_results(results, X_test, y_test):
    """Visualize classification results."""
    n_models = len(results)
    fig, axes = plt.subplots(2, n_models, figsize=(5*n_models, 10))
    
    if n_models == 1:
        axes = axes.reshape(2, 1)
    
    for idx, (name, result) in enumerate(results.items()):
        # Confusion Matrix
        sns.heatmap(result['confusion_matrix'], annot=True, fmt='d', 
                   cmap='Blues', ax=axes[0, idx])
        axes[0, idx].set_title(f'{name}\nAccuracy: {result["accuracy"]:.4f}')
        axes[0, idx].set_ylabel('True Label')
        axes[0, idx].set_xlabel('Predicted Label')
        
        # Classification Report (text)
        report = classification_report(y_test, result['predictions'], 
                                      output_dict=True)
        axes[1, idx].axis('off')
        report_text = f"{name}\n\n"
        report_text += f"Accuracy: {result['accuracy']:.4f}\n\n"
        for class_label in sorted([k for k in report.keys() if k.isdigit()]):
            report_text += f"Class {class_label}:\n"
            report_text += f"  Precision: {report[class_label]['precision']:.3f}\n"
            report_text += f"  Recall: {report[class_label]['recall']:.3f}\n"
            report_text += f"  F1: {report[class_label]['f1-score']:.3f}\n\n"
        axes[1, idx].text(0.1, 0.5, report_text, fontsize=10, 
                         family='monospace', verticalalignment='center')
    
    plt.tight_layout()
    plt.show()

def plot_roc_curves(models, X_test, y_test):
    """Plot ROC curves for all classifiers."""
    plt.figure(figsize=(10, 8))
    
    # Binarize labels for multi-class ROC
    y_test_bin = label_binarize(y_test, classes=[0, 1, 2])
    n_classes = y_test_bin.shape[1]
    
    for name, model in models.items():
        # Get probability predictions
        y_score = model.predict_proba(X_test)
        
        # Compute ROC for each class
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, i], y_score[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])
        
        # Plot ROC for each class
        for i in range(n_classes):
            plt.plot(fpr[i], tpr[i], 
                    label=f'{name} - Class {i} (AUC = {roc_auc[i]:.2f})',
                    linewidth=2)
    
    plt.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves - Multi-Class Classification')
    plt.legend(loc="lower right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def compare_classifiers(results):
    """Compare all classifiers."""
    print("\n" + "=" * 60)
    print("CLASSIFIER COMPARISON")
    print("=" * 60)
    
    # Sort by accuracy
    sorted_results = sorted(results.items(), 
                           key=lambda x: x[1]['accuracy'], 
                           reverse=True)
    
    print("\nRanking by Accuracy:")
    for rank, (name, result) in enumerate(sorted_results, 1):
        print(f"{rank}. {name}: {result['accuracy']:.4f}")
    
    best_name, best_result = sorted_results[0]
    print(f"\n🏆 Best Classifier: {best_name} (Accuracy: {best_result['accuracy']:.4f})")

def main():
    """Main function to run ML classifier solution."""
    print("ML Classifier - Complete Solution")
    print("=" * 60)
    
    # Load data
    print("\n1. Loading data...")
    X, y, df = load_data()
    print(f"   Data shape: {X.shape}")
    print(f"   Classes: {len(np.unique(y))}")
    print(f"   Class distribution: {np.bincount(y)}")
    
    # Split data
    print("\n2. Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"   Training set: {X_train.shape}")
    print(f"   Test set: {X_test.shape}")
    
    # Train classifiers
    print("\n3. Training classifiers...")
    models = train_classifiers(X_train, y_train)
    
    # Evaluate
    print("\n4. Evaluating classifiers...")
    results = evaluate_classifiers(models, X_test, y_test)
    
    # Visualize
    print("\n5. Visualizing results...")
    visualize_results(results, X_test, y_test)
    
    # ROC curves
    print("\n6. Plotting ROC curves...")
    plot_roc_curves(models, X_test, y_test)
    
    # Compare
    compare_classifiers(results)
    
    print("\n" + "=" * 60)
    print("✅ Demo complete!")

if __name__ == "__main__":
    main()
