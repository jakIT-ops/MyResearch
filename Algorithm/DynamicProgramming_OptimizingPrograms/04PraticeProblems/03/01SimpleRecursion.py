# Given the index of the class and the list of schedule, this function returns the last class that does not conflict with this class, if it exists otherwise returns None
def lastNonConflict(index, schedule, isSorted = False):
  if not isSorted:
    schedule = sorted(schedule, key=lambda tup: tup[1])
  for i in range(index, -1, -1):
    if schedule[index][0] >= schedule[i][1]:
      return i
  return None

def WSrecursive(schedule, n):
  if n == None or n < 0:  # base case of conflict with the first event
    return 0
  if n == 0:              # base case of no conflict with the first event
    return schedule[n][2]
  
  # find max of keeping the n-th event or not keeping it
  return max(schedule[n][2] + WSrecursive(schedule, lastNonConflict(n, schedule, isSorted= True)), 
          WSrecursive(schedule, n-1))

def WeightedSchedule(schedule):
  # sort the schedule by end time of events
  schedule = sorted(schedule, key=lambda tup: tup[1])
  return WSrecursive(schedule, len(schedule)-1)
  
print(WeightedSchedule([(0, 2, 25), (1, 6, 40), (6, 9, 170), (3, 8, 220)]))