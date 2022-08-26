package main
import (
  "fmt"
  "sort"
  "container/heap"
)

func minMeetingRooms(meetingTimes [][]int) int {
        
  if(len(meetingTimes) == 0){
      return 0
  }

  sort.Slice(meetingTimes, func(i, j int) bool {
      return meetingTimes[i][0] < meetingTimes[j][0] 
  })       
  //min Heap keeps track of earliest ending meeting:
  minHeap := &MinHeap{}
  heap.Init(minHeap)
  heap.Push(minHeap, meetingTimes[0][1])
  
  for i := 1; i < len(meetingTimes); i++ {
      currStart := meetingTimes[i][0];
      currEnding := meetingTimes[i][1];
      earliestEnding := minHeap.Top();
      
      if earliestEnding <= currStart {
          heap.Pop(minHeap);
      } 
      //update heap with curr ending
      heap.Push(minHeap, currEnding)
  }
  return minHeap.Len()
}


func main() {
    meetingTimes := [][]int{{2, 8}, {3, 4}, {3, 9}, {5, 11}, {8, 20}, {11, 15}}
    fmt.Println(minMeetingRooms(meetingTimes))
}
