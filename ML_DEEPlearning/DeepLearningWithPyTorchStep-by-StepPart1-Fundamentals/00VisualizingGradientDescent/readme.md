* Defining a simple linear regression model.

* Generating synthetic data for it.

* Performing a train-validation split on our dataset.

* Randomly initializing the parameters of our model.

* Performing a forward pass; that is, making predictions using our model.

* Computing the errors associated with our predictions.

* Aggregating the errors into a loss (MSE).

* Learning that the number of points used to compute the loss defines the kind of gradient descent we’re using: batch (all), mini-batch, or stochastic (1).

* Visualizing an example of a loss surface and using its cross-sections to get the loss curves for individual parameters.

* Learning that a gradient is a partial derivative, and it represents how much the loss changes if one parameter changes a little bit.

* Computing the gradients for our model’s parameters using equations, code, and geometry.
 
* Learning that larger gradients correspond to steeper loss curves.

* Learning that backpropagation is nothing more than “chained” gradient descent.

* Using the gradients and a learning rate to update the parameters.

* Comparing the effects on the loss of using small, big, and very big learning rates.

* Learning that loss curves for all parameters should be, ideally, similarly steep.

* Visualizing the effects of using a feature with a larger range, making the loss curve for the corresponding parameter much steeper.

* Using Scikit Learn’s StandardScaler to bring a feature to a reasonable range, and thus making the loss surface more bowl-shaped and its cross-sections similarly steep.

* Learning that preprocessing steps like scaling should be applied after the train-validation split to prevent leakage.

* Figuring that performing all steps (forward pass, loss, gradients, and parameter update) makes one epoch.

* Visualizing the path of gradient descent over many epochs and realizing it is heavily dependent on the kind of gradient descent used: batch, mini-batch, or stochastic.

* Learning that there is a trade-off between the stable and smooth path of batch gradient descent and the fast and somewhat chaotic path of stochastic gradient descent, making the use of mini-batch gradient descent a good compromise between the other two.