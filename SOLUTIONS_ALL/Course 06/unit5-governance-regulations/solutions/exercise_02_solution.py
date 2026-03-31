"""
Unit 5 - Exercise 2: Solution
"""

import pandas as pd
import numpy as np
from datetime import datetime

# Task 1: Risk Assessment
def assess_ai_risk(use_case, data_sensitivity, decision_impact, automation_level):
    # Risk scoring
    sensitivity_scores = {'Low': 1, 'Medium': 2, 'High': 3, 'Critical': 4}
    impact_scores = {'Low': 1, 'Medium': 2, 'High': 3, 'Critical': 4}
    automation_scores = {'Low': 1, 'Medium': 2, 'High': 3, 'Full': 4}
    
    total_score = (
        sensitivity_scores.get(data_sensitivity, 1) +
        impact_scores.get(decision_impact, 1) +
        automation_scores.get(automation_level, 1)
    )
    
    if total_score <= 4:
        risk_level = 'Low'
    elif total_score <= 7:
        risk_level = 'Medium'
    elif total_score <= 10:
        risk_level = 'High'
    else:
        risk_level = 'Critical'
    
    justification = f"Risk assessed based on data sensitivity ({data_sensitivity}), decision impact ({decision_impact}), and automation level ({automation_level})"
    
    return {
        'use_case': use_case,
        'risk_level': risk_level,
        'risk_score': total_score,
        'justification': justification
    }

def create_risk_matrix():
    risk_matrix = pd.DataFrame({
        'Use Case': ['Healthcare Diagnosis', 'Credit Scoring', 'Recommendation', 'Chatbot'],
        'Data Sensitivity': ['High', 'High', 'Medium', 'Low'],
        'Decision Impact': ['High', 'High', 'Low', 'Low'],
        'Automation Level': ['Medium', 'High', 'High', 'Full'],
        'Risk Level': ['High', 'High', 'Medium', 'Low']
    })
    return risk_matrix

# Task 2: Compliance Checklist
def create_gdpr_compliance_checklist():
    checklist = pd.DataFrame({
        'Requirement': [
            'Data Minimization',
            'Purpose Limitation',
            'Storage Limitation',
            'Right to Explanation',
            'Right to Access',
            'Right to Erasure',
            'Data Protection by Design',
            'Privacy Impact Assessment',
            'Consent Management',
            'Data Breach Notification'
        ],
        'Description': [
            'Collect only necessary data',
            'Use data only for stated purposes',
            'Retain data only as long as necessary',
            'Provide explanations for automated decisions',
            'Allow individuals to access their data',
            'Allow individuals to delete their data',
            'Build privacy into system design',
            'Conduct privacy impact assessments',
            'Obtain and manage consent',
            'Notify authorities of data breaches'
        ],
        'Status': ['Not Started'] * 10
    })
    return checklist

def check_compliance_status(checklist, system_info):
    # Simulate compliance check
    compliance_report = {
        'total_requirements': len(checklist),
        'compliant': 0,
        'non_compliant': 0,
        'details': []
    }
    
    for _, row in checklist.iterrows():
        # Simplified compliance check
        is_compliant = np.random.choice([True, False], p=[0.7, 0.3])
        if is_compliant:
            compliance_report['compliant'] += 1
        else:
            compliance_report['non_compliant'] += 1
        
        compliance_report['details'].append({
            'requirement': row['Requirement'],
            'compliant': is_compliant
        })
    
    compliance_report['compliance_rate'] = compliance_report['compliant'] / compliance_report['total_requirements']
    return compliance_report

# Task 3: Governance Framework
def design_governance_framework(organization_type='enterprise'):
    framework = {
        'organization_type': organization_type,
        'governance_structure': {
            'ethics_board': {
                'purpose': 'Oversight of AI ethics and compliance',
                'composition': 'Multi-stakeholder (technical, legal, ethics, business)',
                'responsibilities': [
                    'Review AI projects for ethical implications',
                    'Approve high-risk AI deployments',
                    'Monitor ongoing AI systems',
                    'Handle ethical concerns and appeals'
                ]
            },
            'ai_governance_office': {
                'purpose': 'Day-to-day governance operations',
                'responsibilities': [
                    'Maintain AI inventory',
                    'Conduct risk assessments',
                    'Ensure compliance',
                    'Provide training and guidance'
                ]
            }
        },
        'processes': [
            'Risk assessment for new AI projects',
            'Ethics review for high-risk systems',
            'Regular audits and monitoring',
            'Incident response procedures',
            'Stakeholder engagement'
        ],
        'policies': [
            'AI ethics policy',
            'Data governance policy',
            'Model development standards',
            'Deployment guidelines',
            'Monitoring and maintenance procedures'
        ]
    }
    return framework

def create_ai_ethics_board_structure():
    board_structure = {
        'composition': {
            'technical_experts': 2,
            'ethics_philosophers': 2,
            'legal_compliance': 1,
            'business_stakeholders': 2,
            'external_advisors': 1,
            'community_representatives': 1
        },
        'responsibilities': [
            'Review AI projects for ethical implications',
            'Approve high-risk AI deployments',
            'Monitor ongoing AI systems',
            'Handle ethical concerns',
            'Provide guidance on ethical dilemmas',
            'Conduct regular ethics audits'
        ],
        'review_process': [
            'Initial project proposal review',
            'Risk assessment evaluation',
            'Ethics impact analysis',
            'Stakeholder consultation',
            'Decision and approval',
            'Post-deployment monitoring'
        ],
        'meeting_frequency': 'Monthly (or as needed for urgent issues)'
    }
    return board_structure

# Task 4: Monitoring and Auditing
def design_monitoring_framework():
    framework = {
        'key_metrics': {
            'performance': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
            'fairness': ['Demographic Parity', 'Equalized Odds', 'Calibration'],
            'privacy': ['Data Access Logs', 'Privacy Violations', 'Anonymization Quality'],
            'security': ['Adversarial Attacks', 'Data Breaches', 'Model Integrity']
        },
        'monitoring_frequency': {
            'real_time': ['Security incidents', 'Data breaches'],
            'daily': ['Performance metrics', 'Error rates'],
            'weekly': ['Fairness metrics', 'Privacy compliance'],
            'monthly': ['Comprehensive audits', 'Stakeholder reports']
        },
        'alerting_thresholds': {
            'performance_drop': 0.05,  # 5% drop in accuracy
            'fairness_violation': 0.1,  # 10% difference in metrics
            'privacy_incident': 1,  # Any privacy incident
            'security_breach': 1  # Any security breach
        }
    }
    return framework

def create_audit_report(model_performance, fairness_metrics, privacy_compliance):
    audit_report = {
        'audit_date': datetime.now().strftime('%Y-%m-%d'),
        'model_performance': {
            'accuracy': model_performance.get('accuracy', 0),
            'status': 'Pass' if model_performance.get('accuracy', 0) > 0.8 else 'Fail'
        },
        'fairness_assessment': {
            'demographic_parity': fairness_metrics.get('demographic_parity', 0),
            'equalized_odds': fairness_metrics.get('equalized_odds', 0),
            'status': 'Pass' if fairness_metrics.get('demographic_parity', 1) < 0.1 else 'Review'
        },
        'privacy_compliance': {
            'gdpr_compliant': privacy_compliance.get('gdpr_compliant', False),
            'data_minimization': privacy_compliance.get('data_minimization', False),
            'status': 'Pass' if privacy_compliance.get('gdpr_compliant', False) else 'Fail'
        },
        'overall_status': 'Pass',  # Simplified
        'recommendations': [
            'Continue monitoring performance metrics',
            'Conduct quarterly fairness audits',
            'Review privacy compliance monthly'
        ]
    }
    return audit_report

if __name__ == "__main__":
    print("="*80)
    print("Unit 5 - Exercise 2: Solution")
    print("="*80)
    
    # Task 1
    print("\nTask 1: Risk Assessment")
    risk_assessment = assess_ai_risk(
        'Healthcare Diagnosis',
        'High',
        'High',
        'Medium'
    )
    print(risk_assessment)
    
    risk_matrix = create_risk_matrix()
    print("\nRisk Matrix:")
    print(risk_matrix)
    
    # Task 2
    print("\nTask 2: GDPR Compliance Checklist")
    checklist = create_gdpr_compliance_checklist()
    print(checklist.head())
    
    system_info = {'system_name': 'AI Diagnosis System'}
    compliance_status = check_compliance_status(checklist, system_info)
    print(f"\nCompliance Rate: {compliance_status['compliance_rate']:.2%}")
    
    # Task 3
    print("\nTask 3: Governance Framework")
    framework = design_governance_framework('enterprise')
    print(f"Organization Type: {framework['organization_type']}")
    print(f"Number of Processes: {len(framework['processes'])}")
    
    board_structure = create_ai_ethics_board_structure()
    print(f"\nEthics Board Total Members: {sum(board_structure['composition'].values())}")
    
    # Task 4
    print("\nTask 4: Monitoring Framework")
    monitoring_framework = design_monitoring_framework()
    print(f"Key Metrics Categories: {len(monitoring_framework['key_metrics'])}")
    
    audit_report = create_audit_report(
        {'accuracy': 0.85},
        {'demographic_parity': 0.05, 'equalized_odds': 0.08},
        {'gdpr_compliant': True, 'data_minimization': True}
    )
    print("\nAudit Report:")
    print(f"Overall Status: {audit_report['overall_status']}")
    print(f"Performance Status: {audit_report['model_performance']['status']}")
    
    print("\n" + "="*80)
    print("Solution Complete!")
    print("="*80)

