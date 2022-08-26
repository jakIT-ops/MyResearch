def catalan(n):
    if n == 0:      # base case; c(0) = 1
        return 1
    sum = 0
    # iterate from 1....n to evaluate: c(0)*c(n-1) + c(1)*c(n-2).... + c(n-1)*c(0)
    for i in range(n):
        sum += (catalan(i) * catalan(n-1-i))  # c(i)*c(n-1-i)
    return sum

print(catalan(4))
     