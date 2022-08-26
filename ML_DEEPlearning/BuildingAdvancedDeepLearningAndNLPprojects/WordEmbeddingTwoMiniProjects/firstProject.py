# Introduction to the project
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
print('Imported Successfully!')

# Create the function
# Accepts list_of_words and the word2vec vectors
def odd_one_out(words,word_vectors):

  all_word_vectors = [word_vectors[w] for w in words]
  avg_vector = np.mean(all_word_vectors, axis = 0)
  odd_one_out = None
  min_sim = 1.0

  for w in words:
    sim = cosine_similarity([word_vectors[w]],[avg_vector])
    if sim < min_sim:
      min_sim = sim
      odd_one_out = w

  return odd_one_out

print("Function Created Successfully!")

# Test the function
word_vectors = KeyedVectors.load_word2vec_format('/root/input/GoogleNews-vectors-negative300.bin.gz', binary=True)
list_of_words = ["apple","mango","party","juice","orange"]

print(odd_one_out(list_of_words,word_vectors))
