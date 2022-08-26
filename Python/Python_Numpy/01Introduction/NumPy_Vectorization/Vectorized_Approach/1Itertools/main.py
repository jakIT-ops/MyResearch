from tools import timeit #get timeit function from tools.py(custom module)
from itertools import accumulate #get accumulate function from built accumulate module
import random 
def random_walk_faster(n=1000):
  steps = random.choices([-1,+1], k=n)
  return [0]+list(accumulate(steps))#get the total number of steps

walk = random_walk_faster(1000) 
timeit("random_walk_faster(n=10000)", globals())# calculates the total loops and time per loop