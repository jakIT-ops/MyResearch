package main
import (
  "fmt"
  "container/heap"
)

func reorganizeResults(initialOrder string) string{
    
    freqMap := make(map[rune]int)
    for _, c := range initialOrder {
        freq := 1
        if _, ok := freqMap[c]; ok{
            freq = freqMap[c] + 1
        }
        if freq > (len(initialOrder) + 1) / 2 {
            return initialOrder
        }
        freqMap[c] = freq
    }
    
    pq := &MaxHeap{}
    heap.Init(pq)
    for i, _ := range freqMap {
        heap.Push(pq, []int{int(i), freqMap[i]})
    }
    
    result := ""
    for !pq.Empty() {
        first := pq.Top()
        heap.Pop(pq)
        if len(result) == 0 || first[0] != int(result[len(result) - 1]) {
            result = result + string(first[0])
            first[1]--
            if first[1] > 0 {
                heap.Push(pq, first)
            }
        } else {
            second := pq.Top()
            heap.Pop(pq)
            result = result + string(second[0])
            second[1]--;
            if (second[1] > 0) {

                heap.Push(pq, second)
            }

            heap.Push(pq, first)
        }
    }
    return result
}

func main() {
    initialOrder := "bbbnnc"
    fmt.Println(reorganizeResults(initialOrder))
}
