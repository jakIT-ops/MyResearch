# 1. Introduction to Threads

C++ has had a multithreading interface since C++11. This interface has all the basic building blocks for creating multithreaded programs: threads, synchronization primitives for shared data (e.g. mutexes and locks), thread-local data, synchronization mechanism for threads (e.g. condition variables), and tasks. Tasks are usually called promises, and they provide a higher level of abstraction than native threads. It is okay if you do not understand the terms discussed here, as all of them will be discussed in depth in the following lessons.

# Passing Arguments to Threads

A thread, like any arbitrary function, can get its arguments by copy, by move, or by reference. std::thread is a variadic template which means that it takes an arbitrary num​ber of arguments.

In the case where your thread gets its data by reference, you have to be extremely careful about the lifetime of the arguments; not doing so may result in undefined behavior.

### Copy or Reference

```c++
#include<thread>
#include<iostream>

int main(){ 
  std::string s{"C++11"};

  std::thread t1([=]{ std::cout << s << std::endl;});
  t1.join();

  std::thread t2([&]{ std::cout << s << std::endl;});
  t2.detach();
}
```

Thread t1 gets its argument by copy, thread t2 by reference.

# Argumentss of Threads - Race Conditions and Locks 

Both issues from the previous lesson are actually race conditions because the result of the program depends on the interleaving of the operations. The race condition is the cause of the data race.

Fixing the data race is quite easy; valSleeper should be protected using either a lock or an atomic. To overcome the lifetime issues of valSleeper and std::cout, you have to join the thread instead of detaching it.

```c++
#include <chrono>
#include <iostream>
#include <thread>

class Sleeper{
  public:
    Sleeper(int& i_):i{i_}{};
    void operator() (int k){
      for (unsigned int j= 0; j <= 5; ++j){
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        i += k;
      }
      std::cout << std::this_thread::get_id() << std::endl;
    }
  private:
    int& i;
};

int main(){

  std::cout << std::endl;

  int valSleeper= 1000;
  std::thread t(Sleeper(valSleeper),5);
  t.join();
  std::cout << "valSleeper = " << valSleeper << std::endl;

  std::cout << std::endl;

}
// out: 140276103862016
// valSleeper = 1030

```

# Methofs of Threads

Here is the interface of `std::thread t` in a concise table. For additional details, please refer to cppreference.com.


| Method	 | Description |
| :------------- | ----------: |
| t.join()					                        |Waits until thread t has finished its executable unit. |
| t.detach()					                      |Executes the created thread t independently of the creator. |
| t.joinable()					                    |Returns true if thread t is still joinable. |
| t.get_id() and std::this_thread::get_id()	|Returns the identity of the thread. |
| std::thread::hardware_concurrency()	      |Returns the number of cores, or 0 if the runtime can not determine the number. Indicates the number of threads that can be run concurrently. This is according to the C++ standard. |
| std::this_thread::sleep_until(absTime)	  |Puts thread t to sleep until the time point absTime. Needs a time point or a time duration as an argument. |
| std::this_thread::sleep_for(relTime)	    |Puts thread t to sleep for the time duration relTime. Needs a time point or a time duration as an argument. |
| std::this_thread::yield()	                |Enables the system to run another thread. |
| t.swap(t2) and std::swap(t1, t2)	        |Swaps the threads. |
