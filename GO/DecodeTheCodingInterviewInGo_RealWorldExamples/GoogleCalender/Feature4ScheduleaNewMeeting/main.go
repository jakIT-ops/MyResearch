package main
import (
  "fmt"
  "sort"
  "math"
)

func insertMeeting(meetingTimes [][]int, newMeeting []int) [][]int{
    var output [][]int
    sort.Slice(meetingTimes, func(i, j int) bool {
        return meetingTimes[i][0] < meetingTimes[j][0] 
    }) 
    i := 0
    n := len(meetingTimes)
    for i < n && newMeeting[0] > meetingTimes[i][0]{
        output = append(output, meetingTimes[i])
        i++
    }
    size := len(output);
    if size == 0 || output[size - 1][1] < newMeeting[0] {
        output = append(output, newMeeting)
    } else{
        output[size - 1][1] = int(math.Max(float64(output[size - 1][1]), float64(newMeeting[1])))
    }
    
    for i < n {
        size = len(output)
        if output[size - 1][1] < meetingTimes[i][0] {
            output = append(output, meetingTimes[i])
        } else{
            output[size - 1][1] = int(math.Max(float64(output[size - 1][1]), float64(meetingTimes[i][1])))
        }
        i++
    }
    return output
}


func main() {
    meetingTimes := [][]int{{1, 3}, {4, 6}, {8, 10}, {10, 12}, {13, 15}, {16, 18}}
    newMeeting := []int{9, 13}
    
    print(insertMeeting(meetingTimes, newMeeting))

    meetingTimes = [][]int{{1, 3}, {4, 6}, {8, 10}, {10, 12}, {13, 15}, {16, 18}}
    newMeeting2 := []int{19, 20}    

    print(insertMeeting(meetingTimes, newMeeting2))
}
