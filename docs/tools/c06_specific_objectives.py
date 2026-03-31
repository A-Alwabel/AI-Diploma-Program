#!/usr/bin/env python3
"""Replace generic learning objectives with specific ones in Course 06 notebooks."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
C06 = ROOT / "Course 06"

GENERIC = [
    "Understand the key concepts of this topic",
    "Apply the topic using Python code examples",
    "Practice with small, realistic datasets or scenarios",
]

SPECIFIC_OBJECTIVES = {
    "unit1-ethics-foundations/examples/01_ethical_frameworks.ipynb": [
        "Compare major ethical frameworks (consequentialist, deontological, virtue)",
        "Apply frameworks to AI use cases and dilemmas",
        "Reason about trade-offs in responsible AI",
    ],
    "unit1-ethics-foundations/examples/02_ethical_decision_making.ipynb": [
        "Use structured decision-making processes for AI ethics",
        "Identify stakeholders and weigh impacts",
        "Document and justify ethical choices",
    ],
    "unit1-ethics-foundations/examples/03_case_study_analysis.ipynb": [
        "Analyze real-world AI ethics failures and successes",
        "Extract lessons and preventive measures",
        "Link case studies to frameworks and principles",
    ],
    "unit2-bias-justice/examples/01_bias_detection.ipynb": [
        "Detect bias in datasets and model outputs",
        "Use metrics and visualizations to assess fairness",
        "Identify sources of discriminatory impact",
    ],
    "unit2-bias-justice/examples/02_bias_mitigation.ipynb": [
        "Apply pre-, in-, and post-processing mitigation techniques",
        "Compare fairness–accuracy trade-offs",
        "Evaluate mitigation effectiveness",
    ],
    "unit2-bias-justice/examples/03_fair_representation.ipynb": [
        "Assess representation and inclusion in data and design",
        "Address underrepresentation and stereotyping",
        "Promote equitable outcomes across groups",
    ],
    "unit2-bias-justice/examples/04_bias_case_studies.ipynb": [
        "Analyze bias incidents in real AI systems",
        "Extract root causes and remedies",
        "Connect case studies to detection and mitigation",
    ],
    "unit2-bias-justice/examples/05_fair_ai_development.ipynb": [
        "Integrate fairness into the ML lifecycle",
        "Use fairness-aware development practices",
        "Document and communicate fairness decisions",
    ],
    "unit3-privacy-security/examples/01_data_protection.ipynb": [
        "Apply data protection principles to AI workflows",
        "Identify and minimize privacy risks",
        "Handle sensitive data responsibly",
    ],
    "unit3-privacy-security/examples/02_privacy_technologies.ipynb": [
        "Use privacy-enhancing technologies (PETs)",
        "Compare techniques and their trade-offs",
        "Choose appropriate PETs for use cases",
    ],
    "unit3-privacy-security/examples/03_differential_privacy.ipynb": [
        "Apply differential privacy concepts and mechanisms",
        "Quantify and tune privacy–utility trade-offs",
        "Use DP in realistic ML settings",
    ],
    "unit3-privacy-security/examples/04_gdpr_compliance.ipynb": [
        "Map GDPR requirements to AI systems",
        "Implement compliance-oriented practices",
        "Address rights, consent, and data minimization",
    ],
    "unit3-privacy-security/examples/05_secure_development.ipynb": [
        "Apply secure development practices to AI",
        "Identify and mitigate security threats",
        "Harden ML pipelines and deployments",
    ],
    "unit4-transparency-accountability/examples/01_shap_explanations.ipynb": [
        "Use SHAP for model interpretability",
        "Interpret feature attributions and plots",
        "Communicate model behavior to stakeholders",
    ],
    "unit4-transparency-accountability/examples/02_lime_explanations.ipynb": [
        "Apply LIME for local interpretability",
        "Generate and interpret local explanations",
        "Compare LIME with other XAI methods",
    ],
    "unit4-transparency-accountability/examples/03_counterfactual_analysis.ipynb": [
        "Generate and use counterfactual explanations",
        "Support recourse and understanding of decisions",
        "Assess counterfactual quality and constraints",
    ],
    "unit4-transparency-accountability/examples/04_accountability_frameworks.ipynb": [
        "Apply accountability frameworks to AI systems",
        "Assign roles, governance, and redress",
        "Document and audit decision chains",
    ],
    "unit4-transparency-accountability/examples/05_hitl_approaches.ipynb": [
        "Design human-in-the-loop (HITL) workflows",
        "Balance automation and human oversight",
        "Implement and evaluate HITL patterns",
    ],
    "unit4-transparency-accountability/examples/06_transparency_tools.ipynb": [
        "Use transparency and interpretability tools",
        "Produce explanations and reports for stakeholders",
        "Integrate transparency into AI lifecycle",
    ],
    "unit5-governance-regulations/examples/01_global_regulations.ipynb": [
        "Compare global AI regulations and standards",
        "Map requirements to your systems",
        "Understand cross-jurisdiction implications",
    ],
    "unit5-governance-regulations/examples/02_industry_regulations.ipynb": [
        "Apply industry-specific AI regulations",
        "Address sectoral compliance (e.g. healthcare, finance)",
        "Align practices with relevant standards",
    ],
    "unit5-governance-regulations/examples/03_governance_frameworks.ipynb": [
        "Use governance frameworks for AI oversight",
        "Implement governance structures and processes",
        "Balance innovation and accountability",
    ],
    "unit5-governance-regulations/examples/04_legal_challenges.ipynb": [
        "Identify legal challenges in AI deployment",
        "Address liability, IP, and regulatory uncertainty",
        "Mitigate legal and reputational risks",
    ],
}


def fix_objectives(nb_path: Path, rel: str) -> bool:
    spec = SPECIFIC_OBJECTIVES.get(rel)
    if not spec:
        return False
    try:
        with open(nb_path, encoding="utf-8") as f:
            nb = json.load(f)
    except json.JSONDecodeError:
        return False
    changed = False
    for c in nb["cells"]:
        if c.get("cell_type") != "markdown":
            continue
        lines = c.get("source", [])
        if not isinstance(lines, list):
            continue
        src = "".join(lines)
        if "Understand the key concepts of this topic" not in src:
            continue
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if "- Understand the key concepts of this topic" in line:
                if new_lines and "By completing this notebook" not in new_lines[-1]:
                    new_lines.append("By completing this notebook, you will:\n")
                for s in spec:
                    new_lines.append(f"- {s}\n")
                i += 1
                while i < len(lines) and (
                    "- Apply the topic using Python code examples" in lines[i]
                    or "- Practice with small, realistic datasets or scenarios" in lines[i]
                ):
                    i += 1
                continue
            new_lines.append(line)
            i += 1
        if new_lines != lines:
            c["source"] = new_lines
            changed = True
        break
    if changed:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    return changed


def main():
    done = []
    for nb_path in sorted(C06.rglob("*.ipynb")):
        rel = nb_path.relative_to(C06).as_posix()
        if "DOCS" in rel or "PROJECTS" in rel:
            continue
        if fix_objectives(nb_path, rel):
            done.append(rel)
    print("Updated objectives:", len(done))
    for r in done:
        print(" ", r)


if __name__ == "__main__":
    main()
