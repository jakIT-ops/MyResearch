import numpy as np

Z1 = np.arange(9).reshape(3,3)

# When one operand is N*N and other is 1*1
Z2 = 1
print(Z1 + Z2) # 0-8 3x3 matrix = 1-9 3x3 matrix bolno

# When one operand is N * N and other is N * 1
Z2 = np.arange(3)[::-1].reshape(3,1) # 2 1 0 vector
print(Z1 + Z2)

# When one operand is N * N and other is 1 * N
Z2 = np.arange(3)[::-1] # 2 1 0 array
print(Z1 + Z2)