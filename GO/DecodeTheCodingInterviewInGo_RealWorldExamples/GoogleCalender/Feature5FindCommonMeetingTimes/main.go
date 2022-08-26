package main
import (
  "fmt"
  "math"
)
func meetingsIntersection(meetingsA [][]int, meetingsB [][]int) [][]int{
    i := 0
    j := 0
    var intersection [][]int
    for i < len(meetingsA) && j < len(meetingsB) {
        start := int(math.Max(float64(meetingsA[i][0]), float64(meetingsB[j][0])))
        end := int(math.Min(float64(meetingsA[i][1]), float64(meetingsB[j][1])))
        if start < end {
            intersection = append(intersection, []int{start, end})
        } 
        if (meetingsA[i][1] < meetingsB[j][1]){
            i++
        } else {
            j++
        }
    }
    return intersection
}

func main() {
    meetingsA := [][]int{{1, 3}, {5, 6}, {7, 9}}
    meetingsB := [][]int{{2, 3}, {5, 7}}
    print(meetingsIntersection(meetingsA, meetingsB))


    meetingsC := [][]int{{1, 4}, {6, 9}, {10, 12}}
    meetingsD := [][]int{{4, 6}, {9, 10}}
    print(meetingsIntersection(meetingsC, meetingsD))
}
