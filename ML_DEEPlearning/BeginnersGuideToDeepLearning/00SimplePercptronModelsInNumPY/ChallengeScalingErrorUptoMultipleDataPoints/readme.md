### Problem statement

We have seen how different weights will have different accuracies on a single prediction. Usually, we want to measure model accuracy on many points. Now, write code to compare model accuracies for two different sets of weights which have been stored as `weights_0` and `weights_1`.

`X` is a NumPy array with different inputs and `Y` is the label. Loop over the training samples and calculate the error on multiple data points.

### Sample input

Below is the sample input, i.e., the input features X, weights (weights_0, and weights_1), and the bias value:
```py
X = np.array([[2, 3], [1, 4], [-1, -3], [-4, -5]])
weights_0 = np.array([0.0, 0.0])
weights_1 = np.array([1.0, -1.0])
bias = 0.1
Y = np.array([1.0, 1.0, 0.0, 0.0])
```

### Sample output

The cross-entropy error in case of the weights_0 and weights_1 respectively:

```py
2.7775866402942837, 7.797571499245237
```
