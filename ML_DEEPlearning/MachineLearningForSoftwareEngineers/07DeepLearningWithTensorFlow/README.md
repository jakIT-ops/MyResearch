# 1. Introduction

### A. Multilayer perception

The multilayer perceptron (MLP) is used for a variety of tasks, such as stock analysis, spam detection, and election voting predictions. In the following chapters you will learn how to code your own MLP and apply it to the task of classifying 2-D points in the Cartesian plane.

* Input layer: The first (bottom) layer.
* Output layer: The last (top) layer.
* Hidden layer(s): The layer(s) between the input and output layers. In the diagram, there is 1.

The number of hidden layers represents how "deep" a model is, and you'll see the power of adding hidden layers to a model.

### B. TensorFlow

To code our neural network model, we will be using TensorFlow, one of the most popular deep learning frameworks. The name for TensorFlow is derived from tensors, which are basically multidimensional (i.e. generalized) vectors/matrices. When writing the code, it may be easier to think of anything with numeric values as being a tensor.

In TensorFlow, we first create the computation graph structure (which we will do in chapters 2-5), and then train and evaluate the model with input data and labels.

# 2. Model Initialization

### A. Placeholder

When building the computation graph of our model, tf.compat.v1.placeholder acts as a "placeholder" for the input data and labels. Without the tf.compat.v1.placeholder, we would not be able to train our model on real input data.

### B. Shapes and dimensions

The shape argument is a tuple of integers representing the size of each of the placeholder tensor's dimensions. In Deep Learning with TensorFlow, and many real world problems, the shape of the input data will be a two integer tuple. If we view the input data as coming from a data table, the shape is akin to the dimensions of the table.

### C. Different amounts of data 

One thing to note about TensorFlow is the use of None in place of a dimension size. When we use None in the shape tuple, we are allowing that dimension to take on any size.

# 3. Logits

### A. Fully-connected layer 

Before we can get into multilayer perceptrons, we need to start off with a single layer perceptron. The single fully-connected layer means that the input layer, i.e. self.inputs, is directly connected to the output layer, which has output_size neurons. Each of the input_size neurons in the input layer has a connection to each neuron in the output layer, hence the fully-connected layer.

### B. Weighted connections

The forces that drive a neural network are the real number weights attached to each connection. The weight on a connection from neuron A into neuron B tells how strongly A affects B as well as whether that effect is positive or negative, i.e. direct vs. inverse relationship.

A → B: Direct relationship.
A → C: No relationship.
A → D: Inverse relationship.


### C. Logits

So what exactly are logits? In classification problems they represent log-odds, which maps a probability between 0 and 1 to a real number. When output_size = 1, our model outputs a single logit per data point. The logits will then be converted to probabilities representing how likely it is for the data point to be labeled 1 (as opposed to 0).

### D. Regression

In the next chapter, you'll be producing actual probabilities from the logits. This makes our single layer perceptron model equivalent to logistic regression. Despite the name, logistic regression is used for classification, not regression problems. If we wanted a model for regression problems (i.e. predicting a real number such as a stock price), we would have our model directly output the logits rather than convert them to probabilities. In this case, it would be better to rename logits, since they don't map to a probability anymore.

# 4. Metrics

### A. Sigmoid

As discussed in the previous chapter, our model outputs logits based on the input data. These logits represent real number mappings from probabilities. Therefore, if we had the inverse mapping we could obtain the original probabilities. Luckily, we have exactly that, in the form of the sigmoid function.

### B. Predictions and accuracy

A probability closer to 1 means the model is more sure that the label is 1, while a probability closer to 0 means the model is more sure that the label is 0. Therefore, we can obtain model predictions just by rounding each probability to the nearest integer, which would be 0 or 1. Then our prediction accuracy would be the number of correct predictions divided by the number of labels.

In TensorFlow, there is a function called tf.math.reduce_mean which produces the overall mean of a tensor's numeric values. We can use this to calculate prediction accuracy as the mean number of correct predictions across all input data points.

# 5. Optimization 

### What is training

For any neural network, training involves setting up a loss function. The loss function tells us how bad the neural network's output is compared to the actual labels.

Since a larger loss means a worse model, we want to train the model to output values that minimize the loss function. The model does this by learning the optimal weight settings. Remember, the weights are just real numbers, so the model is essentially just figuring out the best numbers to set the weights to.

### B. Loss as error

In classification problems there's no good error measurement between predictions and labels, since the labels are discrete values. For example, in regression if we predict a stock's price was $99 but the actual value was $100, our prediction is still really good even though it was incorrect. However, in classification a prediction is either right or wrong, without any sense of how close it is to the actual label.

### C. Cross entropy

Rather than defining error as being right or wrong in our prediction, we can instead define it in terms of probability. Therefore, we want a loss function that is small when the probability is close to the label (i.e. a probability of 0.99 for a label of 1) and large when the probability is far from the label (i.e. a probability of 0.99 for a label of 0). The loss function that achieves this is known as cross entropy, also referred to as log loss.

### D. Optimization 

Now we can just minimize the cross entropy based on the model's logits and labels to get our optimal weights. We do this through gradient descent, where the model updates its weights based on a gradient of the loss function until it reaches the minimum loss (at which point the weights converge to the optimum). We use backpropagation to find the optimal gradient for the model to follow. Gradient descent is implemented as an object in TensorFlow, called tf.compat.v1.train.GradientDescentOptimizer.

# 6. Training

### A. Running the model

The tf.compat.v1.Session object has an extremely important function called run. All the code written in the previous chapters was to build the computation graph of the neural network, i.e. its layers and operations. However, we can only train or evaluate the model on real input data using run. The function takes in a single required argument and a few keyword arguments.

### B. Using run

The required argument is normally either a single tensor/operation or a list/tuple of tensors and operations. Calling run on a tensor returns the value of that tensor after executing our computation graph. The output of run with a tensor input is a NumPy array.

```py
with tf.compat.v1.Session() as sess:
    t = tf.constant([1, 2, 3])
    arr = sess.run(t)
    print('{}\n'.format(repr(arr)))

    t2 = tf.constant(4)
    tup = sess.run((t, t2))
    print('{}\n'.format(repr(tup)))
```

### C. Initializing variables

```py
When we call run, every tensor in the model's computation graph must either already have a value or must be fed in a value through feed_dict. However, when we start training from scratch, none of our variables (e.g. weights) have values yet. We need to initialize all the variables using tf.compat.v1.global_variables_initializer. This returns an operation that, when used as the required argument in run, initializes all the variables in the model.
```

```py
with tf.compat.v1.Session() as sess:
  inputs = tf.compat.v1.placeholder(tf.float32, shape=(None, 2))
  feed_dict = {
    inputs: [[1.1, -0.3],
            [0.2, 0.1]]
  }
  logits = tf.keras.layers.Dense(units=1, name='logits')(inputs)
  init_op = tf.compat.v1.global_variables_initializer()
  sess.run(init_op) # variable initialization
  arr = sess.run(logits, feed_dict=feed_dict)
  print('{}\n'.format(repr(arr)))
```

### D. Training logistics

```py
# predefined dataset
print('Input data:')
print('{}\n'.format(repr(input_data)))

print('Labels:')
print('{}\n'.format(repr(input_labels)))
```






































































