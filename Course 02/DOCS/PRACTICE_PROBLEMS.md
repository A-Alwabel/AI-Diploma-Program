# Additional Practice Problems

Extra practice problems beyond the notebooks to reinforce learning.

---

## Practice Problems by Topic

### Topic 1: Python Libraries (NumPy, Matplotlib)

#### Problem 1.1: Array Operations (Beginner)
**Task:** Create a 5x5 NumPy array filled with random integers (1-100). Calculate:
- Mean, median, standard deviation
- Sum of each row
- Maximum value and its position

**Hint:** Use `np.random.randint()`, `np.mean()`, `np.std()`

---

#### Problem 1.2: Data Visualization (Beginner)
**Task:** Create a line plot showing:
- X-axis: Numbers 0 to 10
- Y-axis: X² (quadratic function)
- Add title: "Quadratic Function"
- Add labels for both axes
- Change line color to red

**Hint:** Use `plt.plot()`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()`

---

#### Problem 1.3: Multiple Plots (Intermediate)
**Task:** Create a figure with 2 subplots side-by-side:
- Left: Line plot of sin(x) from 0 to 2π
- Right: Line plot of cos(x) from 0 to 2π
- Add titles to each subplot

**Hint:** Use `plt.subplot()` or `plt.subplots()`

---

### Topic 2: Search Algorithms

#### Problem 2.1: BFS Implementation (Beginner)
**Task:** Implement BFS to find if a path exists between two nodes in a graph.

**Graph:**
```
A -- B -- C
|    |
D -- E
```

**Test Cases:**
- Path from A to C? (Should find: A → B → C)
- Path from A to E? (Should find: A → B → E or A → D → E)
- Path from C to D? (Should find: C → B → A → D)

**Hint:** Use `collections.deque` for queue

---

#### Problem 2.2: DFS Implementation (Beginner)
**Task:** Implement DFS to find a path between two nodes.

**Use the same graph as Problem 2.1**

**Compare:** Does DFS always find the shortest path? Why or why not?

---

#### Problem 2.3: A* with Custom Heuristic (Intermediate)
**Task:** Implement A* algorithm with:
- Manhattan distance heuristic
- Euclidean distance heuristic

**Compare:** Which heuristic finds the path faster? Why?

**Test on a 10x10 grid with obstacles.**

---

### Topic 3: Knowledge Representation

#### Problem 3.1: Knowledge Graph Creation (Beginner)
**Task:** Create a knowledge graph representing:
- 5 people (nodes)
- Relationships: "knows", "works_with", "lives_in"
- At least 10 relationships total

**Visualize the graph using NetworkX.**

---

#### Problem 3.2: Rule-Based System (Intermediate)
**Task:** Create a simple rule-based system for weather advice:

**Rules:**
- IF temperature > 30 AND sunny THEN "Wear sunscreen"
- IF temperature < 10 THEN "Wear jacket"
- IF raining THEN "Bring umbrella"
- IF temperature > 25 AND not_raining THEN "Good weather for outdoor activities"

**Implement forward chaining to give advice based on current conditions.**

---

#### Problem 3.3: Semantic Network (Advanced)
**Task:** Create a semantic network for animals with inheritance:
- Animal (parent class)
  - Mammal (child of Animal)
    - Dog (child of Mammal)
    - Cat (child of Mammal)
  - Bird (child of Animal)
    - Eagle (child of Bird)

**Properties:**
- All animals: "breathes", "eats"
- Mammals: "has_fur", "warm_blooded"
- Birds: "has_feathers", "can_fly"

**Implement inheritance so child classes inherit parent properties.**

---

### Topic 4: Uncertainty & Probability

#### Problem 4.1: Basic Probability (Beginner)
**Task:** Simulate coin flips:
- Flip a coin 1000 times
- Calculate probability of heads
- Calculate probability of getting 3 heads in a row
- Visualize results with histogram

**Hint:** Use `np.random.choice()` or `np.random.randint()`

---

#### Problem 4.2: Bayesian Inference (Intermediate)
**Task:** Implement a simple medical diagnosis system:

**Given:**
- P(Disease) = 0.01 (1% of population has disease)
- P(Positive Test | Disease) = 0.95 (95% accurate if diseased)
- P(Positive Test | No Disease) = 0.05 (5% false positive)

**Calculate:** P(Disease | Positive Test)

**Interpret:** What does this tell you about medical testing?

---

#### Problem 4.3: Monte Carlo Simulation (Intermediate)
**Task:** Estimate π using Monte Carlo method:
- Generate random points in a 1x1 square
- Count points inside quarter circle (radius = 1)
- Estimate π = 4 × (points inside / total points)
- Visualize with scatter plot

**Compare:** How many points needed for accuracy to 2 decimal places?

---

### Topic 5: Optimization

#### Problem 5.1: Gradient Descent (Intermediate)
**Task:** Implement gradient descent to minimize:
f(x) = x² + 2x + 1

**Requirements:**
- Start from x = 5
- Learning rate = 0.1
- Stop when change < 0.001
- Plot the convergence (x value vs iteration)

**What is the minimum value? (Should be at x = -1)**

---

#### Problem 5.2: Genetic Algorithm (Advanced)
**Task:** Use genetic algorithm to find maximum of:
f(x) = -x² + 10x (for x = 0 to 10)

**Requirements:**
- Population size: 20
- Generations: 50
- Mutation rate: 0.1
- Crossover rate: 0.8

**Plot:** Best fitness vs generation

---

#### Problem 5.3: SciPy Optimization (Beginner)
**Task:** Use SciPy to optimize:
- Minimize: f(x) = x² - 4x + 4
- Find minimum using `scipy.optimize.minimize()`

**Compare:** Result with analytical solution (x = 2)

---

### Topic 6: Machine Learning

#### Problem 6.1: Data Preprocessing (Beginner)
**Task:** Load a dataset (Iris or your own) and:
- Check for missing values
- Handle missing values (fill or remove)
- Encode categorical variables
- Normalize/scale features
- Split into train/test (80/20)

**Use Pandas and Scikit-learn.**

---

#### Problem 6.2: Model Comparison (Intermediate)
**Task:** Train and compare 3 models on same dataset:
- Logistic Regression
- Decision Tree
- KNN

**For each model:**
- Train on training set
- Predict on test set
- Calculate accuracy, precision, recall
- Create confusion matrix
- Visualize results

**Which model performs best? Why?**

---

#### Problem 6.3: Feature Importance (Intermediate)
**Task:** For a classification problem:
- Train a Decision Tree
- Extract feature importances
- Visualize feature importances (bar chart)
- Identify top 3 most important features

**Interpret:** What do these features tell you about the problem?

---

## Difficulty Levels

### Beginner (⭐)
- Basic implementation
- Follows notebook examples closely
- Minimal customization needed

### Intermediate (⭐⭐)
- Requires understanding concepts
- Some customization needed
- May need to combine concepts

### Advanced (⭐⭐⭐)
- Requires deep understanding
- Significant customization
- May require research

---

## How to Use

1. **Start with Beginner problems** - Build confidence
2. **Progress to Intermediate** - Apply knowledge
3. **Challenge yourself with Advanced** - Master concepts

**Tips:**
- Try problems yourself first
- Check solutions only after attempting
- Experiment with variations
- Ask for help if stuck

---

## Solutions

Solutions are released by your instructor.

**Remember:** Try problems yourself first! Solutions are for checking your work, not copying.

---

**Created**: 2025  
**For**: Python for AI Course - 112 AIAT
