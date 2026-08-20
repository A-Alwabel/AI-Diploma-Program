# Quiz 02: Search Algorithms | اختبار 2: خوارزميات البحث
## AIAT 111 - Unit 2

**Time Limit:** 45 minutes | **الوقت المحدد:** 45 دقيقة  
**Total Points:** 100 points | **إجمالي النقاط:** 100 نقطة

---

## Part 1: Multiple Choice | الجزء 1: اختيار من متعدد
**(40 points | 40 نقطة)**

### Question 1 (10 points)
What data structure does BFS use?

أ) Stack  
ب) Queue  
ج) Priority Queue  
د) Hash Table


---

### Question 2 (10 points)
What is the main advantage of DFS over BFS?

أ) Always finds shortest path  
ب) Uses less memory  
ج) Faster execution  
د) More accurate


---

### Question 3 (10 points)
What makes A* algorithm optimal?

أ) It uses a stack  
ب) It uses heuristics  
ج) It always finds the shortest path  
د) It's faster than BFS


---

### Question 4 (10 points)
Which algorithm guarantees finding the shortest path in an unweighted graph?

أ) DFS  
ب) BFS  
ج) Both  
د) Neither


---

## Part 2: Short Answer | الجزء 2: إجابة قصيرة
**(30 points | 30 نقطة)**

### Question 5 (15 points)
Explain the difference between BFS and DFS. When would you use each?

اشرح الفرق بين BFS و DFS. متى تستخدم كل منهما؟

---

### Question 6 (15 points)
What is a heuristic function in A* algorithm? Give an example.

ما هي الدالة الاستدلالية في خوارزمية A*؟ أعط مثالاً.

---

## Part 3: Code Writing | الجزء 3: كتابة الكود
**(30 points | 30 نقطة)**

### Question 7 (30 points)
Implement a BFS function that finds the shortest path in a graph.

نفذ دالة BFS تجد أقصر مسار في رسم بياني.


def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None
```

---

> Answers and rubric: released by your instructor.
