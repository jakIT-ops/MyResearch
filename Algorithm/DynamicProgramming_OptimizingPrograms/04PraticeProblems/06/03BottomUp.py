def LCS(str1, str2):
    n = len(str1)   # length of str1
    m = len(str2)   # length of str1

    dp = [[0 for j in range(m+1)] for i in range(n+1)]  # table for tabulation of size m x n
    
    # iterating to fill table
    for i in range(1, n+1):           
        for j in range(1, m+1):
            # if characters at this position match, 
            if str1[i-1] == str2[j-1]:    
                # add 1 to the previous diagonal and store it in this diagonal
                dp[i][j] = dp[i-1][j-1] + 1 
            else:
                # if character don't match, take max of last two positions vertically and horizontally
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
    return dp[n][m]

print(LCS("bed", "read"))

