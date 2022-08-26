# 1. Concurrency vs. Parallelism

> Concurrency is about dealing with lots of things at once. <br> Parallelism is about doing lots of things at once.

### What's Parallelism

Parallelism is when we break up a task into subtasks and execute them simultaneously. Each of the subtasks is independent and may or may not be related. In short, we carry out many computations at the same time in parallelism.

> Concurrency is about structure. <br> Parallelism is about execution.

<div align="center">
  <br>
    <img src="img\concurrency_parallelism.JPG">
  <br>
</div>

### Data Races and Race Conditions

> A data race happens when processes have to access the same variable concur­rently i.e. one process reads from a memory location while another simultaneously writes to the exact same memory location.

<p>The following function is an example of a data race: </p>

```go
package main
import "fmt"

func main() {
  number := 0;

  go func(){
    number++ // reading and modifying the value of 'number'
  }()

  fmt.Println(number) // reading the value of 'number'
  // 0
```

<br>
<div align="center">
  <img src="img\data_race.JPG">
  <br>
  <code>Data Race Explained</code>
</div>
<br>

> A race condition is a flaw in a program regarding the timing/ordering of operations which disrupts the logic of the program and leads to erroneous results.

<p>Let's try to understand it using an example: </p>

```go
package main
import "fmt"

func deposit(balance *int,amount int){
    *balance += amount //add amount to balance
}

func withdraw(balance *int, amount int){
    *balance -= amount //subtract amount from balance
}

func main() {

    balance := 100

    go deposit(&balance,10) //depositing 10

    withdraw(&balance, 50) //withdrawing 50

    fmt.Println(balance)
    // 50
}
```

<br>
<div align="center">
  <img src="img\race_condition.JPG">
  <br>
  <code>Race Condition Explained</code>
</div>
<br>

## Deadlocks

> A deadlock occurs when all processes are blocked while waiting for each other and the program cannot proceed further.

Here is an example of how Go detects deadlocks:

```go
package main
import "fmt"

func main() {
  mychannel := make(chan int)
  mychannel <- 10
  fmt.Println(<-mychannel)
  // error
}
```

```go
package main
import "fmt"

func main() {
	mychannel := make(chan int)
	go func(){
		mychannel <- 10
	}()
	fmt.Println(<-mychannel)
  // 10
}
```

# 2. Building Blocks of Concurrency in Go

> A goroutine is a function or a method which is executed concurrently with the rest of the program

> A channel is a pipe between goroutines to synchronize execution and communicate by sending/receiving data.

<br>
<div align="center">
  <img src="img\sending.JPG">
  <br>
  <code>Sending Data To A Channel</code>
</div>
<br>

<br>
<div align="center">
  <img src="img\receiving.JPG">
  <br>
  <code>Receiving Data From A Channel</code>
</div>
<br>

```go
package main
import "fmt"
func sendValues(myIntChannel chan int){

  for i:=0; i<5; i++ {
    myIntChannel <- i //sending value
  }

}

func main() {
  myIntChannel := make(chan int)

  go sendValues(myIntChannel)

  for i:=0; i<5; i++ {
    fmt.Println(<-myIntChannel) //receiving value
  }
}
```

<br>
<div align="center">
  <img src="img\closing.JPG">
  <br>
  <code>Closing A Channel</code>
</div>
<br>

## Exercise: Merge Sort

<p>In this exercise, you are required to write a concurrent solution to the Merge Sort problem using <code>goroutines</code> and <code>channels</code>.</p>

### [Solution](Problems\01MergeSort\mergesort_concurreny.go)

## Select Statement

> The select statement blocks the code and waits for multiple channel operations simultaneously

## Exercise: Buzz Game

[Solution](Problems\02BuzzGame\buzzgame_concurrency.go)

> A WaitGroup blocks a program and waits for a set of goroutines to finish before moving to the next steps of execution

## Exercise: Multiplication Table

<br>
<div align="center">
  <img src="img\multiplication_table.JPG">
  <br>
  <code>Multiplication Table</code>
</div>
<br>

[Solution](Problems\03MultiplicationTable\multtable_concurrency.go)

## Mutex

> A mutex, or a mutual exclusion prevents other processes from entering a critical section of data while a process occupies it.

```go
package main
import ( "fmt"
        "sync")

func deposit(balance *int,amount int, myMutex *sync.Mutex, myWaitGroup *sync.WaitGroup){
    myMutex.Lock()
    *balance += amount //add amount to balance
    myMutex.Unlock()
    myWaitGroup.Done()
}

func withdraw(balance *int, amount int, myMutex *sync.Mutex, myWaitGroup *sync.WaitGroup){
    myMutex.Lock()
    *balance -= amount //subtract amount from balance
    myMutex.Unlock()
    myWaitGroup.Done()
}

func main() {

    balance := 100
    var myWaitGroup sync.WaitGroup
    var myMutex sync.Mutex

    myWaitGroup.Add(2)
    go deposit(&balance,10, &myMutex, &myWaitGroup) //depositing 10
    withdraw(&balance, 50,&myMutex, &myWaitGroup) //withdrawing 50

    myWaitGroup.Wait()
    fmt.Println(balance)
    // 60
}
```

## Prefix Sum Problem: A Concurrent Approach

The Prefix Sum of an array <coode>arr</code> of length n is another array <code>prefixSum_arr</code> of the same length such that the value of the <code>i</code>th index in <code>prefixSum_arr</code> is the sum of all values from <code>arr[0], arr[1]...arr[i]</code>.

<br>
<div align="center">
  <img src="img\prefix_sum.JPG">
  <br>
  <code>Prefix Sum</code>
</div>
<br>

[Solution](Problems\04Prefix_Sum\prefix_sum_concurrency.go)

## Exercise: Sum of Squares

<br>
<div align="center">
  <img src="img\sum_of_squares.JPG">
  <br>
  <code>Sum Of Squares</code>
</div>
<br>

[Solution](Problems\05Sum_of_Squares\sum_of_squares.concurrency.go)
