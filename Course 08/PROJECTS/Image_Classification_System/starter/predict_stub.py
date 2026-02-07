"""
Project 01 – Inference stub (optional starter).
Load a saved model and run prediction on one or more images.
Replace model_path and image paths with your own.
"""
import os
import sys

def main():
    model_path = "models/image_classifier.keras"
    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}. Run train_stub.py first or set model_path.")
        return

    try:
        import tensorflow as tf
        import numpy as np
    except ImportError:
        print("Install: pip install tensorflow numpy")
        return

    # Load model
    model = tf.keras.models.load_model(model_path)
    print(f"Loaded model from {model_path}")

    # Example: predict on random image (replace with loading your image)
    # For CIFAR-10: shape (32, 32, 3), values in [0, 1]
    dummy_image = np.random.rand(1, 32, 32, 3).astype("float32")
    pred = model.predict(dummy_image)
    class_id = int(np.argmax(pred[0]))
    confidence = float(np.max(pred[0]))
    print(f"Predicted class: {class_id}, confidence: {confidence:.4f}")

    # Optional: load image from file
    # from PIL import Image
    # img = Image.open("path/to/image.jpg").resize((32, 32))
    # arr = np.array(img) / 255.0
    # arr = np.expand_dims(arr, axis=0)
    # pred = model.predict(arr)

if __name__ == "__main__":
    main()
