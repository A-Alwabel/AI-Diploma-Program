# Quiz 01: Introduction & Search Algorithms

## Instructions
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

### Question 2 (5 points)
What is an edge in a graph?
- A) A node
- B) A connection between two nodes
- C) A path
- D) A weight

### Question 3 (10 points)
Draw a simple graph with 4 nodes (A, B, C, D) where:
- A is connected to B and C
- B is connected to D
- C is connected to D

---

## Part 2: BFS (Breadth-First Search) (25 points)

### Question 4 (5 points)
What data structure does BFS use?
- A) Stack (LIFO)
- B) Queue (FIFO)
- C) Priority Queue
- D) List

### Question 5 (5 points)
BFS finds:
- A) The deepest path first
- B) The shortest path (in unweighted graphs)
- C) The longest path
- D) Any path

### Question 6 (10 points)
Trace BFS on the following graph starting from node A:
```
A -- B
|    |
C -- D
```
Show the order nodes are visited.

### Question 7 (5 points)
What is the time complexity of BFS?
- A) O(V)
- B) O(V + E)
- C) O(V²)
- D) O(E)

---

## Part 3: DFS (Depth-First Search) (20 points)

### Question 8 (5 points)
What data structure does DFS use?
- A) Stack (LIFO)
- B) Queue (FIFO)
- C) Priority Queue
- D) List

### Question 9 (5 points)
DFS explores:
- A) Level by level
- B) As deep as possible first
- C) Randomly
- D) Shortest paths first

### Question 10 (10 points)
Trace DFS on the following graph starting from node A:
```
A -- B
|    |
C -- D
```
Show the order nodes are visited (assume alphabetical order for neighbors).

---

## Part 4: A* Search (20 points)

### Question 11 (5 points)
What makes A* different from Dijkstra's algorithm?
- A) It uses a stack
- B) It uses a heuristic function
- C) It doesn't use a priority queue
- D) It's slower

### Question 12 (5 points)
The A* algorithm uses which formula for node evaluation?
- A) f(n) = g(n)
- B) f(n) = h(n)
- C) f(n) = g(n) + h(n)
- D) f(n) = g(n) - h(n)

### Question 13 (5 points)
What does g(n) represent in A*?
- A) Heuristic cost
- B) Actual cost from start to node n
- C) Estimated cost to goal
- D) Total cost

### Question 14 (5 points)
What does h(n) represent in A*?
- A) Actual cost from start
- B) Estimated cost from node n to goal
- C) Total cost
- D) Path length

---

## Part 5: Dijkstra's Algorithm (15 points)

### Question 15 (5 points)
Dijkstra's algorithm finds:
- A) Shortest path in unweighted graphs
- B) Shortest path in weighted graphs
- C) Longest path
- D) Any path

### Question 16 (5 points)
What data structure does Dijkstra's algorithm use?
- A) Stack
- B) Queue
- C) Priority Queue
- D) List

### Question 17 (5 points)
Dijkstra's algorithm works on:
- A) Only unweighted graphs
- B) Only weighted graphs with non-negative weights
- C) Any graph
- D) Only directed graphs

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
