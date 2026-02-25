"""
Project 02 – Sequence / Text Model: Prediction stub (optional starter).
Loads your saved model and runs inference on new text.
Reference: Unit 5 06_flask_fastapi_deployment.ipynb
"""

# ─────────────────────────────────────────────────────────────────────────────
# Load model and tokenizer
# ─────────────────────────────────────────────────────────────────────────────
def load_model_and_tokenizer(model_path="models/best_model.keras",
                              tokenizer_path=None):
    """
    Load the trained model.
    If you trained an LSTM/GRU and saved a tokenizer, pass tokenizer_path too.
    If you used IMDB built-in tokenization, tokenizer_path can be None.
    """
    try:
        import tensorflow as tf
        model = tf.keras.models.load_model(model_path)
        print(f"Model loaded from {model_path}")
    except Exception as e:
        print(f"Could not load model from {model_path}: {e}")
        print("Train the model first using train_stub.py")
        return None, None

    tokenizer = None
    if tokenizer_path:
        try:
            import pickle
            with open(tokenizer_path, "rb") as f:
                tokenizer = pickle.load(f)
            print(f"Tokenizer loaded from {tokenizer_path}")
        except Exception as e:
            print(f"Could not load tokenizer: {e}")

    return model, tokenizer


# ─────────────────────────────────────────────────────────────────────────────
# Preprocess and predict
# ─────────────────────────────────────────────────────────────────────────────
def predict_text(model, text, tokenizer=None, max_len=200):
    """
    Tokenize one text string and return the predicted label + confidence.
    Adjust for your task (binary vs multi-class vs regression).

    TODO: If you used your own tokenizer, uncomment the tokenizer block below.
    TODO: If you used BERT, replace this function with the HuggingFace tokenizer.
    """
    import numpy as np
    from tensorflow.keras.preprocessing.sequence import pad_sequences

    if tokenizer is not None:
        # TODO: Use your saved tokenizer
        seq = tokenizer.texts_to_sequences([text])
        padded = pad_sequences(seq, maxlen=max_len, padding="post")
    else:
        # Placeholder: replace with your actual preprocessing
        print("No tokenizer provided. Using random input as placeholder.")
        padded = np.random.randint(0, 10000, size=(1, max_len))

    prob = float(model.predict(padded, verbose=0)[0][0])

    # TODO: Adjust label names and threshold for your task
    label = "Positive" if prob > 0.5 else "Negative"
    confidence = prob if prob > 0.5 else 1 - prob
    return {"label": label, "confidence": confidence, "raw_prob": prob}


# ─────────────────────────────────────────────────────────────────────────────
# MAIN — test on a few sample texts
# ─────────────────────────────────────────────────────────────────────────────
def main():
    model, tokenizer = load_model_and_tokenizer(
        model_path="models/best_model.keras",
        tokenizer_path=None,   # set to "models/tokenizer.pkl" if you saved one
    )
    if model is None:
        return

    # TODO: Replace these with your own test sentences
    test_texts = [
        "This movie was absolutely amazing! I loved every minute.",
        "Terrible experience. I would never recommend this to anyone.",
        "The product is okay, not great, not bad.",
    ]

    print("\n=== Sample Predictions ===")
    for text in test_texts:
        result = predict_text(model, text, tokenizer=tokenizer)
        print(f"Text:       {text[:60]}...")
        print(f"Predicted:  {result['label']}  (confidence: {result['confidence']:.2%})")
        print()


if __name__ == "__main__":
    main()
