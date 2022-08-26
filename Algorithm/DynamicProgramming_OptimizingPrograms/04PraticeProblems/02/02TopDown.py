def rodCutting_(n, prices, memo):
  if n<0:
    return 0
  if n in memo:
    return memo[n]
  max_val = 0
  for i in range(1,n+1):
      max_val = max(max_val, prices[i-1] + rodCutting_(n - i, prices, memo))
  memo[n] = max_val
  return memo[n]

def rodCutting(n, prices):
  memo = {}
  return rodCutting_(n, prices, memo)

print(rodCutting(3, [3,7,8]))