import numpy as np

# Create an Array of Zeros
# np.zeros(size)
Z = np.zeros(9)
print(Z)

# Create an Array of Ones
# np.ones(size)
Z = np.ones(9)
print(Z)

# Create an Array of 0's and 1's
# np.array([1,0,0,0,0,0,0,1,0])
Z = np.array([1,0,0,0,0,0,0,1,0])
print(Z)

# Create an Array of 2's
# 2*np.ones(size)
Z = 2*np.ones(9)
print(Z)

# Create a NumPy Array of any Length
# np.arange(size)
Z = np.arange(9) # 0 to 8
print(Z)

# Reshape a NumPy Array into a Column Vector
# np.arange(size).reshape(size, 1)
# 9 rows 1 column
Z = np.arange(9).reshape(9,1)
print(Z)

# Generate Array of Random Numbers and in Grid Format
# np.random.randint(0, size, x_dimension, y_dimension)
Z = np.random.randint(0,9,(3,3))
print(Z)

# Create a Linspace
# np.linspace(start, stop, size)  0-1 hurtleh 5 too
Z = np.linspace(0, 1, 5)
print(Z)

# Create a Mesh Grid
# np.mgrid[0:x_dimension, 0:y_dimension]
Z = np.mgrid[0:3,0:3]
print(Z)