#!/usr/bin/env python3
"""
Create Jupyter Notebooks for all modules.

This script generates the notebook structure for modules 02-05.
"""

import json
from pathlib import Path

def create_notebook(module_num):
    """Create a Jupyter notebook for a module."""
    
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Module {module_num:02d}: [Topic Name]\n",
                    "\n",
                    f"> **Note**: Content should be populated from `course-content/{module_num:02d}.pptx`\n",
                    "\n",
                    "---\n",
                    "\n",
                    "## Learning Objectives\n",
                    "\n",
                    "In this module, you will learn:\n",
                    "- The fundamental concepts\n",
                    "- How to implement solutions\n",
                    "- How to analyze and interpret results\n",
                    "\n",
                    "---"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Part 1: WHY\n",
                    "\n",
                    "## Understanding the Motivation\n",
                    "\n",
                    "### Why does this matter?\n",
                    "\n",
                    "**TODO**: Add content from your PowerPoint explaining:\n",
                    "- The problem we're solving\n",
                    "- Why this concept is important\n",
                    "- Real-world applications\n",
                    "- Common scenarios where this is used\n",
                    "\n",
                    "### Real-World Example\n",
                    "\n",
                    "**TODO**: Add a concrete example from your slides"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Why this concept matters\n",
                    "# Add your demonstration code here\n",
                    "\n",
                    "print(\"Why Section - Understanding the motivation\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n",
                    "\n",
                    "# Part 2: HOW\n",
                    "\n",
                    "## Implementation and Practical Application\n",
                    "\n",
                    "### Step-by-Step Explanation\n",
                    "\n",
                    "**TODO**: Add step-by-step explanation from your PowerPoint:\n",
                    "\n",
                    "1. **Step 1**: [Description]\n",
                    "2. **Step 2**: [Description]\n",
                    "3. **Step 3**: [Description]"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Basic implementation\n",
                    "# Add your code examples here with detailed comments\n",
                    "\n",
                    "def example_function():\n",
                    "    \"\"\"\n",
                    "    Example function demonstrating the concept.\n",
                    "    \n",
                    "    TODO: Replace with actual implementation from your slides\n",
                    "    \"\"\"\n",
                    "    pass\n",
                    "\n",
                    "# Call the function\n",
                    "result = example_function()\n",
                    "print(f\"Result: {result}\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Interactive Example\n",
                    "# Add more complex examples here\n",
                    "\n",
                    "print(\"How Section - Implementation details\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "### Best Practices\n",
                    "\n",
                    "**TODO**: Add best practices and tips from your slides:\n",
                    "\n",
                    "- Tip 1\n",
                    "- Tip 2\n",
                    "- Tip 3"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n",
                    "\n",
                    "# Part 3: AFTER\n",
                    "\n",
                    "## Analyzing Results and Understanding Implications\n",
                    "\n",
                    "### What Happens Next?\n",
                    "\n",
                    "**TODO**: Add content explaining:\n",
                    "- What the results mean\n",
                    "- How to interpret the output\n",
                    "- Common outcomes\n",
                    "- Next steps"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Analyzing results\n",
                    "# Add code to demonstrate result analysis\n",
                    "\n",
                    "print(\"After Section - Understanding results\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "### Common Pitfalls and How to Avoid Them\n",
                    "\n",
                    "**TODO**: Add common mistakes and solutions:\n",
                    "\n",
                    "1. **Pitfall 1**: Description and solution\n",
                    "2. **Pitfall 2**: Description and solution"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "### Advanced Topics\n",
                    "\n",
                    "**TODO**: Add advanced concepts for further learning:\n",
                    "\n",
                    "- Advanced topic 1\n",
                    "- Advanced topic 2"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n",
                    "\n",
                    "# Summary\n",
                    "\n",
                    "## Key Takeaways\n",
                    "\n",
                    "**TODO**: Summarize the main points:\n",
                    "\n",
                    "1. Key point 1\n",
                    "2. Key point 2\n",
                    "3. Key point 3\n",
                    "\n",
                    "## Next Steps\n",
                    "\n",
                    f"1. Complete the exercises in the `exercises/` folder\n",
                    "2. Review the solutions if needed\n",
                    f"3. Move on to Module {(module_num + 1) % 6 if module_num < 5 else 'advanced topics'}\n",
                    "\n",
                    "---\n",
                    "\n",
                    "**Ready for exercises?** Navigate to the `exercises/` folder and start practicing!"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Fix the next module reference for module 05
    if module_num == 5:
        notebook["cells"][-1]["source"][-6] = "3. Explore advanced topics and continue learning\n"
    
    notebook_path = Path(f"modules/module_{module_num:02d}/notebook_{module_num:02d}_why_how_after.ipynb")
    notebook_path.write_text(json.dumps(notebook, indent=1))
    print(f"✓ Created notebook for Module {module_num:02d}")


def main():
    """Create notebooks for all modules."""
    print("Creating Jupyter notebooks...")
    
    for module_num in range(2, 6):  # Modules 02-05
        create_notebook(module_num)
    
    print("\n✓ All notebooks created successfully!")


if __name__ == "__main__":
    main()

