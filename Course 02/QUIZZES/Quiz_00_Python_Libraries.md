# Quiz 00: Python Libraries for AI

## Instructions
- **Time Limit**: 30 minutes
- **Total Points**: 100 points
- **Format**: Multiple choice, short answer, code completion
- **Allowed Resources**: None (closed book)

---

## Part 1: NumPy (25 points)

### Question 1 (5 points)
What is the main advantage of NumPy arrays over Python lists?
- A) They use less memory
- B) They are faster for numerical operations
- C) They support more data types
- D) All of the above

### Question 2 (5 points)
What does `np.array([1, 2, 3])` create?
- A) A Python list
- B) A NumPy 1D array
- C) A NumPy 2D array
- D) A tuple

### Question 3 (10 points)
Complete the code to create a 3x3 matrix of zeros:

```python
import numpy as np
matrix = np.______(3, 3)
```

### Question 4 (5 points)
What does `arr.shape` return?
- A) The data type of the array
- B) The dimensions of the array
- C) The number of elements
- D) The memory size

---

## Part 2: Matplotlib (20 points)

### Question 5 (5 points)
What function is used to create a line plot in Matplotlib?
- A) `plt.bar()`
- B) `plt.plot()`
- C) `plt.scatter()`
- D) `plt.hist()`

### Question 6 (10 points)
Complete the code to create a plot with title and labels:

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.______("My Plot")
plt.______("X Label")
plt.______("Y Label")
plt.show()
```

### Question 7 (5 points)
What does `plt.show()` do?
- A) Saves the plot to a file
- B) Displays the plot on screen
- C) Clears the plot
- D) Updates the plot

---

## Part 3: Collections & heapq (15 points)

### Question 8 (5 points)
What is the main advantage of `collections.deque` over a regular list for queue operations?
- A) It's faster for append/pop operations
- B) It uses less memory
- C) It supports more data types
- D) It's easier to use

### Question 9 (5 points)
What does `heapq.heappush()` do?
- A) Removes the smallest element
- B) Adds an element maintaining heap property
- C) Sorts the entire list
- D) Finds the maximum element

### Question 10 (5 points)
Complete the code to create a priority queue:

```python
import heapq
queue = []
heapq.______(queue, (priority, item))
```

---

## Part 4: NetworkX (15 points)

### Question 11 (5 points)
What is a graph in NetworkX?
- A) A visualization
- B) A data structure with nodes and edges
- C) A mathematical function
- D) A file format

### Question 12 (5 points)
How do you add an edge between two nodes in NetworkX?
- A) `G.add_node(edge)`
- B) `G.add_edge(node1, node2)`
- C) `G.connect(node1, node2)`
- D) `G.link(node1, node2)`

### Question 13 (5 points)
What does `G.nodes()` return?
- A) The number of nodes
- B) A list of all nodes
- C) The edges
- D) The graph structure

---

## Part 5: SciPy & Scikit-learn (15 points)

### Question 14 (5 points)
What is SciPy primarily used for?
- A) Machine learning
- B) Scientific computing and statistics
- C) Data visualization
- D) Web development

### Question 15 (5 points)
What is the main purpose of Scikit-learn?
- A) Data visualization
- B) Machine learning algorithms
- C) Web scraping
- D) Database operations

### Question 16 (5 points)
Which Scikit-learn function is used to split data into training and testing sets?
- A) `train_test_split()`
- B) `split_data()`
- C) `divide_data()`
- D) `separate_data()`

---

## Part 6: Practical Application (10 points)

### Question 17 (10 points)
Write code to:
1. Create a NumPy array with values [1, 2, 3, 4, 5]
2. Calculate the mean of the array
3. Plot the array values

---

---

## Grading Rubric

- **90-100 points**: Excellent understanding
- **80-89 points**: Good understanding
- **70-79 points**: Satisfactory understanding
- **60-69 points**: Needs improvement
- **Below 60**: Review required

---

**Created**: 2025  
**For**: Python for AI Course - 112 AIAT
