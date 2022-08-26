import numpy as np
import theano.tensor as T

x = T.fvector('x')
y = T.fvector('y')
z = 2*x + 3*y
f = function([x, y], z)

a = np.random.uniform(0, 1, 1000).astype(np.float32)
b = np.random.uniform(0, 1, 1000).astype(np.float32)
c = f(a, b)