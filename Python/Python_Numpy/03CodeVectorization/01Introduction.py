import numpy as np

def add_python(Z1,Z2):
    return [z1+z2 for (z1,z2) in zip(Z1,Z2)]
def add_numpy(Z1,Z2):
    return np.add(Z1,Z2)
  
Z1 = [[1, 2], [3, 4]]
Z2 = [[5, 6], [7, 8]]
print("Using concatenation:",Z1 + Z2)
   #[[1, 2], [3, 4], [5, 6], [7, 8]]
print("Using pure python:",add_python(Z1, Z2))
   #[[1, 2, 5, 6], [3, 4, 7, 8]]
print("Using numpy.add:",add_numpy(Z1, Z2))
   #[[ 6  8][10 12]]