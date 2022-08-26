def countways_(bills, amount, maximum):
  if amount == 0:     # base case 1
    return 1
  ways = 0
  # iterate over bills
  for bill in bills:    
    # to avoid repetition of similar sequences, use bills smaller than maximum
    if bill <= maximum and amount - bill >= 0:  
      # notice how bill becomes maximum in recursive call    
      ways += countways_(bills, amount-bill, bill)  
  return ways

def countways(bills, amount):
  return countways_(bills, amount, max(bills))

print(countways([1,2,5], 5))