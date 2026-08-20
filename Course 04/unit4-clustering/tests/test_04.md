# Test 4: Clustering and Dimensionality Reduction

**Time Limit:** 90 minutes | **Marks:** 50 points

---

## Instructions
- Answer all questions
- Show your work for code questions
- Use proper comments in your code
- You may use pandas, numpy, sklearn, and matplotlib

---

## Part 1: Multiple Choice (15 points)

### Question 1 (3 points)
What is the main difference between supervised and unsupervised learning?
- A) Supervised learning uses labels, unsupervised learning doesn't
- B) Unsupervised learning uses labels, supervised learning doesn't
- C) There is no difference
- D) Supervised learning is faster

---

### Question 2 (3 points)
What does K-Means clustering try to minimize?
- A) The number of clusters
- B) The within-cluster sum of squares (WCSS)
- C) The number of features
- D) The distance between clusters

---

### Question 3 (3 points)
How do you choose the optimal number of clusters (K) in K-Means?
- A) Always use K=3
- B) Use the Elbow Method or Silhouette Score
- C) Use the number of features
- D) Use the number of samples

---

### Question 4 (3 points)
What is the main purpose of PCA (Principal Component Analysis)?
- A) To increase the number of features
- B) To reduce dimensionality while preserving variance
- C) To remove outliers
- D) To handle missing values

---

### Question 5 (3 points)
What does "explained variance" represent in PCA?
- A) The number of components
- B) The proportion of variance captured by each component
- C) The number of features
- D) The number of samples

---

## Part 2: Code Implementation (25 points)

### Question 6 (10 points)
Complete the following code to implement K-Means clustering with the Elbow Method:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Generate sample data
np.random.seed(42)
cluster1 = np.random.normal([2, 2], 0.6, (50, 2))
cluster2 = np.random.normal([6, 6], 0.6, (50, 2))
cluster3 = np.random.normal([2, 6], 0.6, (50, 2))
X = np.vstack([cluster1, cluster2, cluster3])

# TODO: Scale the data using StandardScaler
# TODO: Apply K-Means with K=3
# TODO: Implement Elbow Method for K from 1 to 10
# TODO: Plot the Elbow curve (WCSS vs K)
# TODO: Calculate and print Silhouette Score for K=3
# TODO: Add labels and title to the plot
```

**Expected Output:**
- Data scaled
- K-Means applied with K=3
- Elbow curve plotted
- Silhouette score printed

---

### Question 7 (10 points)
Write code to apply PCA and visualize the results:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

# Generate sample data
np.random.seed(42)
X, y = make_classification(
    n_samples=200,
    n_features=5,
    n_informative=3,
    random_state=42
)

# TODO: Scale the data
# TODO: Apply PCA with 2 components
# TODO: Transform the data to 2D
# TODO: Plot explained variance ratio
# TODO: Plot the 2D projection colored by original labels
# TODO: Add labels, title, and legend
```

**Expected Output:**
- PCA applied with 2 components
- Explained variance plot
- 2D projection plot with colors

---

### Question 8 (5 points)
Explain the difference between K-Means and Hierarchical clustering. When would you use each?

- **K-Means:**
  - Requires specifying K beforehand
  - Faster for large datasets
  - Creates non-overlapping clusters
  - Use when you know the number of clusters and have large datasets

- **Hierarchical:**
  - Doesn't require specifying K
  - Creates a dendrogram showing all possible clusters
  - Can be slower for large datasets
  - Use when you want to explore different numbers of clusters or have smaller datasets

---

## Part 3: Analysis Questions (10 points)

### Question 9 (5 points)
You apply PCA to a dataset with 10 features and find that the first 3 principal components explain 85% of the variance. Should you use all 10 features or just the 3 principal components? Explain your reasoning.

- **Recommendation:** Use 3 principal components
- **Reasoning:**
  1. 85% variance is typically sufficient (common threshold is 80-95%)
  2. Reduces dimensionality from 10 to 3 (70% reduction)
  3. Reduces overfitting risk
  4. Faster computation
  5. Easier visualization
- **Exception:** If interpretability of original features is critical, keep original features

---

### Question 10 (5 points)
What is the Silhouette Score, and what does it measure? What is a good Silhouette Score?

- **Definition:** Measures how similar an object is to its own cluster compared to other clusters
- **Range:** -1 to 1
- **Interpretation:**
  - Close to 1: Object is well-matched to its cluster and poorly matched to neighboring clusters
  - Close to 0: Object is on or very close to the decision boundary between clusters
  - Close to -1: Object is assigned to the wrong cluster
- **Good Score:** Generally, scores above 0.5 are considered good, above 0.7 are excellent

---

## Grading Rubric

| Question | Points | Criteria |
|----------|--------|----------|
| 1-5 | 15 | Multiple choice - 3 points each |
| 6 | 10 | Code implementation - correctness (6), visualization (4) |
| 7 | 10 | Code implementation - correctness (6), visualization (4) |
| 8 | 5 | Explanation quality - K-Means (2), Hierarchical (3) |
| 9 | 5 | Recommendation (2), reasoning (3) |
| 10 | 5 | Definition (2), interpretation (3) |

---

**Total: 50 points**

**Good luck!** 🍀  
