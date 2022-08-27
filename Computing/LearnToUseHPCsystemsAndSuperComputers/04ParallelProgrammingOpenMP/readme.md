# OpenMP

OpenMP (Open Multi-Processing) is an application programming interface (API) that supports multi-platform shared memory multiprocessing programming in C, C++, and Fortran. It consists of a set of compiler directives, library routines, and environment variables that influence the code’s run-time behavior.

OpenMP uses a portable, scalable model that gives programmers a simple and flexible interface for developing parallel applications for platforms ranging from the standard desktop computer to the supercomputer.

An application built with the hybrid model of parallel programming can run on a computer cluster using both OpenMP and Message Passing Interface (MPI), such that OpenMP is used for parallelism within a (multi-core) node while MPI is used for parallelism between nodes.

## History

OpenMP is managed by the nonprofit technology consortium OpenMP Architecture Review Board (or OpenMP ARB), jointly defined by a group of major computer hardware and software vendors. They publised its first API specifications in October 1997. The latest version specification (4.5) released in 2015 adds/ improves supports for accelerators, atomics, error handling, thread affinity, tasking extensions, user defined reduction, SIMD support, and so on.

## Getting the OpenMP

All the latest OpenMP versions are integrated with the recent GNU compilers (4.9 and above), no need to install them separately!

# Open MP - clauses

| Clause | Description |
| :------------- | :------------- |
| copyin |	Allows threads to access the master thread’s value, for a threadprivate variable. |
| copyprivate |	Specifies that one or more variables should be shared among all threads. |
| default |	Specifies the behavior of unscoped variables in a parallel region. |
| firstprivate	| Specifies that each thread should have its own instance of a variable, and that the variable should be initialized with the value of the variable, because it exists before the parallel construct. |
| if	| Specifies whether a loop should be executed in parallel or in serial. |
| lastprivate |	Specifies that the enclosing context’s version of the variable is set equal to the private version of whichever thread executes the final iteration (for-loop construct) or last section (#pragma sections). |
| nowait |	Overrides the barrier implicit in a directive. |
| num_threads	  | Sets the number of threads in a thread team. |
|ordered	| Required on a parallel for-loop statement if an ordered directive is to be used in the loop. |
| private |	Specifies that each thread should have its own instance of a variable. |
| reduction |	Specifies that one or more variables that are private to each thread are the subject of a reduction operation at the end of the parallel region. |
|schedule |	Applies to the for directive. |
| shared	 | Specifies that one or more variables should be shared among all threads. |


# OpenMP - section parallelization

```c++
#include <stdio.h>
#include <omp.h>

int main(){
  int x;
  x = 2;
  #pragma omp parallel num_threads(2) shared(x)
  {
    if (omp_get_thread_num() == 0) {
      x = 5;
    } else {
      /* Print A: the following read of x has a race */
      printf("A: Thread# %d: x = %d\n", omp_get_thread_num(),x );
    }

    #pragma omp barrier

    if (omp_get_thread_num() == 0) {
      /* Print B */
      printf("B: Thread# %d: x = %d\n", omp_get_thread_num(),x );
     } else {
      /* Print C */
      printf("C: Thread# %d: x = %d\n", omp_get_thread_num(),x );
      }
  }
return 0;
}
```

# OpenMP vector addition

```c++
#include <omp.h>
#define CHUNKSIZE 100
#define N 1000

void main ()
{
  int i, chunk;
  float a[N], b[N], c[N];

  /* Some initializations */
  for (i=0; i < N; i++)
    a[i] = b[i] = i * 1.0;
    chunk = CHUNKSIZE;

    #pragma omp parallel shared(a,b,c,chunk) private(i)
    {
      #pragma omp for schedule(dynamic,chunk) nowait
      for (i=0; i < N; i++)
      c[i] = a[i] + b[i];
    } /* end of parallel section */
}
```
