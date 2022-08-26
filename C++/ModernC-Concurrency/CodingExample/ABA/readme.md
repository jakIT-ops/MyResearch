# ABA

ABA means you read a value twice and it returns the same value A each time. Therefore, you conclude that nothing changed in between, but you missed the fact that the value was updated to B somewhere in between.


### An Analogy

The scenario consists of you sitting in a car and waiting for the traffic light to become green. Green stands for B in our case, and red stands for A. What’s happening?

1. You look at the traffic light and it is red (A).

2. Because you are bored, you begin to check the news on your smartphone and forget the time.

3. You look once more at the traffic light. Damn, it is still red (A).

Of course, the traffic light became green (B) between your two checks. Therefore, what seems to be one red phase was actually a full cycle.

What does this mean for threads (processes)? Here is a more formal explanation:

1. Thread 1 reads the variable var with value A.

2. Thread 1 is preempted and thread 2 runs.

3. Thread 2 changes the variable var from A to B to A.

4. Thread 1 continues to run and checks the value of variable var and gets A. Because of the value A, thread 1 proceeds.


Here are the first two nodes of the stack:

```c++
Stack: TOP -> head -> headNext -> ...
```

### ABA in Action#

Let’s start with the following stack:

```c++
Stack: TOP -> A -> B -> C
```

Thread 1 is active and wants to pop the head of the stack.

* Thread 1 stores

```c++
    head = A
    headNext = B
```

Before thread 1 finishes the pop step, thread 2 kicks in.

* Thread 2 pops A

```c++
    Stack: TOP -> B -> C
```

* Thread 2 pops B and deletes B

```c++
    Stack: TOP -> C
```

* Thread 2 Pushed A back

```c++
    Stack: TOP -> A -> C
```




































