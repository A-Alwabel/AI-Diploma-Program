# Quiz 03: Machine Learning Basics
## AIAT 111 - Unit 3

**Time Limit:** 30 minutes
**Total Points:** 100 points

Every question refers to a result printed by one of the Unit 3 notebooks (`unit3-ml-basics/examples/01` to `05`). You may reason from memory of those outputs; no notebook needs to be open.

---

## Part 1: Multiple Choice
**(40 points)**
### Question 1 (10 points)
In lesson 01 the California house-value model was scored with RMSE (0.8535, about $85,346 of typical error) and the newsgroup-post model with accuracy (0.9357). Why do the two models use different error measures?

A) The housing sample had 2,000 rows and the newsgroup test set had 793 posts, and RMSE becomes reliable at the larger of those two sample sizes  
B) The first model predicts a number, so its error has a size in dollars; the second predicts a label, so its error is a count of mistakes  
C) Accuracy could have scored both models if each predicted house value were rounded to the nearest $100,000 first  
D) RMSE is the number of test block groups the model priced incorrectly, written in dollar units  

---

### Question 2 (10 points)
Lesson 02 trained a network with one hidden layer on XOR (seed 2). It printed 50% accuracy, its outputs for the rows (0,0), (0,1), (1,0), (1,1) were 0, 0, 1, 1, and its loss moved by 0.00008 over the last 200 epochs. What does the lesson conclude from this run?

A) The hidden layer did not give the network enough capacity to represent XOR, so it failed for the same reason the single perceptron fails  
B) Training was cut off too early, and running more epochs from this point would have reached 100%  
C) The network could represent XOR, but gradient descent from this starting point settled on a straight line, the value of the first input  
D) The learning rate of 0.1 was too small for the weights to leave their initial values  

---

### Question 3 (10 points)
Lesson 03 trained the Keras network for 1000 epochs and printed `Final loss: 0.1663` and `Final accuracy: 1.0000`. The figure showed accuracy reaching 1.0000 at epoch 110 and staying there. What happened during the remaining 890 epochs?

A) The loss kept falling as the four outputs moved from just past 0.5 toward 0 and 1, a change accuracy cannot register  
B) Nothing changed after epoch 110, because once every row sat on the correct side of 0.5 the gradient was zero and the weights stopped moving  
C) The network began to overfit the four rows, which is why the loss did not reach zero  
D) Keras kept training because its default stopping rule waits for the loss to reach exactly zero  

---

### Question 4 (10 points)
Lesson 04 ran the same gradient-descent loop three times on the diabetes data, changing only the learning rate: 0.001 ended at MSE 15,197.31 after 200 steps, 0.1 ended at 3,890.46, and 1.2 passed a loss of 10^12 after 26 steps. What went wrong in the 1.2 run?

A) It reached the 200-step limit while the loss was still falling, so it simply needed more steps  
B) The gradient pointed uphill because the BMI feature had not been standardised  
C) The loss settled on the unexplained variation that BMI alone cannot account for, the same floor the 0.1 run had reached  
D) Each update overshot the minimum by more than the one before, so the error flipped sign every step and grew  

---

## Part 2: Short Answer
**(30 points)**
### Question 5 (15 points)
Lesson 05's random forest scored 0.958 test accuracy and gave P(malignant) = 1.00 for test patient 1. Two outputs followed: a ranking of all 30 features by mean |SHAP value| over the 143 test patients (worst area first, at 0.074), and LIME's rule `worst area > 1034.25` (+0.157) for that one patient. Explain the difference between a global and a local explanation, say which of the two outputs is which, and name one thing that neither output can tell the doctor.

---

### Question 6 (15 points)
In lesson 04 one gradient-descent loop trained two different models: MSE fell from 29,074.48 to 3,890.46 on the diabetes line fit, and binary cross-entropy fell from 0.6931 to 0.2560 on the biopsy classifier. Explain why the loss function had to change between the two tasks, and why the classifier's loss started at exactly 0.6931.

---

## Part 3: Code Writing
**(30 points)**
### Question 7 (30 points)
Lesson 04 fitted the line `y_pred = w * x + b` to 442 standardised BMI values by hand. Write, in NumPy:

1. `mse_loss(w, b, x, y)` — returns the mean squared error of that line.
2. `mse_gradients(w, b, x, y)` — returns the partial derivatives of the MSE with respect to `w` and `b`.
3. A loop that starts from `w = 0, b = 0`, takes 100 steps with learning rate 0.1, and prints the loss every 20 steps.

Finish with one comment line stating what the printed losses would do if the learning rate were 1.2 instead, and why.

---

> Answers and rubric: released by your instructor.
