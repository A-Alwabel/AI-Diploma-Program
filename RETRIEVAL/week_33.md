# Retrieval Quiz — Week 33

**Week 33 of 35 · Course 11 — AIAT 125 (Deploying AI Models) and Course 12 — AIAT 126 (Graduation Project)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

The `success_criteria` block taught in Unit 1 pairs a **named metric** with a **numeric threshold** and the reason that threshold was chosen. Which of these is a properly stated success criterion in that form?

A) The model will use a deep neural network trained on the collected image set  
B) The model will be state of the art for this task by the end of the project  
C) Recall above 85% on the validation set, since false negatives are the costly error  
D) The model will perform well on the medical images the partner supplied for the project  

---

### Question 2

The `scope` block taught in Unit 1 requires an **`out_of_scope`** list beside the `in_scope` list. Why?

A) Because the out-of-scope items become the starting point of the literature review section  
B) Because naming what you will not build is what keeps the project finishable in 14 weeks  
C) Because reviewers ask for a longer proposal document before the design review  
D) Because the success criteria are recorded inside the out-of-scope list  

---

### Question 3

Unit 5 motivated one tool with three questions an untracked team cannot answer: which run produced the production model, which hyperparameters were already tried, and which data the model saw. What is **MLflow** used for?

A) Logging parameters, metrics and artifacts per run, so runs can be compared later  
B) Building and deploying the Docker containers that serve a trained model  
C) Writing the Kubernetes manifests that a served model is rolled out with each release  
D) Cleaning and transforming the raw data before a training run begins  

---

### Question 4

A marketplace wants a fresh banner image for each of its listings every night, inside a fixed maintenance window on the GPUs it already owns. A colleague proposes the Unit 3 diffusion model and argues its sampling cost will shrink on its own: the training loss fell `0.2712 → 0.1229 → 0.0956` over three epochs, so a better-trained denoiser should need fewer denoising steps. In the notebook, the from-scratch sampler walked **t = 199 down to t = 0** for each image, while a GAN produces an image in one forward pass. Which reasoning should drive the family choice for this job?

A) The falling MSE is the right signal: a denoiser that predicts noise more accurately can skip steps safely, so diffusion's per-image cost converges on the GAN's as training continues and the maintenance window stops being a constraint.  
B) The step count comes from the schedule, not the weights — the sampler walks t = 199 down to 0 whatever the loss reads — so diffusion's cost scales with its steps and the one-pass GAN is the throughput choice for this nightly job.  
C) Step counts are beside the point for a batch job: how many images fit in the window is set by output resolution and batch size, so pick whichever family gives the sharper banners and tune the batching afterwards.  
D) A VAE decoder is the one-pass option to prefer here: it generates in a single decoder pass, and its pixel-wise reconstruction loss is what keeps each banner crisp enough for a product page, without the GAN's training instability.  

---

### Question 5

Unit 4's Titanic audit trained a survival model with `Sex` and again without it. The sex-aware model predicted survival for **90.7%** of women and **8.8%** of men; the blind model for **35.1%** and **21.6%**. Among passengers who actually survived, the aware model found **97.1%** of the women and **24.2%** of the men; the blind model **44.3%** and **48.5%**. A team lead wants to ship the blind model and stop collecting the attribute altogether, "so nobody can say we used it". What do these figures say about that plan?

A) The plan is sound: with no `Sex` column there is no route from sex to the prediction, so the 35.1% against 21.6% is sampling noise on a small test split that a larger manifest would wash out, and the audit has already done its job.  
B) The plan is sound on the second metric: 44.3% against 48.5% shows the blind model treats surviving women and surviving men nearly alike, so equal opportunity is satisfied and the attribute can safely be retired from the pipeline.  
C) The blind model still predicts survival for women more often than for men, so the disparity came through correlated features — and without the attribute the team could no longer measure it: the audit it would be giving up.  
D) The figures show the gap closed because the model degraded: a classifier that predicts 'died' for everyone would also show matching rates for the two groups, and the blind model's falling rates are drifting toward that.  

---

### Question 6

A teammate posts four status updates about the `wdbc-baseline` model from Unit 1 lesson 01. Which update is the one that means the model has actually been **deployed**?

A) `model.joblib` (2.2 KB) and `model_card.json` have been exported to `~/ai-diploma-portfolio/`  
B) `card['sample_input']` comes back `benign` at 99.9% confidence when the notebook itself calls `model.predict_proba`  
C) Held-out accuracy reads 0.9825 on the stratified 20% split, so the model is now ready for release  
D) `uvicorn main:app --host 0.0.0.0 --port 8000` is running and other programs get answers from `POST /predict`  

---

### Question 7

In Course 01 you built a small knowledge graph over family relations and queried it. What is a knowledge graph?

A) A neural network whose neurons are arranged as nodes and edges rather than as layers  
B) A search algorithm that walks a graph outward from a start node until it first meets a goal node  
C) An activation function applied over a graph of inputs to produce one scalar output  
D) A structure that stores entities as nodes and the relations between them as labelled edges  

---

### Question 8

The eigenvalues lesson notes that the raw USArrests features live on very different ranges — Murder spans 0.8–17.4 and Assault 45–337 arrests per 100,000 — and its figure note says that on raw units PC1 'points almost straight up: 99.8% of it is the Assault axis'. After standardizing, the printed feature variances are Murder = 1.02 and Assault = 1.02, and PC2 keeps 9.91% of the variance. A colleague wants to send the raw-units decomposition to a state governor because 'it explains far more of the variance'. Why is the standardized run the one to report?

A) On raw units PC1 is nearly the Assault column renamed, so its variance figure describes the recording scale, not a crime pattern  
B) Standardizing gives both features a variance of 1.02, which adds spread for PC1 to explain that the raw run lacked  
C) The 9.91% left to PC2 after standardizing shows the raw run had dropped its second component and summed over a single eigenvalue  
D) Because 99.8% of raw PC1 lies along Assault, the raw covariance matrix is close to singular and its eigenvalues cannot be trusted  

---

### Question 9

After setting `requires_grad = False` on the MobileNetV2 base and attaching `Dropout(0.2)` + `Linear(1280, 10)`, the lesson prints **Frozen (reused): 2,223,872 parameters = 99.43%**. Training on **2,000** resized MNIST digits, the head reports train accuracy **0.569** after epoch 1 and **0.843** after epoch 2, then scores **0.854** on the **500** held-out images. Which reading of this run is correct?

A) The 99.43% already encodes digits well enough that the two epochs mostly confirm what the model could do before any training  
B) With 99.43% frozen there is too little capacity left to memorise 2,000 images, so the 500-image hold-out is a formality  
C) The 99.43% stays as ImageNet learned it; the climb from 0.569 to 0.843 is the fresh head learning what the ten digit classes look like  
D) A base frozen to 99.43% pays off once the new dataset is at least ImageNet-sized; at 2,000 digits the whole network should be unfrozen and retrained  

---

### Question 10

Unit 3's logistic-regression lesson sweeps the decision cut from 0.1 to 0.9 on its 3,200-row test set and prints:

```
Threshold    Accuracy     Precision    Recall       F1 Score
0.1          0.9975       0.4000       0.6667       0.5000
0.2          0.9984       0.5714       0.6667       0.6154
0.3          0.9981       0.5000       0.5000       0.5000
...
0.9          0.9981       0.5000       0.5000       0.5000
```

Precision and recall move by tens of points down the table; the accuracy column stays between 0.9975 and 0.9984. A student asks why accuracy looks "stuck". What is the correct explanation?

A) The model's predicted probabilities are nearly identical from row to row, so sliding the cut hardly changes any individual prediction  
B) Accuracy, like AUC, is defined over the whole range of thresholds at once, so a table that varies the cut is not something it is expected to respond to  
C) A 3,200-row test set is simply too small for accuracy to resolve the differences between cuts; a larger test sample would separate the rows of the table cleanly and rank them  
D) 3,194 of 3,200 rows are legitimate and cleared at almost any cut, so accuracy stays pinned near the baseline of calling each row legitimate, whatever the 6 fraud rows do  

---
