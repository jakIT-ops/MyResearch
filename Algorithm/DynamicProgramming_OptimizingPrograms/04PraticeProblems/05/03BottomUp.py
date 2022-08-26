import numpy as np

def findSubsets(numbers, i, subsets):
	if len(numbers) == i:
		return subsets
	if len(subsets) == 0:
		return findSubsets(numbers, i+1, [(), tuple([numbers[i]])])
	temp_subsets = []
	for subset in subsets:
		temp_subsets += [tuple(list(subset) + [numbers[i]])]
	return findSubsets(numbers, i+1, subsets + temp_subsets)
  
# function to find shortest path starting from city `start` and back to it
def TSPbottomup(distances, start):
  dp = {} # dp table
  # subproblem of travelling to second city from start city
  for i in range(len(distances)):
    dp[(tuple([i]), i)] = distances[start][i]
  # find all possible subsets of the cities
  subsets = findSubsets(list(range(len(distances))), 0, [])
  # solve for subset of each size from 2 to n
  for subsetSize in range(2,len(distances)+1):
    for subset in subsets:
      if len(subset) == subsetSize:
        # evaluating minimum cost to travel `subsetSize` number of cities while ending up at each city 
        for lastCity in subset:
          dp[(subset, lastCity)] = np.inf
          l = list(subset)
          l.remove(lastCity)
          subset2 = tuple(l)
          # to end up at city given by `lastCity`, it should be the last city to be traveled
          for city in subset2:
            dp[(subset, lastCity)] = min(dp[(subset, lastCity)], dp[(subset2, city)] + distances[city][lastCity])
  # return answer to the problem of travlling all cities while ending up at start city
  return dp[(subsets[-1], start)]

def TSP(distances):
  minimum = np.inf
  for i in range(len(distances)):
    minimum = min(minimum, TSPbottomup(distances, i))
  return minimum

print(TSP([
      [0, 10, 20],
      [12, 0, 10],
      [19, 11, 0],
]))