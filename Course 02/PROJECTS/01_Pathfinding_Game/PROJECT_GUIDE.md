# Complete Project Guide: 01 Pathfinding Game

---

## 🎯 Real-World Application

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand the Game (Day 1)

**What is a Pathfinding Game?**
A game where you find the best path from start to goal:
- Grid-based map
- Obstacles (walls, enemies)
- Start and goal positions
- Different algorithms find different paths

**Example Grid:**
```
S = Start
G = Goal
# = Wall
. = Empty space

S . . # . .
. # . . . .
. . . # . G
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
pathfinding_game/
├── game.py          # Main game class
├── algorithms.py    # BFS, DFS, A*
├── visualizer.py    # Draw the game
├── main.py          # Run game
└── README.md
```

**Install:**
```bash
pip install pygame numpy
```

---

### Step 3: Create Game Grid (Day 2)

**File: `game.py`**

```python
class PathfindingGame:
    """Pathfinding game with grid"""
    
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.start = (0, 0)
        self.goal = (width-1, height-1)
        self.walls = []
    
    def add_wall(self, x, y):
        """Add obstacle at position"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 1  # 1 = wall
            self.walls.append((x, y))
    
    def is_valid(self, x, y):
        """Check if position is valid (not wall)"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x] == 0
        return False
    
    def get_neighbors(self, x, y):
        """Get valid neighboring cells"""
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                neighbors.append((nx, ny))
        
        return neighbors
```

---

### Step 4: Implement BFS (Day 3)

**File: `algorithms.py`**

```python
from collections import deque

def bfs(game):
    """Breadth-First Search - finds shortest path"""
    queue = deque([(game.start, [game.start])])
    visited = set()
    
    while queue:
        (x, y), path = queue.popleft()
        
        # Check if reached goal
        if (x, y) == game.goal:
            return path
        
        # Mark as visited
        visited.add((x, y))
        
        # Explore neighbors
        for neighbor in game.get_neighbors(x, y):
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
    
    return None  # No path found
```

---

### Step 5: Implement A* (Day 4)

```python
import heapq

def heuristic(pos, goal):
    """Estimate distance to goal (Manhattan distance)"""
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def astar(game):
    """A* algorithm - finds optimal path"""
    queue = [(0, game.start, [game.start])]
    visited = set()
    
    while queue:
        cost, (x, y), path = heapq.heappop(queue)
        
        if (x, y) == game.goal:
            return path
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for neighbor in game.get_neighbors(x, y):
            if neighbor not in visited:
                new_path = path + [neighbor]
                # Cost = path length + estimated distance
                new_cost = len(new_path) + heuristic(neighbor, game.goal)
                heapq.heappush(queue, (new_cost, neighbor, new_path))
    
    return None
```

---

### Step 6: Create Visualizer (Day 5)

**File: `visualizer.py`**

```python
import pygame

class GameVisualizer:
    """Visualize the pathfinding game"""
    
    def __init__(self, game, cell_size=50):
        self.game = game
        self.cell_size = cell_size
        self.width = game.width * cell_size
        self.height = game.height * cell_size
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def draw(self, path=None):
        """Draw the game grid"""
        self.screen.fill((255, 255, 255))
        
        # Draw grid
        for y in range(self.game.height):
            for x in range(self.game.width):
                rect = pygame.Rect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                
                # Color based on cell type
                if (x, y) == self.game.start:
                    color = (0, 255, 0)  # Green = start
                elif (x, y) == self.game.goal:
                    color = (255, 0, 0)  # Red = goal
                elif (x, y) in self.game.walls:
                    color = (0, 0, 0)  # Black = wall
                elif path and (x, y) in path:
                    color = (0, 0, 255)  # Blue = path
                else:
                    color = (200, 200, 200)  # Gray = empty
                
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
        
        pygame.display.flip()
```

---

### Step 7: Create Main Program (Day 6)

**File: `main.py`**

```python
from game import PathfindingGame
from algorithms import bfs, astar
from visualizer import GameVisualizer

def main():
    # Create game
    game = PathfindingGame(width=10, height=10)
    
    # Add some walls
    game.add_wall(2, 1)
    game.add_wall(2, 2)
    game.add_wall(5, 3)
    game.add_wall(5, 4)
    
    # Visualize
    viz = GameVisualizer(game)
    
    # Find path using BFS
    print("Finding path with BFS...")
    path_bfs = bfs(game)
    if path_bfs:
        print(f"Path found: {len(path_bfs)} steps")
        viz.draw(path_bfs)
    else:
        print("No path found")
    
    # Find path using A*
    print("\nFinding path with A*...")
    path_astar = astar(game)
    if path_astar:
        print(f"Path found: {len(path_astar)} steps")
        viz.draw(path_astar)
    
    # Keep window open
    import time
    time.sleep(5)

if __name__ == "__main__":
    main()
```

---

---