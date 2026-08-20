# Project 01: Pathfinding Game

## Overview

Build a pathfinding game where players navigate through a maze using AI search algorithms.

**Learning Objectives:**
- Implement BFS, DFS, and A* algorithms
- Visualize search algorithms in action
- Create an interactive game interface

---

## Requirements

### Functional Requirements
1. **Maze Generation**
   - Generate random mazes or load from file
   - Display maze visually using Matplotlib
   - Mark start and end points

2. **Search Algorithm Implementation**
   - Implement BFS algorithm
   - Implement DFS algorithm
   - Implement A* algorithm
   - Show path visualization

3. **User Interface**
   - Allow user to select algorithm
   - Show algorithm execution step-by-step
   - Display final path
   - Show statistics (path length, nodes explored, time taken)

4. **Comparison Feature**
   - Compare all three algorithms side-by-side
   - Show which algorithm found the shortest path
   - Display performance metrics

### Technical Requirements
- Use Python 3.9+
- Use Matplotlib for visualization
- Use collections.deque for BFS queue
- Use heapq for A* priority queue
- Code should be well-commented
- Include error handling

---

## Deliverables

1. **Source Code**
   - `maze_generator.py` - Maze generation
   - `pathfinding.py` - Search algorithms
   - `game_interface.py` - User interface
   - `main.py` - Main program

2. **Documentation**
   - README.md explaining how to run
   - Code comments explaining algorithms
   - User guide

3. **Demo**
   - Working demonstration
   - Screenshots or video of game in action

---

## Project Structure

```
project_01_pathfinding/
├── maze_generator.py
├── pathfinding.py
├── game_interface.py
├── main.py
├── README.md
└── requirements.txt
```

---

## Evaluation Criteria

See `../../ASSESSMENTS/Project_Rubric.md` for detailed rubric.

**Key Areas:**
- Algorithm correctness (40%)
- Code quality (20%)
- Visualization (20%)
- Documentation (10%)
- Creativity (10%)

---

## Bonus Features

- [ ] Allow user to draw custom mazes
- [ ] Add more algorithms (Dijkstra, Greedy Best-First)
- [ ] Add obstacles that move
- [ ] Multi-level mazes
- [ ] Save/load game states

---

## Resources

- Notebook 01: Introduction & Search Algorithms
- NetworkX documentation for graph visualization
- Matplotlib animation examples

---

## Submission

Submit:
1. All source code files
2. README.md
3. Screenshots or demo video
4. Brief report explaining your implementation

**Due Date:** [Set by instructor]

---

**Created**: 2025  
**For**: Python for AI Course - 112 AIAT
