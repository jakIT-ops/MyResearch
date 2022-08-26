#  Mutex Types and Locking Methods

C++ has five different mutexes that can lock recursively (i.e., multiple layers of locking), tentative with and without time constraints.

| Method | mutex | recursive_mutex | timed_mutex | recursive_timed_mutex | shared_timed_mutex |
| :----- | ----- | --------------- | ----------- | --------------------- | ------------------ |
| m.lock | yes   |	yes        |	yes	 |	yes		 |	yes	      |
| m.unlock|yes	 |	yes	   |	yes	 |	yes		 |	yes 	      |
| m.try_lock |yes|	yes	   |	yes	 |	yes		 |	yes	      |
| m.try_lock_for|no|	no	   |	yes	 |	yes		 |	yes	      |
| m.try_lock_until|no|	no	   |	yes	 |	yes	         |	yes	      |
|m.try_lock_shared|yes|	no	   |	no	 |	no		 |	yes	      |
|m.try_lock_shared_for|no|no	   |	no	 |	no		 |	yes	      |
|m.try_lock_shared_until|no|no	   |	no	 |	no	 	 |	yes	      |


# Issues of Mutexes: Avoiding Exceptions

### Exceptions and Unknown Behavior

The small code snippet has a lot of issues to look at, including a few exceptions and unknown behaviors in the program:

```c++
std::mutex m;
m.lock();
sharedVariable = getVar();
m.unlock();
```

### Issues & Best practices

1. If the function getVar() throws an exception, the mutex m will not be released.

2. Never ever call an unknown function while holding a lock. If the function getVar tries to lock the mutex m, the program has undefined behavior because m is not a recursive mutex. Most of the time, the undefined behavior will result in a deadlock.

3. Avoid calling a function while holding a lock. Maybe the function is from a library and you get a new version of the library, or the function is rewritten, but there is always the danger of a deadlock.

# Types of Locks: std::unique_lock

### Features

* create it without an associated mutex.

* create it without locking the associated mutex.

* explicitly and repeatedly set or release the lock of the associated mutex.
move the mutex.

* try to lock the mutex.

* delay the lock on the associated mutex.

### Methods

| Method	| Description |
| :------------ | ----------: |
| lk.lock()	|Locks the associated mutex.|
| std::lock(lk1, lk2, ... ) | Locks atomically the arbitrary number of associated mutexes. |
| lk.try_lock() and lk.try_lock_for(relTime) and lk.try_lock_until(absTime) | Tries to lock the associated mutex. |
| lk.release() | Release the mutex. The mutex remains locked. |
| lk.swap(lk2) and std::swap(lk, lk2) | Swaps the locks. |
| lk.mutex() | Returns a pointer to the associated mutex. | 
| lk.owns_lock() |	Checks if the lock has a mutex. |





