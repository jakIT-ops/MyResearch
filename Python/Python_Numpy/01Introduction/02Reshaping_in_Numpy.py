import numpy as np

# Reshape to 12 rows and 1 column
# np.array(1D_array).reshape(x_dimension, y_dimension)
Z = np.array([0,0,0,0,0,0,0,0,0,0,1,0]).reshape(12,1)
print(Z)

# Reshape to 3 rows and 4 columns
Z = np.array([0,0,0,0,0,0,0,0,0,0,1,0]).reshape(3,4)
print(Z)

# Reshape to 6 rows and 2 col
Z = np.array([0,0,0,0,0,0,0,0,0,0,1,0]).reshape(6,2)
print(Z)

# Reshape to 2 rows and 6 col
Z = np.array([0,0,0,0,0,0,0,0,0,0,1,0]).reshape(2,6)
print(Z)