# Retrieval Quiz — Week 30

**Week 30 of 35 · Course 11 — AIAT 125 (Deploying AI Models)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

You have a trained scikit-learn model. It must be called from a Java backend service and must also run inside a mobile app that hosts no Python interpreter. Which packaging choice makes that possible?

A) `pickle`, because Python runs on all the major operating systems  
B) `joblib` with `compress=3`, because it produces the smallest artifact of the four  
C) ONNX, because the graph runs in an ONNX runtime with no Python present  
D) JSON of the learned parameters, because most languages parse JSON  

---

### Question 2

Unit 1 put a model behind an HTTP endpoint instead of importing it into the calling program. What is the main advantage of a REST API for model serving?

A) A standardized, language-neutral interface that scales out  
B) Lower latency than an in-process `model.predict()` call  
C) Automatic validation of requests against the model's schema  
D) Automatic scaling of the service as request volume grows  

---

### Question 3

Unit 3 compared cloud hosting tiers for a model endpoint. When is **serverless** compute (AWS Lambda, GCP Cloud Run) the right choice?

A) When each request needs a GPU, since the platform attaches one for the call  
B) When traffic is low or unpredictable and you would rather pay per request than run a server  
C) When the response budget is 10 ms, since scaling to zero removes queueing between requests  
D) When peak throughput matters most, because a managed runtime outruns a container you built yourself  

---

### Question 4

Unit 5 ran a model-free and a model-based agent on FrozenLake over **20 seeds × 300 episodes**, with the same learning rule, the same discount and the same epsilon = 0.2. The sole difference: after each real environment step the model-based agent also replays 20 remembered transitions.

```
  Success rate after ...   | model-free | model-based
  50 episodes              |      0.020 |      0.332
  100 episodes             |      0.217 |      0.584
  the last 50 episodes     |      0.747 |      0.746
```

The model-based agent did about **20× more Q-updates** for the same environment experience. What do these numbers support?

A) The model-based agent had 20× more experience of the environment, so its early lead at 50 and 100 episodes is what you would expect  
B) The model-based agent is more sample-efficient — it reaches a given success rate in fewer environment steps — but it does not end higher  
C) The model-based agent is the better choice when compute is the scarce resource, because it extracts more learning per unit of computation  
D) The 300-episode budget is too short to separate the two: with more episodes the model-based agent's early lead would reappear as a higher final rate  

---

### Question 5

Unit 3's DQN stored each transition in a buffer and trained on random minibatches drawn from it, rather than on the transitions in the order they arrived. What problem does **experience replay** solve?

A) It removes the need for a separate target network, since sampled targets are already stable  
B) It lets the agent learn a useful policy from a single episode of experience  
C) It shortens each training step, because a buffered batch is read faster than a live one  
D) Consecutive transitions are highly correlated, and random sampling breaks that correlation  

---

### Question 6

Unit 4 trained one agent with epsilon fixed at 0.3 and another with epsilon starting at 1.0 and decaying toward 0.05. What does **epsilon decay** change about training?

A) Exploration is broad early and mostly gives way to exploitation as epsilon falls  
B) The update step shrinks over time, so late episodes disturb the learned values less  
C) The discount factor is reduced, so the agent gradually stops valuing distant rewards  
D) The replay buffer is trimmed as training proceeds, so stale transitions go  

---

### Question 7

Unit 4 ran gradient descent on `f(x) = x²` from `x = 5.0`, changing only the learning rate:

```
learning rate    x @ step 3    x @ step 25
0.01                 4.7060         3.0173
0.10                 2.5600         0.0189
0.95                -3.6450        -0.3589
1.10                -8.6400      -476.9810
```

A student concludes: *"a learning rate that overshoots the minimum will diverge."* Which row refutes that, and how?

A) lr = 0.01: it stays on one side of the minimum, so overshoot is not required in order to converge  
B) lr = 0.10: it reaches x = 0.019 without overshooting, so overshoot is what slows a run down  
C) lr = 1.10: its sign alternates, showing that overshoot and divergence are the same behaviour  
D) lr = 0.95: it lands beyond the minimum (x = −3.65 at step 3) and still closes in to |x| = 0.36  

---

### Question 8

What is the main difference between traditional, rule-based AI and modern, data-driven AI?

A) Traditional AI relies on neural networks, and modern AI on hand-written rules  
B) Traditional AI hides its reasoning, and modern AI is transparent by construction  
C) Traditional AI applies rules a person wrote, and modern AI fits its rules to data  
D) Traditional AI runs faster, and modern AI is slower because it does more arithmetic  

---

### Question 9

Unit 3's KNN lesson fits the same model twice on the same 313 real card transactions. Without scaling it scores accuracy **0.9048**; with `StandardScaler` it scores **0.9683**. The lesson also prints that the `Time` column alone contributes **99.9978%** of the raw squared distance between two transactions (`Time` std 46,331.2, against a median feature std of 1.302). What does that 99.9978% figure explain?

A) The V1–V28 columns barely vary across these rows, so they contribute almost nothing to the distances  
B) Unscaled, "nearest neighbour" means roughly "happened at a similar moment", so what V1–V28 know is drowned out  
C) `Time` is the most predictive feature of fraud here, so scaling it down discards the best signal the model has  
D) `StandardScaler` dropped `Time` from the feature set, and removing that dominant column is what lifted accuracy  

---

### Question 10

In the differential privacy lesson, the Laplace mechanism at **ε = 0.1** produced a mean absolute error of about **10** on a count of **212** patients (4.7% of the answer) and about **10** again on a count of **29** patients (34.2% of the answer). What does this tell you about deploying differential privacy?

A) The Laplace mechanism is unsuited to small groups, which should be protected with k-anonymity rather than added noise  
B) Lowering ε further would shrink the error on the small subgroup, because ε is the mechanism's accuracy setting  
C) Laplace noise scales with sensitivity and ε, not with the size of the true answer, so one ε costs small groups more  
D) The small subgroup has fewer records to average over, so collecting more data there would close the gap  

---
