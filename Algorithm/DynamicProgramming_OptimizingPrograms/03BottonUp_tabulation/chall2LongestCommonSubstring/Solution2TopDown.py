def lcs_(str1, str2, i, j, count, memo):
  # base case of when either of string has been exhausted
  if i >= len(str1) or j >= len(str2):  
    return count
  # check if result available in memo
  if (i,j,count) in memo:       
    return memo[(i,j,count)]
  c = count
   # if i and j character matches, increment the count and compare the rest of the strings
  if str1[i] == str2[j]:     
    c = lcs_(str1, str2, i+1, j+1, count+1, memo)
  # compare str1[1:] with str2, str1 with str2[1:], and take max of current count and these two results
  # memoize the result
  memo[(i,j,count)] = max(c, lcs_(str1, str2, i+1, j, 0, memo), lcs_(str1, str2, i, j+1, 0, memo))
  return memo[(i,j,count)]

def lcs(str1, str2):
  memo = {}
  return lcs_(str1, str2, 0, 0, 0, memo)

print(lcs("hel", "elf"))

# testing with longer strings
import random
import string

st1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(40))
st2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(60))
print(lcs(st1, st2+st1))