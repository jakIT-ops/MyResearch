from tools import timeit # get time it from tools.py(custom module)
import random

class RandomWalker:
    def __init__(self):
        self.position = 0
    
    def walk(self, n): # walk method
        self.position = 0
        for i in range(n):
            yield self.position
            self.position += 2 * random.randint(0, 1) - 1
            # return current position after each random step
            
walker = RandomWalker() # make instance of class walk
walk = [position for position in walker.walk(1000)] # call the walk function

walker = RandomWalker()
timeit("[position for position in walker.walk(n=10000)]", globals())
# calculates the total loops and time per loop    