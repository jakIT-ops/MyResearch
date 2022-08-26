def rodCutting(n, prices):
  if n<0:
    return 0
  max_val = 0
  for i in range(1,n+1):
      max_val = max(max_val, prices[i-1] + rodCutting(n - i, prices))
  return max_val

print(rodCutting(3, [3,7,8]))