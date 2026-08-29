# E16 assets — provenance

These four files support `../E16_document_parsing_became_a_vlm_problem.ipynb`.
Read this before quoting anything from them.

| file | what it is | how it was made |
|---|---|---|
| `make_text_layers.py` | The generator for the two text layers below | Written for this lesson; run it to regenerate after editing the source document |
| `page_text_layer_raw.txt` | A simulated PDF text layer in **storage order** — every character present, no geometry at all (`pdftotext` default behaviour) | Produced by `make_text_layers.py` from the real repository document `docs/QUICK_REFERENCE_GUIDE.md` |
| `page_text_layer_layout.txt` | A simulated **layout-preserving** text layer — character columns approximately kept, each cell wrapped inside its own column (`pdftotext -layout` behaviour) | Produced by `make_text_layers.py` from the same real document |
| `reference_parse.md` | The **correct structured parse** of that page: the target output, used as ground truth for scoring | Derived from the source document by the lesson author |

## What is real and what is simulated

**Real:** the source document (`docs/QUICK_REFERENCE_GUIDE.md`), every character of its content, and
the structure recorded in `reference_parse.md`.

**Simulated:** the two text layers. The lesson has no network and no PDF toolchain, so it cannot ship a
real PDF and run a real extractor. `make_text_layers.py` reproduces the specific, documented information
losses those extractors suffer — geometry discarded (raw mode), cells wrapped inside their columns with no
row marker (layout mode), running headers and page footers interleaved with content. The script is checked
in so the simulation can be audited rather than trusted.

**Not present, and deliberately so:** any vision-language model output. SmolDocling
([arXiv:2503.11576](https://arxiv.org/abs/2503.11576), 256M parameters) and MinerU2.5
([arXiv:2509.22186](https://arxiv.org/abs/2509.22186), 1.2B parameters) both require downloading
pretrained weights. No model was run for this lesson. Every claim the notebook makes about
vision-language document parsing is a published claim, quoted with its citation.
