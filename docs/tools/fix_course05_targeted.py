#!/usr/bin/env python3
"""
Targeted fixes for Course 05 notebooks - handles specific patterns carefully.
"""

import nbformat
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent

def fix_cell_source(source):
    """Fix common patterns in Course 05 notebooks."""
    original = source
    fixed = source
    
    # Pattern 1: import pandas as pd_rng -> import pandas as pd\n_rng = np.random.default_rng(7)
    if 'import pandas as pd_rng' in fixed:
        fixed = fixed.replace('import pandas as pd_rng', 'import pandas as pd\n_rng = np.random.default_rng(7)')
    
    # Pattern 2: import numpy as np import pandas -> separate lines
    fixed = re.sub(r'import numpy as np import pandas', 'import numpy as np\nimport pandas', fixed)
    
    # Pattern 2b: import pandas as pd   import numpy -> separate lines and fix order
    fixed = re.sub(r'import pandas as pd\s{2,}import numpy as np', 'import numpy as np\nimport pandas as pd', fixed)
    
    # Pattern 2c: import ...    from sklearn -> separate lines
    fixed = re.sub(r'(import\s+\w+\s+as\s+\w+)\s{2,}(from\s+sklearn)', r'\1\n\2', fixed)
    
    # Pattern 2d: import numpy as np import pandas as pd    from sklearn -> all separate
    fixed = re.sub(r'(import\s+\w+\s+as\s+\w+)\s+(import\s+\w+\s+as\s+\w+)\s{2,}(from)', r'\1\n\2\n\3', fixed)
    
    # Pattern 3: from sklearn.xxx  import (double space) -> single space
    fixed = re.sub(r'from sklearn\.(\w+)\s{2,}import', r'from sklearn.\1 import', fixed)
    fixed = re.sub(r'from sklearn\.(\w+)\.(\w+)\s{2,}import', r'from sklearn.\1.\2 import', fixed)
    
    # Pattern 4: dataset_rng = np.random -> dataset\n_rng = np.random
    fixed = re.sub(r'(\w+)dataset_rng\s*=\s*np\.random', r'\1dataset\n_rng = np.random', fixed)
    fixed = re.sub(r'#\s*(\w+)\s*dataset_rng\s*=', r'# \1 dataset\n_rng =', fixed)
    
    # Pattern 5: code_variable = value -> code\nvariable = value (but only for specific patterns)
    # Only fix when it's clearly a separate statement, not part of a function call
    lines = fixed.split('\n')
    fixed_lines = []
    for line in lines:
        # Skip comments
        if line.lstrip().startswith('#'):
            fixed_lines.append(line)
            continue
        
        # Fix: value)_variable = -> value)\nvariable =
        line = re.sub(r'\)\)_([a-z]\w*)\s*=\s*', r'))\n\1 = ', line)
        
        # Fix: value)_X = -> value)\nX =
        line = re.sub(r'\)\)_X\s*=\s*', r'))\nX = ', line)
        line = re.sub(r'\)\)_y\s*=\s*', r'))\ny = ', line)
        
        # Fix: code_x1 = rng. -> code\nx1 = rng.
        line = re.sub(r'(\w+)_([a-z]\w*)\s*=\s*(rng\.|_rng\.)', r'\1\n\2 = \3', line)
        
        # Fix: code_color = rng. -> code\ncolor = rng.
        line = re.sub(r'(\w+)_color\s*=\s*(rng\.|_rng\.)', r'\1\ncolor = \2', line)
        
        # Fix: code_x2 = rng. -> code\nx2 = rng.
        line = re.sub(r'(\w+)_x2\s*=\s*(rng\.|_rng\.)', r'\1\nx2 = \2', line)
        
        # Fix: code_age = rng. -> code\nage = rng.
        line = re.sub(r'(\w+)_age\s*=\s*(rng\.|_rng\.)', r'\1\nage = \2', line)
        
        # Fix: code_income = rng. -> code\nincome = rng.
        line = re.sub(r'(\w+)_income\s*=\s*(rng\.|_rng\.)', r'\1\nincome = \2', line)
        
        # Fix: code_city = rng. -> code\ncity = rng.
        line = re.sub(r'(\w+)_city\s*=\s*(rng\.|_rng\.)', r'\1\ncity = \2', line)
        
        # Fix: code_clicked = -> code\nclicked =
        line = re.sub(r'(\w+)_clicked\s*=', r'\1\nclicked =', line)
        
        # Fix: _rng = ... = ... (duplicate assignment)
        line = re.sub(r'_rng\s*=\s*np\.random\.default_rng\([^)]+\)\s*=\s*np\.random\.default_rng\([^)]+\)', '_rng = np.random.default_rng(7)', line)
        
        # Fix: code)_variable = -> code)\nvariable =
        line = re.sub(r'(\w+)\)_([a-z]\w*)\s*=', r'\1)\n\2 =', line)
        
        # Fix: # comment_variable[...] -> # comment\nvariable[...]
        line = re.sub(r'(#\s*[^_]+)_([a-z]\w*)\[', r'\1\n\2[', line)
        
        # Fix: # comment_variable = -> # comment\nvariable =
        line = re.sub(r'(#\s*[^_]+)_([a-z]\w*)\s*=', r'\1\n\2 =', line)
        
        # Fix: variable = ..._variable = ... (duplicate assignments - keep first)
        if ' = ' in line:
            parts = line.split(' = ')
            if len(parts) > 2:
                # Check if it's a duplicate pattern like "income = ...income = ..."
                var_name = parts[0].split()[-1] if parts[0].split() else ''
                if var_name and f'{var_name} =' in ' = '.join(parts[1:]):
                    # Keep only first assignment
                    line = ' = '.join([parts[0], ' = '.join(parts[1:]).split(f'{var_name} =')[0].rstrip()])
        
        # Fix: _variable[...] -> variable[...] (when _variable is used incorrectly)
        line = re.sub(r'_([a-z]\w*)\[', r'\1[', line)
        
        # Fix: rng.choice -> _rng.choice (when _rng is defined)
        if '_rng = np.random.default_rng' in '\n'.join(fixed_lines + [line]):
            line = re.sub(r'\brng\.choice', '_rng.choice', line)
            line = re.sub(r'\brng\.normal', '_rng.normal', line)
            line = re.sub(r'\brng\.integers', '_rng.integers', line)
        
        # Fix: n samples = -> n_samples = (or n = ... samples = ...)
        line = re.sub(r'\bn samples\s*=', 'n_samples =', line)
        
        # Fix: print statements with missing quotes (common pattern)
        if 'print(' in line and line.count('"') % 2 != 0 and not line.rstrip().endswith('"'):
            # Try to fix unterminated strings
            if '"' in line:
                # Add closing quote if it's clearly missing
                if not line.rstrip().endswith('\\"'):
                    line = line.rstrip() + '"'
        
        # Fix: import ... as sns_sns. -> import ... as sns\nsns.
        line = re.sub(r'import\s+(\w+)\s+as\s+(\w+)_(\2\.)', r'import \1 as \2\n\3', line)
        
        # Fix: # comment_ (trailing underscore)
        line = re.sub(r'(#\s*[^_]+)_$', r'\1', line)
        
        # Fix: _variable = value -> variable = value (when at start of line)
        if re.match(r'^_([a-z]\w*)\s*=\s*', line) and not line.startswith('_rng'):
            line = re.sub(r'^_([a-z]\w*)\s*=\s*', r'\1 = ', line)
        
        # Fix: rng. -> _rng. (when rng is used but _rng was defined)
        # Check previous lines for _rng definition
        prev_text = '\n'.join(fixed_lines + [line])
        if '_rng = np.random.default_rng' in prev_text:
            line = re.sub(r'\brng\.', '_rng.', line)
            line = re.sub(r'\brng\[', '_rng[', line)
            line = re.sub(r'\brng\s', '_rng ', line)
        
        fixed_lines.append(line)
    
    fixed = '\n'.join(fixed_lines)
    
    # Pattern 6: Fix visualization comments
    fixed = re.sub(r'# Visualization:.*?t r', '# Visualization:', fixed, flags=re.DOTALL)
    fixed = re.sub(r'# تصور:.*?t r', '# تصور:', fixed, flags=re.DOTALL)
    
    return fixed if fixed != original else original

def fix_notebook(notebook_path):
    """Fix a single notebook."""
    try:
        nb = nbformat.read(notebook_path, as_version=4)
        modified = False
        
        for cell in nb.cells:
            if cell.cell_type != 'code':
                continue
            
            original_source = cell.source
            fixed_source = fix_cell_source(original_source)
            
            if fixed_source != original_source:
                cell.source = fixed_source
                modified = True
        
        if modified:
            nbformat.write(nb, notebook_path)
            return True
        return False
    except Exception as e:
        print(f"Error fixing {notebook_path}: {e}")
        return False

def main():
    """Fix Course 05 notebooks."""
    course_05_notebooks = [
        BASE_DIR / "Course 05" / "unit1-introduction" / "examples" / "02_pandas_numpy_basics.ipynb",
        BASE_DIR / "Course 05" / "unit1-introduction" / "examples" / "03_cudf_introduction.ipynb",
        BASE_DIR / "Course 05" / "unit1-introduction" / "examples" / "data_science_applications_working_on_small_real_world_projects_using_data_scienc.ipynb",
        BASE_DIR / "Course 05" / "unit1-introduction" / "examples" / "python_programming_executing_python_code_to_solve_basic_tasks_like_arithmetic_op.ipynb",
        BASE_DIR / "Course 05" / "unit1-introduction" / "examples" / "using_jupyter_notebooks_writing_and_executing_code_in_jupyter_notebooks_combinin.ipynb",
        BASE_DIR / "Course 05" / "unit1-introduction" / "examples" / "working_with_data_structures_performing_tasks_like_indexing_slicing_and_transfor.ipynb",
        BASE_DIR / "Course 05" / "unit2-cleaning" / "examples" / "05_feature_transformation_scaling_encoding.ipynb",
        BASE_DIR / "Course 05" / "unit2-cleaning" / "examples" / "05_missing_values_duplicates.ipynb",
        BASE_DIR / "Course 05" / "unit2-cleaning" / "examples" / "07_cudf_import_export_gpu.ipynb",
        BASE_DIR / "Course 05" / "unit2-cleaning" / "examples" / "feature_transformation_transforming_data_eg_scaling_encoding_to_prepare_it_for_a.ipynb",
        BASE_DIR / "Course 05" / "unit2-cleaning" / "examples" / "performing_eda_visualizing_data_distributions_and_relationships_to_discover_insi.ipynb",
        BASE_DIR / "Course 05" / "unit3-visualization" / "examples" / "applying_visualization_best_practices_for_data_storytelling.ipynb",
        BASE_DIR / "Course 05" / "unit3-visualization" / "examples" / "building_interactive_visualizations_and_dashboards_with_plotly.ipynb",
        BASE_DIR / "Course 05" / "unit3-visualization" / "examples" / "creating_various_chart_types_using_matplotlib_and_seaborn.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "06_data_preparation_ml_tasks.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "07_implementing_ml_models_scikit_learn.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "07_implementing_ml_models_sklearn.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "08_supervised_learning_logistic_regression.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "10_hyperparameter_tuning_grid_random_search.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "11_real_world_problem_solving.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "12_model_evaluation.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "13_cpu_vs_gpu_ml.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "applying_supervised_learning_algorithms_on_labeled_data_eg_logistic_regression.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "applying_unsupervised_learning_techniques_eg_k_means_clustering_on_unlabeled_dat.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "cleaning_and_preparing_data_for_ml_tasks_handling_missing_values_encoding_catego.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "hyperparameter_tuning_using_techniques_like_grid_search_and_random_search.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "implementing_ml_models_using_scikit_learn_library_regression_classification.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "real_world_problem_solving_using_a_mix_of_supervised_and_unsupervised_learning_a.ipynb",
        BASE_DIR / "Course 05" / "unit4-ml-intro" / "examples" / "working_with_data_using_python_libraries_like_pandas.ipynb",
        BASE_DIR / "Course 05" / "unit5-scaling" / "examples" / "17_performance_optimization.ipynb",
        BASE_DIR / "Course 05" / "unit5-scaling" / "examples" / "18_large_datasets.ipynb",
        BASE_DIR / "Course 05" / "unit5-scaling" / "examples" / "19_deployment.ipynb",
        BASE_DIR / "Course 05" / "unit5-scaling" / "examples" / "accelerated_data_with_gpu_using_rapids_using_rapids_libraries_like_cudf_data_fra.ipynb",
    ]
    
    print(f"Fixing {len(course_05_notebooks)} Course 05 notebooks...\n")
    
    fixed_count = 0
    for nb_path in course_05_notebooks:
        if nb_path.exists():
            if fix_notebook(nb_path):
                fixed_count += 1
                print(f"Fixed: {nb_path.relative_to(BASE_DIR)}")
        else:
            print(f"Not found: {nb_path}")
    
    print(f"\nFixed {fixed_count} notebooks.")

if __name__ == "__main__":
    main()
