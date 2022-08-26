def catalan(n):
  table = [None] * (n+1)  # tabulating 
  table[0] = 1            # handling the base case
  for i in range(1,n+1):  # iterating to fill up the tabulation table
    table[i] = 0          # initializing the i-th value to 0
    # iterate from 0 to i; according to formula of catalan i.e. 
    # C0*Ci + C1*Ci-1 + ... Ci*C0
    for j in range(i):    
      table[i] += (table[j] * table[i-j-1]) # C(j) * C(i-j-1)
  return table[n]         

print(catalan(1000))