# helper function with updated signature: i is current index in str1, j is current index in str2
def LCS_(str1, str2, i, j, memo): 
    if i == len(str1) or j == len(str2): # base case
        return 0
    elif (i,j) in memo:
        return memo[(i,j)]
    elif str1[i] == str2[j]:  # if current characters match, increment 1
        memo[(i,j)] = 1 + LCS_(str1, str2, i+1, j+1, memo)
        return memo[(i,j)]
    # else take max of either of two possibilities
    memo[(i,j)] = max(LCS_(str1, str2, i+1, j, memo), LCS_(str1, str2, i, j+1, memo))
    return memo[(i,j)]

def LCS(str1, str2):
    memo = {}
    return LCS_(str1, str2, 0, 0, memo)

print(LCS("bed", "read"))