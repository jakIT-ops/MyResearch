# (C order, big endian)
import numpy as np

# Example 1
Z = np.arange(9).reshape(3, 3).astype(np.int16)
print(Z)

# Example 2
V = Z[::2, ::2]