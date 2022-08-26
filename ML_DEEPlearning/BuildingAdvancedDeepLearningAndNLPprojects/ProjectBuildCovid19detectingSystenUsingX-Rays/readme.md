# 1. Introduction to Convolutional Neural Networks

### How does the human brain read an image?

To understand CNNs, we must understand how our own human brain works or, more specifically, how it reads an image. Our brain depends on detecting features and categorizing the objects we see accordingly. You must have been in a situation where once you saw an image, you perceived it to be something, and, then, after looking at it again more thoroughly, you judged or perceived the image in a different manner.

### How does a CNN work?

There are three elements involved when we work with CNNs:

* Input image

* Convolutional Neural Network

* Output (classified image class)

Here, the CNN works in four steps, which are discussed further in the latter part of the chapter.

* Convolution - the first building block is the convolution operation. In this step, we will discuss the feature detectors, which basically serve as the neural network’s filters. We will also discuss how these filters are learned by the network.

* Pooling - in this lesson, we’ll cover pooling, and you will learn exactly how it works. Our focus, however, will be on a specific type of pooling i.e. max pooling. However, there are some different poolings available and we will be discussing them in the next chapter.

* Flattening - in this lesson, we will discuss how flattening works and creates an output that converts your input to a vector.

* Full Connection - in this lesson, we will see how all of these steps are merged together and how the final predictions are done.

# 2. Assignment

## Problem one

Train a CNN on any other image dataset. You can download a very popular dog vs cat dataset [here](https://www.kaggle.com/datasets/tongpython/cat-and-dog).

Let us first see how you can load any dataset from Kaggle in your Google Colab for faster and easier computations.

```py
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.layers import *
from tensorflow.python.keras.models import *

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation="relu",input_shape=(224,224,3)))
model.add(Conv2D(64, kernel_size=(3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(128, kernel_size=(3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(256, kernel_size=(3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(32, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam",metrics = ["accuracy"])
model.summary()

train_datagen = image.ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = image.ImageDataGenerator(rescale = 1./255)

train_generator = train_datagen.flow_from_directory('training_set/training_set/',target_size=(224,224),batch_size=32, class_mode="binary")
val_generator = test_datagen.flow_from_directory('test_set/test_set/',target_size=(224,224),batch_size=32, class_mode="binary")

hist = model.fit(train_generator, epochs = 80, validation_data=val_generator)
```

`Explanation`:

* We used almost the same code to perform this task.

* The model architecture has been changed a bit and made deeper with (more convolutional layers).

* You can expect an accuracy of around 80%.

## Problem two

Create one more CNN model on any other dataset and try to find a multi-class image dataset. You just need to change the number of output nodes and the activation function in the final output layer of the network.

Let’s use a food image classification dataset. This dataset contains various types of food images. You can download the dataset [here](https://www.kaggle.com/datasets/trolukovich/food11-image-dataset).

```py
# Import the required libraries
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.layers import *
from tensorflow.python.keras.models import *

# Create the model architecture
classifier = Sequential()
classifier.add(Convolution2D(32,(3,3),input_shape = (64,64,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Convolution2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Convolution2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Convolution2D(16, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Flatten())
classifier.add(Dense(128 , activation='relu'))
classifier.add(Dense(11 , activation = 'softmax'))

# Compile the model
classifier.compile(loss="binary_crossentropy", optimizer="adam",metrics = ["accuracy"])
classifier.summary()

# Create the Data Generator Objects
train_datagen = image.ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = image.ImageDataGenerator(rescale = 1./255)

# Generate the dataset
train_generator = train_datagen.flow_from_directory('training/',target_size=(64,64),batch_size=32, class_mode="binary")
val_generator = test_datagen.flow_from_directory('validation/',target_size=(64,64),batch_size=32, class_mode="binary")

# Train the model
hist = classifier.fit(train_generator, epochs = 80, validation_data=val_generator)
```

`Explanation`:

* Again, we have not used anything new that needs explanation.
* We changed the size of the image to 64 x 64 for faster computations.
* We changed the model architecture a bit and that’s it.
* You can expect an accuracy of around 75%. But of course, you can tweak the hyperparameters to achieve even greater accuracy.
