def rodCutting(n, prices):
  # Create a dp array the size of (n+1)
  dp = [0 for _ in range(n + 1)]  
  # starting from rod of length 1, find optimal answer to all subproblems
  for i in range(1, n + 1):       
    max_val = 0
    # for a rod of length i, we can find what cuts give max answer since we have answer to all smaller cuts
    for j in range(i):            
      max_val = max(max_val, prices[j]+dp[i-j-1])
    dp[i] = max_val
  # return answer to n length rod
  return dp[n]                    

print(rodCutting(3, [3,7,8]))
