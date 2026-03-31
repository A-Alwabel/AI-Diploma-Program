"""
Pathfinding Game - Complete Solution
Complete implementation of BFS, DFS, and A* algorithms with visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import heapq
import random

class Maze:
    """Represents a maze for pathfinding."""
    
    def __init__(self, width=10, height=10, wall_probability=0.3):
        """
        Initialize maze.
        
        Args:
            width: Maze width
            height: Maze height
            wall_probability: Probability of a cell being a wall (0-1)
        """
        self.width = width
        self.height = height
        # Create grid: 0 = path, 1 = wall
        self.grid = np.zeros((height, width), dtype=int)
        
        # Randomly place walls
        for y in range(height):
            for x in range(width):
                if random.random() < wall_probability:
                    self.grid[y][x] = 1
        
        # Ensure start and goal are paths
        self.start = (0, 0)
        self.goal = (width - 1, height - 1)
        self.grid[self.start[1]][self.start[0]] = 0
        self.grid[self.goal[1]][self.goal[0]] = 0
    
    def is_valid(self, x, y):
        """Check if position is valid (within bounds and not a wall)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x] == 0
        return False
    
    def get_neighbors(self, x, y):
        """Get valid neighboring cells (4-directional)."""
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                neighbors.append((nx, ny))
        
        return neighbors


def bfs(maze, start, goal):
    """
    Breadth-First Search algorithm.
    Finds shortest path (fewest steps).
    
    Returns:
        List of coordinates representing the path, or empty list if no path found
    """
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    while queue:
        current = queue.popleft()
        
        if current == goal:
            # Reconstruct path
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]  # Reverse to get path from start to goal
        
        for neighbor in maze.get_neighbors(*current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    return []  # No path found


def dfs(maze, start, goal):
    """
    Depth-First Search algorithm.
    Explores deeply before backtracking.
    
    Returns:
        List of coordinates representing the path, or empty list if no path found
    """
    stack = [start]
    visited = {start}
    parent = {start: None}
    
    while stack:
        current = stack.pop()
        
        if current == goal:
            # Reconstruct path
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        
        for neighbor in maze.get_neighbors(*current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
    
    return []


def heuristic(x1, y1, x2, y2):
    """
    Heuristic function for A* (Manhattan distance).
    
    Args:
        x1, y1: Current position
        x2, y2: Goal position
    
    Returns:
        Manhattan distance
    """
    return abs(x1 - x2) + abs(y1 - y2)


def astar(maze, start, goal):
    """
    A* Search algorithm.
    Finds optimal path using heuristic.
    
    Returns:
        List of coordinates representing the path, or empty list if no path found
    """
    # Priority queue: (f_score, g_score, position)
    open_set = [(0, 0, start)]
    came_from = {}
    g_score = {start: 0}  # Cost from start
    f_score = {start: heuristic(*start, *goal)}  # Estimated total cost
    
    visited = set()
    
    while open_set:
        current_f, current_g, current = heapq.heappop(open_set)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        if current == goal:
            # Reconstruct path
            path = []
            node = goal
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            return path[::-1]
        
        for neighbor in maze.get_neighbors(*current):
            if neighbor in visited:
                continue
            
            # Tentative g_score
            tentative_g = current_g + 1
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                h = heuristic(*neighbor, *goal)
                f_score[neighbor] = tentative_g + h
                heapq.heappush(open_set, (f_score[neighbor], tentative_g, neighbor))
    
    return []


def visualize_maze(maze, path=None, algorithm_name="", visited=None):
    """
    Visualize maze and path.
    
    Args:
        maze: Maze object
        path: List of coordinates representing the path
        algorithm_name: Name of algorithm used
        visited: Set of visited nodes (optional)
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Create visualization grid
    vis_grid = np.zeros((maze.height, maze.width))
    
    # Mark walls
    vis_grid[maze.grid == 1] = 1
    
    # Mark visited nodes (lighter color)
    if visited:
        for x, y in visited:
            if (x, y) != maze.start and (x, y) != maze.goal:
                vis_grid[y][x] = 0.5
    
    # Display grid
    ax.imshow(vis_grid, cmap='gray', origin='upper')
    
    # Mark start (green)
    ax.plot(maze.start[0], maze.start[1], 'go', markersize=15, label='Start')
    
    # Mark goal (red)
    ax.plot(maze.goal[0], maze.goal[1], 'ro', markersize=15, label='Goal')
    
    # Draw path if provided
    if path and len(path) > 1:
        path_x = [p[0] for p in path]
        path_y = [p[1] for p in path]
        ax.plot(path_x, path_y, 'b-', linewidth=2, label='Path')
        ax.plot(path_x, path_y, 'bo', markersize=8)
    
    ax.set_title(f'{algorithm_name} - Path Length: {len(path) if path else "No Path"}', 
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def compare_algorithms(maze):
    """Compare all three algorithms on the same maze."""
    print("=" * 60)
    print("PATHFINDING ALGORITHM COMPARISON")
    print("=" * 60)
    print(f"\nMaze Size: {maze.width}x{maze.height}")
    print(f"Start: {maze.start}")
    print(f"Goal: {maze.goal}\n")
    
    # BFS
    print("Running BFS...")
    bfs_path = bfs(maze, maze.start, maze.goal)
    print(f"BFS Path Length: {len(bfs_path)}")
    if bfs_path:
        print(f"BFS Path: {bfs_path[:5]}...{bfs_path[-5:]}")
    visualize_maze(maze, bfs_path, "BFS")
    
    # DFS
    print("\nRunning DFS...")
    dfs_path = dfs(maze, maze.start, maze.goal)
    print(f"DFS Path Length: {len(dfs_path)}")
    if dfs_path:
        print(f"DFS Path: {dfs_path[:5]}...{dfs_path[-5:]}")
    visualize_maze(maze, dfs_path, "DFS")
    
    # A*
    print("\nRunning A*...")
    astar_path = astar(maze, maze.start, maze.goal)
    print(f"A* Path Length: {len(astar_path)}")
    if astar_path:
        print(f"A* Path: {astar_path[:5]}...{astar_path[-5:]}")
    visualize_maze(maze, astar_path, "A*")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"BFS Path Length: {len(bfs_path) if bfs_path else 'No path'}")
    print(f"DFS Path Length: {len(dfs_path) if dfs_path else 'No path'}")
    print(f"A* Path Length: {len(astar_path) if astar_path else 'No path'}")
    
    if bfs_path and dfs_path and astar_path:
        print(f"\nShortest path: {'BFS' if len(bfs_path) <= len(astar_path) else 'A*'}")
        print(f"Longest path: DFS ({len(dfs_path)} steps)")


def main():
    """Main function to run pathfinding game."""
    print("Pathfinding Game - Complete Solution")
    print("=" * 60)
    
    # Create maze
    print("\nCreating maze...")
    maze = Maze(width=15, height=15, wall_probability=0.25)
    
    # Compare algorithms
    compare_algorithms(maze)


if __name__ == "__main__":
    main()

