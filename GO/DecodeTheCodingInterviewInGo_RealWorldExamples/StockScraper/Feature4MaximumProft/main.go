package main
import (
  "fmt"
)

func maxProfit(A []int) int {
    if len(A) < 1 {
        return 0
    }

    currMax := A[0]
    globalMax := A[0]
    for i := 1; i < len(A); i++ {
        if currMax < 0 {
            currMax = A[i]
        } else {
            currMax += A[i]
        }

        if globalMax < currMax {
            globalMax = currMax
        }
    }

    return globalMax
  }

func main() {
    // Driver code
    stocks := []int{-4, 2, -5, 1, 2, 3, 6, -5, 1}
    fmt.Printf("Maximum Profit: %v\n", maxProfit(stocks))

    stocks = []int{1, 2, 15, 10, 20, 7, 16, 5, 9}
    fmt.Printf("Maximum Profit: %v\n", maxProfit(stocks))

    stocks = []int{-42, -12, -52, -1, -7, -2, -18, -92, -210}
    fmt.Printf("Maximum Profit: %v\n", maxProfit(stocks))
}
