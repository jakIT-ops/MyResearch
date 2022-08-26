# Load the dataset
text_path = "train_corpus.txt"
def load_text(filename):
    with open(filename,encoding='utf8') as f:
        return f.read().lower()

text = load_text(text_path)
print('Loaded the dataset.')

# Understand sampling
import numpy as np

fruits = ["apple","banana","mango"]
for i in range(10):
    # Random sampling
    print(np.random.choice(fruits))

# Build the Markov chains
def MarkovChain(text,k=4):
    T = generateTable(text,k)
    T = convertFreqIntoProb(T)
    return T

model = MarkovChain(text)
print('Model Created Successfully!')
