def doLinearSearch(array, targetValue):
  for guess in xrange(len(array)):
    if array[guess] == targetValue:
      return guess  # found it!
      
  return -1;  # didn't find it
