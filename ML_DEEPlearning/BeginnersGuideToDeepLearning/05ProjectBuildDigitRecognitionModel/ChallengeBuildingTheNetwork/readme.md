### Problem statement

The preprocessed MNIST dataset has been provided. Specify the network architecture, compile, fit, and evaluate the model performance on the training data.

* The model architecture should have 2 hidden layers with 60 and 60 nodes respectively and an output layer. The activation function for the first hidden layer should be relu and it should be sigmoid for the second hidden layer. The activation function for the output layer should be softmax.

* The model should be compiled with adam as an optimizer.

* The model should fit on the training data with 5 epochs and batch_size equal to 128.

* Evaluate the model on the training data and check its accuracy.

### Sample input

The preprocessed MNIST data is provided with:

* Training features: X_train
* Training labels: Y_train
* Testing features: X_train
* Testing labels: Y_train

### Sample output

The trained model accuracy after defining the model architecture, the compile method, the fit method, and the evaluation model.
