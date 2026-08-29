# E17 assets — provenance

| file | what it is | how it was made |
|---|---|---|
| `arabic_parallel_sample.tsv` | 40 short sentences in three parallel columns: Modern Standard Arabic, a Saudi dialectal rendering of the same meaning, and an English gloss | **Written by the lesson author for this lesson.** It is a teaching sample, not a scraped or licensed corpus |

## Read this before quoting any number computed from this file

**It is a sample, not a corpus.** Forty sentences of everyday and workplace language, written by one author.
It is large enough to make tokenizer arithmetic visible and far too small to estimate anything about Arabic
in general. The notebook says so at every point where a number is reported, and the size caveat is repeated
in its "Where this breaks" section.

**The dialect column is one rendering, not "the" Saudi dialect.** Saudi Arabia contains several major
dialect regions — Najdi, Hijazi, Eastern, Southern — with substantial differences. The sentences here lean
Najdi/Hijazi and were chosen to be broadly recognisable. Treating them as representative of Saudi dialects
generally would be exactly the mistake the Absher benchmark ([arXiv:2507.10216](https://arxiv.org/abs/2507.10216))
was built to prevent.

**No language model was run to produce or evaluate this file.** Every number the notebook reports from it is
computed by code you can read in the notebook. All claims about Arabic LLM benchmark performance are
published claims, quoted with citations, and never measurements made in the lesson.
