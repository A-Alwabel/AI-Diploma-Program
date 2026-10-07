"""
Pathfinding Game Template
Project 01 Template

Fill in the functions marked with TODO comments.
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import heapq

class Maze:
    """Represents a maze for pathfinding."""
    
    def __init__(self, width, height):
        """
        Initialize maze.
        
        TODO: Create a 2D grid (0 = wall, 1 = path)
        """
        self.width = width
        self.height = height
        # TODO: Initialize grid
        self.grid = None  # Replace with actual grid
        self.start = (0, 0)
        self.goal = (width - 1, height - 1)
    
    def is_valid(self, x, y):
        """Check if position is valid (within bounds and not a wall)."""
        # TODO: Implement validation
        pass
    
    def get_neighbors(self, x, y):
        """Get valid neighboring cells."""
        # TODO: Return list of valid neighbors (up, down, left, right)
        pass


def bfs(maze, start, goal):
    """
    Breadth-First Search algorithm.
    
    TODO: Implement BFS
    - Use deque for queue
    - Track visited nodes
    - Return path from start to goal
    """
    # TODO: Initialize queue with start
    # TODO: Track visited nodes
    # TODO: Track parent nodes (for path reconstruction)
    
    # TODO: Main BFS loop
    # while queue not empty:
    #   current = dequeue
    #   if current == goal: reconstruct path
    #   for each neighbor:
    #     if not visited: mark visited, enqueue
    
    # TODO: Return path (list of coordinates)
    return []


def dfs(maze, start, goal):
    """
    Depth-First Search algorithm.
    
    TODO: Implement DFS
    - Use list as stack
    - Track visited nodes
    - Return path from start to goal
    """
    # TODO: Initialize stack with start
    # TODO: Track visited nodes
    # TODO: Track parent nodes
    
    # TODO: Main DFS loop
    # while stack not empty:
    #   current = pop from stack
    #   if current == goal: reconstruct path
    #   for each neighbor:
    #     if not visited: mark visited, push to stack
    
    # TODO: Return path
    return []


def heuristic(x1, y1, x2, y2):
    """
    Heuristic function for A* (Manhattan distance).
    
    TODO: Calculate Manhattan distance
    """
    # TODO: Return |x1-x2| + |y1-y2|
    return 0


def astar(maze, start, goal):
    """
    A* Search algorithm.
    
    TODO: Implement A*
    - Use heapq for priority queue
    - f(n) = g(n) + h(n)
    - Track g(n) and h(n) values
    - Return path from start to goal
    """
    # TODO: Initialize priority queue
    # TODO: Track g(n) values (cost from start)
    # TODO: Track parent nodes
    
    # TODO: Main A* loop
    # while queue not empty:
    #   current = pop from queue (lowest f(n))
    #   if current == goal: reconstruct path
    #   for each neighbor:
    #     g_new = g(current) + 1
    #     f_new = g_new + h(neighbor, goal)
    #     if better path: update and add to queue
    
    # TODO: Return path
    return []


def visualize_maze(maze, path=None, algorithm_name=""):
    """
    Visualize maze and path.
    
    TODO: Use Matplotlib to draw:
    - Maze grid (walls in black, paths in white)
    - Start point (green)
    - Goal point (red)
    - Path (blue line if provided)
    """
    # TODO: Create figure
    # TODO: Draw grid
    # TODO: Mark start and goal
    # TODO: Draw path if provided
    # TODO: Add title with algorithm name
    # TODO: Show plot
    pass


def main():
    """Main function to run pathfinding game."""
    # Create maze
    maze = Maze(10, 10)
    
    # TODO: Generate or load maze
    # For now, create simple test maze
    
    # Run algorithms
    print("Running BFS...")
    bfs_path = bfs(maze, maze.start, maze.goal)
    visualize_maze(maze, bfs_path, "BFS")
    
    print("Running DFS...")
    dfs_path = dfs(maze, maze.start, maze.goal)
    visualize_maze(maze, dfs_path, "DFS")
    
    print("Running A*...")
    astar_path = astar(maze, maze.start, maze.goal)
    visualize_maze(maze, astar_path, "A*")
    
    # Compare results
    print(f"BFS path length: {len(bfs_path)}")
    print(f"DFS path length: {len(dfs_path)}")
    print(f"A* path length: {len(astar_path)}")


if __name__ == "__main__":
    main()

