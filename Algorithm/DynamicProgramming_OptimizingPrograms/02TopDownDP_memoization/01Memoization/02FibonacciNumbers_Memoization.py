memo = {} 

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n in memo:
        #print(memo)
        return memo[n]
    else: # recursive step
        memo[n] = fib(n-1) + fib(n-2) # store the result of n in memoization dictionary
        return memo[n] 

print(fib(6))
    
        