# helper function with updated signature: i is current index in str1, j is current index in str2
def LCS_(str1, str2, i, j): 
    if i == len(str1) or j == len(str2): # base case
        return 0
    elif str1[i] == str2[j]:  # if current characters match, increment 1
        return 1 + LCS_(str1, str2, i+1, j+1)
    # else take max of either of two possibilities
    return max(LCS_(str1, str2, i+1, j), LCS_(str1, str2, i, j+1))

def LCS(str1, str2):
    return LCS_(str1, str2, 0, 0)

print(LCS("bed", "read"))