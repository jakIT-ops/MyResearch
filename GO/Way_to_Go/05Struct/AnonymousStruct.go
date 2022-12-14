package main

import "fmt"

type C struct {
	x      float32
	int    // int type anonymous field
	string // string type anonymous field
}

func main() {
	c := C{3.14, 7, "hello"}          // making struct via literal expression
	fmt.Println(c.x, c.int, c.string) // out: 3.14 7 hello
	fmt.Println(c)                    // out: {3.14, 7 hello}
}
