# Complete Project Guide: 02 Expert System

---

## 🎯 Real-World Application

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Expert Systems (Day 1)

**What is an Expert System?**
A system that mimics human expert decision-making:
- **Knowledge Base:** Stores facts and rules
- **Inference Engine:** Makes conclusions
- **Explanation System:** Explains decisions
- **User Interface:** Interacts with users

**Example:**
```
Problem: Computer won't start

Rules:
- IF no_power AND plugged_in THEN check_power_supply
- IF no_display AND power_on THEN check_graphics_card
- IF slow_performance THEN check_memory

Conclusion: Check power supply
Explanation: Computer has no power but is plugged in
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
expert_system/
├── knowledge_base.py
├── inference_engine.py
├── explanation.py
├── main.py
└── README.md
```

---

### Step 3: Create Knowledge Graph (Day 2)

**File: `knowledge_base.py`**

```python
class KnowledgeGraph:
    """Knowledge graph for expert system"""
    
    def __init__(self):
        self.facts = {}  # {fact: True/False}
        self.rules = []  # List of rules
        self.relationships = {}  # Graph structure
    
    def add_fact(self, fact, value=True):
        """Add a fact"""
        self.facts[fact] = value
    
    def add_rule(self, conditions, conclusion, confidence=1.0):
        """Add a rule: IF conditions THEN conclusion"""
        rule = {
            'if': conditions,
            'then': conclusion,
            'confidence': confidence
        }
        self.rules.append(rule)
    
    def add_relationship(self, entity1, relationship, entity2):
        """Add relationship in knowledge graph"""
        if entity1 not in self.relationships:
            self.relationships[entity1] = []
        self.relationships[entity1].append((relationship, entity2))
```

---

### Step 4: Implement Inference Engine (Day 3)

**File: `inference_engine.py`**

```python
class InferenceEngine:
    """Makes conclusions from knowledge"""
    
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.conclusions = []
    
    def forward_chaining(self):
        """Forward chaining inference"""
        changed = True
        
        while changed:
            changed = False
            
            for rule in self.kb.rules:
                conditions = rule['if']
                conclusion = rule['then']
                
                # Check if all conditions are met
                if all(self.kb.facts.get(c, False) for c in conditions):
                    # If conclusion not already known
                    if conclusion not in self.kb.facts:
                        self.kb.facts[conclusion] = True
                        self.conclusions.append(conclusion)
                        changed = True
        
        return self.conclusions
    
    def backward_chaining(self, goal):
        """Backward chaining - prove a goal"""
        if goal in self.kb.facts and self.kb.facts[goal]:
            return True
        
        # Find rules that can prove this goal
        for rule in self.kb.rules:
            if rule['then'] == goal:
                # Check if all conditions can be proven
                if all(self.backward_chaining(c) for c in rule['if']):
                    self.kb.facts[goal] = True
                    return True
        
        return False
```

---

### Step 5: Add Explanation (Day 4)

**File: `explanation.py`**

```python
class ExplanationSystem:
    """Explains expert system decisions"""
    
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
    
    def explain(self, conclusion):
        """Explain how conclusion was reached"""
        explanation = []
        
        # Find rule that led to conclusion
        for rule in self.kb.rules:
            if rule['then'] == conclusion:
                explanation.append(f"Rule: IF {rule['if']} THEN {conclusion}")
                explanation.append(f"Conditions met: {rule['if']}")
                explanation.append(f"Confidence: {rule['confidence']}")
                break
        
        return "\n".join(explanation)
```

---

### Step 6: Create Technical Support System (Day 5)

**File: `tech_support_system.py`**

```python
from knowledge_base import KnowledgeGraph
from inference_engine import InferenceEngine
from explanation import ExplanationSystem

class TechSupportSystem:
    """Technical support expert system"""
    
    def __init__(self):
        self.kb = KnowledgeGraph()
        self.setup_rules()
        self.engine = InferenceEngine(self.kb)
        self.explainer = ExplanationSystem(self.kb)
    
    def setup_rules(self):
        """Set up technical support rules"""
        # Hardware issues
        self.kb.add_rule(
            ['no_power', 'plugged_in'],
            'check_power_supply',
            0.9
        )
        
        # Software issues
        self.kb.add_rule(
            ['slow_performance', 'high_memory_usage'],
            'add_more_ram',
            0.8
        )
        
        # Network issues
        self.kb.add_rule(
            ['no_internet', 'wifi_connected'],
            'check_router',
            0.85
        )
    
    def diagnose(self, symptoms):
        """Diagnose problem from symptoms"""
        # Add symptoms as facts
        for symptom in symptoms:
            self.kb.add_fact(symptom)
        
        # Run inference
        conclusions = self.engine.forward_chaining()
        
        # Get explanations
        explanations = []
        for conclusion in conclusions:
            explanations.append(self.explainer.explain(conclusion))
        
        return {
            'diagnosis': conclusions,
            'explanations': explanations
        }
```

---

### Step 7: Create Main Program (Day 6)

**File: `main.py`**

```python
from tech_support_system import TechSupportSystem

def main():
    system = TechSupportSystem()
    
    print("=" * 50)
    print("Technical Support Expert System")
    print("=" * 50)
    
    # Example: User reports problem
    symptoms = [
        'no_power',
        'plugged_in'
    ]
    
    print(f"\nUser symptoms: {symptoms}")
    print("\nDiagnosing...")
    
    result = system.diagnose(symptoms)
    
    print("\n" + "=" * 50)
    print("Diagnosis Results:")
    print("=" * 50)
    print(f"Recommended actions: {result['diagnosis']}")
    print("\nExplanations:")
    for exp in result['explanations']:
        print(f"\n{exp}")

if __name__ == "__main__":
    main()
```

---

---