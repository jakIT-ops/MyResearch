import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    """Compute sigmoid values for each sets of scores in x"""
    return 1 / (1 + np.exp(-z))

def softmax(x):
    """Compute softmax values for each sets of scores in x"""
    return np.exp(x) / np.sum(np.exp(x), axis=1)

def forward_propagation(x, w1, w2, w3, b1, b2, b3):
   """
    Computes the forward propagation operation for the 3-layered
    neural network and returns the output at the 2 hidden layers
    and the output layer
   """
   net_h1 = np.dot(x, w1) + b1 # net output at the first hidden layer
   out_h1 = sigmoid(net_h1) # applying the sigmoid activation to the first hidden layer net output
   net_h2 = np.dot(out_h1, w2) + b2 # net output at the second hidden layer
   out_h2 = sigmoid(net_h2) # applying the sigmoid activation to the second hidden layer net output
   net_y = np.dot(out_h2, w3) + b3 # net output of the output layer
   out_y = softmax(net_y) # applying the softmax activation to the net output of output layer
   return out_h1, out_h2, out_y

# Creating data set
# A
a = [0, 0, 1, 1, 0, 0,
   0, 1, 0, 0, 1, 0,
   1, 1, 1, 1, 1, 1,
   1, 0, 0, 0, 0, 1,
   1, 0, 0, 0, 0, 1]

# B
b =[0, 1, 1, 1, 1, 0,
   0, 1, 0, 0, 1, 0,
   0, 1, 1, 1, 1, 0,
   0, 1, 0, 0, 1, 0,
   0, 1, 1, 1, 1, 0]
# C
c =[0, 1, 1, 1, 1, 0,
   0, 1, 0, 0, 0, 0,
   0, 1, 0, 0, 0, 0,
   0, 1, 0, 0, 0, 0,
   0, 1, 1, 1, 1, 0]

# Creating labels
y =[[1, 0, 0],
   [0, 1, 0],
   [0, 0, 1]]

# converting data and labels into numpy array
x = np.array([a, b, c])
# Labels are also converted into NumPy array
y = np.array(y)

np.random.seed(42) # seed function to generate the same random value
n_x = 30
n_h1 = 5
n_h2 = 4
n_y = 3
w1 = np.random.randn(n_x, n_h1)
w2 = np.random.randn(n_h1, n_h2)
w3 = np.random.randn(n_h2, n_y)
b1 = np.zeros((1, n_h1))
b2 = np.zeros((1, n_h2))
b3 = np.zeros((1, n_y))
out_h1, out_h2, out_y = forward_propagation(x, w1, w2, w3, b1, b2, b3)
print("First Hidden layer output:\n", out_h1)
print("Second Hidden layer output:\n", out_h2)
print("Output layer:\n", out_y)
