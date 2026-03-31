#!/usr/bin/env python3
"""
Update Modules 04 and 05 with ML-focused content
"""

import json
from pathlib import Path

def update_module_04():
    """Update Module 04 notebook with Dimensionality Reduction content"""
    notebook_path = Path("modules/module_04/notebook_04_why_how_after.ipynb")
    
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)
    
    # Update cell 0 - Title and objectives
    notebook['cells'][0]['source'] = [
        "# Module 04: Dimensionality Reduction Techniques and Data Representation\n",
        "\n",
        "تقنيات تقليص الأبعاد وتمثيل البيانات\n",
        "\n",
        "> **Note**: Content should be populated from `course-content/04.pptx`\n",
        "\n",
        "---\n",
        "\n",
        "## Learning Objectives\n",
        "\n",
        "In this module, you will learn:\n",
        "- The curse of dimensionality and why it matters\n",
        "- Principal Component Analysis (PCA) and its implementation\n",
        "- Other dimensionality reduction techniques (t-SNE, UMAP)\n",
        "- Data representation methods for ML\n",
        "- Feature extraction and selection techniques\n",
        "- Visualizing high-dimensional data in reduced spaces\n",
        "\n",
        "---"
    ]
    
    # Update cell 1 - WHY section
    notebook['cells'][1]['source'] = [
        "# Part 1: WHY\n",
        "\n",
        "## Understanding the Motivation\n",
        "\n",
        "### Why does Dimensionality Reduction matter for Machine Learning?\n",
        "\n",
        "High-dimensional data poses significant challenges in ML:\n",
        "\n",
        "- **Curse of Dimensionality**: More dimensions require exponentially more data\n",
        "- **Computational Efficiency**: Reducing dimensions speeds up training and inference\n",
        "- **Visualization**: Humans can only visualize 2D/3D, so we need to reduce dimensions\n",
        "- **Noise Reduction**: Removing irrelevant dimensions improves model performance\n",
        "- **Feature Selection**: Identifying the most important features\n",
        "\n",
        "### Real-World Applications\n",
        "\n",
        "- **Image Processing**: Reducing pixel dimensions while preserving information\n",
        "- **Natural Language Processing**: Reducing word embedding dimensions\n",
        "- **Genomics**: Analyzing high-dimensional genetic data\n",
        "- **Recommendation Systems**: Reducing user-item matrix dimensions\n",
        "- **Data Visualization**: Making high-dimensional data interpretable\n",
        "\n",
        "**TODO**: Add more specific examples from your PowerPoint slides"
    ]
    
    # Update cell 2 - WHY code example
    notebook['cells'][2]['source'] = [
        "# Example: Why Dimensionality Reduction matters in ML\n",
        "import numpy as np\n",
        "\n",
        "# Example: The curse of dimensionality\n",
        "# As dimensions increase, data becomes sparse\n",
        "dimensions = [10, 100, 1000, 10000]\n",
        "data_points = 1000\n",
        "\n",
        "print(\"Curse of Dimensionality Example:\")\n",
        "for dim in dimensions:\n",
        "    # In high dimensions, most points are near the boundary\n",
        "    volume_ratio = (0.9 ** dim)  # Volume of inner 90% hypercube\n",
        "    print(f\"{dim}D: Only {volume_ratio*100:.2f}% of volume is in inner 90%\")\n",
        "\n",
        "print(\"\\nThis is why we need dimensionality reduction!\")\n",
        "print(\"PCA and other techniques help us find the most important dimensions.\")"
    ]
    
    # Save updated notebook
    with open(notebook_path, 'w') as f:
        json.dump(notebook, f, indent=1)
    
    print("✓ Updated Module 04 notebook structure")

def update_module_05():
    """Update Module 05 notebook with Probabilities and Inference content"""
    notebook_path = Path("modules/module_05/notebook_05_why_how_after.ipynb")
    
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)
    
    # Update cell 0 - Title and objectives
    notebook['cells'][0]['source'] = [
        "# Module 05: Probabilities, Samples, and Statistical Inference\n",
        "\n",
        "الاحتمالات، والعينات، والاستدلال الإحصائي\n",
        "\n",
        "> **Note**: Content should be populated from `course-content/05.pptx`\n",
        "\n",
        "---\n",
        "\n",
        "## Learning Objectives\n",
        "\n",
        "In this module, you will learn:\n",
        "- Probability theory and distributions for ML\n",
        "- Random variables and sampling techniques\n",
        "- Statistical inference methods\n",
        "- Hypothesis testing for model evaluation\n",
        "- Bayesian inference concepts\n",
        "- Applying probabilistic models to ML problems\n",
        "\n",
        "---"
    ]
    
    # Update cell 1 - WHY section
    notebook['cells'][1]['source'] = [
        "# Part 1: WHY\n",
        "\n",
        "## Understanding the Motivation\n",
        "\n",
        "### Why do Probabilities and Statistical Inference matter for Machine Learning?\n",
        "\n",
        "Probability and statistics are fundamental to understanding ML:\n",
        "\n",
        "- **Uncertainty**: ML models make predictions with uncertainty that we need to quantify\n",
        "- **Data Sampling**: Understanding sampling helps with train/test splits and cross-validation\n",
        "- **Model Evaluation**: Statistical tests help determine if model improvements are significant\n",
        "- **Bayesian Methods**: Many ML algorithms use probabilistic frameworks\n",
        "- **Decision Making**: Probabilities help make informed decisions from model outputs\n",
        "\n",
        "### Real-World Applications\n",
        "\n",
        "- **Confidence Intervals**: Understanding prediction uncertainty\n",
        "- **A/B Testing**: Statistical tests for comparing models\n",
        "- **Bayesian Networks**: Probabilistic graphical models\n",
        "- **Naive Bayes**: Classification using probability theory\n",
        "- **Monte Carlo Methods**: Sampling-based inference\n",
        "\n",
        "**TODO**: Add more specific examples from your PowerPoint slides"
    ]
    
    # Update cell 2 - WHY code example
    notebook['cells'][2]['source'] = [
        "# Example: Why Probabilities and Inference matter in ML\n",
        "import numpy as np\n",
        "from scipy import stats\n",
        "\n",
        "# Example: Understanding prediction uncertainty\n",
        "# ML models should provide not just predictions, but confidence\n",
        "\n",
        "predictions = np.array([0.85, 0.92, 0.78, 0.95, 0.88])\n",
        "mean_pred = np.mean(predictions)\n",
        "std_pred = np.std(predictions)\n",
        "\n",
        "print(\"Model Predictions with Uncertainty:\")\n",
        "print(f\"Mean prediction: {mean_pred:.2f}\")\n",
        "print(f\"Standard deviation: {std_pred:.2f}\")\n",
        "print(f\"95% confidence interval: [{mean_pred - 1.96*std_pred:.2f}, {mean_pred + 1.96*std_pred:.2f}]\")\n",
        "\n",
        "print(\"\\nStatistical inference helps us:\")\n",
        "print(\"- Understand prediction reliability\")\n",
        "print(\"- Compare different models\")\n",
        "print(\"- Make informed decisions\")"
    ]
    
    # Save updated notebook
    with open(notebook_path, 'w') as f:
        json.dump(notebook, f, indent=1)
    
    print("✓ Updated Module 05 notebook structure")

if __name__ == "__main__":
    update_module_04()
    update_module_05()
    print("\n✓ All modules updated!")

