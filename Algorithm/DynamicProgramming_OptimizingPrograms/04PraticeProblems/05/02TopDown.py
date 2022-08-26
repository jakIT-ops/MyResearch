import numpy as np

def TSPrecursive(distances, check, index, end, memo):
  keys = tuple(sorted(check.keys()))
  if (keys, index) in memo:
    return memo[(keys, index)]
  minimum = np.inf
  for i in range(len(distances)):
    if i != index and i != end and i not in check:
      check[i] = 1
      minimum = min(minimum, distances[index][i]+TSPrecursive(distances, check, i, end, memo))
      del check[i]
  if minimum == np.inf:
    return distances[index][end]
  memo[(keys, index)] = minimum
  return memo[(keys, index)]

def TSP(distances):
  check = {}
  minimum = np.inf
  for i in range(len(distances)):
    minimum = min(minimum, TSPrecursive(distances, check, i, i, {}))
  return minimum

print(TSP([
      [0, 10, 20],
      [12, 0, 10],
      [19, 11, 0],
]))