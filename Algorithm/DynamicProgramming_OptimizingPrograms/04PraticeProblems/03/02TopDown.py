# Given the index of the class and the list of schedule, this function returns the last class that does not conflict with this class, if it exists otherwise returns None
def lastConflict(index, schedule, isSorted = False):
  if not isSorted:
    schedule = sorted(schedule, key=lambda tup: tup[1])
  for i in range(index, -1, -1):
    if schedule[index][0] >= schedule[i][1]:
      return i
  return None

def WSrecursive(schedule, n, memo):
  if n == None or n < 0:
    return 0
  if n == 0:
    return schedule[n][2]
  if n in memo:
    return memo[n]
  memo[n] = max(schedule[n][2] + WSrecursive(schedule, lastConflict(n, schedule, isSorted= True), memo), 
          WSrecursive(schedule, n-1, memo))
  return memo[n]

def WeightedSchedule(schedule):
  schedule = sorted(schedule, key=lambda tup: tup[1])
  memo = {}
  return WSrecursive(schedule, len(schedule)-1, memo)

# make sure start and end of any event is not the same
print(WeightedSchedule([(0, 2, 25), (1, 5, 40), (6, 8, 170), (3, 7, 220)]))
schedule = [(i,i+2,10) for i in range(100)]
print(WeightedSchedule(schedule))
