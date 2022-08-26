# Calculate Sum of a Vector: Conclusion

### Single Threaded

The range-based for loop and the STL algorithm std::accumulate are in the same performance range. This observation holds for the most optimized version. In the optimized version, the compiler uses the optimized version vectorized SIMD instruction (SSE or AVX) for the summation case; therefore, the loop counter will be increased by 2 (SSE) or 4 (AVX).

### Multithreading with a Shared Variable

The usage of a shared variable for the summation variable makes one point clear: synchronization is very expensive and should be avoided as much as possible. Although I used an atomic variable and even broke the sequential consistency, the four threads are 100 times slower than one thread. From a performance perspective, minimizing expensive synchronization has to be our first goal.


### Thread-local Summation

The thread-local summation is only two times faster than the single-threaded range-based for loop or std::accumulate; that holds, even though each of the four threads can work independently. That surprised me because I was expecting a nearly fourfold improvement, and it surprised me even more that my four cores were not fully utilized.





































