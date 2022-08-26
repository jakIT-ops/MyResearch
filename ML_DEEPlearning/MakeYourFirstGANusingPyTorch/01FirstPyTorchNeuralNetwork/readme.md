## MNIST Image Dataset

The MNIST dataset is a well-known set of images often used to measure and compare the performance of machine learning algorithms. It contains 60,000 images to be used for training a machine learning model, and 10,000 images for testing its performance.

The images are 28 by 28 pixels in size, and are monochrome, not colour. The pixels have a numerical value for how light or dark that pixel is and, depending on where you get the data from, the values will be in the range 0 - 255.

> Exercise: Experiment with other images from the dataset by changing the row value and running the cell again. For example, if you try row = 13, you should see an image that looks like a six.

## Learning Points in First PyTorch Neural Network

* The MNIST dataset is a well-known set of images often used to measure and compare the performance of machine learning algorithms. It contains 60,000 images for training a machine learning model, and 10,000 images for testing its performance.

* The MNIST image is 28 by 28, or 784 pixel values. That means the first layer of our neural network must have 784 nodes. We have defined a hidden layer with 200 nodes. The outer layer has 10 nodes, i.e., one node for each of these 10 possible classes.

* The neural network class Classifier is defined using PyTorch’s torch.nn library. The class contains:

    * The neural network architecture.
    * The forward function to perform forward propagation.
    * The train function to optimize network weights during back propagation.
    * The plot_progress function to visualize loss during training.

* The MNIST Dataset class contains functions to load and use data in the PyTorch way.

    * The __len__() function simply returns the length of the dataframe.
    * The __getitem__() function extracts a label from the index-th item in the dataset.
    * The plot_image() function plots the image.

* Training the classifier involves:

    * Creating an object of the neural network Classifier class.

    * Running the train function through every record of the sample epoch times.

* The performance of the network can be tested by using the unseen test data sample and calling a forward function of the neural network class.

* If we want to know how well our classifier performed it has to work through all the 10,000 images in the MNIST test dataset and keep a count of how many it got right.
