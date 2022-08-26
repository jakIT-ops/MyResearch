import numpy as np
import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule
   
mod = SourceModule("""
  __global__ void evaluate(float *c, float *a, float *b)
  {
    const int i = threadIdx.x;
    c[i] = 2*a[i] + 3*b[i];
  }
""")

evaluate = mod.get_function("evaluate")

a = np.random.uniform(0, 1, 1000).astype(np.float32)
b = np.random.uniform(0, 1, 1000).astype(np.float32)
c = np.zeros_like(a)
   
evaluate(drv.Out(c), drv.In(a), drv.In(b), block=(400,1,1), grid=(1,1))