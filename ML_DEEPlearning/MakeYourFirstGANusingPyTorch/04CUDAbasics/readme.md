## Nvidia CUDA

### CPU vs. GPU

All computers have a CPU, the main component that does most of the work. It runs our Python code, for example. We can think of it as the brains of our computer. CPU stands for central processing unit, but nobody really thinks about those words anymore. CPUs are designed to be general-purpose, and good at many different kinds of tasks.

Those graphics cards we mentioned earlier contain a GPU, or graphics processing unit. Unlike a general-purpose CPU, a GPU is designed to perform specific tasks and do them well. One of those tasks is to carry out arithmetic, including matrix multiplication, in a highly parallel way.

### CUDA

NVIDIA has been a leader in the GPU market and is pretty much the standard for machine learning research because their software tools for taking advantage of hardware acceleration are fairly mature. Their software framework is called CUDA.

The downside of CUDA is that it only works with GPUs from NVIDIA. You don’t have a choice except to buy NVIDIA GPUs. NVIDIA’s competitor, AMD is only just starting to develop a comparable framework for its GPUs. In the future, a cross-platform standard might emerge and become well adopted, but for now, we’ll need to use NVIDIA and CUDA


## NumPy vs. CUDA

The following shows how long it takes NumPy and CUDA to multiply matrices of sizes from 100
100
 to 2000
2000
. We can see that NumPy slows down as the matrices get larger. The CUDA calculations do slow down too, but at this scale, the GPU hardly breaks a sweat!

This chart really shows the benefit of using GPUs to crunch through lots of data where it can be broken down into chunks and the calculations are done in parallel.

# Learning Points in CUDA Basics

* GPUs contain many compute cores for performing certain calculations in a highly parallel way. Originally designed to accelerate computer graphics, they are increasingly used to accelerate machine learning calculations.

* CUDA is NVIDIA’s programming framework for GPU accelerated computation. PyTorch makes it very easy to take advantage of CUDA without significantly changing coding style.

* On synthetic benchmarks, such as matrix multiplication, we can see a GPU outperform a CPU by a factor of over 150.

* GPUs can be slower than CPUs at individual calculations. There is also a cost of transferring data between the CPU and GPU. If the data isn’t wide enough to distribute over many cores, there may be little or no benefit to using a GPU.
