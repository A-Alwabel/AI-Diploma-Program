# Quiz 03: Knowledge Representation | اختبار 3: تمثيل المعرفة
## AIAT 111 - Unit 3

**Time Limit:** 30 minutes | **الوقت المحدد:** 30 دقيقة  
**Total Points:** 100 points | **إجمالي النقاط:** 100 نقطة

---

## Part 1: Multiple Choice | الجزء 1: اختيار من متعدد
**(40 points | 40 نقطة)**

### Question 1 (10 points)
What is a knowledge graph?

أ) A type of neural network  
ب) A way to represent relationships between entities  
ج) A search algorithm  
د) An activation function

**Answer:** ب

---

### Question 2 (10 points)
In a rule-based system, what does "IF-THEN" represent?

أ) A loop structure  
ب) A conditional rule  
ج) A data structure  
د) An algorithm

**Answer:** ب

---

### Question 3 (10 points)
What is forward chaining?

أ) Starting from facts and applying rules  
ب) Starting from goals and working backwards  
ج) A type of search algorithm  
د) A neural network training method

**Answer:** أ

---

### Question 4 (10 points)
Which is NOT a knowledge representation method?

أ) Semantic networks  
ب) Production rules  
ج) Binary search  
د) Frames

**Answer:** ج

---

## Part 2: Short Answer | الجزء 2: إجابة قصيرة
**(30 points | 30 نقطة)**

### Question 5 (15 points)
Explain what a knowledge base is and give an example.

اشرح ما هي قاعدة المعرفة وأعط مثالاً.

**Answer Key:**
- Knowledge base: Collection of facts and rules about a domain
- Example: Medical diagnosis system, expert system for troubleshooting

---

### Question 6 (15 points)
What are the main components of an expert system?

ما هي المكونات الرئيسية لنظام خبير؟

**Answer Key:**
- Knowledge base
- Inference engine
- User interface
- Explanation facility

---

## Part 3: Code Writing | الجزء 3: كتابة الكود
**(30 points | 30 نقطة)**

### Question 7 (30 points)
Create a simple knowledge graph for a family and write a function to find all siblings of a person.

أنشئ رسم بياني بسيط للمعرفة لعائلة واكتب دالة للعثور على جميع الأشقاء لشخص ما.

**Sample Answer:**
```python
family_graph = {
    'Ahmed': {'children': ['Sara', 'Omar']},
    'Fatima': {'children': ['Sara', 'Omar']},
    'Sara': {'siblings': ['Omar']},
    'Omar': {'siblings': ['Sara']}
}

def find_siblings(graph, person):
    return graph.get(person, {}).get('siblings', [])
```

---

**For:** AIAT 111 - Introduction to AI Applications and Concepts
