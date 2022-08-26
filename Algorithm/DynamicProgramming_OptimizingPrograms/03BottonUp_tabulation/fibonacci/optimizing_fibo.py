def fib(n):
    if n == 0:              # base cases
        return 0
    if n == 1:              # base cases
        return 1
    secondLast = 0          # base case 1, fib(0) = 0
    last = 1                # base case 2, fib(1) = 1
    current = None          # initially set to None
    for i in range(1, n):     # iterate n times to evaluate n-th fibonacci
        # storing ith fibonacci in current by summing up i-1th and i-2th fibonacci
        current = secondLast + last
        secondLast = last   # updating for next iteration
        last = current
    return current          # return the value of n in tabulation table 

print(fib(6))