def countways(bills, amount):
  if amount <= 0:
    return 0
  dp = [1 for _ in range(amount + 1)]
  for j in range(len(bills)):
    thiscol = [1 for _ in range(amount + 1)]
    for amt in range(1,amount + 1):
      bill = bills[j]
      if amt - bill >= 0:
        x = thiscol[amt - bill]
      else:
        x = 0
      if j >= 1:
        y = dp[amt]
      else:
        y = 0
      thiscol[amt] = x + y
    dp = thiscol
  return dp[amount]

print(countways([1,2,5], 5))