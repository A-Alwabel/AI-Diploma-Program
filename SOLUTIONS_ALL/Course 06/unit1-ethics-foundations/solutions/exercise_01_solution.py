"""
Unit 1: Foundations of AI Ethics
Exercise 1 Solution: Ethical Framework Application
أسس أخلاقيات الذكاء الاصطناعي - حل التمرين 1: تطبيق الإطار الأخلاقي

This is the solution to Exercise 1.
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)

# ============================================================================
# SOLUTION: TASK 1 - Identify Ethical Issues
# الحل: المهمة 1 - تحديد القضايا الأخلاقية
# ============================================================================

def identify_ethical_issues():
    """Identify ethical issues in employee monitoring scenario"""
    ethical_issues = [
        {
            'issue': 'Privacy Violation',
            'issue_ar': 'انتهاك الخصوصية',
            'severity': 9,
            'description': 'Monitoring computer usage, emails, and keystrokes violates employee privacy',
            'description_ar': 'مراقبة استخدام الكمبيوتر والبريد الإلكتروني والضغط على المفاتيح تنتهك خصوصية الموظف'
        },
        {
            'issue': 'Lack of Consent',
            'issue_ar': 'عدم الموافقة',
            'severity': 8,
            'description': 'Employees may not be aware of or consent to this level of monitoring',
            'description_ar': 'قد لا يكون الموظفون على علم أو يوافقون على هذا المستوى من المراقبة'
        },
        {
            'issue': 'Autonomy and Dignity',
            'issue_ar': 'الاستقلالية والكرامة',
            'severity': 8,
            'description': 'Constant monitoring undermines employee autonomy and human dignity',
            'description_ar': 'المراقبة المستمرة تقوض استقلالية الموظف والكرامة الإنسانية'
        },
        {
            'issue': 'Potential for Discrimination',
            'issue_ar': 'إمكانية التمييز',
            'severity': 7,
            'description': 'Productivity metrics may be biased against certain work styles or disabilities',
            'description_ar': 'قد تكون مقاييس الإنتاجية متحيزة ضد أنماط عمل معينة أو الإعاقات'
        },
        {
            'issue': 'Lack of Transparency',
            'issue_ar': 'عدم الشفافية',
            'severity': 7,
            'description': 'Employees may not know how their data is being used or evaluated',
            'description_ar': 'قد لا يعرف الموظفون كيف يتم استخدام أو تقييم بياناتهم'
        }
    ]
    return ethical_issues

# ============================================================================
# SOLUTION: TASK 2 - Apply Ethical Frameworks
# الحل: المهمة 2 - تطبيق الأطر الأخلاقية
# ============================================================================

def apply_utilitarianism():
    """Utilitarian analysis"""
    analysis = {
        'benefits': [
            'Increased productivity for company',
            'Better performance management',
            'Cost savings through efficiency',
            'Data-driven decision making'
        ],
        'harms': [
            'Employee stress and anxiety',
            'Loss of privacy',
            'Reduced trust and morale',
            'Potential for discrimination',
            'Invasion of personal space'
        ],
        'overall_utility': -2,  # Harms outweigh benefits
        'conclusion': 'Unethical - The harms to employees (stress, privacy loss, dignity) outweigh the benefits to the company. The overall utility is negative.',
        'conclusion_ar': 'غير أخلاقي - الأضرار التي تلحق بالموظفين (الإجهاد، فقدان الخصوصية، الكرامة) تفوق الفوائد للشركة. المنفعة الإجمالية سلبية.'
    }
    return analysis

def apply_deontology():
    """Deontological analysis"""
    analysis = {
        'moral_rules': [
            'Respect for human dignity',
            'Right to privacy',
            'Informed consent',
            'Treat people as ends, not means',
            'Fair treatment and non-discrimination'
        ],
        'violations': [
            'Violates right to privacy without consent',
            'Uses employees as means to company ends',
            'Lacks informed consent',
            'May violate fair treatment if biased'
        ],
        'conclusion': 'Unethical - Violates multiple moral duties including respect for privacy, dignity, and informed consent. The system treats employees as means rather than ends.',
        'conclusion_ar': 'غير أخلاقي - ينتهك واجبات أخلاقية متعددة بما في ذلك احترام الخصوصية والكرامة والموافقة المستنيرة. النظام يعامل الموظفين كوسائل وليس كغايات.'
    }
    return analysis

def apply_rights_based():
    """Rights-based analysis"""
    analysis = {
        'rights_at_stake': [
            'Right to privacy',
            'Right to autonomy',
            'Right to dignity',
            'Right to informed consent',
            'Right to fair treatment',
            'Right to work-life balance'
        ],
        'violations': [
            'Severe violation of privacy rights',
            'Violation of autonomy and dignity',
            'Lack of informed consent',
            'Potential violation of fair treatment if biased'
        ],
        'conclusion': 'Unethical - Violates fundamental human rights including privacy, autonomy, and dignity. The system cannot be justified from a rights-based perspective.',
        'conclusion_ar': 'غير أخلاقي - ينتهك حقوق الإنسان الأساسية بما في ذلك الخصوصية والاستقلالية والكرامة. لا يمكن تبرير النظام من منظور قائم على الحقوق.'
    }
    return analysis

# ============================================================================
# SOLUTION: TASK 3 - Identify Stakeholders
# الحل: المهمة 3 - تحديد أصحاب المصلحة
# ============================================================================

def identify_stakeholders():
    """Identify all stakeholders"""
    stakeholders = {
        'Employees': {
            'interests': ['Privacy', 'Autonomy', 'Fair treatment', 'Job security'],
            'interests_ar': ['الخصوصية', 'الاستقلالية', 'المعاملة العادلة', 'أمان الوظيفة'],
            'impact': 9,  # Highly affected
            'influence': 5  # Moderate influence
        },
        'Company Management': {
            'interests': ['Productivity', 'Cost efficiency', 'Performance metrics'],
            'interests_ar': ['الإنتاجية', 'كفاءة التكلفة', 'مقاييس الأداء'],
            'impact': 6,  # Moderately affected
            'influence': 9  # High influence
        },
        'HR Department': {
            'interests': ['Performance management', 'Compliance', 'Employee relations'],
            'interests_ar': ['إدارة الأداء', 'الامتثال', 'علاقات الموظفين'],
            'impact': 7,
            'influence': 7
        },
        'AI Developers': {
            'interests': ['Technical success', 'Innovation', 'Ethical development'],
            'interests_ar': ['النجاح التقني', 'الابتكار', 'التطوير الأخلاقي'],
            'impact': 5,
            'influence': 8
        },
        'Unions/Labor Organizations': {
            'interests': ['Worker rights', 'Privacy protection', 'Fair treatment'],
            'interests_ar': ['حقوق العمال', 'حماية الخصوصية', 'المعاملة العادلة'],
            'impact': 8,
            'influence': 6
        },
        'Regulators': {
            'interests': ['Compliance', 'Privacy laws', 'Labor rights'],
            'interests_ar': ['الامتثال', 'قوانين الخصوصية', 'حقوق العمل'],
            'impact': 4,
            'influence': 9
        }
    }
    return stakeholders

# ============================================================================
# SOLUTION: TASK 4 - Recommendations
# الحل: المهمة 4 - التوصيات
# ============================================================================

def provide_recommendations():
    """Provide ethical recommendations"""
    recommendations = [
        {
            'recommendation': 'Obtain explicit, informed consent from all employees',
            'recommendation_ar': 'الحصول على موافقة صريحة ومستنيرة من جميع الموظفين',
            'priority': 'High'
        },
        {
            'recommendation': 'Limit monitoring to work-related activities only',
            'recommendation_ar': 'تقييد المراقبة على الأنشطة المتعلقة بالعمل فقط',
            'priority': 'High'
        },
        {
            'recommendation': 'Ensure transparency about what is monitored and how data is used',
            'recommendation_ar': 'ضمان الشفافية حول ما يتم مراقبته وكيفية استخدام البيانات',
            'priority': 'High'
        },
        {
            'recommendation': 'Implement privacy-preserving techniques (e.g., aggregate data only)',
            'recommendation_ar': 'تنفيذ تقنيات الحفاظ على الخصوصية (مثل تجميع البيانات فقط)',
            'priority': 'Medium'
        },
        {
            'recommendation': 'Regular audits for bias and discrimination',
            'recommendation_ar': 'عمليات تدقيق منتظمة للتحيز والتمييز',
            'priority': 'High'
        },
        {
            'recommendation': 'Provide opt-out mechanisms for employees',
            'recommendation_ar': 'توفير آليات للانسحاب للموظفين',
            'priority': 'Medium'
        },
        {
            'recommendation': 'Establish clear accountability and redress mechanisms',
            'recommendation_ar': 'إنشاء آليات واضحة للمساءلة والإنصاف',
            'priority': 'High'
        }
    ]
    return recommendations

# ============================================================================
# SOLUTION: TASK 5 - Visualizations
# الحل: المهمة 5 - التصورات
# ============================================================================

def create_stakeholder_matrix(stakeholders):
    """Create stakeholder impact/influence matrix"""
    names = list(stakeholders.keys())
    impacts = [s['impact'] for s in stakeholders.values()]
    influences = [s['influence'] for s in stakeholders.values()]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    scatter = ax.scatter(influences, impacts, s=200, alpha=0.6, 
                        c=range(len(names)), cmap='viridis', edgecolors='black', linewidth=2)
    
    for i, name in enumerate(names):
        ax.annotate(name, (influences[i], impacts[i]), 
                   xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    ax.set_xlabel('Influence Level (1-10) / مستوى التأثير (1-10)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Impact Level (1-10) / مستوى التأثير (1-10)', fontsize=12, fontweight='bold')
    ax.set_title('Stakeholder Impact-Influence Matrix\n'
                'مصفوفة التأثير-التأثير لأصحاب المصلحة',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('unit1-ethics-foundations/solutions/stakeholder_matrix.png',
                dpi=300, bbox_inches='tight')
    print("✅ Saved: stakeholder_matrix.png")
    plt.close()

def create_ethical_issues_chart(ethical_issues):
    """Create ethical issues severity chart"""
    issues = [e['issue'] for e in ethical_issues]
    severities = [e['severity'] for e in ethical_issues]
    colors = ['#e74c3c' if s >= 9 else '#f39c12' if s >= 7 else '#3498db' 
              for s in severities]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    bars = ax.barh(issues, severities, color=colors, alpha=0.8, 
                   edgecolor='black', linewidth=1.5)
    
    ax.set_xlabel('Severity Score (1-10) / درجة الشدة (1-10)', fontsize=12, fontweight='bold')
    ax.set_title('Ethical Issues Severity Analysis\n'
                'تحليل شدة القضايا الأخلاقية',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 10)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    for i, (bar, severity) in enumerate(zip(bars, severities)):
        ax.text(severity + 0.2, i, f'{severity}/10', 
               va='center', fontweight='bold', fontsize=11)
    
    # Legend
    high = mpatches.Patch(color='#e74c3c', label='High (9-10) / عالي')
    medium = mpatches.Patch(color='#f39c12', label='Medium (7-8) / متوسط')
    low = mpatches.Patch(color='#3498db', label='Low (<7) / منخفض')
    ax.legend(handles=[high, medium, low], loc='lower right', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('unit1-ethics-foundations/solutions/ethical_issues_severity.png',
                dpi=300, bbox_inches='tight')
    print("✅ Saved: ethical_issues_severity.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# التنفيذ الرئيسي
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 1 - Exercise 1 Solution")
    print("الوحدة 1 - حل التمرين 1")
    print("="*80)
    
    # Task 1
    print("\n📋 TASK 1: Ethical Issues")
    print("-" * 60)
    ethical_issues = identify_ethical_issues()
    for issue in ethical_issues:
        print(f"\n{issue['issue']} / {issue['issue_ar']}")
        print(f"  Severity: {issue['severity']}/10")
        print(f"  {issue['description']}")
    
    # Task 2
    print("\n\n📋 TASK 2: Framework Analysis")
    print("-" * 60)
    print("\nUtilitarianism:")
    util = apply_utilitarianism()
    print(f"  Overall Utility: {util['overall_utility']}")
    print(f"  Conclusion: {util['conclusion']}")
    
    print("\nDeontology:")
    deon = apply_deontology()
    print(f"  Conclusion: {deon['conclusion']}")
    
    print("\nRights-Based:")
    rights = apply_rights_based()
    print(f"  Conclusion: {rights['conclusion']}")
    
    # Task 3
    print("\n\n📋 TASK 3: Stakeholders")
    print("-" * 60)
    stakeholders = identify_stakeholders()
    for name, info in stakeholders.items():
        print(f"\n{name}:")
        print(f"  Impact: {info['impact']}/10, Influence: {info['influence']}/10")
        print(f"  Interests: {', '.join(info['interests'])}")
    
    # Task 4
    print("\n\n📋 TASK 4: Recommendations")
    print("-" * 60)
    recommendations = provide_recommendations()
    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. [{rec['priority']}] {rec['recommendation']}")
        print(f"   {rec['recommendation_ar']}")
    
    # Task 5
    print("\n\n📋 TASK 5: Creating Visualizations")
    print("-" * 60)
    create_stakeholder_matrix(stakeholders)
    create_ethical_issues_chart(ethical_issues)
    
    print("\n" + "="*80)
    print("✅ Solution completed successfully!")
    print("✅ اكتمل الحل بنجاح!")
    print("="*80)

