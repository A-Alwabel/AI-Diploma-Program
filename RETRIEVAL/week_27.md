# Cumulative Retrieval Quiz — Week 27

**Programme week 27 of 35 · Current course: Course 10 — AIAT 124 (Generative AI), Unit 1 / Unit 2**
**Placement: session 3 of the week (s107), in the closing block. Session 4 (s108) closes Unit 2 with its unit quiz, so the block moves back to s107.**

- **15 minutes**, taken **in class at the END of the session**. Not homework.
- **Not graded.** No mark from this paper reaches your course grade.
- Write your answers, then your instructor **works every correct answer aloud immediately afterwards**. Stay for it.
- Ten items. Three from what you are studying now, seven from courses you finished earlier. The earlier items carry their own context.

---

### 1. [Course 10 · Unit 1]
Unit 1 fits a generative model (Gaussian Naive Bayes) and a discriminative model (logistic regression) to the same two-class dataset. The generative model scores **97.2%** test accuracy; the discriminative model scores **96.1%**. Which conclusion do those two numbers support?

A) The 1.1-point gap shows generative models classify better, so prefer them whenever accuracy matters.
B) Logistic regression could generate new samples too, if its decision boundary were inverted into a data distribution.
C) Accuracy is not what separates the two families here — what separates them is that the generative model learns p(x) and can draw new samples from it.
D) The generative model was bound to win here: p(x|y) turns into a classifier by Bayes' rule, so it carries more information than a bare decision boundary.

---

### 2. [Course 10 · Unit 1]
You are training the GAN from Unit 1. After a few hundred steps the **discriminator's loss has fallen to nearly 0 and stays there**, while the generator's loss climbs. What is happening, and what does it mean for the generator?

A) Training has converged — a discriminator loss near zero is the equilibrium the adversarial game aims for.
B) The generator has mode-collapsed onto a single output, and a collapsed generator is what drives the discriminator's loss to zero over the following steps.
C) The discriminator has overfitted the real images; the standard fix is to lower the generator's learning rate until the two losses cross.
D) The discriminator has saturated — it wins on each batch — so the gradient that reaches G through D vanishes and the generator stops improving.

---

### 3. [Course 09 · Unit 5]
Course 09 Unit 5 introduces hierarchical RL (the options framework). Which difficulty is it aimed at?

A) Continuous action spaces, where the greedy max over actions can no longer be taken by enumerating them
B) Long-horizon tasks, where a flat policy has to chain hundreds of primitive steps to reach a reward
C) Coordination between several agents that share one environment
D) Sample efficiency, by replaying remembered transitions between real steps in the environment

---

### 4. [Course 08 · Unit 5]
A trained FP32 model is converted to INT8. The stored file falls from **5,597 to 4,557 bytes** and validation accuracy is unchanged at **0.840**. Which optimization technique is this, and what did it change?

A) Quantization — the number of **bits** used to store each weight value
B) Pruning — the number of **weights**, by zeroing the smallest
C) Distillation — the **architecture**, by training a smaller model to copy a larger one
D) ONNX export — the **file format**, so the model runs outside the framework that trained it

---

### 5. [Course 08 · Unit 4]
Course 08 Unit 4 trains a standard autoencoder and a variational autoencoder (VAE) on the same images. What does the VAE do that the plain autoencoder does not?

A) It compresses each input to a shorter code, which is what lets the decoder rebuild the image
B) It trains encoder and decoder as two networks competing against each other
C) It scores each input by how far its reconstruction sits from the original, and flags the gap
D) It encodes each input to a distribution and samples from that, so new points can be drawn

---

### 6. [Course 09 · Unit 1]
Course 09's value-iteration lesson runs a 3x3 grid world with **-1 for every ordinary step, +10 for entering the goal, -10 for entering the pit, and gamma = 0.90**. It prints this converged value table and the greedy policy read off it:

```
State values:              Greedy policy:
  4.58   6.20   8.00         →   →   ↓
  6.20   8.00  10.00         →   →   ↓
  P     10.00   G            P   →   G
```

The tile immediately **above the pit** holds **6.20** — a positive value, even though one of its four actions steps straight into the -10 pit. Which explanation is correct?

A) The pit's -10 is discounted once per sweep, so by the time the table converges 0.90 raised to the sweep count has shrunk it below -1.
B) The sweep skips terminal states, so `transition(3, "down")` returns no pit transition, leaving the -10 out of that tile's backup.
C) The backup keeps the maximum over four actions, and the best moves right: -1 + 0.90 x 8.00 = 6.20, so the pit shows in the arrow.
D) The backup averages the four action targets instead of maximising, and the three non-pit actions outweigh the single -10.

---

### 7. [Course 05 · Unit 5]
In Course 05 Unit 5 you measured pandas against Dask on the same 4.3 MB file. pandas ran the groupby in 0.0007 s against Dask's 0.0146 s, and pandas also won the whole job end to end: 0.01 s against 0.02 s. Given that measurement, what does a scaling tool such as Dask, PySpark or RAPIDS actually buy you?

A) Handling data that will not fit in one machine's memory, because the engine works over partitions instead of materialising the whole file
B) Reducing wall-clock time on a job whose data already fits in memory, because the partitions are scheduled in parallel across the available cores
C) Improving data quality, because an engine that partitions a file also validates and repairs the records as it reads them
D) Lowering total cost, because a cluster of small commodity machines comes out cheaper than one machine with more memory

---

### 8. [Course 05 · Unit 5]
In Course 05 Unit 5, `dd.read_csv` on the 4.3 MB sample returned in 0.003 s reporting 4 partitions of 1 MB each, and `df['Flow Duration'].mean()` then printed a `dask_expr` object instead of a number. It took a `.compute()` call to produce 15,409,254.17 — the same value pandas gave. What did Dask actually do?

A) The 0.003 s read the file into four partitions; `mean()` returned an object because each of those partitions holds its own mean, and `.compute()` averages the four into the value shown
B) Almost nothing had happened yet: `dd.read_csv` inferred the schema and stopped there, and `mean()` added a node to a task graph that `.compute()` then ran over the four partitions
C) `mean()` returned an object because 4.3 MB exceeds the memory Dask allows per partition, so `.compute()` spills the partitions to disk and reads them back in order
D) The 0.003 s read the file into four partitions; `mean()` returned an object because Dask types its results lazily, and `.compute()` casts that object to float64

---

### 9. [Course 01 · Unit 1 / Unit 2]
Course 01's `KnowledgeBase` stored facts and rules, and its agent applied the rules to derive new conclusions. What is a key component of a knowledge representation system?

A) A relational database table with indexed columns, plus a query language to search them
B) A labeled training dataset and a loss function
C) A priority queue of nodes ordered by a heuristic estimate of the cost that remains
D) A store of facts, a set of rules over them, and an inference mechanism

---

### 10. [Course 02 · Unit 1]
Course 02's Unit 1 libraries notebook doubled the same numbers twice — once as a Python list comprehension, once as one NumPy whole-array operation — and printed:

```
         N    list (ms)   NumPy (ms)   speed-up
        10       0.0001       0.0003       0.5x
       100       0.0009       0.0003       3.0x
     1,000       0.0123       0.0006      21.5x
    10,000       0.1195       0.0032      37.1x
   100,000       1.2403       0.0254      48.8x
 1,000,000      15.1218       0.2454      61.6x
```

Which statement is supported by this table?

A) NumPy's lead grows with N, and at N = 10 the list version is the faster of the two
B) The list version scales better, because its cost per element falls as N grows
C) Both converge to the same speed at large N, since each loop is run by the interpreter
D) NumPy runs about 100× faster here, the speed-up the notebook's own text quotes

---

**End of paper. Hand nothing in. Stay for the worked answers.**
