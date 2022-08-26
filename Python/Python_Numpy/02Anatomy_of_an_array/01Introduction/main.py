import numpy as np
from tools import timeit #get timeit from tools.py(custom module)
Z = np.ones(4*1000000, np.float32) #create an array of size 4*10000000 np.float32

print("np.float16:")
#time required to view array as np.float16
timeit("Z.view(np.float16)[...] = 0", globals())

print("np.int16:")
#time required to view array as np.int16
timeit("Z.view(np.int16)[...] = 0", globals())

print("np.int32:")
#time required to view array as np.int32
timeit("Z.view(np.int32)[...] = 0", globals())

print("np.float32:")
#time required to view array as np.float32
timeit("Z.view(np.float32)[...] = 0", globals())

print("np.int64:")
#time required to view array as np.int64
timeit("Z.view(np.int64)[...] = 0", globals())

print("np.float64:")
#time required to view array as np.float64
timeit("Z.view(np.float64)[...] = 0", globals())

print("np.complex128:")
#time required to view array as np.complex128
timeit("Z.view(np.complex128)[...] = 0", globals())

print("np.int8:")
#time required to view array as np.int8
timeit("Z.view(np.int8)[...] = 0", globals())

print("np.float16:")
#time required to view array as np.float16
timeit("Z.view(np.float16)[...] = 0", globals())

print("np.int16:")
#time required to view array as np.int16
timeit("Z.view(np.int16)[...] = 0", globals())

print("np.int32:")
#time required to view array as np.int32
timeit("Z.view(np.int32)[...] = 0", globals())

print("np.float32:")
#time required to view array as np.float32
timeit("Z.view(np.float32)[...] = 0", globals())

print("np.int64:")
#time required to view array as np.int64
timeit("Z.view(np.int64)[...] = 0", globals())

print("np.float64:")
#time required to view array as np.float64
timeit("Z.view(np.float64)[...] = 0", globals())

print("np.complex128:")
#time required to view array as np.complex128
timeit("Z.view(np.complex128)[...] = 0", globals())

print("np.int8:")
#time required to view array as np.int8
timeit("Z.view(np.int8)[...] = 0", globals())