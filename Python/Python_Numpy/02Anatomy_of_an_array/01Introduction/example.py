import numpy as np
Z = np.ones(4*1000000, np.float32) # create an array od ones of size 4 * 1000000
print(Z)
Z[...] = 0 # clear the array, sets every value to 0
print(Z)
print(Z.dtype) # prints the datatype of Z
