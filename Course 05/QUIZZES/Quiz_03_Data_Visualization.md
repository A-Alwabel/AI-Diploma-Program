# Quiz 3: Data Visualization
## اختبار 3: تصوير البيانات

**Time Limit:** 30 minutes | **Marks:** 30 points

---

## Part 1: Multiple Choice (10 points)

### Question 1 (2 points)
Which library is best for creating static statistical plots?
- A) Plotly
- B) Matplotlib
- C) Seaborn
- D) Pandas

---

### Question 2 (2 points)
What is the main advantage of Plotly over Matplotlib?
- A) Faster rendering
- B) Interactive visualizations
- C) Better default styling
- D) Smaller file size

---

### Question 3 (2 points)
What does `sns.histplot()` create?
- A) A bar chart
- B) A histogram showing distribution
- C) A scatter plot
- D) A line plot

---

### Question 4 (2 points)
Which plot is best for showing relationships between two continuous variables?
- A) Bar chart
- B) Scatter plot
- C) Pie chart
- D) Histogram

---

### Question 5 (2 points)
What does `plt.subplots()` return?
- A) A single figure
- B) A figure and axes objects
- C) A list of plots
- D) Nothing

---

## Part 2: Code Writing (10 points)

### Question 6 (5 points)
Write code to create a simple line plot using Matplotlib:
1. Import matplotlib
2. Create sample data (x: 1-10, y: squares)
3. Plot the line
4. Add title and labels

```python
import matplotlib.pyplot as plt

# Create data
x = range(1, 11)
y = [i**2 for i in x]

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o')
plt.title('Squares of Numbers')
plt.xlabel('Number')
plt.ylabel('Square')
plt.grid(True)
plt.show()
```

---

### Question 7 (5 points)
Write code to create a scatter plot with Seaborn:
1. Import seaborn and pandas
2. Load or create sample data
3. Create scatter plot with hue (color by category)

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5, 6, 7, 8],
    'y': [2, 4, 6, 8, 10, 12, 14, 16],
    'category': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B']
})

# Create scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='x', y='y', hue='category')
plt.title('Scatter Plot with Categories')
plt.show()
```

---

## Part 3: Short Answer (10 points)

### Question 8 (5 points)
Explain when to use different types of visualizations. Give examples.

**Visualization Types:**
1. **Bar Chart**: Compare categories (e.g., sales by region)
2. **Line Plot**: Show trends over time (e.g., stock prices over months)
3. **Scatter Plot**: Show relationship between two variables (e.g., height vs weight)
4. **Histogram**: Show distribution of a single variable (e.g., age distribution)
5. **Box Plot**: Show distribution and outliers (e.g., income by education level)
6. **Heatmap**: Show correlation matrix or 2D data (e.g., correlation between features)
7. **Pie Chart**: Show proportions (e.g., market share)

---

### Question 9 (5 points)
What are the key principles of effective data visualization?

---

## Grading Rubric

- **90-100% (27-30 points):** Excellent understanding
- **80-89% (24-26 points):** Good understanding
- **70-79% (21-23 points):** Satisfactory
- **60-69% (18-20 points):** Needs improvement
- **Below 60% (<18 points):** Requires additional study

