package main
import (
  "fmt"
  "sort"
  "math"
)

func leastTime(stocks []byte, sTime int) int {
    // frequencies of the stocks
    frequencies := make([]int, 26)
    for _, s := range stocks {
        frequencies[int(s - 'A')]++
    }
    
    sort.Ints(frequencies)

    // max frequency
    fMax := frequencies[25]
    idleIntervals := (fMax - 1) * sTime
    
    for i := len(frequencies) - 2; i >= 0 && idleIntervals > 0; i-- {
        idleIntervals -= int(math.Min(float64(fMax - 1), float64(frequencies[i]))) 
    }
    
    if idleIntervals > 0 {
        return idleIntervals + len(stocks)
    } else {
        return len(stocks)
    }
}


func main() {
    // Driver code
    transaction := []byte{'A', 'A', 'A', 'T', 'T', 'M', 'A'}
    k := 2
    fmt.Printf("Time requires to trade all stocks: %v intervals\n", leastTime(transaction, k)) 
}
