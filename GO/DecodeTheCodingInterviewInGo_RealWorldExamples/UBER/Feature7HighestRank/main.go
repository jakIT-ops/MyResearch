package main
import (
    "fmt"
    "container/heap"
)

func newHeap() *MinHeap {
    min := &MinHeap{}
    heap.Init(min)
    return min
}

func kthHighestRank(ranks []int, k int) int{
    
    minHeap := newHeap()
    // Put first k ranks in the min heap
    for i := 0; i < k; i++ {
      heap.Push(minHeap, ranks[i])
    }

    // Go through the remaining ranks of the array, if the rank from the array is greater than the
    // top (smallest) rank of the heap, remove the top rank from heap and add the rank from array
    for i := k; i < len(ranks); i++ {
        if ranks[i] > minHeap.Top() {
            heap.Pop(minHeap)
            heap.Push(minHeap, ranks[i])
        }
    }

    // The root of the heap has the Kth largest rank
    return minHeap.Top()
}


func main() {
    // Driver code

    driverID := []int{1, 5, 12, 2, 11, 9, 7, 30, 20}
    k := 3 // Supplied by a hidden API

    fmt.Printf("Driver with the rank %v is selected!\n", kthHighestRank(driverID, k)) 
}
