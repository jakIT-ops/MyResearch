package main
import "fmt"

func milestoneReached(matrix [][]int, milestone int) []int {
    
    failed := []int{-1, -1}

    m := len(matrix)
    if m == 0 {
        return failed
    }
    n := len(matrix[0])

    // binary search
    left, right := 0, m * n - 1
    var middleIdx, middleElement int
    for left <= right {
        middleIdx = (left + right) / 2
        middleElement = matrix[middleIdx / n][middleIdx % n]
        if milestone == middleElement{
            failed = []int{middleIdx / n, middleIdx % n}
            return failed
        } else {
            if milestone < middleElement {
                right = middleIdx - 1
            } else{
                left = middleIdx + 1
            }
        }
    }
    return failed
}

func main() {
    // Driver code

    matrix := [][]int{{0,2,4,6,8}, {10,12,14,18,22},{24,30,34,60,64}}
    milestone := 24
    
    res := milestoneReached(matrix, milestone)
    fmt.Printf("Milestone reached on day %v of week %v", res[1] + 1, res[0] + 1)
}
