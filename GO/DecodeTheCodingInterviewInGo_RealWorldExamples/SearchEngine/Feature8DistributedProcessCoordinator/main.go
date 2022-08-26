package main
import (
  "fmt"
  "math"
)

type Snapshot struct {
  snapshotId int
  nodeState map[int]map[int]int
  nCount int
}


func Constructor(length int) Snapshot {
    s := Snapshot{}
    s.snapshotId = 0
    s.nodeState = make(map[int]map[int]int)
    s.nodeState[0] = make(map[int]int)
    s.nCount = length
    return s
}

func (s *Snapshot) SetState (idx int, val int)  {
    if idx < s.nCount {
      s.nodeState[s.snapshotId][idx] = val 
    }
}


func (s *Snapshot) Snap() int {
    s.snapshotId += 1
    temp := make(map[int]int)
    for key, value := range s.nodeState[s.snapshotId - 1]{
      temp[key] = value
    }
    s.nodeState[s.snapshotId] = temp
    return s.snapshotId - 1
}

func (s *Snapshot) FetchState(idx int, snapshotId int) int {
    if snapshotId < s.snapshotId && snapshotId >= 0{
      if _, ok := s.nodeState[snapshotId][idx]; ok {
        return s.nodeState[snapshotId][idx]
      } else{
        return 0
      }
    } else{
      return math.MinInt64
    }
}

func main(){
  fmt.Println("-----Example 1:-----")
fmt.Println()
snapshotArr := Constructor(5) 
fmt.Println("Initializing the data structure with three nodes") 
fmt.Println("Setting the state of node 0 to 5") 
snapshotArr.SetState(0,5)  
fmt.Println("Snap id:",snapshotArr.Snap())  
snapshotArr.SetState(0,1)
fmt.Println("Setting the state of node 0 to 1") 
snapshotArr.SetState(2,3)
fmt.Println("Setting the state of node 2 to 3") 
snapshotArr.SetState(1,10)
fmt.Println("Setting the state of node 1 to 10") 
fmt.Println("Node state at index 0 with Snap id 0 is:", snapshotArr.FetchState(0,0))
fmt.Println("Snap id:",snapshotArr.Snap())
fmt.Println("Node state at index 0 with Snap id 1 is:",snapshotArr.FetchState(0,1))
fmt.Println("Node state at index 1 with Snap id 1 is:",snapshotArr.FetchState(1,1))

fmt.Println()

fmt.Println("-----Example 2:-----")
snapshotArr2 := Constructor(5) 
fmt.Println("Initializing the data structure with five nodes") 
fmt.Println("Setting the state of node 4 to 1") 
snapshotArr2.SetState(4,1)  
fmt.Println("Snap id:",snapshotArr2.Snap())  
fmt.Println("Setting the state of node 2 to 21") 
snapshotArr2.SetState(2,21)
fmt.Println("Snap id:",snapshotArr2.Snap())
fmt.Println("Node state at index 4 with Snap id 1 is::", snapshotArr2.FetchState(4,1))
fmt.Println("Node state at index 2 with Snap id 1 is::",snapshotArr2.FetchState(2,1))
fmt.Println("Node state at index 3 with Snap id 1 is::",snapshotArr2.FetchState(3,1))
}
