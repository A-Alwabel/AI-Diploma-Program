# Quiz 02: Knowledge Representation | اختبار 02: تمثيل المعرفة

## Instructions | التعليمات
- **Time Limit**: 40 minutes
- **Total Points**: 100 points
- **Format**: Multiple choice, short answer, code completion
- **Allowed Resources**: None (closed book)

---

## Part 1: Knowledge Graphs (30 points)

### Question 1 (5 points)
What is a knowledge graph?
- A) A visualization tool
- B) A way to represent facts and relationships
- C) A database
- D) A search algorithm

**Answer: B**

### Question 2 (5 points)
In a knowledge graph, nodes represent:
- A) Relationships
- B) Entities or concepts
- C) Rules
- D) Facts

**Answer: B**

### Question 3 (5 points)
In a knowledge graph, edges represent:
- A) Entities
- B) Relationships between entities
- C) Rules
- D) Facts

**Answer: B**

### Question 4 (10 points)
Create a simple knowledge graph with 3 entities and 2 relationships. Draw it.

**Sample Answer:**
- Entities: Person (John), City (Riyadh), Country (Saudi Arabia)
- Relationships: John lives_in Riyadh, Riyadh located_in Saudi Arabia

### Question 5 (5 points)
Which library is commonly used for knowledge graphs in Python?
- A) NumPy
- B) Matplotlib
- C) NetworkX
- D) SciPy

**Answer: C**

---

## Part 2: Rule-Based Systems (25 points)

### Question 6 (5 points)
What is a rule in a rule-based system?
- A) A fact
- B) A condition-action pair (IF-THEN)
- C) A node
- D) An edge

**Answer: B**

### Question 7 (5 points)
Forward chaining:
- A) Starts from goals and works backward
- B) Starts from facts and applies rules forward
- C) Works randomly
- D) Doesn't use rules

**Answer: B**

### Question 8 (5 points)
Backward chaining:
- A) Starts from facts and applies rules forward
- B) Starts from goals and works backward
- C) Works randomly
- D) Doesn't use rules

**Answer: B**

### Question 9 (10 points)
Given the rules:
- IF it is raining THEN take umbrella
- IF it is cold THEN wear jacket

And the fact: "it is raining"
What can we conclude?

**Answer: "take umbrella"**

---

## Part 3: Semantic Networks (25 points)

### Question 10 (5 points)
What is a semantic network?
- A) A type of knowledge graph
- B) A way to represent concepts and their relationships
- C) A neural network
- D) A database

**Answer: B**

### Question 11 (5 points)
In semantic networks, inheritance means:
- A) Passing properties from parent to child
- B) Creating new nodes
- C) Deleting nodes
- D) Changing relationships

**Answer: A**

### Question 12 (10 points)
Draw a semantic network showing:
- Animal (parent)
- Dog (child of Animal)
- Cat (child of Animal)
- Has property: "has fur"

**Answer: Students should draw inheritance hierarchy**

### Question 13 (5 points)
What Python concept is similar to inheritance in semantic networks?
- A) Lists
- B) Classes and inheritance
- C) Functions
- D) Dictionaries

**Answer: B**

---

## Part 4: Python Implementation (20 points)

### Question 14 (10 points)
Complete the code to create a knowledge graph node:

```python
import networkx as nx
G = nx.Graph()
G.add_______("Person")
G.add_______("City")
G.add_______("Person", "City", relation="lives_in")
```

**Answer: `node`, `node`, `edge`**

### Question 15 (10 points)
Write code to represent a simple rule: "IF temperature > 30 THEN it is hot"

**Sample Answer:**
```python
def check_temperature(temp):
    if temp > 30:
        return "it is hot"
    return None
```

---

## Answer Key Summary

1. B - A way to represent facts and relationships
2. B - Entities or concepts
3. B - Relationships between entities
4. See sample answer
5. C - NetworkX
6. B - A condition-action pair (IF-THEN)
7. B - Starts from facts and applies rules forward
8. B - Starts from goals and works backward
9. "take umbrella"
10. B - A way to represent concepts and their relationships
11. A - Passing properties from parent to child
12. See answer description
13. B - Classes and inheritance
14. `node`, `node`, `edge`
15. See sample answer

---

## Grading Rubric

- **90-100 points**: Excellent understanding
- **80-89 points**: Good understanding
- **70-79 points**: Satisfactory understanding
- **60-69 points**: Needs improvement
- **Below 60**: Review required

---

**Created**: 2025  
**For**: Python for AI Course - 112 AIAT

