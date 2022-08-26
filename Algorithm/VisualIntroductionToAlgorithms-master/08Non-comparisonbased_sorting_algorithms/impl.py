def counting_sort(arr):

  # Finds max and min elements 
  max_element = max(arr)
  min_element = min(arr)

  # Stores the frequency(count) of each element of the given array
  frequency = [0] * (max_element - min_element + 1)
  
  # Finds the frequency of each element of the given array 
  for i in range(len(arr)):
    frequency[arr[i] - min_element] += 1

  # Finds and store the cumulative sum 
  for i in range(1, len(frequency)):
    frequency[i] += frequency[i - 1]
  
  # This will be the output array in the sorted order
  sorted_array = [None] * len(arr)
  

  # Finds the index of each element of the given array(the value of the given array 
  # will be the corresponding index at the sorted_array) in the sorted array
  # and subtract the element by 1 and places it(the value) at the corresponding index at the sorted_array 
  for i in range(len(arr) - 1, -1, -1):
      sorted_array[frequency[arr[i] - min_element] - 1] = arr[i]
      frequency[arr[i] - min_element] -= 1

  # Returns the sorted array    
  return sorted_array


# Driver's code
arr = [3, 4, 2, 5, 1, 7, 3]
print("Array before Sorting:")
print(arr)
print("Array after Sorting:")
print(counting_sort(arr))
