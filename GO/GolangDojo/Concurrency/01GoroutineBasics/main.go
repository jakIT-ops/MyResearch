package main

import (
	"fmt"
	"time"
)


func main() {
	start := time.Now()
	defer func() {
		fmt.Println(time.Since(start))
	}()

	evilNinjas := []string{"Tommy", "Johnny", "Bobby", "Andy"}

	for _, evilNinja := range evilNinjas {
		go attack(evilNinja)
	}

}

func attack(target string) {
	fmt.Println("Throwing ninja stars at", target)
	time.Sleep(time.Second)
}
/*
out:

Throwing ninja stars at Tommy
Throwing ninja stars at Bobby
Throwing ninja stars at Johnny
53.56µs
*/
