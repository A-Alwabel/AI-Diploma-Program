# Project 02: Expert System

## Overview

Build a simple expert system that uses knowledge representation and rule-based reasoning to answer questions or make recommendations.

**Learning Objectives:**
- Implement knowledge graphs
- Create rule-based reasoning system
- Use forward/backward chaining
- Build an interactive expert system

---

## Requirements

### Functional Requirements
1. **Knowledge Base**
   - Create knowledge graph with entities and relationships
   - Define rules (IF-THEN statements)
   - Store facts about domain

2. **Reasoning Engine**
   - Implement forward chaining
   - Implement backward chaining
   - Handle uncertainty (optional)

3. **User Interface**
   - Allow user to input facts
   - Ask questions
   - Display reasoning process
   - Show conclusions

4. **Domain Selection**
   - Choose a domain (medical diagnosis, troubleshooting, recommendations, etc.)
   - Create relevant knowledge base
   - Define appropriate rules

### Technical Requirements
- Use Python 3.9+
- Use NetworkX for knowledge graphs
- Use Python classes for rule representation
- Code should be well-commented
- Include error handling

---

## Deliverables

1. **Source Code**
   - `knowledge_base.py` - Knowledge representation
   - `reasoning_engine.py` - Forward/backward chaining
   - `expert_system.py` - Main system
   - `interface.py` - User interface
   - `main.py` - Main program

2. **Documentation**
   - README.md explaining domain and usage
   - Knowledge base documentation
   - Rule documentation
   - User guide

3. **Demo**
   - Working demonstration
   - Example queries and responses

---

## Project Structure

```
project_02_expert_system/
├── knowledge_base.py
├── reasoning_engine.py
├── expert_system.py
├── interface.py
├── main.py
├── README.md
└── requirements.txt
```

---

## Example Domain: Medical Diagnosis

**Entities:**
- Symptoms: fever, cough, headache
- Diseases: flu, cold, migraine
- Treatments: rest, medicine

**Relationships:**
- fever → indicates → flu
- cough → indicates → cold

**Rules:**
- IF fever AND cough THEN likely flu
- IF headache AND no_fever THEN likely migraine

---

## Evaluation Criteria

See `../../ASSESSMENTS/Project_Rubric.md` for detailed rubric.

**Key Areas:**
- Knowledge base quality (30%)
- Reasoning correctness (30%)
- Code quality (20%)
- Documentation (10%)
- Creativity (10%)

---

## Bonus Features

- [ ] Handle uncertainty/probabilities
- [ ] Visualize knowledge graph
- [ ] Explain reasoning steps
- [ ] Learn from user feedback
- [ ] Multiple domains

---

## Resources

- Notebook 02: Knowledge Representation
- NetworkX documentation
- Expert systems theory

---

## Submission

Submit:
1. All source code files
2. README.md with domain description
3. Knowledge base documentation
4. Demo or screenshots

**Due Date:** [Set by instructor]

---

**Created**: 2025  
**For**: Python for AI Course - 112 AIAT
