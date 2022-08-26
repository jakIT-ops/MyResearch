package main
import (
    "fmt"
    "math"
)

func MinPathSum(grid [][]int) int{
    i := len(grid) - 1
    j := len(grid[0]) - 1

    for k := 0; k <= i; k++ {
        for l := 0; l <= j; l++ {
            if k > 0 && l > 0 {
                grid[k][l] = int(math.Min(float64(grid[k][l] + grid[k][l - 1]), float64(grid[k - 1][l] + grid[k][l])))
            } else if k > 0 || l > 0 {
                if l > 0 {
                    grid[k][l] += grid[k][l - 1]
                } else {
                    grid[k][l] += grid[k - 1][l]
                }
            }   
        }
    }
    return grid[i][j]
}

func main() {
// Driver code
    grid := [][]int{{5,1,9,11},{11,4,8,10},{13,3,6,7},{5,14,12,4}}

    fmt.Println(MinPathSum(grid))
}
