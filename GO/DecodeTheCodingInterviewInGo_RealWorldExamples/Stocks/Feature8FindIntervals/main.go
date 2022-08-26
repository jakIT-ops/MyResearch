package main
import (
  "fmt"
  "strconv"
)

func FindIntervals(Prices []int) []int {
  // number of predicted Prices in the time window
  n := len(Prices)
  intervals := make([]int, n)
  // initialize a stack to store the indices of the intervals
  stack := []int{} 
  // iterate over the Prices 
  for currInter := 0; currInter < n; currInter++ {
    // current intervals predicted price
    currentPrice := Prices[currInter]
    // check if the stack is empty or not and also 
    // check if the price at current interval is higher than 
    // the interval's price at top of the stack
    for len(stack) > 0 && Prices[stack[len(stack) - 1]] < currentPrice {
      prevInter := stack[len(stack) - 1]
      stack = stack[:len(stack) - 1]
      intervals[prevInter] = currInter - prevInter;
    }
    // Append the current index onto the stack
    stack = append(stack, currInter);
  }  
  return intervals;
}

func main() {
  // Driver code
  Prices := []int{68,71,78,67,66,69,79,68};
  intervals := FindIntervals(Prices)
  fmt.Print("Minimum Intervals: [")
  for i := 0; i < len(Prices); i++ {
    fmt.Print(strconv.Itoa(intervals[i]) + ",");
  }
  fmt.Print(strconv.Itoa(intervals[len(Prices)-1]) + "]")
}
