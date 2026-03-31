#!/usr/bin/env python3
"""Replace generic learning objectives with specific ones in Course 07 (NLP) notebooks."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
C07 = ROOT / "Course 07"

SPECIFIC_OBJECTIVES = {
    "unit1-nlp-fundamentals/examples/01_text_preprocessing.ipynb": [
        "Clean and normalize text (lowercasing, punctuation, whitespace)",
        "Use basic preprocessing pipelines for NLP",
        "Prepare text for downstream tasks",
    ],
    "unit1-nlp-fundamentals/examples/02_nltk_spacy_introduction.ipynb": [
        "Use NLTK and SpaCy for tokenization and POS tagging",
        "Apply stemming, lemmatization, and basic NLP utilities",
        "Compare library outputs and choose appropriate tools",
    ],
    "unit1-nlp-fundamentals/examples/03_real_world_nlp_applications.ipynb": [
        "Apply NLP to real-world use cases",
        "Connect preprocessing and tools to applications",
        "Interpret and communicate NLP results",
    ],
    "unit2-tokenization-morphology/examples/01_advanced_tokenization.ipynb": [
        "Implement advanced tokenization (subword, BPE-style)",
        "Handle morphologically rich languages",
        "Choose tokenization strategies for different models",
    ],
    "unit2-tokenization-morphology/examples/02_text_vectorization_bow_tfidf.ipynb": [
        "Build BoW and TF-IDF representations",
        "Use vectorizers for classification and retrieval",
        "Interpret and tune vectorization parameters",
    ],
    "unit3-ml-for-nlp/examples/01_text_classification.ipynb": [
        "Train text classifiers (e.g. on sentiment, topic)",
        "Use traditional ML with text features",
        "Evaluate and compare classifiers",
    ],
    "unit3-ml-for-nlp/examples/03_topic_modeling_lda_nmf.ipynb": [
        "Apply LDA and NMF for topic modeling",
        "Interpret topics and document-topic distributions",
        "Evaluate and visualize topic models",
    ],
    "unit4-deep-learning-nlp/examples/01_rnn_lstm_nlp.ipynb": [
        "Use RNNs and LSTMs for sequence modeling",
        "Implement text generation or classification with recurrent nets",
        "Understand gradients and sequence length effects",
    ],
    "unit4-deep-learning-nlp/examples/02_lstm_text_generation.ipynb": [
        "Build LSTM-based text generation models",
        "Sample and decode from trained models",
        "Tune temperature and sampling for quality",
    ],
    "unit5-applications-ethics/examples/01_bias_detection.ipynb": [
        "Detect bias in NLP models and datasets",
        "Use fairness metrics and qualitative analysis",
        "Address bias in preprocessing and evaluation",
    ],
    "unit5-applications-ethics/examples/02_text_summarization.ipynb": [
        "Implement extractive or abstractive summarization",
        "Evaluate summary quality and coverage",
        "Compare approaches and model choices",
    ],
    "unit5-applications-ethics/examples/03_chatbot_implementation.ipynb": [
        "Build a simple chatbot (rule-based or model-based)",
        "Handle intent detection and response generation",
        "Evaluate and improve chatbot interactions",
    ],
}


def fix_objectives(nb_path: Path, rel: str) -> bool:
    spec = SPECIFIC_OBJECTIVES.get(rel)
    if not spec:
        return False
    try:
        with open(nb_path, encoding="utf-8") as f:
            nb = json.load(f)
    except json.JSONDecodeError:
        return False
    changed = False
    for c in nb["cells"]:
        if c.get("cell_type") != "markdown":
            continue
        lines = c.get("source", [])
        if not isinstance(lines, list):
            continue
        src = "".join(lines)
        if "Understand the key concepts of this topic" not in src:
            continue
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if "- Understand the key concepts of this topic" in line:
                if new_lines and "By completing this notebook" not in new_lines[-1]:
                    new_lines.append("By completing this notebook, you will:\n")
                for s in spec:
                    new_lines.append(f"- {s}\n")
                i += 1
                while i < len(lines) and (
                    "- Apply the topic using Python code examples" in lines[i]
                    or "- Practice with small, realistic datasets or scenarios" in lines[i]
                ):
                    i += 1
                continue
            new_lines.append(line)
            i += 1
        if new_lines != lines:
            c["source"] = new_lines
            changed = True
        break
    if changed:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    return changed


def main():
    done = []
    for nb_path in sorted(C07.rglob("*.ipynb")):
        rel = nb_path.relative_to(C07).as_posix()
        if "DOCS" in rel or "PROJECTS" in rel:
            continue
        if fix_objectives(nb_path, rel):
            done.append(rel)
    print("Updated objectives:", len(done))
    for r in done:
        print(" ", r)


if __name__ == "__main__":
    main()
