# Unit 4: Clustering and Dimensionality Reduction

Official AIAT 114 Unit 4. Unit hours: 20 (of 96 total training hours).

Unsupervised learning: K-Means and hierarchical clustering, and PCA for dimensionality reduction.

## Prerequisites

- Units 1-3 of this course
- PCA theory from AIAT 113 (Course 03, `unit4-dimensionality-reduction`) helps but is re-introduced here
- Environment set up per `../START_HERE.md` (repo root `.venv`, **ai-diploma** kernel)

## Learning Objectives

By the end of this unit you can:

- Cluster data with K-Means and choose K (elbow method, silhouette score)
- Apply agglomerative hierarchical clustering and read dendrograms
- Reduce dimensionality with PCA and interpret explained variance
- Visualize clusters and principal components

## Examples (work in this order)

| # | Notebook | What it covers |
|---|----------|----------------|
| 1 | `examples/01_kmeans_clustering.ipynb` | K-Means; centroids; elbow method; silhouette score; comparing K values |
| 2 | `examples/02_hierarchical_clustering.ipynb` | Agglomerative clustering; linkage methods; dendrograms |
| 3 | `examples/03_pca.ipynb` | PCA; explained variance; 2D projections; choosing component count |

The `examples/` folder also contains the PNG figures the notebooks produce.

## Exercises

Each exercise exists as a notebook (`.ipynb`) and an equivalent script (`.py`) - use the notebook form on the **ai-diploma** kernel.

1. `exercises/exercise_01.ipynb`
2. `exercises/exercise_02_pca.ipynb`

Solutions are released by your instructor.

## Assessment

- Quiz: `../QUIZZES/Quiz_04_Clustering.md`
- Unit test: `tests/test_04.md`

Next unit: `../unit5-model-selection/`
