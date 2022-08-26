* When working with new data, or building a new workflow, it is good practice to preview the data to ensure it was loaded and transformed properly.

* PyTorch can do a lot of the work in a machine learning task for us. To take advantage of this, we need to work with PyTorch’s machinery. For example, neural networks should be derived from PyTorch’s nn.Module class.

* It is good practice to visualize loss values so we can see how well training went.

* The mean squared error loss is suited to regression tasks where the output can be in a continuous range. The binary cross entropy loss is better suited to classification tasks where the output should be 1 or 0, for true and false.

* The traditional sigmoid activation function suffers from vanishing gradients for large input values. This leads to poor feedback signals for training a network. The ReLU activation function solves this by having good gradients for positive inputs. The LeakyReLU improves this by also having a small non-zero gradient for negative values.

* The Adam optimizer uses momentum to overcome local minima and maintains individual learning rates for each learnable parameter. For many tasks, it performs better than the simple SGD optimizer.

* Normalization can stabilize the training of neural networks. It is common to normalize a network’s initial weights. Normalizing signal values as they pass through a neural network with LayerNorm can improve performance.
