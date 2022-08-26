def LCS(str1, str2):
    n = len(str1)   # length of str1
    m = len(str2)   # length of str1

    # table for tabulation, only maintaining state of last row
    dp = [0 for i in range(n+1)]  

    for j in range(1, m+1):           # iterating to fill table
        # calculate new row (based on previous row i.e. dp)
        thisrow = [0 for i in range(n+1)] 
        for i in range(1, n+1):
            # if characters at this position match, 
            if str1[i-1] == str2[j-1]:    
                # add 1 to the previous diagonal and store it in this diagonal
                thisrow[i] = dp[i-1] + 1 
            else:
                # if character don't match, use i-th result from dp, and previous result from thisrow
                thisrow[i] = max(dp[i], thisrow[i-1]) 
        # after evaluating thisrow, set dp equal to this row to be used in the next iteration
        dp = thisrow   
    return dp[n]

print(LCS("who", "wow"))