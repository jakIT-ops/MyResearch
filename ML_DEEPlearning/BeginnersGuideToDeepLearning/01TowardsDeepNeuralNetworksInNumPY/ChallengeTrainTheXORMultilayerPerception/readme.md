### Problem statement

We have learned that the XOR operator cannot be separated by a line. Therefore, a multilayer perceptron should be used. The following functions implementation is provided below:

* `forward_propagation` function

* `backpropagation` function

* `update_parameters` function

* `calculate_error` function

A train function receives the weights, the bias at the two layers respectively, and the losses array. Implement the train function using the batch update and return the updated value of parameters. Also, calculate the error in each epoch and store the losses array passed as an argument to the train function.

### Sample input

The train function takes the input X, labels Y, weights of the two layers w1 and w2, the bias of the two layers b1 and b2, learning_rate, num_iterations, and the losses array to compute the loss in each epoch.


```py
X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]]) # input array
Y = np.array([[0, 1, 1, 0]]) # output label
n_h = 2 # number of neurons in the hidden layer
n_x = X.shape[0] # number of neurons in the input layer
n_y = Y.shape[0] # number of neurons in the output layer
W1 = np.random.randn(n_h, n_x) # weights from the input layer
b1 = np.zeros((n_h, 1)) # bias in the hidden layer
W2 = np.random.randn(n_y, n_h) # weights from the hidden layer
b2 = np.zeros((n_y, 1)) # bias in the output layer

num_iterations = 100000
learning_rate = 0.01
losses = np.zeros((num_iterations, 1))
```

### Sample output

The updated weights of W1 and W2 and the bias at the two layers b1 and b2 along with the loss value in each epoch.

```py
W1:
[[5.65443604 5.65156882]
 [7.49953724 7.48402719]]
b1:
 [[-8.64595499]
 [-3.43532706]]
W2:
 [[-13.81590639  13.0105674 ]]
b2:
 [[-6.09446339]]
loss:
 [[2.82611902]
 [2.82434768]
 [2.82263898]
 ...
 [0.01063611]
 [0.01063599]
 [0.01063587]]
```
