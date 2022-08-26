# 1. Introduction to Recurrent Neural Networks

## What are Recurrent Neural Networks?

We already discussed Convolutional Neural Networks in previous chapters. They were mainly used for computer vision applications. But what happens if the input data is a sequence of text or numbers? To deal with these types of data (sequence-based data), we have a special type of neural network: a Recurrent Neural Network.

Let’s look at an example that explains why an Artificial Neural Network of a Multi-layer Perceptron is not suitable for the sequential data.

We have a Multi-layer Perceptron model which tries to give a rating from 1 to 5 for a particular movie review. For the review, “This is a great movie”, our MLP model predicts a rating of 4. On the other hand, for the review “This is not a good movie”, the MLP model again predicts a rating of 4 (which is wrong). This happens because a Multi-layer Perceptron is not capable of remembering past information and, thus, treats each word as an independent entity.

Therefore, we need sequence models (RNNs), that can process information from left to right (like humans) and maintain what has been read so far (which is what happens in the human brain). RNNs are designed to recognize the sequential characteristics of data and use trends to predict the next probable scenario. While RNNs learn similar to feed-forward neural networks while training, they also remember things learned from prior input(s) while generating output(s). Also, CNNs and ANNs are stateless.

## Architecture of an RNN

RNNs can take one or more input vectors and generate one or more output vectors, and the output(s) is(are) determined not only by weights applied to inputs such as a standard NN but also by a “hidden” state vector, representing meaning based on input(s)/output(s) beforehand. Therefore, the same input may generate a different output depending on the series’ previous inputs.

## Application of RNNs

* Sentiment analysis

* Text summarization

* Machine translation

* Image captioning

Apart from that, you can check out the movie, [Sunspring](https://arstechnica.com/gaming/2021/05/an-ai-wrote-this-movie-and-its-strangely-moving/). You can see how powerful the RNNs are, but you can also see that they have a huge problem. Let’s discuss that problem now.

## Types of RNN Architectures

* One to one (non-sequential)

* One to many

* Many to one

* Many to many

* Encoder-decoder

## Supporting reading materials

1. Please check out this movie, called [Sunspring](https://arstechnica.com/gaming/2021/05/an-ai-wrote-this-movie-and-its-strangely-moving/) (2016). It is a movie written by an algorithm which turns out to be hilarious and intense. Once you watch it, you will have a sense of what AI can do.

2. [Learning long-term dependencies with gradient descent is difficult](http://www.iro.umontreal.ca/~lisa/pointeurs/ieeetrnn94.pdf) by Yoshua Bengio et al. (1994). This paper shows why gradient-based learning algorithms face an increasingly difficult problem as the duration of dependencies increases.

3. [On the difficulty of training recurrent neural networks](http://proceedings.mlr.press/v28/pascanu13.pdf) by Razvan Pascanu et al. (2013). This paper shows an attempt to improve the understanding of the underlying issues by exploring the two problems that RNNs face (vanishing gradient and exploding gradient) from an analytical, a geometric, and a dynamical systems perspective. They proposed a gradient norm clipping strategy to deal with exploding gradients and a soft constraint for the vanishing gradients problem.

4. [Long Short-Term Memory](http://www.bioinf.jku.at/publications/older/2604.pdf) by Sepp Hochreiter and Jurgen Schmidhuber (1997). This paper discusses the way in which LSTMs work and solves the problems of a standard RNN architecture.

5. [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) by Christopher Olah (2015). This is one of the greatest articles that you will find on the internet to understand LSTMs. The author tries to make everything as simple as possible. This is a must-read if you are learning about LSTMs.

6. [Understanding LSTM and its diagrams](https://medium.com/mlreview/understanding-lstm-and-its-diagrams-37e2f46f1714) by Shi Yan (2016). This article was written in reference to the above article on LSTMs. It also contains some diagrams that will help you gain a better understanding of LSTMs.

7. [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) by Andrej Karpathy (2015). This is also a great article; it discusses the usefulness and some of the applications of RNNs. It also helps you to understand the mathematics behind RNNs in the form of Python code.

8. [Visualizing and Understanding Recurrent Networks](https://arxiv.org/pdf/1506.02078.pdf) by Andrey Karpathy et al. (2015). This paper discusses some of the errors in LSTMs and compares them to character-level RNNs. We suggest you read this article, as it will help you understand our next project, which is based on character-level RNN models.

9. [LSTM: A Search Space Odyssey](https://arxiv.org/pdf/1503.04069.pdf) by Klaus Greff et al. (2015). This paper presents the first large-scale analysis of eight LSTM variants on three representative tasks: speech recognition, handwriting recognition, and polyphonic music modeling. They summarized the results of 5400 experimental runs (≈15years of CPU time). It is an excellent paper to read about the applications of LSTMs and what hyperparameters you should choose.

# Assignments

We ask that you take these tasks seriously, as they will help you develop an in-depth understanding. We have three tasks for you:

* You’ll need to create the model with more words. In the project, we only used `10,000` words, so increase this number.

* Try to change the hyperparameters and increase the accuracy of the model.

* Give a new sentence and predict its sentiment. To perform this task, you will first need to convert each word to a number (based on the dictionary that you will get from the Keras dataset) and then treat it like an input to the embedding layer. This may be a little more challenging, but if you’ve made it this far, we believe you can do this.

### Problem one

You’ll need to create the model with more words. In the project, we only used 10,000 words, so increase this number.

### Problem two

Try to change the hyperparameters and increase the accuracy of the model.

```py
# Import the required libraries
from tensorflow.keras.datasets import imdb
from tensorflow.python.keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.callbacks import EarlyStopping
from tensorflow.python.keras.preprocessing import sequence
from tensorflow.python.keras.layers import Embedding,SimpleRNN,Dense
from tensorflow.python.keras.models import Sequential

# Load the Dataset
((XT,YT),(Xt,Yt)) = imdb.load_data(num_words=30000)
print("The length of the Training Dataset is ", len(XT))
print("The length of the Testing Dataset is ", len(Xt))

# Perform the padding
X_train = sequence.pad_sequences(XT,maxlen=500)
X_test = sequence.pad_sequences(Xt,maxlen=500)

# Create the Model Architecture
model = Sequential()
model.add(Embedding(30000,128))
model.add(SimpleRNN(64))
model.add(Dense(1,activation='sigmoid'))

# Compile the Model
model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['acc'])

# Create the Callbacks
checkpoint = ModelCheckpoint("best_model.h5", monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=False)
earlystop = EarlyStopping(monitor='val_acc',patience=1)

# Train the Model
hist = model.fit(X_train,YT,validation_split=0.2,epochs=10,batch_size=128,callbacks=[checkpoint,earlystop])

# Evaluate the Model on Test Dataset
model.evaluate(X_test,Yt)
```

`Explanation:`

* We used a similar code which we discussed in the previous lessons.
* On line 10, we used the top 30000 frequent words that needed to be considered and loaded the dataset.
* From line 19 to line 22, we tweaked the model architecture a bit.
* The rest remains the same.
* You can expect an accuracy of around 96% or more.

### Plot the accuracy and loss

Below, we used the same code snippet to plot the curve between validation accuracy vs. training accuracy and validation loss vs training loss.


```py
import matplotlib.pyplot as plt

# Validation Accuracy vs Training Accuracy
acc = hist.history['acc']
val_acc = hist.history['val_acc']
epochs = range(1,len(acc)+1)
plt.title("Accuracy vs Epochs")
plt.plot(epochs,acc,label="Training Acc")
plt.plot(epochs,val_acc,label="Val Acc")
plt.legend()
plt.show()

# Validation Loss vs Training Loss
loss = hist.history['loss']
val_loss = hist.history['val_loss']
epochs = range(1,len(loss)+1)
plt.title("Loss vs Epochs")
plt.plot(epochs,loss,label="Training Loss")
plt.plot(epochs,val_loss,label="Val Loss")
plt.legend()
plt.show()
```

### Problem 3

Give a new sentence and predict its sentiment. To perform this task, you will first need to convert each word to a number (based on the dictionary that you will get from the Keras dataset) and then treat it like an input to the embedding layer.

```py
sent = "This movie is really bad . I do not like this movie because the direction was horrible ."
inp = []

# Get the word:integer mapping
word_idx = imdb.get_word_index()

# Convert each word to integer
for word in sent.split():
  if word in word_idx.keys():
    inp.append(word_idx[word])
  else:
    inp.append(1)

print(inp)

# Perform the padding
final_input = sequence.pad_sequences([inp],maxlen=500)

# Finally predict the sentiment
model.predict(final_input)
```

`Explanation:`

* On line 1, we defined a sample sentence for which we want to predict the sentiment (0 for positive and 1 for negative).

* From line 5 to line 12, we ran a loop to get the corresponding integer for each word. Remember that we used imdb.get_word_index() to get the word to integer mapping. We appended 1 for those words for which we do not have any corresponding integer.

* On line 14, we printed the inp list. You can expect an output similar to this:

```py
[1, 17, 6, 63, 75, 1, 1, 78, 21, 37, 11, 17, 85, 1, 455, 13, 524, 1]
```

* On line 17, we performed the padding as usual.

* On line 20, we performed the prediction for the sentence. You can expect an output similar to this:

```py
array([[0.5975645]], dtype=float32)
```

This means that our sentiment is 1 because we can assume that the sentiment is 0 if the value is less than 0.5 and 1 if the value is greater than 0.5. Hence, we can say that the sentiment is negative (which is obvious by reading the statement).`
