# Introduction

## A. Memory Usage

While we’re normally concerned with model accuracy, the amount of memory a model uses is important as well. After training a model, we store its computation graph and parameters (weights + biases) for future use. Though a model’s computation graph is relatively small (since even large models won’t have more than a couple hundred layers), the number of parameters a model has can be in the millions.

Most high performance models require hundreds of MB of space to store their parameters. The aforementioned AlexNet uses over 200MB for storage of 60 million parameters. On the other hand, the SqueezeNet model architecture uses less than 1MB. That’s even less memory than the simple digit recognition model we built in the previous chapter (13MB). However, SqueezeNet has significantly better performance than our previous model and actually matches AlexNet in accuracy.


## B. Calculating parameters

To understand model sizes, we need to be able to calculate the number of parameters in a model.


## C. SqueezeNet

There are quite a few benefits of using a smaller model such as SqueezeNet. First, it takes less time to train and load a smaller model. When performance is comparable, it is preferable to use a model that takes less time to train and set up.

Furthermore, when memory usage is limited, it may not even be possible to store a large model. For example, if you’re working in an environment with a limited disk quota (such as a Linux container), storing a large model may exceed the memory limit. This problem is especially prevalent when we are storing multiple variations of a large model (which is often the case during training and experimentation). However, this would not be an issue with a model based on the SqueezeNet architecture.

# 1. Initialization

## A. CIFAR-10

The CIFAR-10 (Canadian Institute for Advanced Research) dataset contains 60,000 color images with dimensions 32x32. The images are distributed evenly across 10 categories: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck. We split the dataset into 50,000 images for training and 10,000 images for testing.

The CIFAR-10 dataset is available for download (along with the 100 category version, CIFAR-100), on Alex Krizhevsky's [website](https://www.cs.toronto.edu/~kriz/cifar.html).

## B. Inputs and labels

Each image has dimensions 32x32, meaning original_dim will be 32 for the CIFAR-10 dataset. The images have color, so they follow the RGB format, meaning each pixel contains three integers (one each for the red, blue, and green channels). In total, an image is represented by

```py
import tensorflow as tf

class SqueezeNetModel(object):
    # Model Initialization
    def __init__(self, original_dim, resize_dim, output_size):
    self.original_dim = original_dim
    self.resize_dim = resize_dim
    self.output_size = output_size
```
