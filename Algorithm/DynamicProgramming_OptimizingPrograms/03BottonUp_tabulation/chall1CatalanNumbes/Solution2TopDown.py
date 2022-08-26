def catalan_memo(n, memo):
    if n == 0:               # base case; C(0) = 1
        return 1
    elif n in memo:
        return memo[n]       # if n already evuated, return from dp
    sum = 0
    # iterate from 1...n to evaluate: C(0)*C(n-1) + C(1)*C(n-2) ... + C(n-1)*C(0)
    for i in range(n):
        sum += (catalan_memo(i, memo) * catalan_memo(n-1-i, memo)) # C(i)*C(n-1-i)
    memo[n] = sum           # store result in dp
    return memo[n]

def catalan(n):
    memo = {}
    return catalan_memo(n, memo)

print(catalan(400))