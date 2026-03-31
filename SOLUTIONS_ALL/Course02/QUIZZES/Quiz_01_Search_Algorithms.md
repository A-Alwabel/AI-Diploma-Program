# Quiz 01: Introduction & Search Algorithms | اختبار 01: مقدمة الدورة و خوارزميات البحث

## Instructions | التعليمات
- **Time Limit**: 45 minutes
- **Total Points**: 100 points
- **Format**: Multiple choice, short answer, code completion, algorithm tracing
- **Allowed Resources**: None (closed book)

---

## Part 1: Graph Basics (20 points)

### Question 1 (5 points)
What is a node in a graph?
- A) A connection between two points
- B) A point or vertex in the graph
- C) A path through the graph
- D) A weight on an edge

**Answer: B**

### Question 2 (5 points)
What is an edge in a graph?
- A) A node
- B) A connection between two nodes
- C) A path
- D) A weight

**Answer: B**

### Question 3 (10 points)
Draw a simple graph with 4 nodes (A, B, C, D) where:
- A is connected to B and C
- B is connected to D
- C is connected to D

**Answer: Students should draw a graph showing these connections**

---

## Part 2: BFS (Breadth-First Search) (25 points)

### Question 4 (5 points)
What data structure does BFS use?
- A) Stack (LIFO)
- B) Queue (FIFO)
- C) Priority Queue
- D) List

**Answer: B**

### Question 5 (5 points)
BFS finds:
- A) The deepest path first
- B) The shortest path (in unweighted graphs)
- C) The longest path
- D) Any path

**Answer: B**

### Question 6 (10 points)
Trace BFS on the following graph starting from node A:
```
A -- B
|    |
C -- D
```
Show the order nodes are visited.

**Answer: A, B, C, D (or A, C, B, D depending on order of neighbors)**

### Question 7 (5 points)
What is the time complexity of BFS?
- A) O(V)
- B) O(V + E)
- C) O(V²)
- D) O(E)

**Answer: B**

---

## Part 3: DFS (Depth-First Search) (20 points)

### Question 8 (5 points)
What data structure does DFS use?
- A) Stack (LIFO)
- B) Queue (FIFO)
- C) Priority Queue
- D) List

**Answer: A**

### Question 9 (5 points)
DFS explores:
- A) Level by level
- B) As deep as possible first
- C) Randomly
- D) Shortest paths first

**Answer: B**

### Question 10 (10 points)
Trace DFS on the following graph starting from node A:
```
A -- B
|    |
C -- D
```
Show the order nodes are visited (assume alphabetical order for neighbors).

**Answer: A, B, D, C (or A, C, D, B depending on implementation)**

---

## Part 4: A* Search (20 points)

### Question 11 (5 points)
What makes A* different from Dijkstra's algorithm?
- A) It uses a stack
- B) It uses a heuristic function
- C) It doesn't use a priority queue
- D) It's slower

**Answer: B**

### Question 12 (5 points)
The A* algorithm uses which formula for node evaluation?
- A) f(n) = g(n)
- B) f(n) = h(n)
- C) f(n) = g(n) + h(n)
- D) f(n) = g(n) - h(n)

**Answer: C**

### Question 13 (5 points)
What does g(n) represent in A*?
- A) Heuristic cost
- B) Actual cost from start to node n
- C) Estimated cost to goal
- D) Total cost

**Answer: B**

### Question 14 (5 points)
What does h(n) represent in A*?
- A) Actual cost from start
- B) Estimated cost from node n to goal
- C) Total cost
- D) Path length

**Answer: B**

---

## Part 5: Dijkstra's Algorithm (15 points)

### Question 15 (5 points)
Dijkstra's algorithm finds:
- A) Shortest path in unweighted graphs
- B) Shortest path in weighted graphs
- C) Longest path
- D) Any path

**Answer: B**

### Question 16 (5 points)
What data structure does Dijkstra's algorithm use?
- A) Stack
- B) Queue
- C) Priority Queue
- D) List

**Answer: C**

### Question 17 (5 points)
Dijkstra's algorithm works on:
- A) Only unweighted graphs
- B) Only weighted graphs with non-negative weights
- C) Any graph
- D) Only directed graphs

**Answer: B**

---

## Answer Key Summary

1. B - A point or vertex in the graph
2. B - A connection between two nodes
3. See answer description
4. B - Queue (FIFO)
5. B - The shortest path (in unweighted graphs)
6. A, B, C, D (or A, C, B, D)
7. B - O(V + E)
8. A - Stack (LIFO)
9. B - As deep as possible first
10. A, B, D, C (or A, C, D, B)
11. B - It uses a heuristic function
12. C - f(n) = g(n) + h(n)
13. B - Actual cost from start to node n
14. B - Estimated cost from node n to goal
15. B - Shortest path in weighted graphs
16. C - Priority Queue
17. B - Only weighted graphs with non-negative weights

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

