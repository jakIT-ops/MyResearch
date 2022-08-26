def lcs(str1, str2):
  n = len(str1)   # length of str1
  m = len(str2)   # length of str1

  dp = [0 for i in range(n+1)]  # table for tabulation, only maintaining state of last row
  maxLength = 0   # to keep track of longest substring seen 

  for j in range(1, m+1):           # iterating to fill table
    thisrow = [0 for i in range(n+1)] # calculate new row (based on previous row i.e. dp)
    for i in range(1, n+1):
      if str1[i-1] == str2[j-1]:    # if characters at this position match, 
        thisrow[i] = dp[i-1] + 1 # add 1 to the previous diagonal and store it in this diagonal
        maxLength = max(maxLength, thisrow[i])  # if this substring is longer, replace it in maxlength
      else:
        thisrow[i] = 0 # if character don't match, common substring size is 0
    dp = thisrow   # after evaluating thisrow, set dp equal to this row to be used in the next iteration
  return maxLength

stressTesting = True  # to only check if your recursive solution is correct, set it to false
testForBottomUp = True   # to test a top down implementation set it to false  

print(lcs("hel", "elf"))

# testing with longer strings
import random
import string

st1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(400))
st2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(600))
print(lcs(st1, st2+st1))