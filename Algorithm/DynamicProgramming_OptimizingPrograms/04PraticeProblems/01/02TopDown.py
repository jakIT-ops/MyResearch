def countways_(bills, amount, maximum, memo):
  if amount == 0:     # base case 1
    return 1
  if amount < 0:      # base case 2
    return 0
  if (amount, maximum) in memo: # checking if memoized
    return memo[(amount, maximum)]
  ways = 0
  for bill in bills:     # iterate over bills
    # to avoid repetition of similar sequences, use bills smaller than maximum
    if bill <= maximum:     
      # notice how maximum becomes bill in recrusive call 
      ways += countways_(bills, amount-bill, bill, memo)  
  memo[(amount, maximum)] = ways #memoizing
  return ways

def countways(bills, amount):
  memo = {}
  return countways_(bills, amount, max(bills), memo)

print(countways([1,2,5], 5))