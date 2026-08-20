# Unit 4: Neural Networks Fundamentals

**Course:** AIAT 111 · **Unit hours:** 14 (7 theory + 7 practical)

Neurons and activation functions, the perceptron, multi-layer networks, and an introduction to deep learning architectures: CNNs, RNNs, LSTM/GRU, plus overfitting and regularization.

**Prerequisites:** Unit 3 (`../unit3-ml-basics/README.md`).

**Kernels:** notebook 01 runs on the `ai-diploma` kernel; notebooks 02–07 and the exercise use TensorFlow/Keras and run on the `tfenv` kernel (see `../START_HERE.md`).

---

## Notebooks (run in order)

| # | Notebook | What it covers |
|---|----------|----------------|
| 01 | `examples/01_simple_perceptron.ipynb` | A simple perceptron: weights, activation, training |
| 02 | `examples/02_cnn_rnn_architectures.ipynb` | Deep learning architectures: CNNs and RNNs (`tfenv` kernel) |
| 03 | `examples/03_single_neuron_activation_functions.ipynb` | One neuron, three activation functions: sigmoid vs tanh vs ReLU compared (`tfenv` kernel) |
| 04 | `examples/04_multiclass_classification_keras.ipynb` | Multi-class digit classification with an MLP: softmax and categorical crossentropy (`tfenv` kernel) |
| 05 | `examples/05_cnn_image_classification.ipynb` | Training a CNN on images and comparing it against a dense network (`tfenv` kernel) |
| 06 | `examples/06_rnn_lstm_gru_sequential.ipynb` | Training RNN, LSTM, and GRU models on sequential data (`tfenv` kernel) |
| 07 | `examples/07_early_stopping_regularization.ipynb` | Overfitting and its fixes: early stopping, dropout, and L2 regularization (`tfenv` kernel) |

---

## After the Notebooks

1. **Exercise:** `exercises/exercise_01.ipynb` (`tfenv` kernel). Solutions are released by your instructor.
2. **Quiz:** `quizzes/quiz_04.md`

Then continue to Unit 5: `../unit5-generative-ai-intro/README.md`.
