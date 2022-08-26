# 1. Introduction to Transfer Learning

### What is transfer learning?

We humans have an inherent ability to transfer our knowledge across different tasks. The knowledge that we as humans acquire while learning to perform one task is utilized while learning to solve other related tasks. The more related the tasks, the easier it is for us to transfer, or cross-utilize, our knowledge. Let’s further understand this with the help of these examples:

* If you know how to ride a motorbike, then you can learn how to drive a car.
* If you know math and statistics', then you can learn machine learning.
* If you know how to play classic piano, then you can learn how to play jazz piano.


### Examples of transfer learning

Let’s discuss some of the examples of transfer learning.

#### Transfer learning in vision (image data)

In computer vision, you deal with image or video data. It is very common to use deep learning models when working with these types of data. Generally, people do not train the networks from scratch for their use case; instead, they use a deep learning model that is pre-trained for a large and challenging image classification task such as the ImageNet 1000-class photograph classification competition.

The researchers who developed the models for this type of competition released the final models’ weights so that they can be used under a permissive license.

Some of the models are:

* Oxford VGG Model
* Google Inception Model
* Microsoft ResNet Model

#### Transfer learning in NLP (text data)

In Natural Language Processing, you deal with text data as input or output. In these types of problems, word embedding is used. Word embedding is the mapping of words to a high-dimensional continuous vector space where different words with similar meanings have a similar vector representation.

The researchers who developed the models and trained them on a very large corpus of text released the models under a permissive license.

Some of the Pre-Trained models are :

* Google’s word2vec Model
* Stanford’s GloVe Model

# 2. Assignment

## Assignments

We ask that you take these tasks seriously, as they will help you develop an in-depth understanding. We have two tasks for you:

* Change the hyperparameters, the number of layers in our classifier, and the number of layers up to which we want to freeze the weight update process and see what the accuracy of the model is. How does it change?

* We used the ResNet50 model here. Your task is to use the MobileNet and AlexNet pre-trained models and build a classifier on the same dataset. You may also use any other image classification dataset. If you are able to complete the above mentioned tasks and assignments, then you have acquired a good command of this topic. You can now go ahead to the next chapter.

### Problem One

Change the hyperparameters, the number of layers in our classifier, and the number of layers up to which we want to freeze the weight update process and see what the accuracy of the model is. How does it change?

We will only change the model architecture here but you can even change the epochs, the number of parameters to freeze for the training process, etc.

```py
# The ResNet50 model's output is going to be connected to this classifier.

av1 = GlobalAveragePooling2D()(model.output)

fc1 = Dense(256, activation = 'relu')(av1)

d1 = Dropout(0.5)(fc1)

fc2 = Dense(128, activation = 'relu')(d1)

d2 = Dropout(0.5)(fc2)

fc3 = Dense(64, activation = 'relu')(d2)

d3 = Dropout(0.5)(fc3)

fc4 = Dense(10, activation = 'softmax')(d3)
```

Explanation:

* We just added some more `Dense()` layers in our classifier architecture. Obviously, it will increase the number of parameters to train and, eventually, the time taken to train the model but it can give better accuracy as compared to the architecture used in our previous lessons.

We get an accuracy rise of 5% with this architecture. You can perform the changes per your choice and look to obtain more accuracy.

### Problem two

We used the ResNet50 model here. Your task is to use the MobileNet and AlexNet pre-trained model and build a classifier on the same dataset. You may also use any other image classification dataset.

Below is the code snippet of the MobileNet model.

```py
# Import the required libraries
from tensorflow.python.keras.applications import MobileNet

# Load the MobileNet model
mobile_net_model = MobileNet(include_top=False, weights='imagenet', input_shape = (224,224,3))
mobile_net_model.summary()

# Create the classifier and connect it to the MobileNet model
av1 = GlobalAveragePooling2D()(mobile_net_model.output)
fc1 = Dense(256, activation = 'relu')(av1)
d1 = Dropout(0.5)(fc1)
fc2 = Dense(128, activation = 'relu')(d1)
d2 = Dropout(0.5)(fc2)
fc3 = Dense(64, activation = 'relu')(d2)
d3 = Dropout(0.5)(fc3)
fc4 = Dense(10, activation = 'softmax')(d3)
mobile_net_final_model = Model(inputs = mobile_net_model.input, outputs = fc4)
mobile_net_final_model.summary()

# Compile the model
adam = Adam(lr = 0.00003)
mobile_net_final_model.compile(loss = 'categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])

# Freeze the training process for the first 50 layers of MobileNet model
for ix in range(50):
    mobile_net_final_model.layers[ix].trainable = False
print(mobile_net_final_model.summary())

# Train the model
hist = mobile_net_final_model.fit(X_train, Y_train, shuffle = True, batch_size = 16, epochs = 8, validation_split = 0.20)
```

`Explanation:`

* On line 2, we imported the MobileNet model.

* On line 5, we loaded the MobileNet model using the imagenet weights.
From line 9 to 18, we connected the MobileNet model and our classifier on top of that.

* On line 22, we compiled our combined model.

* From line 25 to 27, we froze the training process for the first 50 layers in the combined model.

* On line 30, we performed the training process.


You can expect an accuracy of around 70%. You can increase the accuracy by tweaking the architecture and the hyperparameters.

Now let’s have a look at the prediction using our MobileNet model.

```py
from tensorflow.python.keras.applications.mobilenet import preprocess_input

image_path = 'Dataset/Pikachu/00000098.jpg'
img = image.load_img(image_path,target_size = (224,224))
x = image.img_to_array(img)
x = np.expand_dims(x,axis=0)
x = preprocess_input(x)

pred = mobile_net_final_model.predict(x)
print(np.argmax(pred))
```

`Explanation:`

* On line 1, we imported the preprocess_input() function for the MobileNet model.

* All the remaining steps are the same as we discussed above.

* On line 10, we got the integer corresponding to a particular Pokemon.
