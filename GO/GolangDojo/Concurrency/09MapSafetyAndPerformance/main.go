package main

import (
	"fmt"
	"sync"
)

func main() {
	regularMap := make(map[int]interface{})
	syncMap := sync.Map{}

	// put
	regularMap[0] = 0
	regularMap[1] = 1
	regularMap[2] = 2
	syncMap.Store(0, 0)
	syncMap.Store(1, 1)
	syncMap.Store(2, 2)

	// get
	regularValue, regularOk := regularMap[0]
	fmt.Println(regularValue, regularOk)
	syncValue, syncOk := syncMap.Load(0)
	fmt.Println(syncValue, syncOk)
}
