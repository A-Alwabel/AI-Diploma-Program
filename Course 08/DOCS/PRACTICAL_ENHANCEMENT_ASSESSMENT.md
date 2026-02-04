# Course 08 – Practical & Real-Life Assessment
## Do students “know exactly what happens in real life”?

**Conclusion:** Compared to other diploma courses, Course 08 notebooks are **lighter on practical, real-life content**. Many are **objectives + one short code cell** (or no code). Students get theory and structure but **not** the same “run it, see it, understand it” experience as in Course 05 or Course 07.

---

## What other courses do (that Course 08 often doesn’t)

| Aspect | Course 05 / Course 07 (examples) | Course 08 (current) |
|--------|----------------------------------|----------------------|
| **Real data** | Real datasets (text, tables); load → inspect → use | Often no dataset; synthetic or “conceptual” only |
| **End-to-end pipeline** | Clear flow: load → preprocess → model/analyze → output | Many notebooks: objectives + 1 small code cell (imports or a print) |
| **Real outputs** | Plots, tables, printed results the student can see and interpret | Few notebooks show training curves, metrics, or predictions |
| **“Why in real life”** | Narrative: “Solving the Problem from Example 1”, “Where This Fits”, real use case | Little “real-world scenario” or “this is what happens in industry” |
| **Code density** | Multiple code cells; full pipeline in one notebook | Unit 1: most examples have **1 code cell**; 01_simple_neural_network has **0** code cells |
| **Student takeaway** | “I ran it, I saw the data and the result, I get it.” | “I read the objectives; I’m not sure what I’d actually run in a project.” |

So: **in practice, students do *not* yet “know exactly what happens in real life” from Course 08 the same way they can from those other courses.**

---

## Evidence from the repo

- **Course 08 Unit 1 examples:**  
  - `01_simple_neural_network.ipynb`: only markdown (objectives, “Visualization: Neural Network Architecture”, summary). **No code.**  
  - `02_backpropagation_detailed.ipynb`, `03_optimization_techniques.ipynb`, etc.: mostly **1 code cell** (e.g. `import numpy as np` + minimal content).  
  - `04_perceptron_mlp_tensorflow_pytorch_setup.ipynb`: has several code cells (imports, DL vs ML comparison, start of perceptron) – **closest to “practical”** in Unit 1, but still no full “load MNIST → train → evaluate” story.

- **Course 07 Unit 1 (contrast):**  
  - `01_text_preprocessing.ipynb`: real pipeline (tokenization → punctuation → stop words → frequency) with **real text, real printed output, and a plot**. Student sees “what happens in real life” step by step.

- **Course 05 (contrast):**  
  - `02_pandas_numpy_basics.ipynb`: strong narrative (“Solving the Problem from Example 1”, “Where This Notebook Fits”, “The Story: Learning Your Tools”) and explicit link to **real workflow** (lifecycle, tools, next steps).

So the gap is: **Course 08 has structure and theory, but not the same level of runnable, real-data, real-output, real-context practicals.**

---

## What “real life” should mean here

For students to **know exactly what happens in real life**, Course 08 should consistently offer:

1. **Real (or realistic) data**  
   - e.g. MNIST/Keras digits, CIFAR-10, or a small real-world-style dataset.  
   - Load in the notebook, show shape/sample, say why this data is used in practice.

2. **Full pipeline in the notebook**  
   - Load data → preprocess (if needed) → build model → train (with a few epochs) → evaluate (loss/accuracy, maybe a confusion matrix or sample predictions).  
   - So the student runs **one coherent story**, not isolated snippets.

3. **Visible, interpretable outputs**  
   - Training/validation loss and accuracy curves.  
   - Sample predictions (e.g. “this image is predicted as 7”).  
   - Short “how to read this” in markdown.

4. **Real-world context in markdown**  
   - 1–2 sentences per notebook: where this task appears (e.g. “Handwritten digit recognition is used in postal sorting, forms, etc.”).  
   - Optional: “In industry you’d also do X” (e.g. validation split, saving the model).

5. **Inputs & outputs section**  
   - Keep/expand: “Inputs: dataset X, libraries Y. Outputs: curves, metrics, sample predictions.” So the student knows what “running this in real life” produces.

---

## Recommended direction (high level)

1. **Upgrade existing Unit 1 notebooks** (especially `01_simple_neural_network.ipynb` and backprop/optimization) so that each has:  
   - At least one **end-to-end example** (e.g. MNIST with Keras/TF or PyTorch).  
   - Real training loop, real metrics, real plots.  
   - Short “real life” context in markdown.

2. **Use one notebook as the “gold standard”**  
   - e.g. one full “MNIST from load to evaluation” notebook.  
   - Then align other Unit 1 (and later Unit 2–5) notebooks to the same style: real data + full pipeline + clear inputs/outputs + real-world context.

3. **Add 1–2 “real-world scenario” notebooks per unit** (where missing)  
   - One scenario per notebook (e.g. “Digit recognition”, “Simple image classification”, “Sentiment with a small dataset”).  
   - Same pattern: load data → train → evaluate → interpret, with a short “why this matters in real life” at the top.

4. **Keep and reuse good structure from other courses**  
   - “Where This Notebook Fits”, “Inputs & Outputs”, “Real-World Context” (like Course 05/07).  
   - So Course 08 feels as “practical and real-life” as the rest of the diploma.

---

## Summary

- **Your concern is valid:** with the current notebooks, students do **not** get the same “I know exactly what happens in real life” experience as in other courses.  
- **Cause:** Course 08 is strong on **objectives and structure**, but weak on **runnable end-to-end examples**, **real data**, **visible results**, and **real-world narrative**.  
- **Fix:** Systematically add **real data + full pipeline + clear outputs + real-world context** to Course 08, using the same “practical” standard as Course 05 and Course 07, and document the target style in this assessment so the institution can align.

If you want, the next step can be: **concrete edits** to one notebook (e.g. `01_simple_neural_network.ipynb`) as a full “MNIST end-to-end” example, so you have a clear template to replicate across the course.
