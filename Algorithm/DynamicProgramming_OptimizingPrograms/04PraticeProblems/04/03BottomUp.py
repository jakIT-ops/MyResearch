import numpy as np

def minMultiplications(dims):
    
    dp = [[0 for _ in range(len(dims))] for _ in range(len(dims))]

    for l in range(2,len(dims)):
        for i in range(1,len(dims)-l+1):
            j = i+l-1
            dp[i][j] = np.inf
            for k in range(i, j):
                temp = dp[i][k]+ dp[k+1][j] + dims[i-1]*dims[k]*dims[j]
                if temp < dp[i][j]:
                    dp[i][j] = temp
    return dp[1][-1]
print(minMultiplications([3, 3, 2, 1, 2]))