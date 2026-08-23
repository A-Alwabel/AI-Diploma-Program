# When a notebook isn't clear
## For students: what to do when you don't understand (part of) a notebook

Some notebooks are harder than others. If you feel "I didn't understand some of it," use the steps below. Your instructor can also use this to help you.

---

## 1. Pinpoint what’s unclear

- **Which notebook?** (e.g. `05_backpropagation_detailed.ipynb`)
- **Which part?** (e.g. "Theory (short)", "Step 4", "the math", "what the code prints")
- **What did you expect?** (e.g. "I thought we’d see the formula first" or "I don’t know what gradient means")

When you ask your instructor, say: *"In notebook X, I didn’t get [section/step]. I got lost at [sentence or cell]."* That makes it much easier to help.

---

## 2. Use the notebook’s own structure

- **Learning objectives** (top): What you should get by the end. Re-read them after you finish; tick what you’re sure about.
- **Theory (short):** Read it again. The steps below put that theory into code. If the theory is unclear, say so: "I don’t get the chain rule bullet" or "I don’t get what GradientTape does."
- **Steps (Step 1, 2, 3…):** Run **one cell at a time**. Read the markdown above each cell. Look at the **output** (numbers, plot) and compare with the **Expected** line in "📥 Inputs & 📤 Outputs."
- **Summary / "What you did":** At the end. Use it to check: "Did I really do that?" If the summary is clear but the middle wasn’t, tell your instructor which section was unclear.

---

## 3. If the **math** is unclear

- Notebooks with **Key math** (e.g. backprop, activation functions, optimization, attention): the formula is there; the code uses it.
- Try: (1) Read the one sentence under "Key math" that has the main formula. (2) Run the next code cell and see the numbers (e.g. loss before/after update). (3) Say: "I see the numbers but I don’t see how they come from the formula." That’s a clear question.
- For full derivations, the notebook often says: "See lecture slides or [reference]."

---

## 4. If the **code** is unclear

- Run the cell and look at the **output**. Then read the **comment** at the top of the cell (e.g. "Step 2: Load and normalize MNIST").
- If there’s no comment, the **previous markdown cell** usually explains what the code does.
- Ask: "In Step X, what does [this line / this output] mean?" rather than "I don’t understand the code."

---

## 5. Notebooks that are often harder (so you’re not alone)

These often need a bit more time or a recap in class. It’s normal to find them less clear at first:

- **Unit 1:** `05_backpropagation_detailed` (gradients, chain rule), `06_optimization_techniques` (SGD vs Adam math)
- **Unit 2:** Transfer learning notebooks (05, 06) if you haven’t seen "freeze layers" before
- **Unit 3:** `04_transformer_attention` (Q/K/V, attention), `05_bert_finetuning` (the encoder + head fine-tuning pattern)
- **Unit 4:** `03_reinforcement_learning_...` (reward, policy), GANs/VAEs if the idea of generator/discriminator is new
- **Unit 5:** ONNX/TFLite if you haven’t seen "export" before

If you tell your instructor "I didn’t get notebook 05 (backprop)" or "I didn’t get the attention part in 04," they know where to focus.

---

## 6. One sentence you can use with your instructor

- *"I did notebook [number/name] in order, but I didn’t understand [Theory / Step X / the math / what the output means]. Can we go over that part?"*

That gives the instructor exactly what to clarify.

---

**Still stuck?** Ask your instructor using the sentence above — naming the notebook and the exact part is what makes help fast.
