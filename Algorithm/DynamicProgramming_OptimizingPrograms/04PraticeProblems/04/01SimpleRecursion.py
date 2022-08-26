import numpy as np
def minMultiplications(dims):
    if len(dims) <= 2:
        return 0
    minimum = np.inf
    for i in range(1,len(dims)-1):
        minimum = min(minimum, minMultiplications(dims[0:i+1]) + minMultiplications(dims[i:]) +
                    dims[0] * dims[-1] * dims[i])
    return minimum

print(minMultiplications([3, 3, 2, 1, 2]))