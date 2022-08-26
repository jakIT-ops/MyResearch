def lcs_(str1, str2, i, j, count):
  # base case of when either of string has been exhausted
  if i >= len(str1) or j >= len(str2):  
    return count
  # if i and j character matches, increment the count and compare the rest of the strings
  if str1[i] == str2[j]:     
    count = lcs_(str1, str2, i+1, j+1, count+1)
  # compare str1[1:] with str2, str1 with str2[1:], and take max of current count and these two results
  return max(count, lcs_(str1, str2, i+1, j, 0), lcs_(str1, str2, i, j+1, 0))
  

def lcs(str1, str2):
  return lcs_(str1, str2, 0, 0, 0)

print(lcs("hello", "elf"))