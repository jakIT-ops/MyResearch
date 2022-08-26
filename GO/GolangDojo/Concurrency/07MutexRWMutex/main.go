package main

import (
	"fmt"
	"rwLock"
	"sync"
	"time"
)

var (
	lock   sync.Mutex
	relock sync.RWMutex
	count  int
)

func main() {
	// basics()
	readAndWrite()
}

func basics() {

	iterations := 1000
	for i := 0; i < iterations; i++ {
		go increment()
	}
	time.Sleep(3 * time.Second)
	fmt.Println("Resulted count is:", count)
}

func increment() {
	lock.Lock()
	count++ // or count = count + 1
	// temp := count
	// temp = temp + 1
	// count = temp
	lock.Unlock()
}

func readAndWrite() {
	go read()
	go write()

	time.Sleep(5 * time.Second)
	fmt.Println("Done")
}

func read() {
	rwLock.RLock()
	defer rwLock.RUnlock()

	fmt.Println("Read locking")
	time.Sleep(1 * time.Second)
	fmt.Println("Reading unlocking")
}

func write() {
	rwLock.Lock()
	defer rwLock.Unlock()

	fmt.Println("Write locking")
	time.Sleep(1 * time.Second)
	fmt.Println("Write unlocking")
}
