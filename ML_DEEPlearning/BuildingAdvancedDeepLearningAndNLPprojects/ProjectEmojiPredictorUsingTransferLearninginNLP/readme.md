## Introduction to the project

Thus far, we have discussed a variety of topics. Remember what we discussed about transfer learning and word2vec. In this project, we are going to use another pre-trained model (embedding): GloVe. This project will use the concepts of transfer learning, embedding, and LSTMs. In this project, we are going to predict an emoji for a particular sentence.

To get started with this project, you will require the following packages. So, first make sure they are installed. You can run the commands below on your local machine.

pip install emoji
pip install numpy
pip install pandas
pip install keras


## GloVe embedding

Now that we have explored our dataset and have everything ready, let’s take a look at the GloVe Embedding. GloVe stands for Global Vectors for Word Representation and was developed at Stanford University. GloVe is an unsupervised learning algorithm for obtaining vector representations for words.

We will now create a dictionary, which will be a mapping for the words to their vector representation. Before moving on, you need to download the GloVe vectors; you can download it [here](https://www.kaggle.com/datasets/watts2/glove6b50dtxt). It is around 150 MB of data. This will give you a 50-dimension vector representation for each word. It contains around 6 billion words. Alternatively, if you want vectors with more dimensions try using Google Colab as we used in the case of word2vec.

Run the following command on your Colab -

```
!wget  "http://nlp.stanford.edu/data/glove.6B.zip"
!unzip "glove.6B.zip"
```

When you unzip the data, you will be able to see that there are four text files that contain the GloVe vectors in 50-, 100-, 200- and 300-dimensions. We will use the 50-dimension vectors in this project, but you can go ahead with other dimensions as well.
