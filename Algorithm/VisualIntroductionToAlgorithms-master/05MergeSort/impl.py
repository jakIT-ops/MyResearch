# Takes in an array that has two sorted subarrays,
#  from [p..q] and [q+1..r], and merges the array
def merge(array, p, q, r):
  lh = q - p + 1
  rh = r- q

  L = [0] * (lh)
  R = [0] * (rh)
  
  for i in range(0 , lh):
	L[i] = array[p + i]
  for j in range(0 , rh):
	R[j] = array[q + 1 + j]
  i, j, k = 0, 0, p
  
  while i < lh and j < rh :
    if L[i] <= R[j]:
      array[k] = L[i]
      i += 1
    else:
      array[k] = R[j]
      j += 1
    k += 1
  
  while i < lh:
    array[k] = L[i]
    i += 1
    k += 1

  while j < rh:
    array[k] = R[j]
    j += 1
    k += 1

# Takes in an array and recursively merge sorts it
def mergeSort(array, p, r):
  return
