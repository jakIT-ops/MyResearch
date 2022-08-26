package main
import (
  "fmt"
  "math"
)

func twoSetsOfDays(hoursPerDay []int, k int) int {
    hmap := make(map[int]int)
    sum := 0
    lsize := math.MaxInt64
    result := math.MaxInt64
    hmap[0] = -1
    for i := 0; i < len(hoursPerDay); i++ {
        sum += hoursPerDay[i]
        hmap[sum] = i
    }
    sum = 0
    for i := 0; i < len(hoursPerDay); i++ {
        sum += hoursPerDay[i]
        if val, ok := hmap[sum - k]; ok {
            // stores minimum length of sub-array ending with index<= i with sum k. This ensures non- overlapping property.
            lsize = int(math.Min(float64(lsize), float64( i - val))) 
        }
        //searches for any sub-array starting with index i+1 with sum k.
        if val, ok := hmap[sum + k]; ok && lsize < math.MaxInt64 {
            // updates the result only if both left and right sub-array exists.
            result = int(math.Min(float64(result), float64(val - i + lsize))) 
        }
    }

    if result == math.MaxInt64 {
        return -1
    } else {
        return result
    }
}


func main() {
    hoursPerDay := []int{1, 2, 2, 3, 2, 6, 7, 2, 1, 4, 8}
    k := 5
    fmt.Println(twoSetsOfDays(hoursPerDay, k))
}
