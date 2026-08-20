# Unit 1 — Introduction to Deep Learning and Neural Networks
## AIAT 122 — Deep Learning

Unit training hours: 12 (of 64 total)

## Prerequisites

- Semester 1 (AIAT 111–116), including machine learning fundamentals.
- Comfortable with Python and NumPy.
- Environment set up (see `../START_HERE.md`): "ai-diploma" kernel for PyTorch notebooks, "tfenv" kernel for TensorFlow notebooks.

## What this unit teaches

What deep learning is and how it differs from traditional ML; the structure of neural networks (perceptron, MLP, layers, activation functions); how training works (loss, forward and backward propagation, backpropagation, optimizers); building and evaluating first models in TensorFlow/Keras and PyTorch.

## Examples (do in file order)

Run the notebooks in `examples/` in this order:

1. `01_deep_learning_fundamentals_compared_to_traditional_ml.ipynb` — what deep learning is and when it beats (or loses to) traditional ML.
2. `02_simple_neural_network.ipynb` — build and train your first neural network; layers, fit, loss and accuracy curves.
3. `03_perceptron_mlp_tensorflow_pytorch_setup.ipynb` — perceptron and MLP; setting up and comparing TensorFlow and PyTorch.
4. `04_activation_functions_and_optimization_algorithms.ipynb` — sigmoid/ReLU/tanh and how optimizers update weights.
5. `05_backpropagation_detailed.ipynb` — gradients and the chain rule, step by step.
6. `06_optimization_techniques.ipynb` — SGD, momentum, Adam; learning-rate effects.
7. `07_image_processing_feature_extraction.ipynb` — image data as arrays; basic preprocessing and feature extraction.
8. `08_forward_and_backward_propagation.ipynb` — the full forward and backward pass through a network.

## Exercise

- `exercises/01_neural_network_exercise.ipynb` — build, train, and evaluate a neural network classifier. Solutions are released by your instructor.

## Quiz

- `../QUIZZES/quiz_01.md`

## Next

Unit 2: `../unit2-cnns/README.md`
