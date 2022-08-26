package main
import (
  "fmt"
  "math"
)

func FindMinimumServers(workload []int, demand int) int{
  if demand < 1 {
    return 0
  }
  d := make([]int, demand)
  return CalculateMinimumServers(workload, demand, d)
}

func CalculateMinimumServers(workload []int, rem int, counter []int) int{
  if rem < 0 {
    return -1
  }
  if rem == 0 {
    return 0
  } 
  if counter[rem - 1] != 0 {
    return counter[rem - 1]
  }

  minimum := math.MaxInt64

  for _, server := range workload {
    result := CalculateMinimumServers(workload, rem - server, counter)
    if result >= 0 && result < minimum {
      minimum = 1 + result
    }
  }

  if minimum != math.MaxInt64 {
    counter[rem - 1] =  minimum 
  } else{
    counter[rem - 1] = -1
  }

  return counter[rem - 1]
}

func main() {
  // Driver code
  
  capacities := []int{2,3,4}
  demand := 8

  fmt.Println(FindMinimumServers(capacities, demand))
}
