# NumPy

<p>NumPy нь Python хэлний сан бөгөөд том, олон хэмжээст массив болон матрицуудыг дэмждэг бөгөөд эдгээр массивууд дээр ажиллах өндөр түвшний математикийн функцуудын цуглуулгатай.</p>

## 1. Introduction

### Data Types

| Type     | Name | Bytes     | Description |
| :---        |    :----:   |   :----: | ---: |
| bool      | b       | 1   | Boolean (True or False) stored as a byte |
| int   | l        | 4-8      | Platform (long) integer (normally either int32 or int64) |
| intp | p | 4-8 | 	Integer used for indexing (normally either int32 or int64) |
| int8 |	i1 |	1 |	Byte (-128 to 127) |
| int16 |	i2 |	2	| Integer (-32768 to 32767) |
| int32 |	i4 |	4 |	Integer (-2147483648 to 2147483647) |
| int64 |	i8 |	8 |	Integer (-9223372036854775808 to 9223372036854775807) |
| uint8 |	u1 |	1 |	Unsigned integer (0 to 255) |
| uint16 | u2 | 2 |	Unsigned integer (0 to 65535) |
| uint32 |	u4 |	4 |	Unsigned integer (0 to 4294967295) |
| uint64 |	u8 |	8 |	Unsigned integer (0 to 18446744073709551615) |
| float  |	f8 |	8 |	Shorthand for float64 |
| float16 |	f2 |	2 |	Half precision float: sign bit, 5 bits exponent, 10 bits mantissa |
| float32	| f	|4	| Single precision float: sign bit, 8 bits exponent, 23 bits mantissa |
| float64	| d |	8 |	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa |
| complex |	c16 |	16 |	Shorthand for complex128. |
| complex64 |	c8 | 8 | Complex number, represented by two 32-bit floats |
| complex128 | c16 | 16 | Complex number, represented by two 64-bit floats |

- [Creation in NumPy](https://github.com/jakIT-ops/Python_Numpy/blob/main/01Introduction/01Creation_in_Numpy.py)
- [Reshaping in NumPy](https://github.com/jakIT-ops/Python_Numpy/blob/main/01Introduction/02Reshaping_in_Numpy.py) - Reshaping нь массивын хэлбэрийг өөрчлөх болно.
- [Indexing in NumPy](https://github.com/jakIT-ops/Python_Numpy/blob/main/01Introduction/03Indexing_in_Numpy.py) - NumPy массивын индексжүүлэлт нь массивын элементэд хандахтай адилхан байна.
- [Broadcasting in NumPy](https://github.com/jakIT-ops/Python_Numpy/blob/main/01Introduction/04Broadcasting_in_Numpy.py) - Broadcasting нь арифметик үйлдлийн явцад numpy нь янз бүрийн хэлбэртэй массивуудыг хэрхэн авч үздэгийг тодорхойлдог. Мөн массивын үйлдлүүдийг векторжуулахад хэргэлддэг.
- [NumPy Vectorization](https://github.com/jakIT-ops/Python_Numpy/tree/main/01Introduction/NumPy_Vectorization) - Векторчлал гэдэг нь алгоритмыг нэг заавараас олон үйлдэл хийх боломжтой болгохын тулд оновчлох юм. (SIMD)

## 2. Anatomy of an Array 

<p>NumPy массивын үндсэн санах ойн зохион байгуулалт, view, copy Эдгээр нь NumPy-ыг ойлгох чухал ойлголтууд юм.</p>

- [Memory Layout](https://github.com/jakIT-ops/Python_Numpy/tree/main/02Anatomy_of_an_array/02Memory_Layout)
- [Views and Copies](https://github.com/jakIT-ops/Python_Numpy/tree/main/02Anatomy_of_an_array/03Views_and_Copies)

## 3. Code Vectorization

- [Introduction](https://github.com/jakIT-ops/Python_Numpy/blob/main/03CodeVectorization/01Introduction.py)

## 4. Beyond NumPy

<p>Beyond NumPy, there are several other Python packages that are worth a look because they address similar yet different class of problems using different technology (compilation, virtual machine, just in time compilation, GPU, compression, etc.). Depending on your specific problem and your hardware, one package may be better than the other.</p>

- [NumExpr](https://github.com/pydata/numexpr/wiki/Numexpr-Users-Guide) - The numexpr package supplies routines for the fast evaluation of array expressions element-wise by using a vector-based virtual machine. It’s comparable to SciPy’s weave package, but doesn’t require a separate compile step of C or C++ code.

```python
import numpy as np
import numexpr as ne

a = np.random.uniform(0, 1, 1000).astype(np.float32)
b = np.random.uniform(0, 1, 1000).astype(np.float32)
c = ne.evaluate("2*a + 3*b")
```

- [Cython](https://cython.org/) - Cython is an optimizing static compiler for both the Python programming language and the extended Cython programming language (based on Pyrex). It makes writing C extensions for Python as easy as Python itself.

```python
import numpy as np

def evaluate(a,b):
  cdef int i
  cdef np.ndarray c = np.zeros_like(a)
  for i in range(a.size):
    c[i] = 2*a[i] + 3*b[i]
  return c

a = np.random.uniform(0, 1, 1000).astype(np.float32)
b = np.random.uniform(0, 1, 1000).astype(np.float32)
a = np.ndarray
b = np.ndarray
c = evaluate(a, b)
```

- [Numba](https://numba.pydata.org/) - Numba gives you the power to speed up your applications with high-performance functions written directly in Python. With a few annotations, array-oriented and math-heavy Python code can be just-in-time compiled to native machine instructions, similar in performance to C, C++ and Fortran, without having to switch languages or Python interpreters.

```python
from numba import jit
import numpy as np

@jit
def evaluate(np.ndarray a, np.ndarray b):
  c = np.zeros_like(a)
  for i in range(a.size):
    c[i] = 2*a[i] + 3*b[i]
  return c

a = np.random.uniform(0, 1, 1000).astype(np.float32)
b = np.random.uniform(0, 1, 1000).astype(np.float32)
c = evaluate(a, b)
```

- [Theano](http://www.deeplearning.net/software/theano/) - Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. Theano features tight integration with NumPy, transparent use of a GPU, efficient symbolic differentiation, speed and stability optimizations, dynamic C code generation and extensive unit-testing and self-verification.

```python
import numpy as np
import theano.tensor as T

x = T.fvector('x')
y = T.fvector('y')
z = 2*x + 3*y
f = function([x, y], z)

a = np.random.uniform(0, 1, 1000).astype(np.float32)
b = np.random.uniform(0, 1, 1000).astype(np.float32)
c = f(a, b)
```

- [PyCUDA](https://mathema.tician.de/software/pycuda/) - PyCUDA lets you access Nvidia’s CUDA parallel computation API from Python.

```python
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
```

- [PyOpenCL](https://mathema.tician.de/software/pyopencl/) - PyOpenCL lets you access GPUs and other massively parallel computing devices from Python.

```python
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
```
