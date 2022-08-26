from tools import timeit # get timeit function from tools.py(custom module)
import numpy as np

def random_walk_fastest(n=1000):
    # No 's' IS NumPy chice (Python offers choice & choices)
    steps = np.random.choice([-1,+1], n)
    return np.cumsum(steps) # return the cumulative sum of the steps along a given axis.

walk = random_walk_fastest(1000)
timeit("random_walk_fastest(n=1000)", globals())
# calculates the total loops and time per loop