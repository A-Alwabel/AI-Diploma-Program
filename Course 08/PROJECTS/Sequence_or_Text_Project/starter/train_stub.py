"""
Project 02 – Sequence / Text Model: Training stub (optional starter).
Copy this file into your project, rename it train.py, and fill in the TODOs.
Reference notebooks: Unit 3 02_rnn_basics, 03_lstm_advanced, 05_bert_finetuning.
"""
import numpy as np
import os

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1: Load and preprocess data
# ─────────────────────────────────────────────────────────────────────────────
def load_data():
    """
    Load your dataset and return (x_train, y_train), (x_val, y_val), (x_test, y_test).

    Options:
    A) IMDB sentiment (text, binary labels)  — see Unit 3 03_lstm_advanced.ipynb
    B) Custom CSV with 'text' and 'label'    — use pandas + train_test_split
    C) Time series CSV                       — use sliding window sequences
    """
    try:
        import tensorflow as tf
        # Option A: IMDB (downloads automatically)
        (x_train_raw, y_train), (x_test_raw, y_test) = tf.keras.datasets.imdb.load_data(
            num_words=10000
        )
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        MAX_LEN = 200
        x_train = pad_sequences(x_train_raw[:20000], maxlen=MAX_LEN, padding="post")
        x_val   = pad_sequences(x_train_raw[20000:], maxlen=MAX_LEN, padding="post")
        x_test  = pad_sequences(x_test_raw,          maxlen=MAX_LEN, padding="post")
        y_train, y_val = y_train[:20000], y_train[20000:]
        return (x_train, y_train), (x_val, y_val), (x_test, y_test)
    except Exception as e:
        print("Error loading data:", e)
        print("Using dummy data. Replace with your real dataset.")
        x = np.random.randint(0, 10000, size=(1000, 200))
        y = np.random.randint(0, 2,     size=(1000,))
        return (x[:700], y[:700]), (x[700:850], y[700:850]), (x[850:], y[850:])


# ─────────────────────────────────────────────────────────────────────────────
# STEP 2: Build your model
# ─────────────────────────────────────────────────────────────────────────────
def build_model(vocab_size=10000, embed_dim=64, max_len=200):
    """
    Build and return a compiled model.
    Replace the architecture with your own (LSTM, GRU, or BERT).
    Reference: Unit 3 03_lstm_advanced.ipynb
    """
    # TODO: Replace or extend this baseline LSTM with your architecture
    try:
        import tensorflow as tf
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(vocab_size, embed_dim, input_length=max_len),

            # TODO: Add your LSTM / GRU layers here
            tf.keras.layers.LSTM(64, return_sequences=True),
            tf.keras.layers.LSTM(32),

            # TODO: Add Dense layers and Dropout
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dropout(0.3),

            # Output: sigmoid for binary, softmax for multi-class
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ])
        model.compile(
            optimizer="adam",
            loss="binary_crossentropy",   # change for multi-class or regression
            metrics=["accuracy"],
        )
        model.summary()
        return model
    except ImportError:
        print("TensorFlow not installed. Run: pip install tensorflow")
        return None


# ─────────────────────────────────────────────────────────────────────────────
# STEP 3: Train
# ─────────────────────────────────────────────────────────────────────────────
def train(model, x_train, y_train, x_val, y_val):
    """
    Train the model and return the history.
    Reference: Unit 3 03_lstm_advanced.ipynb (training loop + callbacks).
    """
    import tensorflow as tf
    os.makedirs("models", exist_ok=True)

    callbacks = [
        # TODO: Add more callbacks if needed (e.g. LearningRateScheduler)
        tf.keras.callbacks.ModelCheckpoint(
            "models/best_model.keras",
            save_best_only=True,
            monitor="val_accuracy",
            verbose=1,
        ),
        tf.keras.callbacks.EarlyStopping(
            monitor="val_accuracy",
            patience=3,
            restore_best_weights=True,
            verbose=1,
        ),
    ]

    history = model.fit(
        x_train, y_train,
        epochs=10,               # TODO: increase for your real training run
        batch_size=64,
        validation_data=(x_val, y_val),
        callbacks=callbacks,
    )
    return history


# ─────────────────────────────────────────────────────────────────────────────
# STEP 4: Evaluate
# ─────────────────────────────────────────────────────────────────────────────
def evaluate(model, x_test, y_test):
    """Evaluate on the held-out test set and print results."""
    loss, acc = model.evaluate(x_test, y_test, verbose=1)
    print(f"\nTest accuracy: {acc:.4f}  |  Test loss: {loss:.4f}")
    return acc


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
def main():
    print("=== Step 1: Load data ===")
    (x_train, y_train), (x_val, y_val), (x_test, y_test) = load_data()
    print(f"Train: {x_train.shape}  Val: {x_val.shape}  Test: {x_test.shape}")

    print("\n=== Step 2: Build model ===")
    model = build_model()
    if model is None:
        return

    print("\n=== Step 3: Train ===")
    history = train(model, x_train, y_train, x_val, y_val)

    print("\n=== Step 4: Evaluate ===")
    evaluate(model, x_test, y_test)

    print("\nDone. Model saved to models/best_model.keras")
    print("Next: run predict_stub.py to test inference on new text.")


if __name__ == "__main__":
    main()
