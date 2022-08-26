package main
import (
    "fmt"
    "container/heap"
)
type Pair struct {
    first, second int
}


func newHeap() *MinHeap {
    min := &MinHeap{}
    heap.Init(min)
    return min
}

func topBrokers(brokerIDs []int, k int) []int{
  // find the frequency of each number
    numFrequencyMap := make(map[int]int)
    for _, n := range brokerIDs{
        numFrequencyMap[n] = numFrequencyMap[n] + 1
    }

    minHeap := newHeap()
    // go through all numbers of the numFrequencyMap and push them in the minHeap, which will have 
    // top k frequent numbers. If the heap size is more than k, we remove the smallest (top) number 
    for first, second := range numFrequencyMap {
        heap.Push(minHeap, Pair{first, second})
        if minHeap.Len() > k {
            heap.Pop(minHeap)
        }
    }
    // create a list of top k numbers
    var topNumbers []int

    for !minHeap.Empty() {
        pair := minHeap.Top()
        heap.Pop(minHeap);
        topNumbers = append(topNumbers, pair.first)
    }
    return topNumbers
}

func main() {
    // Driver code
    print(topBrokers([]int{ 1, 3, 5, 12, 11, 12, 11, 12, 5 }, 3))
}
