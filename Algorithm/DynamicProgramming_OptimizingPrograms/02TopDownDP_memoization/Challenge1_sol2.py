# Solution 2: Recursion with memoization

def nthStair(n, m, memo):
  
  if n == 0:    
    return 1
  # before recursive step check if result is memoized
  if n in memo: 
    return memo[n]
  ways = 0
  # iterate over number of steps, we can take
  for i in range(1,m+1):    
    # if steps remaining is smaller than the jump step, skip 
    if i <= n:           
      #recursive call with n i units lesser where i is the number of steps taken here   
      ways += nthStair(n-i, m, memo) 
  # memoize result before returning
  memo[n] = ways   
  return ways

def staircase(n, m):
  memo = {}
  # helper function to add memo dictionary to function
  return nthStair(n, m, memo) 

print(staircase(100, 6))