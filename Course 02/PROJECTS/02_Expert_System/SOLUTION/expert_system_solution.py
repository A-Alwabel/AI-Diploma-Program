"""
Expert System - Complete Solution
Rule-based reasoning system with forward and backward chaining
"""

import networkx as nx
from typing import List, Set, Tuple

class Rule:
    """Represents a rule in the expert system."""
    
    def __init__(self, conditions: List[str], conclusion: str):
        """
        Initialize rule.
        
        Args:
            conditions: List of facts that must be true
            conclusion: Fact that becomes true if conditions are met
        """
        self.conditions = set(conditions)
        self.conclusion = conclusion
    
    def is_applicable(self, facts: Set[str]) -> bool:
        """Check if rule can be applied given current facts."""
        return self.conditions.issubset(facts)
    
    def __repr__(self):
        return f"Rule({list(self.conditions)} -> {self.conclusion})"

class KnowledgeBase:
    """Represents the knowledge base."""
    
    def __init__(self):
        """Initialize knowledge base."""
        self.graph = nx.DiGraph()
        self.facts = set()
        self.rules = []
    
    def add_fact(self, fact: str):
        """Add a fact to the knowledge base."""
        self.facts.add(fact)
        if not self.graph.has_node(fact):
            self.graph.add_node(fact, type='fact')
    
    def add_entity(self, entity: str, entity_type: str):
        """Add an entity to the knowledge graph."""
        self.graph.add_node(entity, type=entity_type)
    
    def add_relationship(self, entity1: str, entity2: str, relation: str):
        """Add a relationship between entities."""
        self.graph.add_edge(entity1, entity2, relation=relation)
    
    def add_rule(self, rule: Rule):
        """Add a rule to the knowledge base."""
        self.rules.append(rule)
        # Add to graph
        for condition in rule.conditions:
            if not self.graph.has_node(condition):
                self.graph.add_node(condition, type='fact')
        if not self.graph.has_node(rule.conclusion):
            self.graph.add_node(rule.conclusion, type='fact')
        # Add edges from conditions to conclusion
        for condition in rule.conditions:
            self.graph.add_edge(condition, rule.conclusion, relation='implies')

def forward_chaining(kb: KnowledgeBase, initial_facts: Set[str]) -> Set[str]:
    """
    Forward chaining reasoning.
    
    Args:
        kb: Knowledge base
        initial_facts: Starting facts
    
    Returns:
        All derived facts
    """
    facts = initial_facts.copy()
    new_facts = True
    
    while new_facts:
        new_facts = False
        for rule in kb.rules:
            if rule.is_applicable(facts) and rule.conclusion not in facts:
                facts.add(rule.conclusion)
                new_facts = True
                print(f"  Applied rule: {rule}")
                print(f"  New fact: {rule.conclusion}")
    
    return facts

def backward_chaining(kb: KnowledgeBase, goal: str, facts: Set[str] = None) -> bool:
    """
    Backward chaining reasoning.
    
    Args:
        kb: Knowledge base
        goal: Goal to prove
        facts: Known facts (optional)
    
    Returns:
        True if goal can be achieved
    """
    if facts is None:
        facts = kb.facts.copy()
    
    if goal in facts:
        return True
    
    # Find rules that can achieve goal
    applicable_rules = [r for r in kb.rules if r.conclusion == goal]
    
    for rule in applicable_rules:
        # Check if all conditions can be achieved
        can_achieve = True
        for condition in rule.conditions:
            if condition not in facts:
                # Try to achieve condition recursively
                if not backward_chaining(kb, condition, facts):
                    can_achieve = False
                    break
        
        if can_achieve:
            return True
    
    return False

class ExpertSystem:
    """Main expert system class."""
    
    def __init__(self, kb: KnowledgeBase):
        """Initialize expert system with knowledge base."""
        self.kb = kb
    
    def query(self, question: str) -> str:
        """
        Answer a question using the knowledge base.
        
        Args:
            question: Question to answer
        
        Returns:
            Answer string
        """
        # Simple question parsing
        question_lower = question.lower()
        
        if "is" in question_lower or "can" in question_lower:
            # Extract goal from question
            words = question.split()
            goal = None
            for i, word in enumerate(words):
                if word.lower() in ["is", "can"] and i + 1 < len(words):
                    goal = words[i + 1]
                    break
            
            if goal:
                result = backward_chaining(self.kb, goal)
                return f"Yes, {goal} is true." if result else f"No, {goal} cannot be proven."
        
        # Use forward chaining for general queries
        derived = forward_chaining(self.kb, self.kb.facts)
        return f"Based on current knowledge: {', '.join(sorted(derived))}"

def create_medical_expert_system():
    """Create a medical diagnosis expert system example."""
    kb = KnowledgeBase()
    
    # Add entities
    kb.add_entity("Patient", "person")
    kb.add_entity("Fever", "symptom")
    kb.add_entity("Cough", "symptom")
    kb.add_entity("Flu", "disease")
    kb.add_entity("Cold", "disease")
    
    # Add rules
    kb.add_rule(Rule(["high_fever", "cough"], "flu"))
    kb.add_rule(Rule(["mild_fever", "cough"], "cold"))
    kb.add_rule(Rule(["flu"], "rest_needed"))
    kb.add_rule(Rule(["cold"], "rest_needed"))
    
    return kb

def main():
    """Main function to run expert system."""
    print("Expert System - Complete Solution")
    print("=" * 60)
    
    # Create knowledge base
    kb = create_medical_expert_system()
    
    # Add initial facts
    print("\nAdding initial facts...")
    kb.add_fact("high_fever")
    kb.add_fact("cough")
    print(f"Initial facts: {kb.facts}")
    
    # Forward chaining
    print("\n" + "=" * 60)
    print("FORWARD CHAINING")
    print("=" * 60)
    derived_facts = forward_chaining(kb, kb.facts)
    print(f"\nAll derived facts: {derived_facts}")
    
    # Backward chaining
    print("\n" + "=" * 60)
    print("BACKWARD CHAINING")
    print("=" * 60)
    goal = "rest_needed"
    result = backward_chaining(kb, goal)
    print(f"\nCan we prove '{goal}'? {result}")
    
    # Expert system queries
    print("\n" + "=" * 60)
    print("EXPERT SYSTEM QUERIES")
    print("=" * 60)
    expert = ExpertSystem(kb)
    
    questions = [
        "Is rest needed?",
        "Can we prove flu?",
        "What do we know?"
    ]
    
    for question in questions:
        print(f"\nQ: {question}")
        answer = expert.query(question)
        print(f"A: {answer}")
    
    # Knowledge graph info
    print("\n" + "=" * 60)
    print("KNOWLEDGE GRAPH")
    print("=" * 60)
    print(f"Nodes: {kb.graph.number_of_nodes()}")
    print(f"Edges: {kb.graph.number_of_edges()}")
    print(f"\nGraph structure:")
    for node in kb.graph.nodes():
        neighbors = list(kb.graph.successors(node))
        if neighbors:
            print(f"  {node} -> {neighbors}")

if __name__ == "__main__":
    main()
