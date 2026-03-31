# Course 08 – Notebook run and pedagogy verification

## Were the notebooks run and verified?

**Update (2026-02-07):** All **student-facing** Course 08 notebooks (examples + exercises) were run using the **course2** conda environment (Python 3.8, TensorFlow 2.13, PyTorch 2.4). **All 43 notebooks completed without execution errors (43/43).** The runner excludes `solutions/` folders.

**What was verified:** (1) Each notebook **runs to completion** (43/43 in course2). (2) A **full output and pedagogy verification** was done: for each notebook, promised outputs were checked against actual outputs, and the approach (theory + runnable example) was confirmed as appropriate for teaching that topic. See **`DOCS/OUTPUT_AND_PEDAGOGY_VERIFICATION_COMPLETE.md`** for the per-notebook verification table. Automated output check: **`DOCS/output_pedagogy_verification_report.txt`** (and `.json`).

**What you should do:** Run all Course 08 notebooks (see below), then use the **output alignment** and **pedagogy** checklists to confirm that:
1. Every notebook runs without error and produces the **promised** outputs (and that those outputs are correct).
2. Theory and practice align with what we teach and are a good approach for each topic.

---

## How to run all Course 08 notebooks

### Option 1: Use the Course 08 script (recommended)

From the **AI Diploma** repo root, using your env (e.g. **course2**):

```bash
conda activate course2   # or: source activate course2
pip install --upgrade mistune nbconvert   # if nbconvert fails with mistune import
python "Course 08/tools/run_course08_notebooks.py"
```

The script runs all notebooks under `examples/` and `exercises/` (it skips `solutions/` folders) and writes:
- `Course 08/DOCS/notebook_run_report.json`
- `Course 08/DOCS/notebook_run_report.txt`

### Option 2: Use the existing tools folder

From the **AI Diploma** repo root:

```bash
python tools/execute_all_notebooks.py
```

Then open the generated report and filter for paths under `Course 08/`. This runs all diploma notebooks; for Course 08 only, use Option 1.

### Option 3: Manual run (Jupyter or Colab)

1. Open each notebook in Jupyter or upload to Google Colab (see `DOCS/COLAB_SETUP.md`).
2. **Run All** (Cell → Run All).
3. Check that there are no errors and that the outputs described in the **📥 Inputs & 📤 Outputs** section appear (numbers, plots, sample predictions, etc.).

### Option 4: Command-line execute with nbconvert

From the **AI Diploma** repo root:

```bash
for f in "Course 08"/unit*/*/examples/*.ipynb "Course 08"/unit*/*/exercises/*.ipynb; do
  [ -f "$f" ] && jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=300 --inplace "$f" || true
done
```

Then scan the notebooks for execution errors (e.g. tracebacks in the output).

---

## Output alignment checklist (after running)

For each notebook, confirm that the **actual outputs** match what the notebook promises in the **📥 Inputs & 📤 Outputs** section. Use this table as a verification grid (instructor or maintainer fills it after a run).

| Unit | Notebook | Promised outputs (from notebook) | Verified? (Y/N) | Notes |
|------|----------|----------------------------------|------------------|--------|
| 1 | 01_deep_learning_fundamentals_* | NN accuracy, LR accuracy, comparison sentence | | |
| 1 | 02_simple_neural_network | Loss/accuracy curves, test accuracy, 5 sample predictions | | |
| 1 | 03_perceptron_mlp_* | Setup, perceptron/MLP definition or training | | |
| 1 | 04_activation_functions_* | Plots or table of activations | | |
| 1 | 05_backpropagation_detailed | Loss, gradient info, loss before/after update, bar chart | | |
| 1 | 06_optimization_techniques | SGD vs Adam loss curves | | |
| 2 | 01_cnn_architecture | Train/test shapes, model summary, loss/accuracy curves, sample predictions | | |
| 2 | 02_image_processing_* | Image preprocessing and/or feature extraction outputs | | |
| 2 | 03_cnn_advanced_architectures | Architectures (e.g. LeNet/AlexNet), model or comparison | | |
| 2 | 04_transfer_learning_object_detection | Object detection intro, model or outputs | | |
| 2 | 05_transfer_learning_cnns | Transfer learning flow, fine-tuning or feature extraction | | |
| 2 | 06_pretrained_cnn_architectures | Pretrained models (VGG/ResNet etc.), evaluation | | |
| 2 | 07_training_cnn_image_datasets | Full training pipeline (e.g. CIFAR-10), curves, accuracy | | |
| 3 | 01_understanding_sequential_* | Sequential data / time series, example outputs | | |
| 3 | 02_rnn_basics | RNN definition or training, outputs | | |
| 3 | 03_lstm_advanced | LSTM/GRU, training or outputs | | |
| 3 | 04_transformer_attention | Attention mechanism, code or visualization | | |
| 3 | 05_bert_finetuning | BERT load/fine-tune, metrics | | |
| 4 | 01_gans_and_autoencoders_vaes | GAN/VAE concepts, generator/discriminator or encoder/decoder | | |
| 4 | 02_implementing_a_vae_* | VAE training, reconstruction or anomaly | | |
| 4 | 03_reinforcement_learning_* | RL env (e.g. Gym), agent or DQN/policy | | |
| 4 | 04_ethical_concerns_* | Fairness metrics (e.g. accuracy by group), interpretability | | |
| 5 | 01_model_optimization | Optimization steps, size/speed comparison | | |
| 5 | 02_tensorflow_serving | Serving setup or export | | |
| 5 | 03_onnx_conversion | ONNX export/load, run | | |
| 5 | 04_model_pruning | Pruning, size or accuracy | | |
| 5 | 05_model_distillation | Distillation, student model | | |
| 5 | 06_flask_fastapi_deployment | API definition, test request output | | |
| 5 | 07_model_optimization_quantization | Quantization, model size or latency | | |

**How to use:** After running a notebook, open it and the **Inputs & Outputs** section; tick “Verified?” and add any note (e.g. “Plot present but axis labels small”).

---

## Pedagogy checklist (theory + practice, best approach)

For each **core** notebook, confirm that the **teaching approach** is sound:

1. **Theory (short)**  
   - [ ] The “Theory (short)” section matches the **slide(s)** in **📌 Covers slide(s)** (or “Unit 5 – no slides”).  
   - [ ] Concepts are correct and at the right level (no major gaps or wrong statements).  
   - [ ] It states **why we use this** (and optionally “instead of X”) so students see the motivation.  
   - [ ] **Math-heavy topics** (e.g. backprop, attention, optimization): notebook includes **key formulas and a short derivation** (or a “Key math” subsection); full derivation may link to slides/reference. Math is **required**, not optional (see NOTEBOOK_STANDARD.md).

2. **Practice (code)**  
   - [ ] The code implements what the learning objectives say (e.g. “Train a small NN” → there is a training call and a metric).  
   - [ ] The flow is appropriate: e.g. load data → preprocess → model → train → evaluate (or the right variant for that topic).  
   - [ ] Outputs are **visible and interpretable** (numbers, curves, or sample predictions), not only “model built”.

3. **Best approach for this topic**  
   - [ ] For **theory-heavy / math-heavy** topics (e.g. backprop, attention): the notebook includes **key formulas and short derivation** (required) and balances theory with a **concrete runnable example** (e.g. GradientTape, or one attention computation) so students “see it work.”  
   - [ ] For **practice-heavy** topics (e.g. training a CNN): the notebook gives enough context (objectives + real-life blurb + Inputs & Outputs) so students know what they’re doing and what good looks like.  
   - [ ] Optional/mini-exercises (if present) support the main idea without overwhelming.

4. **Real-life and next steps**  
   - [ ] “Real life” blurb is present and accurate.  
   - [ ] Summary or “In real life you’d also” points to natural next steps (e.g. validation, saving model).

**How to use:** Go through each core notebook once; tick the boxes and fix any notebook where a box can’t be ticked (e.g. wrong slide reference, missing output, or misleading theory).

---

## Summary

- **Run:** Use Option 1 (Course 08 script), 2 (repo-wide script), 3 (manual), or 4 (nbconvert loop) in an environment with TensorFlow (and PyTorch where needed).  
- **Outputs:** Use the **Output alignment checklist** to ensure each notebook’s outputs match the **Inputs & Outputs** section.  
- **Pedagogy:** Use the **Pedagogy checklist** to ensure theory and practice align with what we teach and are a good approach for each topic (theoretical and practical).  

When all three are done and any issues are fixed, the notebooks are **verified** for both run and teaching alignment.

**Last updated:** 2025-02-07
