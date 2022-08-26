# Double-Checked Locking Pattern

The double-checked locking pattern is the classic way to initialize a singleton in a thread-safe way. What sounds like established best practice - or a pattern - is more a kind of an anti-pattern. It assumes guarantees in the classical implementation, which aren’t given by the Java, C#, or C++ memory model. The wrong assumption is that the creation of a singleton is an atomic operation; therefore, a solution that seems to be thread-safe is not thread-safe.

What is the double-checked locking pattern? The first idea for implementing a thread-safe singleton is to protect the initialization of the singleton with a lock.

```c++
#include <iostream>
#include <mutex>
#include <thread>

std::mutex myMutex;

class MySingleton{
public:  
  static MySingleton* getInstance(){    
    std::lock_guard<std::mutex> myLock(myMutex);      
    if(!instance) instance = new MySingleton();    
    return instance;  
  }
private:  
  MySingleton() = default; 
  ~MySingleton() = default;
  MySingleton(const MySingleton&) = delete;  
  MySingleton& operator= (const MySingleton&) = delete;
  static MySingleton* instance;
};

MySingleton* MySingleton::instance = nullptr;

int main(){

  std::cout << std::endl;

  std::cout << "MySingleton::getInstance(): "<< MySingleton::getInstance() << std::endl;
  std::cout << "MySingleton::getInstance(): "<< MySingleton::getInstance() << std::endl;

  std::cout << std::endl;

}
```

Any issues? Yes and no. Yes, because there is a large performance penalty; No, because the implementation is thread-safe. Each access to the singleton in line 7 is protected by a heavyweight lock. This also applies to the read access, which is not necessary after the initial construction of MySingleton. With that, here comes the double-checked locking pattern to our rescue. Let’s have a look at the getInstance function.

```c++
static MySingleton& getInstance(){    
  if (!instance){                                   // check
    lock_guard<mutex> myLock(myMutex);              // lock
    if(!instance) instance = new MySingleton();     // check
  } 
  return *instance; 
}
```

# Performance Measurement

I want to measure how expensive it is to access a singleton object. For reference timing, I will use a singleton which I will access 40 million times sequentially. Of course, the first access will initialize the singleton object. In contrast, the accesses from four threads will be done concurrently. I’m only interested in the performance numbers; therefore, I will sum up the execution time of the four threads. I will measure the performance using a static variable with block scope (Meyers Singleton), a lock std::lock_guard, the function std::call_once in combination with the std::once_flag, and atomics with sequential consistency and acquire release semantic.


# Conclusion

The numbers give a clear indication; the Meyers Singleton is the easiest to understand and the fastest one. It’s about two times faster than the atomic versions. As expected, the synchronization with the lock is the most heavyweight and, therefore, the slowest. In particular, std::call_once on Windows is a lot slower than on Linux.

| Operating System (Compiler) |	Single | Threaded | Meyers Singleton | std::lock_guard | std::call_once | Sequential Consistency | Acquire-Release Semantic |
| :-------------------------- | ------ | -------- | ---------------- | --------------- | -------------- | ---------------------- | ------------------------ |
| Linux (GCC) |	0.03 | 0.04 |  12.47 | 0.22 | 0.09 | 0.07 |
| Windows (cl.exe) |0.02 | 0.03 | 15.48 | 1.74	| 0.07 | 0.07 |


I want to stress one point about the numbers explicitly: These are the summed up numbers for all four threads. That means that we get optimal concurrency with the Meyers Singleton because the Meyers Singleton is nearly as fast as the single threaded implementation.


