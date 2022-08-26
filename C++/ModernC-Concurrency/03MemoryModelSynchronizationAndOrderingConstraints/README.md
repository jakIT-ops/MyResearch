# 1. Introduction

You cannot configure the atomicity of an atomic data type, but you can accurately adjust the synchronization and ordering constraints of atomic operations. This possibility is unique to C++, as it’s not possible in C#'s or Java’s memory model.

There are six different variants of the memory model in C++. The key question is what are their characteristics?

### Variants of the Memory Model

We already know C++ has six variants of the memory models. The default for atomic operations is std::memory_order_seq_cst; this expression stands for sequential consistency. In addition, you can explicitly specify one of the other five. So what does C++ have to offer?

```c++
enum memory_order{
  memory_order_relaxed,
  memory_order_consume,
  memory_order_acquire,
  memory_order_release,
  memory_order_acq_rel,
  memory_order_seq_cst
}
```

### Kind of Atomic Operation

There are three different kinds of operations:

* Read operation: <code>memory_order_acquire</code> and <code>memory_order_consume</code>

* Write operation: <code>memory_order_release</code>

* Read-modify-write operation: <code>memory_order_acq_rel</code> and <code>memory_order_seq_cst</code>

<code>memory_order_relaxed</code> defines no synchronization and ordering constraints; therefore, it does not fit in this taxonomy. The following table orders the atomic operations based on their reading and/or writing characteristics.

| Operation | read | write | read-modify-write |
| :-------- | ---- | ----- | ----------------: |
| test_and_set |   |       | yes 	       |
| clear     |	   | yes   | 	 	       |
| is_lock_free |yes|       |                   | 		
| load      | yes  |       | 		       |		
| store     |	   | yes   | 		       |
| exchange  |      |       |yes                |
| compare_exchange_strong compare_exchange_weak | | | yes |
| fetch_add, += fetch_sub, -= | | | yes |
| fetch_or, = fetch_and, &= fetch_xor, ^= | | | yes |
| ++, --		| | | yes |


# 2. Types of Synchronization & Ordering Constraints

There are, roughly speaking, three different types of synchronization and ordering constraints in C++:

* Sequential consistency: <code>memory_order_seq_cst</code>

* Acquire-release: <code>memory_order_consume</code>, <code>memory_order_acquire</code>, <code>memory_order_release</code> and <code>memory_order_acq_rel</code>

* Relaxed: <code>memory_order_relaxed</code>

# 3. Sequential Consistency

Let us dive deeper into sequential consistency. The key for sequential consistency is that all operations on all threads obey a universal clock. This universal clock makes it quite intuitive to think about it.

<br>
<div align="center">
	<img src="seqcons.png">
</div>
<br>

It is quite easy to understand that the program will always return “done”, as we only have to use the two characteristics of sequential consistency. On one hand, both threads execute their instructions in source code order; On the other hand, each thread sees the operations of the other thread in the same order. Both threads follow the same global timing. This timing will also hold - with the help of the <code>while(!ready.load()){}</code> loop - for the synchronization of the producer and the consumer thread.

# 4. Is the Acquire-Release Semantic Transitive?

<br>
<div align="center">
	<img src="transitivity.png">
</div>
<br>

The important parts of the picture are the arrows.

* The blue arrows are the sequenced-before relations. This means that all operations in one thread will be executed in source code order.

* The red arrows are the synchronizes-with relations; the reason for this is the acquire-release semantic of the atomic operations on the same atomic. Subsequently, the synchronization between the atomics, and therefore between the threads at specific points, takes place.

* Both sequenced-before and synchronizes-with establishes a happens-before relation.

# 5. Data dependencies with std::memory_order_consume

`std::memory_order_consume` deals with data dependencies on atomics; these data dependencies exist in two ways. First, let us look at carries-a-dependency-to in a thread and dependency-ordered before between two threads. Both dependencies introduce a happens-before relation. These are the kind of relations we are looking for. What does carries-a-dependency-to and dependency-order-before mean?

* <code>carries-a-dependency-to:</code> If the result of operation A is used as an operand in operation B, then A carries-a-dependency-to B.

* <code>dependency-ordered-before:</code> A store operation (with std::memory_order_release, std::memory_order_acq_rel or std::memory_order_seq_cst) is dependency-ordered-before load operation B (with std::memory_order_consume) if the result of load operation B is used in a further operation C in the same thread. It is important to note that operations B and C have to be in the same thread.
I know from personal experience that both definitions might not be easy to digest. Here is a grap

<br>
<div align="center">
	<img src="orderconsume.png">
</div>
<br>

The expression `ptr.store(p, std::memory_order_release)` is dependency-ordered-before the expression `while (!(p2 = ptr.load(std::memory_order_consume)))`, because the following line `std::cout << "*p2: " << *p2 << std::endl` will be read as the result of the load operation. Furthermore it holds that `while (!(p2 = ptr.load(std::memory_order_consume))` carries-a-dependency-to `std::cout << "*p2: " << *p2 << std::endl`, because the output of *p2 uses the result of the ptr.load operation.

# 6. Relaxed Semantic

The relaxed semantic is the other end of the spectrum. It’s the weakest of all memory models and only guarantees that the operations on the same atomic data type in the same thread won’t be reordered. That guarantee is called modification order consistency. Other threads can see these operations in a different order.

### No Synchronization & Ordering constraints?

This is quite easy; if there are no rules, we cannot violate them. But that is too easy, as the program should have well-defined behavior. In particular, this means that data races are not allowed. To guarantee this you typically use synchronization and ordering constraints of stronger memory models to control operations with relaxed semantic. How does this work? A thread can see the effects of another thread in arbitrary order, so you have to make sure there are points in your program where all operations on all threads get synchronized.













