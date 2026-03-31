#!/usr/bin/env python3
"""
Fix the remaining 34 markdown_in_code issues directly.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# All 34 remaining issues
FIXES = [
    ('Course 01/unit1-ai-foundations/examples/05_adversarial_search_minimax.ipynb', 4),
    ('Course 01/unit1-ai-foundations/examples/06_knowledge_representation.ipynb', 2),
    ('Course 02/NOTEBOOKS/02_Knowledge_Representation.ipynb', 7),
    ('Course 02/NOTEBOOKS/02_Knowledge_Representation.ipynb', 15),
    ('Course 02/NOTEBOOKS/03_Learning_Under_Uncertainty.ipynb', 6),
    ('Course 02/NOTEBOOKS/05_AI_Learning_Models.ipynb', 11),
    ('Course 02/unit2-knowledge-representation/examples/02_Knowledge_Representation.ipynb', 8),
    ('Course 02/unit2-knowledge-representation/examples/02_Knowledge_Representation.ipynb', 16),
    ('Course 02/unit2-knowledge-representation/examples/05_first_order_logic_fol.ipynb', 7),
    ('Course 02/unit3-learning-under-uncertainty/examples/03_Learning_Under_Uncertainty.ipynb', 7),
    ('Course 02/unit5-ai-learning-models/examples/05_AI_Learning_Models.ipynb', 12),
    ('Course 03/unit1-linear-algebra/examples/05_determinants_inverse_matrices.ipynb', 5),
    ('Course 03/unit1-linear-algebra/examples/06_transformation_matrices_orthogonal_basis.ipynb', 3),
    ('Course 03/unit1-linear-algebra/examples/08_ml_parameter_experiments.ipynb', 4),
    ('Course 03/unit2-calculus/examples/05_function_approximation_ml.ipynb', 7),
    ('Course 03/unit3-optimization/examples/05_image_similarity_measures.ipynb', 5),
    ('Course 03/unit5-probability/examples/06_maximum_likelihood_estimation.ipynb', 3),
    ('Course 03/unit5-probability/examples/06_maximum_likelihood_estimation.ipynb', 5),
    ('Course 05/unit1-introduction/examples/05_jupyter_notebooks_best_practices.ipynb', 1),
    ('Course 05/unit1-introduction/examples/05_jupyter_notebooks_best_practices.ipynb', 7),
    ('Course 05/unit1-introduction/examples/05_jupyter_notebooks_best_practices.ipynb', 11),
    ('Course 05/unit1-introduction/examples/06_data_structures_lists_dictionaries.ipynb', 13),
    ('Course 05/unit1-introduction/examples/08_numba_jit_compilation.ipynb', 3),
    ('Course 05/unit3-visualization/examples/01_chart_types_matplotlib_seaborn.ipynb', 11),
    ('Course 05/unit3-visualization/examples/06_customizing_annotating_visualizations.ipynb', 11),
    ('Course 05/unit5-scaling/examples/08_deployment.ipynb', 16),
    ('Course 05/unit5-scaling/examples/10_data_pipeline_automation.ipynb', 3),
    ('Course 05/unit5-scaling/examples/10_data_pipeline_automation.ipynb', 4),
    ('Course 07/unit4-deep-learning-nlp/examples/03_bert_advanced_usage.ipynb', 5),
    ('Course 07/unit4-deep-learning-nlp/examples/04_seq2seq_attention_translation.ipynb', 5),
    ('Course 08/unit5-deployment/examples/06_flask_fastapi_deployment.ipynb', 7),
    ('Course 09/unit2-policy-value/examples/06_policy_vs_value_iteration_comparison.ipynb', 5),
    ('Course 09/unit2-policy-value/examples/06_policy_vs_value_iteration_comparison.ipynb', 7),
    ('Course 11/unit4-containers-orchestration/examples/02_kubernetes_deployment.ipynb', 6),
]

def convert_to_markdown(source: str) -> str:
    """Convert code with docstrings/comments to markdown."""
    lines = source.split('\n')
    new_lines = []
    in_docstring = False
    
    for line in lines:
        stripped = line.strip()
        
        # Handle docstrings
        if '"""' in stripped or "'''" in stripped:
            cleaned = re.sub(r'["\']{3}', '', stripped)
            if cleaned.strip():
                new_lines.append(cleaned.strip())
            in_docstring = not in_docstring
            continue
        
        if in_docstring:
            if stripped:
                new_lines.append(stripped)
            continue
        
        # Handle comments
        if stripped.startswith('#'):
            cleaned = stripped.replace('#', '', 1).strip()
            if cleaned:
                new_lines.append(cleaned)
            continue
        
        # Keep other lines
        if stripped:
            new_lines.append(stripped)
    
    return '\n'.join(new_lines)

def main():
    """Main function."""
    print("🔧 Fixing remaining 34 markdown_in_code issues...\n")
    
    fixed_count = 0
    
    for nb_path_str, cell_idx in FIXES:
        nb_path = BASE_DIR / nb_path_str
        if not nb_path.exists():
            continue
        
        try:
            with open(nb_path) as f:
                nb = json.load(f)
            
            if cell_idx < len(nb['cells']):
                cell = nb['cells'][cell_idx]
                if cell.get('cell_type') == 'code':
                    source = ''.join(cell.get('source', []))
                    # Convert to markdown
                    cell['cell_type'] = 'markdown'
                    cell['source'] = convert_to_markdown(source).splitlines(keepends=True)
                    
                    with open(nb_path, 'w') as f:
                        json.dump(nb, f, indent=1, ensure_ascii=False)
                    fixed_count += 1
                    print(f"  ✓ Fixed: {nb_path_str} - Cell {cell_idx}")
        except Exception as e:
            print(f"  ✗ Error fixing {nb_path_str} - Cell {cell_idx}: {e}")
    
    print(f"\n✅ Fixed {fixed_count}/34 issues")

if __name__ == "__main__":
    main()
