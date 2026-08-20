# Complete Project Guide: Simple AI Agent

---

## 🎯 Real-World Application

### Example: Delivery Route Optimizer
**Imagine you're building a food delivery app like Uber Eats or DoorDash.**

**Problem:** You need to find the fastest route for a delivery driver to pick up food from a restaurant and deliver it to a customer.

**Solution:** Your AI agent uses search algorithms to find the best path:
- **BFS (Breadth-First Search):** Finds the shortest path (fewest turns)
- **DFS (Depth-First Search):** Explores one route completely before trying another
- **A* Algorithm:** Finds the fastest route considering traffic and distance

**Real-World Impact:**
- ✅ Faster deliveries = happier customers
- ✅ Lower fuel costs = more profit
- ✅ Better driver experience

**Similar Systems:**
- Food Delivery Apps (Uber Eats, DoorDash)
- Navigation Systems (Google Maps, Waze)
- Logistics Companies (Amazon, FedEx)
- Ride-Sharing Apps (Uber, Lyft)

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to AI agents or search algorithms?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

### Project Structure
```
simple_ai_agent/
├── agent.py              # AI agent class
├── search_algorithms.py  # BFS, DFS, A* algorithms
├── problem.py            # Problem definition
├── main.py               # Main program
└── README.md
```

### Key Components to Implement

**problem.py:**
```python
class Problem:
    def __init__(self, start, goal, graph):
        self.start = start
        self.goal = goal
        self.graph = graph
    
    def get_neighbors(self, location):
        return self.graph.get(location, [])
    
    def is_goal(self, location):
        return location == self.goal
```

**search_algorithms.py:**
```python
def bfs(problem):
    # BFS implementation
    pass

def dfs(problem):
    # DFS implementation
    pass

def astar(problem):
    # A* implementation
    pass
```

**agent.py:**
```python
class SimpleAgent:
    def solve(self, algorithm='bfs'):
        # Solve using specified algorithm
        pass
```

### Testing Checklist
- [ ] BFS finds shortest path
- [ ] DFS explores all paths
- [ ] A* finds optimal path
- [ ] Agent works with different problems
- [ ] Solution path is valid

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with search algorithms?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand the Problem (Day 1)

**📖 Course Connection:** Review `unit1-ai-foundations/examples/01_ai_introduction.ipynb` to understand AI agents

**What is an AI Agent?**
An AI agent is a program that:
- Perceives its environment (knows where it is)
- Makes decisions (chooses where to go next)
- Acts (moves to the next location)
- Has a goal (reaches the destination)

**Example:**
```
You are at: Home (A)
Goal: Reach: Work (G)

Map:
A -- B -- C
|    |    |
D -- E -- F
     |    |
     H -- G
```

**Your Task:** Find path from A to G

---

### Step 2: Set Up Your Project (Day 1)

**Create these files:**

1. **`agent.py`** - Your AI agent class
2. **`search_algorithms.py`** - BFS, DFS, A* algorithms
3. **`problem.py`** - Defines your problem (map, start, goal)
4. **`main.py`** - Runs everything
5. **`README.md`** - Explains your project

**Install required libraries:**
```bash
pip install numpy
```

---

### Step 3: Create the Problem Structure (Day 2)

**📖 Course Connection:** Review `unit2-search-algorithms/examples/01_bfs_algorithm.ipynb` for graph representation

**File: `problem.py`**

```python
class Problem:
    """Represents a navigation problem"""
    
    def __init__(self, start, goal, graph):
        """
        start: Starting location (e.g., 'A')
        goal: Target location (e.g., 'G')
        graph: Dictionary representing connections
               Example: {'A': ['B', 'D'], 'B': ['A', 'C', 'E']}
        """
        self.start = start
        self.goal = goal
        self.graph = graph
    
    def get_neighbors(self, location):
        """Get all possible next locations"""
        return self.graph.get(location, [])
    
    def is_goal(self, location):
        """Check if we reached the goal"""
        return location == self.goal
```

**Example Usage:**
```python
# Create a simple map
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E'],
    'E': ['B', 'D', 'F', 'H'],
    'F': ['C', 'E', 'G'],
    'G': ['F', 'H'],
    'H': ['E', 'G']
}

problem = Problem(start='A', goal='G', graph=graph)
```

---

### Step 4: Implement BFS Algorithm (Day 3)

**📖 Course Connection:** Follow `unit2-search-algorithms/examples/01_bfs_algorithm.ipynb` for BFS implementation

**File: `search_algorithms.py`**

```python
from collections import deque

def bfs(problem):
    """
    Breadth-First Search
    Finds shortest path (fewest steps)
    """
    # Queue: locations to explore
    queue = deque([(problem.start, [problem.start])])
    visited = set()
    
    while queue:
        current, path = queue.popleft()
        
        # Check if we reached the goal
        if problem.is_goal(current):
            return path
        
        # Mark as visited
        visited.add(current)
        
        # Explore neighbors
        for neighbor in problem.get_neighbors(current):
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
    
    return None  # No path found

# Test it
path = bfs(problem)
print(f"Path found: {' -> '.join(path)}")
# Output: Path found: A -> B -> E -> F -> G
```

**Why BFS?**
- ✅ Always finds shortest path
- ✅ Guaranteed to find solution if it exists
- ✅ Simple to understand

---

### Step 5: Implement DFS Algorithm (Day 4)

**📖 Course Connection:** Follow `unit2-search-algorithms/examples/02_dfs_algorithm.ipynb` for DFS implementation

```python
def dfs(problem):
    """
    Depth-First Search
    Explores one path completely before trying another
    """
    stack = [(problem.start, [problem.start])]
    visited = set()
    
    while stack:
        current, path = stack.pop()
        
        if problem.is_goal(current):
            return path
        
        visited.add(current)
        
        for neighbor in problem.get_neighbors(current):
            if neighbor not in visited:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))
    
    return None
```

**BFS vs DFS:**
- **BFS:** Finds shortest path, uses more memory
- **DFS:** May find longer path, uses less memory

---

### Step 6: Implement A* Algorithm (Day 5)

**📖 Course Connection:** Follow `unit2-search-algorithms/examples/03_astar_algorithm.ipynb` for A* implementation

```python
import heapq

def heuristic(location, goal):
    """Estimate distance to goal (simplified)"""
    # In real apps, this would use actual distance
    return 1  # Simple heuristic

def astar(problem):
    """
    A* Algorithm
    Finds best path considering both distance and estimated cost
    """
    # Priority queue: (total_cost, current, path)
    queue = [(0, problem.start, [problem.start])]
    visited = set()
    
    while queue:
        cost, current, path = heapq.heappop(queue)
        
        if problem.is_goal(current):
            return path
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for neighbor in problem.get_neighbors(current):
            if neighbor not in visited:
                new_path = path + [neighbor]
                # Cost = steps taken + estimated remaining
                new_cost = len(new_path) + heuristic(neighbor, problem.goal)
                heapq.heappush(queue, (new_cost, neighbor, new_path))
    
    return None
```

---

### Step 7: Create the AI Agent (Day 6)

**File: `agent.py`**

```python
from search_algorithms import bfs, dfs, astar

class SimpleAgent:
    """Simple AI Agent that uses search algorithms"""
    
    def __init__(self, problem):
        self.problem = problem
        self.path = None
        self.algorithm = None
    
    def solve(self, algorithm='bfs'):
        """
        Solve the problem using specified algorithm
        algorithm: 'bfs', 'dfs', or 'astar'
        """
        self.algorithm = algorithm
        
        if algorithm == 'bfs':
            self.path = bfs(self.problem)
        elif algorithm == 'dfs':
            self.path = dfs(self.problem)
        elif algorithm == 'astar':
            self.path = astar(self.problem)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")
        
        return self.path
    
    def get_solution_info(self):
        """Get information about the solution"""
        if not self.path:
            return "No solution found"
        
        return {
            'algorithm': self.algorithm,
            'path': ' -> '.join(self.path),
            'steps': len(self.path) - 1,
            'path_length': len(self.path)
        }
```

---

### Step 8: Create Main Program (Day 7)

**File: `main.py`**

```python
from problem import Problem
from agent import SimpleAgent

def main():
    # Create a map (like a city with streets)
    city_map = {
        'Home': ['Street1', 'Street2'],
        'Street1': ['Home', 'Restaurant', 'Street3'],
        'Street2': ['Home', 'Street4'],
        'Restaurant': ['Street1', 'Street3'],
        'Street3': ['Restaurant', 'Street1', 'Customer'],
        'Street4': ['Street2', 'Customer'],
        'Customer': ['Street3', 'Street4']
    }
    
    # Create problem: Deliver from Restaurant to Customer
    delivery_problem = Problem(
        start='Restaurant',
        goal='Customer',
        graph=city_map
    )
    
    # Create agent
    agent = SimpleAgent(delivery_problem)
    
    # Try different algorithms
    print("=" * 50)
    print("Food Delivery Route Finder")
    print("=" * 50)
    
    for algo in ['bfs', 'dfs', 'astar']:
        print(f"\nUsing {algo.upper()} algorithm:")
        path = agent.solve(algorithm=algo)
        info = agent.get_solution_info()
        print(f"  Path: {info['path']}")
        print(f"  Steps: {info['steps']}")

if __name__ == "__main__":
    main()
```

---

## 🔗 Course Content Connections

### How This Project Connects to Course Content

| Project Step | Course Notebook | What You Learn |
|-------------|----------------|----------------|
| **Understand AI Agents** | `unit1-ai-foundations/examples/01_ai_introduction.ipynb` | What AI agents are |
| **Problem Representation** | `unit2-search-algorithms/examples/01_bfs_algorithm.ipynb` | Graph representation |
| **BFS Algorithm** | `unit2-search-algorithms/examples/01_bfs_algorithm.ipynb` | Breadth-first search |
| **DFS Algorithm** | `unit2-search-algorithms/examples/02_dfs_algorithm.ipynb` | Depth-first search |
| **A* Algorithm** | `unit2-search-algorithms/examples/03_astar_algorithm.ipynb` | A* with heuristics |
| **Knowledge Representation** | `unit3-knowledge-representation/examples/01_knowledge_graph.ipynb` | Knowledge structures |

### Learning Path
1. Complete Unit 1 to understand AI agents
2. Complete Unit 2 to learn search algorithms
3. Then build this project
4. Apply to your own navigation problem

---

## 🐛 Troubleshooting

### Problem: Algorithm returns None
**Error:** `No path found`  
**Solution:** Check if start and goal are connected in the graph

### Problem: Algorithm runs forever
**Error:** Infinite loop  
**Solution:** Make sure you mark locations as visited

### Problem: Path is too long
**Error:** Path has many unnecessary steps  
**Solution:** Try A* algorithm, it finds better paths

### Problem: Can't understand the code
**Error:** Code seems complex  
**Solution:** 
1. Review course notebooks first
2. Start with BFS (simplest)
3. Test with small examples
4. Add print statements to see what's happening

---

## 🎓 Learning Checklist

- [ ] Day 1: Understand what an AI agent is
- [ ] Day 2: Set up project files
- [ ] Day 3: Implement BFS algorithm
- [ ] Day 4: Implement DFS algorithm
- [ ] Day 5: Implement A* algorithm
- [ ] Day 6: Create agent class
- [ ] Day 7: Test with different problems
- [ ] Day 8: Add documentation
- [ ] Day 9: Test edge cases
- [ ] Day 10: Write report

---

## 💡 Tips for Success

1. **Start Simple:** Begin with a small map (3-4 locations)
2. **Test Each Step:** Don't move to next step until current one works
3. **Print Everything:** Use print() to see what's happening
4. **Draw the Map:** Visualize your problem on paper
5. **Compare Algorithms:** See which one finds better paths

---

## 📊 Evaluation Criteria

### Functionality (30%)
- Agent can solve problems
- At least one algorithm works
- Solution path is valid
- Works with different problems

### Code Quality (25%)
- Code is well-organized
- Functions are documented
- Error handling included
- Follows best practices

### Algorithm Implementation (20%)
- Algorithms implemented correctly
- All three algorithms work
- Comparison between algorithms
- Performance analysis

### Documentation (15%)
- README explains the agent
- Code is commented
- Examples provided
- Report explains approach

### Creativity (10%)
- Additional features
- Creative problem domain
- Improved algorithms
- Unique approaches

---

## 📖 Resources

### Course Content
- Unit 1: AI Foundations
- Unit 2: Search Algorithms
- Unit 3: Knowledge Representation

### External Resources
- Graph theory basics
- Search algorithm tutorials
- Python collections documentation

---

**Good luck building your AI agent!** 🚀