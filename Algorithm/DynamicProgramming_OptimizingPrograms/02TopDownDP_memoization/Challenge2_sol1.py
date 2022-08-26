# Solution 1: Simple recursion

def solveKnapsack(weights, prices, capacity, index):
  # base case of when we have run out of capacity or objects
  if capacity <= 0 or index >= len(weights): 
    return 0
  # if weight at index-th position is greater than capacity, skip this object
  if weights[index] > capacity: 
    return solveKnapsack(weights, prices, capacity, index + 1)
  # recursive call, either we can include the index-th object or we cannot, we check both possibilities and return the most optimal one using max
  return max(prices[index]+solveKnapsack(weights, prices, capacity - weights[index], index+1),
        solveKnapsack(weights, prices, capacity, index + 1))

def knapsack(weights, prices, capacity):
  return solveKnapsack(weights, prices, capacity, 0)

print(knapsack([2,1,1,3], [2,8,1,10], 4))
    