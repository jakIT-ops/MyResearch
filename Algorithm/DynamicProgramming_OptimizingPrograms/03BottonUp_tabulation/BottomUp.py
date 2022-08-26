def factorial(n):
    # tabulation table of size n+1
    table = [0] * (n+1)
    # base case of 0! = 1
    table[0] = 1
    # iterate until n
    for i in range(1, n+1):
        # using answer to i-1th problem from tabulation to build answer for ith problem
        table[i] = table[i-1]*i
    # return answer; the nth factorial
    return table[n]

print(factorial(30))