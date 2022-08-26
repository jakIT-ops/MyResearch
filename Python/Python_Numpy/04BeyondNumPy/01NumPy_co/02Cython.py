import numpy as np

def evaluate(a,b):
  cdef int i
  cdef np.ndarray c = np.zeros_like(a)
  for i in range(a.size):
    c[i] = 2*a[i] + 3*b[i]
  return c

a = np.random.uniform(0, 1, 1000).astype(np.float32)
b = np.random.uniform(0, 1, 1000).astype(np.float32)
a = np.ndarray
b = np.ndarray
c = evaluate(a, b)