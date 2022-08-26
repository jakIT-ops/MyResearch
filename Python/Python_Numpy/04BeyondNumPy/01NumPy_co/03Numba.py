from numba import jit
import numpy as np

@jit
def evaluate(np.ndarray a, np.ndarray b):
  c = np.zeros_like(a)
  for i in range(a.size):
    c[i] = 2*a[i] + 3*b[i]
  return c

a = np.random.uniform(0, 1, 1000).astype(np.float32)
b = np.random.uniform(0, 1, 1000).astype(np.float32)
c = evaluate(a, b)