package main
import (
  "fmt"
  "sort"
  "math"
)


func mergeMeetings(meetingTimes [][]int) [][]int{
    var merged [][]int
    sort.Slice(meetingTimes, func(i, j int) bool {
        return meetingTimes[i][0] < meetingTimes[j][0] 
    })    
    for _, meeting := range meetingTimes {
        size := len(merged)
        if size == 0 || merged[size - 1][1] < meeting[0] {
            merged = append(merged, meeting)
        } else{
            merged[size - 1][1] = int(math.Max(float64(merged[size - 1][1]), float64(meeting[1])))
        }
    }
    return merged
}


func main() {
    meetingTimes1 := [][]int{{1, 4}, {2, 5}, {6, 8}, {7, 9}, {10, 13}}

    // First set of meetings
    print(mergeMeetings(meetingTimes1))


    // Second set of meetings
    meetingTimes2 := [][]int{{4, 7}, {1, 3}, {8, 10}, {2, 3}, {6, 8}}
    print(mergeMeetings(meetingTimes2))
}
