#!/usr/bin/env python3
"""
Script to validate all Course 06 notebooks by executing them
and checking for errors and expected outputs.
"""

import json
import subprocess
import sys
import os
from pathlib import Path

# Define notebook execution order
NOTEBOOK_ORDER = [
    # Unit 1: Ethics Foundations
    ("unit1-ethics-foundations/examples/01_ethical_frameworks.ipynb", "Unit 1, Notebook 1"),
    ("unit1-ethics-foundations/examples/02_ethical_decision_making.ipynb", "Unit 1, Notebook 2"),
    ("unit1-ethics-foundations/examples/03_case_study_analysis.ipynb", "Unit 1, Notebook 3"),
    
    # Unit 2: Bias and Justice
    ("unit2-bias-justice/examples/01_bias_detection.ipynb", "Unit 2, Notebook 1"),
    ("unit2-bias-justice/examples/02_bias_mitigation.ipynb", "Unit 2, Notebook 2"),
    ("unit2-bias-justice/examples/03_fair_representation.ipynb", "Unit 2, Notebook 3"),
    ("unit2-bias-justice/examples/04_bias_case_studies.ipynb", "Unit 2, Notebook 4"),
    ("unit2-bias-justice/examples/05_fair_ai_development.ipynb", "Unit 2, Notebook 5"),
    
    # Unit 3: Privacy and Security
    ("unit3-privacy-security/examples/01_data_protection.ipynb", "Unit 3, Notebook 1"),
    ("unit3-privacy-security/examples/02_privacy_technologies.ipynb", "Unit 3, Notebook 2"),
    ("unit3-privacy-security/examples/03_differential_privacy.ipynb", "Unit 3, Notebook 3"),
    ("unit3-privacy-security/examples/04_gdpr_compliance.ipynb", "Unit 3, Notebook 4"),
    ("unit3-privacy-security/examples/05_secure_development.ipynb", "Unit 3, Notebook 5"),
    
    # Unit 4: Transparency and Accountability
    ("unit4-transparency-accountability/examples/01_shap_explanations.ipynb", "Unit 4, Notebook 1"),
    ("unit4-transparency-accountability/examples/02_lime_explanations.ipynb", "Unit 4, Notebook 2"),
    ("unit4-transparency-accountability/examples/03_counterfactual_analysis.ipynb", "Unit 4, Notebook 3"),
    ("unit4-transparency-accountability/examples/04_accountability_frameworks.ipynb", "Unit 4, Notebook 4"),
    ("unit4-transparency-accountability/examples/05_hitl_approaches.ipynb", "Unit 4, Notebook 5"),
    ("unit4-transparency-accountability/examples/06_transparency_tools.ipynb", "Unit 4, Notebook 6"),
    
    # Unit 5: Governance and Regulations
    ("unit5-governance-regulations/examples/01_global_regulations.ipynb", "Unit 5, Notebook 1"),
    ("unit5-governance-regulations/examples/02_industry_regulations.ipynb", "Unit 5, Notebook 2"),
    ("unit5-governance-regulations/examples/03_governance_frameworks.ipynb", "Unit 5, Notebook 3"),
    ("unit5-governance-regulations/examples/04_legal_challenges.ipynb", "Unit 5, Notebook 4"),
]

def check_notebook_structure(notebook_path):
    """Check if notebook has valid structure and required sections."""
    try:
        with open(notebook_path, 'r') as f:
            nb = json.load(f)
        
        issues = []
        
        # Check for problem introduction
        first_markdown = None
        for cell in nb['cells']:
            if cell['cell_type'] == 'markdown':
                content = ''.join(cell['source'])
                if 'THE PROBLEM' in content or 'المشكلة' in content:
                    first_markdown = content
                    break
        
        if not first_markdown:
            issues.append("Missing problem introduction section")
        
        # Check for limitation section
        has_limitation = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'markdown':
                content = ''.join(cell['source'])
                if 'limitation' in content.lower() or 'حد' in content or 'When.*Hits' in content:
                    has_limitation = True
                    break
        
        if not has_limitation and '04_legal_challenges' not in notebook_path:  # Last notebook has course completion instead
            issues.append("Missing limitation section")
        
        return issues
    except Exception as e:
        return [f"Error reading notebook: {str(e)}"]

def execute_notebook(notebook_path, base_dir):
    """Execute a notebook and return results."""
    full_path = os.path.join(base_dir, notebook_path)
    
    if not os.path.exists(full_path):
        return {
            'success': False,
            'error': f"Notebook not found: {full_path}",
            'output': None
        }
    
    # Execute using jupyter nbconvert
    try:
        result = subprocess.run(
            ['jupyter', 'nbconvert', '--to', 'notebook', '--execute', 
             '--inplace', '--ExecutePreprocessor.timeout=300', full_path],
            capture_output=True,
            text=True,
            timeout=600
        )
        
        if result.returncode == 0:
            return {
                'success': True,
                'error': None,
                'output': result.stdout
            }
        else:
            return {
                'success': False,
                'error': result.stderr,
                'output': result.stdout
            }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error': 'Execution timeout (exceeded 10 minutes)',
            'output': None
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'output': None
        }

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_dir)
    
    print("="*80)
    print("COURSE 06 NOTEBOOK VALIDATION")
    print("="*80)
    print()
    
    results = {
        'total': len(NOTEBOOK_ORDER),
        'passed': 0,
        'failed': 0,
        'skipped': 0,
        'details': []
    }
    
    for notebook_path, description in NOTEBOOK_ORDER:
        print(f"\n{'='*80}")
        print(f"Validating: {description}")
        print(f"Notebook: {notebook_path}")
        print(f"{'='*80}")
        
        # Check structure first
        structure_issues = check_notebook_structure(notebook_path)
        if structure_issues:
            print(f"⚠️  Structure issues: {', '.join(structure_issues)}")
        
        # Execute notebook
        print("Executing notebook...")
        exec_result = execute_notebook(notebook_path, base_dir)
        
        if exec_result['success']:
            print("✅ Notebook executed successfully!")
            results['passed'] += 1
            results['details'].append({
                'notebook': notebook_path,
                'description': description,
                'status': 'PASSED',
                'issues': structure_issues
            })
        else:
            print(f"❌ Notebook execution failed!")
            print(f"   Error: {exec_result['error']}")
            results['failed'] += 1
            results['details'].append({
                'notebook': notebook_path,
                'description': description,
                'status': 'FAILED',
                'error': exec_result['error'],
                'issues': structure_issues
            })
    
    # Summary
    print("\n" + "="*80)
    print("VALIDATION SUMMARY")
    print("="*80)
    print(f"Total notebooks: {results['total']}")
    print(f"✅ Passed: {results['passed']}")
    print(f"❌ Failed: {results['failed']}")
    print(f"⏭️  Skipped: {results['skipped']}")
    
    if results['failed'] > 0:
        print("\nFailed notebooks:")
        for detail in results['details']:
            if detail['status'] == 'FAILED':
                print(f"  - {detail['description']}: {detail['notebook']}")
                print(f"    Error: {detail.get('error', 'Unknown error')}")
    
    return 0 if results['failed'] == 0 else 1

if __name__ == '__main__':
    sys.exit(main())

