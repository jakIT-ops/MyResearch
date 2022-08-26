import numpy as np

def TSPrecursive(distances, check, index, start):
  minimum = np.inf
  for i in range(len(distances)):
    if i != index and i != start and i not in check:
      check[i] = 1
      minimum = min(minimum, distances[index][i]+TSPrecursive(distances, check, i, start))
      del check[i]
  if minimum == np.inf:
    return distances[index][start]
  return minimum

def TSP(distances):
  check = {}
  minimum = np.inf
  for i in range(len(distances)):
    minimum = min(minimum, TSPrecursive(distances, check, i, i))
  return minimum

print(TSP([
      [0, 10, 20],
      [12, 0, 10],
      [19, 11, 0],
]))