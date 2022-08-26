from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
print('Imported Successfully!')

def word_analogies(A,B,C,word_vectors):

  A,B,C = A.lower(), B.lower(), C.lower()
  max_sim = -100
  D = None
  words = word_vectors.vocab.keys()
  WA,WB,WC = word_vectors[A],word_vectors[B],word_vectors[C]

  for w in words:
    if w in [A,B,C]:
      continue

    w_vector = word_vectors[w]
    sim = cosine_similarity([WB-WA], [w_vector - WC])
    if sim > max_sim:
      max_sim = sim
      D = w

  return D

print("Function Created Successfully!")

# Test Function

word_vectors = KeyedVectors.load_word2vec_format('/root/input/GoogleNews-vectors-negative300.bin.gz', binary=True)
D = word_analogies("Man","Woman","King",word_vectors)
print(D)

result = word_vectors.most_similar(positive = ['woman','king'], negative = ['man'],topn = 1)
print(result)
