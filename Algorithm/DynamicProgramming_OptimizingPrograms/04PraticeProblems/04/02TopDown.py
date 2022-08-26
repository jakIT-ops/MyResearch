import numpy as np

def minRecursive(dims, i, j, memo):
    if j-i <= 2:
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    minimum = np.inf
    for k in range(i+1, j-1):
        minimum = min(minimum, minRecursive(dims, i, k+1, memo) + minRecursive(dims, k, j, memo) +
                    dims[i]*dims[j-1]*dims[k])
    memo[(i,j)] = minimum
    return minimum

def minMultiplications(dims):
    memo = {}
    return minRecursive(dims, 0, len(dims), memo)

print(minMultiplications([3, 3, 2, 1, 2]))