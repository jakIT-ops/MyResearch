import numpy as np
import pyopencl as cl

a = np.random.uniform(0, 1, 1000).astype(np.float32)
b = np.random.uniform(0, 1, 1000).astype(np.float32)
c = np.empty_like(a)
   
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
gpu_a = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
gpu_b = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)

evaluate = cl.Program(ctx, """
  __kernel void evaluate(__global const float *gpu_a;
                         __global const float *gpu_b;
                         __global       float *gpu_c)
  {
    int gid = get_global_id(0);
    gpu_c[gid] = 2*gpu_a[gid] + 3*gpu_b[gid];
  }
""").build()

gpu_c = cl.Buffer(ctx, mf.WRITE_ONLY, a.nbytes)
evaluate.evaluate(queue, a.shape, None, gpu_a, gpu_b, gpu_c)
cl.enqueue_copy(queue, c, gpu_c)