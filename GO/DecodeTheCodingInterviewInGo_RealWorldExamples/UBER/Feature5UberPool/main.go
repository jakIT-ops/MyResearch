package main
import (
    "fmt"
    "math/rand"
    "time"
)

type Uber struct{
    cumSums []int
}

func newUber(metrics []int) Uber{
    cumSum := 0
    uber := Uber{}
    for i := 0; i < len(metrics); i++ {
        cumSum += metrics[i]
        uber.cumSums = append(uber.cumSums, cumSum)
    }
    return uber
}

func (u Uber) PickRoute() int {
    random := rand.Float64()
    sum := float64(u.cumSums[len(u.cumSums) - 1])
    target := random * sum

    // Binary search to find the target
    low, high := 0, len(u.cumSums)
    for low < high {
        mid := low + (high - low) / 2
        if target > float64(u.cumSums[mid]) {
            low = mid + 1
        } else {
            high = mid
        }
    }
    return low
}

func main() {
    // Driver code
    metrics := []int{1, 2, 3}
    rand.Seed(time.Now().UTC().UnixNano())
    uber := newUber(metrics)
    
    for i := 0; i < 10; i++ {
        fmt.Println("Randomly choose route ", uber.PickRoute())
    }
}
