# Quiz 04: Neural Networks Basics | اختبار 4: أساسيات الشبكات العصبية
## AIAT 111 - Unit 4

**Time Limit:** 30 minutes | **الوقت المحدد:** 30 دقيقة  
**Total Points:** 100 points | **إجمالي النقاط:** 100 نقطة

---

## Part 1: Multiple Choice | الجزء 1: اختيار من متعدد
**(40 points | 40 نقطة)**

### Question 1 (10 points)
What is a perceptron?

أ) A type of graph  
ب) A single-layer neural network  
ج) A search algorithm  
د) A knowledge representation method


---

### Question 2 (10 points)
What does ReLU stand for?

أ) Rectified Linear Unit  
ب) Random Linear Unit  
ج) Recursive Linear Unit  
د) Regular Linear Unit


---

### Question 3 (10 points)
What is the purpose of an activation function?

أ) To add randomness  
ب) To introduce non-linearity  
ج) To reduce memory usage  
د) To speed up computation


---

### Question 4 (10 points)
A single perceptron can solve which type of problems?

أ) Only linear problems  
ب) Only non-linear problems  
ج) Both linear and non-linear  
د) No problems


---

## Part 2: Short Answer | الجزء 2: إجابة قصيرة
**(30 points | 30 نقطة)**

### Question 5 (15 points)
Explain the difference between a perceptron and a multi-layer perceptron.

اشرح الفرق بين البيرسبترون والشبكة العصبية متعددة الطبقات.

---

### Question 6 (15 points)
What is forward propagation in a neural network?

ما هو الانتشار الأمامي في الشبكة العصبية؟

---

## Part 3: Code Writing | الجزء 3: كتابة الكود
**(30 points | 30 نقطة)**

### Question 7 (30 points)
Implement a simple perceptron that can classify AND gate inputs.

نفذ بيرسبترون بسيط يمكنه تصنيف مدخلات بوابة AND.


class Perceptron:
    def __init__(self):
        self.weights = np.zeros(2)
        self.bias = 0
    
    def activation(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, X):
        return [self.activation(np.dot(x, self.weights) + self.bias) for x in X]
```

---

**For:** AIAT 111 - Introduction to AI Applications and Concepts
