# Atomic Smart Pointers

A std::shared_ptr consists of a control block and its resource. The control block is thread-safe, but the access to the resource is not. This means modifying the reference counter is an atomic operation and you have the guarantee that the resource will be deleted exactly once. These are the guarantees std::shared_ptr gives you.

The proposal N4162 for atomic smart pointers directly addresses the deficiencies of the current implementation. The deficiencies boil down to these three points: consistency, correctness, and performance. I will provide an overview of these three points. See the proposal N4162 for details.

* Consistency: the atomic operations for std::shared_ptr are the only atomic operations for a non-atomic data type.

* Correctness: the usage of the global atomic operations is quite error-prone because the right usage is based on discipline. It is easy to forget to use an atomic operation - such as using ptr = localPtr instead of std::atomic_store(&ptr, localPtr). The result is undefined behavior because of a data race. If we used an atomic smart pointer instead, the type-system would not allow it.

* Performance: the std::atomic_shared_ptr and std::atomic_weak_ptr have a big advantage compared to the free atomic_* functions. The atomic versions are designed for the special use case and can internally have a std::atomic_flag as a kind of cheap spinlock. Designing the non-atomic versions of the pointer functions to be thread safe would be overkill if they are used in a single-threaded scenario; they would have a performance penalty.

# Latches and Barriers 

Latches and barriers are simple thread synchronization mechanisms which enable some threads to wait until a counter becomes zero. At first, don’t confuse the new barriers with memory barriers (also known as fences). In C++20, we will presumably get latches and barriers in three variations: std::latch, std::barrier, and std::flex_barrier.

First, there are two questions:

1. What are the differences between these three mechanisms to synchronize threads? You can use an std::latch only once, but you can use an std::barrier and an std::flex_barrier more than once. Additionally, an std::flex_barrier enables you to execute a function when the counter becomes zero.

2. What use cases do latches and barriers support that cannot be done in C++11 and C++14 with futures, threads, or condition variables in combination with locks? Latches and barriers address no new use cases, but they are a lot easier to use; they are also more performant because they often use a lock-free mechanism internally.


### std::latch

std::latch is a countdown counter; its value is set in the constructor. A thread can decrement the counter by using the method thread.count_down_and_wait and wait until the counter becomes zero. In addition, the method thread.count_down only decrements the counter by 1 without waiting. std::latch also has the method thread.is_ready that can be used to test if the counter is zero, and the method thread.wait to wait until the counter becomes zero. You cannot increment or reset the counter of a std::latch, hence you cannot reuse it.

### std::barrier

The subtle difference between std::latch and std::barrier is that you can use std::barrier more than once because the counter will be reset to its previous value. Immediately after the counter becomes zero, the so-called completion phase starts. std::barrier has an empty completion phase; this changes with std::flex_barrier. std::barrier has two interesting methods: std::arrive_and_wait and std::arrive_and_drop. While std::arrive_and_wait waits at the synchronization point, std::arrive_and_drop removes itself from the synchronization mechanism.



### std::flext_barrier

This additional constructor can be parameterized​ by a callable unit that will be invoked in the completion phase. The callable has to return a number; this number sets the value of the counter in the completion phase. A return of -1 means that the counter keeps the same counter value in the next iteration. Numbers smaller than -1 are not allowed.

# Introduction to Coroutines

Coroutines are functions that can suspend and resume their execution while keeping their state. The evolution of functions goes one step further in C++20.

What I present in this section as a new idea in C++20 is actually quite old. The term coroutine was coined by Melvin Conway; He used it in his publication on compiler construction in 1963. Likewise, Donald Knuth called procedures a special case of coroutines. Sometimes, it just takes a while to get your ideas accepted.

With the new keywords co_await and co_yield, C++20 will extend the execution of a C++ function with two new concepts.

Thanks to co_await expression it will be possible to suspend and resume the execution of the expression. If you use co_await expression in a function func, the call auto getResult= func() will not block if the result of the function is not available. Instead of resource-consuming blocking, you have resource-friendly waiting.

co_yield expression allows it to write a generator function that returns a new value each time. A generator function is a kind of data stream from which you can pick values. The data stream can be infinite, therefore, we are in the center of lazy evaluation with C++.


































