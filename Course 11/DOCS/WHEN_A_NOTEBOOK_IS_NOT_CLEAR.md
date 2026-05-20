# When a Notebook Is Not Clear

Use this page when a Course 11 notebook runs but **you do not understand** what it showed.

## Step 1 — Check the run order

1. Open the unit `README.md` and confirm you are on the correct **numbered** notebook.
2. Run cells **from the top** (or **Restart & Run All** once).
3. Read the **Lesson Brief** (first cell) and **Closing Takeaway** (near the end).

## Step 2 — Name what you are stuck on

Pick **one** of these:

| Stuck on… | Re-read in the notebook |
| --------- | ------------------------ |
| **Artifact** | Which file or object is saved (`.pkl`, `.onnx`, `.pt`, Docker image)? |
| **API** | Which URL path and HTTP method (`GET /health`, `POST /predict`)? |
| **Environment** | Which `pip install` cell did you skip? |
| **Cloud / K8s** | Is this cell **simulation** (runs locally) vs **live** (needs account)? |
| **Metric** | What number or plot would get worse if the model broke in production? |

## Step 3 — Compare to the previous notebook

Deployment is cumulative. If Unit 2 feels hard, skim Unit 1 notebook **05** and **06** summaries first.

## Step 4 — Ask your instructor efficiently

Send:

1. Notebook path (e.g. `unit2-versioning-serving/examples/02_fastapi_deployment.ipynb`)
2. Cell number where confusion starts
3. Your one-sentence guess + your specific question

Example: *"In cell 4 I see `uvicorn` but I don't know how a client sends JSON features — is the body the same as the Pydantic model?"*

## Remember

A **clean run** means the code executed. It does **not** mean every production concept is obvious yet. Use the **Did you understand?** section at the end of each example notebook.
