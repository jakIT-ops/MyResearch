# GPUs - graphics processing units

The term GPU was popularized by nVIDIA in 1999, who marketed a computer graphics card called GeForce 256 as “The world’s first GPU”. However, the card was mainly designed for rendering of high-end computer graphics and enhancing computer-based gaming performance. In contrast, today’s GPUs also provide an inexpensive platform for developing and executing high-performance non-graphical applications. The development of general-purpose applications on GPUs is often termed as GPGPU (General Purpose Computing on GPUs) and a number companies have started to produce GPUs that are capable of general purpose computation.

Among the various kinds of GPUs, we have specifically chosen nVIDIA’s Tesla is a popular development platform, however latest GPUs like Fermi K80, Pascal, Volta are also not very different in terms of basics. All these devices allow programmers to develop applications using an easily programmable C-like language, called Compute Unified Device Architecture (CUDA).

https://www.youtube.com/watch?v=g1pq3RfxtB4&feature=emb_title

A schematic diagram of the Tesla’s unified GPU architecture is shown in the figure above. It illustrates the framework of a Tesla C2050 device. The device has a total of 448 streaming-processor (SP) cores organized as a group of 32 stream processors (also called CUDA cores), in 14 streaming multiprocessors (SM). Each core here executes a sequential thread in a so-called SIMT (Single Instruction, Multiple Thread) fashion and all the threads in a same wrap execute the same instruction at the same time, where a wrap is a group of 32 threads. Tesla supports up to 32 active warps on each SM. If one warp stalls at any conditional operation, then it selects another ready warp so that the cores can remain active.

Similar to other GPUs, the Tesla device has a hierarchy of on-board memory, such as a small and fast programmable L1 cache/shared memory (16 – 48 KBs), a fully coherent L2 cache memory (512–768 KBs) and a relatively large on-board DRAM or device main memory (3–6 GBs). The L1 cache is attached to each multiprocessor and shared among the comprising cores, where the unified L2 cache is shared across the device. The main task of L2 memory is to minimize the effect of the long latency of device DRAM. There are also some register files (128 KBs), texture and constant caches within each SM. At the software level, all the memory levels are unified into a single continuous address space.

There exist a number of application programming interfaces (API) that can enable programmers to access the device memory and develop GPU-based applications

## GPU Programming - CUDA

CUDA provides a relatively simple C-like interface to develop GPU-based applications. It exposes an abstraction to the programmers that completely hides the underlying hardware architecture. As a result, they see any CUDA-enabled GPUs as a collection of a number of threads organised into blocks and a collection of blocks that are organised into a grid. At the hardware level, the threads and blocks are handled by the streaming processors (SP) and streaming multiprocessors (SM), respectively, and the device is mapped as a grid. A simplified schematic diagram of the mapping is illustrated in the figure below:

A CUDA program typically consists of a component that runs on the CPU (host), and a smaller, but computationally intensive component called kernel that runs in parallel on the GPUs (device). Programmers can define how many parallel threads will execute the kernel, however, there is a limit to the maximum number of threads per block (since all threads of a block must reside inside the same SM). Currently, Tesla GPUs allow up to 1024 threads per block. Blocks can have 1,2, or 3-dimensional orientation of threads and they can be organised into a 1,2-dimensional grid (a 2D orientation of threads and blocks is illustrated in Figure (a)). Even though all the threads and blocks are designed to execute exactly one kernel function at a time (Figure (b)), they can be assigned to a specific portion of the data to work on. CUDA provides built-in variables that facilitate the identification of each of the blocks and threads separately during the kernel execution (Figure ©).

In terms of memory access, a kernel cannot access the main memory of the host directly (i.e., we need a host CPU to do the memory management). The input data for the kernel must be copied to the GPU’s on-board memory prior to its invocation and the output data from a kernel must first be written to the GPU’s memory, and then copied back to the host CPU memory (Figure (a)). CUDA supports different types of memory and each of them has specific scope (Figure (b)) and life span, such as registers (allocated per thread, handled by the 327,68 32-bit registers in each SM), constant (allocated to all the threads, embedded into the executable code, does not consume any register), local (allocated per thread, physically handled by the DRAM), shared (allocated per thread block, handled by L1 cache by default) and global (allocated to all the threads and blocks, handled by the DRAM). In addition, there is a read-only texture memory, which is purely intended to handle graphical applications.

Recent developments of the CUDA API also allow critical sections, which are implemented as atomic operations. These operations can assist a programmer to avoid any race conditions that may arise when two or more threads try to write in a single memory location. They are capable of read-modify-and-write a value back to the device memory without any interference from other parallel threads, and which guarantees that the race condition will not occur.

# CUDA - vector additiom demo

```CUDA

/**
 * Vector addition: w = u + v.
 *
 * This sample is a very basic sample that implements element by element
 * vector addition. It is the same as the sample illustrating Chapter 2
 * of the programming guide with some additions like error checking.
 */

#include <stdio.h>

// For the CUDA runtime routines (prefixed with "cuda_")
#include <cuda_runtime.h>

/**
 * CUDA Kernel Device code
 *
 * Computes the vector addition of u and v into w. The 3 vectors have the same
 * number of elements numElements.
 */
__global__ void
vectorAdd(const float *u, const float *v, float *w)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    w[i] = u[i] + v[i];
}

/**
 * Host main routine
 */
int
main(void)
{
    // Print the vector length to be used, and compute its size
    int numElements = 50000;
    size_t size = numElements * sizeof(float);
	// Observe that this program is ever so slightly busted,
	// for reasons that will become apparent later.
    printf("[Vector addition of %d elements]\n", numElements);

    // Allocate the host input vector u
    float *h_u = (float *)malloc(size);

    // Allocate the host input vector v
    float *h_v = (float *)malloc(size);

    // Allocate the host output vector w
    float *h_w = (float *)malloc(size);

    // Initialize the host input vectors
    for (int i = 0; i < numElements; ++i)
    {
        h_u[i] = rand()/(float)RAND_MAX;
        h_v[i] = rand()/(float)RAND_MAX;
    }

    // Allocate the device input vector u
    float *d_u = NULL;
    cudaMalloc((void **)&d_u, size);

    // Allocate the device input vector v
    float *d_v = NULL;
    cudaMalloc((void **)&d_v, size);

    // Allocate the device output vector w
    float *d_w = NULL;
    cudaMalloc((void **)&d_w, size);

    // Copy the host input vectors u and v in host memory to the
	// device input vectors in device memory
    printf("Copy input data from the host memory to the CUDA device\n");
    cudaMemcpy(d_u, h_u, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_v, h_v, size, cudaMemcpyHostToDevice);

    // Launch the Vector Add CUDA Kernel
    int threadsPerBlock = 256;
    int blocksPerGrid =(numElements + threadsPerBlock - 1) / threadsPerBlock;
    printf("CUDA kernel launch with %d blocks of %d threads\n", blocksPerGrid, threadsPerBlock);
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_u, d_v, d_w);

    // Copy the device result vector in device memory to the host result vector
    // in host memory.
    printf("Copy output data from the CUDA device to the host memory\n");
    cudaMemcpy(h_w, d_w, size, cudaMemcpyDeviceToHost);

    // Verify that the result vector is correct
    for (int i = 0; i < numElements; ++i)
    {
        if (fabs(h_u[i] + h_v[i] - h_w[i]) > 1e-5)
        {
            fprintf(stderr, "Result verification failed at element %d!\n", i);
            exit(EXIT_FAILURE);
        }
    }
    printf("Test PASSED\n");

    // Free device global memory
    cudaFree(d_u);
    cudaFree(d_v);
    cudaFree(d_w);

    // Free host memory
    free(h_u);
    free(h_v);
    free(h_w);

    // Reset the device and exit
    cudaDeviceReset();

    printf("Done\n");
    return 0;
}

```
