def permutations(str):
  
  if str == "": 
    return [""]
  permutes = []
  for char in str:
    subpermutes = permutations(str.replace(char, "", 1))    # recursive step
    #print(subpermutes)
    for each in subpermutes:
      permutes.append(char+each)
  return permutes

def main():
  print (permutations("abc"))

main()