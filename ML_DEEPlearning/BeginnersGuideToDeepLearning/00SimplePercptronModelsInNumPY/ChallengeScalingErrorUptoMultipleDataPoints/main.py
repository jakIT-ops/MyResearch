import numpy as np
def sigmoid(x):
    """The sigmoid activation function"""
    return 1 / (1 + np.exp(-x))

def forward_propagation(input_data, weights, bias):
   """
    Computes the forward propagation operation of a perceptron and
    returns the output after applying the sigmoid activation function
   """
   # take the dot product of input and weight and add the bias
   return sigmoid(np.dot(input_data, weights) + bias)

def calculate_error(y, y_predicted):
   """Computes the binary cross entropy error"""
   return - y * np.log(y_predicted) - (1 - y) * np.log(1 - y_predicted)

def ce_two_different_weights(X, Y, weights_0, weights_1, bias):
    """Computes sum of error using two different weights and the same bias"""
    sum_error1 = 0.0
    sum_error2 = 0.0
    for j in range(len(X)):
        Y_predicted_1 = forward_propagation(X[j], weights_0.T, bias) # predicted label
        sum_error1 = sum_error1 + calculate_error (Y[j], Y_predicted_1) # sum of error with weights_0
        Y_predicted_2 = forward_propagation(X[j], weights_1.T, bias) # predicted label
        sum_error2 = sum_error2 + calculate_error (Y[j], Y_predicted_2) # sum of error with weights_1
    return sum_error1, sum_error2


# Initialize parameters
X = np.array([[2, 3], [1, 4], [-1, -3], [-4, -5]]) # declaring two data points
Y = np.array([1.0, 1.0, 0.0, 0.0]) # actual label
weights_0 = np.array([0.0, 0.0]) # weights of perceptron
weights_1 = np.array([1.0, -1.0]) # weights of perceptron
bias = 0.0 # bias value
sum_error1, sum_error2 = ce_two_different_weights(X, Y, weights_0, weights_1, bias)
print("sum_error1:", sum_error1, "sum_error2:", sum_error2)
