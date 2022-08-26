# Given the index of the class and the list of schedule, this function returns the last class that does not conflict with this class, if it exists otherwise returns None
def lastConflict(index, schedule, isSorted = False):
  if not isSorted:
    schedule = sorted(schedule, key=lambda tup: tup[1])
  for i in range(index, -1, -1):
    if schedule[index][0] >= schedule[i][1]:
      return i
  return None

def WeightedSchedule(schedule):
  # sort the schedule by end times of events
  schedule = sorted(schedule, key=lambda tup: tup[1])
  dp = [0 for _ in range(len(schedule)+1)]

  for i in range(1, len(schedule)+1):
    # find the last conflicting event
    index_LC = lastConflict(i-1, schedule, isSorted=True)
    if index_LC == None:
      index_LC = -1
    # find the max of either keeping this event or not keeping it
    dp[i] = max(dp[i-1], dp[index_LC+1]+schedule[i-1][2])
  return dp[len(schedule)]

print(WeightedSchedule([(0, 2, 25), (1, 5, 40), (6, 8, 170), (3, 7, 220)]))
schedule = [(i,i+2,10) for i in range(100)]
print(WeightedSchedule(schedule))