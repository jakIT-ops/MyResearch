# Introduction

 In this section of the course you will be writing a basic convolutional neural network (CNN) for handwritten digit recognition of the MNIST dataset. We will take an in-depth look at a model based off of Yann LeCun's [LeNet-5](http://yann.lecun.com/exdb/lenet/).

 ## A. Digit recognition

 When we start building an image recognition model for the first time, it’s usually a good idea to train and evaluate it on a relatively simple dataset. This allows for less complicated models, quicker training, and less image preprocessing. Basically, we want to learn the inner workings of a convolutional neural network before we even try to apply it to more complex tasks.

 One of the simplest tasks we can perform is handwritten digit recognition. Given an image of a handwritten digit (i.e., 0, 1, …, 9), we want our model to be able to correctly classify its numeric value. Though this task seems relatively simple, it is actually used fairly often in real life, such as automatically extracting credit card numbers from a picture. The dataset we will use for digit recognition is the MNIST dataset, which is the de facto dataset used for machine learning-based digit recognition.

## B. CNN dominance

 Nowadays, every task in the field of image recognition is dominated by convolutional neural networks (CNNs). Since the introduction of LeNet-5, the pioneering CNN, in 1998 for digit recognition, CNN architectures have become king in nearly all computer vision tasks. The CNN forms the backbone of many of today's cutting-edge technologies, such as self-driving cars, robotics, and facial recognition.

 Although CNNs dominate image related tasks, we could still theoretically use a multilayer perceptron model for classifying images. However, the MLP would not perform nearly as well as a CNN. So what exactly makes a CNN special for image input data? The key to the model's success is its convolutional layers, which is one of the main topics we'll discuss in the following chapters.


# 1. Initialization

## A. MNIST

The MNIST (Modified National Institute of Standards and Technology) database contains 60,000 training examples and 10,000 testing examples. The database contains grayscale handwritten digits that were resized to fit in a 20x20 pixel box, which was then centered in a 28x28 image (padded with whitespace). The images were resized using an anti-aliasing technique to minimize image distortion.

## B. Inputs and labels

Since each grayscale image has dimensions 28x28, there are 784 pixels per image. Therefore, each input image corresponds to a tensor of 784 normalized floating point values between 0.0 and 1.0. The label for an image is a one-hot tensor with 10 classes (each class represents a digit). In terms of our code, we have input_dim = 28 and output_size = 10 for the MNIST dataset.

When we use a batch of input data, the shape of inputs is (batch_size, self.input_dim**2) and the shape of labels is (batch_size, self.output_size), where batch_size represents the size of the batch.

The shape of inputs is (batch_size, self.input_dim**2) because there are batch_size images and each image is a square with a width of input_dim pixels.

```py
batch_size = 16
dataset = dataset.batch(batch_size)
it = tf.compat.v1.data.make_one_shot_iterator(dataset)
inputs, labels = it.get_next()
with tf.compat.v1.Session() as sess:
    # Batch of data size 16
    input_arr, label_arr = sess.run(
        (inputs, labels))
print(repr(input_arr))
```

# 2. Reshaping

## A. NHWC format

As mentioned in the previous chapter, inputs has shape (batch_size, self.input_dim**2). However, in order to use the data with our convolutional neural network, we need to get it into NHWC format.

NHWC format has a shape with four dimensions:

1. Number of image data samples (batch size)

2. Height of each image

3. Width of each image

4. Channels per image

The height and width of each image from the dataset is self.input_dim, while the number of channels is 1 (since the images are grayscale). The number of samples, i.e. batch size, is unspecified, since we allow for a variable number of input images.

## B. Reshaping the data

The function we use to reshape data in TensorFlow is tf.reshape. It takes in a tensor and a new shape as required arguments. The new shape must be able to contain all the elements from the input tensor. For example, we could reshape a tensor from original shape (5, 4, 2) to (4, 10), since both shapes contain 40 elements. However, we could not reshape that tensor to (3, 10, 2) or (1, 10), since those shapes contain 60 and 10 elements, respectively.

We are allowed to use the special value of -1 in at most one dimension of the new shape. The dimension with -1 will take on the value necessary to allow the new shape to contain all the elements of the tensor. Using the previous example, if we set a new shape of (1, 10, -1), then the third dimension will have size 4 in order to contain the 40 elements. Since the batch size of our input image data is unspecified, we use -1 for the first dimension when reshaping inputs.


```py
with tf.compat.v1.Session() as sess:
    input_arr = sess.run(inputs)
    reshaped_arr = sess.run(
        tf.reshape(inputs, [-1, 2, 2, 1])
    )
print(repr(input_arr))
print(repr(reshaped_arr))
```

# 3. Convolution

```py
import tensorflow as tf

class MNISTModel(object):
    # Model Initialization
    def __init__(self, input_dim, output_size):
        self.input_dim = input_dim
        self.output_size = output_size

    # CNN Layers
    def model_layers(self, inputs, is_training):
        reshaped_inputs = tf.reshape(
            inputs, [-1, self.input_dim, self.input_dim, 1])
        # CODE HERE
        conv1 = tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=[5, 5],
        padding='same',
        activation='relu',
        name='conv1')(reshaped_inputs)
```


# 4. Max Pooling

## A. Purpose of pooling

While the convolution layer extracts important hidden features, the number of features can still be pretty large. We can use pooling to reduce the size of the data in the height and width dimensions. This allows the model to perform fewer computations and ultimately train faster. It also prevents overfitting, by extracting only the most salient features and ignoring potential distortions or uncommon features found in only a few examples.

## B. How pooling works

Similar to a convolution, we use filter matrices in pooling. However, the pooling filter doesn't have any weights, nor does it perform matrix dot products. Instead, it applies a reduction operation to subsections of the input data.

The type of pooling that is usually used in CNNs is referred to as max pooling. The filters of max pooling use the max operation to obtain the maximum number in each submatrix of the input data.

## C. Padding

Similar to convolutions, we may want to pad our input data prior to pooling. We pad our data with a value dependent on the pooling operation. For example, in max pooling we pad each matrix with -∞. Since -∞ is smaller than every number, it allows us to resize the input data without adding any distortions when pooling.


```py
import tensorflow as tf

class MNISTModel(object):
    # Model Initialization
    def __init__(self, input_dim, output_size):
        self.input_dim = input_dim
        self.output_size = output_size

    # CNN Layers
    def model_layers(self, inputs, is_training):
        reshaped_inputs = tf.reshape(
            inputs, [-1, self.input_dim, self.input_dim, 1])
        # Convolutional Layer #1
        conv1 = tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=[5, 5],
        padding='same',
        activation='relu',
        name='conv1')(reshaped_inputs)
        # CODE HERE
        # Pooling Layer #1
        pool1 = tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2,
        name='pool1')(conv1)
```

# 5. Multiple Layers

## A. Adding extra layers

Like all neural networks, CNNs can benefit from additional layers. The additional layers allow a CNN to essentially stack multiple filters together for use on the image data. However, similar to building any neural network, we need to be careful of how many additional layers we add. If we add too many layers to a model, we run the risk of having it overfit to the training data and therefore generalizing very poorly. Furthermore, each additional layer adds computational complexity and increases training time for our model.

Since the MNIST images are pretty simple and only have one channel, we won't need more than one additional convolution and max pooling layer. However, in the next two sections of this course you will build CNNs for classifying much more complex images, necessitating the use of many more convolution layers.

## B. Increased filters

We usually increase the number of filters in a convolution layer the deeper it is in our model. In this case, our second convolution layer has 64 filters, compared to the 32 filters of the first convolution layer. The deeper the convolution layer, the more detailed the extracted features become. For example, the first convolution layer may have filters that extract features such as lines, edges, and curves. When we get to the second level, the filters of the convolution layer could now extract more distinguishing features, such as the sharp angle of a 7 or the intersecting curves of an 8.

```py
import tensorflow as tf

class MNISTModel(object):
    # Model Initialization
    def __init__(self, input_dim, output_size):
        self.input_dim = input_dim
        self.output_size = output_size

    # CNN Layers
    def model_layers(self, inputs, is_training):
        reshaped_inputs = tf.reshape(
            inputs, [-1, self.input_dim, self.input_dim, 1])
        # Convolutional Layer #1
        conv1 = tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=[5, 5],
        padding='same',
        activation='relu',
        name='conv1')(reshaped_inputs)

        # Pooling Layer #1
        pool1 = tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2,
        name='pool1')(conv1)
        # CODE HERE

        # Convolutional Layer #2
        conv2 = tf.keras.layers.Conv2D(
        filters=64,
        kernel_size=[5, 5],
        padding='same',
        activation='relu',
        name='conv1')(pool1)
        # Pooling Layer #2
        pool2 = tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2,
        name='pool2')(conv2)
```

# 6. Fully-Connected

## A. Fully-connected layer

We apply a fully-connected layer of size 1024 (i.e. the number of neurons in the layer) to the output data of the second pooling layer. The number of units is somewhat arbitrary. Enough to be powerful, but not so much as to be too resource intensive. The purpose of the fully-connected layer is to aggregate the data features before we convert them to logits. This allows the model to make better predictions than if we had just converted the pooling output directly to logits. We'll use those logits in a later chapter

## B. Flattening

The data we have been using in our model is of the NHWC format. However, in order to use a fully-connected layer, we need the data to be a matrix, where the number of rows represents the batch size and the columns represent the data features. Similar to how we reshaped our data in the Reshaping chapter, we'll use tf.reshape again. This time, though, we'll be reshaping in the opposite direction and converting from NHWC to a 2-D matrix.

Since the first dimension remains the batch size, we'll still use -1 when reshaping. To calculate the size of the second dimension (i.e. the total number of data features in pool2), we'll use the inherent shape property of tensors in TensorFlow. The shape property gives us a tf.TensorShape object, which we can convert to a list of integers using its as_list function.

```py
import tensorflow as tf

class MNISTModel(object):
    # Model Initialization
    def __init__(self, input_dim, output_size):
        self.input_dim = input_dim
        self.output_size = output_size

    # CNN Layers
    def model_layers(self, inputs, is_training):
        reshaped_inputs = tf.reshape(
            inputs, [-1, self.input_dim, self.input_dim, 1])
        # Convolutional Layer #1
        conv1 = tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=[5, 5],
        padding='same',
        activation='relu',
        name='conv1')(reshaped_inputs)

        # Pooling Layer #1
        pool1 = tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2,
        name='pool1')(conv1)
        # Convolutional Layer #2
        conv2 = tf.keras.layers.Conv2D(
        filters=64,
        kernel_size=[5, 5],
        padding='same',
        activation='relu',
        name='conv1')(pool1)
        # Pooling Layer #2
        pool2 = tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2,
        name='pool2')(conv2)
        # CODE HERE
        hwc = pool2.shape.as_list()[1:]
        flattened_size = hwc[0] * hwc[1] * hwc[2]
        pool2_flat = tf.reshape(pool2, [-1, flattened_size])
        dense = tf.keras.layers.Dense(
            1024, activation='relu', name='dense')(pool2_flat)
```

# 7. Logits

## A. Multiclass logits

Since there are 10 possible digits an MNIST image can be, we use a 10 neuron fully-connected layer to obtain the logits for each digit class. The logits are the output of the model_layers function.

The rest of the model follows the standard format for multiclass classification:

* Softmax applied to the logits to convert them into per class probabilities

* The labels are one-hot vectors, where the "hot index" corresponds to the digit in the MNIST image

* Softmax cross entropy to calculate loss

```py
import tensorflow as tf

class MNISTModel(object):
    # Model Initialization
    def __init__(self, input_dim, output_size):
        self.input_dim = input_dim
        self.output_size = output_size

    # CNN Layers
    def model_layers(self, inputs, is_training):
        reshaped_inputs = tf.reshape(
            inputs, [-1, self.input_dim, self.input_dim, 1])
        # Convolutional Layer #1
        conv1 = tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=[5, 5],
        padding='same',
        activation='relu',
        name='conv1')(reshaped_inputs)

        # Pooling Layer #1
        pool1 = tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2,
        name='pool1')(conv1)

        # Convolutional Layer #2
        conv2 = tf.keras.layers.Conv2D(
        filters=64,
        kernel_size=[5, 5],
        padding='same',
        activation='relu',
        name='conv1')(pool1)

        # Pooling Layer #2
        pool2 = tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2,
        name='pool2')(conv2)

        # Dense Layer
        hwc = pool2.shape.as_list()[1:]
        flattened_size = hwc[0] * hwc[1] * hwc[2]
        pool2_flat = tf.reshape(pool2, [-1, flattened_size])
        dense = tf.keras.layers.Dense(
            1024, activation='relu', name='dense')(pool2_flat)

        # Apply Dropout
        #dropout = tf.layers.dropout(
        dropout = tf.keras.layers.Dropout(rate=0.4)(dense, training=is_training)

        # CODE HERE
        logits = tf.keras.layers.Dense(self.output_size, name='logits')(dropout)
        return logits
```

# 8. Classification

### A. Model logistics

The run_model_setup function below shows how to set up and train the CNN we’ve coded:

```py
def run_model_setup(self, inputs, labels, is_training):
    logits = self.model_layers(inputs, is_training)

    # convert logits to probabilities with softmax activation
    self.probs = tf.nn.softmax(logits, name='probs')
    # round probabilities
    self.predictions = tf.math.argmax(
        self.probs, axis=-1, name='predictions')
    class_labels = tf.math.argmax(labels, axis=-1)
    # find which predictions were correct
    is_correct = tf.math.equal(
        self.predictions, class_labels)
    is_correct_float = tf.cast(
        is_correct,
        tf.float32)
    # compute ratio of correct to incorrect predictions
    self.accuracy = tf.math.reduce_mean(
        is_correct_float)
    # train model
    if self.is_training:
        labels_float = tf.cast(
            labels, tf.float32)
        # compute the loss using cross_entropy
        cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(
            labels=labels_float,
            logits=logits)
        self.loss = tf.math.reduce_mean(
            cross_entropy)
        # use adam to train model
        adam = tf.compat.v1.train.AdamOptimizer()
        self.train_op = adam.minimize(
            self.loss, global_step=self.global_step)
```

### B. Real data

After training a model on the MNIST dataset, it is ready to classify real hand-drawn digits. Using the techniques from the Image Processing section, we can decode the hand-drawn image to obtain its pixel data (in grayscale format) and then resize it to the same dimensions as the MNIST image data. Since our model inputs have shape (batch_size, input_dim**2), we flatten the image’s pixel data and reshape it to (1, input_dim**2).
