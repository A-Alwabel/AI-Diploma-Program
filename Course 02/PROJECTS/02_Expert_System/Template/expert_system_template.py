"""
Expert System Template
Project 02 Template

Fill in the functions marked with TODO comments.
"""

import networkx as nx

class Rule:
    """Represents a rule in the expert system."""
    
    def __init__(self, conditions, conclusion):
        """
        Initialize rule.
        
        Args:
            conditions: List of facts that must be true
            conclusion: Fact that becomes true if conditions are met
        """
        # TODO: Store conditions and conclusion
        self.conditions = None  # Replace with actual conditions
        self.conclusion = None  # Replace with actual conclusion
    
    def is_applicable(self, facts):
        """Check if rule can be applied given current facts."""
        # TODO: Return True if all conditions are in facts
        pass


class KnowledgeBase:
    """Represents the knowledge base."""
    
    def __init__(self):
        """Initialize knowledge base."""
        # TODO: Create NetworkX graph
        self.graph = None  # Replace with nx.DiGraph()
        self.facts = set()  # Current facts
        self.rules = []  # List of rules
    
    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        # TODO: Add fact to facts set
        pass
    
    def add_entity(self, entity, entity_type):
        """Add an entity to the knowledge graph."""
        # TODO: Add node to graph with type attribute
        pass
    
    def add_relationship(self, entity1, entity2, relation):
        """Add a relationship between entities."""
        # TODO: Add edge to graph with relation attribute
        pass
    
    def add_rule(self, rule):
        """Add a rule to the knowledge base."""
        # TODO: Add rule to rules list
        pass


def forward_chaining(kb, initial_facts):
    """
    Forward chaining reasoning.
    
    TODO: Implement forward chaining
    - Start with initial_facts
    - While new facts can be derived:
      - Find applicable rules
      - Add conclusions to facts
    - Return all derived facts
    """
    # TODO: Initialize with initial_facts
    # TODO: Main forward chaining loop
    # while new facts can be derived:
    #   for each rule:
    #     if rule is applicable:
    #       add conclusion to facts
    
    # TODO: Return all facts
    return set()


def backward_chaining(kb, goal):
    """
    Backward chaining reasoning.
    
    TODO: Implement backward chaining
    - Start with goal
    - Find rules that can achieve goal
    - Work backwards to find required facts
    - Return True if goal can be achieved
    """
    # TODO: If goal is already a fact, return True
    # TODO: Find rules with goal as conclusion
    # TODO: For each rule, recursively check if conditions can be achieved
    # TODO: Return True if goal can be achieved
    
    return False


class ExpertSystem:
    """Main expert system class."""
    
    def __init__(self, kb):
        """Initialize expert system with knowledge base."""
        self.kb = kb
    
    def query(self, question):
        """
        Answer a question using the knowledge base.
        
        TODO: Implement query processing
        - Parse question
        - Use forward or backward chaining
        - Return answer
        """
        # TODO: Parse question to extract goal/facts
        # TODO: Use reasoning engine
        # TODO: Return answer
        
        return "I don't know"


def main():
    """Main function to run expert system."""
    # Create knowledge base
    kb = KnowledgeBase()
    
    # TODO: Add entities to knowledge graph
    # TODO: Add relationships
    # TODO: Add rules
    
    # Create expert system
    expert = ExpertSystem(kb)
    
    # TODO: Get user input
    # TODO: Process query
    # TODO: Display result


if __name__ == "__main__":
    main()

