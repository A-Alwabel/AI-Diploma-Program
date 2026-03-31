"""
Unit 2 - Exercise 1: Solutions
الوحدة 2 - تمرين 1: الحلول

Complete solutions to Exercise 1.
الحلول الكاملة للتمرين 1.
"""

from collections import deque

# Solution 1: Complete BFS
def bfs_complete(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

# Solution 2: DFS Path Finding
def dfs_path(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(start)
    path = path + [start]
    
    if start == goal:
        return path
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, visited, path)
            if result:
                return result
    
    return None

# Solution 3: Maze Solver
def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set([start])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    
    while queue:
        (row, col), path = queue.popleft()
        
        if (row, col) == end:
            return path
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 1 and
                (new_row, new_col) not in visited):
                visited.add((new_row, new_col))
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    return None

# Test solutions
if __name__ == "__main__":
    graph = {
        '1': ['2', '3'],
        '2': ['1', '4', '5'],
        '3': ['1', '6'],
        '4': ['2'],
        '5': ['2', '6'],
        '6': ['3', '5']
    }
    
    print("BFS Solution:")
    print(bfs_complete(graph, '1', '6'))
    
    print("\nDFS Solution:")
    print(dfs_path(graph, '4', '3'))

