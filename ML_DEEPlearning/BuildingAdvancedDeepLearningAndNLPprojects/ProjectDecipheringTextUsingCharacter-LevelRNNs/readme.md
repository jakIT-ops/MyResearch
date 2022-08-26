##$ Introduction to the project

Now you understand the working of RNNs, and you have also created a project in the previous chapter. In this chapter, we are going to build a model that will decipher the string encrypted with a certain cipher.

## What is a cipher?

A cipher is a cryptographic algorithm used to encrypt and decrypt data. In this project, we are going to use the Caesar cipher. It is a mono-alphabetic cipher, wherein each letter of the plaintext is substituted by another letter to form the ciphertext. It is the simplest form of a substitution cipher scheme. This cryptosystem is generally referred to as the Shift cipher. The concept is to replace each alphabet with another alphabet that is ‘shifted’ by some fixed number between 0 and 25.

For example, if we want to encrypt the string hello by a shift of 1 towards left, the ciphertext (encrypted data) will be ifmmp.

### Pre-processing the data

For a neural network to predict text data, it first has to be turned into data that it can understand. Text data, like “dog”, is a sequence of ASCII character encodings. Since a neural network is a series of multiplication and addition operations, the input data needs to be in numbers.

```py
from tensorflow.python.keras.preprocessing.text import Tokenizer

def tokenize(x):
    x_tk = Tokenizer(char_level=True)
    x_tk.fit_on_texts(x)
    return x_tk.texts_to_sequences(x), x_tk

text_sentences = [
    'The quick brown fox jumps over the lazy dog .',
    'By Jove , my quick study of lexicography won a prize .',
    'This is a short sentence .']
text_tokenized, text_tokenizer = tokenize(text_sentences)

print(text_tokenizer.word_index)

for sample_i, (sent, token_sent) in enumerate(zip(text_sentences, text_tokenized)):
    print('Sequence {} in x'.format(sample_i + 1))
    print('  Input:  {}'.format(sent))
    print('  Output: {}'.format(token_sent))
```
