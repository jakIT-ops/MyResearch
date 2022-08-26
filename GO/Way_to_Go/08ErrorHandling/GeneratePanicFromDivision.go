package main

import (
	"fmt"
)

func badCall() {
	a, b := 10, 0
	n := a / b // it will cause panic as it's a division by 0
	fmt.Println(n)
}

func test() {
	defer func() {
		if e := recover(); e != nil {
			fmt.Printf("Panicking %s\r\n", e)
		}

	}()
	badCall()
	fmt.Printf("After bad call\r\n") // It won't be called, because we just recovered from an error
}

func main() {
	fmt.Printf("Calling test\r\n")
	test() // calling test function
	fmt.Printf("Test completed\r\n")
}
