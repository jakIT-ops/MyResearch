package main
import (
    "fmt"
    "container/heap"
)
type Location struct{
    x, y int
}

func (l Location) distFromOrigin() int {
    return (l.x * l.x) + (l.y * l.y)
}

func newHeap() *MaxHeap {
    max := &MaxHeap{}
    heap.Init(max)
    return max
}

func findClosestDrivers(locations []Location, k int) []Location{
    maxHeap := newHeap()
    var res []Location
    // put first 'k' locations in the max heap
    for i := 0; i < k; i++{
        heap.Push(maxHeap, locations[i])
    }

    // go through the remaining locations of the input array, if a Location is closer to the origin than the top Location 
    // of the max-heap, remove the top Location from heap and add the Location from the input array
    for i := k; i < len(locations); i++ {
        top := maxHeap.Top()
        if locations[i].distFromOrigin() < top.distFromOrigin() {
            maxHeap.Pop();
            heap.Push(maxHeap, locations[i])
        }
    }

    // the heap has 'k' locations closest to the origin, return them in a list
    for !maxHeap.Empty() {
      res = append(res, maxHeap.Top())
      heap.Pop(maxHeap)
    }
    return res
}

func main() {
    // Driver Code
    locations := []Location{ Location{1, 3}, Location{3, 4}, Location{2, -1} }
    result := findClosestDrivers(locations, 2);
    fmt.Printf("Here are the k drivers locations closest to the user in the Seattle area: ")
    for _, p := range result {
        fmt.Printf("[%v, %v] ", p.x, p.y)
    }
}
