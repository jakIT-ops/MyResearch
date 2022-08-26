package main
import (
    "fmt"
)

func search(milestones []int, n int) int{
    first := 0
    last := len(milestones)
    for first < last {
        var mid int = (first + last) / 2
        if milestones[mid] >= n {
            last = mid;
        } else {
            first = mid + 1
        }
    }
    return first
}
func milestoneDays(milestones []int, target int) (int, int){
    firstDay := search(milestones, target);
    if target == milestones[firstDay]{
        lastDay := search(milestones, target + 1) - 1
        return firstDay, lastDay
    } else {
        return -1, -1
    }
}

func main() {
    milestones := []int{0, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7}
    target := 4
    first, second := milestoneDays(milestones, target)
    fmt.Printf("[%d, %d]", first, second);
}
 
