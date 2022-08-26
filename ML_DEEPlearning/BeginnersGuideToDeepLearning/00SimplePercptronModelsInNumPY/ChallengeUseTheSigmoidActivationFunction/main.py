import numpy as np
def sigmoid(x):
  """
  The sigmoid activation function
  """
  return 1 / (1 + np.exp(-x)) # applying the sigmoid function

def forward_propagation(input_data, weights, bias):
  """
  Computes the forward propagation operation of a perceptron and
  returns the output after applying the sigmoid activation function
  """
  # take the dot product of input and weight and add the bias
  return sigmoid(np.dot(input_data, weights) + bias) # the perceptron equation

# Initializing parameters
X = np.array([2, 3]) # declaring two data points
Y = np.array([0]) # label
weights = np.array([2.0, 3.0]) # weights of perceptron
bias = 0.1 # bias value
output = forward_propagation(X, weights.T, bias) # predicted label
print("Forward propagation output:", output)

Y_predicted = (output > 0.5) * 1 ## apply sigmoid activation
print("Label:", Y_predicted)
