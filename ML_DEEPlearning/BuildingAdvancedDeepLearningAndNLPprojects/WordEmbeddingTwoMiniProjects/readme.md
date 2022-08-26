## What is word embedding?

If you know or have knowledge about NLP, then you might have created vectors for text, i.e., converting textual data to numbers using the two most used techniques: TF-IDF (Term Frequency-Inverse Document Frequency) and CountVectorizer. Let’s look closely at these two techniques.

### `TF-IDF`

It stands for Term Frequency-Inverse Document Frequency. It is a statistical measure that evaluates how relevant a word is to a document in a collection of documents. This is done by multiplying two metrics: how many times a word appears in a document, and the inverse document frequency of the word across a set of documents. TF-IDF for a word in a document is calculated by multiplying two different metrics:

* The term frequency of a word in a document. There are several ways of calculating this frequency, the simplest being a raw count of instances a word appears in a document. Then there are ways to adjust the frequency: by length of a document or by the raw frequency of the most frequent word in a document.

* The inverse document frequency of the word across a set of documents. This refers to how common or rare a word is in the entire document set. The closer it is to 0, the more common a word is. This metric can be calculated by taking the total number of documents, dividing it by the number of documents that contain a word, and calculating the logarithm.

* So, if the word is very common and appears in many documents, this number will approach 0. Otherwise, it will approach 1.

* Multiplying these two numbers results in the TF-IDF score of a word in a document. The higher the score, the more relevant that word is in that particular document.

### `CountVectorizer()`

This technique converts a collection of text documents into a matrix of token counts. This means that the text is converted into vectors which contain the number of times the word has appeared in the sentence.

But as we discussed in our chapter of transfer learning, there are some pre-trained models for NLP tasks that can be used to generate word vectors. These word vectors are nothing but the word embedding. The two most popular word embedding are:

* word2vec

* gloVe


## Supporting reading materials

1. GloVe: [Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf) by Jeffrey Pennington, Richard Socher, and Christopher D. Manning. This is the original paper that introduced the GloVe embeddings. If you skip this paper, then you are skipping some of the most important and interesting techniques that are used to create word vectors. Also, you must read this because, in the latter part of the course, we are going to use GloVe embedding to create our project.

2. [Improving the Accuracy of Pre-trained Word Embeddings for Sentiment Analysis](https://arxiv.org/ftp/arxiv/papers/1711/1711.08609.pdf) by Seyed Mahdi Rezaeinia et al. This paper proposes a novel method, Improved Word Vectors (IWV), which increases the accuracy of pre-trained word embeddings in sentiment analysis. Their method is based on Part-of-Speech (POS) tagging techniques, lexicon-based approaches, and word2vec/GloVe methods. This is a must-read paper and is also written in an easy-to-read manner.

3. [Comparative study of word embedding methods in topic segmentation](https://www.sciencedirect.com/science/article/pii/S1877050917313480?ref=pdf_download&fr=RR-2&rr=736483b0383fc249) by Marwa Naili et al. in 2017. This paper discusses three types of word embedding in the context of topic segmentation. This paper also provides different models and approximation algorithms for word2vec embedding.


# Assignments

We ask that you take these tasks seriously, as they will help you develop an in-depth understanding. We have two tasks for you:

* Create a `word2vec` model that will give you the similarity of two sentences (use cosine similarity). For this, you need to think about how to create a vector for a complete sentence and not just a word.

* Create a `word2vec` object (using `gensim.models`) that, will output the vectors for each word as a 100-dimensional vector. Then see the output of the previous step. Did you notice any change in the similarity?

## Problem one

Create a word2vec model that will give you the similarity of the two sentences (use cosine similarity).

We used a very simple approach to convert the sentence into a vector (embedding) representation. We just summed up all the individual word vectors and took the average of the resultant vector.

```py
# Import the required libraries
import gensim
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

# Load the word2vec embedding
word_vectors = KeyedVectors.load_word2vec_format('/root/input/GoogleNews-vectors-negative300.bin.gz', binary=True)

sent1 = "I like to eat mangoes"
sent2 = "I eat bananas"

# Create the vector representation for sent1
sent_v1 = np.zeros((300,))
count = 0
for word in sent1.split():
  if word in word_vectors:
    count += 1
    sent_v1 += word_vectors[word]

# Averaging the vector to obtain the sentence embedding
final_vector_1 = sent_v1 / count

# Create the vector representation for sent2
sent_v2 = np.zeros((300,))
count = 0
for word in sent2.split():
  if word in word_vectors:
    count += 1
    sent_v2 += word_vectors[word]

# Averaging the vector to obtain the sentence embedding
final_vector_2 = sent_v2 / count

# Calculate the similarity between the two sentences
print(cosine_similarity([final_vector_1],[final_vector_2]))
```

`Explanation:`

* From line 2 to line 4, we imported the required libraries.

* On line 7, we loaded our word2vec embedding.

* From line 13 to line 18, we created a sentence vector for the first sentence.

    * On line 13, we created a vector of 300-D with all 0's, as this is the dimension of our word2vec embedding.

    * On line 18, we added all of the individual word vectors, i.e., summed all the word vectors.

* On line 21, we took the average of the word vectors to obtain the sentence embedding.

* We repeated this process for the second sentence too.

* On line 35, we used cosine_similarity() to get the similarity between the two sentences.

You can expect an output similar to this:

```py
[[0.89234218]]
```

This means that the two sentences are `89.2%` similar.

```py
sent1 = "I like to eat mangoes"
sent2 = "Today is a good day"

# Create the vector representation for sent1
sent_v1 = np.zeros((300,))
count = 0
for word in sent1.split():
  if word in word_vectors:
    count += 1
    sent_v1 += word_vectors[word]

# Averaging the vector to obtain the sentence embedding
final_vector_1 = sent_v1 / count

# Create the vector representation for sent2
sent_v2 = np.zeros((300,))
count = 0
for word in sent2.split():
  if word in word_vectors:
    count += 1
    sent_v2 += word_vectors[word]

# Averaging the vector to obtain the sentence embedding
final_vector_2 = sent_v2 / count

# Calculate the similarity between the two sentences
print(cosine_similarity([final_vector_1],[final_vector_2]))
```

`Explanation:`

* We used the same code as above and changed only the sentences.

You can expect an output similar to this:

```py
[[0.32803528]]
```

This means that the two sentences are `32.8%` similar.
