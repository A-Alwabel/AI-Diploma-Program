# GPU Requirements Summary

Which courses use a GPU, and how to get one for free with Google Colab.

**Last Updated:** 2026-08

---

## Quick Summary

| Course | GPU needed? | Colab guide | Notes |
|--------|-------------|-------------|-------|
| **Course 05** | For the cuDF/RAPIDS notebooks only | `Course 05/DOCS/COLAB_SETUP.md` | Every GPU notebook has a pandas CPU fallback |
| **Course 08** | Strongly recommended | `Course 08/DOCS/COLAB_SETUP.md` | Deep learning training is 10–100x faster on GPU |
| **Course 10** | Strongly recommended | `Course 10/DOCS/COLAB_SETUP.md` | GAN/VAE/diffusion training is impractical on CPU |
| **All other courses** | No | — | Run fine on any CPU |

**Bottom line:** you can complete the entire program without owning a GPU —
use Google Colab for the notebooks that need one.

---

## Detailed Breakdown

### Course 05: Scalable Data Science

**GPU used by:** the cuDF/RAPIDS notebooks, including:

- `unit1-introduction/examples/03_cudf_introduction.ipynb`
- `unit2-cleaning/examples/07_cudf_import_export_gpu.ipynb`
- `unit5-scaling/examples/04_rapids_workflows.ipynb`

**Fallback:** every cuDF notebook falls back to pandas on CPU — slower, but the
whole course is completable without a GPU. Dask notebooks are CPU-based.

### Course 08: Deep Learning

**GPU helps with:** training CNNs, RNNs, and transformers. All notebooks run on
CPU, but training-heavy ones take much longer.

**Local note:** on this repository's reference setup, TensorFlow notebooks run
on the separate `tfenv` kernel (see [SETUP_GUIDE.md](SETUP_GUIDE.md)); PyTorch
notebooks run on the main `ai-diploma` kernel. On Colab, both frameworks are
preinstalled with GPU support.

### Course 10: Generative AI

**GPU helps with:** GAN and VAE training, diffusion models, and larger
language-model examples. CPU training of these models can take days — use Colab.

### All other courses (01–04, 06, 07, 09, 11, 12)

- Standard scientific Python (NumPy, pandas, scikit-learn, etc.)
- No GPU needed; everything runs on a normal laptop
- Course 09's RL environments (`gymnasium` classic-control) are CPU-friendly

---

## Using Google Colab

1. Upload or open the notebook in [Colab](https://colab.research.google.com/)
2. Enable GPU: **Runtime → Change runtime type → GPU**
3. Run the course's Colab setup cell (each GPU course's
   `DOCS/COLAB_SETUP.md` explains what to install)
4. Run the notebook top to bottom

**Free-tier tips:**

- GPU time is limited and resets daily — save your work often
- Mount Google Drive to keep outputs between sessions
- If quota runs out, switch to CPU for reading/small cells and come back later

---

## For Students With a Local NVIDIA GPU

1. Install the CUDA-enabled build of PyTorch
   ([pytorch.org](https://pytorch.org/get-started/locally/))
2. Verify:

   ```python
   import torch
   print(torch.cuda.is_available())
   ```

3. Monitor memory with `nvidia-smi`; lower batch sizes if you hit
   out-of-memory errors
4. RAPIDS/cuDF (Course 05) requires a supported CUDA version — see
   <https://rapids.ai/>

---

## Related Documents

- [SETUP_GUIDE.md](SETUP_GUIDE.md) — environment setup, kernels
- [TROUBLESHOOTING_GUIDE.md](TROUBLESHOOTING_GUIDE.md) — GPU errors and fixes
