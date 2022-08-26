import numpy as np

# Example 1
Z = np.arange(9)
# print(Z)

# Example 2 
Z = np.arange(9).reshape(3,3).astype(np.int16)
print(Z)
V = Z[::2, ::2]
V = V.reshape(1,4)
print(V) # matrix bulangiin 4 elementiig awna 1 hemjeest