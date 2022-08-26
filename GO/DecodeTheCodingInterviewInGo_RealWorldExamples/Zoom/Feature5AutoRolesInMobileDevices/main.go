package main
import (
  "fmt"
)

func autoRotate(matrix [][]int) [][]int{
  left := 0
  right := len(matrix) - 1
  for left < right {
    // `right - left` moves our square in by 1 each outer iteration
    // the index is used to rotate the coordinates 
    for i := 0; i < right - left; i++ {
      top := left
      bottom := right
      topLeft := matrix[top][left + i]
      // move bottomLeft to topLeft
      matrix[top][left +  i] = matrix[bottom - i][left]
      // move bottomRight to bottomLeft
      matrix[bottom - i][left] = matrix[bottom][right - i]
      // move topRight to bottomRight
      matrix[bottom][right - i] = matrix[top + i][right]  
      // set saved to topRight
      matrix[top + i][right] = topLeft
    }
    left++
    right--
  }
  return matrix
}

func main() {
  // Driver code
  matrix := [][]int{
      {5,1,9,11},
      {2,4,8,10},
      {13,3,6,7},
      {15,14,12,16}}

    fmt.Println(autoRotate(matrix))
}
