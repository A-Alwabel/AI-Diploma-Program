#!/usr/bin/env python3
"""
Course Setup Script

This script helps set up the course structure for all modules.
Run this to ensure all modules have the proper structure.
"""

import os
from pathlib import Path

def create_module_structure(module_num):
    """Create the structure for a module."""
    base_path = Path(f"modules/module_{module_num:02d}")
    
    # Create directories
    (base_path / "exercises" / "solutions").mkdir(parents=True, exist_ok=True)
    (base_path / "scripts").mkdir(parents=True, exist_ok=True)
    
    # Create README
    readme_content = f"""# Module {module_num:02d}: [Topic Name]

> **Note**: This module content should be populated from `course-content/{module_num:02d}.pptx`

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Understand the fundamental concepts
- [ ] Implement basic solutions
- [ ] Analyze results and outcomes
- [ ] Apply knowledge to solve problems

## Prerequisites

- Completion of previous modules (if applicable)
- Python environment set up

## Estimated Time

- Reading and following along: 30-45 minutes
- Exercises: 20-30 minutes
- Total: ~1 hour

## Module Structure

1. **Why**: Understanding the motivation
2. **How**: Learning the implementation
3. **After**: Analyzing results and next steps

## Getting Started

1. Open `notebook_{module_num:02d}_why_how_after.ipynb` in Jupyter
2. Follow along with the explanations
3. Run each code cell
4. Complete the exercises in the `exercises/` folder

## Exercises

Practice problems are located in the `exercises/` directory. Try to solve them before checking the solutions!
"""
    
    (base_path / "README.md").write_text(readme_content)
    
    # Create exercise template
    exercise_content = f'''"""
Exercise 01: [Exercise Name]

TODO: Add exercise description from your PowerPoint slides

Instructions:
1. Read the problem statement carefully
2. Implement your solution
3. Test your solution
4. Compare with the solution in solutions/solution_01.py
"""

# TODO: Add your exercise problem here

def solve_problem(input_data):
    """
    Solve the given problem.
    
    Args:
        input_data: Description of input
        
    Returns:
        Description of output
    """
    # Your solution here
    pass


# Test your solution
if __name__ == "__main__":
    # Add test cases here
    test_input = None  # TODO: Add test input
    result = solve_problem(test_input)
    print(f"Result: {{result}}")
'''
    
    (base_path / "exercises" / "exercise_01.py").write_text(exercise_content)
    
    # Create solution template
    solution_content = f'''"""
Solution 01: [Exercise Name]

This is the reference solution for exercise_01.py
"""

def solve_problem(input_data):
    """
    Solve the given problem.
    
    Args:
        input_data: Description of input
        
    Returns:
        Description of output
    """
    # TODO: Add solution implementation
    pass


# Test the solution
if __name__ == "__main__":
    # Add test cases here
    test_input = None  # TODO: Add test input
    result = solve_problem(test_input)
    print(f"Result: {{result}}")
    print("Solution verified!")
'''
    
    (base_path / "exercises" / "solutions" / "solution_01.py").write_text(solution_content)
    
    # Create utils template
    utils_content = f'''"""
Utility functions for Module {module_num:02d} demonstrations.

This file contains helper functions used in the module notebooks and exercises.
"""

def helper_function():
    """
    Example helper function.
    
    TODO: Add utility functions as needed for demonstrations
    """
    pass


def visualize_results(data):
    """
    Visualize results for better understanding.
    
    Args:
        data: Data to visualize
    """
    # TODO: Add visualization code
    pass
'''
    
    (base_path / "scripts" / "utils.py").write_text(utils_content)
    
    print(f"✓ Created structure for Module {module_num:02d}")


def main():
    """Set up all modules."""
    print("Setting up course structure...")
    
    for module_num in range(2, 6):  # Modules 02-05
        create_module_structure(module_num)
    
    print("\n✓ Course structure setup complete!")
    print("\nNext steps:")
    print("1. Create Jupyter notebooks for each module")
    print("2. Populate content from PowerPoint files")
    print("3. Add exercises and solutions")


if __name__ == "__main__":
    main()

