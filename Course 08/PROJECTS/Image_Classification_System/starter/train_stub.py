"""
Project 01 – Training stub (optional starter).
Replace with your dataset, architecture, and paths.
"""
import numpy as np

def main():
    # -------------------------------------------------------------------------
    # 1. Data loading and preprocessing
    # -------------------------------------------------------------------------
    try:
        import tensorflow as tf
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
        x_train = x_train.astype("float32") / 255.0
        x_test = x_test.astype("float32") / 255.0
        num_classes = 10
        input_shape = (32, 32, 3)
    except Exception as e:
        print("Optional: pip install tensorflow. Using dummy data for stub.")
        x_train = np.random.rand(1000, 32, 32, 3).astype("float32")
        y_train = np.random.randint(0, 10, size=(1000, 1))
        x_test = np.random.rand(200, 32, 32, 3).astype("float32")
        y_test = np.random.randint(0, 10, size=(200, 1))
        num_classes = 10
        input_shape = (32, 32, 3)

    # -------------------------------------------------------------------------
    # 2. Model (small CNN – replace with your architecture or transfer learning)
    # -------------------------------------------------------------------------
    try:
        import tensorflow as tf
        model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=input_shape),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(num_classes, activation="softmax"),
        ])
        model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )
    except ImportError:
        print("TensorFlow not found. Install with: pip install tensorflow")
        return

    # -------------------------------------------------------------------------
    # 3. Train and save
    # -------------------------------------------------------------------------
    model.fit(
        x_train, y_train,
        epochs=2,  # use more epochs in your project
        validation_split=0.2,
        verbose=1,
    )
    loss, acc = model.evaluate(x_test, y_test, verbose=1)
    print(f"Test accuracy: {acc:.4f}")

    # Save model (create models/ if needed)
    import os
    os.makedirs("models", exist_ok=True)
    model.save("models/image_classifier.keras")  # or saved_model format
    print("Model saved to models/image_classifier.keras")

if __name__ == "__main__":
    main()
